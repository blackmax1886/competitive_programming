import random

def create_grid(H, W):
    grid = [[random.choice(['#', '.']) for _ in range(W)] for _ in range(H)]

    i = random.randrange(H)
    j = random.randrange(W)
    grid[i][j] = 'S'
    
    return grid


