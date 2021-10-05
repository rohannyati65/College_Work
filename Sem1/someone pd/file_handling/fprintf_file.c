#include <stdio.h>  
    main(){ 
       FILE *fp;  
       fp = fopen("print.txt", "w");//opening file  
       fprintf(fp, "%s", "hello how are you ?");//writing data into file  
       fclose(fp);//closing file  

}
