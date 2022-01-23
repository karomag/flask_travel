from flask import Flask, render_template
from data import tours, title, subtitle, departures, description

app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'index.html',
        departures=departures,
        description=description,
        title=title,
        tours={key: val for key, val in tours.items() if key < 7},
        subtitle=subtitle,
        )


@app.route('/departure/<string:departure_from>')
def departure(departure_from=None):
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
    return render_template(
        'tour.html',
        departures=departures,
        title=title,
        tour=tours.get(tour_id),
        )


if __name__ == '__main__':
    app.run(debug=True)
