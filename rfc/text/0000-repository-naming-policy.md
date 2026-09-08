# RFC: ODP Repository Naming Policy

This RFC defines the naming policy for repositories in the Open Device Partnership (ODP) GitHub organization. The
policy communicates each repository's scope and purpose. For repositories temporarily hosted by ODP, it also
communicates that the repository is not intended to remain in the organization long term.

## Change Log

This text can be modified over time. Add a change log entry for every change made to the RFC.

- 2026-08-05: Initial RFC created.
- 2026-08-12: Replaced reason-specific temporary repository labels with the generic `staging` label and moved
              submodule guidance to the requirements section.
- 2026-08-12: Added preliminary study of which current repositories need to be renamed and clarified exemptions
              in the requirements.

## Motivation

ODP repositories have been created at different times by different projects without a shared naming convention.
Current names use inconsistent prefixes, separators, abbreviations, and ordering. Some identify an ODP project, some
identify a technology, target, or vendor, and others do not communicate how the repository relates to ODP or an
upstream project.

This inconsistency makes repository names difficult to interpret without opening each repository. It also makes it
harder for contributors to browse or search the organization by project, distinguish project repositories from
organization-wide repositories, and identify repositories that ODP does not intend to host long term.

A shared convention gives each label in a repository name one meaning and a predictable position. It allows every name
to answer the following questions:

1. Which ODP project or organization-wide grouping is this repository associated with?
2. What distinguishes this repository within that scope?
3. Is this repository staged temporarily in the ODP organization?

## Technology Background

ODP hosts repositories for individual projects, organization-wide functions, platform demonstrations, and temporary
collaboration with external projects or vendors. GitHub presents these repositories together at the organization
level, where the repository name is the primary information available before a contributor opens it. A predictable
name therefore helps contributors identify relevant repositories while browsing, searching, or following links from
outside ODP.

Git repository names do not define code architecture, package names, or ownership. An ODP repository may contain one
or more modules, tools, applications, or build targets without those choices changing the naming convention.

This RFC uses the following terms for naming cases:

- **Ancillary repository** - A repository whose exact name is established by GitHub or an organization-wide
  convention, such as `OpenDevicePartnership.github.io`.
- **Staging repository** - An ODP-hosted repository that is not intended to remain in the ODP organization long term.

## Goals

1. Make ODP repository names consistent and interpretable across the organization.
2. Identify the ODP project or organization-wide grouping associated with each repository.
3. Make a repository's distinguishing purpose discoverable from its name when the scope alone is insufficient.
4. Identify staging repositories so contributors do not mistake them for repositories ODP intends to maintain.
5. Support contributors searching by project, capability, upstream repository, hardware target, or vendor and item
   name.

## Requirements

The naming policy has the following requirements:

- This policy applies to public, active repositories hosted in the ODP GitHub organization. The following repositories
  are exempt:
  - Ancillary repositories whose names are established by GitHub or an organization-wide convention.
  - Private repositories while they remain private.
  - Archived repositories while they remain archived.
  - Existing vendor repositories already staged for transfer out of ODP when this RFC is adopted.
- Repository names use the pattern `<scope>[-<purpose>[-staging]]`.
- Labels use lowercase ASCII letters and digits. Hyphens separate labels, and underscores separate words within a
  label.
- `<scope>` is required and identifies an approved ODP project or a reserved organization-wide grouping. Additional
  reserved organization-wide scope labels require an update to this RFC.
- `<purpose>` identifies what distinguishes a repository within its scope. It is required unless the repository
  represents the primary project. Project maintainers approve purpose labels within their scope.
- The `staging` suffix is required when ODP does not intend to host a repository long term and must not be used when ODP
  intends to maintain the repository. A staging repository must be removed from ODP as soon as practical after its
  contents have been upstreamed, transferred, or are no longer needed.
- New ODP repositories must use this policy when they are created; existing repositories need a plan for adoption.
- This policy does not govern the name or path under which a repository is included as a Git submodule.

## Unresolved Questions

No unresolved questions are currently known for the naming grammar itself. Review of this RFC may identify additional
reserved organization-wide scopes or naming cases that the proposed labels do not represent. The following related
decisions are outside the scope of this RFC:

- The final list of repositories to rename and their approved new names.
- Whether existing repositories should be combined, divided, transferred, archived, or removed.
- The schedule, tooling, and ownership for repository renames.
- Enforcement mechanisms and deadlines for adopting the policy.
- Repository contents, layout, documentation, build, CI, release, and ownership policy.

## Prior Art

Existing ODP repository names demonstrate several naming approaches. Some use an `odp-` prefix, such as
`odp-platform-qemu-arm-virt`; some use a project prefix, such as `patina-apps`; and others use an unscoped capability,
device, or upstream project name, such as `cortex-m-stack`, `bq40z50`, or `edk2`. These names are the direct prior art
for this proposal, but no single existing approach consistently identifies scope, purpose, and temporary status.

