# For the first person, there will be N-1 people to shake hands with
# For second person, there will be N -1 people available
# but as he has already shaken hands with the first person,
# there will be N-1-1 = N-2 shake-hands
# For third person, there will be N-1-1-1 = N-3, and So On…
# Therefore the total number of handshake=( N – 1 + N – 2 +….+ 1)= ((N-1)* N)/2.
n=int(input('Enter no of persons:'))
print('Total no of hand shakes are:',int((n*(n-1))/2))
