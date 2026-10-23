---
name: attendance-and-scorecard
description: Sets up check-ins as a run club's source of truth for attendance and produces an honest weekly scorecard (unique runners, total visits, first-timers, two-week return rate, drifters, milestones) from a check-in export using a deterministic script. Use for "how many people came", "weekly numbers", "set up check-ins", "what's our retention", "Monday brief", or reconciling Strava, RSVPs, and real attendance.
metadata:
  library: run-club-skills
  version: "1.0"
---

# Attendance and Scorecard

## Check-ins are the source of truth

- QR code at the meeting spot or a leader with a phone list. Takes 10 seconds.
- Capture: date, person id (email or a stable id), first-time flag, optional "who invited you".
- RSVPs are intent. Strava club members, followers, and subscribers are audience. Only check-ins are attendance.
- If check-ins were skipped one week, that week is **unknown**. Note it; don't fill it from memory.

## Definitions (write them once, use them forever)

| Metric | Definition |
|--------|-----------|
| Visits | Total check-ins in the period |
| Unique runners | Distinct people with 1+ check-in in the period |
| First-timers | People whose first-ever check-in is in the period |
| Two-week return rate | Of first-timers at least 14 days ago, share who checked in again within 14 days |
| Drifters | 2+ lifetime check-ins, missed the last 3+ runs in a row |
| Milestones | People whose lifetime count crossed 5, 10, 25, 50, or 100 this week |

## Run it

```bash
python3 scripts/scorecard.py checkins.csv --as-of YYYY-MM-DD
```

CSV columns: `date,person_id,first_time` (first_time is `1` or `0`; if missing, first ever check-in is used).

## Monday brief

Lead with one real moment (with permission), then the numbers, then this week's constraint and named actions (`run-club-operator`). Keep personal data out of anything public.

## Privacy

Store check-ins somewhere access-controlled. Don't publish personal counts or names without permission. Delete what you don't need.
