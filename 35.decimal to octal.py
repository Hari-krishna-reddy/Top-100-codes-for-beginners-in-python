decimal_num=int(input('Enter a decimal number'))
octal=''
while decimal_num>8:
    octal=str(decimal_num%8)
    decimal_num//=8
octal=str(decimal_num)+octal
print(octal)


#Approach2
decimal_num=int(input('Enter a decimal number'))
ans=oct(decimal_num)[2:]
print(ans)


        
