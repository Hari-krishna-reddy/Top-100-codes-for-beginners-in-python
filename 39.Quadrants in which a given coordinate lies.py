# Quadrants in which a given coordinate lies
x=int(input('Enter x co-ordinate value:'))
y=int(input('Enter y co-ordinate value:'))
if x>0:
    if y>0:
        print('q1')
    elif y<0:
        print('q4')
    else:
        print('x axis')
elif x<0:
    if y>0:
        print('q2')
    elif y<0:
        print('q3')
    else:
        print('y axis')
else:
    if y==0:
        print('origin')
    else:
        print('y axis')
    

