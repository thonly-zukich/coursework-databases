# Модель прецедентів

В цьому файлі необхідно перелічити всі документи, розроблені в проекті та дати посилання на них.

*Модель прецедентів повинна містити загальні оглядові діаграми та специфікації прецедентів.*



Вбудовування зображень діаграм здійснюється з використанням сервісу [plantuml.com](https://plantuml.com/). 

В markdown-файлі використовується опис діаграми

```md

<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;"
>

@startuml

    right header
        <font size=24 color=black>Package: <b>UCD_3.0
    end header

    title
        <font size=18 color=black>UC_8. Редагувати конфігурацію порталу
        <font size=16 color=black>Діаграма прецедентів
    end title


    actor "Користувач" as User #eeeeaa
    
    package UCD_1{
        usecase "<b>UC_1</b>\nПереглянути список \nзвітів" as UC_1 #aaeeaa
    }
    
    usecase "<b>UC_1.1</b>\nЗастосувати фільтр" as UC_1.1
    usecase "<b>UC_1.2</b>\nПереглянути метадані \nзвіту" as UC_1.2  
    usecase "<b>UC_1.2.1</b>\nДати оцінку звіту" as UC_1.2.1  
    usecase "<b>UC_1.2.2</b>\nПереглянути інформацію \nпро авторів звіту" as UC_1.2.2
    
    package UCD_1 {
        usecase "<b>UC_4</b>\nВикликати звіт" as UC_4 #aaeeaa
    }
    
    usecase "<b>UC_1.1.1</b>\n Використати \nпошукові теги" as UC_1.1.1  
    usecase "<b>UC_1.1.2</b>\n Використати \nрядок пошуку" as UC_1.1.2
    usecase "<b>UC_1.1.3</b>\n Використати \nавторів" as UC_1.1.3  
    
    
    
    User -> UC_1
    UC_1.1 .u.> UC_1 :extends
    UC_1.2 .u.> UC_1 :extends
    UC_4 .d.> UC_1.2 :extends
    UC_1.2 .> UC_1.2 :extends
    UC_1.2.1 .u.> UC_1.2 :extends
    UC_1.2.2 .u.> UC_1.2 :extends
    UC_1 ..> UC_1.2.2 :extends
    
    
    UC_1.1.1 -u-|> UC_1.1
    UC_1.1.2 -u-|> UC_1.1
    UC_1.1.3 -u-|> UC_1.1
    
    right footer
        Аналітичний портал. Модель прецедентів.
        НТУУ КПІ ім.І.Сікорського
        Киів-2020
    end footer

@enduml

**Діаграма прецедентів**

</center>
```

яка буде відображена наступним чином

<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;"
>

@startuml

    right header
        <font size=24 color=black>Package: <b>UCD_3.0
    end header

    title
        <font size=18 color=black>UC_8. Редагувати конфігурацію порталу
        <font size=16 color=black>Діаграма прецедентів
    end title


    actor "Користувач" as User #eeeeaa
    
    package UCD_1{
        usecase "<b>UC_1</b>\nПереглянути список \nзвітів" as UC_1 #aaeeaa
    }
    
    usecase "<b>UC_1.1</b>\nЗастосувати фільтр" as UC_1.1
    usecase "<b>UC_1.2</b>\nПереглянути метадані \nзвіту" as UC_1.2  
    usecase "<b>UC_1.2.1</b>\nДати оцінку звіту" as UC_1.2.1  
    usecase "<b>UC_1.2.2</b>\nПереглянути інформацію \nпро авторів звіту" as UC_1.2.2
    
    package UCD_1 {
        usecase "<b>UC_4</b>\nВикликати звіт" as UC_4 #aaeeaa
    }
    
    usecase "<b>UC_1.1.1</b>\n Використати \nпошукові теги" as UC_1.1.1  
    usecase "<b>UC_1.1.2</b>\n Використати \nрядок пошуку" as UC_1.1.2
    usecase "<b>UC_1.1.3</b>\n Використати \nавторів" as UC_1.1.3  
    
    
    
    User -> UC_1
    UC_1.1 .u.> UC_1 :extends
    UC_1.2 .u.> UC_1 :extends
    UC_4 .d.> UC_1.2 :extends
    UC_1.2 .> UC_1.2 :extends
    UC_1.2.1 .u.> UC_1.2 :extends
    UC_1.2.2 .u.> UC_1.2 :extends
    UC_1 ..> UC_1.2.2 :extends
    
    
    UC_1.1.1 -u-|> UC_1.1
    UC_1.1.2 -u-|> UC_1.1
    UC_1.1.3 -u-|> UC_1.1
    
    right footer
        Аналітичний портал. Модель прецедентів.
        НТУУ КПІ ім.І.Сікорського
        Киів-2020
    end footer

@enduml

**Діаграма прецедентів**

</center>


## Загальна схема

<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;"
>

@startuml

:Користувач: as User
:Керівник проєкту: as Leader
:Адміністратор: as Admin

usecase "<b>UserManage</b>\nКерувати користувачем" as UserManage
usecase "<b>TaskManage</b>\nКерувати задачами" as TaskManage
usecase "<b>SupportWrite</b>\nНаписати в підтримку" as SupportWrite
usecase "<b>ProjectManage</b>\nКерувати проєктом" as ProjectManage
usecase "<b>TeamManage</b>\nКерувати командою" as TeamManage
usecase "<b>BoardManage</b>\nКерувати дошкою" as BoardManage
usecase "<b>SupportAnswer</b>\nВідповісти в підтримці" as SupportAnswer
usecase "<b>SystemManage</b>\nКерувати системою" as SystemManage

User -up-> UserManage
User -left-> TaskManage
User -right-> SupportWrite

User <|-- Leader

Leader -left-> ProjectManage
Leader -right-> TeamManage
Leader -down-> BoardManage

Leader <|-- Admin

Admin -down-> SupportAnswer
Admin -down-> SystemManage

@enduml

</center>

## Користувач

<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;"
>

@startuml

:Користувач: as User

usecase "<b>UserManage</b>\nКерувати користувачем" as UserManage
usecase "<b>TaskManage</b>\nКерувати задачами" as TaskManage
usecase "<b>SupportWrite</b>\nНаписати в підтримку" as SupportWrite
usecase "<b>UserCreate</b>\nЗареєструватись" as UserCreate
usecase "<b>UserAuthorize</b>\nАвторизуватись" as UserAuthorize
usecase "<b>UserEdit</b>\nРедагувати користувача" as UserEdit
usecase "<b>UserDelete</b>\nВидалити користувача" as UserEdit
usecase "<b>TaskCreate</b>\nСтворити задачу" as TaskCreate
usecase "<b>TaskEdit</b>\nРедагувати задачу" as TaskEdit
usecase "<b>TaskDelete</b>\nВидалити задачу" as TaskDelete
usecase "<b>TaskSort</b>\nВідсортувати задачі" as TaskSort

User -up-> UserManage
User -left-> TaskManage
User -right-> SupportWrite

TaskCreate .up.> TaskManage : extends
TaskEdit .right.> TaskManage : extends
TaskDelete .up.> TaskManage : extends
TaskSort .down.> TaskManage : extends

UserCreate .down.> UserManage : extends
UserAuthorize .down.> UserManage : extends
UserEdit .down.> UserManage : extends


@enduml

</center>

## Керівник проєкту

<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;"
>

@startuml

:Керівник проєкту: as Leader

usecase "<b>ProjectManage</b>\nКерувати проєктом" as ProjectManage
usecase "<b>TeamManage</b>\nКерувати командою" as TeamManage
usecase "<b>BoardManage</b>\nКерувати дошкою" as BoardManage
usecase "<b>ProjectCreate</b>\nСтворити проєкт" as ProjectCreate
usecase "<b>ProjectEdit</b>\nРедагувати проєкт" as ProjectEdit
usecase "<b>ProjectDelete</b>\nВидалити проєкт" as ProjectDelete
usecase "<b>MemberAdd</b>\nДодати учасника" as MemberAdd
usecase "<b>MemberRemove</b>\nВидалити учасника" as MemberRemove
usecase "<b>BoardCreate</b>\nСтворити дошку" as BoardCreate
usecase "<b>BoardEdit</b>\nРедагувати дошку" as BoardEdit
usecase "<b>BoardDelete</b>\nВидалити дошку" as BoardDelete

Leader -left-> ProjectManage
Leader -right-> TeamManage
Leader -down-> BoardManage

ProjectCreate .right.> ProjectManage : extends
ProjectEdit .down.> ProjectManage : extends
ProjectDelete .up.> ProjectManage : extends

MemberAdd .up.> TeamManage : extends
MemberRemove .down.> TeamManage : extends

BoardCreate .up.> BoardManage : extends
BoardEdit .up.> BoardManage : extends
BoardDelete .up.> BoardManage : extends


@enduml

</center>

## Адміністратор

<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;"
>

@startuml

:Адміністратор: as Admin

usecase "<b>SupportAnswer</b>\nВідповісти в підтримці" as SupportAnswer
usecase "<b>SystemManage</b>\nКерувати системою" as SystemManage
usecase "<b>UserBan</b>\nЗаборонити користувача" as UserBan
usecase "<b>UserUnban</b>\nДозволити користувача" as UserUnban

Admin -down-> SupportAnswer
Admin -down-> SystemManage

UserBan .up.> SystemManage : extends
UserUnban .up.> SystemManage : extends

@enduml

</center>


## Сценарії використання

В діаграмі діяльності має бути алгоритм виконання сценарію використання (див. "Основний сценарій" у характеристиці бізнес-процесів)  

Шаблон для таблиці:

<table>
    <tr>
        <th>ID</th>
        <th>
            <code>
            </code>
        </th>
    </tr>
    <tr>
        <th>Назва</th>
        <td></td>
    </tr>
    <tr>
        <th>Учасники</th>
        <td></td>
    </tr>
    <tr>
        <th>Передумови</th>
        <td></td>
    </tr>
    <tr>
        <th>Результат</th>
        <td></td>
    </tr>
    <tr>
        <th>Виключні ситуації</th>
        <td></td>
    </tr>
</table>

<table>
    <tr>
        <th>ID</th>
        <th id="CreateTask"><code>CreateTask</code></th>
    </tr>
    <tr>
        <th>Назва</th>
        <td>Створити задачу</td>
    </tr>
    <tr>
        <th>Учасники</th>
        <td>Користувач (керівник проєкту), адміністратор, система</td>
    </tr>
    <tr>
        <th>Передумови</th>
        <td>
            <ul>
                <li>Система авторизувала користувача</li>
                <li>Користувач має права на редагування проєкту</li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>Результат</th>
        <td>Система створює задачу</td>
    </tr>
    <tr>
        <th>Виключні ситуації</th>
        <td>
            <ul>
                <li>Користувач не ввів назву задачі (NullTaskNameException)</li>
                <li>Користувач ввів назву задачі у неправильному форматі (InvalidTaskNameException)</li>
                <li>Користувач має недостатньо прав для створення задачі (AccessDeniedException)</li>
            </ul>
        </td>
    </tr>
</table>
<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;"
>

@startuml

|Користувач| 
start; 
:Обирає проєкт і натискає на кнопку\n"Створити задачу";

|Система| 
:Відкриває форму із полями\nінформації про задачу;

|Користувач| 
:Заповнює поля інформації про задачу:\nвказує назву, дедлайн, виконавця, статус,\nтеги, додає файли; 
:Натискає кнопку "Створити";

|Система| 
:Перевіряє на валідність інформацію про задачу;
note right #ffaaaa
<b>Можлива
<b> NoEssentialDataException
end note


|Користувач| 
stop;

@enduml


</center>

<table>
    <tr>
        <th>ID</th>
        <th id="EditTask"><code>EditTask</code></th>
    </tr>
    <tr>
        <th>Назва</th>
        <td>Редагувати задачу</td>
    </tr>
    <tr>
        <th>Учасники</th>
        <td>Користувач (керівник проєкту), адміністратор, система</td>
    </tr>
    <tr>
        <th>Передумови</th>
        <td>
            <ul>
                <li>Система авторизувала користувача</li>
                <li>Користувач має права на редагування задачі</li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>Результат</th>
        <td>Система змінює дані задачі</td>
    </tr>
    <tr>
        <th>Виключні ситуації</th>
        <td>
            <ul>
                <li>Система не знайшла задачу (TaskNotFoundException)</li>
                <li>Користувач має недостатньо прав для редагування (AccessDeniedException)</li>
            </ul>
        </td>
    </tr>
</table>
<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;"
>

@startuml

|Користувач| 
start; 
:Обирає задачу і натискає на кнопку\n"Редагувати";

|Система| 
:Відкриває форму із полями\nінформації про задачу;

|Користувач| 
:Заповнює поля інформації про задачу:\nвказує назву, дедлайн, виконавця, статус,\nтеги, додає файли; 
:Натискає кнопку "Редагувати";
note right #ffaaaa
<b>Можлива
<b>TaskNotFoundException
end note

|Система| 
:Перевіряє на валідність інформацію про задачу; 
note right #ffaaaa
<b>Можлива
<b>NoEssentialDataException
end note

:Зберігає зміни у базі даних;

|Користувач| 
stop;

@enduml

</center>
<table>
    <tr>
        <th>ID</th>
        <th id="DeleteTask"><code>DeleteTask</code></th>
    </tr>
    <tr>
        <th>Назва</th>
        <td>Видалити задачу</td>
    </tr>
    <tr>
        <th>Учасники</th>
        <td>Користувач (керівник проєкту), адміністратор, система</td>
    </tr>
    <tr>
        <th>Передумови</th>
        <td>
            <ul>
                <li>Система авторизувала користувача</li>
                <li>Користувач має права на видалення задачі</li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>Результат</th>
        <td>Система видаляє задачу</td>
    </tr>
    <tr>
        <th>Виключні ситуації</th>
        <td>
            <ul>
                <li>Система не знайшла задачу (TaskNotFoundException)</li>
                <li>Користувач має недостатньо прав для видалення (AccessDeniedException)</li>
            </ul>
        </td>
    </tr>
</table>
<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;"
>

@startuml

|Користувач| 
start; 
:Обирає задачу і натискає на кнопку\n"Видалити";

|Система| 
:Перевіряє права на видалення задачі;
note right #ffaaaa
<b>Можлива
<b>InsufficientPermissionsException
end note
:Видаляє задачу з бази даних;

|Користувач| 
stop;

@enduml

</center>
<table>
    <tr>
        <th>ID</th>
        <th id="SortTasks"><code>SortTasks</code></th>
    </tr>
    <tr>
        <th>Назва</th>
        <td>Відсортувати задачі</td>
    </tr>
    <tr>
        <th>Учасники</th>
        <td>Користувач, система</td>
    </tr>
    <tr>
        <th>Передумови</th>
        <td>
            <ul>
                <li>Система авторизувала користувача</li>
                <li>Користувач є учасником проєкту</li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>Результат</th>
        <td>Система відсортовує список задач</td>
    </tr>
    <tr>
        <th>Виключні ситуації</th>
        <td>
            <ul>
                <li>Система не знайшла задачі (TasksNotFoundException)</li>
                <li>Користувач не є учасником проєкту (UserNotProjectMemberException)</li>
            </ul>
        </td>
    </tr>
</table>
<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;"
>

@startuml

|Користувач| 
start; 
:Обирає список задач і натискає на кнопку\n"Відсортувати";

|Система| 
:Перевіряє користувача на причасність до проєкту;
note right #ffaaaa
<b>Можлива
<b>UserNotProjectMemberException
end note
|Система| 
:Відсортує список задач;

|Користувач| 
stop;

@enduml

</center>