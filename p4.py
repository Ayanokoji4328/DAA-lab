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

def merge_two_sorted_lists(list1, list2):
    merged_list = list1 + list2
    merge_sort(merged_list)
    return merged_list

list1 = [34, 7, 23, 32, 5]
list2 = [78, 12, 3, 56, 89]

sorted_list = merge_two_sorted_lists(list1, list2)
print("Sorted Merged List:", sorted_list)
