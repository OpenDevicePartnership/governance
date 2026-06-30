#!/usr/bin/env python3
"""Generate an ODP Steering Committee meeting agenda from the template.

The script fills in the relatively stable meeting details (time, chair, and
location) from a TOML configuration file and computes the meeting date from a
recurring "Nth weekday of the month" pattern, also described in the config.

It renders ``agenda-template.md`` into a dated ``YYYY-MM-DD.md`` file, removing
some content so the generated agenda only contains the content contributors
edit.

Usage examples::

    py -3 generate_agenda.py                              # next meeting from today
    py -3 generate_agenda.py --month 2026-08              # meeting in a specific month
    py -3 generate_agenda.py --date 2026-08-04
    py -3 generate_agenda.py --if-due                     # create only when due
    py -3 generate_agenda.py --if-due --ignore-lead-time  # manual dispatch
"""

from __future__ import annotations

import argparse
import calendar
import os
import re
import tomllib
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

try:
    from babel.dates import get_timezone_name
except ModuleNotFoundError as exc:  # pragma: no cover - dependency guard
    raise SystemExit(
        "This script requires the 'babel' package. Install dependencies "
        "with: py -3 -m pip install -r "
        "steering-committee-meetings/scripts/requirements.txt"
    ) from exc

SCRIPT_DIR = Path(__file__).resolve().parent
MEETINGS_DIR = SCRIPT_DIR.parent
DEFAULT_CONFIG = SCRIPT_DIR / "config.toml"
DEFAULT_TEMPLATE = MEETINGS_DIR / "agenda-template.md"

WEEKDAYS = {
    name.lower(): index for index, name in enumerate(calendar.day_name)
}
ORDINALS = {"first": 0, "second": 1, "third": 2, "fourth": 3, "fifth": 4}
COMMENT_PATTERN = re.compile(r"<!--.*?-->", re.DOTALL)

# How many days after a meeting the next agenda should be created. The nightly
# --if-due run waits this long so the just-completed meeting's minutes can be
# added before the next agenda appears.
AGENDA_LEAD_DAYS = 2

# Status value (compared case-insensitively) that marks a meeting's agenda as
# canceled. A canceled meeting's agenda file remains in the repository, so
# --if-due must look past it when deciding whether the next agenda is missing.
CANCELED_STATUS = "canceled"


def load_config(path: Path) -> dict:
    """Load and minimally validate the meeting configuration."""
    if not path.exists():
        raise FileNotFoundError(
            f"Configuration file not found: {path}\n"
            "Create a 'config.toml' with [meeting] and [recurrence] sections "
            "(see steering-committee-meetings/README.md)."
        )
    with path.open("rb") as handle:
        config = tomllib.load(handle)

    for section in ("meeting", "recurrence"):
        if section not in config:
            raise ValueError(f"Missing required [{section}] section in {path}")
    return config


def nth_weekday_of_month(
    year: int, month: int, weekday: int, ordinal: str
) -> date:
    """Return the date of the Nth (or last) weekday in the given month."""
    matching = [
        week[weekday]
        for week in calendar.monthcalendar(year, month)
        if week[weekday] != 0
    ]
    if ordinal == "last":
        return date(year, month, matching[-1])

    index = ORDINALS[ordinal]
    if index >= len(matching):
        raise ValueError(
            f"There is no '{ordinal}' {calendar.day_name[weekday]} in "
            f"{calendar.month_name[month]} {year}."
        )
    return date(year, month, matching[index])


def meeting_date_for_month(recurrence: dict, year: int, month: int) -> date:
    """Compute the meeting date within a month from the recurrence rule."""
    weekday_name = str(recurrence["weekday"]).lower()
    ordinal = str(recurrence["ordinal"]).lower()

    if weekday_name not in WEEKDAYS:
        raise ValueError(
            f"Invalid recurrence weekday: {recurrence['weekday']!r}"
        )
    if ordinal != "last" and ordinal not in ORDINALS:
        raise ValueError(
            f"Invalid recurrence ordinal: {recurrence['ordinal']!r}"
        )

    return nth_weekday_of_month(year, month, WEEKDAYS[weekday_name], ordinal)


def next_meeting_date(recurrence: dict, today: date) -> date:
    """Find the next meeting date on or after ``today``."""
    candidate = meeting_date_for_month(recurrence, today.year, today.month)
    if candidate >= today:
        return candidate

    # This month's meeting has passed, so advance to the next month.
    if today.month == 12:
        year, month = today.year + 1, 1
    else:
        year, month = today.year, today.month + 1
    return meeting_date_for_month(recurrence, year, month)


