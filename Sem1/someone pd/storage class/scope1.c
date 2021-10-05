#include<stdio.h>
int main(void){
	int x = 5;
	printf("outer block x = %d\n", x);
	{
		int x = 10;
		printf("inner block x = %d\n", x);
	}
	printf("%d\n", x);
}
