def marsExploration(s):
   
    x = 0
    y=0
    z=0
    n = len(s)
    p = 0
    substrings = []
    for i in range(0, n, 3):
        substring = s[i:i+3]
        substrings.append(substring)
    
    for i in substrings:
        for j in range(len(i)):
            p = j%2
            if p == 0 and i[j] =='S':
                y+=1 
            elif p == 1 and i[j] =='O':
                z+=1
            else:
                x += 1
    return x

s = 'SOSOOSOSOSOSOSSOSOSOSOSOSOS'
#another process
def mar2(s):
    l = len(s)
    original = 'SOS'*int(l/3)
    count = 0
    for i in range(len(s)):
        if original[i]!=s[i]:
            count+=1
    return count

print(marsExploration(s))
print(mar2(s))