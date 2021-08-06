import random
import math
from sklearn import preprocessing
import numpy as np
from Chromosome import Chromosome
from Population import Population


class Genetic_Algorithm:
    def __init__(self, population_size=10, chromosome_length=2,
                 mutation_rate=0.01):
        self.population_size = population_size
        self.chromosome_length = chromosome_length
        self.mutation_rate = mutation_rate
        self.iteration = []

    # Seleciona os indivíduos para cruzamento, seguindo a logica da roleta
    def selection(self, population):
        fitness = [[x.fitness for x in population.population]]
        fitness = preprocessing.normalize(fitness)[0]
        acc_fitness = np.cumsum(fitness)
        parents = []
        for trial in range(population.population_size):
            random_value = random.uniform(0, max(acc_fitness))

            for i in range(population.population_size):
                if (acc_fitness[i] >= random_value):
                    parents.append(i)
                    break

        return parents

    # Foi utilizado o crossover aritmetico completo
    def crossover(self, population, parents):
        childs = []
        for i in range(0, len(parents), 2):
            alpha_value = random.uniform(0.25, 1)
            p1 = parents[i]
            p2 = parents[i + 1]
            c1 = []
            c2 = []
            for j in range(self.chromosome_length):
                c1.append(alpha_value * population.population[p1].genes[j] + (
                    1 - alpha_value) * population.population[p2].genes[j])
                c2.append(alpha_value * population.population[p2].genes[j] + (
                    1 - alpha_value) * population.population[p1].genes[j])
            childs.append(Chromosome(self.chromosome_length, c1))
            childs.append(Chromosome(self.chromosome_length, c2))
        return childs

    def mutation(self, childs):
        for i in range(len(childs)):
            for j in range(self.chromosome_length):
                if(random.uniform(0, 1) <= self.mutation_rate):
                    childs[i].genes[j] = random.uniform(0.1, 10)
        return childs

    def genetic_algorithm(self, iterations=100):
        population = Population(self.population_size, self.chromosome_length)
        population.calculate_fitness()

        for i in range(iterations):
            print(f'Iteration {i}: {population.get_best_score()}')
            self.iteration.append(population.get_best_score())
            parents = self.selection(population)
            childs = self.crossover(population, parents)
            childs = self.mutation(childs)
            new_population = Population(
                self.population_size, self.chromosome_length, chromosomes=childs)
            new_population.calculate_fitness()
            population = new_population

        return self.iteration
