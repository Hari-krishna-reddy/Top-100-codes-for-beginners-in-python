# Generate all cyclic permutations of a number
# Input :  123
# Output : 123
#          312
#          231
# 
# Input :  5674
# Output : 5674
#          4567
#          7456
#          6745
#Formulae to add last digit at first is after_add=pow(10,n-1)*remainder+num where n is the length of the number
def count_length(num):
    c=0
    while num:
        c+=1
        num//=10
    return c
import math

def cyclic_permutation(num):
    n=num
    c=count_length(num)
    while 1:
        rem=num%10
        num//=10
        ans=int(math.pow(10,c-1))*rem+num
        num=ans
        print(ans)
        if ans==n:
            return
cyclic_permutation(123)
