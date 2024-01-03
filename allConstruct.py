def allConstruct(target, wordBank, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == "": return [[]]
    total_ways = []
    for word in wordBank:
        if target.find(word) == 0: #check if the "word" in the wordbank starts at the beginning of the target word
            result = target[len(word):]
            each_way = allConstruct(result, wordBank, memo)
            #print(each_way)
            all_ways = []
            for way in each_way:
                new_way = [word] + way
                all_ways.append(new_way)
                total_ways= total_ways + all_ways
    memo[target] = total_ways

    return total_ways
            
print(allConstruct("word", ["job", "rd", "wo", "li", "jk", "ing"]))
print(allConstruct("program", ["job", "pr", "gram", "a", "m", "ming", "o"]))
print(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeeee", "eeeeeeeeeeeee", "aaaaaaaaaaa"]))
print(allConstruct("purple", ["urpl", "p", "le", "e", "urp", "le"]))
