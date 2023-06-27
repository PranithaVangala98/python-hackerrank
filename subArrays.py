def birthdays(s,d,m):
    count = 0
    for i in range(len(s)-m+1):
        if sum(s[i:i+m]) ==d:
            count+=1
    return count 
    
s =[2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3 ,3 ,4, 2, 1]
d = 3
m = 2
print(birthdays(s,d,m))
