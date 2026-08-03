# RFC: Private Repository Access and Role

This RFC proposes that repositories in Open Device Partnership (ODP) that are marked as **private** should be invisible
and inaccessible to ODP organization members by default unless those members are explicitly granted access through an
approved team or direct repository permission.

It also defines the limited role of private repositories in ODP. A private repository is only a temporary staging state
for content that is intended to become public. Confidential content, and repositories with no plan to become public, do
not belong in the open-source ODP organization. Updated the Alternatives section to remove stale content.

## Change Log

- 2026-06-08: Initial RFC draft created.
- 2026-06-11: Addressed review feedback — explicit org admin visibility, required team-based access, 6-month audit
  evidence, private-to-public intent and transition checklist.
- 2026-08-03: Clarified that private repositories are only a temporary staging mechanism for content intended to become
  public, and that confidential content and repositories with no plan to become public do not belong in the ODP
  organization. Simplified access controls accordingly.

## Motivation

ODP exists to promote cooperative innovation in firmware development through contribution and transparency. The ODP
GitHub organization is meant to be an open, collaborative community where every level of access, from reader to
administrator, is available to participants regardless of their employer or affiliation. To realize that goal, ODP must
ensure that content added to the organization is scoped appropriately.

Private repositories exist to stage content that is intended to become public while it is being prepared for release. A
private repository is a temporary holding state, not a permanent destination. Content that will never be published, and
content that carries a confidentiality obligation, does not belong in the ODP organization.

This RFC therefore applies two main policies:

1. A least-privilege access model, so membership in ODP does not by itself grant visibility into private repositories
   and access is instead intentional and explicitly granted.
2. A scope control, so private repositories are limited to temporarily staging content that is actively being prepared
   for public release, and repositories with a confidentiality element or with no plan to become public are kept out of
   the ODP organization.

## Technology Background

ODP uses GitHub for governance and repository management. Access is controlled through organization membership, teams,
and repository-level grants.

Today, ODP grants members default read access to private repositories through an organization-wide base permission. This
RFC changes that model so private repository access is granted only through explicit allowlists:

- approved GitHub teams mapped to a repository, or
- explicit repository collaborator grants where justified.

## Goals

The goals of this RFC are:

1. Keep the ODP organization open and transparent, with equal access for all participants regardless of affiliation.
2. Limit private repositories to temporarily staging content that is intended and being actively prepared to become
   public.
3. Keep confidential content, including material covered by a non-disclosure agreement, out of the ODP organization.
4. Keep repositories that have no plan to become public out of the ODP organization.
5. Ensure private repositories are visible only to explicitly authorized users while they remain private.
6. Encourage repository owners to make an intentional visibility choice:
   - **Public** when broad collaboration is desired.
   - **Private** only as a temporary staging state for content being prepared for public release.

## Requirements

The following requirements define the proposed policy:

1. **No implied access from ODP membership alone**: Membership in the ODP GitHub organization must not, by itself, grant
   visibility into or access to any private repository. ODP GitHub organization owners (admins) retain full visibility
   and access to all repositories, including private repositories, as this is inherent to the GitHub platform
   administration role.

2. **Team-based access required by default**: Team-based access is the required model for private repos for
   maintainability and clear ownership. Users should be added to an appropriate team rather than granted individual
   access.

3. **ODP platform and framework code must become public**: Any ODP platform or framework code developed within a private
   repository must be published to a public ODP repository. A private repository must not become the permanent or sole
   home for reusable ODP platform or framework work. While a repository remains private, it must still comply with all
   other requirements in this RFC.

4. **No confidential content in the ODP organization**: The ODP organization must not host content that carries a
   confidentiality obligation. This includes material covered by non-disclosure agreements or other non-public
   information. Work that requires this kind of protection must be kept outside the ODP organization.

## Proposed Policy

ODP adopts the following repository access policy:

