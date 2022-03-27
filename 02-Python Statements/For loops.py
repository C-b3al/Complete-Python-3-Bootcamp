#### for loops
# allows you to iterate over an object
# i.e. perform an operation on each item

my_list = [1,2,3]
for i in my_list:
    my_list.pop(0)
    my_list.append(i*2)
print(my_list)

second_list = []
for i in range(1,11):
    second_list.append(i)

print(second_list)
even_list =[]
for j in second_list:
    if j % 2 == 0:
        even_list.append(j)
print(even_list)

for letter in 'Hello':
    print(letter)

# tuple unpacking
mylist = [(1,2),(3,4),(5,6),(7,8)]
for (a,b) in mylist: # assigns elements in tuple to variables
    # by using same shape as tuple
    print(a)
    print(b)

# dictionary iteration
d = {'k1':1, 'k2': 2, 'k3': 3}

for item in d: # this code will iterate through keys only
    print(item)

for item in d.items(): # will print out dictionary items 
    # i.e. the key and the value
    print(item)

for item in d.values(): # will print values
    print(item)
