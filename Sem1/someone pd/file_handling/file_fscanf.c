#include <stdio.h> 
#define MAX 20 
main(){  
   FILE *fp;  
   char buff[MAX];//creating char array to store data of file 
   fp = fopen("one.txt", "r");  
   while(fscanf(fp, "%s", buff)!=EOF){  
   printf("%s ", buff );  
   }  
   fclose(fp);  
}

//fscanf() returns EOF
