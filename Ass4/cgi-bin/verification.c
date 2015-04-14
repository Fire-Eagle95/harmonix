#include<stdlib.h>
#include<stdio.h>
#include<string.h>

int main(){

//declare HTML header
printf("Content-Type:text/html\r\n\r\n");

//string holds the parsed output of the cgi POST
char string[100];
char c;
//these strings hold the final values taken from the cgi POST
char username[20];
char password[20];

//a keeps track of position in String "string"
int a = 0;
int size = atoi(getenv("CONTENT_LENGTH"));
int validString = 1;

// this while loop iterates through the chars of the cgi POST and puts relevant characters into "string"
while((c=getchar()) != EOF && a < size){
	if (a<100){
		if(c == '+'){
			string[a] = ' ';
		}
		else{
			string[a] = c;
		}
		a++;
	}
}
//end the output string
string[a] = '\0';

//these next two loops put the values of the output "string" into the more useful strings "username" and "password"
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

//VALID will be the boolean check to see if a member with the right credentials was found
int VALID=0;

//open the members file and iterate through the lines searching for the correct username and password match
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
	//take the first substring that is bordered by space characters (this will be the users actual name)
        entry = strtok(line," ");
	//take the second substring that is bordered by space characters (this will be the username)
        entry2 = strtok(NULL," ");
	//take the first substring that is bordered by space characters (this will be the users password)
        entry = strtok(NULL," ");
	//if correct username and corresponding password were found, swich "VALID"
	if(strcmp(entry2,username)==0 && strcmp(entry,password)==0){
		//printf("Switching");
		VALID=1;
	}
}
fclose(file);

//check if correct username and corresponding password were found, if so, print out success webpage
if(VALID){
	printf("<html><body bgcolor=\"#A9F5F2\" text=\"#08088A\"><h3><center> WELCOME BACK %s!!! </center></h3></body></html>", username);
	printf("<form action=http://cgi.cs.mcgill.ca/~pgianf/cgi-bin/MyFacebookPage.py method=POST>");
	printf("<input type=\"hidden\" name=\"username\" value=\"%s\">", username);
	printf("<center><input type=\"submit\" value=\"Go to the Wall of musical expression\"></center>");
	printf("</form></body></html>");
	return 0;
}
//else, print out failure page
else{
	printf("<html><body bgcolor=\"#A9F5F2\" text=\"#08088A\"><h3><b><center> Invalid Username/Password </center></b></h3><br/><br/>");
	printf("<center><a href=\"http://cgi.cs.mcgill.ca/~pgianf/welcome.html\">Go back to Home page</a></center></body></html>");
}
}
