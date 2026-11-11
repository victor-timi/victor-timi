"""Monthly contribution counts: read from data/, refetched from GitHub with the gh CLI."""
import collections
import json
import subprocess
from pathlib import Path

CONTRIB = Path(__file__).resolve().parents[2] / "data" / "contributions.json"
QUERY = ("query($login: String!) { user(login: $login) { contributionsCollection { contributionCalendar "
         "{ totalContributions weeks { contributionDays { date contributionCount } } } } } }")


def load_contributions():
    return json.loads(CONTRIB.read_text())


def refresh_contributions(login):
    raw = subprocess.run(["gh", "api", "graphql", "-f", f"query={QUERY}", "-f", f"login={login}"],
                         capture_output=True, text=True, check=True).stdout
    cal = json.loads(raw)["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    months = collections.OrderedDict()
    for week in cal["weeks"]:
        for day in week["contributionDays"]:
            months[day["date"][:7]] = months.get(day["date"][:7], 0) + day["contributionCount"]
    CONTRIB.write_text(json.dumps({"total": cal["totalContributions"], "months": months}, indent=2) + "\n")
