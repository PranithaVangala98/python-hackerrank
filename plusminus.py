#!/bin/python3

import math
import os
import random
import re
import sys
def plusMinus(arr):
    # Write your code here
       # Write your code here
    count_positive = 0
    count_negative = 0
    count_zero = 0
    deci_negative = 0
    deci_positive = 0
    deci_zero = 0
    for i in arr:
      if i == 0 :
        count_zero+=1
      elif i > 0:
        count_positive +=1
      elif i < 0:
        count_negative +=1
    n = count_positive+count_negative+count_zero
    deci_positive = count_positive/n
    deci_negative = count_negative/n
    deci_zero = count_zero/n
    print("{:.6f}".format(deci_positive))
    print("{:.6f}".format(deci_negative))
    print("{:.6f}".format(deci_zero))
    

arr = [1,2,0,0,9,-1,-6,-6]
plusMinus(arr)
