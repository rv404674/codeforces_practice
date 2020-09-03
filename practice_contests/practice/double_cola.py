# Yandex Algo 2011 Problem A
# Saw the Solution.
import sys
sys.setrecursionlimit(10 ** 5)

n = int(input())-1
while n>4:
    n = (n-5)//2

# for n=1, o/p = Sheldon. Hence the -1
print(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"][n])