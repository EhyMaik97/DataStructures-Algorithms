def min_and_max_in_array(array):
    if len(array) == 0:
            raise Exception('Max of an empty array')
        
    min_index, max_index = 0, 0

    for i in range(1, len(array)):
        if array[i] < array[min_index]:
            min_index = i
        if array[i] > array[max_index]:
            max_index = i
    return array[min_index], array[max_index]

print(min_and_max_in_array([-4,2,3,79,5,0,1]))