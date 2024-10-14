#include <stdio.h>

int main()
{
    int r , c , n ;
    scanf("%d", &n);

    for(r=1 ; r<= n ; r++)
    {
        for(c=1 ; c<=r ; c++)
        {
           if(r%2==0)
           {
               printf("&");
           }
           else
           {
               printf("#");
           }
        }
       for(c=2*r-1 ; c<=2*n-2 ;c++)
       {
           printf(" ");
       }
       for(c=1 ; c<=r ; c++)
        {
           if(r%2==0)
           {
               printf("#");
           }
           else
           {
               printf("&");
           }
        }
        printf("\n");
    }

    return 0 ;
}

