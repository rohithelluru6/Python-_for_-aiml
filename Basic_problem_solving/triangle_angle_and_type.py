a1=float(input("enter the first angle: "))
a2=float(input("enter the second angle: "))
a3=180-a1-a2
print(a3)
if a1==a2 or a2==a3 or a1==a3:
    print("triangle is isoscles ")
elif a1==90 or a2==90 or a3==90:
    print("triangle is right angled triangle")
else:
    print("traingle is normal")
