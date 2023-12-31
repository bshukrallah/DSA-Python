def recurse(n):
    if (n <= 1): 
        return
    recurse(n - 1)
    
#print(recurse(7))


def EvenNums(num):
    if(num%2 == 1):
        #print("Not an even number") 
        return "Not an even number"
    #print(num)
    elif num == 2: return num
    else: return EvenNums(num-2)
    
print(EvenNums(8))
print(EvenNums(99))

def addNums(list1, list2, total=0):
    difference = len(list1) - len(list2)
    if (len(list1) - len(list2) > 0):
        list2+=[0] * difference
    else:
        list1+=[0] * -difference
    print(list1)
    print(list2) 
        
    
    if len(list1) == 0 or len(list2) == 0:
        return total
    
    total += list1[0] + list2[0]

    return addNums(list1[1:], list2[1:], total)

print(addNums([1,1,1], [1,1,1,1]))