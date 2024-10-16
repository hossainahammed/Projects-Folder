#include<stdio.h>
int main(){
	int n,i,j,k;
	scanf("%d",&n);
	for(i=1;i<=n;i++){
		for(j=1;j<=n;j++){
			if(i==j)printf("s");
			else if(i>1 && i>j){
				printf("#");
				}
				else printf("@");
		}
		printf("\n");
	}
	}
