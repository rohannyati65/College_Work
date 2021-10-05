#include<stdio.h>
#include<time.h>
void display();
int partition(int [], int, int);
void quick(int [], int, int);
void merge(int [], int, int, int);
void merge_sort(int [], int, int);
void selectionSort(int [], int );
void bubble_sort(int[],int);
int main()
{
  int start, end, mid;
  clock_t start_time,end_time;
  double time_required;
  start = 0;
  int i,n;
  printf("Enter the number of elements:");
  scanf("%d",&n);
  int arr[n],a1[n],a2[n],a3[n],a4[n];
  printf("Enter the elements of array:\n");
  for(i = 0; i< n; i++){
       scanf("%d",&arr[i]);
    }
    for(i=0;i<n;i++){
        a1[i]=a2[i]=a3[i]=a4[i]=arr[i];
    }
  end = n - 1;
  mid = (start + end) / 2;
      start_time=clock();
      quick(a1, start, end);
      end_time=clock();
        time_required=("%d\n",((double)(end_time-start_time))*10e6)/CLOCKS_PER_SEC;
	  printf("total time taken by quick sort to sort the elements:%6.3f\n",time_required);
      start_time=clock();
      merge(a2, start, mid, end);
      merge_sort(a2, start, end);
      end_time=clock();
      time_required=("%d\n",((double)(end_time-start_time))*10e6)/CLOCKS_PER_SEC;
	  printf("total time taken by merge sort:%6.3f\n",time_required);
	  start_time=clock();
      selectionSort(a3,n);
       end_time=clock();
        time_required=("%d\n",((double)(end_time-start_time))*10e6)/CLOCKS_PER_SEC;
	  printf("total time taken by selection sort:%6.3f\n",time_required);
	  start_time=clock();
      bubble_sort(a4,n);
       end_time=clock();
        time_required=("%d\n",((double)(end_time-start_time))*10e6)/CLOCKS_PER_SEC;
	  printf("total time taken by bubble sort:%6.3f\n",time_required);
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


void swap(int *a, int *b) {
  int t = *a;
  *a = *b;
  *b = t;
}
int partition(int array[], int low, int high) {

  int pivot = array[high];
  int i = (low - 1);

  for (int j = low; j < high; j++) {
    if (array[j] <= pivot) {
      i++;
      swap(&array[i], &array[j]);
    }
  }

  swap(&array[i + 1], &array[high]);
  return (i + 1);
}
void quick(int a[], int start, int end) {
   int loc;
   if(start < end) {
     loc = partition(a, start, end);
     quick(a, start, loc - 1);
     quick(a, loc + 1, end);
}
}
void merge(int a[], int start, int mid, int end) {
    int i, j, k, index = start, temp[20000];
    i = start;
    j = mid +1;
    while((i<= mid) && (j <= end)) {
         if(a[i] < a[j]) {
             temp[index] = a[i];
             i++;
}
         else {
             temp[index] = a[j];
             j = j + 1;
}
      index++;
}
     if(i> mid) {
          while(j <= end) {
              temp[index] = a[j];
              j++;
              index++;
   }
}
      else {
         while(i<= mid) {
             temp[index] = a[i];
             i++;
             index++;
   }
}
     for(k = start; k < index; k++) {
         a[k] = temp[k];
    }
}
void merge_sort(int a[], int start, int end) {
    int mid;
    if(start < end) {
         mid = (start + end) / 2;
         merge_sort(a, start, mid);
        merge_sort(a, mid + 1, end);
merge(a, start, mid, end);
}
}
void selectionSort(int arr[], int n)
{
 int i, j, min_idx;
 for (i = 0; i < n-1; i++)
    {
        min_idx = i;
        for (j = i+1; j < n; j++)
		{
          if (arr[j] < arr[min_idx])
            min_idx = j;
		}
		int temp=arr[i];
		arr[i]=arr[min_idx];
		arr[min_idx]=temp;
	}

}
