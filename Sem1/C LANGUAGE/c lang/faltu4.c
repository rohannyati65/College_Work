#include<stdio.h>
main()
{
    char ch;
        printf("enter a character");
        scanf("%c",&ch);
    switch(ch)
    {
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
            printf("\n %c is a vowels",ch);
            break;
        default:
            printf("%c is a constant",ch);
            break;
    }
}

