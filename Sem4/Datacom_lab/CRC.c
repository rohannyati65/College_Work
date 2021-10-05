#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void display(char msg[] , char rem[])
{
    int l1 = strlen(msg); //length of data(message)
    int l2 = strlen(rem); // length of remainder string(array)[]
    int i,j=0;
    char Data[20];

	//getting the encoded data

    for ( i=0; i<l1 ; i++) // going through data(message)
    {
        Data[i]=msg[i]; //copying the message into data array
    }

    for (i=l1; i<(l1 + l2); i++) // now combing message and remainder into data for the encoded data
    {
        Data[i]=rem[j]; //since i started from l1 it will just append rem values in further locations
        j++; //for rem values
    }

    printf("\n\n R E M A I N D E R  : %s", rem);

	int l3 = strlen(Data); //length of encoded data

    printf("\n E N C O D E D  D A T A  : ");

    for ( i = 0; i < l3 ; i++)
    {
		if(Data[i]=='0' || Data[i]=='1')
		{
            printf("%c", Data[i]);
		}
    }
    printf("\n\n");

}

void Div(char msg[] , const char* newmsg , char key[], int len1, int len2)
{
    char temp1[30], temp2[100], rem[30], temp3[30];
    strcpy(temp3, key); //key string copied to a temporary(3) array
	int i,j;
    for ( i = 0; i < len2; i++)
	{
		temp1[i] = newmsg[i];  // another temporary(1) array copying the new message (with the extra zeros one)
	}

    for (i = 0; i < len1; i++)
    {
        temp2[i] = temp1[0]; // cloning the temporary(1) into another temporary(2) array

        if (temp2[i] == '0') //when encountered a '0'
        {
			for ( j = 0; j < len2; j++)
			{
				key[j] = '0'; // make that location element(character) in key '0'
			}
		}
        else //when encountered a '1'
        {
			for ( j = 0; j < len2; j++)
			{
				key[j] = temp3[j]; // keep that element(character) same as temp3 is a clone of key itself
			}
		}

        for ( j = len2 - 1; j > 0; j--) //loop starting from key last element(character) till the first element
        {
            if (temp1[j] == key[j]) // when both data(temp1) and key have same element(character)
            {
				rem[j - 1] = '0'; // the subtraction of that will be '0'
			}
            else // when both data(temp1) and key do not have same element(character)
            {
				rem[j - 1] = '1'; // the subtraction of that will be '1'
			}
        }
        rem[len2 - 1] = newmsg[i+len2]; // keeping the element(character) 0 from *Append function
        strcpy(temp1, rem); // temp1 getting overwritten one by one
    }
    strcpy(rem, temp1); // after complete overwriting temp1 we copy it back to remainder array
    display(msg , rem) ;
}

// const char * is used as we are returning a string
const char *Append(char msg[], int len1, int len2) // to add extra zeroes
{
	int i;
    for (i=0; i <(len2-1); i++)
    {
        msg[len1 + i] = '0'; // addition of zeroes after the entered data for the updated data
    }
    return msg;
}

int main()
{
    char msg[50], key[25];
    char temp[50] ;

    printf("\nD A T A  : ");
    gets(msg);
    strcpy(temp , msg) ;

    printf("\nK E Y  : ");
    gets(key);

    int len1 = strlen(msg);
    int len2 = strlen(key);

	const char *newmsg = Append(msg, len1, len2); //getting a string

    printf("\nU P D A T E D   D A T A  : %s", newmsg);

	printf("\n\n[%s / %s]",key,newmsg);

    Div(temp , newmsg, key, len1, len2);
    return 0;
}
