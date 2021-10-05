#include <stdio.h>

int main () {
   FILE *fp;
   char ch;

   fp = fopen("read_write.txt","w"); //dont create a new file if file dont exist
   
   fputs("hello how are you ?", fp); // start writing from the beginning and replace the existing content of the file
   fclose(fp);
   
   fp = fopen("read_write.txt", "r");
   while((ch = getc(fp)) != EOF)
   		printf("%c", ch);
		
   fclose(fp);
   
   return(0);
}
