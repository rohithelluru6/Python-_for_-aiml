n=int(input("enter the number: "))
total_sum=0
for i in range(1,n+1):
    sum=((-1)**i)*((1/3)**i)
    total_sum+=sum
print("sum of series=",total_sum)
     
     
