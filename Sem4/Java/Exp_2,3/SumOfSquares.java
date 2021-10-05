import java.util.Scanner;
class SumOfSquares
{
	public static void main(String[] args)
	{
		int n=10,sum=0;
		Scanner s = new Scanner(System.in);
		int a[] = new int[n];
		for(int i=0; i <n; i++){
			a[i] = s.nextInt();
			sum = sum + (a[i] * a[i]);
		}
		System.out.println("Sum : "+sum);
	}
}