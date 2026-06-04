# Steering Committee Meetings

This directory holds the ODP Steering Committee meeting agendas and the tooling that generates them. The meeting
process itself (how agendas are proposed, approved, finalized, and recorded) is defined in [STEERING-COMMITTEE-MEETING.md](../STEERING-COMMITTEE-MEETING.md).

Note: This process is automated on GitHub. In the normal case, no one is expected to run the agenda generator script
or create agenda files manually.

## Contents

- `agenda-template.md` - The reference agenda template used by automation to create new agendas and serves as a general
  reference for the agenda document structure.
- `YYYY-MM-DD.md` - A generated agenda for a specific meeting date.
  - These files can be modified with pull requests while in "Draft" status.
- `scripts/` - The agenda generator script and its configuration.

## Generating an agenda

The generator fills the template's meeting details from `scripts/config.toml` and determines the meeting date from the
recurrence rule in that file.

Steps to run the agenda generator script manually:

```sh
# Note: Requires Python 3.11+.
# Install dependencies once.
py -3 -m pip install -r scripts/requirements.txt

# Create the agenda for the next scheduled meeting.
py -3 scripts/generate_agenda.py

# Other options: Such as a specific month or an explicit date.
py -3 scripts/generate_agenda.py --month 2026-08
py -3 scripts/generate_agenda.py --date 2026-08-04
```

## Automation

The `Create Meeting Agenda` workflow ([.github/workflows/create-meeting-agenda.yml](../.github/workflows/create-meeting-agenda.yml))
runs nightly. It calls `generate_agenda.py --if-due`, which creates the next agenda only once it has been at least two
days since the previous meeting, then opens a pull request. It can also be triggered manually on GitHub if needed.
