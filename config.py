import os, ConfigParser, random

class botConfig:
	def __init__(self):
		self.host = "irc.wenet.ru"
		self.channel = "#Bryansk"
		self.nick = "Guest" + str(random.randrange(10000))
		self.uname = "guest" + str(random.randrange(10000))
		self.password = "qwerty"
		
		if os.path.exists('bot.cfg'):
			self.__config = ConfigParser.RawConfigParser()
			self.__config.read('bot.cfg')
			
			self.host = self.__config.get("General","host")
			self.channel = self.__config.get("General","channel")
			self.nick = self.__config.get("General","nick")
			self.uname = self.__config.get("General","uname")
			self.password = self.__config.get("General","password")
		else:
			self.__config = ConfigParser.RawConfigParser()
			self.__config.add_section('General')
			self.__config.set('General','host', self.host)
			self.__config.set('General','channel', self.channel)
			self.__config.set('General','nick', self.nick)
			self.__config.set('General','uname',self.uname)
			self.__config.set('General','password',self.password)
		
			with open('bot.cfg', 'wb') as configfile:
				self.__config.write(configfile)