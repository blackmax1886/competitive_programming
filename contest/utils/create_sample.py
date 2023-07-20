import random

def generate_grid(H, W):
    grid = [[random.choice(['#', '.']) for _ in range(W)] for _ in range(H)]

    i = random.randrange(H)
    j = random.randrange(W)
    grid[i][j] = 'S'
    
    return grid

def generate_int(min,max):
    return random.randint(min,max)

def generate_ints(min, max):
    return random.randint(min,max), random.randint(min,max)

def generate_matrix(h, w, min, max):
    matrix = [[random.randint(min,max) for _ in range(w)] for _ in range(h)]
    return matrix
