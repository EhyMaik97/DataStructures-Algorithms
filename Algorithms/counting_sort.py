"""
Counting Sort -> non-comparison-based sorting algorithm
Complexity Average case: O(n + k)
"""

def counting_sort(arr: list):
    if not arr:
        return arr
    
    max_val = max(arr)
    min_val = min(arr)
    
    range_val = max_val - min_val + 1
    count = [0] * range_val
    
    for value in arr:
        count[value - min_val] += 1
    
    print(count)
    sorted = []
    for index, freq in enumerate(count):
        sorted.extend([index + min_val] * freq)
    
    return sorted

print(counting_sort([5, 10, 2, 2, 3, 34, 1, 92]))