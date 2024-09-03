# prime numbers with in a range
import math
def prime(n):
    if n<=2:
        return True
    else:
        for j in range(2,int(math.sqrt(n)+1)):
            if n%j==0:
                return False
        return True







low=int(input('Enter lower num:'))
high=int(input('Enter higher num:'))
for i in range(low,high+1):
    if prime(i):
        print(i,'--',end='')