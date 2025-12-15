from EncodingAndInit import ALL_SLOTS, ALL_MATCHES
from typing import List, Set, Dict
import random


def repair_hard_constraints(chromosome: List[int]) -> List[int]:
    used_slots_set = set(chromosome)
    num_total_slots = len(ALL_SLOTS)

    unused_slots = [s for s in range(num_total_slots) if s not in used_slots_set]
    random.shuffle(unused_slots)

    new_chromosome = list(chromosome)

    round_teams: Dict[int, Set[int]] = {}

    for i in range(len(new_chromosome)):
        slot_id = new_chromosome[i]

        home, away = ALL_MATCHES[i]

        slot_info = ALL_SLOTS[slot_id]
        current_round = slot_info['RoundIndex']

        if current_round not in round_teams:
            round_teams[current_round] = set()

        has_conflict = (home in round_teams[current_round]) or (away in round_teams[current_round])

        if not has_conflict:
            round_teams[current_round].add(home)
            round_teams[current_round].add(away)
        else:
            repaired = False

            for u_idx, u_slot_id in enumerate(unused_slots):
                u_slot_info = ALL_SLOTS[u_slot_id]
                u_round = u_slot_info['RoundIndex']

                u_teams_in_round = round_teams.get(u_round, set())

                if home not in u_teams_in_round and away not in u_teams_in_round:
                    new_chromosome[i] = u_slot_id

                    if u_round not in round_teams:
                        round_teams[u_round] = set()
                    round_teams[u_round].add(home)
                    round_teams[u_round].add(away)

                    unused_slots.pop(u_idx)
                    unused_slots.append(slot_id)
                    repaired = True
                    break

            if not repaired:
                pass

    return new_chromosome
