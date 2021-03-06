﻿# -*- coding: utf-8 -*-

import os
import ConfigParser
import random


class botConfig:
    def __init__(self):
        self.__randomnum = str(random.randrange(10000))
        self.host = "irc.wenet.ru"
        self.channels = "#Bryansk"
        self.nick = "Guest" + self.__randomnum
        self.uname = "guest" + self.__randomnum
        self.password = "qwerty"
        self.charset = "cp1251"

        if os.path.exists('bot.cfg'):
            self.__config = ConfigParser.RawConfigParser()
            self.__config.read('bot.cfg')

            self.host = self.__config.get("General", "host")
            self.channels = self.__config.get("General", "channels").split(',');
            self.nick = self.__config.get("General", "nick")
            self.uname = self.__config.get("General", "uname")
            self.password = self.__config.get("General", "password")
            self.charset = self.__config.get("General", "charset")
        else:
            self.__config = ConfigParser.RawConfigParser()
            self.__config.add_section('General')
            self.__config.set('General', 'host', self.host)
            self.__config.set('General', 'charset', self.charset)
            self.__config.set('General', 'channels', self.channels)
            self.__config.set('General', 'nick', self.nick)
            self.__config.set('General', 'uname', self.uname)
            self.__config.set('General', 'password', self.password)

            with open('bot.cfg', 'wb') as configfile:
                self.__config.write(configfile)