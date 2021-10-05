#include <stdio.h>

int main () {
   FILE *fp; //creating a file pointer that will store the address of the file 
   char ch;

   fp = fopen("write_mode.txt","w"); //open the already existing file and return the address 
   //of the file to fp OR create a new file if file doesnot exist and than return the address
   //of the file to the fp
   
   fputs("hello how are you ?", fp); // start writing from the beginning and replace the existing content of the file
   fclose(fp); 
   
   
   
   fp = fopen("write_mode.txt", "r");
   while((ch = getc(fp)) != EOF)
   		printf("%c", ch);
		
   fclose(fp);
   
   return(0);
}
