#include<stdio.h>
#include<malloc.h>


main(){
	int *ptr;
	int n, i;
	
	printf("enter the size of array");
	scanf("%d",&n);
	
	ptr = (int*)malloc(n*sizeof(int));

	for(i=0;i<=n-1;i++)
		scanf("%d",&ptr[i]);
	
	printf("you entered\n");	
	for(i=0;i<=n-1;i++)
		printf("\n%d",ptr[i]);
	
	free(ptr);
}

	
