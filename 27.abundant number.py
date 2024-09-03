#Abundant number
# Example
# Input : Number = 12
# Output : Yes, It's an Abundant Number
# Explanation : The Factors for the number 12 are, 1, 2, 3, 4 and 6.
#We don't want to include the number itself.
# Now the sum of the factors except the number itself is :
# 1 + 2 + 3 + 4 + 6 = 16
# as the number 16>12 , the number itself.
# It's an abundant number.
num=int(input('Enter a number:'))
factors=[]
for i in range(1,num):
    if num%i==0:
        factors.append(i)
s=sum(factors) #here sum is built in function to add all numbers in a list
if s<num:
    print(num,'is Abundant')
else:
    print(num,'is not an abundant number')