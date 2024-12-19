from app import db

class SMS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)  # Link to the User ID
    message = db.Column(db.String(255), nullable=False)

    def __init__(self, user_id, message):
        self.user_id = user_id
        self.message = message
