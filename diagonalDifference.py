# def diagonalDifference(arr):
#     sum1=0
#     sum2=0
#     n= len(arr)
#     for i in range (0,n):
#         for j in range (0,n):
#             if i == j :
#                 sum1 = sum1+arr[i][j] 
#                 print("left to right",i,j)
#             elif j == (n-1-i):
#                 sum2 = sum2+arr[i][n-1-j]
#                 print(i,j)



#     print(abs(sum1-sum2))

def dd(arr):
    n = len(arr[0])
    i =0
    j=n-1
    sum1 = 0 
    sum2=0
    for _ in range(n):
        print(i,i)
        print(i,j)
        sum1+=arr[i][i]
        sum2+=arr[i][j]
        i=i+1
        j-=1
        
    print(abs(sum1-sum2))


arr = [[1,2,3],
       [4,5,6],
       [7,8,9]]
dd(arr)
