#Binary to decimal number
#Approach 1 (binary number is given as string)
def binary_to_decimal(bin_num):
    l=len(bin_num)
    decimal_num=0
    for i in range(len(bin_num)):
        decimal_num=decimal_num+int(bin_num[i])*(2**(l-1-i))
    return decimal_num
bin_num=input('Enter a binary number:')
print('Decimal number for',bin_num,'is:',binary_to_decimal(bin_num))

#Approch 2
bin_num=input('Enter a binary number:')
decimal_num=int(bin_num,2)#for binary we use int(bin_num,2),for octal we use int(octal_num,8)
print('Decimal number for',bin_num,'is:',decimal_num)

#Approach 3
bin_num=input('Enter a binary number:')
decimal_num=eval('0b'+bin_num)#for binary we use eval('0b'+bin_num),for octal we use eval('0o'+octal_num)
print('Decimal number for',bin_num,'is:',decimal_num)#for hexa decimal we use eval('0x'+hexadecimal_num)

#Approach 4 (if binary number is given as intger as an input
bin_num=int(input('Enter a binary number:'))
decimal_num=0
bin_num_copy=bin_num
i=0
while bin_num>0:
    last_digit_of_bin_num=bin_num%10
    decimal_num+=last_digit_of_bin_num*(2**i)
    i+=1
    bin_num//=10
print('Decimal number for',bin_num_copy,'is:',decimal_num)
    