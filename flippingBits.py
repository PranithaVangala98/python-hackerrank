def flippingBits(n):
    p = []
    integer =[]
    b = 0
    final_number = 0
    b = format(n,"032b")
    for i in range(32):
        p.append(0)
        integer.append(0)
    for i in range(32):
        integer[i] += int(b[i]) 
    for i in range(32):
        if integer[i] == 1:
            p[i]+= 0
        else:
            p[i]+=1
    for i in p:
        final_number = final_number*2+int(i)
    return final_number
       
n = 2147483647
print(flippingBits(n))



     


