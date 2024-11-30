from models.user import User
from database.db import db

def get_all_users_from_db():
    return [{"id": u.id, "username": u.username, "email": u.email, "role": u.role, "isBanned": u.isBanned} for u in User.query.all()]

def get_user_from_db(user_id):
    user = User.query.get(user_id)
    if user:
        return {"id": user.id, "username": user.username, "email": user.email, "role": user.role, "isBanned": user.isBanned}
    return None

def add_user_to_db(data):
    new_user = User(username=data["username"], password=data["password"], email=data["email"], role=data.get("role", "member"), isBanned=data.get("isBanned", False))
    db.session.add(new_user)
    db.session.commit()
    return {"id": new_user.id, "username": new_user.username, "email": new_user.email, "role": new_user.role, "isBanned": new_user.isBanned}

def update_user_in_db(user_id, data):
    user = User.query.get(user_id)
    if user:
        user.username = data.get("username", user.username)
        user.email = data.get("email", user.email)
        user.role = data.get("role", user.role)
        user.isBanned = data.get("isBanned", user.isBanned)
        db.session.commit()
        return {"id": user.id, "username": user.username, "email": user.email, "role": user.role, "isBanned": user.isBanned}
    return None

def remove_user_from_db(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    return False
