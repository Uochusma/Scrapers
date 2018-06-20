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
#===================================================================================================
print("phase ",phase," start", "=" * 60, time.ctime())
def getContent(aQuestionURL):
    q_html = urllib.request.urlopen(aQuestionURL)
    q_soup = BeautifulSoup(q_html)
    print(q_soup.body)
    questionDiv = q_soup.find('div',attrs={'class': 'ptsQes'})
    questionList = questionDiv.find_all('p')
    for i,q in enumerate(questionList):
        print(i)
        #print(q)
        print(q.text)
    #スリープ
    time.sleep(1)
    return
save_dir = os.getcwd()
for i,qURL in enumerate(question_url):
    print(qURL)
    getContent(qURL)
    """
    if(ref.attrs['href'].find('.log')==-1):
        continue
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