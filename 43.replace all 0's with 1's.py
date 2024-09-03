#Replace all 0'swith 1's
def reverse_of_num(num):
    ans=0
    while num>0:
        last_digit=num%10
        ans=ans*10+last_digit
        num//=10
    return ans



num=int(input('Enter a number:'))
print(num,end='')
value=0
if num==0:
    value=1
else:
    while num>0:
        last_digit=num%10
        if last_digit==0:
            value=value*10+1
        elif last_digit==1:
            value=value*10+0
        else:
            value=value*10+last_digit
        num//=10
print(" after replacing 0's with 1's and 1's with 0's is",reverse_of_num(value))


#Approach 2 using list
num=int(input('Enter a number:'))
l=[int(i) for i in str(num)]
ans=[]
for i in l:
    if i==0:
        ans.append(1)
    elif i==1:
        ans.append(0)
    else:
        ans.append(i)
val=0
for i in ans:
    val=val*10+i
print(val)
        

        