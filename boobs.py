import random, urllib2
class getBoobsUrl:
	def __init__(self):
		self.url = self.getBoobs()

	def getBoobs(self):
		number = random.randrange(7600)
		url =    "http://media.oboobs.ru/boobs/0"+str(number)+".jpg"
		
		try:
			urllib2.urlopen(url)
			res =  url

		except urllib2.HTTPError, e:
			if e.code != 200:
				self.getBoobs()
		
		return res