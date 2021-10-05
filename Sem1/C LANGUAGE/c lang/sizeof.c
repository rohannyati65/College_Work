#include<stdio.h>
void add(int x,int y)
{
    printf("enter first element:%d\n",x);
    printf("enter second element:%d\n",y);
    printf("addition is %d\n",x+y);
}
main()
{
    int a,b;
    void (*ptr)(int,int);
    ptr=add;
    printf("enter 1st value:");
    scanf("%d",&a);
    printf("enter second value:");
    scanf("%d",&b);
    ptr(a,b);
}
