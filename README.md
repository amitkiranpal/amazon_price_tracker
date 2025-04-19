## Amazon Price Tracker Bot
Tracks the price of a product on Amazon and sends an email when the price drops below a set threshold.

## Tech Stack
- Python
- BeautifulSoup
- smtplib

## Features
- Scrapes live product prices
- Sends email alerts when a threshold is reached
- Easy to automate via cron jobs

## Usage
1. Update the product URL and your email credentials.
2. Run `python amazon_price_tracker.py`
3. To run daily, set up a cron job or Windows Task Scheduler.
