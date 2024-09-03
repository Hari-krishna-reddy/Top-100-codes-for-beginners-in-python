#perfect number or not

# Example
# Input : 28
# Divisors : [1, 2, 4, 7, 14]
# Sum = 1 + 2 + 4 + 7 + 14 = 28
# Output : It's a Perfect Number
num=int(input('Enter a number:'))
factors=[1]
for i in range(2,num):
    if num%i==0:
        if i in factors or num//i in factors:
            break
        factors.append(i)
        factors.append(num//i)
if sum(factors)==num: #Here sum is a built-in function to fin sum of numbers in a list
    print(num,'is a perfect number')
else:
    print(num,'is not a perfect number')
    