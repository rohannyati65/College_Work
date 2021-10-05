#include<stdio.h>


void f();

int main(void){
	extern int x;
	printf("x = %d\n", x);
	x++;
	f();
}

int x;
void f(){
	printf("x = %d", x);
}
