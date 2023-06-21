
def flippingBits(n):
    def binay_to_integer(b):
        sum = 0
        r = b[::-1]
        for i in range(len(b)):
            sum+=(2**i)*int(r[i])
        return sum

    b = 0
    b = format(n,"032b")
    print(type(b),b)
    flip_str = ''
    for i in b:
        if int(i) == 0:
            flip_str+='1'
        else:
            flip_str+='0'
    print('flipstr',flip_str)
    
    return binay_to_integer(flip_str)
      
n = 9
print(flippingBits(n))

 # for i in p:
    #     final_number = final_number*2+int(i)
    # return final_number
       


     


