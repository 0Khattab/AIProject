from crossover import *
from EncodingAndInit import *
from calcFitness import *
from selection import *
from mutation import *
from repair import repair_hard_constraints

POP_SIZE = 120
GENERATIONS = 500
ELITISM_COUNT = 10
MUTATION_RATE = 0.1

POP = []
for i in range(POP_SIZE):
    ind = create_individual()
    POP.append(ind)

print(f"Starting GA with Population: {POP_SIZE}, Generations: {GENERATIONS}, Elitism: {ELITISM_COUNT}")

for gen in range(GENERATIONS):
    population_data = []
    for chrom in POP:
        fitness, penality, H, S1, S2 = calculate_fitness(chrom)
        population_data.append({
            'chromosome': chrom,
            'fitness': fitness,
            'penality': penality,
            'H': H,
            'S1': S1,
            'S2': S2
        })

    population_data.sort(key=lambda x: x['fitness'], reverse=True)

    best = population_data[0]
    print(
        f"Gen {gen + 1}: Best Fitness: {best['fitness']:.6f}, Penalty: {best['penality']}, H: {best['H']}, S1: {best['S1']}, S2: {best['S2']}")

    new_pop = [ind['chromosome'] for ind in population_data[:ELITISM_COUNT]]

    while len(new_pop) < POP_SIZE:
        parent1 = tournament_select(population_data)
        parent2 = tournament_select(population_data)

        child_chrom = partial_order_crossover(parent1['chromosome'], parent2['chromosome'])
        child_chrom = swap_mutation(child_chrom, MUTATION_RATE)
        child_chrom = repair_hard_constraints(child_chrom)  # Repair child

        new_pop.append(child_chrom)

    POP = new_pop

population_data = []
for chrom in POP:
    fitness, penality, H, S1, S2 = calculate_fitness(chrom)
    population_data.append({
        'chromosome': chrom,
        'fitness': fitness,
        'penality': penality,
        'H': H,
        'S1': S1,
        'S2': S2
    })
population_data.sort(key=lambda x: x['fitness'], reverse=True)
best = population_data[0]

print("\nFinal Best Solution:")
print(f"Fitness: {best['fitness']:.6f}")
print(f"Penalty: {best['penality']}")
print(f"H (Double Play/Round): {best['H']}")
print(f"S1 (Rest Time): {best['S1']}")
print(f"S2 (Home/Away Seq): {best['S2']}")
