import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def Making_Rest_Call():
    response = requests.get("https://www.barchart.com/stocks/most-active/daily-volume-leaders")
    print(response.json())
Making_Rest_Call()

#def Send_SMS():
#def Receive_SMS():