def camelCase(input):
    final = ''
    if input[0] == 'S':
        if input[2] =='M':
            word = input[4:-2]  
            for i in word:
                if 65 <= ord(i) <= 90:
                    final+=' '
                    final+=i.lower()
                else:
                    final+=i
            print(final)
        elif input[2] =='C':
            word = input[4:]
            for i in range(len(word)):   
                if 65 <= ord(word[i]) <= 90:
                    if i!=0:
                        final+=' '
                    final+=word[i].lower()    
                else:
                    final+=word[i]
            print(final)
        elif input[2] == 'V':
            word = input[4:]
            for i in word:   
                if 65 <= ord(i) <= 90:
                    final+=' '
                    final+=i.lower()
                else:
                    final+=i
            print(final)
    else:
        final_new = ''
        if input[2] =='M':
            word = input[4:]
            for i in range(len(word)):
                if word[i-1] == ' ':
                    final += word[i].upper()
                else:                    
                    final+=word[i]    
            final_new = final.replace(" ","")        
            print(final_new+'()')
        elif input[2] =='C':
            word = input[4:]
            
            for i in range(len(word)):                
                if word[i-1] == ' ':
                    final +=word[i].upper()
                else:
                    if i == 0:
                        final+=word[i].upper()
                    else:
                        final+=word[i]  
            final_new = final.replace(" ","")
            print(final_new)
        elif input[2]=='V':
            word = input[4:]
            for i in range(len(word)):
                if word[i-1] == ' ':
                    final +=word[i].upper()
                else:
                    final+=word[i]  
            final_new = final.replace(" ","")
            print(final_new.strip())



flag = True
while flag:
    try:
        s = input("")
        if not s:
            flag = False
        else:
            camelCase(s)
    except:
        flag = False
    