def meeting_after(recurrence: dict, meeting_day: date) -> date:
    """Return the first meeting date strictly after ``meeting_day``."""
    return next_meeting_date(recurrence, meeting_day + timedelta(days=1))


def last_meeting_date(recurrence: dict, today: date) -> date:
    """Find the most recent meeting date on or before ``today``."""
    candidate = meeting_date_for_month(recurrence, today.year, today.month)
    if candidate <= today:
        return candidate

    # This month's meeting has not happened yet, so fall back to last month.
    if today.month == 1:
        year, month = today.year - 1, 12
    else:
        year, month = today.year, today.month - 1
    return meeting_date_for_month(recurrence, year, month)


def format_time_label(value: str) -> str:
    """Convert a 24-hour ``HH:MM`` string to a 12-hour label with am/pm."""
    parsed = datetime.strptime(value, "%H:%M")
    label = parsed.strftime("%I:%M %p")  # e.g. "09:00 AM"
    return label[1:] if label.startswith("0") else label


def format_meeting_time(meeting: dict, meeting_day: date) -> str:
    """Build the time field with am/pm times and a spelled-out timezone."""
    tz_key = str(meeting["timezone"])
    try:
        tzinfo = ZoneInfo(tz_key)
    except ZoneInfoNotFoundError as exc:
        raise ValueError(
            f"Unknown timezone {tz_key!r}. Use an IANA name such as "
            "'America/Los_Angeles'. On Windows, ensure the 'tzdata' "
            "package is installed."
        ) from exc

    start_time = datetime.strptime(meeting["time_start"], "%H:%M").time()
    start_dt = datetime.combine(meeting_day, start_time, tzinfo=tzinfo)
    # Resolving the name against the concrete date yields the correct
    # daylight/standard variant (for example "Pacific Daylight Time").
    tz_name = get_timezone_name(start_dt, width="long", locale="en_US")

    start_label = format_time_label(meeting["time_start"])
    end_label = format_time_label(meeting["time_end"])
    return f"{start_label} \u2013 {end_label} {tz_name}"


def format_location(value: str) -> str:
    """Wrap a join URL in an autolink so markdown linters do not flag it."""
    value = value.strip()
    if value.startswith(("http://", "https://")):
        return f"<{value}>"
    return value


def build_context(config: dict, meeting_day: date) -> dict[str, str]:
    """Assemble the metadata values that replace the template placeholders."""
    meeting = config["meeting"]
    chair = f"{meeting['chair_name']} (GitHub: @{meeting['chair_github']})"
    return {
        "date": meeting_day.isoformat(),
        "time": format_meeting_time(meeting, meeting_day),
        "chair": chair,
        "location": format_location(str(meeting["location"])),
    }


