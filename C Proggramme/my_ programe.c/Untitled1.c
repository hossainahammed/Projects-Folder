//Non alphabetic characters totall number print kora
#include <string.h>

int main()
{
    char s[1000];
    int i,alphabets=0,digits=0,specialcharacters=0,nonalphebaticcharacter;

    printf("Enter  the string : ");
    gets(s);

    for(i=0;s[i];i++)
    {
        //if((s[i]>=65 && s[i]<=90)|| (s[i]>=97 && s[i]<=122) )
         if((s[i]>='a' && s[i]<='z') || (s[i]>='A' && s[i]<='Z'))
          alphabets++;
        else if(s[i]>='0' && s[i]<='9')// else if(s[i]>=48 && s[i]<=57)
         digits++;
        else
         specialcharacters++;

 	}


/* printf("Alphabets = %d\n",alphabets);
    printf("Digits = %d\n",digits);
    printf("Special characters = %d\n", specialcharacters);
*/
nonalphebaticcharacter =(alphabets+digits+specialcharacters)-(alphabets);
  printf("non Alphabets = %d\n",nonalphebaticcharacter);
    return 0;
}
