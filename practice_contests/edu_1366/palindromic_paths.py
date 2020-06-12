# started 5.10
# 
from sys import setrecursionlimit, stdin
import math

setrecursionlimit( 10 ** 5)
readline = stdin.readline

def check_palindrome():
    # procees temp_list and then empty it
    # [ {(0,0):1}, {(0,1):0}, {(0,2):1}, {(2,2):1}]
    for i,j in enumerate(temp_list):
        if i < math.ceil(len(temp_list)/2):
            x,y = j,temp_list[ -(i+1)]
            if list(x.values())[0] != list(y.values())[0]:
                count +=1
                x,y = list(j.keys())[0][0], list(j.keys())[0][1]
                grid[x][y] =  


def dfs(i,j):
    visited[i][j] = True
    temp_list.append( { (i,j):grid[i][j]})
    # check if we have reached end cell
    if i==r and j==c:
        check_palindrome()
        return
    
    if i+1<r:
        dfs(i+1, j)
    if j+1<c:
        dfs(i, j+1)

for _ in range(int(readline().rstrip())):
    r,c = map(int, readline().split())

    visited = [ [False]*c for _ in range(r)]
    temp_list = []
    grid = [ list(map(int, readline().split())) for _ in range(r)]
    count = 0

    dfs(0,0)
    check_palindrome()