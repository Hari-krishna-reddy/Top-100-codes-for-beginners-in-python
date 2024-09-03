# friendly pair
# Example
# Input : 6 28
# Output : Yes, they are a friendly pair
# Explanation : The factors of 6 and 28 except the numbers themselves
# are 1, 2, 3 and 1, 2, 4, 7, 14respectively.
# Now the sum of factors of both the numbers are 6 and 28 respectively. 
# When we divide the sums with the numbers we get 1 and 1 respectively. 
# As the ratio of both the number match, they are considered as a friendly pair.
def factor_sum(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    return sum
            




num1,num2=(int(i) for i in input('Enter two numbers:').split())
if (factor_sum(num1)/num1)==(factor_sum(num2)/num2):
    print(num1,num2,'are friendly pair')
else:
    print(num1,num2,'are not friendly pair')
