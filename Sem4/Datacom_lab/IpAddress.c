#include<stdio.h>
#include<stdlib.h>
void dectobin(int a, int b, int c, int d)
{
    int firstoctet[30],secondoctet[30],thirdoctet[30],fourthoctet[30];
    int i=0,j=0;
    printf("\nBINARY FORM  : ");
    while (a > 0)
	{
    	firstoctet[i]=a%2;
        a=a/2;
        i++;
    }
    for (j = i - 1; j >= 0; j--)
        printf("%d",firstoctet[j]);
	printf(".");
	i=0,j=0;
    while (b>0)
	{
        secondoctet[i]=b%2;
        b=b/2;
        i++;
    }
    for (j = i - 1; j >= 0; j--)
        printf("%d",secondoctet[j]);
	printf(".");
	i=0,j=0;
	while (c > 0)
	{
        thirdoctet[i]=c%2;
        c=c/2;
        i++;
    }
    for (j = i - 1; j >= 0; j--)
        printf("%d",thirdoctet[j]);
	printf(".");
	i=0,j=0;
	while (d>0)
	{
        fourthoctet[i]=d%2;
        d=d/2;
        i++;
    }
    for (j = i - 1; j >= 0; j--)
        printf("%d",fourthoctet[j]);
	printf("\n");
}

int main()
{
	system("CLS");
	int a,b,c,d,i;
	int subnet=0,networkid,hostid;
	printf("ENTER THE IP ADDRESS: \n");
	scanf("%d.%d.%d.%d", &a,&b,&c,&d);

    for(i=1; i<173; i++)
    {
		printf(">");
	}

	if(a>=1 && a<=126)
	{
		printf("\nCLASS A\n");
		subnet=8;
	}
	else if(a>=128 && a<=191)
	{
		printf("\nCLASS B\n");
		subnet=16;
	}
	else if(a>=192 && a<=223)
	{
		printf("\nCLASS C\n");
		subnet=24;
	}
	else if(a>=224 && a<=239)
	{
		printf("\nCLASS D\n");
		printf("\n its a MULTICAST ADDRESS\n");
	}
	else if(a>=240 && a<=255)
	{
		printf("\nCLASS E\n");
		printf("\n its a RESERVED ADDRESS\n");
	}

	switch(subnet)
	{
		case 8:	  printf("\nNETWORK PART : %d",a);
				  printf("\nHOST PART : %d.%d.%d\n",b,c,d);
  				  dectobin(a,b,c,d);
				  b=0;
				  c=0;
				  d=0;
				  printf("\nNETWORK ID : %d.%d.%d.%d\n",a,b,c,d);
				  printf("\nBROADCAST ADDRESS : %d.255.255.255\n",a);
				  break;
		case 16:  printf("\nNETWORK PART : %d.%d",a,b);
				  printf("\nHOST PART : %d.%d\n",c,d);
				  dectobin(a,b,c,d);
				  c=0;
				  d=0;
				  printf("\nNETWORK ID : %d.%d.%d.%d\n",a,b,c,d);
				  printf("\nBROADCAST ADDRESS : %d.%d.255.255\n",a,b);
				  break;
		case 24:  printf("\nNETWORK PART : %d.%d.%d",a,b,c);
				  printf("\nHOST PART : %d\n",d);
				  dectobin(a,b,c,d);
				  d=0;
				  printf("\nNETWORK ID : %d.%d.%d.%d\n",a,b,c,d);
				  printf("\nBROADCAST ADDRESS : %d.%d.%d.255\n",a,b,c);
				  break;
	}
    return 0;
}
