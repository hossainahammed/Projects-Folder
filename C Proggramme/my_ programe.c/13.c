#include<stdio.h>
int main(){
	int n,i,j,k;
	scanf("%d",&n);
	for(i=1;i<=n;i++){
		for(j=1;j<=2*n;j++){
			if(j<=i){
				if(i%2!=0)printf("#");
				else printf("&");
				}
		else if(j>i && j<=2*n-i)printf(" ");
		else{
			if(i%2!=0)printf("&");
			else printf("#");
			}
		}
		printf("\n");
	}
	}
