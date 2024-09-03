import math
def prime(num):
    if num<=3:
        return True
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True

print('2-->',end='')
for i in range(3,100,1):# all the even numbers are not prime except 2
    if prime(i):
        print(i,end='-->')
