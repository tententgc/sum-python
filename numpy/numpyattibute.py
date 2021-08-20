import numpy as np

a = np.array([1, 2, 3, 45])

b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(a.ndim, b.ndim)
print("type b = " ,b.dtype)
print("shape b  =", b.shape)
print("size b =",b.size)
print("item size = ",b.itemsize) #calculate byte from bit 