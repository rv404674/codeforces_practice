# brute force
# place # at every empty cell, and then check whether all good cells are reachable and
# all bad cells aren't reachable

# complexty - O(t * m*n * (m*n))

# optimized
# place # on all the cells surrounding bad cell
import sys

readline = sys.stdin.readline
from sys import setrecursionlimit
 
setrecursionlimit(10 ** 5)
# by default it is 1000

dx = [0,0,-1,1]
dy = [1,-1,0,0]

DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def is_valid(i,j, n,m):
    if i>=0 and j>=0 and i<n and j<m:
        return True
    else:
        return False

def dfs(x,y):
    visited[x][y] = 1
    for di,dj in DIR:
        xx = x + di
        yy = y + dj

        if is_valid(xx, yy, n,m) and not visited[xx][yy] and grid[xx][yy] != '#':
            dfs(xx,yy)

for t in range(int(readline().rstrip())):
    # readline().split()
    # 2 3
    # Out[56]: ['2', '3']
    n,m = map(int, readline().split())

    #[n,m] = list( map(int, input().split(' ')))
    visited = [ [0] * m for _ in range(n) ]
    grid = [ list(readline().rstrip()) for _ in range(n)]

    # for i in range(n):
    #     s = input().strip()
    #     for j in range(len(s)):
    #         grid[i][j] = s[j]

    ok = True
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'B':
                for di,dj in DIR:
                    xx = i+di
                    yy = j+dj

                    if is_valid(xx, yy, n,m):
                        if grid[xx][yy] == 'G':
                            ok = False
                        if grid[xx][yy] == '.':
                            grid[xx][yy] = '#'

    # CRITICAL EDGE CASE
    if grid[n-1][m-1] != '#':
        dfs(n-1,m-1)

    for i in range(n):
        for j in range(m):
            # basically if it is a good person and he is not visited.
            if grid[i][j] == 'G' and not visited[i][j]:
                ok = False
        
    print("yes" if ok else "no")

