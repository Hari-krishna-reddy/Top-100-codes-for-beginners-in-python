#largest element in array using recursion
import math
def largest_element_arr(arr,m=-(math.inf)):

    if len(arr)==0:
        return m
    elif arr[0]>m:
        m=arr[0]
    return largest_element_arr(arr[1:],m)
    

print(largest_element_arr([1,2,10,10,3,4]))
        
        
#Approach 2
def largest(arr):
    m=-(math.inf)
    for i in arr:
        if i>m:
            m=i
    return m
print(largest([1,2,3,4]))