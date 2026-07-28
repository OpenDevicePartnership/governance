# RFC: Documentation Philosophy for ODP Projects

This RFC proposes that Open Device Partnership (ODP) adopt a documentation
philosophy built on two principles:

1. **No project-specific documentation lives in the `documentation`
   repository.**
2. **Each ODP project has its own project-level [mdBook][mdbook]**, owned
   and maintained by that project and published via GitHub Pages.

The `documentation` repository continues to exist, but its role narrows to
hosting **organization-level** content (charter, governance, cross-project
standards, the RFC index) and to acting as a landing page that links out to
each project's mdBook.

## Change Log

- 2026-07-21: Initial RFC draft created.

## Motivation

ODP projects today handle documentation inconsistently. Some projects, such
as Secure EC and Standardized EC Services, keep their documentation in the
ODP org-level `documentation` repository. Others, such as Patina, keep their
documentation in a project specific repository. The two principles proposed
by this RFC resolve that inconsistency.

The current split causes real friction:

- **Discoverability.** Contributors browsing a project repository do not
  reliably find its documentation; they have to know that a separate
  documentation repository exists and how it is organized.
- **Ownership ambiguity.** Centralized docs are edited by many people across
  many projects, which weakens per-project ownership and review signal
  (CODEOWNERS, project maintainers, subsystem owners).
- **Cross-repo coordination cost.** Reviewers, release processes, and
  automation have to reason about two repositories to land a single logical
  change.
- **Inconsistent contributor experience.** New contributors have to learn a
  different workflow depending on which ODP project they are working on.

Patina has already validated the project-level mdBook approach in
production within ODP. Elevating that pattern into an explicit
organization-wide philosophy removes the split, aligns ODP with common
Rust ecosystem practice, and gives every project a first-class,
independently owned documentation surface.

## Technology Background

- **mdBook** ([`rust-lang/mdBook`][mdbook]) is the documentation tool used by
  the Rust project and much of the Rust ecosystem. It builds a static book
  site from a tree of Markdown files and a `SUMMARY.md` table of contents.
- **GitHub Pages** publishes static sites directly from a GitHub repository,
  typically via a GitHub Actions workflow that builds the mdBook on push and
  deploys the rendered output.

## Goals

1. Establish a single, consistent documentation philosophy across all ODP
   projects, expressed as two clear principles:
   - No project-specific documentation lives in the `documentation`
     repository.
   - Every ODP project has its own project-level mdBook.
2. Give each project a first-class, independently owned documentation
   surface that can evolve with the project.
3. Standardize the documentation toolchain on **mdBook + GitHub Pages** so
   contributors, reviewers, and readers have a consistent experience across
   projects.
4. Preserve a clear home for **organization-level** documentation (charter,
   governance, cross-project standards, the RFC index) that is not
   project-specific.
5. Migrate existing project-specific documentation currently in the
   `documentation` repository (Secure EC, Standardized EC Services) into
   the corresponding project's mdBook without loss of content or history
   where practical.

## Requirements

1. **No project-specific docs in the `documentation` repository.** The
   `documentation` repository hosts only organization-level content:
   charter, governance, cross-project standards and conventions, the RFC
   index, and a landing page that links out to each project's published
   mdBook. Project-specific technical documentation does not belong there.
2. **Every ODP project has a project-level mdBook.** Each project owns and
   maintains its own mdBook (Markdown + `SUMMARY.md`, built with `mdbook`)
   covering that project's documentation. NOTE: this does not mean that
   every repository in the organization must have an `mdbook`.
3. **Project mdBooks live in an appropriate project repository** under a
   conventional in-repo path (default: `docs/`), so documentation is
   owned, reviewed, and versioned alongside the project.
4. **GitHub Pages publishing.** Each project publishes its rendered mdBook
   via GitHub Pages from a project repository, using a GitHub Actions
   workflow that builds on push to the project's default branch.
6. **Existing centralized docs are migrated.** Documentation currently held
   in the `documentation` repository for Secure EC and Standardized EC
   Services is moved into those projects' mdBooks. The original locations
   in the `documentation` repository are then replaced with short link
   stubs pointing at the new canonical location, then removed once inbound
   links have been updated.
7. **New projects follow this model on day one.** Any new project onboarded
   under ODP governance stands up a project-level mdBook with a GitHub
   Pages workflow as part of initial setup, and does not place
   project-specific documentation in the `documentation` repository.
8. **Project owners decide which repository to host the mdBook from.**
   Projects may have multiple repositories and the specific question of
   which repository to host the prject level mdBook out of is left up
   to the project owners.

## Migration Plan

The migration is performed **per project** and is expected to run
incrementally. For each project currently documented in the `documentation`
repository (initially: Secure EC and Standardized EC Services), the owning
maintainers:

1. **Stand up mdBook in a project repository.**
   - Add a `docs/` directory containing `book.toml`, `src/SUMMARY.md`, and
     an initial `src/` tree.
   - Add a GitHub Actions workflow that builds the mdBook and deploys it to
     GitHub Pages on push to the default branch.
   - Enable GitHub Pages on the project repository.
2. **Move content.** Copy the project's documentation from the
   `documentation` repository into `docs/src/` in the project repository,
   preserving structure where it still makes sense. Update internal links
   to be relative to the new location.
3. **Publish.** Land the new mdBook, verify the published GitHub Pages
   site, and confirm the `SUMMARY.md` covers the migrated content.

Once all previously centralized project docs have been migrated, the
`documentation` repository's top-level index/landing page is updated to
enumerate ODP projects and link to each project's published mdBook.

## Unresolved Questions

- **Migration timeline.** This RFC does not fix a completion date. Should
  a target window (e.g. "by the next release cycle") be set for the
  initial two projects, or is best-effort acceptable?

## Prior Art

- **Patina** already co-locates its documentation with its source code and
  publishes it as an mdBook. This RFC generalizes Patina's approach to the
  rest of ODP.
- **Docs-as-code more broadly.** Treating documentation as source that
  lives with the code, is reviewed in the same PRs, and is built by CI is
  a well-established pattern across open-source projects.

## Alternatives

- **Keep the status quo (mixed model).** Continue to allow both
  centralized and co-located documentation on a per-project basis.
  Rejected because it perpetuates the drift, discoverability, and
  ownership problems described in Motivation, and because contributors
  and reviewers continue to face inconsistent workflows across projects.
- **Centralize everything in the `documentation` repository.** Move
  Patina's documentation out of the Patina repository and require all
  projects to document themselves in `documentation`. Rejected because it
  worsens the drift problem, prevents atomic code+docs PRs, weakens
  per-project ownership, and reverses a model that is already working
  well for Patina.
- **Co-locate, but leave tooling open.** Require co-location without
  mandating mdBook or GitHub Pages. Rejected as a primary recommendation
  because it does not give contributors, reviewers, or readers a
  consistent experience across projects, and because mdBook + GitHub Pages
  is already the working approach in Patina and is well-supported in the
  Rust ecosystem. A future RFC can revisit the toolchain if a compelling
  reason emerges.
- **Publish from the `documentation` repository, author in project
  repositories.** Have project repositories author docs but centralize
  publishing. Rejected as unnecessarily complex; GitHub Pages publishing
  from the project repository is straightforward and keeps ownership in
  one place.

[mdbook]: https://github.com/rust-lang/mdBook
[rust-book]: https://doc.rust-lang.org/book/
[cargo-book]: https://doc.rust-lang.org/cargo/
[rustc-dev-guide]: https://rustc-dev-guide.rust-lang.org/
