from flask import Flask, jsonify, request

from config import Config
from models import User, db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# USER:
# ----- SELECT todos:
@app.route('/users')
def users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

# ----- SELECT por ID:
@app.route('/users/<int:user_id>', methods = ['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())

# ----- Inserir usuario:
@app.route('/users', methods = ['POST'])
def insert_user():
    data = request.get_json()
    new_user = User(
        username = data['username'],
        email = data['email'],
        password = data['password'],
        phone = data['phone'],
        location = data['location'],
        description = data['description']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

# ----- UPDATE por ID:
@app.route('/users/<int:user_id>', methods = ['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = User.query.get_or_404(user_id)
    user.username = data['username']
    user.email = data['email']
    user.password = data['password']
    user.phone = data['phone']
    user.location = data['location']
    user.description = data['description']
    db.session.commit()
    return jsonify(user.to_dict())

# ----- DELETE por ID:
@app.route('/users/<int:user_id>', methods = ['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return '', 204

# RUN:
if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug = True, port = 5001)
