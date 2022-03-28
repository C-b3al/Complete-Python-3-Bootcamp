#### Uncategorised useful operators

# range - generate a list of integers
mylist = list(range(1,11,3)) # start,stop,step size
print(mylist)

# enumerate - controls loop size by auto indexing conditions
for i,letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i,letter))
# can use tuple unpacking 

print(list(enumerate('abcde')))

# zip - create a list of tuples by using the zip function
mylist1 = [1,2,3,4,5]
mylist2 = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h']
print(list(zip(mylist1,mylist2)))
# zip will only create tuples for indices with two values present, and will ignore extra values

# in - check if an object is present; returns a boolean
print("Answer to print('x' in ['x','y','z']: ", 'x' in ['x','y','z'])
print("Answer to print('x' in [1,2,3]): ", 'x' in [1,2,3])

# not in - opposite of in
print("Answer to 'x' not in ['x','y','z']: ", 'x' not in ['x','y','z'])
print("Answer to 'x'not in [1,2,3]: ", 'x'not in [1,2,3])

# min and max - check minimum and maximum
mylist = [10,20,30,40,100]
print(min(mylist))
print(max(mylist))

# random - this is a library containing lots of useful functions
from random import shuffle
shuffle(mylist) # operation done in place
print(mylist)

from random import randint
print(randint(0,100)) # prints random integer in range 0-100

# input - receives user-generated inputs
hello = input('Say hi: ')
print(hello)
