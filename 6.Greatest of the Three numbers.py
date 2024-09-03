#Greatest of the Three numbers
n1=int(input('Enter 1st number:'))
n2=int(input('Enter 2nd number:'))
n3=int(input('Enter 3rd number:'))
if n1>n2 and n1>n3:
    print(n1,'is grater than',n2,n3)
elif n2>n3:
    print(n2,'is grater than',n1,n3)
else:
    print(n3,'is grater than',n1,n2)
    
    
#Approach 2
n1=int(input('Enter 1st number:'))
n2=int(input('Enter 2nd number:'))
n3=int(input('Enter 3rd number:'))
gratest_num=n1 if n1>n2 and n1>n3 else n2 if n2>n3 else n3
print('grater number among',n1,n2,'and',n3,'is',grater_num)

    
    