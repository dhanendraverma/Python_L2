

import math

def cos(x):
    return math.cos(x)

def sin(x):
    return math.sin(x)

def tan(x):
    return math.tan(x)

def degree_to_radian(x):
    return math.radians(x)

def log_base10(x):
    try:
        return math.log10(x)
    except ValueError:
        return('log base 10 can be calculated only for numbers greater than 0')

def factorial(x):
    if x<0:
        return('Factorial can be calculated only for postive numbers')
    elif x==0:
        return 1
    else:
        temp=1
        for i in range(1,x+1):
            temp=temp*i
        return temp
