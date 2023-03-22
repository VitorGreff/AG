import random
import numpy as np

# origem / destino
cities = np.array([[60, 200], [180, 200], [80, 180], 
                   [140, 180], [20, 160], [100, 160],
                   [200, 160], [140, 140], [40, 120], 
                   [00, 120], [180, 100], [60, 80],
                   [120, 80], [180, 60], [20, 40], 
                   [100, 40], [200, 40], [20, 20],
                   [60, 20], [160, 20]])

# parametros do AG
POP_SIZE = 50
NUM_ITER = 100
MUT_RATE = 0.02
ELITISM = True

# distancia euclidiana 
def dist(x, y):
    return np.linalg.norm(x - y)


def custo(rota):
    custo = 0
    for i in range(len(rota)):
        custo += dist(rota[i], rota[(i+1) % len(rota)])
    return custo


pop = [np.random.permutation(len(cities)) for i in range(POP_SIZE)]

# Evolução da população
for it in range(NUM_ITER):
    # Avaliação da população
    fitness = np.array([1/custo(pop[i]) for i in range(POP_SIZE)])
    fitness /= sum(fitness)

    # Seleção de pais
    parents = np.random.choice(np.arange(POP_SIZE), size=POP_SIZE, replace=True, p=fitness)

    # Cruzamento
    offspring = []
    for i in range(POP_SIZE):
        parent1 = pop[parents[i]]
        parent2 = pop[parents[(i+1)%POP_SIZE]]
        child = np.full(len(cities), -1)
        start, end = sorted(random.sample(range(len(cities)), 2))
        child[start:end+1] = parent1[start:end+1]
        j = 0
        for k in range(len(cities)):
            if parent2[k] not in child:
                while child[j] != -1:
                    j += 1
                child[j] = parent2[k]
        offspring.append(child)

    # Mutação
    for i in range(POP_SIZE):
        if random.random() < MUT_RATE:
            idx1, idx2 = random.sample(range(len(cities)), 2)
            offspring[i][idx1], offspring[i][idx2] = offspring[i][idx2], offspring[i][idx1]

    # Elitismo
    if ELITISM:
        elite_idx = np.argmax(fitness)
        offspring[0] = pop[elite_idx]

    # Atualização da população
    pop = offspring

# Seleção da melhor rota
best_idx = np.argmin([custo(pop[i]) for i in range(POP_SIZE)])
best_route = pop[best_idx]
print("Melhor rota encontrada:", best_route)

