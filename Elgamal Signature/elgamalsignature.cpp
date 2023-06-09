#include<bits/stdc++.h>
using namespace std;
#define llt long long int
llt poww(llt x, llt y, llt z)
{
    llt sum=1;
    while(y--)
    {
        sum=(sum*x)%z;
    }
    return sum;
}
llt modinverse(llt a, llt b)
{
    llt i=2,s;
    a=a%b;
    for(i=2;i<b;i++)
    {
        s=(a*i)%b;
        if(s==1)
            return i;
    }
    return 1;
}

int main()
{
    llt p,a,e1,e2,k,y1,y2,m,first,second;
    p=1721;
    a=13;
    e1=17;
    e2=poww(e1,a,p);
    m=1807000;
    k=29;
    y1=poww(e1,k,p);
    y2=((m-a*y1)*modinverse(k,p-1))%(p-1);
    first=(poww(y1,y2,p)*poww(e2,y1,p))%p;
    second=poww(e1,m,p);
    cout<<"First = "<<first<<" Second = "<<second<<endl;
}
