#include <stdio.h>
int main()
{
	int n,bt[10] , wt[10] , i , j;
	printf("Enter total number of process : ");
	scanf("%d" , &n);

	printf("\nEnter the burst time\n");
	for(i=0;i<n;i++)
	{
		printf("P[%d] : " , i+1);
		scanf("%d" , &bt[i]);
	}

	for(i=0;i<n;i++)
	{
		wt[i]=0;
		for(j=0;j<i;j++)
		{
			wt[i]+=bt[j];
		}
	 }

	 printf("\nProcess\tBurst Time\tWaiting Time");

	 for(i=0;i<n;i++)
	 {
	 	printf("\nP[%d]\t\t%d\t\t%d" , i+1 , bt[i] , wt[i]);
	 }

	 return 0;
}
