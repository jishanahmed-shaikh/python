import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import mysql.connector
import datetime

def sendmail(username,mail,type):
    # create a message object
    msg = MIMEMultipart()
    msg['From'] = 'bloodbridge2023@gmail.com'
    msg['To'] = mail

    if type=="donation":
        msg['Subject'] = 'Bloodbridge : Your Donation Status Changed'
        # add the message body
        body = 'Hello '+username+', This is to Confirm that your Donation status has Changed, log in to Bloodbridge and check it.'
        msg.attach(MIMEText(body, 'plain'))
    elif type=="decline":
        msg['Subject'] = 'Bloodbridge: Your Request Status Changed'
        body = 'Hello '+username+', This is to Confirm that your Blood Request has been Declined, log in to bloodbridge and check it.'
        msg.attach(MIMEText(body, 'plain'))
    else:
        msg['Subject'] = 'Your Request Status Changed'
        # add the message body
        body = 'Hello '+username+', This is to Confirm that your Blood Request has been Approved by '+type+', log in to bloodbridge and check it.'
        msg.attach(MIMEText(body, 'plain'))

    # establish a secure SMTP connection
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # login to the email account
    server.login('bloodbridge2023@gmail.com', 'pywjityzdaojsjul')

    # send the email
    text = msg.as_string()
    server.sendmail('bloodbridge2023@gmail.com', mail, text)

    # close the SMTP connection
    server.quit()

def sendmail_donation(username,bname,bloc,appoitment_date,appointment_time):
    mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='bloodbridge'
        )
    cursor = mydb.cursor()
    query="select name,email from users where username=%s"
    cursor.execute(query,(username,))
    result=cursor.fetchone()
    name=result[0]
    mail=result[1]
    # create a message object
    msg = MIMEMultipart()
    msg['From'] = 'bloodbridge2023@gmail.com'
    msg['To'] = mail
    msg['Subject'] = 'Bloodbridge : Your Donation Request was registered!'
    body = f"Hello {name},\n\nThis is to confirm that you have made a Blood Donation Request at {bname}\n situated at {bloc} on {appoitment_date} at {appointment_time}. Please report at the given time slot with your government identification.\n\nBest regards,\nBloodBridge"
    msg.attach(MIMEText(body, 'plain'))

    # establish a secure SMTP connection
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # login to the email account
    server.login('bloodbridge2023@gmail.com', 'pywjityzdaojsjul')

    # send the email
    text = msg.as_string()
    server.sendmail('bloodbridge2023@gmail.com', mail, text)

    # close the SMTP connection
    server.quit()

def sendmail_request(username):
    mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='bloodbridge'
        )
    cursor = mydb.cursor()
    query="select name,email from users where username=%s"
    cursor.execute(query,(username,))
    result=cursor.fetchone()
    name=result[0]
    mail=result[1]
    # create a message object
    msg = MIMEMultipart()
    msg['From'] = 'bloodbridge2023@gmail.com'
    msg['To'] = mail
    msg['Subject'] = 'Bloodbridge : Your Blood Request was registered!'
    body = f"Hello {name},\n\nThis is to confirm that you have made a Blood Request at"+str(datetime.date.today())+"\nYou will receive a mail when there is change in status of your request\n or alternatively you can check the status in profile section of blood bridge app\n\nBest regards,\nBloodBridge"
    msg.attach(MIMEText(body, 'plain'))

    # establish a secure SMTP connection
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # login to the email account
    server.login('bloodbridge2023@gmail.com', 'pywjityzdaojsjul')

    # send the email
    text = msg.as_string()
    server.sendmail('bloodbridge2023@gmail.com', mail, text)

    # close the SMTP connection
    server.quit()