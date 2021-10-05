#include<stdio.h>
main()
{
    float a=234.5678;
    printf("%3.2f\n",a);
    printf("%2.3f",a);//compiler never deletes any number before decimal point
}
