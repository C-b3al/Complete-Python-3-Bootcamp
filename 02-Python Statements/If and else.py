#### if elif and else
# pay attention to identation

x = True
if x:
    print( 'True')
else: # only executes when if statement doesn't
    print( 'False')

hungry = False
if hungry:
    print('Feed me')
else:
    print("I'm not hungry")

loc = 'Bank'
if loc == 'Supermarket':
    print('Shopping time')
elif loc == 'Bank':
    print("I'm rich!")
else:
    print('Pizza at home')
