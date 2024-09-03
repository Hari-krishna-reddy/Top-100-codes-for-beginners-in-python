# Factorial of a number
num=int(input('Enter a number:'))
if num<0:
    print('factorial is not possible for negative numbers')
elif num==0 or num==1:
    print('factorial of',num,'is',1)
else:
    fact=1
    for i in range(2,num+1):
        fact*=i
    print('factorial of',num,'is',fact)
    
#OR
#Approach 2
def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)
num=int(input('Enter a number:'))
print('factorial of',num,'is',factorial(num))


    