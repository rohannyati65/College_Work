#include<stdio.h>

    struct pr
      {
	int n;       //no
	int bt;      //brust time
	int py;       //priority
      } ;

int  main()
       {
	int q,i,n,temp;
	int aw,j;
	struct pr p[10];
	printf("enter number of process :\t");
	scanf("%d",&n);
	printf("\n enter brust time  and priority\n");

	for(i=0;i<n;i++)
	   {
	      printf("P%d  ",i+1);
	      p[i].n=i+1;
	      scanf("%d%d",&p[i].bt,&p[i].py);
	   }
	printf("\nprocess      :")  ;

	for(i=0;i<n;i++)
	  {
	     printf("  %d",p[i].n);
	  }
	printf("\nPriority     :")  ;

	for(i=0;i<n;i++)
	  {
	     printf("  %d",p[i].py);
	  }
	printf("\nBrust time   :");

	for(i=0;i<n;i++)
	  {
	     printf("  %d",p[i].bt);
	  }

	for(i=0;i<n;i++)
	 {
	   for(j=i+1;j<n;j++)
	    {
		if(p[i].py>p[j].py)             //sorting using selection sort
		  {
			temp=p[i].bt;
			p[i].bt=p[j].bt;
			p[j].bt=temp;
			temp=p[i].n;
			p[i].n=p[j].n;
			p[j].n=temp;
			temp=p[i].py;
			p[i].py=p[j].py;
			p[j].py=temp;
		  }
	    }
	 }

	printf("\n Gaint chart \n\t");

	for(i=0;i<n;i++)
		  {
	     printf("\tP%d",p[i].n);
	  }
		printf("\nWaiting time:"); q=0; aw=0;

	for(i=0;i<n;i++)
	 {
	   printf("\t %d",q);
	   aw=aw+q;
	   q=q+p[i].bt;
	 }

	printf("\n\nWaiting time for all process   %d",aw);

	return(0);
}
