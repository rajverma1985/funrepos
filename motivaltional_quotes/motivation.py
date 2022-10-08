import datetime
import os
import random
import smtplib
import calendar

from dotenv import load_dotenv

# load all env variables
load_dotenv()

now = datetime.datetime.today()
day_of_week = calendar.day_name[now.weekday()]


def quote():
    with open('quotes.md', 'r') as quotes:
        quote_list = quotes.readlines()
        return random.choice(quote_list)


message = f"""From: Raj Verma <noreply@rajverma.com>
To: {os.getenv('my_email')}
Subject: QUOTE of the day for {day_of_week}

{quote()}
Have  Wonderful Day ahead!
"""


def send_email():
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
        # secure the connection(packets sent using ttls)
        connection.ehlo()
        connection.login(user=os.getenv('user'), password=os.getenv('password'))
        connection.sendmail(
            from_addr=os.getenv('my_email'),
            to_addrs=os.getenv('my_email'),
            msg=message)


if now.weekday():
    send_email()

# ToDO: identify day and send quotes every day:
