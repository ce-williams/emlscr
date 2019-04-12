import smtplib

import config

def send_email(subject, msg):
    try:
        server = smtplib.SMTP("smtp.gmail.com:587")
        # protocol for establishing a server 
        server.ehlo()
        server.starttls()
        # account for outgoing
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = "Subject: {}\n\n{}".format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message)
        server.quit()
        print("Message sent")
    except:
        print("Email failed to send")

subject = "Test subject"
msg = "Hi, how are you today?"

send_email(subject, msg)
