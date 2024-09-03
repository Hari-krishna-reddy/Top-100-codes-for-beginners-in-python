#Hcf of two numbers
#https://chatgpt.com/share/afc06b76-1617-4def-8903-b88415682290 (use this link for explanation)

a=int(input('Enter a number:'))
x=a
b=int(input('Enter second number:'))
y=b
while b>0:
    a,b=b,a%b
print(a,'is the hcf of',x,y)

#Approach 2:(Continuous division
#Initialize HCF = 1
# Run a loop in the iteration of (i) between [2, min(num1, num2)+1]
# Note down the highest number that divides both num1 & num2
# If i satisfies (num1 % i == 0 and num2 % i == 0) then new value of HCF is i
# Print value of HCF
a=int(input('Enter a number:'))
b=int(input('Enter second number:'))
minimum=min(a,b)
hcf=1
for i in range(2,minimum+1):
    if a%i==0 and b%i==0:
        hcf=i
print(hcf,'is the hcf of',a,b)

#Approach 3 using recursion
def hcf(a,b):
    if b==0:
        return a
    return hcf(b,a%b)
print(hcf(2,10))

        
