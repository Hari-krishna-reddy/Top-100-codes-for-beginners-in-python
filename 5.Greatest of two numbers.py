# Greatest of two numbers
n1=int(input('Enter 1st number:'))
n2=int(input('Enter 2nd number:'))
if n1>n2:
    print(n1,'is grater than',n2)
elif n1<n2:
    print(n2,'is grater than',n1)
else:
    print(n1,'is equals to',n2)
    
    
    ''' OR'''
# Approach 2
n1=int(input('Enter 1st number:'))
n2=int(input('Enter 2nd number:'))
grater_num=n1 if n1>n2 else n2
print('grater number between',n1,'and',n2,'is',grater_num)

    