# RFC: AI Security Bug Reporting Policy

This RFC updates the Open Device Partnership Security Policy template to state that a security bug identified with the
help of an AI tool must be treated as public information once it is reported, since such bugs are readily accessible to
the public with the same tools.

## Change Log

This text can be modified over time. Add a change log entry for every change made to the RFC.

- 2026-08-07: Initial RFC created

## Motivation

AI tools are increasingly used to review code and find vulnerabilities, including in ODP repositories. When a bug is
found this way, treating it as something that can stay confidential under an embargo gives a false sense of safety,
since these bugs are often surfaced independently by more than one person around the same time. Several major open
source projects have reported a measurable rise in AI-assisted vulnerability research, such as
[curl](https://daniel.haxx.se/blog/2025/07/14/death-by-a-thousand-slops/) and the
[Linux kernel](https://docs.kernel.org/process/security-bugs.html#what-qualifies-as-a-security-bug). This RFC updates
the ODP security policy to clearly account for security bugs found with AI assistance in a way that such bugs can be
handled consistently and efficiently.

## Technology Background

AI coding and security research tools are now commonly used to scan source code and identify potential vulnerabilities.
ODP's organization-wide AI policy (RFC 0031) governs how AI tools are used to produce contributions. This RFC addresses
a related but separate topic of how a security bug is handled once AI assistance was used to find it.

## Goals

- Define clear policy for security bugs found with AI tools.
- Avoid embargo and delays for AI-discovered reports that are likely to surface elsewhere during the embargo period.
- Add the policy revision to the existing ODP SECURITY.md template.

## Requirements

- The template must state that AI-assisted findings are treated as public information.
- Reporters should still avoid posting public information to reproduce the bug, but be ready to offer it privately on
  request.

## Unresolved Questions

- None

## Prior Art

This is today's Open Device Partnership SECURITY.md file template:

```md
# Vulnerability Disclosure and Embargo Policy

The Open Device Partnership project welcomes the responsible disclosure of vulnerabilities.

## Initial Contact

All security bugs in Open Device Partnership should be reported to the security team. To do so, please reach out in the
form of a
[Github Security Advisory](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities).

You will be invited to join this private area to discuss specifics. Doing so allows us to start with a high level of
confidentiality and relax it if the issue is less critical, moving to work on the fix in the open.

Your initial contact will be acknowledged within 48 hours, and you’ll receive a more detailed response within 96 hours
indicating the next steps in handling your report.

After the initial reply to your report, the security team will endeavor to keep you informed of the progress being made
towards a fix and full announcement. As recommended by
[RFPolicy](https://dl.packetstormsecurity.net/papers/general/rfpolicy-2.0.txt), these updates will be sent at least
every five working days.

## Disclosure Policy

The Open Device Partnership project has a 5 step disclosure process.

1. Contact is established, a private channel created, and the security report is received and is assigned a primary
   handler. This person will coordinate the fix and release process.
2. The problem is confirmed and a list of all affected versions is determined. If an embargo is needed (see below),
   details of the embargo are decided.
3. Code is audited to find any potential similar problems.
4. Fixes are prepared for all releases which are still under maintenance. In case of embargo, these fixes are not
   committed to the public repository but rather held in a private fork pending the announcement.
5. The changes are pushed to the public repository and new builds are deployed.

This process can take some time, especially when coordination is required with maintainers of other projects. Every
effort will be made to handle the bug in as timely a manner as possible, however it is important that we follow the
release process above to ensure that the disclosure is handled in a consistent manner.

## Embargoes

While the Open Device Partnership project aims to follow the highest standards of transparency and openness, handling
some security issues may pose such an immediate threat to various stakeholders and require coordination between various
actors that it cannot be made immediately public.

In this case, security issues will fall under an embargo.

An embargo can be called for in various cases:

- when disclosing the issue without simultaneously providing a mitigation would seriously endanger users,
- when producing a fix requires coordinating between multiple actors (such as upstream or downstream/dependency
  projects), or simply
- when proper analysis of the issue and its ramifications demands time.

If we determine that an issue you report requires an embargo, we will discuss this with you and try to find a reasonable
expiry date (aka “embargo completion date”), as well as who should be included in the list of need-to-know people.
```

This policy update is inspired by the Linux kernel's security bug reporting process. It states that a bug found with AI
assistance must be treated as public, since such bugs tend to be found by multiple researchers around the same time, and
it asks reporters to avoid publishing a reproducer in that case. See the
[Linux kernel security bug documentation](https://docs.kernel.org/process/security-bugs.html#what-qualifies-as-a-security-bug)
for the full guidance.

## Proposed Policy

This is the ODP SECURITY.md template shown above with the new section added after Initial Contact:

```md
# Vulnerability Disclosure and Embargo Policy

The Open Device Partnership project welcomes the responsible disclosure of vulnerabilities.

## Initial Contact

All security bugs in Open Device Partnership should be reported to the security team. To do so, please reach out in the
form of a
[Github Security Advisory](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities).

You will be invited to join this private area to discuss specifics. Doing so allows us to start with a high level of
confidentiality and relax it if the issue is less critical, moving to work on the fix in the open.

Your initial contact will be acknowledged within 48 hours, and you’ll receive a more detailed response within 96 hours
indicating the next steps in handling your report.

After the initial reply to your report, the security team will endeavor to keep you informed of the progress being made
towards a fix and full announcement. As recommended by
[RFPolicy](https://dl.packetstormsecurity.net/papers/general/rfpolicy-2.0.txt), these updates will be sent at least
every five working days.

## Security Bugs Found Using AI

If an AI tool directly identifies a security vulnerability, the vulnerability must be treated as public information.
Even when there is reason to believe otherwise, industry experience has shown that vulnerabilities discovered through
AI-assisted analysis often surface independently across multiple parties within a short period of time. Delaying public
acknowledgment can increase the period during which others may be aware of the issue while no fix is available.

For this reason, do not publish detailed reproduction steps or exploit methods. When submitting a bug report, it is
acceptable to note that a reproduction method exists and be prepared to provide it privately upon request.

If the AI tool did not directly identify the vulnerability and was used only to generate reproduction code, test cases,
or supporting artifacts, the report should follow the project's standard vulnerability disclosure process.

## Disclosure Policy

The Open Device Partnership project has a 5 step disclosure process.

1. Contact is established, a private channel created, and the security report is received and is assigned a primary
   handler. This person will coordinate the fix and release process.
2. The problem is confirmed and a list of all affected versions is determined. If an embargo is needed (see below),
   details of the embargo are decided.
3. Code is audited to find any potential similar problems.
4. Fixes are prepared for all releases which are still under maintenance. In case of embargo, these fixes are not
   committed to the public repository but rather held in a private fork pending the announcement.
5. The changes are pushed to the public repository and new builds are deployed.

This process can take some time, especially when coordination is required with maintainers of other projects. Every
effort will be made to handle the bug in as timely a manner as possible, however it is important that we follow the
release process above to ensure that the disclosure is handled in a consistent manner.

## Embargoes

While the Open Device Partnership project aims to follow the highest standards of transparency and openness, handling
some security issues may pose such an immediate threat to various stakeholders and require coordination between various
actors that it cannot be made immediately public.

In this case, security issues will fall under an embargo.

An embargo can be called for in various cases:

- when disclosing the issue without simultaneously providing a mitigation would seriously endanger users,
- when producing a fix requires coordinating between multiple actors (such as upstream or downstream/dependency
  projects), or simply
- when proper analysis of the issue and its ramifications demands time.

If we determine that an issue you report requires an embargo, we will discuss this with you and try to find a reasonable
expiry date (aka “embargo completion date”), as well as who should be included in the list of need-to-know people.
```

## Alternatives

- Do not define a process for AI-assisted discovery.
  - This increases project overhead, risks delaying fixes, and prevents a broader audience from participating in
    reviewing and fixing the bug.

## Rust Code Design

N/A

## Guide-Level Explanation

N/A
