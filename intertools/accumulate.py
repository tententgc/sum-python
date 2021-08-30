from itertools import accumulate 

# + โชว์ผลบวกไปเรื่อยๆ ได้
a= [1,2,3,4]
acc  = accumulate(a)
print(a)
print(list(acc))