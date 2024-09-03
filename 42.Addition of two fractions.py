# Addition of two fractions 1/3 +3/9 =6/9=2/3

# (1 / 3) + (3 / 9) = (6 / 9) = (2 / 3)
# 
# Find LCM of 3 and 9 and the result will be 9.
# Multiply 3 in first fraction : (3 / 9) + (3 / 9)
# Add both fractions and then the result will be : (6 / 9)
# Now simplify it by finding the HCF of 6 and 9 and the result will be 3.
# So divide 6 and 9 by 3 and then the result will be : (2 / 3)
# This will be your simplified answer for the given problem.

def hcf(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def lcm(a,b):
    return (a*b)/hcf(a,b)



def addTwoFractions(a,b,c,d):
    if hcf(b,d)==1:
        numerator=a*d+b*c
        denominator=b*d
        e= numerator/hcf(numerator,denominator)
        f=denominator/hcf(numerator,denominator)
        print('e/f =',int(e),'/',int(f))
    else:
        value=lcm(b,d)
        numerator=a*(value/b)+c*(value/d)
        denominator=value
        e= numerator/hcf(numerator,denominator)
        f=denominator/hcf(numerator,denominator)
        print('e/f =',int(e),'/',int((f)))

a=int(input("Enter 'a' value in a/b fraction:"))
b=int(input("Enter 'a' value in a/b fraction:"))
c=int(input("Enter 'a' value in a/b fraction:"))
d=int(input("Enter 'a' value in a/b fraction:"))
addTwoFractions(a,b,c,d)
