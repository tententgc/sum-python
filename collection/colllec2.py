from collections import namedtuple


points = namedtuple('point', 'x,y')  
pt = points(1, -4)
print(pt.x , pt.y)