import datetime as dt
import random
import smtplib, ssl
WEEKDAYS = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday',
            5: 'Saturday', 6: 'Sunday'}


def send_mail(quote=None):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "kobygs78@gmail.com"
    password = input("Type your password and press enter: ")
    message = f"Subject: Motivation Quote \n\n {quote[0]}\n{quote[1]}"
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


dict_file = {}
idx = 0
with open("quotes.txt", "r") as file:
    for line in file:
        dict_file[idx] = line.replace('"', '').strip().split(" - ")
        idx += 1


if WEEKDAYS[dt.datetime.weekday(dt.datetime.now())] == 'Wednesday':
    send_mail(dict_file[random.randint(0, idx)])
