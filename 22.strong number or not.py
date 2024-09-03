#strong number or not

# Example
# Input : 145
# Output : It's a Strong Number.
# Explanation : Number = 145
# 145 = 1! + 4! + 5!
# 145 = 1 + 24 + 120



# logic for factorial of a number
def factorial(num):
    if num<=1:
        return 1
    return num*factorial(num-1)

#logic for strong number
n=int(input('Enter a number:'))
num1=n
sum=0
while n>0:
    last_digit_of_n=n%10
    sum+=factorial(last_digit_of_n)
    n//=10
if num1==sum:
    print(num1,'is a strong number')
else:
    print(num1,'is not a strong number')