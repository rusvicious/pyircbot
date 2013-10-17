#!/usr/bin/env python
# -*- coding: cp1251 -*-

import socket
import time
import sys

from config import botConfig
from plugins.boobs import getBoobsUrl
from plugins.kote import getkoteUrl



class ircBot:
    def __init__(self):
        self.__config = botConfig()
        self.__attemptscount = 0;
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.try_connect()

    def try_connect(self):
        if not(self.Connect()):
            if (self.__attemptscount <= 20):
                time.sleep(15)
                self.__attemptscount+= 1
                self.try_connect()


    def Connect(self):
        try:
            self.sock.connect((self.__config.host, 6667))
            self.sock.send(
                'USER %s host servname : %s  - Python Bot by RusVicious\r\n' % (self.__config.uname, self.__config.nick))
            self.sock.send('NICK %s\r\n' % (self.__config.nick ))
            self.sock.send('IDENTIFY %s\r\n' % (self.__config.password))
            self.sock.send('JOIN %s\r\n' % (self.__config.channel))
            result = True
            self.__listening()

        except socket.error,e:
            result = False

        return result

    def sendMessage(self, msg):
        self.sock.send('PRIVMSG %s :%s\r\n' % (self.__config.channel, str(msg)))

    def getNick(self, text):
        string = text[:text.find('!')]
        string = string[1:]
        return string

    def __listening(self):
        while 1:
            try:
                self.__text = self.sock.recv(2040)
                if not self.__text:
                    break

                if self.__text.find('PING') != -1:
                    self.sock.send('PONG %s\r\n' % (self.__text.split()[1]))

                if self.__text.find('KICK') != -1:
                    self.sock.send('JOIN %s\r\n' % (self.__config.channel))
                    self.sendMessage('Hello, I\'m %s, my platform is %s' %(self.__config.nick, sys.platform))

                if self.__text.find(':!������') != -1:
                    boobs = getBoobsUrl()
                    self.sendMessage(boobs.url)

                if self.__text.find(':!����') != -1:
                    kote = getkoteUrl()
                    self.sendMessage(kote.url)


                print "[GET]", self.__text

            except socket.error, e:
                self.try_connect()


if __name__ == '__main__':
    bot = ircBot()