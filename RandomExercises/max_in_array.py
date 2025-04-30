def max_in_array(array):
    if len(array) == 0:
            raise Exception('Max of an empty array')
        
    max_index = 0
    for i in range(1, len(array)):
        if array[i] > array[max_index]:
            max_index = i
    return array[max_index]
    
print(max_in_array([1,2,3,79,5]))