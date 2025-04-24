def recursive_sum(list):
    if list == []:
        return 0
    return list[0] + recursive_sum(list[1:])

print(recursive_sum([1,2,3,4,5]))

def recursive_count(arr: list):
    if arr == []:
        return 0
    return 1 + recursive_count(arr[1:])

print(recursive_count([1,2,34,5,6,7,8,8,6,5,4,32,2]))

def find_max(arr: list):
    max = 0
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

print(find_max([1,2,34,5,6,7,8,8,6,5,4,32,2]))

def recursive_max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max