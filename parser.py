import xml.dom.minidom


class Parser():

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
