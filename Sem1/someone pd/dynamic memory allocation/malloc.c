#include<stdio.h>
#include<malloc.h>

int main(void){
	int *ptr, n, i = 0;
		
	printf("enter the size of memory to allocate\n");
	scanf("%d", &n);
	
	ptr = (int*)malloc(n*sizeof(int));
	
	printf("\n%d\n", *ptr);
	
	printf("enter n values\n");
	
	while(i <= n-1){
		scanf("%d", &ptr[i]); // &ptr[i] = (ptr+i)
		i++;
		}
		
	i = 0;	
	
	printf("you enter \n");
	while(i <= n-1)
		printf("%d\n", *(ptr+i++));	 // ptr[i] = *(ptr+i)
}
