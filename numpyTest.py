import numpy as np

a = np.zeros(3)

print(a)
print(type(a[0]))

print(a.shape)

ones = np.ones(10)
print(ones)

b = np.empty(10)
print(b)

lin_space = np.linspace(2,10,5) #lin space, goes from 2 to 10, has 5 elements
print(lin_space)

z = np.array([10,20])

print(z)

a_list = [1,2,3,4,5]

z = np.array(a_list)

print(z)

print(z[0])# first element
print(z[-1]) #last element

np.random.seed(0) #seeding a random array
z1 = np.random.randint(10,size=6)
print(z1)