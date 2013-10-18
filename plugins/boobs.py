import random
import urllib2


class getBoobsUrl:
    def __init__(self):
        self.url = self.getBoobs()

    def getUrl(self):
        result = True
        number = random.randrange(7630)
        url = 'http://media.oboobs.ru/boobs/0%s.jpg' % (str(number))
        self.__url = url

        try:
            urllib2.urlopen(url)
        except urllib2.HTTPError, e:
            if e.code != 200:
                result = False

        return result

    def getBoobs(self):
        while not(self.getUrl()):
            pass
        return self.__url

