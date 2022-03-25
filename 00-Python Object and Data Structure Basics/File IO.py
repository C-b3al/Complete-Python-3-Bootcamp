#### file I/O
# input and output of basic files

# creating a test text file in Jupyter (only works in Jupyter)
'''%%writefile myfile.txt
Hello this is a text file
This is the second line'''

# opening a file

test_file = open('test.txt')
# FileNotFoundError will result from entering wrong file name
# or not providing the same file path

# type 'pwd' into Jupyter cell to know the current directory
print(test_file.read()) # returns a long string of everything in txt file

# in order to read a file again you have to reset the cursor position
test_file.seek(0) # sets cursor back to 0 position
contents = test_file.read()
print(contents)
test_file.seek(0)
print('Line by line:', test_file.readlines())
# returns list of each line


# file locations
myfile = open("C:\\Users\\ceejo\\Documents\\Personal\\Private Studies\\Python\Complete-Python-3-Bootcamp\\00-Python Object and Data Structure Basics\\test.txt")
print(myfile)

# to avoid errors all files need to be closed once you're finished with them
test_file.close()
myfile.close()

# to get around this the following syntax is used:
with open('test.txt') as new_file:
    contents = new_file.read()
print(contents)

# reading and writing to files
with open('test.txt', mode='r') as myfile:
    contents = myfile.read() # reading file
print(contents) 
# mode is important: trying to read a file open with 'w' returns an error
file_options = ['a - append', 'w - overwrite', 'r - read',
'r+ - reading and writing',' w+ - writing and reading']
# w+ will create a new file for reading and writing if no file exists
print(file_options)

f = open('readme.txt', mode='w+')
f.write('this is a readme \n')
f.writelines(['Line one \n', 'Line two \n','Line three \n'])
f.seek(0)
fileread = f.read()
f.close()

print(fileread)

# creates new file called readme using w+ mode
# writes to it, then writes the 3 lines of the list to it
