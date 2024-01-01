# The idea is that the function will start iterating through each item in the lists (nums)
# We will subtract each item from the target, and store the result as a key, and the index of that iteration as the value
# For example, if the target is 9, and the first number iterated is 5, the hashmap key will be "4" and the value will be "0"
# It will continue for each number storing the sum of the target - each item in the list in the hashmap
# If the answer is another item in the list, that means subtracting the target from that will equal 0
# The function will return the dictionary value for that iteration, and the current index it is on
# For example, after doing the previous 9 - 5, 4 is stored as a key, with the value of 5's index, so if 4 is in the list that means 4-4 is 0, so 4+5 is 9
# It will look up the key of 4, and return "0" since that was 5's key, and then return the current index the for loop is on.

def twoSum(nums, target):
    result = {}
    for i, n in enumerate(nums):
        if n in result:
            return result[n],i 
        else:
            result[target-n]=i


print(twoSum([3,3],6))

print(twoSum([5,3,4],9))