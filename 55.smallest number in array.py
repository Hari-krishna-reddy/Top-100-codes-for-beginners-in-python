#smallest number in array using recursion
import math
def smallest_ele_arr(arr,m=math.inf):
    if len(arr)==0:
        return m
    if arr[0]<m:
        m=arr[0]
    return smallest_ele_arr(arr[1:],m)
print(smallest_ele_arr([10,4,2,11,1]))


#Approach2 using loops
def small(arr):
    m=math.inf
    for i in arr:
        if i<m:
            m=i
    return m
print(small([10,4,2,11,1]))
