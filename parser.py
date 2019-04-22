import xml.dom.minidom
import urllib.request
import datetime


class Parser:

    def __init__(self, response):
        self.dom = xml.dom.minidom.parse(response)
        self.dom.normalize()
        self.nodeArray = self.dom.getElementsByTagName("Valute")

    def getCorrectValutes(self):
        res = []
        for node in self.nodeArray:
            childList = node.childNodes
            res.append(childList[3].childNodes[0].nodeValue)
            # print(childList[3].childNodes[0].nodeValue)
        return res

    def getValue(self, name):
        for node in self.nodeArray:
            childList = node.childNodes
            if(childList[3].childNodes[0].nodeValue == name):
                s = str(childList[4].childNodes[0].nodeValue)
                s = s.replace(',', '.')
                return float(s)
        return None

    def getNominal(self, name):
        for node in self.nodeArray:
            childList = node.childNodes
            if(childList[3].childNodes[0].nodeValue == name):
                return int(childList[2].childNodes[0].nodeValue)
        return None


def getValue(date, name):
    url = "http://www.cbr.ru/scripts/XML_daily.asp?date_req={}".format(date.strftime("%d/%m/%Y"))
    response = urllib.request.urlopen(url)
    dom = xml.dom.minidom.parse(response)
    dom.normalize()
    nodeArray = dom.getElementsByTagName("Valute")
    for node in nodeArray:
        childList = node.childNodes
        if (childList[3].childNodes[0].nodeValue == name):
            s = str(childList[4].childNodes[0].nodeValue)
            s = s.replace(',', '.')
            return float(s)
    return None