The proposed convention retains useful project and purpose terms from existing names while assigning them predictable
positions. The examples in the Guide-Level Explanation section show how representative existing names map to the
proposed convention.

## Alternatives

### Keep Existing Names

ODP could leave repository naming to individual projects. This avoids migration work but preserves the current
inconsistency and requires contributors to open repositories to determine their relationship to ODP.

### Use Only Scope and Purpose

The convention could omit the `staging` suffix and use only `<scope>-<purpose>`. This is simpler, but staging
repositories would be indistinguishable from repositories ODP intends to maintain.

### Use Vendor Names as Scope

Repositories associated with a hardware vendor could use that vendor as `<scope>`. This would make vendor searches
direct, but it would obscure the ODP project responsible for the work and could incorrectly imply vendor ownership.
Vendor and item names therefore belong in `<purpose>` when they help distinguish a repository.

### Use Reason-Specific Temporary Status Labels

The temporary status could identify why a repository is hosted temporarily, using labels such as `fork` or `handoff`.
This would provide more detail in the name, but it would restrict the known reasons for temporary hosting and require
new labels as other cases arise. The literal `staging` suffix identifies temporary repositories without constraining
why they are temporary.

### Use Hyphens for All Word Boundaries

Repository names could use hyphens both between labels and between words within labels. This is familiar, but it makes
the label boundaries ambiguous. Using hyphens between labels and underscores within labels keeps the name parseable.

## Rust Code Design

Not applicable.

## Guide-Level Explanation

Choose labels for scope, purpose, and if staging is needed in the name `<scope>[-<purpose>[-staging]]`:

