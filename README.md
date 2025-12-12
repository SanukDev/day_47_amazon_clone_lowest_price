Amazon Price Tracker


This project is a simple price-tracking script that monitors a product on Amazon and sends an email alert when the price drops below a defined target value.
It uses BeautifulSoup to scrape the product’s price, compares it with your target, and automatically sends an email using Gmail’s SMTP server.


Features


Scrapes product title and price from Amazon
Compares the price to a TARGET value
Sends an email alert when the price drops
Uses BeautifulSoup, requests, and Python’s built-in SMTP features
Easy to customize for any product URL


How It Works


The script fetches the product page HTML using requests.
BeautifulSoup parses the HTML and extracts:
Product title
Product price
The price is formatted and converted to a numeric value.
If the price is below your TARGET, the script:
Logs in to Gmail using SMTP
Sends an alert email to your inbox
