import sys
sys.setrecursionlimit(10 **5)

# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

readline = sys.stdin.readline

# used extra memory
# but with one loop
def proc():
    x,n = map(int, readline().rstrip().split())
    a = list(map(int, readline().rstrip().split()))
    hash_map = {}
    for i in a:
        hash_map[i] = True
    
    if not n or x not in hash_map:
        return x
    
    
    p,q = x-1, x+1
    while 1:
        if p not in hash_map and q not in hash_map:
            return p
        elif p not in hash_map:
            return p
        elif q not in hash_map:
            return q
        
        p-=1
        q+=1
    
# atcoder editorial
# simple implementation - O(n2), but no memory


#for _ in range(int(readline())):
print(proc())