#!/usr/bin/env python3
"""Weekly run club scorecard from a check-in export.

Usage: python3 scorecard.py checkins.csv [--as-of YYYY-MM-DD] [--weeks 8]

CSV columns: date,person_id[,first_time]
Run dates are the distinct dates in the file. A week with no rows is treated as
"no run recorded", which is UNKNOWN, not zero attendance.
"""
import argparse
import csv
import datetime as dt
import sys
from collections import defaultdict

TIERS = [5, 10, 25, 50, 100]


def parse(path):
    try:
        f = open(path, newline="")
    except FileNotFoundError:
        sys.exit(f"File not found: {path}")
    with f:
        r = csv.DictReader(f)
        if not r.fieldnames or not {"date", "person_id"}.issubset(r.fieldnames):
            sys.exit("CSV needs columns: date, person_id (optional: first_time)")
        rows = []
        for i, row in enumerate(r, start=2):
            try:
                d = dt.date.fromisoformat(row["date"].strip())
            except ValueError:
                sys.exit(f"Row {i}: date must be YYYY-MM-DD")
            pid = row["person_id"].strip()
            if pid:
                rows.append((d, pid))
    return sorted(set(rows))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--as-of", default=dt.date.today().isoformat())
    ap.add_argument("--weeks", type=int, default=8, help="lookback window")
    a = ap.parse_args()
    as_of = dt.date.fromisoformat(a.as_of)
    rows = [(d, p) for d, p in parse(a.csv) if d <= as_of]
    if not rows:
        sys.exit("No check-ins on or before --as-of")

    by_person = defaultdict(list)
    for d, p in rows:
        by_person[p].append(d)
    run_dates = sorted({d for d, _ in rows})
    week_start = as_of - dt.timedelta(days=6)
    window_start = as_of - dt.timedelta(weeks=a.weeks)

    week = [(d, p) for d, p in rows if d >= week_start]
    window = [(d, p) for d, p in rows if d > window_start]
    firsts = {p: min(ds) for p, ds in by_person.items()}

    print(f"Scorecard as of {as_of} (last {a.weeks} weeks unless noted)")
    print(f"This week: {len(week)} check-ins, {len({p for _, p in week})} people, "
          f"{sum(1 for p in {p for _, p in week} if firsts[p] >= week_start)} first-timers")
    print(f"Window: {len(window)} visits, {len({p for _, p in window})} unique runners")
    print(f"Lifetime: {len(rows)} visits, {len(by_person)} unique runners")

    eligible = [p for p, f in firsts.items() if window_start < f <= as_of - dt.timedelta(days=14)]
    returned = [p for p in eligible
                if any(firsts[p] < d <= firsts[p] + dt.timedelta(days=14) for d in by_person[p])]
    if eligible:
        print(f"Two-week return rate: {len(returned)}/{len(eligible)} = {len(returned)/len(eligible):.0%}")
    else:
        print("Two-week return rate: not enough data")

    last3 = run_dates[-3:]
    drifters = [p for p, ds in by_person.items()
                if len(ds) >= 2 and len(last3) == 3 and not set(ds) & set(last3)]
    print(f"\nDrifters (2+ visits, missed last 3 recorded runs): {len(drifters)}")
    for p in sorted(drifters, key=lambda x: max(by_person[x]), reverse=True):
        print(f"  {p}: {len(by_person[p])} visits, last {max(by_person[p])}")

    print("\nMilestones crossed this week:")
    hit = False
    for p, ds in by_person.items():
        before = sum(1 for d in ds if d < week_start)
        now = len(ds)
        for t in TIERS:
            if before < t <= now:
                print(f"  {p}: {t}")
                hit = True
    if not hit:
        print("  none")

    gaps = []
    d = run_dates[0]
    while d <= as_of:
        if not any(d <= r < d + dt.timedelta(days=7) for r in run_dates):
            gaps.append(d)
        d += dt.timedelta(days=7)
    if gaps:
        print(f"\nWeeks with no check-ins recorded (UNKNOWN, not zero): {len(gaps)}")


if __name__ == "__main__":
    main()
