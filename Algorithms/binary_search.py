def binary_search(my_list:list, target:int):
    low = 0
    high = len(my_list) -1 
    count = 0
    if my_list != sorted(my_list):
        return "Binary search works only with sorted list!"
    while low <= high:
        count += 1
        mid = (low + high) // 2
        guess = my_list[mid]
        if guess == target:
            return f"Element at index: {mid}, found after: {count} times"
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return "Not Found: -1"

print(binary_search([1, 4, 5, 6, 8, 9, 34, 54, 78, 79, 90, 102, 123, 145], 8)) # test case n.1
print(binary_search([1, 4, 5, 6, 8, 9, 34, 54, 78, 79, 90, 102, 123, 145], 54)) # test case n.2
print(binary_search([1, 4, 5, 6, 8, 9, 34, 54, 78, 79, 90, 102, 123, 146], 79)) # test case n.3
print(binary_search([1, 4, 5, 6, 8, 9, 34, 54, 78, 79, 90, 102, 123, 145], 45)) # Element not present in the list
print(binary_search([1, 144, 6, 8, 91, 4, 6, 54, 0, 12, 123, 145], 45)) # Not sorted List