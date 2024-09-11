from flask_sqlalchemy import SQLAlchemy
from flask import url_for


db=SQLAlchemy()

class Book(db.Model):
    __tablename__='book'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    cover_photo = db.Column(db.String(250))
    num_page= db.Column(db.Integer)
    description = db.Column(db.String(300))

    @property
    def image_url(self):
        return url_for("static", filename=f"images/{self.cover_photo }")
