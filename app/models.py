from datetime import datetime
from . import db

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    image = db.Column(db.String(100), nullable=True)
    user_id = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"ToDo('{self.title}', '{self.description}', '{self.time}', '{self.image}')"
