from itertools import combinations

#โชว์จำนวนทั้งหมดที่สามารถเกิดได้โดยไม่ซ้ำเคส 
a=[1,2,3,4 ]
comb = combinations(a,2)
print(list(comb))