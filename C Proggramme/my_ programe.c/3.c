#include <stdio.h>

int main ()
{
    int r, c, n ;
    scanf("%d", &n);

    for(r=n-1 ; r>=1 ; r--)   //printing rows.
    {
        for(c=1 ; c<=r ; c++) //printing column and star(*)
        {
            printf("*");
        }
        for(c=(2*r-1) ; c<(2*n-2) ; c++)  //printing space.
        {
            printf(" ");
        }
        for(c=1 ; c<=r ; c++)   //printing column and star(*)
        {
            printf("*");
        }
         printf("\n");    //printing new line.
    }
    printf("\n");

    for(r=1 ; r<n ; r++)   //printing rows.
    {
        for(c=1 ; c<=r ; c++) //printing column and star(*)
        {
            printf("*");
        }
        for(c=(2*r-1) ; c<(2*n-2) ; c++)  //printing space.
        {
            printf(" ");
        }
        for(c=1 ; c<=r ; c++)   //printing column and star(*)
        {
            printf("*");
        }
         printf("\n");    //printing new line.
    }
    return 0 ;
}
