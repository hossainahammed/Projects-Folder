#include <stdio.h>

int main()
{
    int r , c , n;
    scanf("%d", &n);

    for(r=1 ; r<=n ; r++) // Printing rows.
    {
        for(c=1 ; c<=n ; c++) // Printing columns.
        {
           if(r==c)
           {
               printf("$ ");   // Printing $.
           }
           else if(r<c)
           {
               printf("@ ");    // Printing @.
           }
           else
           {
               printf("# ");    // Printing #.
           }
        }
        printf("\n");        // Printing new line.
    }

    return 0 ;
}


