#!usr/cgi-bin/python
import cgi
#import os
#form = FieldStorage()
#username = form.get('username')
#update = form.get('update')
username= "sam"
update = "You don't know pentatonix yet ? Check out their YouTube chanel ! I recommend Radioactive as a first, it's a-ma-zing"
topics = open("./topic.csv", "r")
newfile = username+"\n"+update+"\n"
for line in topics:
	 newfile += line
print newfile
topics.close()
toWrite = open("./topic.csv", "w")
toWrite.write(newfile)
toWrite.close()
#os.system("MyFacebookPage.py")
