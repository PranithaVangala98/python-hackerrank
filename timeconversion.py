import math
import os
import random
import re
import sys
s = "07:05:45PM"


def timeConversion(s):
    if s[-2:] == "AM":
        if s[:2] == "12":
            return "00"+s[2:-2]
        else:
            return s[:-2]
    
    else:
        if s[:2] == "12":
            return s[:-2]
        else:
            a = 12 +int(s[:2])
            return str(a)+s[2:-2]

print(timeConversion(s))
