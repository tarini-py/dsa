import numpy as np
import math
def maze(rows :int, cols :int) -> int:
    
    dp = np.full((rows,cols),0)
    
    if rows == 0 or cols == 0:
        return
    
    dp[0,1:]=1
    dp[1:,0]=1
    
    for r in range(1,rows):
        for c in range(1,cols):
            dp[r,c]=dp[r-1,c]+dp[r,c-1]
    return dp[rows-1,cols-1]
    
def maze_2(rows: int, cols: int) -> int:
    return math.factorial(rows+cols-2)//(math.factorial(rows-1)*math.factorial(cols-1))

def print_maze_path(rows: int, cols: int, i=0, j=0, path=''):
    if i==rows-1 and j==cols-1:
        print(path)
        return
    if j < cols:
        print_maze_path(rows, cols, i, j+1, path+'R')
    if i < rows:
        print_maze_path(rows, cols, i+1, j, path+'D')
        


r=4
c=3
print(maze(r,c))
print(maze_2(r,c))

print_maze_path(r,c)