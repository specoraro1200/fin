from urllib import request
from urllib.request import Request, urlopen
# import requests
import csv
from bs4 import BeautifulSoup

# requestUrl = Request("https://finviz.com/quote.ashx?t=MSGM&p=d",headers={'User-Agent':'Mozilla/5.0'})
# webpage = urlopen(requestUrl).read()
# print(webpage)
# soup = BeautifulSoup(url.content,'html.parser')
# print(soup)
keyPhrases = ['nasdaq listing']
with open('list.csv', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        url = ("https://finviz.com/quote.ashx?t={}&p=d").format(row[0])
        test = ("https://finviz.com/quote.ashx?t=VINO&p=d")
        try:
            requestUrl = Request(url,headers={'User-Agent':'Mozilla/5.0'})
            webpage = urlopen(requestUrl).read()
            soup = BeautifulSoup(webpage,'html.parser').find_all("table", {"id": "news-table"})
            store = soup[0].find('tr').find('a').encode_contents().decode().lower()
            if(store.__contains__(keyPhrases[0])):
                print(store)
                print("true")

        # print(soup[0].find('tr').find("div",{"class":"news-link-left"}).find('a').encode_contents())
        except:
            a = 1
        
        # print(webpage)
