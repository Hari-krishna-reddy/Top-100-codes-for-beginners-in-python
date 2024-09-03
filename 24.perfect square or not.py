#perfect square or not
num=int(input('Enter a number:'))
ans='perfect' if int(num**(1/2))*int(num**(1/2))==num else 'not perfect'
print(num,'is',ans,'square')