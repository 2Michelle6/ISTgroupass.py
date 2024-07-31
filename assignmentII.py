print ("Tracer")
import math

A=int(input("Enter coefficient A: "))
B=int(input("Enter coefficient B: "))
C=int(input("Enter coefficient C: "))
root= (B**2-4*A*C)


if root > 0:
    Root1 = (-B+math.sqrt(root)/(2.0*A))
    Root2 = (-B-math.sqrt(root)/(2.0*A))
    print(f"root1 is: {Root1} root 2 is {Root2}")
