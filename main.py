import requests
from bs4 import BeautifulSoup
import smtplib
import time

desired_price = 28000.0
URL = 'https://www.daraz.com.np/products/xiaomi-poco-f1-6-gb-ram-64-gb-rom-618-inches-screen-blue-i100848277-s1021366380.html?spm=a2a0e.searchlistcategory.list.16.5f79fae2GbbARz&search=1' 
fromAddr = 'iamashishsubedi@gmail.com'
toAddr = 'ashishsubedi10@gmail.com'
password = 'tfdtzqdnhfibznmi'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
}

def check_price():
    request = requests.get(URL, headers=header)
    soup = BeautifulSoup(request.content , 'html.parser')

    price = soup.find(class_ = ' pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl').get_text()[3:].strip()
    price = float(price.replace(',',''))
    print(price)
    if(price< desired_price):
        send_mail()
        

def send_mail():
    server =  smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(fromAddr,password)
    msgSubject = "Oi, Price Dropped "
    msgBody = f"Check the link: {URL}"
    msg = f"Subject: {msgSubject}\n\n {msgBody}"
    server.sendmail(fromAddr,toAddr,msg)
    print("Email Sent")
    server.quit()

while(True):
    print("Checking for Price...")
    check_price()
    print("Sleeping for 5 hours now...")
    time.sleep(60*60*5) #Checks every 5 hours
