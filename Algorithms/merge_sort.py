"""
Merge Sort
Complexity Average case: O(n log n)
"""

def merge_sort(arr: list):
    if len(arr) <= 1:
        return

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)
    
    merge_two_sorted_lists(left, right, arr)


def merge_two_sorted_lists(a, b, arr):
    len_a = len(a)
    len_b = len(b)

    i = j = 0 # Index for left and right sub-array 
    k = 0 # Index for arr 

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1

    # Two more cycles for the rest of elements
    while i < len_a:
        arr[k] = a[i]
        i+=1
        k+=1

    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1


test_cases = [
    [10, 3, 15, 7, 8, 23, 98, 29],
    [],
    [3],
    [9,8,7,2],
    [1,2,3,4,5]
]

for arr in test_cases:
    merge_sort(arr)
    print(arr)