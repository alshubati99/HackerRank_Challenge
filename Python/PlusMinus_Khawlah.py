
import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

# input = array of n integers

# ouput = 3 decimal values representing the proportions of +, -, 0 each rounded to 6 decimal places

# steps: 1. count number of -,+,0 values in array, 2. calculate ration by dividing each count by total number of elements, 3. print results with 6 decimal places

# Time Complexity: O(n) (we loop through the array once)
# Space Complexity: O(1) (only a few variables are used)

def plusMinus(arr):
    
    positives_count = 0
    negatives_count = 0
    zero_count = 0
    n = len(arr) #total num of elements
    for num in arr:
        if num > 0:
            positives_count += 1 #count pos
        elif num < 0:
            negatives_count += 1 #count neg
        else:
            zero_count += 1      #count zero
    #calculate proportions:
    
    p_ratio = positives_count/n
    n_ratio = negatives_count/n
    zero_ratio = zero_count/n
    
    # print results with 6 decimal places
    print(f"{p_ratio: .6f}")
    print(f"{n_ratio: .6f}")
    print(f"{zero_ratio : .6f}")
    


if __name__ == '__main__':
    arr = [-1, -2, 0, 1, 2]
    plusMinus(arr)
