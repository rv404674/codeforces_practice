
for _ in range( int(input()) ):
    n,x = list(map(int, input().split()))
    a = list(map(int, input().split()))

    l,r = -1,-1
    temp_sum = 0
    for i,j in enumerate(a):
        if j%x !=0:
            if l==-1:
                l,r = i,i
            else:
                r = i
        temp_sum +=j
    
    if l==-1:
        print("-1")
    elif temp_sum%x !=0:
        print(n)
    else:
        #7 7 6 3 5
        # 7 7 4 3 7
        # observation - if you remove, a multiple of x, then that wont be of any use,
        # as the remaining sum will still be divisible by x
        # remove something that is not divisible by x
        print( max(n-l-1, n-(n-r)))