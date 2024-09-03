#Harshad number
# Example
# Input : 21
# Output : Yes ' It's a Harshad Number.
# Explanation : The sum of the digits of 21 is 3 i.e 2 + 1.
# As the number 21 is divisible by 3, It's a Harshad Number.
num=int(input('Enter a number:'))
num1=num
sum=0
while num>0:
    last_digit_of_num=num%10
    sum+=last_digit_of_num
    num//=10
ans='Harshad number' if num1%sum==0 else 'Not a harshad number'
print(num1,'is',ans)