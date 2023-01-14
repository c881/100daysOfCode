import datetime as dt
import random
import smtplib, ssl


smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "kobygs78@gmail.com"

dict_file = {}
idx = 0
with open("quotes.txt", "r") as file:
    for line in file:
        dict_file[idx] = line.replace('"', '').strip().split(" - ")
        idx += 1
# for key in dict_file.keys():
#     print(dict_file[key])
password = input("Type your password and press enter: ")
message = dict_file[random.randint(0,idx)]
# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
with smtplib.SMTP(smtp_server,port) as server:
    try:
        server.starttls(context=context) # Secure the connection
        server.login(sender_email, password)
        server.sendmail(from_addr=sender_email, to_addrs="jacov.g@gmail.com", msg=message)
    except Exception as e:
        # Print any error messages to stdout
        print(e)
