# RFC: Default Private Repository Access by Explicit Access List Only

This RFC proposes that repositories in Open Device Partnership (ODP) that are marked as **private** should be invisible and inaccessible to ODP organization members by default unless those members are explicitly granted access through an approved team or direct repository permission.

## Change Log

- 2026-06-08: Initial RFC draft created.
- 2026-06-11: Addressed review feedback — explicit org admin visibility, required team-based access, 6-month audit evidence, private-to-public intent and transition checklist.

## Motivation

ODP has both public and private repositories. Private repositories are often used for early-stage, partner-sensitive, or pre-disclosure work that should not be broadly visible. Today, all ODP organization members can see all private repositories by default, which weakens confidentiality controls and makes "private" less predictable in practice.

This RFC applies a least-privilege model to private repositories:

- Being a member of ODP should **not** by itself imply visibility into private repositories.
- Access to a private repository should be intentional, reviewable, and auditable.
- Repository owners should be able to keep early-stage work, partner-sensitive material, and limited-distribution discussions private without relying on informal expectations.

## Technology Background

ODP uses GitHub for governance and repository management. Access is controlled through organization membership, teams, and repository-level grants.

Today, ODP grants members default read access to private repositories through an organization-wide base permission. This RFC changes that model so private repository access is granted only through explicit allowlists:

- approved GitHub teams mapped to a repository, or
- explicit repository collaborator grants where justified.

## Goals

The goals of this RFC are:

1. Ensure private repositories are visible only to explicitly authorized users.
2. Reduce accidental overexposure of pre-release, partner-sensitive, or incubation work.
3. Improve auditability of who has access to sensitive repositories.
4. Encourage repository owners to make an intentional visibility choice:
   - **Public** when broad collaboration is desired.
   - **Private** when access should be tightly controlled.

## Requirements

The following requirements define the proposed policy:

1. **No implied access from ODP membership alone**  
   Membership in the ODP GitHub organization must not, by itself, grant visibility into or access to any private repository. ODP GitHub organization owners (admins) retain full visibility and access to all repositories, including private repositories, as this is inherent to the GitHub platform administration role.

2. **Explicit authorization required**  
   A user must be explicitly granted access to a private repository through one of the following:
   - Add to a GitHub team that has been granted permissions to that repository (preferred).
3. **Default deny for private repositories**  
   Private repositories must default to a deny-by-default posture. No broad organization-wide read access should be assumed or inherited for private repositories. At the GitHub organization level, base access must be configured so private repository visibility is not granted through membership alone.

4. **Team-based access required by default**  
   Team-based access is the required model for maintainability and auditability. Users should be added to an appropriate team rather than granted individual access.

5. **6-month access audit**  
   Owners or designated maintainers of a private repository must review its access list at least every six months and remove stale or unnecessary access.

6. **Audit evidence and record-keeping**  
   Each 6-month access review must produce a permanent, verifiable record confirming the audit was performed. Acceptable evidence includes a dated issue or pull request in the repository, or a signed-off audit log. ODP should provide an automated mechanism (for example, a scheduled GitHub Actions workflow) that reminds repository owners when a review is due and tracks completion.

7. **Exceptions must be explicit**  
   Any broad-access exception for private repositories (for example, the cargo vet auditor team needing cross-repository visibility, or security and release administration scenarios) must be explicitly documented and approved by the Steering Committee or a formally delegated operations group. Each exception must record owner, scope, justification, and review date.

8. **Private means not discoverable within ODP unless authorized**  
   For ODP governance purposes, a private repository should be treated as not visible to other ODP members unless they are on the approved access list.

9. **ODP platform and framework code must be contributed upstream**  
   Any ODP platform or framework code developed within a private repository — including partner collaboration repositories — must be contributed back upstream to a public ODP repository. Private repositories containing partner intellectual property may remain private when justified, but they must not become the sole home for reusable ODP platform or framework work. In all cases, private repositories must still comply with all other requirements in this RFC (team-based access, 6-month audits, etc.).

## Proposed Policy

ODP adopts the following repository access policy:

- **Public** repositories are intended for broad visibility and contribution.
- **Private** repositories are intended to be visible only to explicitly authorized users. Partner collaboration repositories containing partner IP may remain private when justified, but any ODP platform or framework code in those repositories must be contributed back upstream to a public ODP repository.
- ODP organization membership alone is insufficient to view or access a private repository.
- ODP GitHub organization owners (admins) retain full visibility to all repositories as part of their platform administration role.

The **Requirements** section is normative and applies to all private repositories upon ratification of this RFC.

## Unresolved Questions

The following questions should be resolved during RFC review:

