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
    q_url_list = []
    all_q_list = soup.find_all('ul', attrs={'class': 'okw_lt newest_all'})
    for q_list in all_q_list:
        q_list_content = q_list.find_all('li')
        for i,ref in enumerate(q_list_content):
            print(ref)
            q_url = url + ref.find('a').attrs['href']
            q_url_list.append(q_url)
    return(q_url_list)

# アクセスするURL
url = "https://okwave.jp/"
question_url = getQustionURL(url)
print(question_url)
print("phase ",phase," done", "=" * 60, time.ctime())
phase+=1
#===================================================================================================
print("phase ",phase," start", "=" * 60, time.ctime())
def getContent(aQuestionURL):
    q_html = urllib.request.urlopen(aQuestionURL)
    q_soup = BeautifulSoup(q_html)
#     print(q_soup.body)
    # Questionを取得
    questionList = q_soup.find('div', attrs={'class': 'q_desc'})
#     questionList = questionDiv.find_all('p')
#     print(questionList)
    total_q_text = ''
    for i,q in enumerate(questionList):
#         print(i)
#         print(q)
#         text = q.text
#         text = text.replace(r'\s','')
#         text = text.replace(r'\n','')
#         text = text.replace(r'違反報告','')
        text = q
#         print(text)
#         print(type(text))
#         print(isinstance(text,))
#         print('len=',len(text))
        if(len(text)!=0):
            total_q_text+=text
#         print(total_text)
    print("----------Question----------")
    print(total_q_text)
    # Answerを取得
    answerList = q_soup.find_all('div', attrs={'class': 'a_textarea'})
#     print(answerList)
    total_a_text_list = []
    for i,answer in enumerate(answerList):
#         print(i)
#         print(answer
        total_a_text = ''
        for j,a in enumerate(answer):
            text = a
            if(len(text)!=0):
                total_a_text+=text
#         print(total_a_text)
        total_a_text_list.append(total_a_text)
    
#     for i,a in enumerate(answerList):
#         print(i)
#         print(a)
#         text = a
#         if(len(text)!=0):
#             total_a_text+=text
    print("----------Answer----------")
    print(total_a_text_list)
    #スリープ
    time.sleep(1)
    return
save_dir = os.getcwd()
for i,qURL in enumerate(question_url):
    print(qURL)
#     qURL = 'https://okwave.jp/qa/q9505931.html'
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