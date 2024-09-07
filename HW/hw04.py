def areaOfTriangle(base = 7.7, height = 50):
    x = f"Base of Triangle: {base:,.1f} \nHeight of Triangle: {height}"
    area = 1/2 * base * height
    print("The area of the triangle: ")
    return print(area)
print(areaOfTriangle())



base = input("Base of Parallelogram: ")
height = input("Height of Parallelogram: ")


print("--------------------------------------")
def areaOfParallelogram(base, height):
    x = f"Base of Parallelogram: {base.upper()} Height of Parallelogram: {height}"
    value = base + height
    print("Area of Parallelogram: " + value)
    return print(value)

areaOfParallelogram(base, height)

