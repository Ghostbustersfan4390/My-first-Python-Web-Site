from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def web_page():
    return render_template("index 2.0.html")
app.run()