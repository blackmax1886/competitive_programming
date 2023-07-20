# import random

def getInts():
    return map(int, input().split())

def getIntsMatrix(N):
    mat = []
    for _ in range(N):
        mat.append(list(map(int, input().split())))
    return mat

def max_sum(matrix, h, w):
    for i in range(h-2, -1, -1):
        for j in range(w):
            down = matrix[i+1][j]
            down_left = matrix[i+1][j-1] if j-1 >= 0 else 0
            down_right = matrix[i+1][j+1] if j+1 < w else 0
            matrix[i][j] += max(down, down_left, down_right)
    return max(matrix[0])

H, W = getInts()
scores = getIntsMatrix(H)

# def generate_ints(min, max):
#     return random.randint(min,max), random.randint(min,max)

# def generate_matrix(h, w, min, max):
#     matrix = [[random.randint(min,max) for _ in range(w)] for _ in range(h)]
#     return matrix

# H, W = generate_ints(7,7)
# scores = generate_matrix(H,W,0,10)
# for score in scores:
#     print(score)

print(max_sum(scores, H, W))
