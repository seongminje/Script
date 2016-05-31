import urllib
import http.client
from xml.dom.minidom import *

def API(client, server) :
    conn = http.client.HTTPConnection(client)
    hangul_utf8 = urllib.parse.quote("")
    conn.request("GET", server+hangul_utf8)
    req = conn.getresponse()
    print(req.status,req.reason)
    cLen = req.getheader("Content-Length")
    data = req.read(cLen).decode('utf-8')
    return data

def Parsing(xmlsrc) :
    doc = parseString(xmlsrc)
    names = doc.getElementsByTagName("item")
    list= []
    for i in range (names.length):
        contents = names[i].getElementsByTagName("ttTitle")
        list.append(contents[0].firstChild.data)
    return list
