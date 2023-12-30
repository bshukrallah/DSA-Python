import time

def gridTraveler(m, n):
    if (m == 1 and n == 1): return 1
    if (m == 0 or n == 0): return 0 
    return gridTraveler(m-1, n) + gridTraveler(m, n-1)

print("** Slow **")
original = time.time()
print(gridTraveler(1,1))
print(gridTraveler(2,3))
print(gridTraveler(3,2))
print(gridTraveler(3,3))

print("unoptimized time: " + str(time.time()-original))
#print(gridTraveler(18,18))


def gridTraveler_fast(m, n, memo={}):
    key = str(m) + "," + str(n)
    print(memo)
    if (key in memo):
        return memo[key]
    if (m == 1 and n == 1): return 1
    if (m == 0 or n == 0): return 0 
    memo[key] = gridTraveler(m-1, n) + gridTraveler(m, n-1)
    return memo[key]

print("** Optimized **")
optimized = time.time()
print(gridTraveler_fast(1,1))
print(gridTraveler_fast(2,3))
print(gridTraveler_fast(3,2))
print(gridTraveler_fast(3,3))
print(gridTraveler_fast(18,18))
print("unoptimized time: " + str(time.time()-optimized))