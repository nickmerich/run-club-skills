---
name: member-lifecycle
description: Classifies every named run club participant into a lifecycle state (Prospect, First-Timer, Regular, Bringer, Anchor, Drifter, Paused, Released) from check-ins and known signals, detects weekly transitions, and outputs one named action per person for the week. Use for "who should I message this week", "member states", "run the growth loop", "turn regulars into bringers", or a weekly people review.
metadata:
  library: run-club-skills
  version: "1.0"
---

# Member Lifecycle

## States (define them, then never fudge them)

| State | Rule (adapt numbers to your club) | This week's action |
|-------|-----------------------------------|--------------------|
| Prospect | Interested, never checked in | Personal invite with the promise and a buddy offer |
| First-Timer | 1 check-in | 24-hour follow-up, day-before nudge (`newcomer-welcome`) |
| Regular | 3+ check-ins in the last 8 weeks | Light touch; ask to buddy once they've done 3 in a row |
| Bringer | Brought at least one person who checked in | Thank them; ask about their next invite (`bring-a-friend`) |
| Anchor | Regular for months, helps lead | Involve in decisions; candidate captain |
| Drifter | 2+ prior check-ins, then 3+ missed runs in a row, no known reason | `drifter-save` |
| Paused | Known reason: injury, new baby, travel, life | Care only, no asks; check back on a date |
| Released | Said no, or 2 unanswered save messages | No more outreach; always welcome back |

Membership definition to write down: a member is someone who has checked in at least once. Strava club members, followers, and email subscribers are separate counts.

## Rules

- Missing check-in data is **unknown**. Don't mark someone a drifter because the check-in sheet was skipped that week.
- Paused is not Drifter. Injury and life events get care, not "we miss you."
- One action per person per week. Most people need nothing.
- Keep the list private. Never post states publicly.

## Weekly run

1. Run `scripts/scorecard.py` on the check-in export.
2. Assign states; list transitions since last week (new Regulars, new Drifters, returns).
3. Output a named action list with sender and channel.

```
[Name] Regular → Drifter (last: Sep 26, 5 total) → drifter-save, sender: [their buddy]
[Name] First-Timer (Oct 17) → 24h follow-up, sender: [leader]
[Name] Regular, 3 in a row → buddy ask
```
