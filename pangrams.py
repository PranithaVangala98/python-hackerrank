
import string
def pangrams(s):
    a = string.ascii_lowercase
    A = string.ascii_uppercase
    alphabets = a +' '   
    lowerCase = s.lower()
    for i in alphabets:
        if i not in lowerCase:
            return 'not pangram'
    return 'pangram'        
s = 'We promptly judged antique uckles for the next prize'
print(pangrams(s))