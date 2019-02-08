from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "Hello"

@app.route("/home") 
def check():
    return "Welcome to home page"   

@app.route("/about")
def about():
    return "Page created by Adarsh Rajesh"    

@app.route("/institution")
def institute():
    return "LKG-XII in BMV KYLM     Engg. 4 yrs in SVNCE"    


if(__name__=="__main__"):
    app.run()