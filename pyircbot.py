#!/usr/bin/env python
# -*- coding: cp1251 -*-

import socket
from config import botConfig
from boobs import getBoobsUrl
from kote import getkoteUrl


class ircBot:
    def __init__(self):
        self.__config = botConfig()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.Connect()

    def Connect(self):
        self.sock.connect((self.__config.host, 6667))
        self.sock.send(
            'USER ' + self.__config.uname + ' host servname : ' + self.__config.nick + ' - Python Bot by RusVicious\r\n')
        self.sock.send('NICK ' + self.__config.nick + '\r\n')
        self.sock.send('IDENTIFY ' + self.__config.password + '\r\n')
        self.sock.send('JOIN ' + self.__config.channel + '\r\n')
        self.__listening()

    def sendm(self, msg):
        self.sock.send('PRIVMSG ' + self.__config.channel + ' :' + str(msg) + '\r\n')

    def getNick(self, text):
        string = text[:text.find('!')]
        string = string[1:]
        return string

    def __listening(self):
        while 1:
            self.__text = self.sock.recv(2040)
            if not self.__text:
                break

            if self.__text.find('PING') != -1:
                self.sock.send('PONG ' + self.__text.split()[1] + '\r\n')

            if self.__text.find(':!сиськи') != -1:
                boobs = getBoobsUrl()
                self.sendm(boobs.url)

            if self.__text.find(':!котэ') != -1:
                kote = getkoteUrl()
                self.sendm(kote.url)

            print "[GET]", self.__text


if __name__ == '__main__':
    bot = ircBot()