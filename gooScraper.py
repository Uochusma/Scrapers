# -*- coding: utf-8 -*-
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

# ===================================================================================================
starttime = time.ctime()
phase = 1
# ===================================================================================================
print("phase ", phase, " start", "=" * 60, time.ctime())


def getQustionURL(aTopURL):
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html)
    # print(soup.body)
    result_list = soup.find('div', attrs={'class': 'r_list'})
    # print(result_list)
    result_list_content = result_list.ul.find_all(
        'li', attrs={'class': 'clearfix'})
    #aref_list = soup.body.findAll('div')
    #total = len(soup.body.findAll('a'))
    q_url_list = []
    for i, result in enumerate(result_list_content):
        print(i)
        # print(result)
        text = result.find('div', attrs={'class': 'result'})
        print(text)
        q_url = text.ul.li.h2.a.attrs['href']
        q_url_list.append(q_url)
    return(q_url_list)


# アクセスするURL
url = "https://oshiete.goo.ne.jp/articles/qa/"
question_url = getQustionURL(url)
print(question_url)
print("phase ", phase, " done", "=" * 60, time.ctime())

phase += 1
# ===================================================================================================
print("phase ", phase, " start", "=" * 60, time.ctime())


def getContent(aQuestionURL):
    q_html = urllib.request.urlopen('https:'+aQuestionURL)
    q_soup = BeautifulSoup(q_html)
    qID = aQuestionURL.replace('https://oshiete.goo.ne.jp/qa/', '')
    qID = qID.replace('.html', '')
    print("q_soup.body")
#     print(q_soup.body)
#     questionDiv = q_soup.find('div',attrs={'class': 'ptsQes'})
#     questionList = questionDiv.find_all('p')

    question_list = q_soup.body.find('p', attrs={'class': 'q_text'})
#     print(question_list)
    question_text = ''
    for i, q in enumerate(question_list):
        #         print('='*60)
        #         print(i)
        #         print(q)
        q_text = str(q)
#         print(q_text)
#         if q_text == '<br/>':
#             q_text = ''
        q_text = re.sub(r'<br/>', '', q_text)
#         q_text = q_text.replace('\n', '')
#         q_text = re.sub(r'\n', '', q_text)
        q_text = re.sub(r'\s', '', q_text)
#         q_text = re.sub(r'\S', '', q_text)
#         print(q_text)
        if len(q_text) != 0:
            question_text += q_text
#         print(question_text)
    print('*****Question*****')
    print(question_text)
    # スリープ
    time.sleep(1)

    answer_list = q_soup.body.find_all('div', attrs={'class': 'a_text'})
#     print(answer_list)
    answer_text_list = []
    for i, a in enumerate(answer_list):
        #         print('='*60)
        #         print(i)
        #         print(a)
        a_text = str(a)
#         for j, a_line in enumerate(a_text)
        a_text = re.sub(r'<div.*>', '', a_text)
        a_text = re.sub(r'</div>', '', a_text)
        a_text = re.sub(r'<h2>', '', a_text)
        a_text = re.sub(r'</h2>', '', a_text)
        a_text = re.sub(r'<br/>', '', a_text)
        a_text = re.sub(r'\s', '', a_text)
        print('*****Answer*****')
        print(a_text)
        answer_text_list.append(a_text)
    time.sleep(1)
    if(len(question_text) > 0 and len(answer_text_list) > 0):
        return(question_text, answer_text_list, qID)
    else:
        return(None, None, None)


#save_dir = os.getcwd()
save_dir = '/home/itolab/virtualenvs/sharedData/Q&A/goo'


def saveContentS(aQuestion_URL_list):
    for i, qURL in enumerate(aQuestion_URL_list):
        print(qURL)
        qText, aTextList, qID = getContent(qURL)
        if(qText != None and aTextList != None):
            # print(save_dir+'/Question/'+'Q'+qID+'.txt')
            pathQ = save_dir+"/Question/"+"Q"+qID+".txt"
            fQ = open(pathQ, 'w')
            fQ.write(qText)
            fQ.close()
            pathA = save_dir+"/Answer/"+"A"+qID+".txt"
            fA = open(pathA, 'w')
            fA.writelines(aTextList)
            fA.close()
    return


saveContentS(question_url)
#
import datetime


def scraping():
    #starttime = time.ctime()
    starttime = datetime.datetime.now()  # 現在の日時を取得
    while((datetime.datetime.now()-starttime).seconds < 600):
        # アクセスするURL
        # url = "https://okwave.jp/"
        url = "https://oshiete.goo.ne.jp/articles/qa/"
        question_url = getQustionURL(url)
        save_dir = '/home/itolab/virtualenvs/sharedData/Q&A/goo'
        saveContentS(question_url)
        time.sleep(60)
    return


scraping()
