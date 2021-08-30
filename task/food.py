
from itertools import permutations

a = int(input())
FoodList = [int(x) for x in range(1, a+1)]
b = int(input())
BanList = [int(x) for x in input().split()]

perm = list(permutations(FoodList, a))
for i in range(len(perm)):
    if perm[i][0] not in BanList:
        print(" ".join(map(str, perm[i])))

