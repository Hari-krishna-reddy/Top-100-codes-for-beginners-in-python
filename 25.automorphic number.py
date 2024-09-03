#Automorphic number
# Example
# Input : number = 5
# Output : It's an Automorphic number.
# Explanation : Number = 5
# Square of number = 25
# as the square of the number ends with the number itself, It's an Automorphic number.
num=int(input('Enter a number:'))
ans='Auto-morphic' if (num*num)%10==num else 'Non auto-morphic'
print(num,'is',ans)