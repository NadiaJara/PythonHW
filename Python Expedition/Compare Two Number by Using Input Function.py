
# we can use input function to provide value from terminal as we wish
a = input("Please provide value of a: ")
b = input("Please provide value of b: ")

if a > b:
    print(a, "is greater than", b)
elif a < b:
    print(a, "is less than", b)  
elif a == b:
    print(a, "is equal to", b)
else:
    print("The system failed to execute this order")    