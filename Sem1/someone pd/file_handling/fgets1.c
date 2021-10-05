#include <stdio.h>
#define MAX 15
int main () {
   FILE *fp;
   char ch[MAX];

   fp = fopen("r+_mode.txt","r+"); //dont create a new file if file dont exist
   
   fputs("hello how are you ?", fp); // start writing from the beginning and replace the existing content of the file
   fclose(fp);
   
   fp = fopen("r+_mode.txt", "r");
   while(fgets(ch, MAX, fp) != NULL)
   		printf("%s", ch);
		
   fclose(fp);
   
   return(0);
}
