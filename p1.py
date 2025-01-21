#WAP to implement linear and binary search
#Linear search
arr = [1, 3, 5, 4, 7, 9]
key = 7
n = len(arr)
def linear_search(arr, n ,key):
    for i in range(0, n):
        if arr[i] == key:
            return i
    return -1
res = linear_search(arr, n, key)
if res == -1:
    print("Element not found.")
else:
    print("Element found at index: ", res)

#Binary search
arr = [12, 24, 32, 39, 45, 50, 54]
n = 45
def binary_search(arr, n):
    low = 0
    high = len(arr) - 1 
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < n:
            low = mid + 1
        elif arr[mid] > n:
            high = mid - 1
        else:
            return mid
    return -1
res = binary_search(arr, n)
if res != -1:
    print("Element found at index: ", res)
else:
    print("Element not found.")