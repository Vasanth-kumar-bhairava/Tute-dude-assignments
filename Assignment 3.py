#Task 1
def factorial():
    x=int(input("Enter a number:"))
    y=1
    for x in range(1,x+1):
        y*=x
    print("Factorial of",x,"is",y)    

factorial()

#Task 2

import math

x=int(input("Enter the number :"))
print("Square root:",math.sqrt(x),"\nLogarithm:",math.log(x),"\nSine:",math.sin(x))



