#Integer to roman number convertion
num=15
maps=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
ans=''
for value,symbol in maps:
    while num>=value:
        ans+=symbol
        num-=value
print(ans)