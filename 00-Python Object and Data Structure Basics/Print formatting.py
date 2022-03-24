#### using .format()
print('This is a string {}'.format('inserted'))
print('The {} {} {}'.format('big', 'fat', 'ass'))
# using index positions to call string inserts
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
# using keywords to call string inserts
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

# float formatting with .format()
result = 100/777
print('The result was {r:1.3f}'.format(r = result))
# format is {value:width.precision f}
# so the above example rounds to 3 dp with a width of 1
# width adds whitespace before the number
print('The result was {r:0.5f}'.format(r = result)) # playing around

#### f strings - allows you to format with using .format
name = 'Ciaran'
print(f'Hello my name is {name}')
age = 22
print (f'{name} is {age} years old')
# float formatting with f strings
my_fav_num =  24.6578123485323
print(f'My favourite number is: \n {my_fav_num:{10}.{6}}')
# the precision is now the number of characters

#### padding and precision of floating point numbers
print('Floating point numbers: %5.2f' %(13.144))
# the 5 is the minimum number of characters the string should contain
# if it doesn't contain this number then it will pad with whitespace
# the .2f indicates the number of decimal points
print('Floating point numbers: %1.0f' %(13.144))
print('Floating point numbers: %1.5f' %(13.144))
print('Floating point numbers: %10.2f' %(13.144))
print('Floating point numbers: %25.2f' %(13.144))


#### alignment and padding with .format()
print('{0:<8} | {1:^8} | {2:>8}'.format('Left','Center','Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11,22,33))
# .format() deautls to left alighment for text, right for numbers
# using < ^ > you can change alightment to left, centre or right
print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:9}'.format('Apples', 3.))
print('{0:8} | {1:9}'.format('Oranges', 10))
# the numbers in the brackets are used to pad strings
# they set the lengths of the string fields
# Quantity takes up all but one of the field spaces
