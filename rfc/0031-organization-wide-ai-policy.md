# RFC: `Organization-Wide AI Policy for ODP`

This RFC proposes an organization-wide policy governing the use of AI coding assistants across all Open Device
Partnership (ODP) repositories. It establishes clear expectations for contributors using AI tools, covering
accountability, legal compliance, and quality standards to ensure that AI-assisted contributions meet the same
bar as fully human-authored work.

## Change Log

- 2026-04-21: Initial RFC created

## Motivation

AI coding assistants such as GitHub Copilot, ChatGPT, and Claude are increasingly used in software development.
These tools can accelerate development, help with boilerplate code, and assist in identifying bugs. However, they
also introduce risks around code quality, licensing, intellectual property, and contributor accountability.

Currently, the Patina project within ODP has established its own [AI policy](https://github.com/OpenDevicePartnership/patina/blob/main/CONTRIBUTING.md#ai-policy),
but no equivalent guidance exists at the organization level. This creates inconsistency across ODP repositories—some
projects may implicitly allow AI-generated contributions without safeguards, while others may have varying
expectations.

An organization-wide policy is needed to:

- Establish a consistent baseline for AI tool usage across all ODP repositories.
- Protect the project from legal and licensing risks associated with AI-generated code.
- Ensure that contributors remain accountable for the code they submit.
- Provide transparency into how AI tools are being used in the development process.

## Technology Background

As of today, AI coding assistants generally fall into two categories:

1. **Inline code completion tools** (e.g., GitHub Copilot, Codeium): These integrate into an editor and suggest
   code completions as the developer types. The developer selects, modifies, or rejects suggestions.

2. **Conversational AI tools** (e.g., ChatGPT, Claude, Gemini): These generate code, documentation, or
   explanations in response to natural language prompts. Output is typically copied into the codebase by the
   developer.

Key concerns with AI-generated code include:

- **Licensing ambiguity**: AI models are trained on large corpora of code with varying licenses. Generated output
  may inadvertently reproduce copyrighted or incompatibly licensed code.
- **Quality and correctness**: AI tools can produce plausible-looking but incorrect code, especially in
  safety-critical, low-level, or domain-specific contexts such as firmware development.
- **Accountability**: When AI generates code, it can be unclear who is responsible for reviewing, testing, and
  maintaining it. The contributor who submits the code must bear this responsibility.

## Goals

1. Define a clear, enforceable AI policy that applies to all ODP repositories.
2. Ensure that human contributors remain fully accountable for all submitted code, regardless of whether AI tools
   were used in its creation.
3. Protect ODP from legal and licensing risks associated with AI-generated content.
4. Maintain code quality standards by requiring thorough human review and testing of AI-assisted contributions.
5. Provide a framework that individual ODP projects can extend with project-specific requirements.
6. Define how the policy integrates into existing contribution workflows and guidelines.

## Requirements

1. **Human accountability**: A human contributor must take full responsibility for every contribution, including
   understanding, reviewing, testing, and maintaining the code.
2. **Legal compliance**: Contributors must ensure that AI-generated code complies with the licensing terms of the
   target ODP repository and that they have the legal right to submit the code.
3. **Quality standards**: AI-assisted contributions must meet the same quality, testing, and review standards as
   fully human-authored contributions.
4. **No direct AI submissions**: ODP does not accept contributions submitted directly by AI tools without
   substantive human involvement. Automated pull requests generated entirely by AI agents without human review are
   not permitted.
5. **Enforcement**: Maintainers reserve the right to reject contributions that violate this policy. Repeated
   violations may result in temporary or permanent restrictions on the contributor.
6. **Discoverability**: The policy must be easily discoverable by contributors, ideally surfaced at the point
   where contribution guidelines are read.

## Unresolved Questions

- Should ODP adopt a specific attribution format for AI-assisted contributions (e.g., the Linux kernel's
  `Assisted-by:` commit trailer)? If so, what information should be included (tool name, model version,
  specialized analysis tools)? **Resolved**: ODP will adopt a standard `Assisted-by:` commit trailer
  similar to the Linux kernel, where contributors are expected to indicate the AI tool(s) used, including
  model version and any specialized analysis tools that contributed to the generated code. (e.g., `Assisted-by: Claude:claude-3-opus coccinelle sparse`)
- ~~Should there be different tiers of policy strictness depending on the nature of the repository (e.g., firmware
  vs. documentation vs. tooling)?~~ **Resolved**: The policy uses a single baseline with project-specific
  extensions (see Proposed Policy §5). Individual projects may adopt stricter requirements but not weaker ones.
- How should this policy apply to AI-generated documentation, test cases, and non-code artifacts?
- ~~Should there be a mechanism for contributors to self-certify compliance with this policy (e.g., a checkbox in
  PR templates)?~~ **Resolved**: No. Policy compliance is already expected of all contributors, consistent with
  how the Code of Conduct and security policy are handled. A checkbox adds no enforcement value.

- How should this policy interact with existing project-level AI policies such as
  [Patina's AI policy](https://github.com/OpenDevicePartnership/patina/blob/main/CONTRIBUTING.md#ai-policy)?
  Should Patina's policy be updated to reference this org-wide policy as its baseline?

## Prior Art

### Patina AI Policy

The [Patina project](https://github.com/OpenDevicePartnership/patina/blob/main/CONTRIBUTING.md#ai-policy) within
ODP has established an AI policy that does not accept contributions directly from AI tools and requires
contributors to:

1. Have the legal right to submit AI-assisted code under Patina's licensing terms.
2. Fully understand the changes and be able to explain them to other contributors.
3. Thoroughly review the code to ensure it meets contribution guidelines.
4. Thoroughly test the code, including on QEMU and physical platforms for firmware changes.

Patina also requires that contributors have a working understanding of the relevant technologies (Rust, UEFI
firmware development) and reserves the right to reject or close pull requests that violate the policy, including
banning repeat offenders.

Notably, Patina embeds its AI policy directly within its `CONTRIBUTING.md` file. This approach makes the policy
highly visible to contributors who read the contribution guide before submitting their first pull request.

### Linux Kernel AI Policy

The [Linux kernel](https://github.com/torvalds/linux/blob/master/Documentation/process/coding-assistants.rst)
has adopted guidance for AI coding assistants that includes:

1. **Legal requirements**: All contributions must comply with GPL-2.0-only licensing.
2. **Human certification**: AI agents must not add `Signed-off-by` tags. Only humans can certify the Developer
   Certificate of Origin (DCO).
3. **Attribution**: Contributions should include an `Assisted-by:` tag indicating the AI tool, model version, and
   any specialized analysis tools used (e.g., `Assisted-by: Claude:claude-3-opus coccinelle sparse`).

The Linux kernel policy is notable for its pragmatic approach—it does not ban AI tools outright but places clear
responsibility on the human submitter and requires transparent attribution. The kernel maintains this policy as a
standalone document within its process documentation, separate from the general contribution guide but referenced
by it.

### Linux Foundation Generative AI Guidance

The [Linux Foundation](https://www.linuxfoundation.org/legal/generative-ai) has published organization-wide
guidance on the use of generative AI tools for open source development. Key points include:

1. **Contractual compatibility**: Contributors must ensure that the terms of their AI tool do not place
   restrictions on the tool's output that are inconsistent with the project's open source license, IP policies,
   or the Open Source Definition.
2. **Third-party copyrighted materials**: If the AI tool's output includes pre-existing copyrighted materials
   (including open source code) authored by third parties, the contributor must confirm they have permission
   (e.g., a compatible open source license or public domain declaration) to use, modify, and contribute those
   materials, and must provide appropriate notice and attribution.
3. **Project-specific policies**: Individual Linux Foundation projects may develop their own stricter guidance,
   and contributors must also comply with any employer-specific policies.

The Linux Foundation guidance is notable for explicitly allowing AI-generated contributions while placing the
burden on contributors to verify licensing compatibility and third-party IP compliance. It treats AI-generated
code the same as any other contribution in terms of technical merit and peer review.

## Alternatives

- **No organization-wide policy**: Leave AI policy decisions to individual projects.
  - This is the current state and leads to inconsistency. Contributors may be unaware of expectations when
    moving between ODP repositories.

- **Ban AI tools entirely**: Prohibit all use of AI coding assistants in ODP contributions.
  - This is difficult to enforce, excludes a useful class of development tools, and is increasingly out of step
    with industry practices.

- **Adopt Patina's policy verbatim for all repos**: Apply the existing Patina AI policy organization-wide.
  - Patina's policy includes firmware-specific requirements (e.g., QEMU and physical platform testing) that are
    not applicable to all ODP repositories. A broader policy should be more general while allowing projects to
    add stricter requirements.

## Proposed Policy

The following policy shall apply to all ODP repositories unless a project has adopted a stricter project-specific
policy (in which case the stricter policy takes precedence).

### 1. Human Accountability

ODP does not accept contributions submitted directly by AI tools. All contributions must be made by a human
contributor who takes full responsibility for the submission. Specifically, the contributor must:

- Fully understand the changes being made and be able to explain them to other contributors and maintainers.
- Ensure the contribution meets the project's coding standards, contribution guidelines, and review expectations.
- Take responsibility for maintaining the contributed code.

### 2. Legal and Licensing Compliance

Contributors must ensure that any AI-assisted code complies with the licensing terms of the target repository.
By submitting a contribution, the contributor certifies that:

- They have the legal right to submit the code under the repository's license.
- The code does not infringe on any third-party intellectual property rights.
- The contribution complies with the repository's Developer Certificate of Origin (DCO) requirements, where
  applicable.

### 3. Review and Testing

AI-assisted contributions must meet the same quality bar as human-authored contributions:

- Code must be thoroughly reviewed by the contributor before submission.
- Code must be tested according to the project's testing requirements including device testing requirements where applicable.
- Contributors should not rely on AI tools as a substitute for understanding the codebase or the problem domain.

### 4. Enforcement

- Maintainers reserve the right to reject or request changes to any contribution that does not comply with this
  policy.
- Maintainers may ask contributors whether AI tools were used and request additional explanation or testing.
- Repeated violations of this policy may result in temporary or permanent restrictions on the contributor's
  ability to contribute to ODP repositories, in accordance with the
  [ODP Code of Conduct](https://github.com/OpenDevicePartnership/governance/blob/main/CODE-OF-CONDUCT.md).

### 5. Project-Specific Extensions

Individual ODP projects may adopt stricter AI policies that extend this organization-wide policy. For example,
a project may:

- Require additional testing for AI-assisted firmware contributions (as Patina does).
- Require contributors to demonstrate domain-specific expertise.
- Restrict the use of specific AI tools.

Project-specific policies must not be less restrictive than this organization-wide policy.

## Integration with Contribution Guidelines

A key question is how this policy should be surfaced to contributors. There are two primary options:

### Option A: Embed in each repository's `CONTRIBUTING.md` (Recommended)

Each ODP repository's `CONTRIBUTING.md` would include an "AI Policy" section (as Patina already does) that:

1. States the key rules directly in the contribution guide so contributors encounter them naturally.
2. Links back to this governance RFC (or a rendered version) as the authoritative source.

This is the approach Patina has already taken. It has the advantage of being immediately visible to contributors
at the point where they read the contribution guidelines. To maintain consistency, a standard paragraph could be
provided that repositories copy into their `CONTRIBUTING.md`:

```markdown
## AI Policy

This project follows the [ODP Organization-Wide AI Policy](https://github.com/OpenDevicePartnership/governance/blob/main/AI-POLICY.md).
Contributors using AI coding assistants must ensure they fully understand, review, and test all AI-assisted
code before submission. AI-generated contributions must comply with this project's licensing terms. See the
full policy for details.
```

Projects with stricter requirements (e.g., Patina) would add their additional rules below this standard
paragraph.

### Option B: Standalone governance document only

The policy lives solely as a document in the `governance` repository (e.g., `AI-POLICY.md`) and is referenced
from the ODP-wide `CONTRIBUTING.md` or `README.md`. Individual repositories are not required to duplicate the
text.

- **Pro**: Single source of truth; easier to update.
- **Con**: Contributors may not discover the policy unless they actively look for it. New contributors who only
  read a project's `CONTRIBUTING.md` could miss it entirely.

### Recommendation

**Option A** provides the best discoverability: the policy is surfaced in the contribution guide where
contributors naturally look. A standalone `AI-POLICY.md` in the governance repository should also be maintained
as the canonical, detailed reference that individual repositories link to.

## Rust Code Design

Not applicable.

## Guide-Level Explanation

Not applicable.