def agenda_status(path: Path) -> str | None:
    """Return the status value recorded in an existing agenda file.

    Looks for the ``- **Status:**`` line, strips any trailing HTML comment,
    and returns the remaining text. Returns ``None`` if the file cannot be
    read or has no status line.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("- **Status:**"):
            value = stripped[len("- **Status:**"):]
            value = COMMENT_PATTERN.sub("", value)
            return value.strip()
    return None


def render_agenda(template_text: str, context: dict[str, str]) -> str:
    """Strip reference comments and fill in the meeting metadata."""
    text = COMMENT_PATTERN.sub("", template_text)

    replacements = {
        "# ODP Steering Committee Meeting":
            f"# ODP Steering Committee Meeting: {context['date']}",
        "- **Date:**": f"- **Date:** {context['date']}",
        "- **Time:**": f"- **Time:** {context['time']}",
        "- **Meeting Chair:**": f"- **Meeting Chair:** {context['chair']}",
        "- **Location / Join Link:**":
            f"- **Location / Join Link:** {context['location']}",
    }

    rendered_lines = []
    for line in text.splitlines():
        stripped = line.rstrip()
        for prefix, replacement in replacements.items():
            if stripped.startswith(prefix):
                stripped = replacement
                break
        rendered_lines.append(stripped)

    # Collapse the blank lines left behind by removed comments.
    body = re.sub(r"\n{3,}", "\n\n", "\n".join(rendered_lines))
    return body.strip() + "\n"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG,
        help="Path to the TOML config (default: config.toml).",
    )
    parser.add_argument(
        "--template",
        type=Path,
        default=DEFAULT_TEMPLATE,
        help="Path to the agenda template file.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=MEETINGS_DIR,
        help="Directory for the generated agenda file.",
    )

    date_group = parser.add_mutually_exclusive_group()
    date_group.add_argument(
        "--month",
        help="Target month as YYYY-MM. Applies the recurrence rule.",
    )
    date_group.add_argument(
        "--date",
        help="Explicit meeting date as YYYY-MM-DD. Overrides recurrence.",
    )

    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite the output file if it already exists.",
    )
    parser.add_argument(
        "--if-due",
        action="store_true",
        help=(
            "Create the next agenda only when it has been at least "
            f"{AGENDA_LEAD_DAYS} days since the last meeting and the file "
            "does not already exist. A canceled meeting's agenda is skipped "
            "so the following meeting's agenda is created. Intended for "
            "scheduled automation."
        ),
    )
    parser.add_argument(
        "--ignore-lead-time",
        action="store_true",
        help=(
            "With --if-due, skip the "
            f"{AGENDA_LEAD_DAYS}-day post-meeting wait. Intended for a "
            "manual workflow dispatch (for example, creating the next "
            "agenda right after a meeting is canceled)."
        ),
    )
    return parser.parse_args(argv)


def emit_github_output(**values: str) -> None:
    """Write ``key=value`` pairs to the GitHub Actions output file, if set."""
    output_file = os.environ.get("GITHUB_OUTPUT")
    if not output_file:
        return
    with open(output_file, "a", encoding="utf-8") as handle:
        for key, value in values.items():
            handle.write(f"{key}={value}\n")


def write_agenda(
    args: argparse.Namespace, config: dict, meeting_day: date
) -> Path:
    """Render and write the agenda file for ``meeting_day``."""
    context = build_context(config, meeting_day)
    template_text = args.template.read_text(encoding="utf-8")
    agenda_text = render_agenda(template_text, context)
    output_path = args.output_dir / f"{meeting_day.isoformat()}.md"
    output_path.write_text(agenda_text, encoding="utf-8")
    return output_path


def resolve_meeting_date(args: argparse.Namespace, recurrence: dict) -> date:
    if args.date:
        return date.fromisoformat(args.date)
    if args.month:
        year, month = (int(part) for part in args.month.split("-", 1))
        return meeting_date_for_month(recurrence, year, month)
    return next_meeting_date(recurrence, date.today())


def run_if_due(args: argparse.Namespace, config: dict) -> int:
    """Create the next agenda only when scheduling is due and it is missing."""
    recurrence = config["recurrence"]
    today = date.today()
    last_meeting = last_meeting_date(recurrence, today)
    days_since = (today - last_meeting).days

    # The lead-time wait keeps the nightly scheduled run from creating the next
    # agenda before the just-completed meeting's minutes can be added. A manual
    # dispatch (--ignore-lead-time) is an explicit request, so it skips the
    # wait. This might be used to create the next agenda immediately after
    # canceling a meeting.
    if not args.ignore_lead_time and days_since < AGENDA_LEAD_DAYS:
        print(
            f"Not due: the last meeting ({last_meeting.isoformat()}) was "
            f"{days_since} day(s) ago. Waiting for {AGENDA_LEAD_DAYS}."
        )
        emit_github_output(created="false")
        return 0

    meeting_day = next_meeting_date(recurrence, today)
    output_path = args.output_dir / f"{meeting_day.isoformat()}.md"

    # Skip past meetings that already have an agenda. A canceled meeting's
    # agenda file stays in the repository, so when the next scheduled meeting
    # is canceled this advances to the following meeting.
    while output_path.exists():
        status = agenda_status(output_path)
        if status is not None and status.lower() == CANCELED_STATUS:
            print(f"Skipping canceled meeting agenda: {output_path}")
            meeting_day = meeting_after(recurrence, meeting_day)
            output_path = args.output_dir / f"{meeting_day.isoformat()}.md"
            continue
        print(f"Agenda already exists: {output_path}")
        emit_github_output(
            created="false", meeting_date=meeting_day.isoformat()
        )
        return 0

    output_path = write_agenda(args, config, meeting_day)
    print(f"Created agenda: {output_path}")
    emit_github_output(
        created="true",
        meeting_date=meeting_day.isoformat(),
        agenda_file=str(output_path),
        chair_github=str(config["meeting"]["chair_github"]),
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    config = load_config(args.config)

    if args.if_due:
        return run_if_due(args, config)

    meeting_day = resolve_meeting_date(args, config["recurrence"])
    output_path = args.output_dir / f"{meeting_day.isoformat()}.md"
    if output_path.exists() and not args.force:
        print(
            f"Refusing to overwrite existing file: {output_path} "
            "(use --force)."
        )
        return 1

    output_path = write_agenda(args, config, meeting_day)
    print(f"Created agenda: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
