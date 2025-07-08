# Open Device Partnership RFC Process

Open Device Partnership (ODP) uses a Request for Comments (RFC) process to propose, discuss, and evolve significant changes to the ODP ecosystem. This includes governance changes, notable technical decisions, alignment with standards, API changes, engineering processes, and other organizational decisions that benefit from broad community input.

## Table of Contents

- [Opening](#opening)
- [When you need to follow this process](#when-you-need-to-follow-this-process)
- [Before creating an RFC](#before-creating-an-rfc)
- [What the process is](#what-the-process-is)
- [The RFC life cycle](#the-rfc-life-cycle)
- [Implementing and maintaining an RFC](#implementing-and-maintaining-an-rfc)
- [Why we have this process](#why-we-have-this-process)

## Opening

Changes to the ODP ecosystem are proposed and discussed via pull requests to the RFC folder of this [Governance repository](https://github.com/opendevicepartnership/governance/).

## When you need to follow this process

You need to submit an RFC if you are proposing:

- New projects to be managed under ODP governance
- Changes to core governance, working group structure, or project policies
- New features or major architectural changes to ODP software or specifications
- New or significantly modified public APIs, protocols, or data formats
- Deprecation of existing features, interfaces, or services
- Major tooling changes or infrastructure upgrades that impact the community

Small bug fixes, documentation updates, or minor enhancements can be proposed via normal contribution workflows and do not require an RFC.

## Before creating an RFC

It's best to first engage the community via chat in the ODP:

- [Zulip Server](https://opendevicepartnership.zulipchat.com/)
- [GitHub Discussions](https://github.com/orgs/OpenDevicePartnership/discussions)

This will help you refine your thinking and build consensus before you invest effort into writing a full RFC.

## What the process is

1. **Fork** the [ODP Governance repository](https://github.com/opendevicepartnership/governance)
2. **Create a new branch** for your RFC
3. **Copy** the template from `rfc/0000-template.md` to `rfc/text/0000-my-feature.md` (change "my-feature" to describe the RFC).  Don't assign an RFC number yet; This will be filled in later using the RFC PR number if the RFC is accepted.
4.  **Fill in** the RFC with the details: RFCs are usually poorly received if they lack clear motivation, show little understanding of the design’s impact, or ignore drawbacks and alternatives.
5. Submit a **pull request** (PR) with your RFC
6. The PR will be discussed, reviewed, and may be iteratively updated
7. Once there is consensus and approval, the RFC will be **merged** and assigned an official number

## The RFC life cycle

Each RFC goes through these stages:

- **Draft**: The initial state when a PR is opened. Note that the draft state refers to the RFC and not the PR (it should be submitted as a normal PR). The community and relevant steering committee(s) provide feedback.
- **Final Comment Period (FCP)**: Once there is rough consensus, an FCP of **7–10** weekdays starts. During this time, final objections can be raised.
- **Merged**: After FCP with no blocking concerns, the RFC is merged and becomes official.
- **Postponed**: RFCs may be deferred due to lack of clarity, priority, or readiness.
- **Rejected**: With strong reasoning and community consensus, RFCs can be declined.

## Implementing and maintaining an RFC

Once accepted:

- The implementation is tracked through linked GitHub work items or repositories as relevant.
- Any changes during implementation that deviate from the RFC must go through a **follow-up RFC** or an **amendment** process.
- An RFC can be **revised** in-place via a new RFC that supersedes or modifies the previous one.

## Why we have this process

The ODP RFC process serves to:

- Empower contributors and stakeholders to shape the direction of ODP
- Provide a consistent and transparent decision-making path
- Encourage open design and community participation
- Document major decisions and their motivations
