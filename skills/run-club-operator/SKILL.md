---
name: run-club-operator
description: Runs a run club week to week by finding the main constraint (not enough first-timers, first-timers not returning, regulars drifting, founder burnout, unsafe or unclear logistics) and routing to the right run club skill. Use for "what should I focus on this week", "how do I grow my run club", "Monday plan", "our club is stuck", or any broad run club operations question.
metadata:
  library: run-club-skills
  version: "1.0"
---

# Run Club Operator

## Step 1: Get the facts (label each VERIFIED, REPORTED, ASSUMPTION, UNKNOWN)

- Weekly run: day, time, meeting spot, routes, post-run spot
- Last 8 weeks of check-ins (or whatever attendance record exists)
- Who leads: founder, captains, buddies
- Channels: where people find the club and get updates
- What the founder can realistically give per week, in hours

If there are no check-ins, the first job is starting them (`attendance-and-scorecard`). You can't fix what you can't see.

## Step 2: Find the constraint

Run the scorecard, then pick **one**:

| Symptom | Constraint | Skill |
|---------|-----------|-------|
| Day, time, or spot changes often; people ask "when is it?" | Ritual | `founding-ritual` |
| Few first-timers | Discovery and invites | `bring-a-friend`, `local-partners`, `run-reports-and-stories` |
| First-timers come once and don't return | Welcome | `newcomer-welcome`, `buddy-system` |
| Regulars disappearing | Retention | `member-lifecycle`, `drifter-save` |
| Regulars stay but never bring anyone | Belonging | `milestones-and-streaks`, `bring-a-friend` |
| Founder is the only person who can run it | Capacity | `captains-and-succession` |
| Confusing routes, people dropped, weather surprises | Safety | `routes-and-safety` |

Fix the earliest broken stage first. More first-timers into a leaky welcome just leaks faster.

## Step 3: The weekly cadence

| Day | Do |
|-----|----|
| Mon | Scorecard. Lifecycle states. This week's named action list. |
| Tue | Post the run plan (date, time, spot, routes, weather plan). Buddy assignments for expected first-timers. |
| Wed to Thu | Drifter saves and bring-a-friend asks, one person at a time. |
| Fri | Reminder with weather status. Day-before nudges to first-timers from last week. |
| Run day | Ritual, welcome, check-ins, buddies, hang. |
| Run day + 1 | 24-hour first-timer follow-ups. Recap. |

## Step 4: Output

A short Monday brief:

```
This week's constraint: [one]
Why: [one line with numbers and labels]
Named actions:
- [Person] → [action] (owner, due)
One thing we're not doing this week: [the shiny distraction]
```

Keep it small. One constraint, five to ten named actions, done by the owner who has time.
