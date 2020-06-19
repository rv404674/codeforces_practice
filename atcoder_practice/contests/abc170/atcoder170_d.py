import sys
sys.setrecursionlimit(10 **5)

# sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")

readline = sys.stdin.readline

# did it after reading editorial
# nice one
def proc():
    _ = int(readline().rstrip())
    a = list(map(int, readline().rstrip().split()))

    mx = max(a) +1
    cnt = [0] * mx
    for i in a:
        if cnt[i]!=0:
            if cnt[i] == 2:
                continue
        
        for j in range(i, mx, i):
            cnt[j]+=1
    
    return sum(cnt[i] for i in a if cnt[i]==1)

#for _ in range(int(readline().rstrip())):
print(proc())

