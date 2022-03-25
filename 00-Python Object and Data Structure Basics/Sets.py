#### sets
# unordered collections of unique values
my_set = set()
my_set.add(1)
print(my_set)
my_set.add(2)
print(my_set)
my_set.add(2)
print(my_set) # won't accept repeat value

# useful to cast a list to a set to extract unique values
my_list = [2,1,1,2,2,3,1,3,1,4,3,1,2,2,3,5,3]
print(my_list)
print('list to set', set(my_list))

