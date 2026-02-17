n=int(input("enter the number: "))
a=n
reverse=0
while n>0:
    number=n%10
    reverse=reverse*10+number
    n//=10
print(reverse)
c=reverse-a
print(c)
