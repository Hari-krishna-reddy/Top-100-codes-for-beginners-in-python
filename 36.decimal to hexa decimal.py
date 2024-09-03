decimal_num=int(input('Enter a decimal number'))
hexa_decimal=''
while decimal_num>16:
    if decimal_num%2<10:
        hexa_decimal=str(decimal_num%16)+hexa_decimal
    else:
        if decimal_num%16==10:
            hexa_decimal='A'+hexa_decimal
        if decimal_num%16==11:
            hexa_decimal='B'+hexa_decimal
        if decimal_num%16==12:
            hexa_decimal='C'+hexa_decimal
        if decimal_num%16==13:
            hexa_decimal='D'+hexa_decimal
        if decimal_num%16==14:
            hexa_decimal='E'+hexa_decimal
        if decimal_num%16==15:
            hexa_decimal='f'+hexa_decimal
    decimal_num//=16
hexa_decimal=str(decimal_num)+hexa_decimal
print(hexa_decimal)


#Approach2
decimal_num=int(input('Enter a decimal number'))
ans=hex(decimal_num)[2:]
print(ans)


        
