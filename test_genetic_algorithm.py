import unittest
from genetic_algorimth import GeneticAlgorithm, CustomFitnessFunction, GeneType


class TestInitializePopulation(unittest.TestCase):
    def setUp(self):
        # Define parameters
        self.population_size = 10
        self.chromosome_length = 5
        self.gene_ranges = [(0, 10), (0, 10), (0, 10), (0, 10), (0, 10)]
        self.gene_types = [GeneType.DISCRETE, GeneType.CONTINUOUS, GeneType.DISCRETE, GeneType.CONTINUOUS, GeneType.DISCRETE]
        self.ga = GeneticAlgorithm(self.population_size, self.chromosome_length, 0.1, 100, [1, 1, 1, 1, 1], self.gene_ranges, self.gene_types, CustomFitnessFunction())

    def test_initialize_population_size(self):
        population = self.ga._initialize_population()
        self.assertEqual(len(population), self.population_size)

    def test_initialize_population_chromosome_length(self):
        population = self.ga._initialize_population()
        for chromosome in population:
            self.assertEqual(len(chromosome), self.chromosome_length)


class TestMutate(unittest.TestCase):
    def setUp(self):
        # Define parameters
        self.chromosome_length = 5
        self.gene_ranges = [(0, 10), (0, 10), (0, 10), (0, 10), (0, 10)]  # Example gene ranges
        self.gene_types = [GeneType.DISCRETE, GeneType.CONTINUOUS, GeneType.DISCRETE, GeneType.CONTINUOUS, GeneType.DISCRETE]  # Example gene types
        self.ga = GeneticAlgorithm(10, self.chromosome_length, 0.1, 100, [1, 1, 1, 1, 1], self.gene_ranges, self.gene_types, CustomFitnessFunction())

    def test_mutate(self):
        chromosome = [5, 3.5, 7, 2.1, 8]
        mutated_chromosome = self.ga.mutate(chromosome)
        self.assertNotEqual(chromosome, mutated_chromosome)


class TestCrossover(unittest.TestCase):
    def setUp(self):
        # Define parameters
        self.chromosome_length = 5
        self.ga = GeneticAlgorithm(10, self.chromosome_length, 0.1, 100, [1, 1, 1, 1, 1], [(0, 10)] * self.chromosome_length, [GeneType.DISCRETE] * self.chromosome_length, CustomFitnessFunction())

    def test_crossover(self):
        parent1 = [1, 2, 3, 4, 5]
        parent2 = [6, 7, 8, 9, 10]
        child1, child2 = self.ga.crossover(parent1, parent2)
        self.assertNotEqual(parent1, child1)
        self.assertNotEqual(parent2, child2)
        self.assertEqual(len(child1), self.chromosome_length)
        self.assertEqual(len(child2), self.chromosome_length)


class TestSelection(unittest.TestCase):
    def setUp(self):
        # Define parameters
        self.population_size = 10
        self.chromosome_length = 5
        self.gene_ranges = [(0, 10), (0, 10), (0, 10), (0, 10), (0, 10)]  # Example gene ranges
        self.gene_types = [GeneType.DISCRETE, GeneType.CONTINUOUS, GeneType.DISCRETE, GeneType.CONTINUOUS, GeneType.DISCRETE]  # Example gene types
        self.ga = GeneticAlgorithm(self.population_size, self.chromosome_length, 0.1, 100, [1, 1, 1, 1, 1], self.gene_ranges, self.gene_types, CustomFitnessFunction())

    def test_selection(self):
        selected_population = self.ga.selection()
        self.assertEqual(len(selected_population), self.population_size)
        for chromosome in selected_population:
            self.assertEqual(len(chromosome), self.chromosome_length)


if __name__ == '__main__':
    unittest.main()
