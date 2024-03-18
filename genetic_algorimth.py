import random
from enum import Enum


class FitnessFunction:
    def __init__(self, maximize=True):
        self.maximize = maximize

    def calculate_fitness(self, chromosome):
        raise NotImplementedError("Subclasses must implement calculate_fitness method.")


class GeneType(Enum):
    DISCRETE = 'discrete'
    CONTINUOUS = 'continuous'


class GeneticAlgorithm:
    def __init__(self, population_size, chromosome_length, mutation_rate, generations, target, gene_ranges, gene_types, fitness_function, stagnation_generations=100):
        self.population_size = population_size
        self.chromosome_length = chromosome_length
        self.mutation_rate = mutation_rate
        self.generations = generations
        self.target = target
        self.gene_ranges = gene_ranges
        self.gene_types = gene_types
        self.fitness_function = fitness_function
        self.stagnation_generations = stagnation_generations
        self.population = self._initialize_population()
        self.best_individual_id = None
        self.best_individual_fitness = float('-inf') if self.fitness_function.maximize else float('inf')
        self.best_fitness_over_last_x_generations = [self.best_individual_fitness] * self.stagnation_generations

    def _initialize_population(self):
        population = []
        for _ in range(self.population_size):
            chromosome = []
            for i in range(self.chromosome_length):
                gene_type = self.gene_types[i]
                gene_range = self.gene_ranges[i]
                if gene_type == GeneType.DISCRETE:
                    chromosome.append(random.randint(gene_range[0], gene_range[1]))
                elif gene_type == GeneType.CONTINUOUS:
                    chromosome.append(random.uniform(gene_range[0], gene_range[1]))
                else:
                    raise ValueError("Invalid gene type. Must be GeneType.DISCRETE or GeneType.CONTINUOUS.")
            population.append(chromosome)
        return population

    def selection(self):
        selection_size = 3
        selected = []
        for _ in range(len(self.population)):
            contestants = random.sample(self.population, selection_size)
            winner = max(contestants, key=self.fitness_function.calculate_fitness)
            selected.append(winner)
        return selected

    def crossover(self, parent1, parent2):
        crossover_point = random.randint(0, self.chromosome_length - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2

    def mutate(self, chromosome):
        mutated_chromosome = []
        for gene, gene_type, gene_range in zip(chromosome, self.gene_types, self.gene_ranges):
            if gene_type == GeneType.DISCRETE:
                if random.random() < self.mutation_rate:
                    mutated_gene = random.randint(gene_range[0], gene_range[1])
                else:
                    mutated_gene = gene
            elif gene_type == GeneType.CONTINUOUS:
                if random.random() < self.mutation_rate:
                    mutated_gene = random.uniform(gene_range[0], gene_range[1])
                else:
                    mutated_gene = gene
            else:
                raise ValueError("Invalid gene type. Must be GeneType.DISCRETE or GeneType.CONTINUOUS.")
            mutated_chromosome.append(mutated_gene)
        return mutated_chromosome

    def evolve(self):
        for generation in range(self.generations):
            selected_population = self.selection()
            new_population = []

            while len(new_population) < self.population_size:
                parent1, parent2 = random.sample(selected_population, 2)
                child1, child2 = self.crossover(parent1, parent2)
                new_population.extend([child1, child2])
            self.population = [self.mutate(chromosome) for chromosome in new_population]

            for index, individual in enumerate(self.population):
                individual_fitness = self.fitness_function.calculate_fitness(individual)
                if (self.fitness_function.maximize and individual_fitness > self.best_individual_fitness) or \
                   (not self.fitness_function.maximize and individual_fitness < self.best_individual_fitness):
                    self.best_individual_id = index
                    self.best_individual_fitness = individual_fitness

            self.best_fitness_over_last_x_generations.pop(0)
            self.best_fitness_over_last_x_generations.append(self.best_individual_fitness)

            if generation % 10 == 0:
                print(
                    f"Generation {generation + 1}: Best individual - {self.population[self.best_individual_id]}, Fitness - {self.best_individual_fitness}")
            if len(set(self.best_fitness_over_last_x_generations)) == 1:
                print(f"Evolution stopped early at generation {generation + 1} due to stagnation in fitness.")
                break

        final_best_individual = self.population[self.best_individual_id]
        print(f"Final result: Best individual - {final_best_individual}, Fitness - {self.best_individual_fitness}")
        return final_best_individual, self.best_individual_fitness


# Define custom fitness function
class CustomFitnessFunction(FitnessFunction):
    def calculate_fitness(self, chromosome):
        return sum(chromosome)
