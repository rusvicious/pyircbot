import random
import urllib2
import re


class getkoteUrl:

    def __init__(self):
        self.url = self.getKote()

    def getKote(self):
        number = random.randrange(353)
        url =    "http://kote-img.com/" + str(number)

        try:
            response = urllib2.urlopen(url)
            data = response.read()
            kote  = re.findall("src=\"/media/kotes/(.+)\"",data)
            res = "http://kote-img.com/media/kotes/" + kote[0]
        
        except urllib2.HTTPError, e:
            if e.code != 200:
                self.getKote()

        return res