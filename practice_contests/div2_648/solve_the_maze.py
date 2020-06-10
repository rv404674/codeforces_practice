# brute force
# place # at every empty cell, and then check whether all good cells are reachable and
# all bad cells aren't reachable

# complexty - O(t * m*n * (m*n))

# optimized
# place # on all the cells surrounding bad cell
import copy
from sys import setrecursionlimit
 
setrecursionlimit(10 ** 5)
# by default it is 1000

dx = [0,0,-1,1]
dy = [1,-1,0,0]
good_persons = 0
bad_persons = 0

def is_valid(i,j, n,m):
    if i>=0 and j>=0 and i<n and j<m:
        return True
    else:
        return False

def dfs(grid, visited, n,m, x,y):
    visited[x][y] = 1
    for k in range(4):
        xx = x + dx[k]
        yy = y + dy[k]

        if is_valid(xx, yy, n,m) and not visited[xx][yy] and grid[xx][yy] != '#':
            if grid[xx][yy] == 'G':
                global good_persons
                good_persons +=1
            elif grid[xx][yy] == 'B':
                global bad_persons
                bad_persons += 1
            
            dfs(grid, visited, n,m, xx,yy)

def process():
    [n,m] = list( map(int, input().split(' ')))
    visited = [ [0 for _ in range(m)] for _ in range(n)]
    grid = copy.deepcopy(visited)

    for i in range(n):
        s = input().strip()
        for j in range(len(s)):
            grid[i][j] = s[j]

    
    total_bad, total_good = 0,0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'B':
                total_bad +=1
                for k in range(4):
                    xx = i+dx[k]
                    yy = j+dy[k]

                    if is_valid(xx, yy, n,m) and grid[xx][yy] == '.':
                        grid[xx][yy] = '#'
            elif grid[i][j] == 'G':
                total_good +=1
    
    global good_persons
    good_persons = 0
    global bad_persons
    bad_persons = 0

    dfs(grid, visited, n,m, n-1,m-1)
    # print("GOOD, bad", total_good, total_bad)
    # print(good_persons, bad_persons)

    if grid[n-1][m-1] == '#' and total_good == 0:
        print("yes")
    elif good_persons == total_good and bad_persons == 0:
        print("yes")
    elif good_persons == total_good and bad_persons != 0:
        print("no")
    else:
        print("no")

t = int(input())
for _ in range(t):
    process()