### Resolved

1. Should there be a small number of standing exception teams (for example, security or release administration), and if so, how are those exceptions governed?
   - Yes. Exceptions are addressed in Requirement 7 with explicit documentation and Steering Committee approval.
2. What evidence should repository owners retain to show six-month access recertification was completed?
   - Addressed in Requirement 6. Acceptable evidence includes a dated issue, pull request, or signed-off audit log, with an automated reminder mechanism.
3. Should direct collaborator grants on private repositories require additional justification or expiration?
   - Direct grants now require documented justification (Requirement 2 and 4). Team-based access is required by default.
4. Should ODP also define guidance for when work should move from private to public?
   - Yes. Requirement 9 establishes that private repos should have a path to public, and a transition checklist is provided in the Adoption Strategy.

### Open

1. Should private repositories containing partner IP have a maximum retention period (for example, 12 or 24 months), after which the repository must be deleted or transferred out of the ODP organization?

## Prior Art

Common open-source governance practice distinguishes between broadly collaborative repositories and repositories intended for limited visibility. ODP already uses governance documentation and an RFC process to formalize organization-level policy decisions. This proposal extends that governance style to repository access control by making the default behavior for private repositories explicit and predictable.

Within ODP itself, the repository set already includes both public and private repositories, which reinforces the need for a clear policy about what "private" operationally means for maintainers and contributors.

## Alternatives

### Alternative 1: Make all ODP members able to see all private repositories (current behavior)

This is the current default in ODP. While it maximizes discoverability inside the organization, it weakens least-privilege controls and makes "private" less meaningful for sensitive or early-stage work. In practice, this is especially problematic for repositories that contain work related to unreleased hardware or that support early engagement with partners under confidentiality constraints. In those cases, broad visibility to all ODP members risks exposing pre-disclosure material to people who are not part of the relevant workstream, undermining the trust model that partners and hardware vendors expect.

### Alternative 2: Create a separate GitHub organization for partner engagement

A separate GitHub organization could be used to host private repositories intended for partner engagement and pre-release hardware work, keeping them fully isolated from the main ODP organization. However, maintaining a second GitHub organization is expensive in terms of licensing costs and introduces a significant maintenance burden. Teams, permissions, CI/CD integrations, and governance policies would need to be duplicated and kept in sync across both organizations. Contributors working across both organizations would face additional friction, and the split would fragment project history and tooling. The cost and operational complexity outweigh the benefits when the same isolation can be achieved through explicit access controls within a single organization.

## Rust Code Design

Not applicable.

## Guide-Level Explanation

Contributors:

- Use **public** when broad collaboration and discoverability are intended.
- Use **private** when access should be intentionally restricted.
- Do not assume ODP membership implies private repository access.
- Request private repository access through the appropriate team or explicit repository permission.

Repository owners:

- Choose private only when restricted visibility is intended.
- Maintain a deliberate access list.
- Prefer team-based permissions over individual additions.
- Periodically confirm that each person or team still needs access.

## Adoption Strategy

This policy applies to all private repositories upon RFC ratification. The rollout below defines remediation and verification steps:

1. Configure organization settings immediately so membership alone does not grant private repository visibility.
2. Inventory existing private repositories in ODP.
3. Review current access grants for those repositories.
4. Remove broad or stale access that does not align with the new policy.
5. Document any approved exception cases.
6. Set up a scheduled GitHub Actions workflow (or equivalent automation) to remind repository owners of 6-month access reviews and track audit completion.

### Private-to-Public Transition Checklist

When transitioning a repository from private to public, the repository owner must complete the following before changing visibility:

1. Review the full git history for secrets, tokens, API keys, or credentials and remove them (consider using tools such as `git filter-repo` or BFG Repo-Cleaner).
2. Review the full git history for partner-sensitive, pre-disclosure, or personally identifiable information and remove it.
3. Ensure all dependencies are compatible with public distribution and licensing requirements.
4. Confirm the repository license is correct and visible.
5. Review and update the README and CODEOWNERS for public-facing context.
6. Remove or redact any internal-only documentation, links, or references.
7. Obtain sign-off from the repository owner or designated maintainer that the scrub is complete.

Completion criteria:

1. All private repositories have an explicit team-based or justified direct access model.
2. Organization-wide membership does not grant private repository visibility by default.
3. Approved exceptions are documented with owner, scope, justification, and review date.

## Drawbacks

This policy increases administrative overhead for repository owners and may slow down access for contributors who need to join a private workstream. It also reduces incidental discoverability of work inside ODP. Those tradeoffs are intentional and are the cost of a clearer least-privilege posture for private repositories.
