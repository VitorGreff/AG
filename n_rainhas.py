import random

POP_SIZE = 50
NUM_ITER = 100
MUT_RATE = 0.02
ELITISM = True

def generate_board(n):
    board = [0] * n
    for i in range(n):
        board[i] = random.randint(0, n-1)
    return board

def fitness(board):
    n = len(board)
    collisions = 0
    for i in range(n):
        for j in range(i+1, n):
            if board[i] == board[j] or abs(board[i]-board[j]) == abs(i-j):
                collisions += 1
    return collisions

def crossover(parent1, parent2):
    n = len(parent1)
    child = [0] * n
    crossover_point = random.randint(1, n-1)
    for i in range(crossover_point):
        child[i] = parent1[i]
    for i in range(crossover_point, n):
        child[i] = parent2[i]
    return child

def mutate(board):
    n = len(board)
    mutated_board = list(board)
    if random.random() < MUT_RATE:
        i = random.randint(0, n-1)
        mutated_board[i] = random.randint(0, n-1)
    return mutated_board

def genetic_algorithm(n):
    population = [generate_board(n) for i in range(POP_SIZE)]
    for i in range(NUM_ITER):
        population = sorted(population, key=lambda board: fitness(board))
        if ELITISM:
            new_population = [population[0]]
        else:
            new_population = []
        while len(new_population) < POP_SIZE:
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)
        population = new_population
    population = sorted(population, key=lambda board: fitness(board))
    return population[0]

if __name__ == '__main__':
    board = genetic_algorithm(8)
    print(board)
