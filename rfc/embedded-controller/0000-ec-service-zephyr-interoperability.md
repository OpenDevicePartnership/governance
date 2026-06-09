# RFC: Enable ODP Secure EC Services on Zephyr

- **RFC PR:** TBD  
- **Author(s):** Jerry Xie
- **Status:** Draft  
- **Created:** 2026-06-08  
- **Tracking Issue:** TBD  

## Summary

ODP intends to enable Secure EC services to run on Zephyr through a staged interoperability approach.

This RFC proposes:
- Supporting ODP Rust-based Secure EC services in Zephyr-based environments
- Providing an incremental adoption path for OEMs already aligned on Zephyr
- Collaborating with the Zephyr and Linaro communities on Rust integration gaps

This is **not** a replacement of the Embassy-native ODP architecture. Instead, this is an interoperability and ecosystem expansion effort.

## Motivation

ODP partners (notably OEMs such as Dell) have indicated:
- Zephyr is a strategic baseline for EC firmware due to ecosystem maturity and hardware support
- A full migration to a Rust-first stack is not immediately feasible
- Incremental adoption of Rust components is preferred

At the same time:
- ODP’s Secure EC architecture is centered on memory safety, modular services, and Rust
- Early internal prototypes show that Rust services can run on Zephyr with adapter layers
- Zephyr’s Rust support is evolving but incomplete

This creates a clear opportunity:

> Enable ODP Secure EC capabilities in Zephyr environments without requiring a full stack replacement.

## Guide-level Explanation

ODP will support a **hybrid integration model**:

### Path A — Rust Services on Zephyr

- Run ODP Rust services on top of Zephyr
- Reuse existing Zephyr drivers (C-based initially)
- Use thin abstraction layers / FFI where necessary

### Path B — Rust Drivers in Zephyr

- Enable Rust-based drivers in Zephyr
- Improve devicetree integration and driver ergonomics
- Reduce reliance on C over time

### Staged Approach

- **Phase 1:** ODP services running on Zephyr with minimal changes  
- **Phase 2:** Incremental introduction of Rust drivers and deeper integration  
- **Long-term:** Portable Rust EC services across Embassy and Zephyr environments  

## Goals

1. **Signal Intent Publicly**  
   Clearly communicate ODP’s direction to partners and the Zephyr community.

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

## Non-Goals

This RFC does **not**:

- Replace the Embassy-native ODP architecture  
- Guarantee immediate production readiness on Zephyr  
- Commit to full Rust driver coverage in the near term  
- Require upstream acceptance of all contributions  

## Reference-level Explanation

### Current State

- ODP Secure EC is tightly coupled to a Rust-first architecture
- Zephyr is C-based with evolving Rust support
- Initial prototypes demonstrate:
  - Rust application logic running on Zephyr
  - Rust interacting with Zephyr drivers via wrappers

### Proposed Model

#### Phase 1: ODP on Zephyr

- Execute ODP Rust services within Zephyr runtime
- Bridge to Zephyr drivers using wrapper layers
- Validate functionality on real hardware platforms

#### Phase 2: Rust Driver Enablement

- Introduce Rust-native drivers where beneficial
- Improve:
  - Device abstraction layers
  - Devicetree integration
  - FFI tooling and ergonomics

#### Long-term Direction

- Portable async Rust services across:
  - Embassy-native environments
  - Zephyr-based environments
- OEMs can choose their migration path and pace

## Why This Approach

This approach balances:

| Requirement | Approach |
|------------|----------|
| OEM adoption | Meet Zephyr users where they are |
| Security goals | Preserve Rust-first architecture |
| Ecosystem alignment | Collaborate with Zephyr community |
| Engineering practicality | Allow staged migration |

## Drawbacks

- Increased complexity from hybrid Rust/C systems  
- Additional maintenance (wrappers, integration layers)  
- Potential confusion about “primary” architecture  
- Dependency on evolving upstream Rust support in Zephyr  

## Rationale and Alternatives

### Alternative 1: Stay Embassy-only

- Pros: Clean architecture  
- Cons: Limits OEM adoption  

### Alternative 2: Rust Drivers Only

- Pros: Incremental and upstream-friendly  
- Cons: Does not enable reuse of ODP services  

### Alternative 3: Services on C Drivers Only

- Pros: Fastest path to adoption  
- Cons: Does not improve long-term safety or ecosystem  

**Decision:** Support both service-level and driver-level integration paths.

## Prior Art

- Zephyr Rust effort (Linaro / community initiative)
- ODP internal PoCs:
  - Rust services running on Zephyr
  - Rust driver experiments via thin abstraction layers
- ODP “Journey to Zephyr” architectural exploration

## Unresolved Questions

- Which Secure EC services should be prioritized first?
- What is the upstream contribution strategy (wrapper-first vs driver-first)?
- How should temporary forks or patches be managed?
- What metrics (RAM, flash, performance) should be published?
- What belongs upstream vs ODP-specific?

## Security and Ecosystem Implications

- Aligns with ODP goals:
  - Memory safety
  - Modular architecture
  - Reusable services
- Expands reach of Secure EC capabilities to Zephyr ecosystem
- Encourages open collaboration rather than proprietary divergence

## Proposed Decision

ODP will:

> Enable Secure EC services on Zephyr through a staged interoperability strategy, prioritizing practical OEM adoption while investing in upstream Rust ecosystem improvements where impactful.

## Rollout / Next Steps

1. Publish this RFC in the governance repository  
2. Share with Zephyr maintainers and collaborators for feedback  
3. Link to existing PoC work and define follow-on issues  
4. Select initial services and benchmarks for implementation  

