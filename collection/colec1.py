from collections import Counter
from collections import  namedtuple 

a="aaaaabbbccc" 
my_counter = Counter(a)
print(my_counter.values())
print(my_counter.keys())
print(my_counter. most_common(1)[0][0])
print(list(my_counter. elements()))
