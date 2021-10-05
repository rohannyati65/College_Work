#include<stdio.h>
main()
{
    int a[10],n,i,pos,big;
    printf("enter the no. of elements:\n");
    scanf("%d",&n);
    printf("enter the elements\n");
    for(i=0;i<=n-1;i++)
        scanf("%d\n",&a[i]);
    big=a[0];
    pos=0;
    for(i=0;i<=n-1;i++)
    {
        if(a[i]>big)
        {
            big=a[i];
            pos=i;
        }
    }
    printf("the biggest value is %d\n",big);
    printf("its position is %d\n",pos+1);
}
