def isOK(arr, index, key):
    return arr[index] >= key

def binary_search(arr, key):
    left = -1
    right = len(arr)
    while right - left > 1:
        mid = left + (right - left) // 2

        if isOK(arr, mid, key):
            right = mid
        else:
            left = mid
    return right
