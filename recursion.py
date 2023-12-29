def recurse(n):
    if (n <= 1): 
        return
    recurse(n - 1)
    
print(recurse(7))