# observe
# basically the solution is
# to convert to 0001111... or 1110000
# check min
# see the editorial for clearer explannation

import sys
from sys import setrecursionlimit
setrecursionlimit(10 **5)

# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

readline = sys.stdin.readline

def process():
    a = readline().rstrip()
    total_one,total_zero = 0,0
    for i in a:
        if i=='0':
            total_zero +=1
        else:
            total_one +=1

    ans = float('+inf')
    done_zero, done_one = 0,0
    for i in a:
        if i=='0':
            done_zero+=1
        else:
            done_one+=1

        # convert to 100000 (1 start from i)
        cost1 = done_zero + total_one - done_one
        # convert to 011111
        cost2 = done_one + total_zero - done_zero

        ans = min(ans, cost1, cost2)
    
    print(ans)


    



for _ in range(int(readline())):
    process()
