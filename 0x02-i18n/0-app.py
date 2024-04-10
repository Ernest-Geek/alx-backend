#!/usr/bin/env python3
from flask import flask
render template


# create the flask app
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
