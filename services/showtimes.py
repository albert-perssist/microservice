from services import root_dir, nice_json
from flask import Flask
from werkzeug.exceptions import NotFound
import json


app = Flask(__name__)

with open("{}/database/showtimes.json".format(root_dir()), "r") as f:
    showtimes = json.load(f)


@app.route("/", methods=['GET'])
def hello():
    return nice_json({
        "uri": "/",
        "subresource_uris": {
            "showtimes": "/showtimes",
            "showtime": "/showtimes/<date>"
        }
    })


@app.route("/showtimes", methods=['GET'])
def showtimes_list():
    return nice_json(showtimes)


@app.route("/showtimes/<date>", methods=['GET'])
def showtimes_record(date):
    if date not in showtimes:
        raise NotFound
    print showtimes[date]
    return nice_json(showtimes[date])

from opbeat.contrib.flask import Opbeat

OPBEAT = {
    'DEBUG': True
        }


opbeat = Opbeat(
        app,
        organization_id='7f7fa7744c924fe4adc32c676975d041',
        app_id='e0cdcf4185',
        secret_token='8739153bccd94d5a080231e27266a1547212431f',
    )

if __name__ == "__main__":
    app.run(port=5002, debug=True, host='0.0.0.0')
