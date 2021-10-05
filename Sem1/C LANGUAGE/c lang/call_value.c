#include<stdio.h>
void call_value(int,int);
main()
{
    int a=10,b=20;
    call_value(a,b);
    printf("a=%d\nb=%d\n",a,b);
}
void call_value(int a,int b)
{
    int temp=0;
    temp=a;
    a=b;
    b=temp;
    printf("a=%d\nb=%d\n",a,b);
}
