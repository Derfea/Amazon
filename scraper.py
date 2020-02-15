import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.de/Sony-Digitalkamera-Touch-Display-Vollformatsensor-Kartenslots/dp/B07B4L1PQ8/ref=sr_1_3?keywords=sony+a7&qid=1561393494&s=gateway&sr=8-3'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}


def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if(converted_price < 1.700):
        send_mail()

    print(title.strip())
    print(converted_price)

    if (converted_price > 1.700):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('xboxchampion20@gmail.com', 'qddxylslepdlyaul')

    subject = 'Price Fell Down!'
    body = 'Check the amazon link: https://www.amazon.de/Sony-Digitalkamera-Touch-Display-Vollformatsensor-Kartenslots/dp/B07B4L1PQ8/ref=sr_1_3?keywords=sony+a7&qid=1561393494&s=gateway&sr=8-3'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'xboxchampion20@gmail.com',
        'chikamso.kanu@outlook.com',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()


while(True):
    check_price()
    time.sleep(60 * 60)