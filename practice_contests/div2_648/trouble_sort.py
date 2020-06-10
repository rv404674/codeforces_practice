# Author Rahul
# Python3
from collections import OrderedDict
import sys

# For getting input from input.txt file 
sys.stdin = open('input.txt', 'r')  

# My approach
t = int(input())
for _ in range(t):
    n = int(input())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    flag = True
    for i in range(len(a) - 1):
        if a[i+1] < a[i]:
            flag = False
            break
    
    if flag:
        print("yes")
    
    if not flag:
        counter0, counter1 = 0,0
        for i in b:
            if i==0:
                counter0 +=1
            else: counter1 +=1 
        
        if counter0 == n or counter1 == n:
            print("no")
        else:
            print("yes")

# optimized solution
t = int(input())
for _ in range(t):
    n = int(input())
    a = list( map(int, input().split()))
    b = list( map(int, input().split()))
    a2 = sorted(a)

    if (1 not in b or 0 not in b) and a2 != a:
        print("no")
    else:
        print("yes")






