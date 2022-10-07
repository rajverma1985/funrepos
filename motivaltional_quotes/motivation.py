import datetime
import smtplib

now = datetime.datetime.now()

quote_list = []
with open('quotes.md', 'r') as quotes:
    quote_list.append(quotes.readline())

print(quote_list[0])