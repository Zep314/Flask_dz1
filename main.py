import os
import sys
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route('/')
def base():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/catalog/')
def catalog():
    return render_template('catalog.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)
