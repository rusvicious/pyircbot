#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time
import sys
import re


from conf.config import botConfig
from plugins.boobs import getBoobsUrl
from plugins.kote import getkoteUrl

class ircBot:
    def __init__(self):
        self.__config = botConfig()
        self.connected = False;
        self.__attemptscount = 0;
        self.try_connect()

    def try_connect(self):
        if not(self.connected == True):
            if (self.__attemptscount <= 20):
                if (self.__attemptscount > 0):
                    print "Trying to connect to", self.__config.host                  
                    time.sleep(15);
                self.__attemptscount+= 1
                self.Connect()
				
    def Connect(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.__config.host, 6667))
            self.sock.send(
                'USER %s host servname : %s  - Python Bot by RusVicious\r\n' % (self.__config.uname, self.__config.nick))
            self.sock.send('NICK %s\r\n' % (self.__config.nick ))
            self.sock.send('IDENTIFY %s\r\n' % (self.__config.password))
            self.joinChannels(self.__config.channels)
            self.connected = True
            self.__attemptscount = 0;
            self.__listening()

        except socket.error,e:
            self.connected = False
            print "Could not connect to", self.__config.host  
            self.try_connect()

    
    def getmesInfo(self,msg):
        irc_pat = re.compile(ur"""
  ^\s*:
  # nickname:
  (?P<nickname>
    [a-zа-яёЁ_\-\[\]\\^{}|`]
    [a-zа-яёЁ0-9\-\[\]\\^{}|`]*
  )
  !~
  # ident:
  (?P<identifier>
    \w+
  )
  @
  # host:
  (?P<hostname>
    .*
  )
  \ PRIVMSG\      #
  # channel
  (?P<channel>
    \#\w+
  )
  \ :           #
  # message itself:
  (?P<message>
    .*
  )$
""", re.VERBOSE | re.UNICODE | re.IGNORECASE)
        match = irc_pat.match(msg)
        return match;
    
    def sendMessage(self, msg, channel):
        self.sock.send('PRIVMSG %s :%s\r\n' % (channel, self.mesEncode(str(msg))))
        
    def joinChannels(self, channels):
        for channel in channels:
            self.sock.send('JOIN %s\r\n' % (channel))


    def mesEncode(self, text):
        result = text.decode(self.__config.charset,'replace')
        return result

    def __listening(self):
        while self.connected:
            try:
                self.__text = self.sock.recv(2040)
                self.__text = self.mesEncode(self.__text)
                
                if not self.__text:
                    break

                if self.__text.find('PING') != -1:
                    self.sock.send('PONG %s\r\n' % (self.__text.split()[1]))

                if self.__text.find('KICK') != -1:
                    self.joinChannels(self.__config.channels)

                
                if self.__text.find(u':!сиськи') != -1:
                    boobs = getBoobsUrl()
                    match = self.getmesInfo(self.__text)
                    self.sendMessage(boobs.url, match.group('channel'))
                
                if self.__text.find(u':!котэ') != -1:
                    kote = getkoteUrl()
                    match = self.getmesInfo(self.__text)
                    self.sendMessage(kote.url, match.group('channel'))
					
                if self.__text.find(u':!quit') != -1:
                    self.sock.send('QUIT Bye!\r\n')

                print "[GET]", self.__text.encode(self.__config.charset);

            except socket.error, e:
                self.connected = False
                print "Disconnected from", self.__config.host 
                self.try_connect()
                
if __name__ == '__main__':
    bot = ircBot()