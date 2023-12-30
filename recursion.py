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