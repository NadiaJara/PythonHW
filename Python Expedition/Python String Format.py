fName = "Nadia"
lName = "Jara"
age = 13

print(fName + lName)
# print(fName + age) can only concatenate str to str (not "int" to str)
print(fName, age) # this is ok

# can't concatenate str to "int"
# print("My Name: " + fName + " " + lName + ", Age: " + age)

# Python Format String
fName = "Nadia"
lName = "Jara"
age = 13
salary = 125000

# by formatting text, we can get an outcome of String and other data types
# this {} is called place holder
outcome = f"My Name is {fName} {lName} and my age is {age} and my salary is {salary}"
print(outcome)

cost1 = 4
print(f"Fuel price: {cost1:.2f}$")

cost2 = 5
total1 = f"Gas price: {cost2:.3f}$"
print(total1)

cost3 = 6
total2 = f"Gas price: {cost1 * cost2 + cost3}$"
print(total2)