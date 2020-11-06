import requests


def Making_Rest_Call():
    response = requests.get("https://www.barchart.com/stocks/most-active/daily-volume-leaders")
    print(response.json())
Making_Rest_Call()

#def Send_SMS():
#def Receive_SMS():


