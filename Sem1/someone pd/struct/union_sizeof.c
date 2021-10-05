#include<stdio.h>

union abc{
	int a;
	char ch[22];
};

int main(void){
	union abc a1;
	printf("%d", sizeof(a1));
}


