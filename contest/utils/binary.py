def highest_power_of_two(n: int):
    if n <= 0:
        return None
    return len(bin(n)) - 2 - 1
