def linear_search(array, target):
    for i in range(0, len(array)):
        if target == array[i]:
            return f'Index: {i}'
    return 'None - Element not present in this list'

print(linear_search([1,23,4,5,56,7], 34))
print(linear_search([1,23,4,5,56,7], 56))