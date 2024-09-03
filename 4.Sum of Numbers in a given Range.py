#Sum of Numbers in a given Range
n1=int(input('Enter lower number in range:'))
n2=int(input('Enter upper number in range:'))
sum=0
for i in range(n1,n2+1):
    sum+=i
print('sum of numbers in range',n1,'and',n2,'is:',sum)