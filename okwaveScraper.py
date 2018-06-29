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
import bs4
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
            #print(ref)
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
    qID = aQuestionURL.replace("https://okwave.jp//qa/","")
    qID = qID.replace(".html","")
#     print(q_soup.body)
    # Questionを取得
    questionList = q_soup.find('div', attrs={'class': 'q_desc'})
#     questionList = questionDiv.find_all('p')
#     print(questionList)
    total_q_text = ''
    for i,q in enumerate(questionList):
        text = q
        if(len(text)!=0):
            total_q_text+=text
    print("----------Question----------")
    print(total_q_text)
    # Answerを取得
    answerList = q_soup.find_all('div', attrs={'class': 'a_textarea'})
    total_a_text_list = []
    for i,answer in enumerate(answerList):
        total_a_text = ''
        for j,a in enumerate(answer):
            text = a
            if(len(text)!=0 and type(text)!=bs4.element.Tag):
                total_a_text+=text
#         print(total_a_text)
        total_a_text_list.append(total_a_text)
    print("----------Answer----------")
    print(total_a_text_list)
    #スリープ
    time.sleep(1)
    if(len(total_q_text)>0 and len(total_a_text_list)>0):
        return(total_q_text,total_a_text_list,qID)
    else:
        return(None,None,None)
#save_dir = os.getcwd()
save_dir = '/home/itolab/virtualenvs/sharedData/Q&A/okwave'
def saveContentS(aQuestion_URL_list):
    for i,qURL in enumerate(aQuestion_URL_list):
        print(qURL)
        qText,aTextList,qID = getContent(qURL)
        if(qText!=None and aTextList!=None):
            #print(save_dir+'/Question/'+'Q'+qID+'.txt')
            pathQ = save_dir+"/Question/"+"Q"+qID+".txt"
            fQ = open(pathQ,'w')
            fQ.write(qText)
            fQ.close()
            pathA = save_dir+"/Answer/"+"A"+qID+".txt"
            fA = open(pathA,'w')
            fA.writelines(aTextList)
            fA.close()
    return
saveContentS(question_url)
#
import datetime
def scraping():
    #starttime = time.ctime()
    starttime = datetime.datetime.now() # 現在の日時を取得
    while((datetime.datetime.now()-starttime).seconds<600):
        # アクセスするURL
        url = "https://okwave.jp/"
        question_url = getQustionURL(url)
        save_dir = '/home/itolab/virtualenvs/sharedData/Q&A/okwave'
        saveContentS(question_url)
        time.sleep(60)
    return
scraping()