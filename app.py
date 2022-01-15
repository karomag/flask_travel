from flask import Flask, render_template
from data import tours

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/departure/<departure>')
def departures(departure):
    return render_template('departure.html')


@app.route('/tour/<id>')
def tours(id):
    return render_template('tour.html')


@app.route('/data/')
def data():
    return render_template('tour.html')


if __name__ == '__main__':
    app.run()
