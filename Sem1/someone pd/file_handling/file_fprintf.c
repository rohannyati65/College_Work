    #include <stdio.h>  
    main(){
	   char buff[255];//creating char array to store data of file 
       FILE *fp;  
       fp = fopen("file.txt", "w");//opening file  
       fprintf(fp, "%s", "Hello file by fprintf...");//writing data into file  
       fclose(fp);//closing file  
     	
	   fp = fopen("file.txt", "r");  
       while(fscanf(fp, "%s", buff)!=EOF){  
           printf("%s ", buff );  
       }  

       fclose(fp);  

}
