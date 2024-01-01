def howSum_old(target, numbers, memo = None):
    if memo is None:
        memo = {}
    if target == 0: return []
    if target < 0: return None
    if target in numbers:
        values = list(memo.values())
        values.append(target)
        return values
    for num in numbers:
        memo[target] = num
        target = target-num
        return howSum_old(target, numbers, memo)
    
    return None

print(howSum_old(9, [2,3]))
print(howSum_old(99, [2,3]))


def howSum(target, numbers, memo = None):
    if memo is None:
        memo = {}
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None
    
    for num in numbers:
        remainder = target - num
        if remainder < 0:
            continue
        remainder_result = howSum(remainder, numbers, memo)
        if remainder_result is not None:
            memo[target] = remainder_result + [num]
            return memo[target]
        
    memo[target] = None
    return None

print(howSum(9, [2,3]))
print(howSum(1000, [2,3]))