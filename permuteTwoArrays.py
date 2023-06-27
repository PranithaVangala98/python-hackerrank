def twoArrays(k,A,B):
    A.sort()
    B.sort(reverse = True)
    count = 0
    x = 0
    for i in range(len(A)):
        if A[i]+B[i] >= k:
            count+=1
        else:
            x+=0
    if count == len(A):
        return 'YES'
    else:
        return 'NO'
    
k = 10       
A = [ 1,2,2,1]
B = [ 3,3,3,4]

print(twoArrays(k,A,B))