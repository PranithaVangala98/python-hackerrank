def superDigit(n, k):
    result = 0
    c = 0
    for i in n:
        c += int(i)
    result = c*k
    print(result)
    while len(str(result)) > 1:
        print('asdf')
        x = str(result)
        add = 0
        for i in x:
            add += int(i)
        result = add
        if len(str(result)) == 1:
            print(result)

n = '148'
k = 3   
superDigit(n, k)
