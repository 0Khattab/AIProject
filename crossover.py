import random
from typing import List


def partial_order_crossover(parent1, parent2):
    size = len(parent1)
    child = [-1] * size

    start = random.randint(0, size - 2)
    end = random.randint(start + 1, size - 1)

    subset = set(parent1[start:end + 1])
    for i in range(start, end + 1):
        child[i] = parent1[i]

    p2_idx = 0
    for i in range(size):
        if child[i] == -1:
            while parent2[p2_idx] in subset:
                p2_idx += 1
            child[i] = parent2[p2_idx]
            p2_idx += 1

    return child


def cycle_crossover_corrected(parent1: List[int], parent2: List[int]):

    size = len(parent1)
    child = [-1] * size
    visited = [False] * size
    take_from_parent1 = True

    while not all(visited):
        try:
            start_idx = visited.index(False)
        except ValueError:
            break

        current_idx = start_idx
        while True:
            if take_from_parent1:
                child[current_idx] = parent1[current_idx]
            else:
                child[current_idx] = parent2[current_idx]

            visited[current_idx] = True

            if take_from_parent1:
                value_to_find = parent2[current_idx]
                try:
                    next_idx = parent1.index(value_to_find)
                except ValueError:
                    break
            else:
                value_to_find = parent1[current_idx]
                try:
                    next_idx = parent2.index(value_to_find)
                except ValueError:
                    break
            if next_idx == start_idx:
                break
            current_idx = next_idx
        take_from_parent1 = not take_from_parent1

    return child