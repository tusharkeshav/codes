#code

def sum_subarray(sum, arr):
    total = 0
    a=0
    for i in range(0, len(arr)):
        # if sum > total:
        total = total + int(arr[i])
        if sum == total:
            return a, i
        elif sum < total:
            for x in range(a, i):
                total = total - int(arr[x])
                a+=1
                if sum == total:
                    return a , i
                elif sum > total:
                    break
    return 0, 0


if __name__ == '__main__':
    t = int(input())
    for i in range(0,t):
        n = int(input())
        sum = int(input())
        arr = list(input().split())
        # arr = [int(x) in range(input().split())]
        x, y = sum_subarray(sum, arr)
        if x==0 and y==0:
            print(-1)
        else:
            print(x+1, y+1)
    
