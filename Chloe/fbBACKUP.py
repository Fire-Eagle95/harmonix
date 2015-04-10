#!usr/bin/python

import cgi
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
username=form.getvalue("username")
#username = "lesly"

class Topic:
    def __init__(self, pName, pTopic):
        self.name=pName
        self.topic=pTopic
def membersList():
    memberFile = open("../members.csv", "r", 0)
    finalList=[]
    for line in memberFile:
        name_end = line.index(" ")
        name = line[:name_end]
        finalList.append(name)
    memberFile.close()
    return finalList


def topicsToDisplay(friendsList):
    topics = open("../topic.csv", "r")
    line = topics.readline()
    toDisplay=[]
    while line!="" and len(toDisplay)!=10:
        name=line.replace("\n","")
        if name in friendsList:
            line = topics.readline()
            topikku = Topic(name,line)
            toDisplay.append(topikku)
        line = topics.readline()
    for i in toDisplay:
        print i.name
        print i.topic,
    topics.close()
    return toDisplay

def userFriends(nameToFind):
    members = open("../members.csv", "r", 0)
    for line in members:
        name_end = line.index(" ")
        name = line[:name_end]
        if name==nameToFind:
            splitList = line.split()
            friends = splitList[3:]
            members.close()
            return friends
    members.close()
    return none

def write():
#	f = open("updatedTopics.html", "w")
    print 'Content-Type: text/html\r\n\r\n'
    print '''<html>
<head>
	<title>Talk music to me!</title>
</head>'''
    str = '''<body background="best.jpg">
<table width="100%" cellpadding=50>
  <tr>
    <td>
      <center><h1><font color=#9933FF>Hey '''+username+'''!</font></h1><br><br><br>
      <form name="input" action="/cgi-bin/update_topic.py" method="get">
	<p><font color=#CC0099>Hey ! Update your status and tell us what's on your musical mind:</font> </p>
	<br>
 	<input type="hidden" name="username" value='''+username+'''>
	<input type="text" name="update" size=100>
	<br>
	<input type="submit" value="Submit">
      </form>
'''
 
    friends = userFriends(username)
    if friends:
        topicsToPrint = topicsToDisplay(friends)
    if topicsToPrint:
        str += '<table width=700 cellpadding=25>'
        for toWrite in topicsToPrint:
            str += '''<tr bgcolor=#9933FF>
        <th>'''+toWrite.name+'''</th>
		</tr>
		<tr bgcolor=#CCFFFF>
		<td colspan=3><center>'''+toWrite.topic+'''
		</center></td>
		</tr>
		'''
        str+= '</table>'
    str+= '''<form name="input" action="/cgi-bin/add_friend.py" method="get">
	<p><font color=#CC0099>Add a SiDoReLa member to your FriendList: </font> </p><br>
  	<input type="hidden" name="username" value='''+username+'''>
	<input type="text" name="friend" size=15>
<br>	<input type="submit" value="Submit">
      </form>
</center>
    </td>
    <td width=150 bgcolor=#993366>
	<font color=#00FFFF><i>SiDoReLa members:</i>
	<ul>
	'''
    sidorelas = membersList()
    for member in sidorelas:
        str+='<li>'+member+'</li>'
    str+= '''</ul>
	<a href="http://cgi.cs.mcgill.ca/~pgianf/harmonix/Pierre/become_member.html">LOGOUT</a></font>
    </td>
 
  </tr>
</table>
</body>
</html>
'''
    print str
    return

write()
