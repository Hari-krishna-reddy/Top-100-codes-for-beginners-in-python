def armstrong(num):
    l=len(str(num))
    s=sum(int(digit)**l for digit in str(num))
    if s==num:
        return True
    else:
        return False
    
    
low=int(input('Enter lower number:'))
high=int(input('Enter higher number:'))
for i in range(low,high+1):
    if armstrong(i):
        print(i," ",end='')