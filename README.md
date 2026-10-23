# Run Club Skills

An operating system for run clubs, written as agent skills. Lock the weekly ritual, welcome first-timers so they come back, keep track of people without losing the human part, and grow through members bringing friends instead of ads.

Built by [GRYT Run Club](https://grytrunclub.com) in Pittsburgh from running a free weekly Saturday run. Works for any club: neighborhood crews, brand-hosted runs, parent run clubs, campus clubs, run/walk groups.

**The idea in one line:** people don't come back for the workout. They come back because someone learned their name, ran with them, and noticed when they were gone.

## The skills

| # | Skill | Use it to |
|---|-------|-----------|
| 0 | [`run-club-operator`](skills/run-club-operator/SKILL.md) | Run the club week to week. Finds the main constraint and routes to the right skill. Start here. |
| 1 | [`founding-ritual`](skills/founding-ritual/SKILL.md) | Lock day, time, place, and the post-run hang. Audit drift. Handle cancellations. |
| 2 | [`newcomer-welcome`](skills/newcomer-welcome/SKILL.md) | The first 15 seconds, the first run, and the first week for every first-timer. |
| 3 | [`buddy-system`](skills/buddy-system/SKILL.md) | Build a pool of regulars who run with first-timers, and assign them each week. |
| 4 | [`member-lifecycle`](skills/member-lifecycle/SKILL.md) | Track each person's state (first-timer, regular, bringer, anchor, drifter, paused) and the one action each state needs. |
| 5 | [`drifter-save`](skills/drifter-save/SKILL.md) | Reach people who stopped showing up, with the right message from the right person, or let them go gracefully. |
| 6 | [`bring-a-friend`](skills/bring-a-friend/SKILL.md) | Make member invites part of the ritual and credit the people who bring others. |
| 7 | [`milestones-and-streaks`](skills/milestones-and-streaks/SKILL.md) | Recognize showing up (5, 10, 25, 50, 100 runs) in a way that never punishes a missed week. |
| 8 | [`attendance-and-scorecard`](skills/attendance-and-scorecard/SKILL.md) | Check-ins as the source of truth, honest metric definitions, and a weekly scorecard from a script. |
| 9 | [`routes-and-safety`](skills/routes-and-safety/SKILL.md) | Routes nobody gets dropped on, pace groups, sweeps, weather calls, waivers, insurance, permits. |
| 10 | [`run-reports-and-stories`](skills/run-reports-and-stories/SKILL.md) | Weekly recaps and member stories with real numbers and real consent. |
| 11 | [`local-partners`](skills/local-partners/SKILL.md) | Coffee shops, run stores, and local brands that make the run better and help fund it. |
| 12 | [`captains-and-succession`](skills/captains-and-succession/SKILL.md) | Stop being the single point of failure. Backup captains, role cards, founder time budget. |

## Quick start

```bash
cp -r skills/* ~/.claude/skills/     # or point any agent at skills/
python3 scripts/scorecard.py examples/checkins-sample.csv --as-of 2026-10-17
python3 scripts/validate_skills.py
```

`scorecard.py` reads a check-in export (date, person id, first-time flag) and prints unique runners, total visits, first-timers, two-week return rate, who's drifting, and who just crossed a milestone.

## Ground rules

1. **The ritual doesn't move.** Same day, same time, same place, same hang.
2. **Nobody runs alone their first time.** Nobody gets dropped, ever.
3. **Effort over pace.** Walkers, run/walkers, and first-timers are the club, not a side group.
4. **Counts stay honest.** Strava members, followers, RSVPs, check-ins, and unique runners are different numbers. Missing data is unknown, not proof someone quit. See [evidence rules](docs/evidence-rules.md).
5. **People's info is private.** Personal counts, health details, and contact info stay private. Names and photos go public only with permission.
6. **Grow through members first.** Organic invites beat ads for a community product.
7. **Safety calls are written down in advance** and nobody overrides them.

## Related

- [Artist-Led Athletic Events skills](https://github.com/nickmerich/artist-led-events-skills): when the weekly run becomes a produced event.

Not medical, legal, or insurance advice.
