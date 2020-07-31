// Question: Count numbers in range such that digits in it and it’s product with q are unequal
// GeeksforGeek


#include<iostream>
using namespace std;

int check(int t, int n)
{
    int hash[10]={0};
    int hash1[10]={0};
    int count=0;
    while(n>0)
    {
        hash[n%10]++;
        n = n/10;
    }
    while(t>0)
    {
        hash1[t%10]++;
        t = t/10;
    }
    // for(int i=0; i<10; i++)
    //     cout<<hash[i]<<" ";
    for(int i=0; i<sizeof(hash)/sizeof(hash[0]); i++)
    {
        if(hash[i]>0 && hash1[i]>0)
        {
            count++;
        }
    }
    if(count>0)
        return 0;       //invalid
    else
        return 1;      //valid


}

int main()
{
    int x,y,z,n;
    cin>>x;
    cin>>y>>z;
    for(int i=y; i<=z; i++)
    {
        int t = x * i;
        cout<<check(t, i);
    }
    
}