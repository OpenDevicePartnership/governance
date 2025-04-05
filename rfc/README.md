# Open Device Partnership (ODP) RFC Process

ODP uses an RFC (Request for Comments) process to propose, discuss, and evolve significant changes to the Open Device Partnership's ecosystem. This includes notable technical decisions, governance changes, standards, APIs, and other organizational decisions that benefit from broad community input.

## Table of Contents

- [Opening](#opening)
- [When you need to follow this process](#when-you-need-to-follow-this-process)
- [Before creating an RFC](#before-creating-an-rfc)
- [What the process is](#what-the-process-is)
- [The RFC life cycle](#the-rfc-life-cycle)
- [Implementing and maintaining an RFC](#implementing-and-maintaining-an-rfc)
- [Why we have this process](#why-we-have-this-process)

## Opening

Changes to the ODP ecosystem are proposed and discussed via pull requests to this [RFCs repository](https://github.com/opendevicepartnership/governance/rfcs).

## When you need to follow this process

You need to submit an RFC if you are proposing:

- New projects to be managed under ODP governance.
- Changes to core governance, working group structure, or project policies.
- New features or major architectural changes to ODP software or specifications.
- New or significantly modified public APIs, protocols, or data formats.
- Deprecation of existing features, interfaces, or services.
- Major tooling changes or infrastructure upgrades that impact the community.

Small bug fixes, documentation updates, or minor enhancements can be proposed via normal contribution workflows and do not require an RFC.

## Before creating an RFC

It's best to first engage the community via:

- Chat in the ODP [Zulip Server](https://opendevicepartnership.zulipchat.com/) or our [Discord Server](https://discord.gg/cHGTwjgS)
- Open issues summarizing a problem and gathering input

This will help you refine your thinking and build consensus before you invest effort into writing a full RFC.

## What the process is

1. **Fork** the [ODP governance repository](https://github.com/opendevicepartnership/governance).
2. **Create a new branch** for your RFC.
3. **Copy** the template from `rfc/0000-template.md` to `rfc/text/0000-my-feature.md`, and fill in the details.
4. Submit a **pull request** (PR) with your RFC.
5. The PR will be discussed, reviewed, and may be iteratively updated.
6. Once there is consensus and approval, the RFC will be **merged** and assigned an official number.

## The RFC life cycle

Each RFC goes through these stages:

- **Draft**: The initial state when a PR is opened. The community and relevant teams provide feedback.
- **Final Comment Period (FCP)**: Once there is rough consensus, an FCP of 7–10 days starts. During this time, final objections can be raised.
- **Merged**: After FCP with no blocking concerns, the RFC is merged and becomes official.
- **Postponed**: RFCs may be deferred due to lack of clarity, priority, or readiness.
- **Rejected**: With strong reasoning and community consensus, RFCs can be declined.

## Implementing and maintaining an RFC

Once accepted:

- The implementation is tracked through linked issues or repositories.
- Any changes during implementation that deviate from the RFC must go through a **follow-up RFC** or an **amendment** process.
- An RFC can be **revised** in-place via a new RFC that supersedes or modifies the previous one.

## Why we have this process

The ODP RFC process serves to:

- Provide a consistent and transparent decision-making path.
- Encourage open design and community participation.
- Document major decisions and their motivations.
- Empower contributors and stakeholders to shape the direction of ODP.
