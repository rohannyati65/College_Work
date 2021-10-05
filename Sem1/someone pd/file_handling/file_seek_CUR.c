#include <stdio.h>

int main () {
   FILE *fp;
   char ch;

   fp = fopen("w_seek.txt","w");
   fputs("hello dear how are you ?", fp);
   
   fseek(fp, 6, SEEK_CUR); //move the pointer 6 positions from the current position of the file pointer. 
   
   fputs("jini", fp);
   fclose(fp);
   
   fp = fopen("w_seek.txt", "r");
   while((ch = getc(fp)) != EOF)
   		printf("%c", ch);
		
   fclose(fp);
   
   return(0);
}
