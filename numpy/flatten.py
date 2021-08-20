import numpy as np 

a=np.array([[1,2],[3,4],[5,6]])
# print(a.flatten())  #flatten that mean is convert array 3 or 2 or anything to 1 array
b=a.flatten()
b[0]= 5
print(a)
# flatten ไม่่่เปลี่ยน a
c = a.ravel()
c[0]=5
print(a)
#ravel เปลี่ยน a

