from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def display():
    return render_template('index.html')
