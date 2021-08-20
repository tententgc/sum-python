import numpy as np
a=np.arange(1,21)
# a=np.split(a,4)
print(a)
a=a.reshape(5,4)
print(a)
a = np.hsplit(a, 4)
print(a)
