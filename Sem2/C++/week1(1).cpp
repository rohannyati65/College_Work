#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
bool smaller(string s1,string s2){
    return(s1<s2);
}
int main(){
    string data[]={"orange","apple","banana","pineapple"};
    sort(data,data+4,smaller);
    for(int i=0;i<4;i++)
    cout<<data[i]<<" ";
    return 0;
}
