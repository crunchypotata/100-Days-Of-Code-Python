from flask import Flask, redirect,  request

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def index():
    page = ""
    return page

@app.route("/blog/78")
def hr():
  return redirect("/day78")

@app.route("/blog/79")
def br():
  return redirect("/day78")

@app.route('/day78', methods = ["GET"])
def day78():
    data = request.args
    template = "default"
    if data != {}:
      template = data["template"]
    title = "78"
    link = "https://replit.com/@crunchpotata/Day78100Days"
    text = "Please, working"
    page = ""
    f = open("template/blog.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{title}", title)
    page = page.replace("{link}", link)
    page = page.replace("{text}", text)
    page = page.replace("{template}", template)
    return page

@app.route('/day78', methods = ["GET"])
def day79():
    data = request.args
    template = "default"
    if data != {}:
      template = data["template"]
    title = "79"
    link = "https://replit.com/@crunchpotata/Day79100Days"
    text = "Yay!"
    page = ""
    f = open("template/blog.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{title}", title)
    page = page.replace("{link}", link)
    page = page.replace("{text}", text)
    page = page.replace("{template}", template)

    return page

app.run(host='0.0.0.0', port=81)