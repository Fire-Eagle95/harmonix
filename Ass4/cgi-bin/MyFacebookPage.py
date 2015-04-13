#!/usr/bin/python

import cgi
form = cgi.FieldStorage()
username=form.getvalue("username")
#username="yko16"
name=""
userList= []
class User:
    def __init__(self, pUsername, pName, pFriendsList):
        self.us=pUsername
        self.na=pName
        self.friendslist=pFriendsList

def findName(pUsername):
    mList = open("./members.csv", "r", 0)    
    nameFound = ""
    for line in mList:
        NandUN = line.split(" ", 2)
        if pUsername==NandUN[1]:
            nameFound=NandUN[0]
    mList.close()
    return nameFound

def createUserList():
    mList = open("./members.csv", "r", 0)
    tempList= []
    for line in mList:
        attributes = line.split()
        aName=attributes[0]
        aUsername=attributes[1]
        aList=attributes[3:]
        userToAdd= User(aUsername, aName, aList)
        tempList.append(userToAdd)
    return tempList

class Topic:
    def __init__(self, pName, pTopic):
        self.user=pName
        self.topic=pTopic

def membersList():
    memberFile = open("./members.csv", "r", 0)
    finalList=[]
    for line in memberFile:
        attr = line.split(" ",2)
        aName = attr[1]
        finalList.append(aName)
    memberFile.close()
    return finalList


def topicsToDisplay():
    topics = open("./topic.csv", "r")
    line = topics.readline()
    toDisplay=[]
    while line!="" and len(toDisplay)!=10:
        aName=line.replace("\n","")
        if aName in fList:
            line = topics.readline()
            topikku = Topic(aName,line)
            toDisplay.append(topikku)
        line = topics.readline()
    topics.close()
    return toDisplay

def userFriends(nameToFind):
    friends = []
    members = open("./members.csv", "r", 0)
    for line in members:
        name_end = line.index(" ")
        currname = line[:name_end]
        if currname==nameToFind:
            splitList = line.split()
            friends = splitList[3:]
            members.close()
            return friends
    members.close()
    return friends

def write():
    print "Content-Type:text/html\r\n\r\n"
    print '<html>'
    print '<head>'
    print '<title>Talk music to me!</title>'
    print '</head>'
    print '<body background="../best2.jpg"><table width="100%" cellpadding=50><tr><td><center><h1><font color=#9933FF>Hey '
    print currentUser.na
    print '!</font></h1><br/><br/><br/><form name="input" action="http://cgi.cs.mcgill.ca/~pgianf/cgi-bin/MyFacebookPage.py" method="POST"><p><font color=#CC0099>Hey ! Update your status and tell us what is on your musical mind:</font></p><br/><input type="hidden" name="username" value='
    print currentUser.us
    print '><input type="text" name="update" size=100><br/><input type="submit" value="Submit"></form>'
 
#    friends = userFriends(username)
    if fList:
        topicsToPrint = topicsToDisplay()
        if topicsToPrint:
            print '<table width=700 cellpadding=25>'
            for toWrite in topicsToPrint:
                print '<tr bgcolor=#9933FF><th>'
                print toWrite.user
                print '</th></tr><tr bgcolor=#CCFFFF><td colspan=3><center>'
                print toWrite.topic
                print '</center></td></tr>'
            print '</table>'
    print '<form name="input" action="http://cgi.cs.mcgill.ca/~pgianf/cgi-bin/MyFacebookPage.py" method="POST"><p><font color=#CC0099>Add a SiDoReLa member to your FriendList: </font> </p><br><input type="hidden" name="username" value='
    print currentUser.us
    print '><input type="text" name="friend" size=15><br><input type="submit" value="Submit"></form></center></td><td width=150 bgcolor=#993366><font color=#00FFFF><i>SiDoReLa members usernames:</i><ul>'
    sidorelas = membersList()
    for member in sidorelas:
        print '<li>'
        print member
        print '</li>'
    print '</ul><a href="http://cgi.cs.mcgill.ca/~pgianf/welcome.html">LOGOUT</a></font></td></tr></table></body></html>'
    return

def updateTopics():
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

def addFriend():
    friend = form.getvalue('friend')
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

name=findName(username)
if "update" in form:
    updateTopics()
elif "friend" in form:
    addFriend()
fList= userFriends(name)
currentUser=User(username,name,fList)
userList=createUserList()
write()
