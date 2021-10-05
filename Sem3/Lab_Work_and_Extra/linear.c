#include <stdio.h>
int search(int arr[], int n, int x)
{
    int i;
    for (i = 0; i < n; i++)
    {
        if (arr[i] == x)
        {
            printf("element found at index: %d",i);
        }
        if(i==n)
            {
                printf("element not found");
            }
    }

    return 0;
}
int main(void)
{
    int arr[] = { 24, 33, 41, 105, 30 };
    int x = 105;
    int n = sizeof(arr) / sizeof(arr[0]);
    int result = search(arr, n, x);
    return 0;
}
