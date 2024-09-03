#Find the Nth Term of the Fibonacci Series
n=int(input('Enter a number:'))
if n<=0:
    print('No fibonacci numbers are available')
elif n==1:
    print(0)
elif n==2:
    print(1)
else:
    n1=0
    n2=1
    for i in range(3,n+1):
        n3=n1+n2
        n1=n2
        n2=n3
    print(n3)