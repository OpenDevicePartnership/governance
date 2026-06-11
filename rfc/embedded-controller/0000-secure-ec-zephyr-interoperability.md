# RFC: ODP Secure EC and Zephyr Interoperability

- **RFC PR:** TBD  
- **Author(s):** Jerry Xie
- **Status:** Draft  
- **Created:** 2026-06-08  
- **Tracking Issue:** TBD  

ODP intends to enable Secure EC services to run on Zephyr through a staged interoperability approach. This RFC proposes supporting ODP Rust-based Secure EC services in Zephyr-based environments, providing an incremental adoption path for OEMs already aligned on Zephyr, and collaborating with the Zephyr and Linaro communities on Rust integration gaps. This is **not** a replacement of the Embassy-native ODP architecture. Instead, this is an interoperability and ecosystem expansion effort.

## Change Log

- 2026-06-08: Initial RFC created
- 2026-06-11: Clarified platform support scope, safety caveats, and phasing based on review feedback

## Motivation

ODP partners have indicated:
- Zephyr is a strategic baseline for EC firmware due to ecosystem maturity and hardware support
- A full migration to a Rust-first stack is not immediately feasible
- Incremental adoption of Rust components is preferred

At the same time:
- ODP's Secure EC architecture is centered on memory safety, modular services, and Rust
- Early internal prototypes show that Rust services can run on Zephyr with adapter layers
- Zephyr's Rust support is evolving but incomplete

This creates a clear opportunity:

> Enable ODP Secure EC capabilities in Zephyr environments without requiring a full stack replacement.

## Technology Background

