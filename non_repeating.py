def first_non_repeating_char(string):
    dict = {}
    for each in string:
        if each in dict:
            dict[each] += 1
        else:
            dict[each] = 1
    for each in dict:
        if dict[each] == 1:
            return each

    return None

print( first_non_repeating_char("leetcode") )

print( first_non_repeating_char("hello") )

print( first_non_repeating_char("aabbcc") )

print( first_non_repeating_char("a") )