- Scope: Select the ODP project most directly associated with the repository. Approved labels are derived from the
  ODP project names maintained by the [governing board](https://opendevicepartnership.org/projects) and normalized
  according to this policy. For example, `Patina` becomes `patina`.  Or use a reserved organization-wide scope when
  no individual project is the appropriate scope:
  - `common` for repositories associated with multiple projects or not clearly associated with one project.
  - `governance` for the primary ODP governance repository and repositories supporting organization-wide governance or
    rule enforcement.
  - `platform` for repositories integrating a bootable demonstration for a hardware or emulated target.
- Purpose: Select a label that represents the primary project within the scope. Describe why the repository exists,
  rather than its language, packaging format, or repository type. When a vendor identifies an item, include both in
  the same label, separated by an underscore; for example, `bq40z50_ti`.
- Staging: Add the staging suffix when ODP does not intend to host and maintain the repository. A vendor name in
  `<purpose>` does not by itself mean the repository is staging.

As of 2026-08-12, a total of 89 repositories were visible to the author of this RFC under the ODP organization.  The
following tables list suggested actions to take according to this specification for each one.  If other repositories
are present in the org and are not listed due to access rights, they would fall under the 'private repo' listing table
below.

### Public Repositories that need changes

The following 32 repositories out of the 89 were determined to be the ones that may need name changes.  There is
another directive to reduce the number of repositories (example, 'embedded-drivers' repo with common build tools,
documentation, layout, CI, etc.), which if done first could reduce this number to around 20.

| Proposed Name | Current Name | Notes |
| --- | --- | --- |
| **common** | | |
| common-cga | cga | Call graph analysis tool |
| common-crateplace | crateplace | Embedded crate placement tool |
| common-pico_de_gallo | pico-de-gallo | QEMU build tooling |
| common-qemu_builder | odp-qemu-builder | QEMU build tooling |
| **embedded** | | |
| embedded | odp-embedded-controller | Primary Embedded Controller project repository |
| embedded-keyboard_rs | embedded-keyboard-rs | Matrix keyboard driver |
| embedded-power_sequence | embedded-power-sequence | SoC power sequencing HAL |
| embedded-usb_pd | embedded-usb-pd | USB Power Delivery types |
| embedded-utilities | odp-utilities | Tools used across ODP EC projects |
| embedded-cortex_m_stack | cortex-m-stack | ODP-owned Cortex-M stack usage tools |
| embedded-systemview_tracing | systemview-tracing | Tracing support |
| embedded-slimloader | ec-slimloader | Embedded Controller stage-one bootloader |
| embedded-zephyr_lang_rust-staging | zephyr-lang-rust | Temporary Zephyr fork |
| embedded-zephyr-staging | zephyr | Temporary Zephyr fork |
| **governance** | | |
| governance-discussions | discussions | Organization-wide community discussions |
| governance-documentation | documentation | Organization-wide documentation supporting ODP governance |
| governance-rust_driver_template | drive-rs | Rust driver project template; confirm organization-wide scope |
| governance-rust_crate_audits | rust-crate-audits | Organization-wide Rust crate audits |
| **patina** | | |
| patina-dxe_core_qemu | patina-dxe-core-qemu | Patina DXE Core build for QEMU |
| patina-fw_patcher | patina-fw-patcher | Patina firmware patching tool |
| patina-readiness_tool | patina-readiness-tool | Patina platform readiness tools |
| **platform** | | |
| platform-common | odp-platform-common | Common platform integration content |
| platform-qemu | odp-platform-qemu-arm-virt | Arm virtual platform demonstration |
| platform-radxa_orion_o6 | odp-platform-radxa-orion-o6 | Radxa Orion O6 platform demonstration |
| platform-windows_drivers | odp-windows-drivers | Windows drivers |
| platform-arm_trusted_firmware-staging | arm-trusted-firmware | Trusted Firmware-A mirror |
| platform-edk2-staging | edk2 | Temporary EDK II fork for platform builds |
| platform-ffa-staging | ffa | Arm Firmware Framework library |
| **secure services** | | |
| services | embedded-services | Primary Secure Services framework and service implementations |
| services-hafnium | odp-secure-services | Hafnium deployment of secure services |
| services-hafnium_platforms-staging | odp-hafnium-project | Imported Hafnium platform configurations with ODP-specific changes |
| N/A (unused) | hafnium | Mirror repo with no ODP activity, assuming it will be deleted |

### Public Repositories Named Properly

Under this RFC, several of the repositories are already named properly.  This assumes the name used to represent each of the projects under
the ODP umbrella are patina, embedded, and services.  This list removes another 16 of the 89 repositories from the list of names that need
to change.

| Repository Name | Notes |
| --- | --- |
| embedded-batteries | Battery fuel gauge and charger HAL |
| embedded-cfu | Component Firmware Update library |
| embedded-fans | Fan control HAL |
| embedded-mcu | MCU-agnostic traits and libraries |
| embedded-perfmon | Confirm purpose and long-term ownership |
| embedded-regulator | Voltage regulator HAL |
| embedded-sensors | Sensor HAL |
| governance | Primary repository for the reserved `governance` scope |
| patina | Primary Patina project repository |
| patina-apps | Patina applications |
| patina-components | Components used with Patina |
| patina-devops | Patina development operations |
| patina-edk2 | Patina definitions for EDK II-style C code |
| patina-mtrr | Patina Memory Type Range Register support |
| patina-paging | Patina paging support |
| patina-qemu | Patina QEMU demonstration |

### Exempt Repositories

Under this RFC, any ancillary, private, currently staged vendor, and archived repos are exempt from the naming convention.
Those rules allow 41 of the 89 repositories to be removed from the naming change.

| Repository Name | Policy |
| --- | --- |
| .github | Ancillary repository |
| basic-template | Private repository |
| bq25763 | Private repository |
| ec-slimloader-descriptors | Archived public repository |
| ec-test-app | Archived public repository |
| embassy-imxrt | Current vendor staging repository |
| embassy-mcxa | Current vendor staging repository |
| embassy-npcx | Current vendor staging repository |
| embedded-rust-template | Private repository |
| gh-orchestrator | Private repository |
| mcxa-pac | Current vendor staging repository |
| mec17xx-pac | Current vendor staging repository |
| mctp-rs | Archived public repository |
| mimxrt600-fcb | Current vendor staging repository |
| mimxrt633s-pac | Current vendor staging repository |
| mimxrt685s-pac | Current vendor staging repository |
| mimxrt685s-examples | Archived public repository |
| modern-payload | Private repository |
| npcx490m-pac | Current vendor staging repository |
| npcx490m-examples | Archived public repository |
| odp-platform-qemu-q35 | Private repository |
| OpenDevicePartnership.github.io | Ancillary repository |
| patina-lzma-rs | Private repository |
| pfd-devops | Private repository |
| slimloader | Private repository |
| soc-embedded-controller | Private repository |
| standup-dashboard | Private repository |
| uefi-bds | Private repository |
| uefi-corosensei | Archived public repository |
| uefi-sdk | Private repository |
| INA4230 | Texas Instruments staging repository |
| bq25723 | Texas Instruments staging repository |
| bq25770g | Texas Instruments staging repository |
| bq25773 | Texas Instruments staging repository |
| bq40z50 | Texas Instruments staging repository |
| bq41z50 | Texas Instruments staging repository |
| is31fl3743b | Lumissil Microsystems staging repository |
| lis2dw12-i2c | STMicroelectronics staging repository |
| pcal6416a | NXP Semiconductors staging repository |
| tmp108 | Texas Instruments staging repository |
| tps6699x | Texas Instruments staging repository |
