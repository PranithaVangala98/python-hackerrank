
def countingSort(arr):
    n = len(arr)
    result = []
    for i in range (0,n):
        result.append(0)
    for i in arr:
        result[i]+=1    
    print(result)
arr = [1,1,1,1]
countingSort(arr)