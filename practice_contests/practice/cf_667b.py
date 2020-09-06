import sys
from sys import setrecursionlimit
from collections import defaultdict

setrecursionlimit( 10 ** 5)

# sys.stdin = open("input.txt", 'r')
# sys.stdout = open("output.txt", 'w')

readline = sys.stdin.readline

def process():
    a,b,x,y,n = map(int, readline().strip().split())
    mn = float('+INF')
    if a-n>=x:
        mn= min(mn, (a-n)*b)
    else:
        left = n-(a-x)
        mn = min(mn, x*(b-min(left, b-y)))
    
    #print("MIN1", mn)
    if b-n>=y:
        mn = min(mn, a*(b-n))
    else:
        left = n-(b-y)
        mn = min(mn, y*(a-min(left,a-x)))

    #print("MIN2", mn)
 
    # if n%2 == 0:
    #     left = n//2
    #     mn = min(mn, min(x, a-left)*min(x, b-left))
    #     print("min3", mn)
    # else:
    #     p,q = n//2, n//2+1
    #     print(p,q,"P q")
    #     mn = min(mn, min(x,a-p)*min(y,b-q))
    #     print("min3", mn)
    #     p,q = q,p
    #     mn = min(mn, min(x,a-p)*min(y,b-q))
    #     print("min4",mn)
    
    return mn



for _ in range(int(readline())):
    print(process())
