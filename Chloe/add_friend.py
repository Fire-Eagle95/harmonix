#!usr/bin/python
import cgi
#import os
#form = cgi.FieldStorage()
#username = form.getvalue('username')
#newfriend = form.getvalue('friend')
username = "vithu"
friend = "theophile"
newfile = ""
members = open("./members.csv","r", 0)
for line in members:
	name_end = line.index(" ")
	name = line[:name_end]
	if name==username:
		toRemove = line.index("\n")
		newline = line[:toRemove]+" "+friend+("\n")
		newfile+= newline
	else:
		 newfile += line

members.close()
addFriend = open("./members.csv", "w", 0)
addFriend.write(newfile)
addFriend.close()
#os.system("MyFacebookPage.py")
