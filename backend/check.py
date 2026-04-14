import schedule
import collections

sched = [m for m in schedule.IPL_2026_SCHEDULE if m['team1'] != 'TBD']

print("Teams playing themselves:")
for m in sched:
    if m['team1'] == m['team2']:
        print(m)

team_dates = collections.defaultdict(list)
for m in sched:
    team_dates[m['team1']].append(m['date'])
    team_dates[m['team2']].append(m['date'])

print("\nTeams playing multiple times a day:")
for team, dates in team_dates.items():
    if len(dates) != len(set(dates)):
        print(f"{team} has duplicates: {[item for item, count in collections.Counter(dates).items() if count > 1]}")

print("\nTotal matches per team:")
for team, dates in team_dates.items():
    print(f"{team}: {len(dates)}")
