# Реалізація інформаційного та програмного забезпечення


## SQL-скрипт для створення початкового наповнення бази даних

```sql
CREATE SCHEMA IF NOT EXISTS ProjectManagement;
USE ProjectManagement;

-- Створення таблиць
CREATE TABLE IF NOT EXISTS Project (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS Board (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    project_id BIGINT,
    FOREIGN KEY (project_id) REFERENCES Project(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Task (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    deadline DATETIME,
    status VARCHAR(50),
    board_id BIGINT,
    FOREIGN KEY (board_id) REFERENCES Board(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS Attachment (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    format VARCHAR(50),
    content BLOB,
    task_id BIGINT,
    FOREIGN KEY (task_id) REFERENCES Task(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Label (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    color VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS Tag (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    task_id BIGINT,
    label_id BIGINT,
    FOREIGN KEY (task_id) REFERENCES Task(id) ON DELETE CASCADE,
    FOREIGN KEY (label_id) REFERENCES Label(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS User (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    role VARCHAR(50),
    isBanned TINYINT DEFAULT 0
);

CREATE TABLE IF NOT EXISTS Member (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    user_id BIGINT,
    project_id BIGINT,
    FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE,
    FOREIGN KEY (project_id) REFERENCES Project(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Assignee (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    task_id BIGINT,
    member_id BIGINT,
    FOREIGN KEY (task_id) REFERENCES Task(id) ON DELETE CASCADE,
    FOREIGN KEY (member_id) REFERENCES Member(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Permission (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    action VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS AccessGrant (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    member_id BIGINT,
    permission_id BIGINT,
    FOREIGN KEY (member_id) REFERENCES Member(id) ON DELETE CASCADE,
    FOREIGN KEY (permission_id) REFERENCES Permission(id) ON DELETE CASCADE
);

-- Очищення таблиць
DELETE FROM AccessGrant;
DELETE FROM Assignee;
DELETE FROM Member;
DELETE FROM User;
DELETE FROM Tag;
DELETE FROM Label;
DELETE FROM Attachment;
DELETE FROM Task;
DELETE FROM Board;
DELETE FROM Project;
DELETE FROM Permission;

-- Вставка даних у Project
INSERT INTO Project (id, title, description) VALUES
(1, 'Project Alpha', 'Description Alpha'),
(2, 'Project Beta', 'Description Beta');

-- Вставка даних у Board
INSERT INTO Board (id, title, project_id) VALUES
(25, 'Board 1', 1),
(26, 'Board 2', 1),
(27, 'Board 3', 2);

-- Вставка даних у Task
INSERT INTO Task (id, title, description, deadline, status, board_id) VALUES
(1, 'Task 1', 'Description Task 1', '2024-12-31 23:59:59', 'open', 25),
(2, 'Task 2', 'Description Task 2', '2024-11-30 23:59:59', 'in progress', 26),
(3, 'Task 3', 'Description Task 3', '2024-10-15 23:59:59', 'completed', 27);

-- Вставка даних у Label
INSERT INTO Label (id, name, color) VALUES
(1, 'Urgent', 'red'),
(2, 'Review', 'blue'),
(3, 'Low Priority', 'green');

-- Вставка даних у Tag
INSERT INTO Tag (id, task_id, label_id) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3);

-- Вставка даних у User
INSERT INTO User (id, username, password, email, role, isBanned) VALUES
(1, 'john_doe', 'password123', 'john@example.com', 'admin', 0),
(2, 'jane_smith', 'password456', 'jane@example.com', 'member', 0),
(3, 'alice_jones', 'password789', 'alice@example.com', 'member', 0);

-- Вставка даних у Member
INSERT INTO Member (id, user_id, project_id) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 3, 2);

-- Вставка даних у Assignee
INSERT INTO Assignee (id, task_id, member_id) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3);

-- Вставка даних у Permission
INSERT INTO Permission (id, action) VALUES
(1, 'view'),
(2, 'edit'),
(3, 'delete');

-- Вставка даних у AccessGrant
INSERT INTO AccessGrant (id, member_id, permission_id) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 2, 1),
(4, 2, 3),
(5, 3, 1);
```


## RESTfull сервіс для управління даними
Цей RESTful сервіс розроблений із застосуванням Flask та SQLAlchemy, що дозволяє створювати масштабовані веб-додатки для управління даними. Сервіс забезпечує простоту створення API для операцій CRUD з базою даних і реалізує основні функції для управління користувачами, проектами та завданнями. Ось основні компоненти цього сервісу:

**Flask**:
Flask — це мінімалістичний фреймворк для розробки веб-додатків на Python. Він забезпечує необхідні інструменти для швидкого створення веб-сервісів і API.  
Використовує Blueprints для організації коду в модульні компоненти, що полегшує масштабування та обслуговування.

