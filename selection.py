import random

def tournament_select(population, k=5):
    success = random.sample(population, min(k, len(population)))
    # for s in success:
    #     print(s)
    best = max(success, key=lambda p: p['fitness'])
    # print(best)
    return best