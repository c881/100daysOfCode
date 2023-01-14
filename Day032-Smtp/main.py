import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "kobygs78@gmail.com"
password = input("Type your password and press enter: ")
message = "Subject: Hi there \n\n Have a great day."
# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
# Like with files, using with to auto close the connection
with smtplib.SMTP(smtp_server,port) as server:
    try:
    # server = smtplib.SMTP(smtp_server,port)
        server.starttls(context=context) # Secure the connection
        server.login(sender_email, password)
        server.sendmail(from_addr=sender_email,
                        to_addrs="jacov.g@gmail.com",
                        msg=message)
    except Exception as e:
        # Print any error messages to stdout
        print(e)