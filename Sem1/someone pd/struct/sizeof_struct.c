#include<stdio.h>

struct abc{
	int a;
	char ch[5];
};

int main(void){
	struct abc a1;
	printf("%d", sizeof(a1));
}


