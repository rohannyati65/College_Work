import java.util.Scanner;
class Grades
{
public static void main( String [] args )
{
Scanner key = new Scanner(System.in);
System.out.println("Enter the number of students");
int n = key.nextInt();
Student student_list[] = new Student[ n ];
System.out.println("Enter the name and score of --- ");
for( int i = 0 ; i < n ; i++ )
{
System.out.println("Student - " + (i+1));
String name = key.next();
int score = key.nextInt();
student_list[i] = new Student( name , score );
}
for( int i = 0 ; i < n - 1 ; i++ )
{
for( int j = 0 ; j < n - i - 1 ; j++ )
{
if( student_list[j+1].score < student_list[j].score )
{
Student temp = student_list[j+1];
student_list[j+1] = student_list[j];
student_list[j] = temp ;
}
}
}
System.out.print("\nSorted List ---> \n" );
for( int i = 0 ; i < n ; i++ )
{
student_list[i].printInformation();
}
String status[]= { "Pass" , "Merit" , "Distinction" };
int current = 0 ;
System.out.print("\nFail - ");
for( int i = 0 ; i < n ; i++ )
{
if( (student_list[i].score >=40 && current == 0) || (student_list[i].score >=51 && current == 1 ) ||
(student_list[i].score >=75 && current == 2))
System.out.print("\n" + status[current++] + " - ");
System.out.print(" " + student_list[i].name);
}
System.out.println();
}
}
class Student
{
int score ;
String name;
public Student( String name , int score )
{
this.score = score ;
this.name = name;
}
void printInformation ()
{
System.out.println("name - " + this.name + " grade --> "+ this.score );
}
}
