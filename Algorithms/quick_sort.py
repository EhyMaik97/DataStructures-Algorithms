"""
Quick Sort
Complexity Average case: O(nlogn)
Complexity Worst case: O(n^2)
"""

def quick_sort(arr: list):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i >= pivot]
        
        return quick_sort(less) + [pivot] + quick_sort(greater)
    
print(quick_sort([10, 5, 2, 3, 34, 1, 92]))