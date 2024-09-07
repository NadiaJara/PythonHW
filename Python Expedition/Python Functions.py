# print() is a function that came from python library
# len() to know the length of the String
# type()
print("Hello")
print(len("Hello"))

# user define function

def myFunction():
    print("This is my first created function")

myFunction() 

empName = "Alex Wu"
empId = 352
empSalary = 5568346.563
fullTimeEmployee = True

def empInfo():
    print(empName)
    print(empId)
    print(empSalary)
    print(fullTimeEmployee)

empInfo()   

# Another way

def emp_info():
    x = f"Employee Name: {empName.upper()}, Employee Id: {empId}, Employee Salary: {empSalary:,.2f} \nFull Time Employee: {fullTimeEmployee}"
    print(x)
emp_info()