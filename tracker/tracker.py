import mod
import csv
import pandas as pd
import numpy as np
"""from myanimelist.session import Session"""

mod.write_browserhistory_txt()

website = str(input("Enter Website to Search: "))

### Modifying previous CSV File
header = "Visited Websites"
bhistory = pd.read_csv('chrome_history.csv', header= None)

"""print (bhistory[:10][0])"""

x = bhistory[:10][0]
df = pd.DataFrame(x)
df.to_csv('chrome_history.csv', header=False, sep="|")

## Check if website visited
def check():                                                                         
    with open('chrome_history.csv', 'rt') as csv_file:
        for rows in csv_file:
            if website in rows[0:25]:
                print(rows[2:], "It's in line", int(rows[:1]) + 1)
            else:
                print("...")
    return
check()

## MAL Authentication

"""mal_username = str(input("Enter Username: "))
mal_password = str(input("Enter Password: "))

session = myanimelist.session.Session(username="mal_username", password="mal_password")
session.login()"""
