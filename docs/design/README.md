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

package UserAdministration {
    entity User {
        id: UUID
        nickname: TEXT
        email: TEXT
        password: TEXT
        photo: IMAGE
        isBanned: TINYINT
    }
}

entity Collaborator {
    id: NUMBER
}

entity Action {
    id: NUMBER
    datetime: DATETIME
}

entity Project {
    id: UUID
    name: TEXT
    description: TEXT
}

entity Team {
    id: NUMBER
    name: TEXT
    motto: TEXT
}

package AccessControl {
    enum Role {
        id: NUMBER
        name: TEXT
        description: TEXT
    }

    entity Permission {
        id: NUMBER
        action: TEXT
    }

    entity Grant {
        id: UUID
    }

    object developer
    object teamlead
    object administrator

    developer .u.> Role : instanceOf
    teamlead .u.> Role : instanceOf
    administrator .u.> Role : instanceOf
}

package TaskManagement {
    entity Assignment {
        id: NUMBER
        datetime: DATETIME
    }

    entity Task {
        id: NUMBER
        name: TEXT
        description: TEXT
        creationDate: DATETIME
        deadline: DATETIME
    }

    enum Tag {
        id: NUMBER
        name: TEXT
        description: TEXT
    }

    entity Label {
        id: UUID
    }

    entity Task_comment {
        id: NUMBER
        subject: TEXT
        text: TEXT
        datetime: DATETIME
    }

    entity Sprint {
        id: NUMBER
        name: TEXT
        goal: TEXT
        startdate: DATE
        enddate: DATE
    }
}

' Relationships
Action "0," -r-> "0,1" Collaborator
Action "0," -u-> "0,1" Sprint
Action "0," -u-> "0,1" Task
Action "0," -u-> "0,1" Assignment

Collaborator "0," -d-> "1,1" User
Team "1,1" -u-> "0," Collaborator
Team "0," -u-> "1,1" Project
Collaborator "0," --> "1,1" Role
Grant "0," -r-> "1,1" Role
Grant "0," -l-> "1,1" Permission
Assignment "0," -d-> "1,1" Collaborator
Assignment "0," -u-> "1,1" Task
Label "0," -d-> "1,1" Task
Label "0," -u-> "1,1" Tag
Task_comment "0," -d-> "1,1" Collaborator : author
Task_comment "0," -u-> "1,1" Task
Task "0," -l-> "1,1" Sprint
Sprint "0," -d-> "1,1" Project

@enduml
