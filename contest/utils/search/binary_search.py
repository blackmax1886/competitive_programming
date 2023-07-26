def binary_search(arr, key):
    left = 0
    right = len(arr) - 1 # 配列 a の左端と右端
    while right >= left:
        mid = left + (right - left) // 2 # 区間の真ん中
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            right = mid - 1
        elif arr[mid] < key:
            left = mid + 1
    return -1
