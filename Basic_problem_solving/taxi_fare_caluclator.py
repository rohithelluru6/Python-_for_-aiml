distance=float(input("enter the distance in kilometers: "))
if distance<=12:
    totalfare=100
    print(totalfare)
elif distance<=16:
    totalfare=100+(distance-12)*8
    print(totalfare)
elif distance<=20:
    totalfare=100+(4*8)+(distance-16)*6
    print(totalfare)
else:
    totalfare=100+(4*8)+(4*6)+(distance-20)*5
    print(totalfare)

    
