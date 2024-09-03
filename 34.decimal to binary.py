decimal_num=int(input('Enter a decimal number'))
binary=''
while decimal_num!=1:
    if decimal_num%2==0:
        binary='0'+binary
    else:
        binary='1'+binary
    decimal_num//=2
binary='1'+binary
print(binary)


#Approach2
decimal_num=int(input('Enter a decimal number'))
ans=bin(decimal_num)[2:]
print(ans)


        