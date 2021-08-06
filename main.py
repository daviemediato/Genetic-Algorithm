import matplotlib.pyplot as plt
from Genetic_Algorithm import Genetic_Algorithm

def main():
    genetic = Genetic_Algorithm(population_size=100, chromosome_length=2, mutation_rate=0.1)
    results = genetic.genetic_algorithm()
    
    plt.plot(results)
    plt.xlabel('Geração')
    plt.ylabel('Valor')

if __name__ == "__main__":
    main()