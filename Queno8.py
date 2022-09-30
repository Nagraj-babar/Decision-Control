# Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots
a=int(input("Enter a value a: "))
b=int(input("Enter a value b:"))
c=int(input("Enter a value c"))
d=(b * b) - (4 * a * c)
if d==0:
    print("real root")
elif d>0:
    print("two real root")   
elif  d<0:
    print("Two complex root")    