def fib(n):
    table=[0]*(n+1)
    table[1] = 1
    for index in range(n):
        table[(index+1)] += table[index]
        if index + 2 <= n:
            table[(index+2)] += table[index]
    return table[n]
print(fib(6))
print(fib(7))
print(fib(8))
print(fib(55))
