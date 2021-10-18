# import smtplib
#
# my_email = "kobygs78@gmail.com"
# my_password = input("Please type in your password: ")
#
#
# connection = smtplib.SMTP("smtp.google.com", port=587)
# connection.starttls()
# connection.login(user=my_email,password=my_password)
# connection.sendmail(from_addr=my_email, to_addrs="jacov.g@gmail.com", msg="hello world")
# connection.close()

import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "kobygs78@gmail.com"
password = input("Type your password and press enter: ")
message = "Subject: Hi there \n\n Have a great day."
# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
with smtplib.SMTP(smtp_server,port) as server:
    try:
    # server = smtplib.SMTP(smtp_server,port)
    # server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
    # server.ehlo() # Can be omitted
        server.login(sender_email, password)
        server.sendmail(from_addr=sender_email, to_addrs="jacov.g@gmail.com", msg=message)
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    # finally:
    #     server.quit()