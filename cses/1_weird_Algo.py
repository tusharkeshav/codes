#code by 0xP0is0n

a=[]

def check(n):

    if n==1:
        a.append(n)
        for i in range(0,len(a)):
            print(a[i], end=' ')
    elif int(n%2) == 0:
        a.append(n)
        n = int(n/2)
        check(n)
        
    elif int(n%2) != 0:
        a.append(n)
        n = n*3 + 1
        check(n)

if __name__ == "__main__":
    n = int(input())
    check(n)
    # print(x)