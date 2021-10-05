#include<stdio.h>

main(){
	FILE *fp;
	char ch;
	
	fp = fopen("file_write.c","r");
	
	while((ch = getc(fp)) != EOF)
   		printf("%c", ch);
   		
	fclose(fp);
}
