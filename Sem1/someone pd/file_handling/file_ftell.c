#include <stdio.h>

int main () {
   FILE *fp;
   char ch;
   long file_location = 0;

   fp = fopen("f_tell.txt","w");
   
   file_location = ftell(fp);
	printf("\nlocation of pointer from the starting = %ld", file_location);
	
   fputs("hello dear how are you ?", fp);
   
	file_location = ftell(fp);
	printf("\nlocation of pointer from the starting = %ld", file_location);
	
	rewind(fp);
	
	file_location = ftell(fp);
	printf("\nlocation of pointer from the starting = %ld", file_location);
	

  
   /*fseek( fp, 7, SEEK_SET); 
   fputs("C", fp);
   fclose(fp);
   
   /*fp = fopen("file.txt", "r");
   while((ch = getc(fp)) != EOF)
   		printf("%c", ch);
	
	file_location = ftell(fp);
	printf("\nlocation of pointer from the starting = %ld", file_location); // including white spaces
	
   fclose(fp);
   */
   return(0);
}
