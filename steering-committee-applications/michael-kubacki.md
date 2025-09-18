# Open Device Partnership (ODP)

## Steering Committee Application

<img src="michael-kubacki.png" alt="Portrait" style="width: 150px; height: 150px; border-radius: 75px; display: block; margin: 0 auto;">

<div style="text-align: center;">

### Michael Kubacki • Principal Software Engineer • Microsoft

**`michael.kubacki@microsoft.com` / [makubacki (GitHub)](https://github.com/makubacki) / [linkedin.com/in/michaelkubacki](www.linkedin.com/in/michaelkubacki)**

**Proposed term** Jan 2026 – Dec 2026

**Primary focus area(s)** Patina (UEFI firmware)

</div>

---

## Professional Background

Michael Kubacki is a Principal Software Engineer in Microsoft's Core OS organization, where he leads strategic firmware
initiatives within the Core UEFI team. With over 14 years of experience in system firmware and five years at Microsoft,
Michael brings deep technical expertise and a strong commitment to advancing secure and reliable computing platforms.

Michael is a long-standing contributor to the open-source firmware ecosystem. He serves as a maintainer and steward in
the TianoCore community and actively supports multiple open-source efforts. In 2022, he helped initiate the Patina
project, guiding its evolution from a prototype into a full-fledged open-source initiative under the ODP umbrella.

## Value Added to ODP

- Technical expertise in UEFI firmware development, with a focus on modern security practices, memory-safe programming,
  and x86/64 architecture.
- A proven track record of collaborating in open-source projects and fostering collaboration among diverse stakeholders.
- A position in the ecosystem that allows him to bridge industry-wide firmware needs across various vendors.
- Passion for advancing memory-safe programming in firmware through Rust, aligning with ODP's mission.

## Strategic Impact & Vision for ODP

Michael's leadership has been instrumental in establishing Patina's architecture and development practices to reflect
modern security and reliability standards.

Key contributions to date in Patina include:

- Driving the adoption of memory-safe programming through Rust, establishing Patina as a viable pure Rust-based
  firmware solution.
- Architectural direction for core subsystems so Patina's foundation is built on modern, secure design
  principles.
- Phasing out legacy firmware constructs like a priori dispatch and Traditional SMM in favor of safer models such as
  Standalone MM.
- Implementing rigorous supply chain security practices with tools like `cargo-deny` and `cargo-vet` to audit
  dependencies and mitigate risk in dependencies.

As the current Patina project lead, Michael oversees governance, technical direction, and cross-organizational
alignment between Patina and ODP. He holds a weekly technical working group meeting to facilitate collaboration among
contributors and ensure steady progress toward project milestones.

Michael envisions Patina and ODP as catalysts for modernizing firmware development across the industry. He champions
the use of Rust to improve memory safety and reduce systemic vulnerabilities in platform firmware. His goal is to
establish Patina as an implementation for secure, modern firmware that is auditable and scalable.

He is committed to fostering a collaborative and inclusive community, where contributors can engage openly and drive
innovation together reducing the barriers to memory safe firmware adoption for all.

## Commitments & Outcomes

These are the key outcomes I plan to focus on during this term:

- **Ease Patina Adoption**
  - Continue to develop and publish comprehensive documentation and tutorials for new Patina contributors.
    Success = Public docs are complete with up to date getting started guides, architecture overviews, and
    API references.
  - Make Standalone MM easier to adopt in x86/64 platform firmware since this is a key Patina DXE core requirement.
    Success = A viable, documented path for a project to adopt Standalone MM without significant engineering effort.
- **Patina MM Core Support**
  - Work with the Patina team to create a Rust (Patina) Standalone MM core with privilege separation that can replace
    existing C-based MM cores.
    Success = At least a prototype Rust Standalone MM core with documentation, tests, and at least one platform
    demonstrating its use.
- **Increase the Number of Patina DXE Modules**
  - Work with the community to identify and prioritize key DXE modules needed for common platform functionality.
    Success = At least three new DXE modules developed and merged into Patina, with documentation, tests, and
    integration examples on QEMU.

## Year in Review (If Renewing)

N/A
