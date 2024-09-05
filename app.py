from flask import Flask
from routes import *

app = Flask(__name__)

app.register_blueprint(main, url_prefix = '/')

if __name__== '__main__':
    app.run(debug=True)


# Сделать роут / по которому запустится сайт