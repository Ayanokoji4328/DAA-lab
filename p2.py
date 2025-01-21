#WAP to implement bubble and selection sort
#bubble sort
listl = [9, 16, 6, 26, 0]
print("Unsorted array: ", listl)
for j in range(len(listl) - 1):
    for i in range(len(listl) - 1):
        if listl[i] > listl[i + 1]:
            listl[i], listl[i + 1] = listl[i + 1], listl[i]
    print("List after iteration " , j + 1, " is ", listl)
print("Sorted array: ", listl)

#selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
arr =  [64, 25, 12, 22, 11]
print("\nOriginal array: ", arr)
selection_sort(arr)
print("Sorted array: ", arr)