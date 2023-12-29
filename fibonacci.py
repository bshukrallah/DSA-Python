def fib(n):
    if (n <= 2):
        return 1
    return fib(n - 1) + fib(n - 2)


def faster_fib(n, memo = {}):
    if (n in memo):
        return memo[n]
    if (n <= 2):
        return 1
    memo[n] = faster_fib(n - 1) + faster_fib(n - 2)
    print(memo)
    return memo[n] 


print(faster_fib(6))
print(faster_fib(7))
#print(faster_fib(100))