#include<bits/stdc++.h>
using namespace std;
long long int poww(long long int x, long long int y, long long int z)
{
    long long int ans=1;
    while(y--)
    {
        ans=(ans*x)%z;
    }
    return ans;
}

int main()
{
    long long int p,d,e1,e2,r,c1,c2,i,s,m,message;

    p=23;
    d=12;
    e1=12;
    e2=pow(e1,d);
    e2=e2%p;
    cout<<"e2 is "<<e2<<endl;
    r=4;
    c1=pow(e1,r);
    c1=c1%p;
    cout<<"c1 is "<<c1<<endl;
    cout<<"Enter message"<<endl;
    cin>>m;
    c2=poww(e2,r,p);
    c2=c2*m;
//    c2=c2%p;
    cout<<"Cipher text is c1= "<<c1<<" and c2= "<<c2<<endl;
//    i=2;
//    while(1)
//    {
//        i=i+1;
//        s=poww(c1,d,p);
//        s=s*i;
//        s=s%p;
//        cout<<s<<endl;
//        if(s==1)
//        {
//            break;
//        }
//    }
    long long int q=poww(c1,d,p);

    cout<<q<<endl;
    long long int dec=c2/q;
    cout<<dec<<endl;
    dec=c2/poww(c1,d,p);
//    message=c2*i;
//    message=message%p;
    cout<<"Decrypted message is "<<dec<<endl;
}
