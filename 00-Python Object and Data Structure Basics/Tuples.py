#### tuples
# immutable - elements cannot be reassigned or removed
t = ('one',2,3.0)
my_list = [1,2,3]

len(t)
print(t[0])
print(t[-1])
t = ('a','a','b')
print(t.count('a')) # fewer function methods available for tuples
print(t.index('b'))
my_list[0] = 'new'
print(my_list)
t[0] = 'new' # will give error

# tuples useful when you need data integrity
# when you need data objects to stay the same throughout large pieces of code

