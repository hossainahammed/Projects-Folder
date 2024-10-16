#include<stdio.h>

int main()
{
   int id;
scanf("%d",id);
id= id%3;
int covid=0;
while(id%2){

 printf("\tHate!!\nOnline exam!\n");
covid++;

if(covid==id+3)break;

}
return 0;
}
