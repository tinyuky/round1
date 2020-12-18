from .db import db


class Commits(db.Document):
    authored_date = db.DateTimeField()
    committer_id = db.StringField()
    committer_name = db.StringField()
    committer_avatar_url = db.StringField()
    commit_html_url = db.StringField()
