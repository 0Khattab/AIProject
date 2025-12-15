from EncodingAndInit import *


def check_rest_time(schedule: List[Dict]) -> float:

    ideal_rest_seconds = 7 * 24 * 3600
    total_diff = 0.0

    team_schedule: Dict[int, List[datetime]] = {team: [] for team in range(1, NUM_TEAMS + 1)}

    for match in schedule:
        team_schedule[match['Home']].append(match['DateTime'])
        team_schedule[match['Away']].append(match['DateTime'])

    for team in team_schedule:
        schedule_dates = sorted(team_schedule[team])

        if len(schedule_dates) > 1:
            for i in range(1, len(schedule_dates)):
                time_diff = schedule_dates[i] - schedule_dates[i - 1]
                rest_seconds = time_diff.total_seconds()

                total_diff += abs(rest_seconds - ideal_rest_seconds) / 3600

    return total_diff / NUM_TEAMS