from EncodingAndInit import *


def check_home_away_sequence(schedule: List[Dict]) -> int:

    MAX_CONSECUTIVE = 3
    penalty = 0
    team_sequence: Dict[int, List[Tuple[str, datetime]]] = {team: [] for team in range(1, NUM_TEAMS + 1)}

    sorted_schedule = sorted(schedule, key=lambda x: x['DateTime'])

    for match in sorted_schedule:
        team_sequence[match['Home']].append(('H', match['DateTime']))
        team_sequence[match['Away']].append(('A', match['DateTime']))

    for team in team_sequence:
        sequence = sorted(team_sequence[team], key=lambda x: x[1])

        current_streak_status = None
        current_streak_length = 0

        for status, date in sequence:
            if status == current_streak_status:
                current_streak_length += 1
            else:
                if current_streak_length > MAX_CONSECUTIVE:
                    penalty += (current_streak_length - MAX_CONSECUTIVE)

                current_streak_status = status
                current_streak_length = 1

        if current_streak_length > MAX_CONSECUTIVE:
            penalty += (current_streak_length - MAX_CONSECUTIVE)

    return penalty