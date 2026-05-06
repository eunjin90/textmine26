import os
import sys
import urllib.request
import json

def crawl_naver_news(url, start=0, display=10):
    client_id = "bq36QTcF8F2VxKKQnNP1"
    client_secret = "LNvYgryipi"
    url += f'&start={start}&display={display}'
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        # news_data = json.loads(response_body.decode('utf-8'))['items']
        json_str = response_body.decode('utf-8')
        py_data = json.loads(json_str)
        news_data = py_data['items']

        # print(news_data)
        return news_data, None
    else:
        # print("Error Code:" + rescode)
        return None, rescode
    

def crawl_naver_news_all(keyword):
    encText = urllib.parse.quote(keyword)

    start = 1
    display = 10

    url = "https://openapi.naver.com/v1/search/news?query=" + encText # JSON 결과

    corpus = []
    while start <= 100:
        crawl_news, status = crawl_naver_news(url, start, display)
        if crawl_news:
            corpus += crawl_news
            start += display
        else:
            print("Error Code:" + status)
            break
    return corpus
    