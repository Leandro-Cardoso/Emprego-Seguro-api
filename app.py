from flask import Flask, jsonify, request

from config import Config
from models import User,Message, db

# CONFIG:
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# ERROR:
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error' : 'not found',
        'message' : 'The requested URL was not found on the server'
    }), 404

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
# ----- SELECT todos:
@app.route('/messages')
def get_all_messages():
    messages = Message.query.all()
    return jsonify([msg.to_dict() for msg in messages])

# ----- SELECT por ID:
@app.route('/messages/<int:message_id>', methods=['GET'])
def get_message(message_id):
    message = Message.query.get_or_404(message_id)
    return jsonify(message.to_dict())

# ----- INSERT mensagem:
@app.route('/messages', methods=['POST'])
def insert_message():
    data = request.get_json()
    new_message = Message(
        sender_id=data['sender_id'],
        receiver_id=data['receiver_id'],
        content=data['content']
    )
    db.session.add(new_message)
    db.session.commit()
    return jsonify(new_message.to_dict()), 201

# ----- UPDATE por ID:
@app.route('/messages/<int:message_id>', methods=['PUT'])
def update_message(message_id):
    data = request.get_json()
    message = Message.query.get_or_404(message_id)
    message.content = data['content']
    db.session.commit()
    return jsonify(message.to_dict())

# ----- DELETE por ID:
@app.route('/messages/<int:message_id>', methods=['DELETE'])
def delete_message(message_id):
    message = Message.query.get_or_404(message_id)
    db.session.delete(message)
    db.session.commit()
    return '', 204
# MESSAGE:

# ----- SELECT por ID:
@app.route('/messages/<int:message_id>', methods=['GET'])
def get_message(message_id):
    message = Message.query.get_or_404(message_id)
    return jsonify(message.to_dict())

# ----- INSERT mensagem:
@app.route('/messages', methods=['POST'])
def insert_message():
    data = request.get_json()
    new_message = Message(
        sender_id=data['sender_id'],
        receiver_id=data['receiver_id'],
        content=data['content']
    )
    db.session.add(new_message)
    db.session.commit()
    return jsonify(new_message.to_dict()), 201

# ----- UPDATE por ID:
@app.route('/messages/<int:message_id>', methods=['PUT'])
def update_message(message_id):
    data = request.get_json()
    message = Message.query.get_or_404(message_id)
    message.content = data['content']
    db.session.commit()
    return jsonify(message.to_dict())

# ----- DELETE por ID:
@app.route('/messages/<int:message_id>', methods=['DELETE'])
def delete_message(message_id):
    message = Message.query.get_or_404(message_id)
    db.session.delete(message)
    db.session.commit()
    return '', 204    
# RUN:
if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug = True, port = 5001)
