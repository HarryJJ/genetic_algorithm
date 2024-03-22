# Genetic Algorithm

This Python script implements a genetic algorithm for optimization problems. Genetic algorithms are a type of evolutionary algorithm inspired by the process of natural selection. They are commonly used to find approximate solutions to optimization and search problems.

## Usage

1. **Define Custom Fitness Function**: Before using the genetic algorithm, define a custom fitness function by subclassing the `FitnessFunction` class. Implement the `calculate_fitness` method to calculate the fitness of an individual chromosome.

2. **Set Parameters**: Define the parameters for the genetic algorithm, including population size, chromosome length, mutation rate, number of generations, target solution, gene ranges, and gene types.

3. **Create Genetic Algorithm Instance**: Instantiate the `GeneticAlgorithm` class with the defined parameters and custom fitness function.

4. **Execute Evolution**: Call the `evolve` method of the genetic algorithm instance to run the evolution process. The algorithm will evolve the population over multiple generations, aiming to find the optimal solution.

5. **Retrieve Results**: After the evolution process completes, the `evolve` method returns the best individual chromosome and its fitness score.

## Example

```python
# Define custom fitness function
class CustomFitnessFunction(FitnessFunction):
    def calculate_fitness(self, chromosome):
        return sum(chromosome)

# Define parameters
population_size = 10
chromosome_length = 5
mutation_rate = 0.1
generations = 100
target = [1, 1, 1, 1, 1]
gene_ranges = [(0, 10), (0, 10), (0, 10), (0, 10), (0, 10)]  # Example gene ranges
gene_types = [GeneType.DISCRETE, GeneType.CONTINUOUS, GeneType.DISCRETE, GeneType.CONTINUOUS, GeneType.DISCRETE]  # Example gene types

# Create genetic algorithm instance with custom fitness function and execute
fitness_function = CustomFitnessFunction(maximize=True)  # For maximizing fitness
ga = GeneticAlgorithm(population_size, chromosome_length, mutation_rate, generations, target, gene_ranges, gene_types, fitness_function)
best_individual, best_fitness = ga.evolve()
```

## Requirements

- Python 3.x
