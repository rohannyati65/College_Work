#include<stdio.h>

void main()
{
	int bt[20],p[20],wt[20],i,j,n,total=0,pos,temp;
	printf("Enter number of process : ");
	scanf("%d",&n);
	
	printf("Enter Burst Time :\n");
	for(i=0;i<n;i++)
	{
		printf("p%d:",i+1);
		scanf("%d", &bt[i]);
		p[i]=i+1;
	}
	
	for(i=0;i<n;i++)
	{
		pos=i;
		for(j=i+1;j<n;j++)
		{
			if(bt[j]<bt[pos])
			pos=j;
		}
		temp=bt[i];
		bt[i]=bt[pos];
		bt[pos]=temp;
		
		temp=p[i];
		p[i]=p[pos];
		p[pos]=temp;
	}
	wt[0]=0;
	
	for(i=1;i<n;i++)
	{
		wt[i]=0;
		for(j=0;j<i;j++)
		{
			wt[i]+=bt[j];
		}
		total+=wt[i];
	}
	
	printf("\nProcess\t\tBurst Time\tWaiting Time");
	 
	 for(i=0;i<n;i++)
	 {
	 	printf("\nP%d\t\t%d\t\t%d" , p[i] , bt[i] , wt[i]);
	 }
}
