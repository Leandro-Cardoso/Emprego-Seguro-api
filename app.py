from flask import Flask, jsonify

from config import Config
from models import User, db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/users')
def users():
    return jsonify({'name' : 'Teste'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
    app.run(debug = True, port = 5001)
