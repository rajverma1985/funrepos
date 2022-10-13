import random
from datetime import datetime
import pandas as pd
import smtplib
import os
from dotenv import load_dotenv

# load all env variables
load_dotenv()

df = pd.read_csv('birthdays.csv')
birth_dates = (datetime.now().day, datetime.now().month)

birthday = {(data.day, data.month,): data for (index, data) in df.iterrows()}


def send_email(birth_name, mail):
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
        # secure the connection(packets sent using ttls)
        connection.ehlo()
        connection.login(user=os.getenv('user'), password=os.getenv('password'))
        connection.sendmail(
            from_addr=os.getenv('my_email'),
            to_addrs=os.getenv('my_email'),
            msg=f"Subject: Happy birthday to you {birth_name} \n\n {mail}")


if birth_dates in birthday:
    person = birthday[birth_dates]
    # get the name and replace that persons name with a random letter
    name = person['name']
    letter_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(letter_path) as letter:
        send_letter = letter.read().replace("[NAME]", name)
    send_email(name, send_letter)

