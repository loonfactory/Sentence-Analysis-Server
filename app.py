from flask import Flask, render_template, request
from konlpy.tag import Mecab
import json

app = Flask(__name__)
mecab = Mecab()

@app.route("/")
def hello():
    return render_template("index.html") 

@app.route("/version")
def version():
  return "0.1.0"

@app.route('/sentence')
def sentence_defualt():
  return "Use: GET /sentence/[string]"


@app.route('/sentence', methods=['POST'])
def sentence_post():
  string = request.form['string']
  return json.dumps(mecab.pos(string), ensure_ascii = False)


@app.route('/sentence/<string>')
def sentence(string):
  return json.dumps(mecab.pos(string), ensure_ascii = False)
