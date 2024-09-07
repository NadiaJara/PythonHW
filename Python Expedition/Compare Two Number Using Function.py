# compareTwoNumber is called  user define function
# a and b is called parameter

a = input("Please provide value of a: ")
b = input("Please provide value of b: ")


def compareTwoNumber():
    a = input("a: ")
    b = input("b: ")

if a > b:
    print(a, "is greater than", b)
elif a < b:
    print(a, "is less than", b)  
elif a == b:
    print(a, "is equal to", b)
else:
    print("The system failed to execute this order")  

# here two value is called argument
# compareTwoNumber(2312, 2312)  
# compareTwoNumber(312, 34)  
# compareTwoNumber(12, 55)  
compareTwoNumber(a, b)


 