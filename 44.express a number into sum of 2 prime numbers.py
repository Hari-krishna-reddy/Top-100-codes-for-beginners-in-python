import math
def prime(num):
    if num<=2:
        return True
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True






num=int(input('Enter a number which i greater than 2 and a even number:'))
prime_pairs=[]
if num%2==0 and num>2:
    for i in range(2,(num//2)+1):
        if prime(i) and prime(num-i):
            prime_pairs.append((i,num-i))
else:
    print('you entered wrong number')
print(prime_pairs,'are the prime pairs and sum of those two numbers are',num)