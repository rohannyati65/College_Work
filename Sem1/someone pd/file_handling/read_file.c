#include<stdio.h>
main(){

FILE *fp;
char ch;

fp = fopen("file_open.c", "r");
//fseek(fp,0,SEEK_SET);
 
 while ((ch = getc(fp)) != EOF)
    printf("%c",ch);
    
 fclose(fp);
}
