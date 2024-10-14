#include <stdio.h>

int main ()
{
    int r , s , c , n ;
    scanf("%d", &n) ;

    for(r=1 ; r<=n-2 ; r++)   //printing rows.
    {
        for(s=1 ; s<= n-r-1 ; s++)
        {
            printf(" ");
        }
        for(c=1 ; c<=2*r-1 ; c++) //printing column and star(*)
        {
            printf("*");
        }
        for(c=(2*r-1) ; c<(2*n-6) ; c++)  //printing space.
        {
            printf(" ");
        }
        for(c=1 ; c<=2*r-1 ; c++)   //printing column and star(*)
        {
            printf("*");
        }
         printf("\n");    //printing new line.
    }
    for(r=n-3 ; r>=1 ; r--)   //printing rows.
    {
        for(s=1 ; s<= n-r-1 ; s++)
        {
            printf(" ");
        }
        for(c=1 ; c<=2*r-1 ; c++) //printing column and star(*)
        {
            printf("*");
        }
        for(c=(2*r-1) ; c<(2*n-6) ; c++)  //printing space.
        {
            printf(" ");
        }
        for(c=1 ; c<=2*r-1 ; c++)   //printing column and star(*)
        {
            printf("*");
        }
         printf("\n");    //printing new line.
    }

    return 0 ;
}

