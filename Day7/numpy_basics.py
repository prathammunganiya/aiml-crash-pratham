import numpy as np

a = np.array([1, 2, 3, 4, 5])

b = np.arange(10)

c = np.zeros((2, 3))

d = np.linspace(0, 10, 5)

print(a.shape, a.dtype, a.ndim)
print(c.shape, c.dtype, c.ndim)

print("Negative Index:", a[-1])

print("Slice:", a[1:4])