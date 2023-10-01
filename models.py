"""Models for Cupcake app."""


from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def connect_db(app):
    """connects the app inherited from app.py to the proper database"""
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """model for cupcake."""

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    flavor = db.Column(db.Text,
                       nullable=False)

    size = db.Column(db.Text,
                     nullable=False)

    rating = db.Column(db.Float,
                       nullable=False)

    image = db.Column(db.Text,
                      nullable=False,
                      default="https://tinyurl.com/demo-cupcakes")
    
    def serialize(self):
        """returns json dict of instance"""

        return {
            "id" : self.id,
            "flavor" : self.flavor,
            "size" : self.size,
            "rating" : self.rating,
            "image" : self.image
        }