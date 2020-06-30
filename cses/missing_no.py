#code

def missing_no(arr, n):
    arr.sort()
    count = 0
    if(len(arr)==1):
        if(arr[0]==1):
            print(2)
        elif(arr[0]==2):
            print(1)
        count = 1
    
    for i in range(1, n-1):
        if(arr[i-1]+1 != arr[i]):
            print(arr[i-1] + 1)
            count = 1
            break
    if count==0:
        print(arr[n-2]+1)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split(' ')))
    missing_no(arr, n)