def min_in_array(array):
    if len(array) == 0:
            raise Exception('Max of an empty array')
    min_index = 0
    for i in range(1, len(array)):
        if array[i] < array[min_index]:
            min_index = i
    return array[min_index]

print(min_in_array([1,2,3,79,5,0,-4]))