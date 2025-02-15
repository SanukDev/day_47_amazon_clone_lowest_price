from bs4 import BeautifulSoup
import requests
import smtplib
from email.message import EmailMessage

URL = "https://www.amazon.com.br/PlayStation-DualSense-Controle-sem-fio-dp-B0CQKKHT5J/dp/B0CQKKHT5J/ref=dp_ob_title_vg"
URL2 = "https://appbrewery.github.io/instant_pot/"
TARGET = 400
response = requests.get(URL2)
data = response.text

soup = BeautifulSoup(data, "html.parser")

title = soup.find_all(name="span", id="productTitle")[0].getText()

#price = soup.find_all(name="span", class_="a-price-whole")[0].getText()
price = soup.find_all(name="span", class_="aok-offscreen")[0].getText()

price2 = price.split("$")
price_final = float(price2[1])
print(price_final)
print(title)


# prepare the email
msg = EmailMessage()
msg.set_content(f"{title} is now {price}")

# Set the email subject and addresses
msg['Subject'] = "To buy now. Lowest Price"
msg['From'] = "samukakaroto123@gmail.com"
msg['To'] = "samukakaroto123@gmail.com"
if price_final < TARGET:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user="samukakaroto123@gmail.com", password="wplk zuyj gapn ntrs")
        connection.send_message(msg)