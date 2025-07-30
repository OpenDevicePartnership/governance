# RFC: `Apache 2.0 License for Patina`

[Patina](https://opendevicepartnership.github.io/boot-firmware) currently uses a [BSD-2-Clause-Patent](https://spdx.org/licenses/BSD-2-Clause-Patent.html)
license. This RFC proposes to change the license to the [Apache License 2.0](https://spdx.org/licenses/Apache-2.0.html).

## Change Log

- 2025-07-30: Initial RFC created

## Motivation

The UEFI firmware ecosystem contains a rich source of intellectual property that is protected by patents. In order for
vendors to freely collaborate in an open source project, it has always been important to clearly establish how patent
rights are granted to participants in the project. In the past, ambiguity in some licenses has been supplemented with
a Contributor License Agreement (CLA) that grants patent rights to the project. However, even CLAs have had to be
revised over time to ensure they provide sufficient patent protection and developers have to maintain the text of that
agreement and resolve any issues that arise with it.

Patina is a Rust project. We have found that Rust projects tend to use either the [MIT](https://spdx.org/licenses/MIT.html)
or the [Apache License 2.0](https://spdx.org/licenses/Apache-2.0.html) as their primary license. For example, the
[rust-lang/rust](https://github.com/rust-lang/rust) repo is primarily distributed under the terms of both the MIT
license and the Apache License (Version 2.0), with portions covered by various BSD-like licenses.

While the BSD-2-Clause-Patent license does meet the licensing requirements of Patina, it is not as widely used in
Rust projects as MIT and Apache License 2.0. To motivation for this RFC is to transition to a license that satisfies
the requirements of Patina while also being more widely recognized and used in the Rust ecosystem.

## Technology Background

This section does not attempt to provide a comprehensive overview of the licenses involved, that can be found in more
authoritative sources such as the [Open Source Initiative](https://opensource.org/licenses) or the [Software Package Data
Exchange (SPDX)](https://spdx.org/licenses/). Instead, this section briefly describes why Apache 2.0 is preferred
over MIT given the requirements noted in the RFC.

The MIT license does not explicitly contain a patent grant, and therefore, it could be argued that it does not
automatically extend patent rights to modifications contributed to MIT licensed code.  If so, and we take the code and
implement it lacking patent rights to those modifications, then downstream users could be exposed to infringement
claims. It could be argued that MIT provides an implied patent grant due to its permissive nature, but this is not
universally accepted.

Apache 2.0 explicitly includes a patent grant that provides contributors with a clear and unambiguous license to use
the patents that cover the contributions they make.

It should be noted that a [Developer Certificate of Origin (DCO)](https://developercertificate.org/) is not a license,
but rather a statement that the contributor has the right to submit the code under the terms of the license. It is
often used in conjunction with licenses and CLAs to ensure that contributors have the right to submit their code.
However, it does not provide any additional patent rights beyond what is already granted by the license itself.
Therefore, it is not considered a substitute for a license that includes a patent grant, such as Apache 2.0.

## Goals

The primary goal of this RFC is to change the license of the Patina project from `BSD-2-Clause-Patent` to
`Apache License 2.0`. This change aims to:

1. Align Patina with the licensing practices of other Rust projects, particularly those that are widely used in the
   Rust ecosystem.
2. Simplify the licensing model by avoiding the need for a separate Contributor License Agreement (CLA) for patent
   rights.

More specifically, the goal is to adopt the following licensing model in Patina:

- All content in Patina repositories will be licensed under the Apache License 2.0.
- Patina repositories may depend on code (e.g. crates) with the following licenses:
  - Apache License 2.0
  - MIT License
  - BSD-Like Licenses (e.g. BSD-2-Clause, BSD-3-Clause)
- Patina contributions require a DCO to ensure that contributors have the right to submit their code under
  the terms of the Apache License 2.0.

## Requirements

At a high-level, Patina's license requirements are:

1. To foster an open source community that can freely collaborate on firmware development that aligns with the way
   open source code is integrated and distributed in proprietary firmware solutions.
2. To ensure that all contributors to the Patina project are granted sufficient patent rights to use the code in their
   products without fear of litigation.
3. To avoid the need for a Contributor License Agreement (CLA) that requires contributors to sign a separate document
   to grant patent rights, which can be cumbersome and may lead to misunderstandings or disputes.
4. To ensure that the license is compatible with popular existing UEFI firmware codebases, such as Tianocore's edk2, to
   facilitate integration and reuse of existing code.
5. To ensure that contributors comply with the licensing requirements of Patina via a Developer Certificate of Origin
   (DCO).

## Unresolved Questions

- At this time this RFC is scoped to Patina repositories within Open Device Partnership (ODP). Should this RFC be
  extended to other ODP repositories? It is left to the maintainers of those repositories to reply to the RFC if that
  should be the case.

## Prior Art

Since Tianocore's edk2 repository is the most prominent source of UEFI firmware code, this section briefly summarizes
how it has handled patents in the past per the details in [License-History.txt](https://github.com/tianocore/edk2/blob/master/License-History.txt).

- Prior to August 3, 2017
  - License: [BSD-2-Clause](https://opensource.org/licenses/BSD-2-Clause)
  - Patent Grant: Provided via a Contributor License Agreement (CLA) in the form of the
                  TianoCore Contribution Agreement 1.0 (covered source files)
- After August 3, 2017
  - License: [BSD-2-Clause](https://opensource.org/licenses/BSD-2-Clause)
  - Patent Grant: The TianoCore Contribution Agreement 1.1 was introduced to cover source files in adition to
                  documentation files in source and compiled form.
- After April 9, 2019
  - License: [BSD-2-Clause-Patent](https://spdx.org/licenses/BSD-2-Clause-Patent.html)
  - Patent Grant: The `BSD-2-Clause-Patent` license was adopted removing the need for the TianoCore Contribution
                  Agreement.

Based on this precedent and for this simplest integration of UEFI code within the framework of existing codebases based
on edk2, Patina initially adopted the `BSD-2-Clause-Patent` license.

Extending on the TianoCore case study, it should be noted the following licenses are accepted in the edk2 project:

- [Apache License, Version 2.0](https://opensource.org/license/apache-2-0/)
- [BSD 2-Clause](https://opensource.org/license/BSD-2-Clause)
- [BSD 3-Clause](https://opensource.org/license/BSD-3-Clause)
- [MIT](https://opensource.org/license/MIT)
- [Python-2.0](https://opensource.org/license/Python-2.0)
- [Zlib](https://opensource.org/license/Zlib)

## Alternatives

- Stay with the current `BSD-2-Clause-Patent` license.
  - This would achieve all of Patina's licensing goals but it is not as commonly used in the Rust ecosystem as
    Apache 2.0 or MIT.
- Use the `MIT` license.
  - To gain an equivalent patent grant, a separate Contributor License Agreement (CLA) would be required.
  - This would add complexity to the project and could lead to misunderstandings or disputes regarding patent
    rights.

## Rust Code Design

Not applicable.

## Guide-Level Explanation

Not applicable.
