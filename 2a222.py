import math
x=int(input("x ni kiriting: "))
n=int(input("n ni kiriting: "))
y=(((-1)**n)*x**(2*n+1))/(math.factorial(2*n))
print("natija: ",y)