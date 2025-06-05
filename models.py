from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique = True, nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    password = db.Column(db.String(100), unique = True, nullable = False)
    phone = db.Column(db.String(100), unique = True, nullable = False)
    location = db.Column(db.String(100), unique = True, nullable = False)
    description = db.Column(db.String(100), unique = True, nullable = False)

    def to_dict(self):
        return {
            'id' : self.id,
            'username' : self.username,
            'email' : self.email,
            'password' : self.password,
            'phone' : self.phone,
            'location' : self.location,
            'description' : self.description
        }
