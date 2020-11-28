import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.flipkart.com/realme-classic-watch/p/itm46dd62c0398fc?pid=SMWFQZ8NXG6YBM8E&lid=LSTSMWFQZ8NXG6YBM8EC4BB7G&marketplace=FLIPKART&srno=b_1_3&otracker=hp_reco_Top%2BSelection_4_13.dealCard.OMU_cid%3AS_F_N_ajy__bs___NONE_ALL%3Bnid%3Aajy_%3Bet%3AS%3Beid%3Aajy_%3Bmp%3AF%3Bct%3Ab%3B_8&otracker1=hp_reco_WHITELISTED_personalisedRecommendation%2FC6_Top%2BSelection_DESKTOP_HORIZONTAL_dealCard_cc_4_NA_view-all_8&fm=personalisedRecommendation%2FC6&iid=6038143a-b80b-48e3-a800-222467b87d48.SMWFQZ8NXG6YBM8E.SEARCH&ppt=browse&ppn=browse&ssid=vxdowksvy80000001606546038957"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}

def send_mail(title):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('mail.address01@gmail.com', 'xxxxxxxxxxx')
    subject = '[SBOT]Notification: Price down for your desiered product.'
    body = "Check the link, " + URL
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'mail.address01@gmail.com',
        'mail.address02@gmail.com',
        msg
    )

    print('Message send')
    server.quit()

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find("span", {"class":"B_NuCI"}).get_text().strip()
    price = soup.find("div", {"class":"_30jeq3 _16Jk6d"}).get_text().strip()[1:]

    _price = ''
    for i in price:
        if i != ',':
            _price += i
    _price = int(_price)
    print(_price)
    if _price < 2500:
        send_mail(title)

check_price()