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
    q_url_list = []
    all_q_list = soup.find_all('div', attrs={'class': 'questionList'})
    for q_list in all_q_list:
        q_list_content = q_list.find_all('li')
        for i, ref in enumerate(q_list_content):
            # print(ref)
            q_url = ref.find('a').attrs['href']
            q_url_list.append(q_url)
    return(q_url_list)


# アクセスするURL
url = "https://chiebukuro.yahoo.co.jp/"
question_url = getQustionURL(url)
# print(question_url)
print("phase ", phase, " done", "=" * 60, time.ctime())
phase += 1
# ===================================================================================================
print("phase ", phase, " start", "=" * 60, time.ctime())


def getContent(aQuestionURL):
    print('='*50)
    print("*Question*")
    print(aQuestionURL)
    q_html = urllib.request.urlopen(aQuestionURL)
    q_soup = BeautifulSoup(q_html)
    # print(q_soup.body)
    #questionDiv = q_soup.find('div', attrs={'class': 'ptsQes'})
    #questionDiv1 = q_soup.body.find_all('div', attrs={'class': 'mdPstd mdPstdQstn sttsRslvd  clrfx'})
    questionDiv1 = q_soup.body.find_all(
        'div', attrs={'class': re.compile('mdPstdQstn')})[0]
    # print(questionDiv1)
    questionDiv2 = questionDiv1.find('div', attrs={'class': 'ptsQes'})
    questionList = questionDiv2.find_all('p')
    # print(questionList)
    total_text = ''
    for i, q in enumerate(questionList):
        print(i)
        # print('*'*30)
        print('text=', q.text)
        """
        if(q.p!=None):
            print('p=',q.p.text)
        if(q.br!=None):
            print('br=',q.br.text)
        if(q.span!=None):
            print('span=',q.span.text)
        #"""
        # q.find('br').extract()
        text = q.text
        # print('text_replaced1=',text)
        #text = text.replace('\s','')
        text = re.sub(r'\s', "", text)
        # print('text_replaced2=',text)
        #text = text.replace(r'\s','')
        text = text.replace('   ', '')
        # print('text_replaced3=',text)
        text = text.replace(r'\n', '')
        text = re.sub(r'\n', "", text)
        # print('text_replaced4=',text)
        text = re.sub(r'\t', "", text)
        # print('text_replaced5=',text)
        text = re.sub(r'\v', "", text)
        # print('text_replaced6=',text)
        #text = text.replace(r'^違反報告$','')
        text = re.sub(r'^違反報告$', "", text)
        # print('text_replaced7=',text)
        print('text_replaced=', text)
        # print('*'*30)
        # print('len=',len(text))
        if(len(text) != 0):
            total_text += text
    qID = aQuestionURL.replace(
        'https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/', '')
    print(qID)
    print('total=', total_text)
    print("*Answer*")
    answer_text = ''
    answerDiv1 = q_soup.body.find('div', attrs={'id':  re.compile('ba')})
    if(answerDiv1 != None):
        answerDiv2 = answerDiv1.find('div', attrs={'class': 'ptsQes'})
        answerList = answerDiv2.find_all('p')
        for i, q in enumerate(answerList):
            # print('text=',q.text)
            text = q.text
            text = re.sub(r'\s', "", text)
            text = text.replace('   ', '')
            text = text.replace(r'\n', '')
            text = re.sub(r'\n', "", text)
            text = re.sub(r'\t', "", text)
            text = re.sub(r'\v', "", text)
            text = re.sub(r'^違反報告$', "", text)
            # print('text_replaced=',text)
            if(len(text) != 0):
                answer_text += text
    if(len(answer_text) != 0):
        print('answer=', answer_text)
    else:
        print("No Answer")
    # スリープ
    time.sleep(1)
    if(len(total_text) > 0 and len(answer_text) > 0):
        return(total_text, answer_text, qID)
    else:
        return(None, None, None)


#save_dir = os.getcwd()
save_dir = '/home/itolab/virtualenvs/sharedData/Q&A/yahoo'
#save_dir = '/home/itolab/notebooks/yoshino/Data/Q&A/yahoo'


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
        url = "https://okwave.jp/"
        question_url = getQustionURL(url)
        save_dir = '/home/itolab/virtualenvs/sharedData/Q&A/okwave'
        saveContentS(question_url)
        time.sleep(60)
    return


scraping()
