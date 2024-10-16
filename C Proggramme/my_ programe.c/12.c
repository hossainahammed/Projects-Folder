#include<stdio.h>
int main(){
	int n,i,j,k;
	scanf("%d",&n);
	for(i=1;i<=2*n;i++){
		for(j=1;j<=2*n;j++){
			if(j>n-i && j<=n+i && i<n )printf(" ");
			else if(i==n || i==n+1)printf(" ");
			else if(i>n && j>=i-n && j<=3*n-i+1)printf(" ");
			else printf("#");
				}
				printf("\n");
		}
	}
