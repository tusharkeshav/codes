#coded by 0xp0is0n
#Solution Add alernate in between two sequence from half
'''
e.g 1,2,3,4,5 => 3 1 4 2 5 i.e isme half section se age se start hoga
'''

def main(n):
    l = [-1]*n
    half = int(n/2)
    a=1
    for i in range(0, len(l)):
        if(i%2!=0): #odd
            l[i] = a
            a+=1
        else:
            half+=1
            l[i]= half
    if(n<=3) and (n!=1):
        print('NO SOLUTION')
    else:
        for i in range(len(l)):
            print(l[i],end=' ')



if __name__ == "__main__":
    n = int(input())
    main(n)