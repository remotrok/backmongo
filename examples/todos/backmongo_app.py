from flask import Flask

from flask.ext import backmongo

app = Flask(__name__)

backmongo.init_app(app)


if __name__ == "__main__":
    app.run(debug=True)
