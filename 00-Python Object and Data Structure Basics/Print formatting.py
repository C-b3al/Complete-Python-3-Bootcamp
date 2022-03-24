# using .format()
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

# f strings - allows you to format with using .format
name = 'Ciaran'
print(f'Hello my name is {name}')
age = 22
print (f'{name} is {age} years old')
