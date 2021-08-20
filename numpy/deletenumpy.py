import numpy as np
# a=np.arange(1,10)
# print(a)
# a=np.delete(a,2)
# print(a)

a=np.arange(1,13).reshape(4,3)
print(a)
a=np.delete(a,2,axis=0)
print(a)