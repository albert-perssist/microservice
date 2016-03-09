from services import root_dir, nice_json
from flask import Flask
from werkzeug.exceptions import NotFound
import json


app = Flask(__name__)

with open("{}/database/movies.json".format(root_dir()), "r") as f:
    movies = json.load(f)


@app.route("/", methods=['GET'])
def hello():
    return nice_json({
        "uri": "/",
        "subresource_uris": {
            "movies": "/movies",
            "movie": "/movies/<id>"
        }
    })

@app.route("/movies/<movieid>", methods=['GET'])
def movie_info(movieid):
    if movieid not in movies:
        raise NotFound

    result = movies[movieid]
    result["uri"] = "/movies/{}".format(movieid)

    return nice_json(result)


@app.route("/movies", methods=['GET'])
def movie_record():
    return nice_json(movies)

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
    app.run(port=5001, debug=True, host='0.0.0.0')

