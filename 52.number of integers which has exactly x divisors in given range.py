import math

def div_count(num):
    c=0
    for i in range(1,int(math.sqrt(num))+1):
        if num%i==0:
            c+=1
            if i!=num//i:
                c+=1
    return c
        




num=int(input('Enter range:'))
x=int(input('Enyer x value:'))
count=0
arr=[]
for i in range(1,num+1):
    if div_count(i)==x:
        count+=1
        arr.append(i)
        
print('The number of integers which has exactly',x,'divisiors in range',num,'is',count,'and  numbers are',arr)