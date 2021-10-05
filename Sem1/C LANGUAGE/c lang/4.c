#include<stdio.h>
int main(int argc , char* argv[])
{
    int a[10],i,sum=0;
    float avg;
    printf("enter 10 nos\n");
    for(i=0;i<=9;i++)
        scanf("%d",&a[i]);
    for(i=0;i<=9;i++)
        sum=sum+a[i];
    avg=sum/10.0;
    printf("the avg is %f",avg);
}
