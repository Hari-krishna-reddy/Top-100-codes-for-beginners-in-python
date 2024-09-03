#reverse of a number using recursion
def rev(num,ans=0):
    if num==0:
        return ans
    else:
        return rev(num//10,ans*10+(num%10))
    
print(rev(123))