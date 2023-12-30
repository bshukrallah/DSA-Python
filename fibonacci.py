import time

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


#print(faster_fib(6))
#print(faster_fib(7))
#print(faster_fib(100))


def Fibonacci(index):
    if index <= 1: return index
    else: return Fibonacci(index - 1) + Fibonacci(index-2)
    
def fibonacci(index):
    seq = [0,1]
    for i in range(index):
        seq.append(seq[-1]+seq[-2])
    return seq[-2]    

print("** Recursion **")
rec_time = time.time()
print(Fibonacci(30))
print("Speed: " + str(time.time()-rec_time))

print("** Iteration **")
iteration_time = time.time()
print(fibonacci(30))
print("Speed: " + str(time.time()-iteration_time))