# reverse of a number
num=int(input('Enter a number:'))
num1=num
reverse=0
while num>0:
    last_digit_of_num=num%10
    reverse=reverse*10+last_digit_of_num
    num//=10
print('reverse of the number',num1,'is',reverse)

          #Or
#approach 2
num=int(input('Enter a number:'))
reverse=int(str(num)[::-1])
print('reverse of the number',num,'is',reverse)


