from flask import Flask

app = Flask(__name__, static_url_path="/static")

dairy = {}
dairy["78"] = {"link": "https://replit.com/@crunchpotata/Day78100Days", "text": "Not clear"}
dairy["79"] = {"link": "https://replit.com/@crunchpotata/Day79100Days", "text": "Now it's ok"}

@app.route('/<pageNumber>')
def index(pageNumber):
  global dairy
  page = ""
  f = open("/static/template/day.html", "r")
  page = f.read()
  f.close()

  page = page.replace("{day}", pageNumber)
  page = page.replace("{link}", dairy[pageNumber]["link"])
  page = page.replace("{text}", dairy[pageNumber]["text"])
  return page

app.run(host='0.0.0.0', port=81)

