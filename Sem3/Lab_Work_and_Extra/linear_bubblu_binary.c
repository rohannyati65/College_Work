#include<stdio.h>
#include<stdlib.h>
#include<time.h>

void linear_search(int*,int,int);
void bubble_sort(int*,int);
void binary_search(int*,int,int);

int main()
{
   int i, n, search, array[100000], loc;
   clock_t start,end;
   double time_required;

   printf("Enter number of elements\n");
   scanf("%d",&n);

   printf("Enter %d integers\n", n);

   for (i = 0; i < n; i++)
      scanf("%d",&array[i]);

	printf("enter the key to search\n");
	scanf("%d",&search);

	start=clock();
	linear_search(array,n,search);
	end=clock();
	time_required=("%d\n",((double)(end-start))*10e9)/CLOCKS_PER_SEC;
	printf("total time taken by linear search:%6.3f\n",time_required);

	bubble_sort(array, n);

	start=clock();
    binary_search(array,n,search);
   	end=clock();
   	time_required=("%d\n",((double)(end-start))*10e9)/CLOCKS_PER_SEC;
	printf("total time taken by binary search:%6.3f\n",time_required);

return 0;
}
void linear_search(int array[],int n,int search){
	 for(int i=0;1<n;i++){
		if(array[i]==search){
			printf("key location is %d\n",i+1);
			break;
		}
	}
}
void bubble_sort(int array[], int n)
{
   for ( int i = 0; i < n ; i++)
   {
	  for ( int j = 0; j < n-i -1 ; j++)
	   {

           if (array[j] > array[j+1])
		   {
			int temp=array[j];
			array[j]=array[j+1];
			array[j+1]=temp;
		   }
	   }

	}
}
void binary_search(int array[],int n,int search)
{
   int first, last, middle;
   first = 0;
   last = n - 1;
   middle = (first+last)/2;

   while (first <= last) {
      if (array[middle] < search)
         first = middle + 1;

      else if (array[middle] == search) {
         printf("%d found at location %d.\n", search, middle+1);
         break;
      }

      else
         last = middle - 1;

      middle = (first + last)/2;
   }
   if (first > last)
      printf("Not found! %d is not present in the list.\n", search);
}
