#include<stdlib.h>
#include<stdio.h>
#include<string.h>

int main(){

printf("Content-Type:text/html\r\n\r\n");

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
file = fopen("./members.csv","r");
char line[100];
if(file == NULL){
	printf("ERROR WITH FILE");
	return 0;
}
while(fgets(line,100,file)!=NULL){
	char *entry;
        char *entry2;
        entry = strtok(line," ");
        entry2 = strtok(NULL," ");
        entry = strtok(NULL," ");
	//printf("username is %s, password is %s, entry2(name) is %s, entry(pswd) is %s \n", username, password, entry2, entry); 
	//printf("username comparison is %d", strcmp(entry2,username));
	//printf("psswd comparison is %d", strcmp(entry,password));
	if(strcmp(entry2,username)==0 && strcmp(entry,password)==0){
		//printf("Switching");
		VALID=1;
	}
}
fclose(file);

if(VALID){
	printf("<html><body bgcolor=\"#A9F5F2\" text=\"#08088A\"><h3><center> WELCOME BACK %s!!! </center></h3></body></html>", username);
	printf("<form action=http://cgi.cs.mcgill.ca/~pgianf/cgi-bin/MyFacebookPage.py method=POST>");
	printf("<input type=\"hidden\" name=\"username\" value=\"%s\">", username);
	printf("<center><input type=\"submit\" value=\"Go to the Wall of musical expression\"></center>");
	printf("</form></body></html>");
	return 0;
}
else{
	printf("<html><body bgcolor=\"#A9F5F2\" text=\"#08088A\"><h3><b><center> Invalid Username/Password </center></b></h3><br/><br/>");
	printf("<center><a href=\"http://cgi.cs.mcgill.ca/~pgianf/welcome.html\">Go back to Home page</a></center></body></html>");
}
}
