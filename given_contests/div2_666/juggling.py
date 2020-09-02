import sys
from sys import setrecursionlimit
from collections import defaultdict

setrecursionlimit( 10 ** 5)

# sys.stdin = open("input.txt", 'r')
# sys.stdout = open("output.txt", 'w')

readline = sys.stdin.readline

def process():
    n = int(readline().strip())
    
    hash_table = defaultdict(int)
    for _ in range(n):
        s = readline().strip()
        for i in s:
            hash_table[i] += 1
    
    for val in hash_table.values():
        if val%n !=0 :
            print("NO")
            return
    
    print("YES")

for _ in range(int(readline())):
    process()

