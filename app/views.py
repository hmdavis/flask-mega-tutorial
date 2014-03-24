from app import app 

# create mappings from urls to function
@app.route('/')
@app.route('/index')
def index(): 
  return "Hello, World!"
