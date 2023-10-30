from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
app = Flask(__name__)
boostrap = Bootstrap5(app)

@app.route('/')
def hello():
    return '<p>Sergio LMAO Jean-Luc LOL<p>'

@app.route('/Alexis')
def wc():
    return render_template("task4.html")