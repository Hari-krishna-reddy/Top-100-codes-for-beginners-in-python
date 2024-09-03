# F(N)= (1) +(2*3) + (4*5*6) … N. We are given with an integer N and we need to print the F(N)th term
def F(n):
    s=0
    k=1
    for i in range(1,n+1):
        f=1
        for j in range(i):
            f*=k
            k+=1
        s+=f
    return s

print(F(4))
            
            