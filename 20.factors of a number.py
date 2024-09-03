#factors of a number
num=int(input('Enter a number:'))
factors=[]
for i in range(1,num+1):
    if num%i==0:
        factors.append(i)
print('factors of',num,'are',factors)


#OR
#Approach 2 with less runtime
#factors of a number
num=int(input('Enter a number:'))
factors=[]
for i in range(1,(num//2)):
    if num//i in factors or i in factors:
            break
    if num%i==0:
        factors.append(i)
        factors.append(num//i) #Eg: if if 2 if a fa
print('factors of',num,'are',factors)

        