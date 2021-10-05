#include<iostream>
#include<algorithm>
using namespace std;
bool compare(int i,int j){
    return(i>j);
}
int main(){
    int data[]={32,71,12,46,26};
    //start ptr,end ptr, func. ptr
    sort(data,data+5,compare);
    for(int i=0;i<5;i++)
        cout<<data[i]<<" ";
    return 0;
}
