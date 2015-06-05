__author__ = 'Ran'
import urllib
import urllib.request
import urllib.parse
import http.cookiejar
import re

loginurl  = 'http://www.renren.com/PLogin.do'

class Login(object):

    def __init__(self):
        self.name = ''
        self.password = ''

        self.cj = http.cookiejar.CookieJar()
        self.pro = urllib.request.HTTPCookieProcessor(self.cj)
        self.opener = urllib.request.build_opener(self.pro)

        # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'}
        # self.opener.addheaders = headers

    def setLoginInfo(self,name, password):
        self.name = name
        self.password = password
        # self.domain = domain

    def login(self):

        loginparam = {
            # 'domain': self.domain,
            'email': self.name,
            'password': self.password
        }
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'}

        # req = urllib.request.Request(loginurl, urllib.parse.urlencode(loginparam).encode(), headers = headers)
        # response = urllib.request.urlopen(req)
        # self.op = self.opener.open(req)
        # data = response.read()
        # data = data.decode()
        # print(data)

        loginparam = urllib.parse.urlencode(loginparam).encode()
        op = self.opener.open(loginurl, loginparam)
        self.data = op.read()
        self.data = self.data.decode()
        print(self.data)


    def GetPic(self):

        visited = set()
        picre = re.compile('src=\"(.+?\\.jpg)\"')

        for x in picre.findall(self.data):
            if x not in visited:
                url = x
                if 'http' not in url:
                    url = 'http:' + url
                visited |= {url}
                hf = url.split('/')
                name = hf.pop()
                try:
                    urllib.request.urlretrieve(url, 'd:\pic\%s' % name)
                except:
                    continue


userlogin = Login()
name = 'This is your email'
password = 'This is you pwd'
# domain = logindomain
userlogin.setLoginInfo(name, password)
userlogin.login()
userlogin.GetPic()


