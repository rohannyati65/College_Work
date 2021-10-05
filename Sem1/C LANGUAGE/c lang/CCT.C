#include<stdio.h>
int func(int, int);
int main()
{

int a = func(3,8);

printf("%d", a);

return 0;

}
int func(int a, int b)
{

if(b==0)        return 0;

if(b==1)        return a;

return a + func(a,b-1);
}
