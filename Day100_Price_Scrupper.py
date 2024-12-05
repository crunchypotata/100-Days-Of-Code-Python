import requests, schedule, time, os, smtplib
from bs4 import BeautifulSoup
from replit import db
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def addToDB():
    link = input("Link: ")
    price = float(input("Price: "))
    db[time.time()] = {"link" : link, "price" : None, "level" : price}

def emailMe(level, price, link):
    password = os.environ['mailPassword']
    username = os.environ['mailUsername']
    host = "smtp.gmail.com"
    server = "smtp.gmail.com"
    port = 587
    s = smtplib.SMTP(host=server, port=port)
    s.starttls()
    s.login(username, password)

    msg = MIMEMultipart()
    msg["To"] = username
    msg["From"] = username
    msg["Subject"] = "Sale!"
    text = f"""<p><a href="{link}"This item is now {price} which is below your purchase level of {level}</p>"""
    msg.attach(MIMEText(text, "html" ))
    s.send_message(msg)
    del msg

def update():   
    keys = db.keys()
    for key in keys:
        url = db[key]["link"]
        price = db[key]["price"]
        level = db[key]["price"]
        response = requests.get(url)
        html = response.text

        soup = BeautifulSoup(html, "html.parser")

        myPrice = soup.find_all("div", {"class": "f-productPageMain__buyBox"})

        thisPrice = float(myPrice[0].text[1:].replace(",", ""))
        if thisPrice != price:
            db[key]["price"] = thisPrice
            if thisPrice <= level:
                print("Cheaper!")
                emailMe(level, price, url)

schedule.every(1).day.do(update)

while True:
    schedule.run_pending()
    time.sleep(1)