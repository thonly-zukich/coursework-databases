# Проєктування бази даних


## Модель бізнес-об'єктів

@startuml

entity User #green
entity Project #green
entity Task #green
entity Board #green
entity Member #blue
entity Grant #blue
entity Permission #green
entity Attachment #green
entity Assignee #blue
entity Tag #blue
entity Label #green

entity User.username
entity User.password
entity User.email
entity User.role
entity User.isBanned

entity Task.title
entity Task.description
entity Task.deadline
entity Task.status

entity Board.title

entity Project.title
entity Project.description

entity Attachment.content
entity Attachment.format


User.username --* User
User.password --* User
User.email --* User
User.role --* User
User.isBanned --* User
User "1, 1" -- "0, *" Member

Task.title --* Task
Task.description --* Task
Task.deadline --* Task
Task.status --* Task
Task "1, 1" -- "0, *" Attachment
Task "1, 1" -- "0, *" Assignee

Attachment.format --* Attachment
Attachment.content --* Attachment

Board.title --* Board
Board "1, 1" -- "0, *" Task

Project.title --* Project
Project.description --* Project
Project "1, 1" -- "0, *" Member
Project "1, 1" -- "0, *" Board

Member "1, 1" -- "0, *" Assignee

Grant "0, *" -- "1, 1" Member
Grant "0, *" -- "1, 1" Permission

Tag "0, *" -- "1, 1" Label
Tag "0, *" -- "1, 1" Task

@enduml