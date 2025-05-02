def linear_search(array, target):
    for i in range(0, len(array)):
        if target == array[i]:
            return i

def delete(array, target) -> None:
        '''
        Delete a target value from the array.

        Parameters:
            target (any): The value to delete from the sorted array.

        Returns:
            None

        Functionality:
            Finds the leftmost index of the target value using the find method.
            If the target is not found, raises a ValueError.
            Otherwise, deletes the target value by shifting all values after it to the left,
            to keep the remaining elements in the order they were inserted.
        '''

        index = linear_search(array, target)
        if index is None:
            raise ValueError(f'Unable to delete element {target}: the entry is not in the array')

        # Must shift all the elements after the position of the target
        print(array)
        for i in range(index, len(array) - 1):
            array[i] = array[i + 1]
            print(array)
        print(array[1:])
array = [1,23,4,5,6,7,8]

delete(array, 4)