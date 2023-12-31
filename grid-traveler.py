import timeit

def gridTraveler(m, n):
    if (m == 1 and n == 1): return 1
    if (m == 0 or n == 0): return 0 
    return gridTraveler(m-1, n) + gridTraveler(m, n-1)

print("** Slow **")
start = timeit.default_timer()
print(gridTraveler(1,1))
print(gridTraveler(2,3))
print(gridTraveler(3,2))
print(gridTraveler(3,3))
print(gridTraveler(15,12))
end = timeit.default_timer()
unoptimized = (end - start) * 1000
print(f"unoptimized time: {unoptimized:.4f}")



def gridTraveler_fast(m, n, memo={}):
    key = str(m) + "," + str(n)
    #print(memo)
    if (key in memo):
        return memo[key]
    if (m == 1 and n == 1): return 1
    if (m == 0 or n == 0): return 0 
    memo[key] = gridTraveler_fast(m-1, n, memo) + gridTraveler_fast(m, n-1, memo)
    return memo[key]

print("** Optimized **")
start = timeit.default_timer()
print(gridTraveler_fast(1,1))
print(gridTraveler_fast(2,3))
print(gridTraveler_fast(3,2))
print(gridTraveler_fast(3,3))
print(gridTraveler_fast(18,18))
end = timeit.default_timer()
optimized = (end - start) * 1000
print(f"optimized time: {optimized:.4f}")

if unoptimized < optimized:
    print("The unoptimized code is faster")
else:
    print("The optimized code is faster")