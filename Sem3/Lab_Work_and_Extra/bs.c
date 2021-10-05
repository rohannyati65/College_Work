#include<stdio.h>
int binarySearch(int a[],int l,int r,int data)
{
    while(l<r)
    {
        int mid=((l+r)/2);
        if(data=a[mid])
            return mid;
        else if(data<a[mid])
            r=mid-1;
        else
            l=mid+1;
    }
    return -1;
}
int main(void)
{
    int a[] = { 3, 7, 14, 30, 58 };
    int data = 14;
    int n = sizeof(a) / sizeof(a[0]);
    int result = binarySearch(a, 0, n - 1, data);
    (result == -1) ? printf("Element is not present in array")
                   : printf("Element is present at index %d",result);
    return 0;
}
