import timeit

def canSum(target, numbers):
    if (target == 0):
        return True
    if (target < 0):
        return False
    for num in numbers:
        remainder = target - num
        if (canSum(remainder, numbers) == True):
            return True
    
    return False
            
print("** Slow **")
start = timeit.default_timer()
print(canSum(7, [2,3,4,5]))
print(canSum(7, [2,4]))
print(canSum(9, [2,3,4,5]))


end = timeit.default_timer()
unoptimized = (end - start) * 1000
print(f"unoptimized time: {unoptimized:.4f}")


#print(canSum(300, [7,14]))


def canSum_faster(target, numbers, memo = None): #initialize memo with None, create it in the function
    if(memo is None):
        memo = {}
    if(target in memo): #Use target as the key, because it changes
        return memo[target] #can return the value from the key if it exists, no need for a branching if
    if (target == 0):
        return True
    if (target < 0):
        return False

    for num in numbers:
        remainder = target - num
        if (canSum_faster(remainder, numbers, memo) == True):
            memo[target] = True #Use target as the key, because it changes
            return True
        
    memo[target] = False
    return False


print("** Optimized **")
start = timeit.default_timer()
print(canSum_faster(7, [2,3,4,5]))
print(canSum_faster(7, [2,4]))
print(canSum_faster(9, [2,3,4,5]))
print(canSum_faster(900, [7,14]))
end = timeit.default_timer()
optimized = (end - start) * 1000
print(f"optimized time: {optimized:.4f}")