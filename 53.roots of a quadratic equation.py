#Roots of quadratic equation
import math
a=int(input('Enter co-efficient of a:'))
b=int(input('Enter co-efficient of b:'))
c=int(input('Enter co-efficient of c:'))
delta=b**2-4*a*c
if delta<0:
    print('There are no real roots for given quadratic equation')
elif delta==0:
    print('The roots are real and equal,they are:',int(-b/2*a),(-b/2*a))
else:
    r1=(-b+math.sqrt(delta))/2*a
    r2=(-b-math.sqrt(delta))/2*a
    print('The roots are real and dinstinct and they are:',int(r1),',',int(r2))
