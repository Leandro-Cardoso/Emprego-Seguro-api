from flask import Flask, jsonify, request

from config import Config
from models import User, Service, Message, db

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

# ----- INSERT usuario:
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

# SERVICE:
# ----- SELECT todos:
@app.route('/services')
def services():
    services = Service.query.all()
    return jsonify([service.to_dict() for service in services])

# ----- SELECT por ID:
@app.route('/services/<int:service_id>', methods = ['GET'])
def get_service(service_id):
    service = Service.query.get_or_404(service_id)
    return jsonify(service.to_dict())

# ----- SELECT por KEYWORDS:
@app.route('/services/search', methods=['GET'])
def search_services():
    query = request.args.get('q')
    if query:
        keywords = query.split()
        services_query = Service.query
        for keyword in keywords:
            services_query = services_query.filter(
                (Service.title.ilike(f'%{keyword}%')) |
                (Service.description.ilike(f'%{keyword}%')) |
                (Service.category.ilike(f'%{keyword}%'))
            )
        services = services_query.all()
        return jsonify([service.to_dict() for service in services])
    else:
        return 404

# ----- INSERT usuario:
@app.route('/services', methods = ['POST'])
def insert_service():
    data = request.get_json()
    new_service = Service(
        user_id = data['user_id'],
        title = data['title'],
        description = data['description'],
        category = data['category'],
        price = data['price'],
        location = data['location']
    )
    db.session.add(new_service)
    db.session.commit()
    return jsonify(new_service.to_dict()), 201

# ----- UPDATE por ID:
@app.route('/services/<int:service_id>', methods = ['PUT'])
def update_service(service_id):
    data = request.get_json()
    service = Service.query.get_or_404(service_id)
    service.user_id = data['user_id']
    service.title = data['title']
    service.description = data['description']
    service.category = data['category']
    service.price = data['price']
    service.location = data['location']
    db.session.commit()
    return jsonify(service.to_dict())

# ----- DELETE por ID:
@app.route('/services/<int:service_id>', methods = ['DELETE'])
def delete_service(service_id):
    service = Service.query.get_or_404(service_id)
    db.session.delete(service)
    db.session.commit()
    return '', 204

# TODO Implementar controllers de MESSAGE:
# MESSAGE:
# ----- SELECT todos:
# ----- SELECT por ID:
# ----- INSERT usuario:
# ----- UPDATE por ID:
# ----- DELETE por ID:

# RUN:
if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug = True, port = 5001)
