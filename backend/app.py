import os
import json

from flask import Flask, Response
from database.db import initialize_db
from services.github import import_list_commits, call_languages_api
from database.models import Commits
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.config['MONGODB_SETTINGS'] = {
    'host': f"mongodb://{os.environ['MONGODB_USERNAME']}:{os.environ['MONGODB_PASSWORD']}@{os.environ['MONGODB_HOST']}:27017/webapp?authSource=admin"
}

initialize_db(app)


@app.route("/api")
def index():
    import_list_commits()
    return Response("Hello", mimetype="application/json", status=200)


@app.route("/commits/weekly")
def show_weekly():
    pipeline = [
        {'$group':
            {
                '_id': {'$week': '$authored_date'},
                'count': {'$sum': 1}
            }
        },
        {"$sort": {"_id": 1}},
    ]

    data = Commits.objects().aggregate(*pipeline)
    return Response(json.dumps(list(data)), mimetype="application/json", status=200)

@app.route("/commits/monthly")
def show_monthly():
    pipeline = [
        {'$group':
            {
                '_id': {'$month': '$authored_date'},
                'count': {'$sum': 1}
            }
        },
        {"$sort": {"_id": 1}},
    ]

    data = Commits.objects().aggregate(*pipeline)
    return Response(json.dumps(list(data)), mimetype="application/json", status=200)


@app.route("/committer")
def show_committer():
    pipeline = [
        {
            '$group':
                {
                    '_id': '$committer_avatar_url',
                    'count': {'$sum': 1}
                }
        },
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]

    data = Commits.objects().aggregate(*pipeline)
    return Response(json.dumps(list(data)), mimetype="application/json", status=200)


@app.route("/languages")
def show_languages():
    return Response(call_languages_api(), mimetype="application/json", status=200)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
