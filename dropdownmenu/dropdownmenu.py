from flask import Flask, render_template, session

app = Flask('dropdownmenu')


@app.route('/')
def index():
    return render_template('indexdropdown.html')

app.secret_key = "super secret key"