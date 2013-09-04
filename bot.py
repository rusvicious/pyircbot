#!/usr/bin/env python
# -*- coding: cp1251 -*-
import socket,time, random, urllib2, ConfigParser;

config = ConfigParser.RawConfigParser()
config.read('bot.cfg')

host = config.get("General","host")
channel = config.get("General","channel")
nick = config.get("General","nick")
uname = config.get("General","uname")
password = config.get("General","password")

def getUrl():
	number = random.randrange(7600)
	url =    "http://media.oboobs.ru/boobs/0"+str(number)+".jpg"
	return url;

def getBoobs(url):
	try:
		urllib2.urlopen(url);
		return url    
	except urllib2.HTTPError, e:
		if e.code != 200:
			getBoobs(getUrl())

def sendm(msg): 
	sock.send('PRIVMSG '+ channel + ' :' + str(msg) + '\r\n')
	
def getNick(text):
	string = text[:text.find('!')]
	string = string[1:]
	return string

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.connect((host, 6667)) 

sock.send('USER '+uname+' host servname : Boobsy - Python Bot by RusVicious\r\n') 
sock.send('NICK '+nick+'\r\n')
sock.send('IDENTIFY '+password+'\r\n')  

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
			sendm(getNick(text) +': Не командуй мне, ты не мой хозяин!')

	if (text.find(':bot') != -1) or (text.find(':бот') != -1):
		sendm(getNick(text) +': Кто бот, ты бот ёпта!')

	if text.find('JOIN :'+ channel) != -1:
		sendm('Здрасьте вам')

	if text.find(':KICK') != 1:
		sock.send('JOIN '+ channel +'\r\n')

	if text.find(':!date') != -1:
		sendm(''+ time.strftime("%A, %B %d, %Y", time.localtime()))
	
	if text.find(':!сиськи') != -1:
		sendm(getBoobs(getUrl()))
	
	if text.find(':!time') != -1:
		sendm(''+ time.strftime("%H:%M:%S", time.localtime()))

	print '[GET]', text