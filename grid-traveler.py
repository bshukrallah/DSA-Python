def gridTraveler(m, n):
    if (m == 1 and n == 1): return 1
    if (m == 0 or n == 0): return 0 
    return gridTraveler(m-1, n) + gridTraveler(m, n-1)

print(gridTraveler(1,1))
print(gridTraveler(2,3))
print(gridTraveler(3,2))
print(gridTraveler(3,3))
#print(gridTraveler(18,18))



def gridTraveler_nr(m, n):
    answer = 0, 0
    if (m == 1 and n == 1): return 1
    if (m == 0 or n == 0): return 0 
    for i in range(m):
        m -= 1
        gridm = m , n
        for k in range(n):
            n -= 1
            gridn = m, n
            answer += gridm + gridn
    return answer
print(gridTraveler_nr(2,3))