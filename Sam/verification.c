#include<stdlib.h>
#include<stdio.h>

int main(){

char string[100];
char c;
int a = 0;
int size = atoi(getenv("CONTENT_LENGTH"));
int validString = 1;

while((c=getchar()) != EOF && a < size){
	if (a<100){
		if(c == '+'){
			string[a] = ' ';
		}
		else if(c == '%'){
			validString = 0;	
		}
		else{
			string[a] = c;
		}
		a++;
	}
}

printf("Content-Type:text/html\n\n");
if(validString){
	printf("<html><body><center> string </center></body></html>");
	return 0;
}
else{
	printf("<html><body><center> ERROR </center></body></html>");
}

}
