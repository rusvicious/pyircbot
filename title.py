import urllib2
import re


class getTitleText:
    def __init__(self, link):
        self.title = self.getTitle(link)

    def getUrl(self, link):
        result = True
        url = link
        self.__url = url

        try:
            request = urllib2.Request(url)
            request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.0; rv:21.0) Gecko/20100101 Firefox/21.0')
            opener = urllib2.build_opener()
            data = opener.open(request).read()
            text = re.findall('<title>(.+)</title>',data)
            self.__title = text[0]
        except urllib2.HTTPError, e:
            if e.code != 200:
                result = False
                print "Error"

        return result

    def getTitle(self, link):
        self.getUrl(link)
        return "Title: " + self.__title

