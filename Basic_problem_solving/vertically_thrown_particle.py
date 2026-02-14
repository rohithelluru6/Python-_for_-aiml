# code
g=9.8
def caluclate_time(u):
    T=2*u/g
    return T
u=int(input("enter the velocity"))
V=caluclate_time(u)
print("velocity of particle",V)
    
