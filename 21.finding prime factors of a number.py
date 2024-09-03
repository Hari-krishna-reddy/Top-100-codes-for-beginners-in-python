import math
#Logic for prime number or not
def prime(num):
    if num<=3:
        return True
    else:
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                return False
        return True



#finding prime factors of a number
num=int(input('Enter a number:'))
factors=[]
for i in range(1,num+1):
    if num%i==0 and prime(i):
        factors.append(i)
print('prime factors of',num,'are',factors)


#OR
#Approach 2 with less runtime
#finding prime factors of a number
num=int(input('Enter a number:'))
factors=[]
for i in range(1,(num//2)):
    if num//i in factors or i in factors:
            break
    if num%i==0:
        if prime(i):
            factors.append(i)
        if prime(num//i):
            factors.append(num//i) #Eg: if if 2 if a fa
print('prime factors of',num,'are',factors)

        
