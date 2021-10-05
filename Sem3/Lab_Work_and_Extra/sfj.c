#include<stdio.h>

void main()
{
	int at[20],bt[20],p[20],wt[20],ct[20],tat[20],i,j,n,total=0,pos,temp,sum=0,add=0;
	printf("Enter number of process : ");
	scanf("%d",&n);
	
	printf("Enter Burst Time :\n");
	for(i=0;i<n;i++)
	{
		printf("p%d:",i+1);
		scanf("%d", &bt[i]);
		p[i]=i+1;
	}
	printf("Enter Arrival Time :\n");
	for(i=0;i<n;i++)
	{
		printf("p%d:",i+1);
		scanf("%d", &at[i]);
		p[i]=i+1;
	}
	
	for(i=0;i<n;i++)
	{
		pos=i;
		for(j=i+1;j<n;j++)
		{
			if(at[j]<at[pos])
			pos=j;
		}
		temp=at[i];
		at[i]=at[pos];
		at[pos]=temp;
		
		temp=p[i];
		p[i]=p[pos];
		p[pos]=temp;
		
		temp=bt[i];
		bt[i]=bt[pos];
		bt[pos]=temp;
	}
	wt[0]=at[0];
	
	for(i=1;i<n;i++)
	{
		wt[i]=0;
		for(j=0;j<i;j++)
		{
			wt[i]=wt[i-1]+bt[i-1];
		}
		total+=wt[i];
	}
	
	 for(i=0;i<n;i++)
    {
        tat[i]=0;
        for(j=0;j<i;j++)
        {
        	tat[i]=wt[i]+bt[i];
        	break;
		}
    }
    
    for(i=0;i<n;i++)
    {
        ct[i]=0;
        for(j=0;j<i;j++)
        {
        	ct[i]=tat[i]+at[i];
        	break;
		}
		add = ct[i];
    }
    printf("\nProcess\t\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\tCompletion Time");
    
    for(i=0;i<n;i++)
	 {
	 	printf("\nP[%d]\t\t%d\t\t%d\t\t%d\t\t%d\t\t%d" , p[i] , at[i] , bt[i] , wt[i] , tat[i] , ct[i]);
	 }
}
