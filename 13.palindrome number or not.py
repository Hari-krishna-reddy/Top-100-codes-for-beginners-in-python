#palindrome number or not

num=int(input('Enter a number:'))
num1=num
reverse=0
while num>0:
    last_digit_of_num=num%10
    reverse=reverse*10+last_digit_of_num
    num//=10
if num1==reverse:
    print(num1,'is the palindrome number')
else:
    print(num1,'Not a palindrome number')
    
    
    
          #Or
#approach 2
num=int(input('Enter a number:'))
if int(str(num)[::-1])==num:
    print(num,'is the palindrome number')
else:
    print(num,'Not a palindrome number')
