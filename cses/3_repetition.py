#coded by 0xp0is0n

def repetition(arr):
    pre_sum = 0
    fin_sum = 0
    # net_sum = 0
    for i in range(0,len(arr)-1):
        if arr[i] == arr[i+1]:
            pre_sum +=1
            # fin_sum +=1
        elif arr[i] != arr[i+1]:
            if(fin_sum <= pre_sum):
                fin_sum = pre_sum
            pre_sum = 0
        # print(i)
        if i==len(arr)-2:
            # print(i)
            if pre_sum > fin_sum:
                fin_sum = pre_sum
    # print(pre_sum)
    return fin_sum + 1
    

if __name__ == "__main__":
    arr = str(input())
    print(repetition(arr))

