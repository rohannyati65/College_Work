#include"extern1.c"
#include<stdio.h>

int main(void){
	extern a;
	printf("%d", a);
}
