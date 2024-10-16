from flask import Flask, redirect

app = Flask(__name__, static_url_path="/static")

@app.route('/')
def portfolio():
    myName = "Alex"
    title = "Day 45 Solution"
    text = "I created simple programm for Todo manager"
    images = "calculator.jpeg"
    link = "https://replit.com/@crunchpotata/Day66100Days?v=1"

    page = ""
    f = open("template/portfolio.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{name}", myName)
    page = page.replace("{title}", title)
    page = page.replace("{text}", text)
    page = page.replace("{images}", images)
    page = page.replace("{link}", link)
    return page
    
@app.route('/45')
def fortyfive():
    return redirect("https://github.com/crunchypotata/100-Days-Of-Code-Python/blob/main/Day045_ToDo_Organizer.py")
    

app.run(host='0.0.0.0', port=81)
