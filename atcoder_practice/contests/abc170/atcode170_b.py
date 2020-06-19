import sys
sys.setrecursionlimit(10 **5)

# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

readline = sys.stdin.readline

def proc():
    k,n = map(int,readline().rstrip().split())
    #2x + 4y = n
    p,q = -1,-1
    ans = []
    #print(k,n, "**")
    for i in range(0, 101):
        for j in range(0,101):
            #print(i,j,"***")
            if 2*i + 4*j == n:
                p,q = i,j
                ans.append( (p,q))

    for pair in ans:
        p,q = pair[0],pair[1]
        if p+q == k:
            return "Yes"
    
    return "No"


# after seeing editorial
def proc_optimized():
    x,y = map(int, readline().rstrip().split())
    # if x=3, there are (x+1) solutions
    # (0,3), (1,2), (2,1), (3,0)

    result = 'No'
    for a in range(x+1):
        b = x-a
        if 2*x + 4*b == y:
            result = 'Yes'

    return result

#for _ in range(int(readline())):
print(proc())
