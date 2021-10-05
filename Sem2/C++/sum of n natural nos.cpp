#include<iostream>
using namespace std;
int main(){
    int n;
    int sum=0;
    cout<<"input limit:"<<endl;
    cin>>n;
    for(int i=0;i<=n;++i)
        sum=sum+i;
    cout<<"sum of "<<n;
    cout<<" numbers is:"<<sum<<endl;
    return 0;
    }
