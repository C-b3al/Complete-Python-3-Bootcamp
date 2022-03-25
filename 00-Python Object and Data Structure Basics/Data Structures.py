#### Lists

my_list = [1,2,3,4,5]
my_list_2 = ['String', 100, 23.2]
len(my_list)
# can use indexing and slicing
print(my_list[1])
print(my_list[1:])
# can concatenate lists
new_list = my_list + my_list_2
print(new_list)
new_list[1] = 'ONE' # list objects are mutable
new_list.append('six') # adds items to end of list
print(new_list)
new_list.pop() # removes and returns last list entry
print(new_list)
new_list.pop(1) # removes and returns index position 1
let_list = ['a','e','x','b','c']
num_list = [4,1,8,3,6]
print(let_list)
let_list.sort() # sorts let_list in place
print(let_list)
print(num_list)
num_list.sort() # sorts num_list in place
print(num_list)
num_list.reverse()
print('Reversed list: ', num_list)

list_1 = [1,2,3]
list_2 = [4,5,6]
list_3 = [7,8,9]
matrix = [list_1+list_2+list_3] # creates nested list
print(matrix)
print('First item, first list: ' , matrix[0][0])


#### Dictionaries

# stores values using key value pairs
# dictionaries cannot be sorted, lost slicing functionality

my_dict = {'key1':1, 'key2':2, 'key3':3}
print(my_dict['key1']) # prints value associated with this key

# very flexible in data types they can hold
my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
print(my_dict)
print(my_dict['key2'])
# key:value calls can be stacked to access nested objects
print('nested item: ' + my_dict['key3'][0])

# Dictionary nested inside a dictionary nested inside a dictionary
d = {'key1':{'nestkey':{'subnestkey':'value'}}}
print(d)
d['key1']['nestkey']['subnestkey']
print(d)

# adding in key value pairs
d = {'k1':100, 'k2':200}
print(d)
d['k3']=300
print(d)
d.keys() # returns all dictionary keys
d.values() # returns all values
d.items() # returns keys and values together

