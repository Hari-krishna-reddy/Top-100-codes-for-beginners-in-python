#Binary to decimal number
#Approach 1 (binary number is given as string)
def octal_to_decimal(oct_num):
    l=len(oct_num)
    decimal_num=0
    for i in range(len(oct_num)):
        decimal_num=decimal_num+int(oct_num[i])*(8**(l-1-i))
    return decimal_num
oct_num=input('Enter an octal number:')
print('Decimal number for',oct_num,'is:',octal_to_decimal(oct_num))

#Approch 2
oct_num=input('Enter a binary number:')
decimal_num=int(oct_num,8)#for binary we use int(bin_num,2),for octal we use int(octal_num,8)
print('Decimal number for',oct_num,'is:',decimal_num)

#Approach 3
oct_num=input('Enter a binary number:')
decimal_num=eval('0o'+oct_num)#for binary we use eval('0b'+bin_num),for octal we use eval('0o'+octal_num)
print('Decimal number for',oct_num,'is:',decimal_num)#for hexa decimal we use eval('0x'+hexadecimal_num)

#Approach 4 (if octal number is given as intger as an input
oct_num=int(input('Enter a binary number:'))
decimal_num=0
oct_num_copy=oct_num
i=0
while oct_num>0:
    last_digit_of_oct_num=oct_num%10
    decimal_num+=last_digit_of_oct_num*(8**i)
    i+=1
    oct_num//=10
print('Decimal number for',oct_num_copy,'is:',decimal_num)
    