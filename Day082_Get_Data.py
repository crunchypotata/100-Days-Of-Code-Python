from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
  get = request.args
  if get["language"].lower() == "english":
    return "Hello dude!"
  elif get["language"].lower() == "spanish":
    return "Aloha amigo!"
  else:
    return "No data"

app.run(host='0.0.0.0', port=81)
