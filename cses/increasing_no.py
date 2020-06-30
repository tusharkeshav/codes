#code

def increasing_no(n, arr):
    sum = 0
    for i in range(0,n-1):
        if (arr[i] > arr[i+1]):
            sum += arr[i] - arr[i+1]
            arr[i+1] += arr[i] - arr[i+1]
    return sum
            


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split(' ')))
    print(increasing_no(n, arr))
    