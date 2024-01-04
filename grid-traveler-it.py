def gridTraveler(m, n):
    table = [[0]*(m+1) for each in range(n+1)] #the for loop makes it repeat, you cannot multiple it by n+1 or it's the same array over and over.
    table[1][1] = 1
    for m_index in range(n+1):
        for n_index in range(m+1):
            current = table[m_index][n_index]
            if (n_index + 1) <= m:
                table[m_index][n_index+1] += current
            if (m_index + 1) <= n:
                table[m_index+1][n_index] += current

    return table

print(gridTraveler(3,2))