**SQLAlchemy**:
SQLAlchemy — це ORM (Object-Relational Mapping) бібліотека для Python, що дозволяє працювати з базою даних за допомогою об'єктно-орієнтованих принципів.  
SQLAlchemy забезпечує гнучкість і простоту в роботі з базою даних. Він автоматично генерує SQL-запити на основі класів моделей, що значно спрощує код і знижує ймовірність помилок.  
Використовується для здійснення CRUD операцій, таких як додавання нових користувачів, оновлення даних і видалення записів.

**Flask Marshmallow**:  
Flask Marshmallow використовується для серіалізації і десеріалізації даних між Python об'єктами та JSON форматом. Це дозволяє автоматично перетворювати моделі SQLAlchemy в JSON для обміну даними між клієнтом і сервером.

**Swagger/OpenAPI**:  
Swagger використовується для автоматичної генерації документації RESTful API. Це дозволяє розробникам та користувачам швидко ознайомлюватися з доступними маршрутами API та їх параметрами.  
За допомогою Swagger UI можна тестувати API прямо з браузера, без необхідності використовувати додаткові інструменти (наприклад, Postman).

**Data Transfer Objects (DTO)**:  
DTO (Data Transfer Objects) використовуються для безпечної та організованої передачі даних між різними шарами додатку. Вони допомагають абстрагувати внутрішню структуру моделей і дозволяють контролювати, які саме дані будуть передаватися через API.  
DTO дозволяють захистити вашу внутрішню бізнес-логіку, створюючи чіткий інтерфейс для спілкування з клієнтами через API.

### Діаграма Класів 
![image](https://github.com/user-attachments/assets/b4ff8fce-ffd1-4f52-ab54-87c11332c42d)

### Головна вхідна точка для Flask додатку, конфігурація сервера і запуск API.
```py
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
```
### Контролер для обробки запитів, що стосуються користувачів (CRUD операції).
```py
from flask import jsonify, request, abort
from services.user_service import (
    get_all_users,
    get_user_by_id,
    create_new_user,
    update_user_data,
    delete_user_data
)

def get_users():
    users = get_all_users()
    return jsonify(users), 200

def get_user(user_id):
    user = get_user_by_id(user_id)
    if user is None:
        abort(404, description="User not found")
    return jsonify(user), 200

def create_user():
    data = request.get_json()
    if not data or not "username" in data or not "email" in data:
        abort(400, description="Missing required fields: username or email")
    new_user = create_new_user(data)
    return jsonify(new_user), 201

def update_user(user_id):
    data = request.get_json()
    updated_user = update_user_data(user_id, data)
    if not updated_user:
        abort(404, description="User not found")
    return jsonify(updated_user), 200

def delete_user(user_id):
    success = delete_user_data(user_id)
    if not success:
        abort(404, description="User not found")
    return jsonify({"message": "User deleted successfully"}), 200
```
### Сервіс для обробки бізнес-логіки, пов'язаної з користувачами.
```py
from repositories.user_repository import (
    get_all_users_from_db,
    get_user_from_db,
    add_user_to_db,
    update_user_in_db,
    remove_user_from_db
)

def get_all_users():
    return get_all_users_from_db()

def get_user_by_id(user_id):
    return get_user_from_db(user_id)

def create_new_user(data):
    return add_user_to_db(data)

def update_user_data(user_id, data):
    return update_user_in_db(user_id, data)

def delete_user_data(user_id):
    return remove_user_from_db(user_id)
```
### Репозиторій для взаємодії з таблицею користувачів у базі даних.
```py
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
```
### Data Transfer Object для користувача, забезпечує безпечний обмін даними між шарами додатку.
```py
class UserDTO:
    def __init__(self, name, email):
        self.name = name
        self.email = email
```
### Модель SQLAlchemy для користувачів, визначає структуру таблиці користувачів у базі даних.
```py
from database.db import db

class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    role = db.Column(db.String(50))
    isBanned = db.Column(db.Boolean, default=False)
```
### Маршрути API для доступу до різних функціональних частин додатку.
```py
from flask import Blueprint, request, jsonify, abort
from controllers.user_controller import get_users, create_user, get_user, update_user, delete_user

user_routes = Blueprint('users', __name__)

user_routes.route('/users', methods=['GET'])(get_users)
user_routes.route('/users', methods=['POST'])(create_user)
user_routes.route('/users/<int:user_id>', methods=['GET'])(get_user)
user_routes.route('/users/<int:user_id>', methods=['PUT'])(update_user)
user_routes.route('/users/<int:user_id>', methods=['DELETE'])(delete_user)
```
### Конфігурація з'єднання з базою даних і ініціалізація SQLAlchemy.
```py
from flask_sqlalchemy import SQLAlchemy

# Ініціалізація SQLAlchemy
db = SQLAlchemy()
```
