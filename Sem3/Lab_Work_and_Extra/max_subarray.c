// C program to find the maximum product subarray in the given array

#include

#include

int min (int x, int y) {return x < y? x : y; }

int max (int x, int y) {return x > y? x : y; }

int maxSubarrayProduct(int arr[], int n)

{

int max_ending_here = 1;

int min_ending_here = 1;

int max_so_far = 1;

for (int i = 0; i < n; i++)

{

if (arr[i] > 0)

{

max_ending_here = max_ending_here*arr[i];

min_ending_here = min (min_ending_here * arr[i], 1);

}

else if (arr[i] == 0)

{

max_ending_here = 1; // max at current position

min_ending_here = 1;

}

else

{

int temp = max_ending_here; // temp variable to store max

max_ending_here = max (min_ending_here * arr[i], 1); // update maximum product

min_ending_here = temp * arr[i];

}

if (max_so_far < max_ending_here)

max_so_far = max_ending_here; // update max value

}

return max_so_far; // return the max value

}

int main()

{

int siz;

printf(“nEnter the size of the array : “);

scanf(“%d”,&siz);

int arr[10];

// Input the array elements

printf(“nInput the array elements : “);

for(int i=0;i<siz;i++)

scanf(“%d”,&arr[i]);

printf(“nMaximum product : %dn”,maxSubarrayProduct(arr, siz)); // call the function

return 0;

}
