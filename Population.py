from Chromosome import Chromosome

class Population:
    def __init__(self, population_size=10, chromosome_length=2, chromosomes=None):
        self.population_size = population_size
        self.chromosome_length = chromosome_length
        if(chromosomes == None):
            self.population = [Chromosome(chromosome_length)
                            for i in range(population_size)]
        else:
            self.population = chromosomes

    def sort_population(self):
        self.population.sort(
            key=lambda x: x.objective, reverse=True)
        return self.population

    def calculate_fitness(self):
        for i in range(self.population_size):
            self.population[i].objective_function()
			            
        self.sort_population()
        min_value = self.population[-1].objective
        min_value = self.population[-1].objective
        max_value = self.population[0].objective

        for i in range(self.population_size):
            self.population[i].fitness = min_value + (max_value - min_value) * ( (self.population_size - i) / (self.population_size - 1 ))
    
        return self.population

    def get_best_score(self):
        self.sort_population()
        return self.population[0].objective

    def __str__(self):
        string = 'Population:\n'
        for i in range(self.population_size):
            string += f'{self.population[i]}\n'
        return string    