#include<stdio.h>
main()
{
    int a[10],n,i;
    float avg,sum;
    printf("enter the no. of elements:\n");
    scanf("%d",&n);
    printf("enter the elements");
    for(i=0;i<=n-1;i++)
        scanf("%d",&a[i]);
    sum=0;
    for(i=0;i<=n-1;i++)
        sum=sum+a[i];
    avg=sum/n;
    printf("avg=%f\n",avg);
}
