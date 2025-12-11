import random
from datetime import timedelta
from math import ceil
from typing import List, Dict, Tuple

from fitness import BASE_DATE, DAYS_PER_ROUND, HOURS_PER_TIMESLOT

NUM_TEAMS = 16
NUM_ROUNDS = 2 * (NUM_TEAMS - 1)
MATCHES_PER_ROUND = NUM_TEAMS // 2

NUM_VENUES = 3

def generate_all_matches() -> List[Tuple[int, int]]:
    matches = []
    teams = list(range(1, NUM_TEAMS + 1))
    for h in teams:
        for a in teams:
            if h != a:
                matches.append((h, a))
    return matches

TIME_SLOTS_PER_ROUND = ceil(MATCHES_PER_ROUND / 3)

def generate_all_slots() -> List[Dict]:
    slots = []
    slot_id = 0

    for r in range(1, NUM_ROUNDS + 1):
        round_start_time = BASE_DATE + timedelta(days=(r - 1) * DAYS_PER_ROUND)
        for t in range(1, TIME_SLOTS_PER_ROUND + 1):
            slot_time = round_start_time + timedelta(hours=(t - 1) * HOURS_PER_TIMESLOT)
            for v in range(1, NUM_VENUES + 1):
                slots.append({
                    "SlotID": slot_id,
                    "RoundIndex": r,
                    "TimeIndex": t,
                    "VenueID": v,
                    "DateTime": slot_time
                })
                slot_id += 1
    return slots

ALL_MATCHES = generate_all_matches()
ALL_SLOTS = generate_all_slots()

NUM_MATCHES = len(ALL_MATCHES)
NUM_SLOTS = len(ALL_SLOTS)

def create_individual() -> List[int]:
    slot_ids = list(range(NUM_SLOTS))
    random.shuffle(slot_ids)
    return slot_ids[:NUM_MATCHES]


