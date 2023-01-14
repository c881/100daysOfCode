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
            server.starttls(context=context)  # Secure the connection
            server.login(sender_email, password)
            server.sendmail(from_addr=sender_email,
                            to_addrs="jacov.g@gmail.com",
                            msg=message)
        except Exception as e:
            # Print any error messages to stdout
            print(e)


today = dt.datetime.now()
# today_mmdd = (today.month, today.day)
birthdate_data = pd.read_csv("birthdays.csv")
birth_dict = birthdate_data.to_dict(orient="records")
# birth_dict = {index: row for (index, row) in birthdate_data.iterrows()}
# print(birth_dict2)
# print(birth_dict)
for row in birth_dict:
    if today.month == row["month"] and today.day == row["day"]:
        with open(f"letter_templates/letter_{rd.randint(1, 4)}.txt") as letter:
            letter_cont = letter.read()
            letter_cont = letter_cont.replace("[NAME]", row["name"])
            print(f"got {row['name']}")
            send_mail(letter_cont)





