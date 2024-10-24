import numpy as np

ones = np.ones((3,10), dtype=np.float64)
print(ones)
print(ones)
print(ones.shape, ones.ndim)

a = np.arange(1, 10, 3)

print(a)


b = np.array([[1,2,3],[7,8,9]])
b1 = np.array([1,2,3,4,5,6])
b2 = np.array([[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,21]]]])
print(b1.shape, b1.ndim)
print(b.shape, b.ndim)
print(b2,b2.shape, b2.ndim)
