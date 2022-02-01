#include <stdio.h>
#include<string.h>
int main(void) {
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
	    char s[100];
	    int c=0,d=0;
	    scanf("%s",s);
	    int l=strlen(s);
	    for(int j=0;j<=l;j++)
	    {
	        if(s[j]=='a'){
	            c+=1;
	        }
	        else if(s[j]=='b'){
	            d+=1;
	        }
	    }
	    if(c<=d)
	    printf("%d\n",c);
	    else if(d<=c)
	    printf("%d\n",d);
	    else if(c==0 || d==0)
	    printf("0");
	}
	return 0;
}

