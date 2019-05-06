import urllib.request
import random
from bs4 import BeautifulSoup
import requests
import json
import time
from labelFilter import html_filter
from outToTxt import outTxt

def searchContentById(questionId):

    #  虚拟header头部
    headers = [{
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'},
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'},
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'},
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'},
        {
        }]
    header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

    url1 = "https://www.zhihu.com/question/"+str(questionId);

    # 随机header编码，据说防封
    head_No = random.randint(0, len(headers) - 1)
    res = urllib.request.urlopen(url1)
    html = res.read().decode('utf-8')
    soup=BeautifulSoup(html,'html.parser')
    body = soup.html.body
    question_content=""
    richText=soup.select('.QuestionRichText .RichText')
    if len(richText)==0:
        return ""
    question_content=richText[0].text
    # print(html_filter(question_content))
    print(question_content)
    return  question_content

searchContentById(63849806)