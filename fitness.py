from datetime import datetime, timedelta
from typing import List

from chromosome import ALL_MATCHES, ALL_SLOTS

BASE_DATE = datetime(2025, 1, 1, 15, 0)
HOURS_PER_TIMESLOT = 2
DAYS_PER_ROUND = 1


def fitness(individual: List[int]) -> float:
    penalty = 0

    team_round_time = {}
    venue_round_time = {}
    match_seen = set()

    assigned = []

    for i, slot_id in enumerate(individual):
        home, away = ALL_MATCHES[i]
        slot = ALL_SLOTS[slot_id]

        r = slot["RoundIndex"]
        t = slot["TimeIndex"]
        v = slot["VenueID"]
        dt = slot["DateTime"]

        assigned.append((r, dt))

        for team in (home, away):
            key = (team, r, t)
            team_round_time[key] = team_round_time.get(key, 0) + 1
            if team_round_time[key] > 1:
                penalty += 10000

        key_v = (v, r, t)
        venue_round_time[key_v] = venue_round_time.get(key_v, 0) + 1
        if venue_round_time[key_v] > 1:
            penalty += 10000


        m = (home, away)
        if m in match_seen:
            penalty += 20000
        match_seen.add(m)

    n = len(assigned)
    for i in range(n):
        for j in range(i+1, n):
            r1, dt1 = assigned[i]
            r2, dt2 = assigned[j]

            if r1 < r2 and dt1 >= dt2:
                penalty += 50000

    return -penalty
