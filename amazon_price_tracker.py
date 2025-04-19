import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com/dp/B08N5WRWNW'  # Replace with product URL
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}

THRESHOLD = 200.00  # Alert if price is below this
EMAIL = 'your_email@gmail.com'
PASSWORD = 'your_app_password'
TO_EMAIL = 'receiver_email@gmail.com'

def check_price():
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='productTitle').get_text().strip()
    price_str = soup.find('span', {'class': 'a-price-whole'}).get_text().replace(',', '')
    price = float(price_str)

    if price < THRESHOLD:
        send_email(title, price)

def send_email(title, price):
    subject = f'Price Drop Alert: {title} is now ${price}'
    body = f'Check the Amazon link: {URL}'
    msg = f'Subject: {subject}\n\n{body}'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    server.sendmail(EMAIL, TO_EMAIL, msg)
    server.quit()

if __name__ == '__main__':
    check_price()
