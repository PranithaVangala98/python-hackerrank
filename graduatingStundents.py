def graduatingStudents(n):
    ar = []
    for i in range(len(n)):
        ar.append(0)
    for i in range(len(n)):
        if n[i]>=38:
            if (n[i]+1)%5 == 0:
                ar[i] += n[i]+1
            elif (n[i]+2)%5 ==0:
                ar[i] += n[i]+2
            else:
                ar[i] += n[i]
        else:
            ar[i] += n[i]
    return ar
n = [84,29,57]
print(graduatingStudents(n))
