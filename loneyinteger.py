
def lonelyinteger(a):
    
    # for i in a:
    #     if a.count(i) == 1:
    #         return i


  #  x = a.copy()
   # n = len(a)
    #for i in range (0,n) :
     #   for j in range (i+1,n) :
      #      if a[i] == a[j]:
       #         x = [k for k in x if k!=a[i]]
    #return x[0]
    d={}
    for i in a:
        d[i] = 0
    for i in a:
        d[i] = d[i]+1

    for x, y in d.items():
        if y == 1:
            return x





a = [1,2,3,4,3,2,1]
print(lonelyinteger(a))
