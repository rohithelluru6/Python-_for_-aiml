# code
import math
def area_and_circumference_of_the_circle(r):
    area=math.pi*(r**2)
    circumference=2*math.pi*r
    return area,circumference
r=int(input("enter the radius of the circle: "))
A=area_and_circumference_of_the_circle(r)
print("area and circumference",A)
