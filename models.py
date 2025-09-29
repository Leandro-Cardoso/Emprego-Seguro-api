from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique = True, nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    password = db.Column(db.String(100), unique = False, nullable = False)
    phone = db.Column(db.String(100), unique = True, nullable = False)
    location = db.Column(db.String(100), unique = False, nullable = False)
    description = db.Column(db.String(100), unique = False, nullable = True)

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
    
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(100))
    price = db.Column(db.Numeric(10, 2))
    location = db.Column(db.String(100), nullable=False)
    published_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'price': float(self.price) if self.price else None,
            'location': self.location,
            'published_at': self.published_at.isoformat() if self.published_at else None
        }

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    sent_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    read = db.Column(db.Boolean, nullable=False, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'sender_id': self.sender_id,
            'receiver_id': self.receiver_id,
            'content': self.content,
            'sent_at': self.sent_at.isoformat() if self.sent_at else None,
            'read': self.read
        }
