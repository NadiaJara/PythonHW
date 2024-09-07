# [] called square bracket
# the first character has 0 index
# Specify the start index and the end index, separated by a colon, to return the part (slice) of the string. Note: the first character has 0 index and the end index is not included
x = "Pack my box with five liquor jugs"
print(len(x))
print(x[2:10]) 

print(x[0:39])

print(x[:10]) # this represents start from 0, and end index is excluded
print(x[5:]) # this represents start index 0, and index is last index which is not included

print(x[0:60]) # although we know that the length is 39, we wrote 60

# Negative indexing
# first index: 0
# last index: -1
# we can use negative indexes to start the slice from the end of the string
print(x[-10:-1])