
class Sum
    {
        public static void main(String[] args)
	{
        int sum=0;
        //for-loop for numbers 40-250
        for(int i=40 ;i<251 ;i++)
		{
            	// condition to check if number should be divided by 5
            	if(i%5==0){                
                //adding values of array so that total sum can be calculated
                	sum=sum+i;   
            		}   
       		}
        //final display output for the code 
        System.out.println("the sum of intergers from 40 to 250 that are divisible by 5 : "+sum);
    	}
}