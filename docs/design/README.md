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

## ER-модель

@startuml

skinparam entity {
  BackgroundColor #f7f711
}

package UserManagement {
  entity User {
    id: UUID
    username: TEXT
    password: TEXT
    email: TEXT
    role: TEXT
    isBanned: BOOLEAN
  }
}

package ProjectManagement {
  entity Project {
    id: UUID
    title: TEXT
    description: TEXT
  }

  entity Board {
    id: UUID
    title: TEXT
  }

  entity Task {
    id: UUID
    title: TEXT
    description: TEXT
    deadline: DATETIME
    status: TEXT
  }

  entity Attachment {
    id: UUID
    format: TEXT
    content: BLOB
  }
}

package AccessControl {
  entity Member {
    id: UUID
  }

  entity Assignee {
    id: UUID
  }

  entity Grant {
    id: UUID
  }

  entity Permission {
    id: UUID
    action: TEXT
  }

  entity Label {
    id: UUID
  }

  entity Tag {
    id: UUID
    name: TEXT
    description: TEXT
  }
}

User "1,1" -d- "0,*" Member
Project "1,1" -d- "0,*" Member
Board "1,1" -d- "0,*" Task
Project "1,1" -d- "0,*" Board
Task "1,1" -u- "0,*" Attachment
Task "1,1" -d- "0,*" Assignee
Member "1,1" -d- "0,*" Assignee
Grant "0,*" -u- "1,1" Member
Grant "0,*" -u- "1,1" Permission
Tag "0,*" -d- "1,1" Task
Tag "0,*" -u- "1,1" Label

@enduml
