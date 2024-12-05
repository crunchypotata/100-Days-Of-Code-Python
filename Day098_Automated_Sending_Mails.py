import schedule, random, time, os, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

quotes = []
f = open("quites.txt", "r")
quotes = eval(f.read())
f.close()

password = os.environ['mailPassword']
username = os.environ['mailUsername']

def sendMail(quote):
    quotes = random.choice("quotes")
    server = "smtp.gmail.com"
    port = 587
    s = smtplib.SMTP(host=server, port=port)
    s.starttls()
    s.login(username, password)

    msg = MIMEMultipart()
    msg["To"] = username
    msg["From"] = username
    msg["Subject"] = "Daily Inspiration"
    msg.attach(MIMEText(quote, "html" ))
                        
    s.send_message(msg)
    del msg

schedule.every(24).hours.do(sendMail)

while True:
    schedule.run_pending()
    time.sleep(1)
