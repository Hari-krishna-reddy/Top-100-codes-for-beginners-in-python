
def decode(string, prefix=""):
    if len(string) == 0:
        print(prefix)
        l.append(prefix)
    elif len(string) == 1:
        # Decode the last single digit
        print(prefix + chr(64 + int(string[0])))
        l.append(prefix)
    else:
        # Decode the first single digit
        decode(string[1:], prefix + chr(64 + int(string[0])))
        
        # Decode the first two digits as a pair if they form a valid character
        if int(string[0:2]) <= 26:
            decode(string[2:], prefix + chr(64 + int(string[0:2])))

# Example usage

l=[]
decode('1123')
print(len(l))