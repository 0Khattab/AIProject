from typing import Dict, List


def check_double_play_per_round(schedule: List[Dict]) -> int:

    penalty = 0
    round_teams: Dict[int, set] = {}

    for match in schedule:
        round_idx = match['RoundIndex']
        home, away = match['Home'], match['Away']

        if round_idx not in round_teams:
            round_teams[round_idx] = set()

        if home in round_teams[round_idx]:
            penalty += 1
        if away in round_teams[round_idx]:
            penalty += 1
        round_teams[round_idx].add(home)
        round_teams[round_idx].add(away)

    return penalty