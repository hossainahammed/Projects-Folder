#include <stdio.h>

int main()
{
    int r , c , s , n ;
    scanf("%d", &n);

    for(r=1 ; r<=n ; r++) // Printing rows.
    {
        for(c=1 ; c<=r ; c++) //printing star(*)
        {
            printf("*");
        }
        printf("\n");   // Printing new line.
    }
    for(r=n ; r>=1 ; r--) // Printing rows.
    {

        for(s=1 ; s<=n-r+1 ; s++) // printing space.
        {
            printf(" ");
        }
        for(c=1 ; c<=r ; c++) //printing star(*)
        {
            printf("*");
        }
        printf("\n");   // Printing new line.
    }

    return 0 ;
}
