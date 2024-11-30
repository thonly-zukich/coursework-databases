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

