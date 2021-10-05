#include<stdio.h>
main()
{
    int i=1,j=1;
    for(;;)
    {
        if(i>5)
            break;
        else
            j+=i;
        printf("%d\n",j);
        i+=j;
    }
}
