def bestSum(target, numbers, memo = None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0: return []
    if target < 0: return None
    
    shortestCombination = None
    
    for num in numbers:
        remainder = target - num
        result = bestSum(remainder, numbers, memo)
        if result is not None:
            combination = result + [num]
            print("result: " + str(result) + " combination: " + str(combination))
            if shortestCombination is None or len(combination) < len(shortestCombination):
                shortestCombination = combination
                
    memo[target] = shortestCombination
    return shortestCombination
                
print(bestSum(190, [3,2,6]))
print(bestSum(100, [3,2,25]))