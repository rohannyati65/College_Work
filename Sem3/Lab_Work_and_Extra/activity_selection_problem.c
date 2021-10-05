
// C program for activity selection problem.
#include <stdio.h>
void printMaxActivities(int s[], int f[], int n)
{
    int i, j;
    printf("Following activities are selected n");
    i = 0;
    printf("%d ", i);
    for (j = 1; j < n; j++) {
        if (s[j] >= f[i]) {
            printf("%d ", j);
            i = j;
        }
    }
}
int main()
{
    int s[] = { 1, 5, 6, 8};
    int f[] = { 5, 8, 7, 10};
    int n = sizeof(s) / sizeof(s[0]);
    printMaxActivities(s, f, n);
    return 0;
}
