"""
Insertion Sort
Complexity Best case: O(n)
Complexity Average case: O(n^2)
Complexity Worst case: O(n^2)
"""

def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        anchor = arr[i]
        k = i - 1
        while k >= 0 and anchor < arr[k]:
            arr[k+1] = arr[k]
            k = k - 1
        arr[k+1] = anchor
        
    return arr

print(insertion_sort([5, 10, 2, 3, 34, 1, 92]))