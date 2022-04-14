#Python program to solve a quadratic equation
#Solution of a quadratic equation is (-b ± (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
import math
def quadeq():
    print("The quadratic equation is ax^2+bx+c=0")
    a=int(input("Enter the value a: "))
    b=int(input("Enter the value b: "))
    c=int(input("Enter the value c: "))
    sol1=(-b+(b**2-4*a*c)**0.5)/(2*a)
    sol2=(-b+(b**2-4*a*c)**0.5)/(2*a)
    print("Solution of {0}x^2+{1}x+{2} is {3} & {4}".format(a,b,c,round(sol1,2),round(sol2,2)))
quadeq()
