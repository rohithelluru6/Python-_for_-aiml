
a = int(input("enter the first angle: "))
b = int(input("enter the second angle: "))
c = 180-(a+b)

if c == 90:
 print("it is right angled triangle")
elif c == 60:
    print("it is isosceles triangle")
else :
    print("it is a triangle")
