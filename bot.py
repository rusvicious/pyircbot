#!/usr/bin/env python
# -*- coding: cp1251 -*-
import os, socket, time, random, urllib2, ConfigParser;
from config import botConfig

config = botConfig()

def sendm(msg): 
	sock.send('PRIVMSG '+ config.channel + ' :' + str(msg) + '\r\n')
	
def getNick(text):
	string = text[:text.find('!')]
	string = string[1:]
	return string

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.connect((config.host, 6667)) 

sock.send('USER '+config.uname+' host servname : '+config.nick+' - Python Bot by RusVicious\r\n') 
sock.send('NICK '+config.nick+'\r\n')
sock.send('IDENTIFY '+config.password+'\r\n')  

while 1:
	text = sock.recv(2040)
	if not text:
		break
        
	if text.find('PING') != -1: 
		sock.send('PONG ' + text.split() [1] + '\r\n')

	if (text.find(':!quit') != -1): 
		if(getNick(text) == 'Trollface'):
			sock.send('QUIT :I\'ll be back!\r\n')
		else:
			sendm(getNick(text) +': You are not my owner!')

	if (text.find(':bot') != -1):
		sendm(getNick(text) +': I\'m not bot!')

	if text.find('JOIN :' + config.channel) != -1:
		sendm('Hello, ' + config.channel)

	if text.find(':KICK') != 1:
		sock.send('JOIN '+ config.channel +'\r\n')

	if text.find(':!date') != -1:
		sendm(''+ time.strftime("%A, %B %d, %Y", time.localtime()))
	
	if text.find(':!time') != -1:
		sendm(''+ time.strftime("%H:%M:%S", time.localtime()))

	print '[GET]', text