import random

from flask import Flask, abort, render_template
from data import tours, title, subtitle, departures, description

app = Flask(__name__)


@app.route('/')
def index():
    random_keys = random.sample(list(tours.keys()), k=6)
    return render_template(
        'index.html',
        departures=departures,
        description=description,
        title=title,
        # tours={key: val for key, val in tours.items() if key < 7},
        tours={key: tours.get(key) for key in random_keys},
        subtitle=subtitle,
        )


@app.route('/departure/<string:departure_from>')
def departure(departure_from=None):
    if departure_from not in departures.keys():
        abort(404)
    return render_template(
        'departure.html',
        departures=departures,
        title=title,
        tours={key: val for key, val in tours.items()
               if val.get('departure') == departure_from},
        departure_from=departures.get(departure_from),
    )


@app.route('/tour/<int:tour_id>')
def tour(tour_id):
    if tour_id not in tours.keys():
        abort(404)
    return render_template(
        'tour.html',
        departures=departures,
        title=title,
        tour=tours.get(tour_id),
        )


if __name__ == '__main__':
    app.run()
