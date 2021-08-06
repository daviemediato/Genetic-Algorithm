import random
import math

class Chromosome:
    def __init__(self, chromosome_length=2, genes= None):
        if(genes == None):
            self.genes = [random.uniform(0.1, 10)
                        for i in range(chromosome_length)]
        else:
            self.genes = genes
        self.chromosome_length = chromosome_length
        
        self.objective = None
        self.fitness = None
    
    def objective_function(self):
        product_result = 1

        for i in range(self.chromosome_length):
            gene_product = math.sqrt(self.genes[i]) * math.sin(self.genes[i])
            product_result = product_result * gene_product

        self.objective = product_result
    
    def __repr__(self):
        return f'Genes: {self.genes} - Objetivo: {self.objective} - Fitness: {self.fitness}'
