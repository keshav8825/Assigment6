#. Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots
print("Enter quadratic equation")
a=int(input("enter cofficent of x**2 "))
b=int(input("enter cofficent of x "))
c=int(input("enter constant value "))
d=b**2-4*a*c
if d>0:
    print("real and dinstinct root")
elif d<0:
    print("imaginary roots")
else:
    print("real and equal root")
    

