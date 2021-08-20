import numpy as np
a=np.array([[1,2,],[3,4]])
a=np.insert(a,1,100,axis=0)
a=np.insert(a,1,[10,20],axis=0)
a=np.insert(a,1,50,axis=1)
print(a)