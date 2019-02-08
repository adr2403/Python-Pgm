from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home") 
def check():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")   

@app.route("/institution")
def institute():
    return "LKG-XII in BMV KYLM     Engg. 4 yrs in SVNCE"    


if(__name__=="__main__"):
    app.run(debug=True)