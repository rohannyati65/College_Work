#include<stdio.h>

void selection_sort(int arr_wt[],int arr_pro[],int n)
{
    int temp,max_loc;
    double fractional;
    for(int i=0;i<n;i++)
    {
        fractional = arr_pro[i]/arr_wt[i];
        //max=arr_pro[i];
        max_loc=i;
        for(int j=i;j<n;j++)
        {
            int frac = ((double)arr_pro[j]/arr_wt[j]);
            if(frac>fractional)
            {
                //max=array[j];
                max_loc=j;
            }
        }

        //sorting profit array
        temp=arr_pro[i];
        arr_pro[i]=arr_pro[max_loc];
        arr_pro[max_loc]=temp;

        //sorting weight array
        temp = arr_wt[i];
        arr_wt[i] = arr_wt[max_loc];
        arr_wt[max_loc] = temp;

    }
}


int knapsack(int arr_wt[],int arr_pro[],int n,float w)
{
    float currpro=0;

    for(int i=0;i<n;i++)
    {
        if(w>0 && arr_wt[i]<=w)
        {
            w=w-arr_wt[i];
            currpro+=arr_pro[i];
        }
        else if(w>0)
        {
            currpro+=(w*((arr_pro[i])/(arr_wt[i])));
        }
        else break;

    }

    return currpro;
}


int main()
{
    int n;
    float w=0;

    scanf("%d",&n);
    printf("enter the length of input : %d\n ",n);
    printf("\n");

    int weight[n],profit[n];
    for(int i=0;i<n;i++)
    {
        scanf("%d",&weight[i]);
        printf("weight : %d\n",weight[i]);
        scanf("%d",&profit[i]);
        printf("profit : %d\n",profit[i]);
    }


    scanf("%f",&w);
    printf("enter the max weight that can be stored : %f\n",w);

    selection_sort(weight,profit,n);

    float res = knapsack(weight,profit,n,w);
    printf("The maximum profit : %f",res);

    return 0;
}
