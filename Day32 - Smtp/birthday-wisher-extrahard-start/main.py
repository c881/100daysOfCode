##################### Extra Hard Starting Project ######################
import smtplib, ssl
import datetime as dt
import random as rd
import pandas as pd

def send_mail(message1):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "kobygs78@gmail.com"
    password = input("Type your password and press enter: ")
    message = f"Subject: Happy Birthday \n\n {message1}"
    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    # Like with files, using with to auto close the connection
    with smtplib.SMTP(smtp_server, port) as server:
        try:
            # server = smtplib.SMTP(smtp_server,port)
            server.starttls(context=context)  # Secure the connection
            server.login(sender_email, password)
            server.sendmail(from_addr=sender_email,
                            to_addrs="jacov.g@gmail.com",
                            msg=message)
        except Exception as e:
            # Print any error messages to stdout
            print(e)

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

today = dt.datetime.now()

birthdate_data = pd.read_csv("birthdays.csv")
birth_dict = {row[1][0]: {"email": row[1][1],
                         "month": row[1][3],
                         "day":row[1][4]} for row in birthdate_data.iterrows()}
for item in birth_dict.items():
    # print(item[1]['email'])
    if today.month == item[1]["month"] and today.day == item[1]["day"]:
        with open(f"letter_templates/letter_{rd.randint(1, 4)}.txt") as letter:
            letter_cont = letter.read()
        letter_cont = letter_cont.replace("[NAME]", item[0])
        send_mail(letter_cont)





