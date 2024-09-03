# Permutations in which n people can occupy r seats in a classroom
import math
n=int(input('Enter number of students:'))
r=int(input('Enter number of chairs:'))
# formulae n!/(n-r)!
print(math.perm(n,r))