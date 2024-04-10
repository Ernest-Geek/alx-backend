#!/usr/bin/env python3
from flask import flask
render template


# start the flask app
app = Flask(__name__)


@app.route('/')
def index():
    """
    Render the index.html template

    return: Rendered html content
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
