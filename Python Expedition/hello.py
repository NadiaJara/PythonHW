# this is an example of single-line comment
# shortcut: control + /

"""
When we use 3 double quotation/3 single quotation, it creates multiple-line comments

"""

'''
Here, we used 3 single quotation

'''

# print() is called a function
# more specifically library function bc it came from python library
print("Hello World!!")
print('Good Afternoon') # single quotation is ok too

print("Nadia")
print(13)
print(4.000)

# here name is a variable, which is holding a data
print("--------------------------------------------------")
name = "Sabia"
age = 9
grade = 4.000
usCitizen = True

# above 4 data isn't the same 

print(name)
print(age)
print(grade)
print(usCitizen)

print("--------------------------------------------------")
print(type(name)) # str represent string/text type, represented by double quotation
print(type(age))  # int represent integer/numeric type, represented by no quotation
print(type(grade))  # float represent float/numeric type, represented by no quotation
print(type(usCitizen))  # bool represent boolean type [true/false], represented by no quotation

# naming convention of variable
# we have to assign a value for a variable
x = 483
y = 488

# variables are case sensitive, myName and MYname isn't same
myName = "Hi"
MYname = "hi"
print(myName)
print(MYname)

# how to write 2/3 words inside variable name
# alpha-numeric characters means that alpha and number character both allowed
# a variable name can't start with a number
my1var = "Fatema"

# how to write multi words inside variable name
# CamelCase, Snake case, and pascal case
# Example of CamelCase -- myName
# Generally, variable name starts with lowder case, but this isn't a rule
myName = "Bill"
myAge = 11
myGradeScore = 3.01

# Example of pascal case -- MyName
MyName = "Nadia"
MyAge = 13
MyGradeScore = 3.01

# Example of snake case -- my_name
my_name = "Sabia"
my_age = 9
my_grade_score = 3.886

# CamelCase and snakecase is most popular and used in the industry

print("--------------------------------------------------")
# variables can even change type after they have been set
x = 483 # int type
x = 483.0 # float type
print(x)
print(type(x))

y = 510
y = "Fatema"
print(y) # int type
print(type(y)) # str type
# because interpreter converts source code to binary code line by line, last statement will be executed

# What is casting
x = 4
print(x)
print(type(x))

y = str(4) # we cast int type to a string type
print(type(y))

z = bool("Bill")
print(type(z))

# although the data type is different, casting allows us to get a new data type