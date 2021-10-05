import java.util.Scanner;
class PossibleCombinations
{
	public static void main( String [] args )
	{
		Scanner key = new Scanner( System.in );
		System.out.println("Enter the three digits");
		char a = key.next().charAt(0);
		char b = key.next().charAt(0);
		char c = key.next().charAt(0);
		char arr[] = {a,b,c};
		System.out.println("Output:");
		for(int i = 0 ; i<3 ; i++){
			for(int j = 0 ; j<3 ; j++){
				for(int k = 0 ; k<3 ; k++){
					if(i!=j && j!=k && k!=i)
						System.out.println(arr[i]+" "+arr[j]+" "+arr[k]);
				}
			}
		}
	}
}
