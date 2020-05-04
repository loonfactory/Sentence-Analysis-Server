from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html") 

@app.route("/version")
def version():
  return "0.0.1"

@app.route('/sentence')
def sentence_defualt():
  return "Use: GET /sentence/[string]"


@app.route('/sentence/<string>')
def sentence(string):
  return string
