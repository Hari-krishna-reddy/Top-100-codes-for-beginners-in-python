#Finding Number of times x digit occurs in a given input
num=int(input('Enter a number:'))
x=int(input('Enter x value:'))
x_count=0
while num>0:
    last_digit=num%10
    if last_digit==x:
        x_count+=1
    num//=10
print(x,'count is:',x_count)