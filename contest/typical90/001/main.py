def getInt():
    return int(input())

def getInts():
    return map(int, input().split())

def getIntsArray():
    return list(map(int, input().split()))

def calculate_max_pieces(array, piece_len):
    count = 0
    current_len = 0
    for i in range(1, len(array)):
        current_len += array[i] - array[i-1]
        if current_len >= piece_len:
            count += 1
            current_len = 0 
    return count

n, l = getInts()
k = getInt()
positions = getIntsArray()
positions.insert(0,0)
positions.append(l)

left = -1
right = l
while right - left > 1:
    mid = left + (right - left) // 2
    if calculate_max_pieces(positions, mid) < k + 1:
        right = mid
    else:
        left = mid
# result = 0
# for i in range(1,l):
#     max_pieces = calculate_max_pieces(positions, i)
#     if max_pieces >= k+1:
#         result = i
print(left)
