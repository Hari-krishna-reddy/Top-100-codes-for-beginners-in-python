#Hexadecimal to decimal
def hexadecimal_to_decimal(hex_num):
    l=len(hex_num)
    decimal_num=0
    for i in range(len(hex_num)):
        if ord(hex_num[i])<58:
            decimal_num=decimal_num+int(hex_num[i])*(16**(l-1-i))
        else:
            if hex_num[i]=='a' or hex_num[i]=='A':
                decimal_num=decimal_num+10*(16**(l-1-i))
            if hex_num[i]=='b' or hex_num[i]=='B':
                decimal_num=decimal_num+11*(16**(l-1-i))
            if hex_num[i]=='c' or hex_num[i]=='C':
                decimal_num=decimal_num+12*(16**(l-1-i))
            if hex_num[i]=='d' or hex_num[i]=='D':
                decimal_num=decimal_num+13*(16**(l-1-i))
            if hex_num[i]=='e' or hex_num[i]=='E':
                decimal_num=decimal_num+14*(16**(l-1-i))
            if hex_num[i]=='f' or hex_num[i]=='F':
                decimal_num=decimal_num+15*(16**(l-1-i))
                
    return decimal_num
hex_num=input('Enter a hexadecimal  number:')
print('Decimal number for',hex_num,'is:',hexadecimal_to_decimal(hex_num))

#Approach2
hex_num=input('Enter a hexadecimal number:')
decimal_num=int(hex_num,16)#for binary we use int(bin_num,2),for octal we use int(octal_num,8) for hex_decimal) we use int(hex_num,16
print('Decimal number for',hex_num,'is:',decimal_num)


#Approach 3
hex_num=input('Enter a hexadecimal number:')
decimal_num=eval('0x'+oct_num)#for binary we use eval('0b'+bin_num),for octal we use eval('0o'+octal_num)
print('Decimal number for',hex_num,'is:',decimal_num)#for hexa decimal we use eval('0x'+hexadecimal_num)