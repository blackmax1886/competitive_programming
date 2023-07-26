# import random

# def create_grid(H, W):
#     grid = [[random.choice(['#', '.']) for _ in range(W)] for _ in range(H)]

#     i = random.randrange(H)
#     j = random.randrange(W)
#     grid[i][j] = 'S'
    
#     return grid

def getInts():
    return map(int, input().split())

def find_indices_2d(data, target):
    for i, row in enumerate(data):
        for j, item in enumerate(row):
            if item == target:
                return (i, j)
    return None

# 脱出可能
def is_goal(position, h, w):
    return position[0] == h-1 or position[1] == w-1 or position[0] == 0 or position[1] == 0

def is_valid_position(position, h, w):
    return 0 <= position[0] <= h-1 and 0 <= position[1] <= w-1

def is_path(position, maze):
    return maze[position[0]][position[1]] == '.' or maze[position[0]][position[1]] == 'S'

def is_not_searched(position, searched):
    return searched[position[0]][position[1]] == -1

def main(H, W, maze):
    start_index = find_indices_2d(maze, "S")
    stack = [start_index]
    searched = [[-1]*W for _ in range(H)]
    searched[start_index[0]][start_index[1]] = 0
    if is_goal(start_index, H, W):
        print('YES')
        return
    while stack:
        current_index = stack.pop()
        # 上下左右を確認して未探索ならstackに加える
        ch = current_index[0]
        cw = current_index[1]
        up_index = (ch, cw-1)
        down_index = (ch, cw+1)
        left_index = (ch-1, cw)
        right_index = (ch+1, cw)
        nears = [up_index, down_index, left_index, right_index]
        for near in nears:
            if is_valid_position(near, H, W) and is_path(near, maze) and is_not_searched(near, searched):
                if is_goal(near, H, W):
                    print("YES")
                    return
                else:
                    stack.append(near)
                    searched[near[0]][near[1]] = 0
    print("NO")

H, W = getInts()
maze = []
for _ in range(H):
    maze.append(list(input()))

# H = random.randint(3,10)
# W = random.randint(3,10)
# maze = create_grid(H, W)
# print('\n'.join(''.join(row) for row in maze))
main(H, W, maze)
