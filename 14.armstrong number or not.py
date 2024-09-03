#Armstrong number or not
num=int(input('Enter a number:'))
num1=num
l=len(str(num))
s=0
while num>0:
    last_digit_of_num=num%10
    s+=last_digit_of_num**l
    num//=10
if num1==s:
    print(num1,'is an armstrong number')
else:
    print(num1,'is not an armstrong number')
    
    
# OR
#approach 2

num=int(input('Enter a number:'))
length=len(str(num))
s=0
for i in str(num):
    s+=int(i)**length
if num==s:
    print(num,'is an armstrong number')
else:
    print(num,'is not an armstrong number')
    
    
    # OR
#approach 2

num=int(input('Enter a number:'))
length=len(str(num))
s=sum([int(digit)**length for digit in str(num)])


if s==num:
    print(num,'is an armstrong number')
else:
    print(num,'is not an armstrong number')

    
    


    
    