#include <stdio.h>

int main ()
{
    int r, c, n;
    scanf("%d", &n);

    for(r=1 ; r<=n ; r++)
    {
        for(c=1 ; c<=n ; c++)
        {
          if((r==c && (r!=n-r+1 || c!=n-r+1)) ||(r+c==n+1 && (r!=n-r+1 || c!=n-r+1)))
          {
              printf("@");
          }
         if((r==n-r+1) && (c==n-r+1))
          {
             printf("?");
          }

          else
            printf(" ");
        }
        printf("\n");
    }

    return 0 ;
}

