#include<stdio.h>
int sum();
main()
{
    int ans;
    ans=sum();
    printf("%d",ans);
}
void sum()
{
    int a,b;
    scanf("%d%d",&a,&b);
    return a+b;
}
