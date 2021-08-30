a = [1,5,2,456,45,23,87,88,2,3,4,5,6]

filter_list= list(filter(lambda x: (x >7), a ))
filter_list.sort()

print(filter_list)
