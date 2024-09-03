#Lcm of 2 numbers
#Lcm(num1,num2)=(num1*num2)/hcf
def hcf(a,b):
    while b:
        a,b=b,a%b
    return a
        
        
num1=int(input('Enter a number:'))
num2=int(input('Enter second number:'))
lcm=(num1*num2)/hcf(num1,num2)
print(lcm,'is the lcm of',num1,num2)

#Approach 2
num1=int(input('Enter a number:'))
num2=int(input('Enter second number:'))
for i in range(max(num1,num2),num1*num2,max(num1,num2)):
    if i%num1==0 and i%num2==0:
        print(i,'is the lcm of',num1,num2)
        break
        


