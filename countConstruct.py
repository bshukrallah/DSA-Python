def canConstruct(target, wordBank, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == "": 
        return 1
    count = 0
    for word in wordBank:
        if target.find(word) == 0: #check if the "word" in the wordbank starts at the beginning of the target word
            result = canConstruct(target[len(word):], wordBank, memo)
            memo[target] = result
            count += result

    return count

print(canConstruct("purple", ["urpl", "p", "le", "e", "urp", "le"]))
print(canConstruct("word", ["job", "rd", "wo", "li", "jk", "d", "r"]))
print(canConstruct("program", ["job", "pr", "gram", "a", "m", "ming", "o"]))
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeeee", "eeeeeeeeeeeee", "aaaaaaaaaaa"]))