from genetic_algorimth import GeneType, GeneticAlgorithm, CustomFitnessFunction


# Define parameters
population_size = 1000
chromosome_length = 5
mutation_rate = 0.1
generations = 1000
target = [1, 1, 1, 1, 1]
gene_ranges = [(0, 10), (0, 10), (0, 10), (0, 10), (0, 10)]  # Example gene ranges
gene_types = [GeneType.DISCRETE, GeneType.CONTINUOUS, GeneType.DISCRETE, GeneType.CONTINUOUS, GeneType.DISCRETE]

# Create genetic algorithm instance with custom fitness function and execute
fitness_function = CustomFitnessFunction(maximize=True)
ga = GeneticAlgorithm(
    population_size=population_size,
    chromosome_length=chromosome_length,
    mutation_rate=mutation_rate,
    generations=generations,
    target=target,
    gene_ranges=gene_ranges,
    gene_types=gene_types,
    fitness_function=fitness_function
)
best_individual, best_fitness = ga.evolve()
