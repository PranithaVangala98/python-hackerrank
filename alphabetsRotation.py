
def caesarCipher(s, k):
    result = "" 
    k = k%26
    for i in range (0,len(s)):
        print(ord(s[i]))
        if 97 <= ord(s[i]) <=122 :    
            if 97<= ord(s[i])+k <=122:
                result += chr(ord(s[i])+k)
            elif ord(s[i])+k >= 122:
                result += chr(ord(s[i])-122+k+96)    
        elif 65<= ord(s[i]) <= 90:
            if ord(s[i])+k <=90:
                result += chr(ord(s[i])+k)
            else:
                result += chr(ord(s[i])-90+64+k)
        else:
            result += s[i]
    #     print("new")    
    #     print(ord(result[i]))    
    print(result)
    for i in range (0,len(s)):
        print(ord(result[i]))
s = "middle-Outz"
k = 27
caesarCipher(s, k)
