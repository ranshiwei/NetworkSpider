__author__ = 'Ran'
import re
import urllib
import urllib.request

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    html = html.decode('GBK')
    return html

def getImg(html):
    imgre = re.compile('src=\"(.+?\\.jpg)\"')
    imglist = imgre.findall(html)
    x = 0
    for imgurl in imglist:
        if 'http' not in imgurl:
            imgurl = 'http:' + imgurl
        urllib.request.urlretrieve(imgurl, 'D:\pic\%s.jpg' % x)
        x += 1

html = getHtml('http://mm.taobao.com/json/request_top_list.htm?type=0&page=0')
getImg(html)
