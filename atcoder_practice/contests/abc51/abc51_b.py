import sys
sys.setrecursionlimit(10 ** 5)

# 7.57 - 8.22

# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w') 

readline =sys.stdin.readline

# time - O(n2)
def process():
    k,s = map(int,readline().rstrip().split())
    cnt=0

    for i in range(0,k+1):
        for j in range(0,k+1):
            z = s-(i+j)
            if z>=0 and z<=k:
                cnt+=1
    
    return cnt



# for _ in range(int(readline().rstrip())):
print(process())
