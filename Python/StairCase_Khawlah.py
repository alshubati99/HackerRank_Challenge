def staircase(n):
    for i in range(1,n+1):
        spaces = ' '*(n-i) 
        hashes = '#' * i
        print(spaces + hashes)
    
staircase(7)
