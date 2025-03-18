

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

# sort the array to easily identify the smallest and largest numbers. 

#min = sum of first four numbers
#max = sum of last four numbers

# O(nlogn) is time complexity for sort and  O(1) for sum calculations space complexity

def miniMaxSum(arr):
    arr.sort()
    min_sum = sum(arr[:4])
    max_sum = sum(arr[1:])
    print(min_sum, max_sum)


miniMaxSum([6, 2, 2, 5, 1, 2])

    
"""
another way to solve it is 
def miniMaxSum(arr):
    total_sum = sum(arr)
    min_sum = total_sum - max(arr)
    max_sum = total_sum - min(arr)
    print(min_sum, max_sum)


Time Complexity: O(n) (since sum, max, and min each take 

Space Complexity:  O(1)
"""
