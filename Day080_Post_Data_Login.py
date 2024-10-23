from flask import Flask, request

app = Flask(__name__)

users = {}
users["alex"] = {"email": "a@mail.com", "password": "Qwerty"}
users["lev"] = {"email": "l@mail.com", "password": "l9L"}
users["pet"] = {"email": "p@mail.com", "password": "Meow"}

@app.route("/login", methods=["POST"])
def login():
  form = request.form
  details = {}
  try:
    details = users[form["username"]]
  except KeyError:
    return "Username, email or password incorrect"
  if form["email"] == details["email"] and form["password"] == details["password"]:
    return "You are logged in"
  else:
    return "Username, email or password incorrect"


@app.route('/')
def index():
  page = """<form method = "post" action="login">
    <p>Username: <input type="text" name="username" required> </p>
    <p>Email: <input type="Email" name="email" required> </p>
    <p>Password: <input type="password" name="password"required> </p>
    
    <button type="submit">Login</button>
    
  </form>"""
  
  return page
  
app.run(host='0.0.0.0', port=81)
