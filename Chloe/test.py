#!usr/bin/env python
# -*- coding: UTF-8 -*-
import cgi
form = cgi.FieldStorage()
hi = form.getvalue("username")
print "Content-type: text/html\r\n\r\n"
str = "<html><head><title>Hi</title></head>"
str+= "<body><p>Hi People i just want this to work.<br> The user is:"+username+"</p>"
str += "</body>"
str += "</html>"
print str
