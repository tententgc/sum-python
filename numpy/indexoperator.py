import numpy as np

# x= np.arange(1,10,dtype="int")
# index = np.array([1,5,7])
# a = x[index] # that will can call index in array x 
# print(a)

b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print (b[[0,2]])
print(b[b<6])
print(b[b>6]*2)
