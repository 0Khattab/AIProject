from EncodingAndInit import *
from detiled_schedule import get_detailed_schedule
from doubleTeamPerRound import check_double_play_per_round
from homeAwaySeq import check_home_away_sequence
from restTime import check_rest_time

W_H = 1000
W_S1 = 50
W_S2 = 100
NUM_MATCHES = 2 * (NUM_TEAMS - 1) * (NUM_TEAMS // 2)


def calculate_fitness(chromosome: List[int]):

    schedule = get_detailed_schedule(chromosome)
    P_H1 = check_double_play_per_round(schedule)
    P_H3 = 0

    P_S1 = check_rest_time(schedule)
    P_S2 = check_home_away_sequence(schedule)

    Total_Penalty = (
            W_H * (P_H1 + P_H3) +
            W_S1 * P_S1 +
            W_S2 * P_S2
    )

    fitness = 1 / (1 + Total_Penalty)
    return fitness, Total_Penalty , P_H1, P_S1, P_S2