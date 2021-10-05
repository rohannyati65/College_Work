#include<stdio.h>
struct abc{
	int a;
	char b;
};
int main(){
	struct abc h;
	printf("\n%d", sizeof(h));
}
