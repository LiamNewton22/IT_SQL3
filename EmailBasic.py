import smtplib
from time import sleep

email = 'goodshepherdiot@gmail.com'  # your email
password = 'P@ssword#1'  # your email password
send_to_email = 'newtonliam03@gmail.com'  # WHO WE ARE SENDING EMAIL TO
message = 'Hooray this is working!'  # message with the email

while True: 
    server = smtplib.SMTP('smtp.gmail.com', 587)  # connect to the server
    server.starttls()  # use TLS (Transport Layer Security)
    server.login(email, password)
    server.sendmail(email, send_to_email, message)
    sleep(10)

server.quit()
