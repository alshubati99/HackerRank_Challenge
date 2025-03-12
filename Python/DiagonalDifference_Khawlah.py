

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    n = len(arr)
    
    primary_diagonal = 0
    Secondary_diagonal = 0
     
    for i in range (n):
        primary_diagonal += arr[i][i]
        Secondary_diagonal += arr[i][n-1-i]
    return abs(primary_diagonal-Secondary_diagonal)


array = [
    [11, 2, 4],
    [10,40,60],
    [22,55,66]
]

print(diagonalDifference(array))
