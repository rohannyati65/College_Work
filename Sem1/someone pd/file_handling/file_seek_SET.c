#include <stdio.h>

int main () {
   FILE *fp;
   char ch;

   fp = fopen("w_set.txt","w");
   fputs("?", fp);
  
   fseek( fp, 6, SEEK_SET);// move the pointer 6 position away from the beginning of the file 
   fputs("Ram", fp);
   fclose(fp);
   
   fp = fopen("w_set.txt", "r");
   while((ch = getc(fp)) != EOF)
   		printf("%c", ch);
	
   fclose(fp);
   
   return(0);
}
