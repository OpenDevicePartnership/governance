# RFC: `Standardize on bytemuck for casting between structs and bytes`

Converting between a series of bytes and a struct is a commonly used feature in embedded development. Usually, the bytes have a specific format and layout dictated by a datasheet or spec. It's possible to do this manually with a combination of [repr(C)], and unsafe code, but it's not very ergonomic. This RFC proposes `bytemuck` as the standard crate to provide this functionality. 

## Change Log

- 2026-01-26: Initial RFC created as issue
- 2026-02-02: RFC migrated to governance repo, favoring `bytemuck` over `zerocopy`

## Motivation

Multiple crates are currently used for this functionality, type-C code, in particular, currently uses `bincode`. However, it's no longer maintained on Github, and wasn't ideal for the task. We want to migrate away and standardize on a new crate. Using a single crate makes code consistent and reduces binary size.

## Requirements

The chosen crate should provide traits to facilitate conversion between a struct and a specific binary layout. The crate should also be endian-aware.

## Alternatives

* `zerocopy` provides very similar features. The benefits of `bytemuck` is that it has a richer set of traits and disallows structs with padding. The latter is significant because padding values are not currently specified in Rust, possibly resulting in unspecified bytes ending up in reserved bit ranges.
* `bincode` is better suited for serialization into its own bespoke format. In many case, custom seralization code is required to produce the desired binary layout. Endianness is supported, but is passed as a configuration option instead of being a property of the struct, requiring it to be supplied at every encode/decode call.
* Serde-compatible crates like `binary_serde` are similar to `bincode` in that they tend to be targeted towards general serialization and not a specific format. `binary_serde` also doesn't support dynamically sized types like &[T]. This ultimately makes it partially incompatible with the broader Serde environment. Code would have to be specifically written for `binary_serde`, negating some of the benefit of using Serde.