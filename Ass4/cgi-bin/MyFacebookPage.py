#!/usr/bin/python

import cgi
form = cgi.FieldStorage()				#get info from form
username=form.getvalue("username")

name=""							#declare name,

class User:						#User class,
    def __init__(self, pUsername, pName, pFriendsList):	#with username, name
        self.us=pUsername				#and friendsList
        self.na=pName
        self.friendslist=pFriendsList

def findName(pUsername):				#find name associated
    mList = open("./members.csv", "r", 0)    		#to the username,
    nameFound = ""					#that is given as
    for line in mList:					#parameter
        NandUN = line.split(" ", 2)
        if pUsername==NandUN[1]:
            nameFound=NandUN[0]
    mList.close()
    return nameFound

class Topic:						#Topic class, 
    def __init__(self, pName, pTopic):			#with the username
        self.user=pName					#and the topic itself
        self.topic=pTopic

def membersList():					#create a List of 
    memberFile = open("./members.csv", "r", 0)		#all the members
    finalList=[]					#with their usernames
    for line in memberFile:
        attr = line.split(" ",2)
        aName = attr[1]
        finalList.append(aName)
    memberFile.close()
    return finalList

def userFriends(nameToFind):				#return the friendList
    friends = []					#of a chosen user
    members = open("./members.csv", "r", 0)		#that is passed as a 
    for line in members:				#parameter.
        name_end = line.index(" ")			#(list of usernames)
        currname = line[:name_end]
        if currname==nameToFind:
            splitList = line.split()
            friends = splitList[3:]
            members.close()
            return friends
    members.close()
    return friends


def topicsToDisplay():					#find which topics
    topics = open("./topic.csv", "r")			#the current User should
    line = topics.readline()				#see on his/her page.
    toDisplay=[]					#It creates a list of
    while line!="" and len(toDisplay)!=10:		#Topic objects, stores
        aName=line.replace("\n","")			#them in a list which is
        if aName in fList:				#then returned
            line = topics.readline()
            topikku = Topic(aName,line)
            toDisplay.append(topikku)
        line = topics.readline()
    topics.close()
    return toDisplay

def write():						#write the page, 
    print "Content-Type:text/html\r\n\r\n"		#print headers
    print '<html>'
    print '<head>'
    print '<title>Talk music to me!</title>'
    print '</head>'
    print '<body background="../best2.jpg"><table width="100%" cellpadding=50><tr><td><center><h1><font color=#9933FF>Hey '		#print name of current
    print currentUser.na				#user
    print '!</font></h1><br/><br/><br/><form name="input" action="http://cgi.cs.mcgill.ca/~pgianf/cgi-bin/MyFacebookPage.py" method="POST"><p><font color=#CC0099>Hey ! Update your status and tell us what is on your musical mind:</font></p><br/><input type="hidden" name="username" value='
    print currentUser.us	#form: sends username + topicUpdate to the
				#MyFacebookPage.py program
    print '><input type="text" name="update" size=100><br/><input type="submit" value="Submit"></form>'
    if fList:					#if the friend List is not empty
        topicsToPrint = topicsToDisplay()	#calls topicsToDisplay,get list
        if topicsToPrint:			#of topics to display
            print '<table width=700 cellpadding=25>'
            for toWrite in topicsToPrint:	#if this list is not empty
                print '<tr bgcolor=#9933FF><th>'#display the topics
                print toWrite.user
                print '</th></tr><tr bgcolor=#CCFFFF><td colspan=3><center>'
                print toWrite.topic
                print '</center></td></tr>'
            print '</table>'
    print '<form name="input" action="http://cgi.cs.mcgill.ca/~pgianf/cgi-bin/MyFacebookPage.py" method="POST"><p><font color=#CC0099>Add a SiDoReLa member to your FriendList: </font> </p><br><input type="hidden" name="username" value='
    print currentUser.us	#form: sends username + friendToAdd to the
				#MyFacebookPage.py program
    print '><input type="text" name="friend" size=15><br><input type="submit" value="Submit"></form></center></td><td width=150 bgcolor=#993366><font color=#00FFFF><i>SiDoReLa members usernames:</i><ul>'
    sidorelas = membersList()			#call membersList to get
    for member in sidorelas:			#all the usernames and print
        print '<li>'				#them all
        print member
        print '</li>'
    print '</ul><a href="http://cgi.cs.mcgill.ca/~pgianf/welcome.html">LOGOUT</a></font></td></tr></table></body></html>'	#LOGOUT link
    return

def updateTopics():				#add a Topic to topic.csv
    update = form.getvalue('update')		
    topics = open("./topic.csv", "r")		
    newfile = username+"\n"+update+"\n"
    for line in topics:
        newfile += line
    topics.close()
    toWrite = open("./topic.csv", "w")
    toWrite.write(newfile)
    toWrite.close()
    return

def addFriend():				#add a friend to a user in 
    friend = form.getvalue('friend')		#members.csv
    newfile = ""		
    members = open("./members.csv","r", 0)	
    for line in members:
        name_end = line.index(" ")
        currname = line[:name_end]
        if currname==name:
            toRemove = line.index("\n")
            newline = line[:toRemove]+friend+" "+("\n")
            newfile+= newline
        else:
            newfile += line
    members.close()
    addF = open("./members.csv", "w", 0)
    addF.write(newfile)
    addF.close()
    return

name=findName(username)			#get the name matching 'username'
if "update" in form:			#if there is a variable 'update' in form
    updateTopics()			#update topic.csv with the given topic
elif "friend" in form:			#if there is a variable 'friend' in form
    addFriend()				#update members.csv
fList= userFriends(name)		#get the  friendList of the current user
currentUser=User(username,name,fList)	#create a User instance for current user
write()					#calls write(), creating the page
