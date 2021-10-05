
#include <stdio.h>

#include<stdio.h>
int binarySearch(int a[], int l, int r, int data)
{
	if (r >= l) {
		int mid = l + (r - l) / 2;

		if (a[mid] == data)
			return mid;

		if (a[mid] > data)
			return binarySearch(a, l, mid - 1, data);
        return binarySearch(a, mid + 1, r, data);
	}
	return -1;
}

int main(void)
{
	int a[] = { 1, 5, 9,30, 50 };
	int n = sizeof(a) / sizeof(a[0]);
	int data = 1;
	int result = binarySearch(a, 0, n - 1, data);
	if(result == -1)
        printf("Element is not present in array");
    else
        printf("Element is present at index %d",
							result);
	return 0;
}
