# Patina Repository Licensing

The Patina projects within ODP have adopted the Apache 2.0 license as detailed in
[RFC: `Apache 2.0 License for Patina`](https://github.com/OpenDevicePartnership/governance/blob/main/rfc/0013-patina-apache-20-license.md).

## Applying the License

All new code contributions to Patina repositories must be licensed under the Apache 2.0 license.

### Repository License File

The Apache 2.0 license is present in `LICENSE` files in the root of each Patina repository.

### Source Code File Headers

Each source code file must include the license SPDX identifier for Apache 2.0 as shown below:

  ```text
  // SPDX-License-Identifier: Apache-2.0
  ```

Contributors can add their copyright to the file header when they make contributions to the file. For example:

  ```text
  // File description...
  //
  // Copyright (c) Example Corporation.
  // SPDX-License-Identifier: Apache-2.0
  ```

### Commit Message Developer Certificate of Origin (DCO)

Every commit must include a "sign-off line" to certify that the contributor has the right to submit the code under
the terms of the Apache 2.0 license. The sign-off line is added to the end of the commit message as shown below:

  ```text
  Signed-off-by: Example Contributor <example.contributor@example.com>
  ```

In the Git CLI, a sign-off line can be added with the `-s` option to `git commit`. For example:

  ```bash
  git commit -s -m "Commit message"
  ```

For more information, see the [Developer Certificate of Origin (DCO)](https://developercertificate.org/).

## Allowed Licenses for Dependencies

Patina repositories may depend on code (e.g. crates) with the following licenses:

- Apache License 2.0
- MIT License
- BSD-Like Licenses (e.g. BSD-2-Clause, BSD-3-Clause)
- Other licenses may be considered on a case-by-case basis by the maintainers of the repository.

Dependencies with licenses that are not compatible with Apache 2.0 are not allowed. All dependency licenses are
automatically checked via `cargo-deny` in CI.
