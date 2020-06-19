#code

def sum_subarray(n, arr):
    #arr.sort()
    arr_dict = {}
    for i in range(0, len(arr)):
        if arr[i] in arr_dict:
            arr_dict[arr[i]] +=1
        else:
            arr_dict[arr[i]] = 1
    max_val = max(arr_dict, key=arr_dict.get)
    if float(max_val) < float(len(arr))/2:
        max_val = -1
    return max_val



if __name__ == "__main__":
    t = int(input())            #total
    arr = []
    for i in range(0,t):
        n = input()
        # arr = [int(x) for x in input().split()]
        arr = list(input().split())
        # print (m)
        print_Data = sum_subarray(n, arr)
        print(print_Data)


