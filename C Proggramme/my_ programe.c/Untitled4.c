#include<stdio.h>
int main()
{
    char x,y;

    scanf("%c %c",&x, &y);
    for(char  i=x; i<=y; i++)
    {
        printf("%c=%d\n",i,i);
    }
    return 0;
}
