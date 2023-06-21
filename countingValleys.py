   
steps = 8 
path = "DDUUUUDD"

def cv2(steps,path):
    x = 0
    valleys = 0
    for i in path:
        prev = x
        x+= 1 if i == 'D' else -1
        if x == 0 and prev==-1:
            valleys+=1
    return valleys
print(cv2(steps,path))

        