#include <stdio.h>

int main ()
{
    int r, c, n;
    scanf("%d", &n);

    for(r=1 ; r<=n ; r++)
    {
        for(c=1 ; c<=n ; c++)
        {
            if(r==1||r==n || c==1||c==n|| r+1==c+1||r+c-1==n)
              {
                 printf("@");
              }
          else
            printf(" ");
        }
        printf("\n");
    }

    return 0 ;
}

