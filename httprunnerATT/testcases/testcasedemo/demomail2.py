#!/usr/bin/python
#-*- coding: utf-8 -*-
import smtplib
import sys
import string

#def sendemail():
smtp = smtplib.SMTP()

user = "1304085583@qq.com"
passwd = "gxxacyfysvgtfgge"

try:
	smtp.connect("smtp.qq.com", "465")
# except Exception:
# 	print "smtp.connect:",str(Exception)
# 	exit()
smtp.starttls()
smtp.login(user, passwd)

text = "Hello!"
body = string.join((
	"From: %s" % user,
	"To: %s" % sys.argv[1],
	"Subject: %s" % "Python",
	"",
	text
	),"\r\n")

print body
try:
	smtp.sendmail(user, [sys.argv[1]], body)
except Exception,e:
	print "smtp.sendmail:",str(e)
	exit()

smtp.quit()