- **Public** repositories are intended for broad visibility and contribution, and represent the normal state for work in
  the ODP organization.
- **Private** repositories are a temporary staging state for content that is intended to become public and is being
  prepared for release. While private, they are visible only to explicitly authorized users. Confidential content, and
  repositories with no plan to become public, do not belong in the ODP organization.

- ODP organization membership alone is insufficient to view or access a private repository.
- ODP GitHub organization owners (admins) retain full visibility to all repositories as part of their platform
  administration role.

The **Requirements** section is normative and applies to all private repositories upon ratification of this RFC.

## Unresolved Questions

The following questions should be resolved during RFC review:

### Resolved

1. Should there be a small number of standing exception teams (for example, security or release administration), and if
   so, how are those exceptions governed?
   - Yes. Exceptions are allowed with explicit documentation and Steering Committee approval.
2. Should direct collaborator grants on private repositories require additional justification or expiration?
   - Team-based access is required by default.
3. Should ODP also define guidance for when work should move from private to public?
   - Yes. The requirements establish that private repositories are only a temporary staging state and must have a plan
     to become public, and a transition checklist is provided in the Adoption Strategy.

### Open

1. Should private repositories have a maximum time they may remain private (for example, 12 or 24 months) before they
   must either become public or be removed from the ODP organization?

## Prior Art

Common open-source governance practice distinguishes between broadly collaborative repositories and repositories
intended for limited visibility. ODP already uses governance documentation and an RFC process to formalize
organization-level policy decisions. This proposal extends that governance style to repository access control by making
the default behavior for private repositories explicit and predictable.

Within ODP itself, the repository set already includes both public and private repositories, which reinforces the need
for a clear policy about what "private" operationally means for maintainers and contributors.

## Alternatives

### Alternative 1: Make all ODP members able to see all private repositories

This could reduce administrative overhead, but it would also defeat the purpose of private repositories serving as a
place to prepare content in a way that is meaningful to release to the intended audience.

## Rust Code Design

Not applicable.

## Guide-Level Explanation

Contributors:

- Use **public** for normal work, when broad collaboration and discoverability are intended.
- Use **private** only to temporarily stage content that is intended to become public and is being prepared for release.
- Do not place confidential content, including anything covered by a non-disclosure agreement, in the ODP organization.
- Do not assume ODP membership implies private repository access.
- Request private repository access through the appropriate team or explicit repository permission.

Repository owners:

- Choose private only as a temporary staging state, with a plan to make the repository public.
- Do not create a private repository that is intended to stay private indefinitely or that holds confidential material.
- Maintain a deliberate access list.
- Prefer team-based permissions over individual additions.
- Periodically confirm that each person or team still needs access.

## Adoption Strategy

This policy applies to all private repositories upon RFC ratification. The rollout below defines remediation and
verification steps:

1. Configure organization settings immediately so membership is given by being a member of a GitHub team with access to
   the private repository.
2. Inventory existing private repositories in ODP.
3. For each private repository, confirm it holds no confidential content and has a documented plan to become public.
   Move confidential work out of the ODP organization, and either establish a path to public or remove any repository
   that has no plan to become public.
4. Review current access grants for those repositories.
5. Remove broad or stale access that does not align with the new policy.
6. Document any approved exception cases.

### Private-to-Public Transition Checklist

When transitioning a repository from private to public, the repository owner must complete the following before changing
visibility:

1. Review the full git history for secrets, tokens, API keys, or credentials and remove them.
2. Review the full git history for sensitive or personally identifiable information and remove it.
3. Ensure all dependencies are compatible with public distribution and licensing requirements.
4. Confirm the repository license is correct and visible.
5. Review and update the README and CODEOWNERS for public-facing context.
6. Remove or redact any non-public documentation, links, or references.
7. Obtain sign-off from the repository owner and the ODP Steering Committee that the repository is ready to become
   public.
8. Remove GitHub teams and collaborators that are no longer needed for the public repository.
