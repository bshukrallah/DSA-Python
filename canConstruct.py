def canConstruct(target, wordBank, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == "": return True
    
    for word in wordBank:
        if target.find(word) == 0: #check if the "word" in the wordbank starts at the beginning of the target word
            result = target[len(word):]
            if (canConstruct(result, wordBank, memo) == True):
                memo[target] = True
                print(memo)
                return True
            else:
                memo[result] = False

    memo[target] = False
    return False
            
print(canConstruct("word", ["job", "rd", "wo", "li", "jk", "ing"]))
print(canConstruct("program", ["job", "pr", "gram", "a", "m", "ming", "o"]))
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeeee", "eeeeeeeeeeeee", "aaaaaaaaaaa"]))