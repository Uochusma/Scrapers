## -*- coding: utf-8 -*-
import os
from __future__ import unicode_literals
from __future__ import print_function
import json
import codecs
import re
import urllib3
import urllib.request
import requests
import time
from bs4 import BeautifulSoup

# アクセスするURL
url = "https://okwave.jp/"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html)
#print(soup.body)
save_dir = os.getcwd()
topicsindex = soup.find('ul', attrs={'class': 'okw_lt newest_all'})
topics = topicsindex.find_all('li')
aref_list = soup.body.findAll('div')
total = len(soup.body.findAll('a'))
for i,ref in enumerate(topics):
    
    print(ref)
    print(ref.find('a'))
    print(ref.find('a').attrs['href'])
    """
    if(ref.attrs['href'].find('.log')==-1):
        continue
    #スリープ
    time.sleep(2)
    #print(ref)
    #print("%s's url is %s" % (ref.text, ref.attrs['href']))
    file_name = ref.attrs['href']
    print(i,'/',total,':',file_name)
    download_url = url+file_name
    #print(download_url)
    r = requests.get(download_url)
    #print('content=',r.content)
    #print('content2=',r.content.decode('utf-8'))
    text = r.content.decode('utf-8')
    # ファイルの保存
    if r.status_code == 200:
        #f = open(save_dir+'/'+file_name+'.txt', 'w','utf-8')
        f = codecs.open(save_dir+'/train2/'+file_name+'.txt', 'w', 'utf-8')
        f.write(text)
        f.close()
    #"""