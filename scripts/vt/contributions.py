"""Refetch monthly contribution counts from GitHub with the gh CLI."""
import collections
import json
import subprocess

from vt.hero import CONTRIB


def refresh_contributions():
    query = "{viewer{contributionsCollection{contributionCalendar{totalContributions weeks{contributionDays{date contributionCount}}}}}}"
    raw = subprocess.run(["gh", "api", "graphql", "-f", f"query={query}"], capture_output=True, text=True, check=True).stdout
    cal = json.loads(raw)["data"]["viewer"]["contributionsCollection"]["contributionCalendar"]
    months = collections.OrderedDict()
    for week in cal["weeks"]:
        for day in week["contributionDays"]:
            months[day["date"][:7]] = months.get(day["date"][:7], 0) + day["contributionCount"]
    CONTRIB.write_text(json.dumps({"total": cal["totalContributions"], "months": months}, indent=2) + "\n")
