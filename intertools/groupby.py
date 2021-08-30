from itertools import groupby

# def smaller_than_3 (x):
#     return x<3


a=[1,2 ,3 ,4]
group_obj = groupby(a, key=lambda x: x < 3)  # can put to function smaller_than_3 because it mean same that  

for key,value in group_obj:
    print(key, list(value))

