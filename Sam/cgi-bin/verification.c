#include<stdlib.h>
#include<stdio.h>
#include<string.h>

int main(){

printf("Content-Type: text/html\r\n\r\n");

char string[100];
char c;
char username[20];
char password[20];

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
string[a] = '\0';

int pos = 9;
int start = 0;
while(string[pos] != '&'){
	username[start]=string[pos];
	pos++;
	start++;	
}
username[start] = '\0';
start = 0;

pos = pos+10;
while(string[pos] != '\0'){
        password[start]=string[pos];
        pos++;
        start++;
}
password[start] = '\0';

int VALID=0;

FILE *file;
file = fopen("members.csv","r");
char line[50];
if(file == NULL){
	printf("ERROR WITH FILE");
	return 0;
}
while(fgets(line,50,file)!=NULL){
	char *entry;
        char *entry2;
        entry = strtok(line," ");
        entry2 = strtok(NULL," ");
        entry = strtok(NULL," ");
	if(strcmp(entry2,username) == 0 && strcmp(entry,password) == 0){
		VALID=1;
	}
}
fclose(file);

if(VALID){
	printf("<html><body><center> WELCOME BACK %s </center></body></html>", username);
	return 0;
}
else{
	printf("<html><body><center> Invalid Username/Password </center></body></html>");
}
}
