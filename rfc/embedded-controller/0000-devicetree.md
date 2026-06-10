# RFC: `Use devicetrees for hardware instatiation and configuration`

Instantiating drivers for hardware is currently done by creating the corresponding driver struct and connecting any dependencies manually. This approach can be cumbersome, error prone, and inflexible: taking an existing hardware configuration and making small tweaks often requires complete duplication. Drivers may also require additional variables for internal state or channels to allow for communication between components. This boilerplate is required for drivers to function but is another tedious part of using hardware. This RFC proposes using devicetrees for hardware instantiaton and configuration.

## Change Log

- 2026-01-27: Initial RFC created
- 2026-02-02: RFC migrated to governance repo

## Motivation

* Unified hardware configuration: The same devicetree can be used in multiple different ways. Both async and synchronous code can be supported. Intergation tests can use the same devicetree as real hardware and instiatiate emulators.
* Ergonomics: Abstracts away boilerplate setup code and makes it easier to create, modify, and extend hardware configuration.
* Open ecosystem and familiarity: The devicetree spec is open and devicetrees are already used in system programming applications
* Applicable to more than hardware: Devicetrees can also be used to configure software components and connect application logic to hardware devices

## Technology Background

The Devicetree spec is an open spec (https://www.devicetree.org/specifications/) that defines a data structure intended to describe hardware configurations. A devicetree consists of a tree of nodes and their child nodes. Each node can contain various named values (called properties) used to configure the corresponding hardware. Nodes can also reference other nodes by name, enabling things like using a specific GPIO to use as an interrupt line. There is both a human-readable format (DTS files) and a binary format (DTB, also called a flattened or compiled devicetree). Hardware is matched based on a node's `compatible` property which is a string of the format `<vendor name>,<product name>`. Devicetrees also support overlays, which allow expanding and modifying an existing devicetree. DTBs are widely used by Linux on non-x86, non-PC platforms to define the drivers that the kernel needs to load.

Devicetrees aren't limited to use by general-purpose kernels. The Zephyr RTOS uses devicetrees to define hardware layouts. Instead of loading compiled devicetrees at runtime, Zephyr instead compiles them into C code at build time. These devices can then be accessed through various macros at runtime. There are several pieces that Zephyr uses to achieve this:

* Binding definitions: These are YAML files defining the valid properties and other metadata associating with a given `compatible` string. At build time, the properties in each node are validated against the binding definition.
* Macro-based driver instantiation: a driver uses special macros to define the `compatible` string that it matches, and to define a macro to generate the C instantiation code.
* Macros to get a pointer to a device at runtime

[Example binding YAML excerpt](https://github.com/zephyrproject-rtos/zephyr/blob/a5d4626b8c16550666983f793d8d3789850115fb/dts/bindings/sensor/st%2Clis2dh-i2c.yaml):
```yaml
description: |
    STMicroelectronics LIS2DH 3-axis accelerometer accessed through I2C bus

compatible: "st,lis2dh"
```

[Example devicetree fragment](https://github.com/zephyrproject-rtos/zephyr/blob/a5d4626b8c16550666983f793d8d3789850115fb/boards/ezurio/bt510/bt510.dts)
```
&i2c0 {
	compatible = "nordic,nrf-twim";
	status = "okay";

	pinctrl-0 = <&i2c0_default>;
	pinctrl-1 = <&i2c0_sleep>;
	pinctrl-names = "default", "sleep";

	lis2dh12: lis2dh12@18 {
		compatible = "st,lis2dh12", "st,lis2dh";
		reg = <0x18>;
		irq-gpios = <&gpio1 5 GPIO_ACTIVE_HIGH>,
			    <&gpio1 12 GPIO_ACTIVE_HIGH>;
		disconnect-sdo-sa0-pull-up;
	};

	...
};
```

[Declaring the compatible string in driver code](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/lis2dh_i2c.c)
```
#define DT_DRV_COMPAT st_lis2dh
```

[Example macro to instantiate device configuration in C](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/lis2dh.c)
```
/*
 * Instantiation macros used when a device is on an I2C bus.
 */

#define LIS2DH_CONFIG_I2C(inst)						\
	{								\
		.bus_init = lis2dh_i2c_init,				\
		.bus_cfg = { .i2c = I2C_DT_SPEC_INST_GET(inst), },	\
		.hw = { .is_lsm303agr_dev = IS_LSM303AGR_DEV(inst),	\
			.disc_pull_up = DISC_PULL_UP(inst),		\
			.anym_on_int1 = ANYM_ON_INT1(inst),		\
			.anym_latch = ANYM_LATCH(inst),			\
			.anym_mode = ANYM_MODE(inst), },		\
		LIS2DH_CFG_TEMPERATURE(inst)				\
		LIS2DH_CFG_INT(inst)					\
	}
```

## Unresolved Questions

* Zephyr uses the human-readable DTS but existing Rust crates deal with the compiled DTB. The DTB doesn't contain node labels, which are convenient names for human use like `temp0` instead of a full node path like `/i2c@0/temp@25`. This might require us to maintain our own DTS parser.
* Rust support for YAML isn't the best and crates like `serde_yaml` are deprecated.
* Zephyr uses devicetrees to define peripherals, while this is typically done with a PAC in Rust. References to PAC-defined peripherals can be passed into functions that need them, but there will likely need to be PAC devicetree definitions to glue things together.

### Zephyr Compatibility

A high degree of compatibility with Zephyr is desired to allow re-use of existing devicetrees and binding definitions. However, the differences between C and Rust results in the following limitations:

* Binding definitions need Rust types. Rust's stronger type system and ownership rules end up in types being needed to generate valid code. This should not be a major issue if our binding definitions end up as a superset of Zephyr ones.
* Some Zephyr devices might have a tighter coupling with C code through things like passing the name of its interrupt handler as a string in the devicetree. These would require special care, but complete compatibility may not be possible.

## Rust Code Design

Driver devicetree crates would generate a function for each devicetree node, returning the corresponding driver struct. This provides a minimum standard for generated code to follow while allowing for a high degree of flexibility in other aspects. In particular, this supports both basic let bindings and storing the resulting driver struct in a `static` variable. References to other devices in the devicetree will be passed into the generated function as arguments. Generation configuration options would control how arguments would be passed (move, reference, or clone).

### Code generation by `dt-common`

The only requirement on generated code is the above function structure. What's described here will be the generated code provided by `dt-common`. This is meant to be generally useful but an application can implement its own bespoke generation if required.

The generated code struct is fairly simple and arranged in a hierachal manner to resemble the devicetree itself. Devices with children will have their child devices contained within an ad-hoc struct, e.g. an I2C bus `i2c@0` will have a `BusChildrenI2cAt0` struct, with fields for each device attached to it. There will be a corresponding function which would create all child devices and package them up in a `BusChildrenI2cAt0`. `Devicetree` will be the top-level struct containing all available devices.

### Proof of concept

[dt-poc](https://github.com/RobertZ2011/dt-poc/tree/main) is a proof of concept for this proposal. It consists of the following parts:

* `dt-common` fulling the same purpose as the `dt-common` mentioned above.
* `dt-demo-driver`: driver implementations for the proof of concept
* `dt-demo-devicetree`: Binding definitions and generation code for `dt-demo-driver`
* `dt-demo`: Application that defines a simple device tree consisting of a GPIO pin, an I2C bus, and 3 sensors attached to the bus. All hardware is instantiated using the code generated by `dt-common` and then a value is read from each sensor.

The generated devicetree for `dt-demo` is located in the `devicetree.rs` file. The `instantiate_node_*` functions are generated by the `dt-demo-devicetree` crate. `dt-common` generates the `instantiate_bus_i2c_at_0` which attaches the sensors to I2C bus 0 and returns those children in the `BusChildrenI2CAt0` struct. The top-level `Devicetree` struct contains the `BusChildrenI2CAt0` struct.
