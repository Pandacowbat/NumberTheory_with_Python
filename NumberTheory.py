#Chapter 1
import math
def quadratic_soln(a,b,c):
    d=(b*b)-(4*a*c)
    if(d<0):
        return d,0,0
    root1= (-b + math.sqrt(d))/(2*a)
    root2= (-b - math.sqrt(d))/(2*a)
    return d,root1,root2
def checktriangular(num):
    if num<0:
        return False
    a=1
    b=1
    c=(-2*num)
    d,root1,root2=quadratic_soln(a,b,c)
    if d<0:
        return False
    elif (root1>0 and math.floor(root1)==root1):
        return True
    elif (root2>0 and math.floor(root2)==root2):
        return True
    else:
        return False
def chapter1():
    print("What can I help you with?\n")
    while True:
        option_selected=input("Available options:"
                +"\n1.Check if a number is triangular."
                +"\n2.Find the nth triangular number."
                +"\n3.Find out whether a number is prime or not."
                +"\n4.Find the sum of n natural numbers.")
        if (option_selected=='1'):
            num=int(input("What number would you like to check?"))
            x=checktriangular(num)
            if(x==True):
                print("The number you entered is triangular!")
            else:
                print("The number you entered isn't triangular.")
        else:
            print("Not getting 1")
        break
chapter1()
