from datetime import datetime
import pandas as pd

# 1. Update the birthdays.csv -- Done!

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


df = pd.read_csv('birthdays.csv')
birth_dates = (datetime.now().day, datetime.now().month)

birthday = {(data.day, data.month, ): data for (index, data) in df.iterrows()}


if birth_dates in birthday:
    person = birthday[birth_dates]
    # get the name and replace that persons anme with a random letter
    name = person['name']










