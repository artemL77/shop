from flask import render_template, Blueprint

main = Blueprint('/', __name__)

@main.route('')
def home():
    return render_template('index.html')