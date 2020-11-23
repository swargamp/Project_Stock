import requests
from bs4 import BeautifulSoup

def Making_Rest_Call():
    #response = requests.get("https://www.barchart.com/stocks/most-active/daily-volume-leaders")
    #response = requests.get("https://www.google.com/finance/quote/NIO:NYSE")
    response = requests.get("https://gis.conservation.ca.gov/server/rest/services/CGS_Earthquake_Hazard_Zones/SHP_Liquefaction_Zones/MapServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json")
    soup = BeautifulSoup(response.content,'html.parser')
    print(soup)
Making_Rest_Call()

#def Send_SMS():
#def Receive_SMS():