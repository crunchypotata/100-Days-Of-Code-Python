from flask import Flask

app = Flask(__name__, static_url_path="/static")

@app.route('/')
def index():
  return "Go to /portfolio or /linktree"
  
@app.route('/portfolio')
def portfolio(): 
  page = """<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Portfolio</title>
  <link href="/static/css/portfolio.css" rel="stylesheet" type="text/css" />
</head>

<body>
  <h1>My Portfolio</h1>
  <h2>Todo Manager</h2>

  <p>I created simple programm for Todo manager</p>

  <ul>
    <li>Python</li>
    <li>List</li>
    <li>Login</li>
  </ul>

     
  <h2>Calcutalor</h2>
  <p>I created simple programm for Calculator</p>

  <ul>
    <li>Python</li>
    <li>GUI</li>
    </ul>
    
<img src="/static/image/calculator.jpeg" width = 90%>
<p><a href="https://replit.com/@crunchpotata/Day66100Days?v=1">You can see it here</a></p>

  <script src="script.js"></script>

</body>

</html>
"""
  return page
  
@app.route('/linktree')
def linktree(): 
  page = """<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Linktree</title>
  <link href="/static/css/linktree.css" rel="stylesheet" type="text/css" />
</head>
  
<body>
  <h2> My Linktree </h2>
  <ul>
    <li><a href="https://www.linkedin.com/in/ayakimova"> LinkedIn </a></li>
    <li><a href="https://github.com/crunchypotata"> GitHub </a></li>
    
  <script src="script.js"></script>
</body>
    
</html>
"""
  return page

app.run(host ='0.0.0.0', port = 81)
