def find_duplicates(nums):
    new_list = {}
    for num in nums:
        if num in new_list:
            new_list[num] += 1
        else:
            new_list[num] = 1
    duplicates = []
    for num in new_list:
        if new_list[num] > 1:
            duplicates.append(num)
            
    return duplicates



print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )