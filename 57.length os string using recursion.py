#length of string using recursion
def length_string(string,i=0):
   
    if string[0:2]=='0/':
        return i
    return length_string(string[1:],i+1)

string='hari krishna reddy'
string+='0/'
print(length_string(string))