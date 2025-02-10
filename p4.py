def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
def merge_and_sort_lists(list1, list2):
    merged_list = list1 + list2
    merge_sort(merged_list)
    return merged_list
list1 = list(map(int, input("Enter element of 1st list: ").split()))
list2 = list(map(int, input("Enter element of 2nd list: ").split()))
sorted_list = merge_and_sort_lists(list1, list2)
print("List 1 is: ", list1)
print("List 2 is: ", list2)
print("Sorted merged list is: ", sorted_list)
