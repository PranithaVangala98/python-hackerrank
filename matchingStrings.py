def matchingStrings(str,queries):
    ar =[]
    for i in range(len(queries)):
        ar.append(0) 
    for i in range(0,len(queries)):
        count = 0
        for j in range(0,len(str)):
            if queries[i] == str[j]:
                count+=1
        ar[i] += count
    return ar
str = ['ab','ab','abc']
queries = ['ab','abc','bc']
print(matchingStrings(str,queries)) 
