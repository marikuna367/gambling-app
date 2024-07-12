from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    bio = db.Column(db.String(255))
    avatar_url = db.Column(db.String(255))

    def __repr__(self):
        return f'<User {self.username}>'
