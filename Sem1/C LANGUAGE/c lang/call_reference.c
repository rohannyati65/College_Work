#include<stdio.h>
void call_reference(int*,int*);
main()
{
    int a=10,b=20;
    call_reference(&a,&b);
    printf("a=%d\nb=%d\n",a,b);
}
void call_reference(int*a,int*b)
{
    int temp=0;
    temp=*a;
    *a=*b;
    *b=temp;
    printf("a=%d\nb=%d\n",*a,*b);
}
