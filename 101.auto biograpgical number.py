#Auto biographical number
string=input('Enter a number:')
for i in range(len(string)):
    if string.count(str(i))!=int(string[i]):
        print('Non auto biographical number')
        break
else:
    print('auto biographical number')