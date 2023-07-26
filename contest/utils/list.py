def find_max_index(numbers):
    max_index, max_value = max(enumerate(numbers), key=lambda pair: pair[1])
    return max_index

def find_indices_2d(data, target):
    for i, row in enumerate(data):
        for j, item in enumerate(row):
            if item == target:
                return (i, j)
    return None

def find_first_index(lst, condition):
    return next((i for i, x in enumerate(lst) if condition(x)), None)

def max_index_le_threshold(lst, value):
    return next((i for i in reversed(range(len(lst))) if lst[i] <= value), None)

def max_index_ge_threshold(lst, value):
    return next((i for i in reversed(range(len(lst))) if lst[i] >= value), None)

def sum_last_column(matrix):
    return sum(row[-1] for row in matrix)
