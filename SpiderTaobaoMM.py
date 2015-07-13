__author__ = 'Ran'
import urllib
import re
import urllib.request
import urllib.parse
from collections import deque

initurl = 'http://mm.taobao.com/json/request_top_list.htm?type=0&page='
i = 0
ph = -1
temp = '''<img src="'''
while i < 1:
    cururl = initurl + str(i)
    i += 1
    queue = deque()
    visited = set()
    lolurl = 'http://www.zhihu.com/'
    renurl = 'http://www.renren.com/'
    queue.append(initurl)

    while queue:

        url = queue.popleft()

        visited |= {url}
        # print('正在抓取-------->' + url)

        try:
            data = urllib.request.urlopen(url, timeout = 2).read()
            # data = ungzip(data)
            #data = data.decode()
            data = data.decode('GBK')
        except:
            continue
        #print(data)

        picre = re.compile('src=\"(.+?\\.jpg)\"')
        linkre = re.compile('href=\"(.+?)\"')
        picvisited = set()
        for x in picre.findall(data):
            if x not in picvisited:
                url = x
                if 'http' not in url:
                        url = 'http:' + url
                print(url)
                hf = url.split('/')
                name = hf.pop()
                # print(name)
                picvisited.add(x)
                try:
                    urllib.request.urlretrieve(url, 'D:\pic\%s' % name)
                except:
                    continue

        for x in linkre.findall(data):
            if x not in visited:
                if 'http' not in x:
                    x = 'http:' + x
                queue.append(x)
                # print(x)

    #print(data)
