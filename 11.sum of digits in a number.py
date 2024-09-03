#sum of digits in a number
num=int(input('Enter a number:'))
num1=num
sum=0
while num>0:
    last_digit_of_num=num%10
    sum+=last_digit_of_num
    num//=10
print('sum of the digits of',num1,'is',sum)


          #Or
#approach 2
num=int(input('Enter a number:'))
num1=num
sum=0
for i in str(num):
    sum+=int(i)
print('sum of the digits of',num1,'is',sum)

          