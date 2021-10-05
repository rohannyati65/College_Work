#include<stdio.h>
int binarySearch(int a[],int l,int r,int data)
{
    if(r>=1)
    {
        int mid=((l+(r-1))/2);
        if(data==a[mid])
            return mid;
        else if(data<a[mid])
            return binarySearch(a,1,mid-1,data);
        else
            return binarySearch(a,mid=1,r,data);
    }
    return -1;
}
int main(void)
{
    int a[] = { 2, 3, 4, 10, 40 };
    int data = 10;
    int n = sizeof(a) / sizeof(a[0]);
    int result = binarySearch(a, 0, n - 1, data);
    (result == -1) ? printf("Element is not present in array")
                   : printf("Element is present at index %d",result);
    return 0;
}
