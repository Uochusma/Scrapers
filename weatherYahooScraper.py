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
#===================================================================================================
starttime = time.ctime()
phase = 1
#===================================================================================================
print("phase ",phase," start", "=" * 60, time.ctime())
def getQustionURL(aTopURL):
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html)
    #print(soup.body)
    result_list = soup.find('div', attrs={'class': 'r_list'})
    #print(result_list)
    result_list_content = result_list.ul.find_all('li', attrs={'class': 'clearfix'})
    #aref_list = soup.body.findAll('div')
    #total = len(soup.body.findAll('a'))
    q_url_list = []
    for i,result in enumerate(result_list_content):
        print(i)
        #print(result)
        text = result.find('div', attrs={'class': 'result'})
        print(text)
        q_url = text.ul.li.h2.a.attrs['href']
        q_url_list.append(q_url)
    return(q_url_list)

# アクセスするURL
url = "https://oshiete.goo.ne.jp/articles/qa/"
question_url = getQustionURL(url)
#print(question_url)
print("phase ",phase," done", "=" * 60, time.ctime())
phase+=1