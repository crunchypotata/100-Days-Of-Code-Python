from flask import Flask

app = Flask(__name__, static_url_path = "/static")

@app.route('/')
def index():
  return "Go to /portfolio or /linktree"
  
@app.route('/')
def portfolio(): 
  page = """

   <html>

     <head>
       <title>Portfolio</title> 
     </head>

     <body>
       <h1>My Portfolio</h1>
       <h2>Todo Manager</h2>

       <p>I created simple programm for Todo manager

         <ul>
           <li>Python</li>
           <li>List</li>
           <li>Login</li>
         </ul>

       </p>
       <h2>Calcutalor</h2>
       <p>I created simple programm for Todo manager

         <ul>
           <li>Python</li>
           <li>GUI</li>
         </ul>

       </p>
       <img src="static/images/calculator.jpeg" width = 90%>
       <p><a href="https://replit.com/@crunchpotata/Day66100Days?v=1">You can see it here</a></p>

     </body>



   </html>

    """

  return page
  
 
@app.route('/linktree')
def linktree(): 
  page = """
  
  <html>
  
    <head>
       <title>Linktree</title> 
    </head>
  
    <body>
      <h2> My Linktree </h2>
      <ul>
        <li><a href="https://github.com/crunchypotata"> GitHub </a></li>
    
    </body>
    
  </html>"""
  return page

app.run(host ='0.0.0.0', port = 81)