- **Zephyr RTOS:** A widely adopted open-source RTOS written in C, supported by the Linux Foundation and Linaro. It offers broad hardware support, mature tooling, and a growing ecosystem of EC firmware implementations.
- **Zephyr Rust Support:** Zephyr has [official Rust language support](https://docs.zephyrproject.org/latest/develop/languages/rust/index.html) via the [`zephyr-lang-rust`](https://github.com/zephyrproject-rtos/zephyr-lang-rust) optional module. Key characteristics of the current support:
  - Enabled via `CONFIG_RUST` in application configuration
  - Applications are built with Cargo and linked as a static library (`crate-type = ["staticlib"]`)
  - A `zephyr` crate provides thin FFI bindings to Zephyr APIs, though bindings are described as "under development" and "currently rather minimalistic." Safe, ergonomic Rust wrappers around drivers are [largely missing](https://github.com/zephyrproject-rtos/zephyr-lang-rust/issues/73) — application code must currently use `unsafe` calls to the FFI layer directly
  - Devicetree bindings are available via `dt-rust.yaml` with traits augmenting device representations
  - Bool, numeric, and string Kconfig settings are accessible from Rust via `zephyr::kconfig`
  - Only a limited set of platforms are [CI-tested](https://github.com/zephyrproject-rtos/zephyr-lang-rust/blob/main/etc/platforms.txt) (e.g., `qemu_cortex_m0`, `qemu_cortex_m3`, `qemu_riscv32`, `qemu_riscv64`, `m2gl025_miv`, `frdm_mcxa156`, `esp32c3_supermini`, `nrf5340dk`). However, the underlying [Kconfig gate](https://github.com/zephyrproject-rtos/zephyr-lang-rust/blob/main/Kconfig) checks architecture support (`CPU_CORTEX_M`, `RISCV`, `ARCH_POSIX && 64BIT`), meaning any board on a supported architecture can work with appropriate overlay files — as demonstrated by ODP PoCs running on IMXRT
  - Applications must use `no_std` and export a `rust_main` entry point called from C
- **Embassy:** A Rust async runtime for embedded systems used as the foundation of ODP's Secure EC architecture.
- **ODP Secure EC:** A Rust-first modular EC service architecture focused on memory safety, secure boot, and composable firmware services.
- **FFI (Foreign Function Interface):** The mechanism by which Rust code can interoperate with C code, used here to bridge ODP services to Zephyr drivers.

## Goals

1. **Signal Intent Publicly**  
   Clearly communicate ODP's direction to partners and the Zephyr community.

2. **Support Incremental Adoption**  
   Allow OEMs to adopt ODP Secure EC capabilities without platform rewrites.

3. **Improve Rust Integration in Zephyr**  
   Address gaps such as:
   - Devicetree bindings
   - Driver abstractions
   - Async and wakeup behavior
   - Ergonomic Rust APIs

4. **Engage Upstream Ecosystem**  
   Collaborate with Zephyr maintainers and Linaro rather than diverging.

### Non-Goals

This RFC does **not**:

- Replace the Embassy-native ODP architecture
- Guarantee immediate production readiness on Zephyr
- Commit to full Rust driver coverage in the near term
- Require upstream acceptance of all contributions

## Requirements

1. ODP Secure EC services must be executable on Zephyr-based platforms without requiring a full stack replacement.
2. Interoperability layers must preserve memory safety guarantees of the Rust service code. Where a Zephyr subsystem's internal design makes fully safe wrapping impractical, the boundary must be explicitly documented and the unsafe surface minimized.
3. The approach must support incremental adoption — OEMs should not need to migrate all components at once.
4. Integration must work with existing Zephyr drivers via FFI or wrapper layers.
5. The architecture must remain compatible with Embassy-native deployments.

## Unresolved Questions

- Which Secure EC services should be prioritized first?
- What is the upstream contribution strategy (wrapper-first vs driver-first)?
- How should temporary forks or patches be managed?
- What metrics (RAM, flash, performance) should be published?
- What belongs upstream vs ODP-specific?
- Which Zephyr subsystems can be wrapped safely, and which may require accepting a bounded unsafe surface?
- What is the threshold for accepting an interop layer that cannot fully guarantee safety?

## Prior Art

- Zephyr Rust effort (Linaro / community initiative)
- ODP internal PoCs:
  - Rust services running on Zephyr
  - Rust driver experiments via thin abstraction layers
- ODP "Journey to Zephyr" architectural exploration

## Alternatives

### Alternative 1: Stay Embassy-only

- Pros: Clean architecture
- Cons: Limits OEM adoption

### Alternative 2: Rust Drivers Only

- Pros: Incremental and upstream-friendly
- Cons: Does not enable reuse of ODP services; requires changes to the Zephyr kernel itself, which is a harder upstream sell than improving the `zephyr-lang-rust` module (though Linux has set a precedent for accepting Rust drivers while the core kernel remains C)

### Alternative 3: Services on C Drivers Only

- Pros: Fastest path to adoption
- Cons: Does not improve long-term safety or ecosystem

### Alternative 4: Invest in migrating Zephyr itself to Rust

- Pros: Would achieve the strongest long-term safety and ecosystem alignment
- Cons: Very long-term effort with uncertain timeline; effectively forks ODP Secure EC investment into two parallel directions (Embassy-native and Zephyr upstream), diluting engineering focus

The chosen design supports both service-level and driver-level integration paths, balancing OEM adoption with long-term safety and ecosystem alignment.

### Drawbacks

- Increased complexity from hybrid Rust/C systems
- Additional maintenance (wrappers, integration layers)
- Potential confusion about "primary" architecture
- Dependency on evolving upstream Rust support in Zephyr
- Some Zephyr subsystems may be inherently difficult to wrap safely without upstream redesign, potentially requiring bounded unsafe interop layers

## Rust Code Design

### Current State

- ODP Secure EC is tightly coupled to a Rust-first architecture
- Zephyr is C-based with evolving Rust support
- Initial prototypes demonstrate:
  - Rust application logic running on Zephyr
  - Rust interacting with Zephyr drivers via wrappers

### Phase 1: ODP on Zephyr

- Execute ODP Rust services within Zephyr runtime
- Bridge to Zephyr drivers using the existing thin FFI bindings from `zephyr-lang-rust`
- Validate functionality on real hardware platforms

### Phase 1.5: Safe Driver Libraries

- Build safe, ergonomic Rust libraries around the existing thin FFI wrappers provided by `zephyr-lang-rust`
- Eliminate the need for application code to make direct `unsafe` FFI calls to Zephyr drivers
- Prioritize driver abstractions needed by target Secure EC services (e.g., I2C, GPIO, sensor subsystems)
- Contribute safe wrapper libraries upstream where appropriate

### Phase 2: Rust Driver Enablement

- Introduce Rust-native drivers where beneficial
- Improve:
  - Device abstraction layers
  - Devicetree integration
  - FFI tooling and ergonomics
- Note: This phase requires changes closer to the Zephyr kernel, which carries a higher upstream acceptance bar than `zephyr-lang-rust` module improvements

### Long-term Direction

- Portable async Rust services across:
  - Embassy-native environments
  - Zephyr-based environments
- Partners can choose their migration path and pace

## Guide-Level Explanation

ODP will support a **hybrid integration model**:

### Path A — Rust Services on Zephyr

- Run ODP Rust services on top of Zephyr
- Reuse existing Zephyr drivers (C-based initially) through the thin FFI bindings already provided by `zephyr-lang-rust`
- Build safe, ergonomic Rust libraries around these FFI bindings so that application code does not require direct `unsafe` calls

### Path B — Rust Drivers in Zephyr

- Enable Rust-based drivers in Zephyr
- Improve devicetree integration and driver ergonomics
- Reduce reliance on C over time

### Staged Approach

- **Phase 1:** ODP services running on Zephyr via existing thin FFI bindings
- **Phase 1.5:** Safe, ergonomic Rust driver libraries replacing direct unsafe FFI usage
- **Phase 2:** Incremental introduction of Rust-native drivers and deeper kernel integration
- **Long-term:** Portable Rust EC services across Embassy and Zephyr environments
