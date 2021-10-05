#include<stdio.h>
main()
{
 FILE *fp;
 char ch;
 fp = fopen("file_fscanf.c", "r");
 
 while ((ch = getc(fp)) != EOF)
    printf("%c",ch);
    
 fclose(fp);
}
