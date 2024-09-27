import re
import urllib.request


def craw(url):
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    pat1 = '<ul class="content">.+?<div class="pageindex">'
    result1 = re.compile(pat1).findall(html1)
    result1 = result1[0]
    pat2 = '<img src="https://(.+?\.jpg)".+?alt="(.+?)"'
    infos = re.compile(pat2).findall(result1)
    x = 1

    


