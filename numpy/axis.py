import numpy as np
a=np.array([[1,2,3],[4,5,9],[8,10,5]])
print(np.min(a,axis=1)) #axis 1 =แนวนอน  axis 0 ==แนวตั้ง
print(np.min(a,axis= 0))
print(np.max(a,axis= 0)) 
