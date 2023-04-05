
import math
import os
import random
import re
import sys
 
sum = 0 
def miniMaxSum(arr):
    sum_max = 0
    sum_min = 0
    x = sorted(arr)
    print(x)
    for i in range(0,5):
        sum_min = sum_min + x[i]
    for i in range(1,6):
        sum_max = sum_max + x[i]

    print(sum_min ,sum_max)
arr = [1,1,1,1,1,1]
miniMaxSum(arr)



