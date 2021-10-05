#include<stdio.h>

void f();

int main(void){
	f();
	f();
	f();
	f();
}

void f(){
	static int a; //bydefault 0
	a++;
	printf("value of a = %d\n", a);
}
