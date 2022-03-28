#### List Comprehensions
# allow list-building by using for loops inside a list
wordlist = [x for x in 'word']
print(wordlist)

lst = [x**2 for x in range(0,11)]
print(lst)

# incorporating ifs
lst = [x for x in range(11) if x % 2 == 0]
lst

# convert celsius to fahrenheit
celsius = [0,10,20.1,34.5]

fahrenheit = [((9/5)*temp + 32) for temp in celsius ]

print(fahrenheit)

# it's possible to nest list comprehensions
lst = [ x**2 for x in [x**2 for x in range(11)]]
print(lst)

