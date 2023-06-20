def divisibleSumPairs(n,k,ar):
    p = 0
    count = 0
    for i in range(n):
        for j in range(i,n-1):
            p = ar[i]+ar[j+1]
            if p%k == 0:
                count+=1
    return count
n = 6
k = 3
ar = [1,3,2,6,1,2]        
print(divisibleSumPairs(n,k,ar))