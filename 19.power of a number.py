# power of a number
base=int(input('Enter base value:'))
power=int(input('Enter power value:'))
ans=1
for i in range(power):
    ans*=base
print(base,'power',power,'is',ans,'using loops')

#OR
#Approach 2 using built in function pow(base,power)
print(base,'power',power,'is',pow(base,power),'using built_in pow() function')

#OR
#Approach 3 using power operator **
print(base,'power',power,'is',base**power,'using power operator **')

#OR
#Approach 4 using recursion
def power_number(base,power):
    if power==0:
        return 1
    else:
        return base*power_number(base,power-1)
print(base,'power',power,'is',power_number(base,power),'using recursion')



