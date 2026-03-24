from extensions import db

class User(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(40), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "fullname": self.fullname,
            "age": self.age,
            "username": self.username,
            "email": self.email
        }

