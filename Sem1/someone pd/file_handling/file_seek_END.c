#include <stdio.h>

int main () {
   FILE *fp;
   char ch;

   fp = fopen("w_end.txt","w");
   fputs("hello dear how are you ?", fp);
   
   fseek(fp, 15, SEEK_END); 
   
   //seek_set = 0
   //seek_cur = 1
   //seek_end = 2
   
   fputs(" C Programming Language", fp);
   fclose(fp);
   
   fp = fopen("w_end.txt", "r");
   while((ch = getc(fp)) != EOF)
   		printf("%c", ch);
		
   fclose(fp);
   
   return(0);
}

