import requests
from bs4 import BeautifulSoup

def Making_Rest_Call():
    #response = requests.get("https://www.barchart.com/stocks/most-active/daily-volume-leaders")
    response = requests.get("https://www.google.com/finance/quote/NIO:NYSE")
    soup = BeautifulSoup(response.content,'html.parser')
    print(soup)
Making_Rest_Call()

#def Send_SMS():
#def Receive_SMS():