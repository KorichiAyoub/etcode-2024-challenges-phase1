def min_op(nums):
    counts = {}
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    for value in counts.values():
        if value == 1:
            return -1

    operations = 0

    for value in counts.values():
        if value >= 3:
            operations += value // 3
            value %= 3
        operations += 1 if value > 0 else 0

    return int(operations)

arr1 = [2,3,3,2,2,4,2,3,4]
arr2 = [2,1,2,2,3,3]
arr3 = [14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]
print(min_op(arr1))  
print(min_op(arr2)) 
print(min_op(arr3))  
