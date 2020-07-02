t=int(input())
a=[]
b=[]
for i in range(0,t):
    x = list(map(int, input().split(' ')))
    # print(x[0])
    a.append(int(x[0]))
    b.append(int(x[1]))
for i in range(0, t):
    max1 = max(a[i], b[i])
    # print(max1)
    max_product = max1 * max1
    if int(max1%2)==0:
        sub = abs(a[i] - max1) + abs(b[i] - 1)
    else:
        sub = abs(a[i]-1) + abs(b[i]-max1)
    print(max_product - sub)