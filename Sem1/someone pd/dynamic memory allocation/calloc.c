#include<stdio.h>
#include<malloc.h>

int main(void){
	int *ptr, n, i = 0;
	
	printf("enter the size of memory to allocate\n");
	scanf("%d", &n);
	
	ptr = (int*)calloc(n, sizeof(int));
	
	printf("\n%d\n", *ptr);
	
	
	while(i <= n-1)
		scanf("%d", ptr+i++);
		
	i = 0;	
	
	while(i <= n-1)
		printf("%d\n", *(ptr+i++));	
}
