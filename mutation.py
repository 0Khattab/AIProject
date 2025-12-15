import random
from typing import List


def swap_mutation(chromosome: List[int], mutation_rate: float) -> List[int]:

    mutated_chromosome = list(chromosome)
    size = len(mutated_chromosome)

    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(size), 2)
        mutated_chromosome[idx1], mutated_chromosome[idx2] = mutated_chromosome[idx2], mutated_chromosome[idx1]

    return mutated_chromosome