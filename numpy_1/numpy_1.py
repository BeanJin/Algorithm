import numpy as np

a = np.array([1, 2])

print(a)

a = np.zeros((3, 2))
b = np.ones((2, 1))

print(a)
print(b)

a = np.array([1., 2., 3.])
b = np.array([4., 3., 2.])

print(np.add(a, b))
print(np.multiply(a, b))

a = np.random.rand(1, 3)
b = np.random.randn(2, 4)

print(a)
print(b)

pi = np.pi
e = np.e
print(pi)
print(e)