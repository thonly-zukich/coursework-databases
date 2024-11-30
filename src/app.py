from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1111@localhost:3306/ProjectManagement'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    role = db.Column(db.String(50))
    isBanned = db.Column(db.Boolean, default=False)

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{
        "id": u.id,
        "username": u.username,
        "email": u.email,
        "role": u.role,
        "isBanned": u.isBanned
    } for u in users]), 200

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if not user:
        abort(404, description="User not found")
    return jsonify({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "role": user.role,
        "isBanned": user.isBanned
    }), 200

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    if not data or not "username" in data or not "email" in data:
        abort(400, description="Missing required fields: username or email")
    
    if User.query.filter_by(username=data['username']).first():
        abort(400, description="Username already exists")
    
    if User.query.filter_by(email=data['email']).first():
        abort(400, description="Email already exists")

    new_user = User(
        username=data["username"],
        password=data["password"],
        email=data["email"],
        role=data.get("role", "member"),
        isBanned=data.get("isBanned", False)
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "id": new_user.id,
        "username": new_user.username,
        "email": new_user.email,
        "role": new_user.role,
        "isBanned": new_user.isBanned
    }), 201

@app.route('/users/<int:id>', methods=['PATCH'])
def update_user(id):
    user = User.query.get(id)
    if not user:
        abort(404, description="User not found")

    data = request.get_json()

    if "username" in data:
        user.username = data["username"]
    if "email" in data:
        user.email = data["email"]
    if "role" in data:
        user.role = data["role"]
    if "isBanned" in data:
        user.isBanned = data["isBanned"]

    db.session.commit()

    return jsonify({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "role": user.role,
        "isBanned": user.isBanned
    }), 200

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        abort(404, description="User not found")

    db.session.delete(user)
    db.session.commit()

    return jsonify({
        'message': f'User {user.username} has been deleted successfully',
        'user_id': user.id
    }), 200

@app.errorhandler(HTTPException)
def handle_exception(e):
    return jsonify({
        "error": f"{e.code} {e.name}",
        "message": e.description
    }), e.code

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
