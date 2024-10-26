# Модель прецедентів


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


<table>
    <tr>
        <th>ID</th>
        <th id="CreateUser"><code>CreateUser</code></th>
    </tr>
    <tr>
        <th>Назва</th>
        <td>Створити користувача</td>
    </tr>
    <tr>
        <th>Учасники</th>
        <td>Користувач, система</td>
    </tr>
    <tr>
        <th>Передумови</th>
        <td>Система не зареєструвала користувача</td>
    </tr>
    <tr>
        <th>Результат</th>
        <td>Система створює обліковий запис користувача</td>
    </tr>
    <tr>
        <th>Виключні ситуації</th>
        <td>
            <ul>
                <li>Користувач не ввів ім'я користувача (NullUsernameException)</li>
                <li>Користувач не ввів пошту (NullEmailException)</li>
                <li>Користувач не ввів пароль (NullPasswordException)</li>
                <li>Користувач з таким ім'ям вже існує (UserAlreadyExistsException)</li>
                <li>Користувач вказав неправильний формат пошти (WrongEmailFormatException)</li>
                <li>Користувач ввів недостатньо сильний пароль (менше 8 символів, не містить букв і цифр) (WeakPasswordException)</li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>Основний сценарій</th>
        <td>
            <ol>
                <li>Користувач натискає на кнопку "Зареєструватись"</li>
                <li>Користувач заповнює поля реєстрації (ім'я користувача, пошта, пароль)</li>
                <li>Користувач натискає на кнопку "Створити"</li>
                <li>Система перевіряє введені поля на валідність</li>
                <li>Система створює обліковий запис користувача</li>
                <li>Користувач автоматично входить в систему</li>
            </ol>
        </td>
    </tr>
</table>

<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;">

@startuml

|Користувач|
start;
: Натискає на кнопку "Зареєструватись";
: Заповнює поля реєстрації (ім'я користувача, пошта, пароль);
: Натискає на кнопку "Створити";

|Система|
: Перевіряє введені поля на валідність;
note right #ffaaaa
<b> Можливі виключення:
<b> NullUsernameException
<b> NullEmailException
<b> NullPasswordException
<b> UserAlreadyExistsException
<b> WrongEmailFormatException
<b> WeakPasswordException
end note
: Створює обліковий запис користувача;

|Користувач|
: Автоматично входить в систему;
stop;

@enduml

</center>

<table>
    <tr>
        <th>ID</th>
        <th id="AuthorizeUser"><code>AuthorizeUser</code></th>
    </tr>
    <tr>
        <th>Назва</th>
        <td>Авторизувати користувача</td>
    </tr>
    <tr>
        <th>Учасники</th>
        <td>Користувач, система</td>
    </tr>
    <tr>
        <th>Передумови</th>
        <td>Система зареєструвала користувача</td>
    </tr>
    <tr>
        <th>Результат</th>
        <td>Система авторизувала користувача</td>
    </tr>
    <tr>
        <th>Виключні ситуації</th>
        <td>
            <ul>
                <li>Користувач ввів неправильний пароль (InvalidPasswordException)</li>
                <li>Користувач ввів неправильне ім'я користувача (InvalidUsernameException)</li>
                <li>Система заблокувала користувача (UserBannedException)</li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>Основний сценарій</th>
        <td>
            <ol>
                <li>Користувач вводить ім'я користувача і пароль.</li>
                <li>Система перевіряє введені дані (можливе InvalidPasswordException або InvalidUsernameException)</li>
                <li>Система перевіряє статус користувача (можливе UserBannedException)</li>
                <li>Користувач успішно входить у систему</li>
            </ol>
        </td>
    </tr>
</table>

<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;">

@startuml

|Користувач|
start;
: Вводить ім'я користувача і пароль;

|Система|
: Перевіряє введені дані;

note right #ffaaaa
<b> Можливі виключення:
<b> InvalidPasswordException
<b> InvalidUsernameException
end note

: Перевіряє статус користувача;

note right #ffaaaa
<b> Можливе виключення:
<b> UserBannedException
end note

|Користувач|
: Успішно входить у систему;

stop;

@enduml

</center>


<table>
    <tr>
        <th>ID</th>
        <th id="EditUser"><code>EditUser</code></th>
    </tr>
    <tr>
        <th>Назва</th>
        <td>Редагувати користувача</td>
    </tr>
    <tr>
        <th>Учасники</th>
        <td>Користувач, адміністратор, система</td>
    </tr>
    <tr>
        <th>Передумови</th>
        <td>Система авторизувала користувача або адміністратора</td>
    </tr>
    <tr>
        <th>Результат</th>
        <td>Система змінила дані користувача</td>
    </tr>
    <tr>
        <th>Виключні ситуації</th>
        <td>
            <ul>
                <li>Система не знайшла користувача (UserNotFoundException)</li>
                <li>Користувач має недостатньо прав для редагування (InsufficientPermissionsException)</li>
                <li>Користувач ввів дані у неправильному форматі (InvalidDataFormatException)</li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>Основний сценарій</th>
        <td>
            <ol>
                <li>Адміністратор або користувач відкриває профіль користувача.</li>
                <li>Користувач або адміністратор змінює потрібні поля.</li>
                <li>Система перевіряє права (можливе InsufficientPermissionsException).</li>
                <li>Система перевіряє введені дані на правильність (можливе InvalidDataFormatException).</li>
                <li>Система зберігає оновлені дані користувача.</li>
            </ol>
        </td>
    </tr>
</table>

<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;">

@startuml

|Користувач|
start;
: Відкриває профіль користувача;

|Адміністратор|
: Змінює потрібні поля;

|Система|
: Перевіряє права;
note right #ffaaaa
<b> Можливе виключення:
<b> InsufficientPermissionsException
end note
: Перевіряє введені дані;
note right #ffaaaa
<b> Можливі виключення:
<b> InvalidDataFormatException
end note
: Зберігає оновлені дані користувача;
stop;

@enduml

</center>

<table>
    <tr>
        <th>ID</th>
        <th id="DeleteUser"><code>DeleteUser</code></th>
    </tr>
    <tr>
        <th>Назва</th>
        <td>Видалити користувача</td>
    </tr>
    <tr>
        <th>Учасники</th>
        <td>Адміністратор, система</td>
    </tr>
    <tr>
        <th>Передумови</th>
        <td>Система авторизувала адміністратора</td>
    </tr>
    <tr>
        <th>Результат</th>
        <td>Система видаляє користувача</td>
    </tr>
    <tr>
        <th>Виключні ситуації</th>
        <td>
            <ul>
                <li>Система не знайшла користувача (UserNotFoundException)</li>
                <li>Користувач має недостатньо прав для видалення (InsufficientPermissionsException)</li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>Основний сценарій</th>
        <td>
            <ol>
                <li>Адміністратор вибирає користувача для видалення.</li>
                <li>Адміністратор натискає кнопку "Видалити користувача".</li>
                <li>Система перевіряє права адміністратора (можливе InsufficientPermissionsException).</li>
                <li>Система видаляє користувача (можливе UserNotFoundException).</li>
            </ol>
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

|Адміністратор|
start;
: Вибирає користувача для видалення;

: Натискає на кнопку "Видалити користувача";

|Система|
: Перевіряє права адміністратора;

note right #ffaaaa
<b> Можливе виключення:
<b> InsufficientPermissionsException
end note

: Видаляє користувача;

note right #ffaaaa
<b> Можливе виключення:
<b> UserNotFoundException
end note

stop;

@enduml

</center>

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


<table>
    <tr>
        <th>ID</th>
        <th id="WriteToSupport"><code>WriteToSupport</code></th>
    </tr>
    <tr>
        <th>Назва</th>
        <td>Написати в службу підтримки</td>
    </tr>
    <tr>
        <th>Учасники</th>
        <td>Користувач, система</td>
    </tr>
    <tr>
        <th>Передумови</th>
        <td>Система авторизувала користувача</td>
    </tr>
    <tr>
        <th>Результат</th>
        <td>Система відправила повідомлення до служби підтримки</td>
    </tr>
    <tr>
        <th>Виключні ситуації</th>
        <td>Користувач не ввів текст повідомлення (NullInstanceException)</td>
    </tr>
    <tr>
        <th>Основний сценарій</th>
        <td>
            <ol>
                <li>Користувач відкриває форму для зв'язку зі службою підтримки.</li>
                <li>Користувач вводить текст повідомлення.</li>
                <li>Система перевіряє введені дані (можливе NullInstanceException).</li>
                <li>Система відправляє повідомлення до служби підтримки.</li>
                <li>Користувач отримує підтвердження про відправлення повідомлення.</li>
            </ol>
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
start
:Відкриває форму для зв'язку зі службою підтримки;
:Вводить текст повідомлення;

|Система|
:Перевіряє введені дані;
note right #ffaaaa
<b> Можлива виключна ситуація:
<b> NullInstanceException - користувач не ввів текст повідомлення
end note
:Відправляє повідомлення до служби підтримки;

|Користувач|
:Отримує підтвердження про відправлення повідомлення;
stop

@enduml

</center>

<table>
    <tr>
        <th>ID</th>
        <th id="CreateProject"><code>CreateProject</code></th>
    </tr>
    <tr>
        <th>Назва</th>
        <td>Створити проект</td>
    </tr>
    <tr>
        <th>Учасники</th>
        <td>Користувач, система</td>
    </tr>
    <tr>
        <th>Передумови</th>
        <td>Користувач авторизований</td>
    </tr>
    <tr>
        <th>Результат</th>
        <td>Система створює новий проект</td>
    </tr>
    <tr>
        <th>Виключні ситуації</th>
        <td>
            <ul>
                <li>Користувач не ввів назву проекту (NullProjectNameException)</li>
                <li>Користувач ввів неправильний формат назви (InvalidProjectNameException)</li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>Основний сценарій</th>
        <td>
            <ol>
                <li>Користувач натискає "Створити проект".</li>
                <li>Користувач заповнює необхідні поля для створення проекту.</li>
                <li>Користувач натискає кнопку "Створити".</li>
                <li>Система перевіряє дані.</li>
                <li>Система створює новий проект.</li>
            </ol>
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
: Натискає "Створити проект";

: Заповнює поля проекту;

: Натискає "Створити";

|Система|
: Перевіряє дані проекту;

note right #ffaaaa
<b> Можливі виключення:
<b> NullProjectNameException
<b> InvalidProjectNameException
end note

: Створює новий проект;

stop;

@enduml

</center>

<table>
    <tr>
        <th>ID</th>
        <th id="EditProject"><code>EditProject</code></th>
    </tr>
    <tr>
        <th>Назва</th>
        <td>Редагувати проект</td>
    </tr>
    <tr>
        <th>Учасники</th>
        <td>Користувач, система</td>
    </tr>
    <tr>
        <th>Передумови</th>
        <td>Користувач є учасником проекту</td>
    </tr>
    <tr>
        <th>Результат</th>
        <td>Проект успішно змінений</td>
    </tr>
    <tr>
        <th>Виключні ситуації</th>
        <td>
            <ul>
                <li>Користувач не має прав на редагування проекту (InsufficientPermissionsException)</li>
                <li>Невірний формат даних (InvalidDataFormatException)</li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>Основний сценарій</th>
        <td>
            <ol>
                <li>Користувач відкриває проект для редагування.</li>
                <li>Користувач змінює потрібні поля.</li>
                <li>Користувач натискає "Зберегти".</li>
                <li>Система перевіряє права доступу.</li>
                <li>Система зберігає зміни.</li>
            </ol>
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
: Відкриває проект для редагування;

: Змінює поля проекту;

: Натискає "Зберегти";

|Система|
: Перевіряє права доступу;

note right #ffaaaa
<b> Можливі виключення:
<b> InsufficientPermissionsException
<b> InvalidDataFormatException
end note

: Зберігає зміни проекту;

stop;

@enduml

</center>

<table>
    <tr>
        <th>ID</th>
        <th id="DeleteProject"><code>DeleteProject</code></th>
    </tr>
    <tr>
        <th>Назва</th>
        <td>Видалити проект</td>
    </tr>
    <tr>
        <th>Учасники</th>
        <td>Користувач, система</td>
    </tr>
    <tr>
        <th>Передумови</th>
        <td>Користувач має права на видалення проекту</td>
    </tr>
    <tr>
        <th>Результат</th>
        <td>Система видаляє проект</td>
    </tr>
    <tr>
        <th>Виключні ситуації</th>
        <td>
            <ul>
                <li>Користувач не має прав на видалення проекту (InsufficientPermissionsException)</li>
                <li>Проект не знайдено (ProjectNotFoundException)</li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>Основний сценарій</th>
        <td>
            <ol>
                <li>Користувач відкриває проект для видалення.</li>
                <li>Користувач натискає "Видалити".</li>
                <li>Система перевіряє права користувача.</li>
                <li>Система видаляє проект.</li>
            </ol>
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
: Відкриває проект для видалення;

: Натискає "Видалити";

|Система|
: Перевіряє права користувача;

note right #ffaaaa
<b> Можливі виключення:
<b> InsufficientPermissionsException
<b> ProjectNotFoundException
end note

: Видаляє проект;

stop;

@enduml

</center>



<table>
    <tr>
        <th>ID</th>
        <th id="AddMemberToProject"><code>AddMemberToProject</code></th>
    </tr>
    <tr>
        <th>Назва</th>
        <td>Додати учасника до проекту</td>
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
                <li>Користувач має права на редагування проекту</li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>Результат</th>
        <td>Система додає учасника до проєкту</td>
    </tr>
    <tr>
        <th>Виключні ситуації</th>
        <td>
            <ul>
                <li>Система не знайшла користувача (UserNotFoundException)</li>
                <li>Система не знайшла проєкт (ProjectNotFoundException)</li>
                <li>Користувач має недостатньо прав для додавання учасника (AccessDeniedException)</li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>Основний сценарій</th>
        <td>
            <ol>
                <li>Користувач відкриває проект.</li>
                <li>Користувач натискає кнопку "Додати учасника".</li>
                <li>Користувач вводить дані нового учасника.</li>
                <li>Система перевіряє права на додавання учасника.</li>
                <li>Система додає учасника до проекту.</li>
            </ol>
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

|Користувач (керівник проєкту)|
start
:Відкриває проект;
:Натискає кнопку "Додати учасника";
:Вводить дані нового учасника;

|Система|
:Перевіряє права на додавання учасника;
note right #ffaaaa
<b> Можливі виключні ситуації:
<b> UserNotFoundException - система не знайшла користувача
<b> ProjectNotFoundException - система не знайшла проєкт
<b> AccessDeniedException - недостатньо прав для додавання
end note
:Додає учасника до проекту;

|Користувач|
:Отримує підтвердження про успішне додавання учасника;
stop

@enduml

</center>


<table>
    <tr>
        <th>ID</th>
        <th id="RemoveMemberFromProject"><code>RemoveMemberFromProject</code></th>
    </tr>
    <tr>
        <th>Назва</th>
        <td>Видалити учасника з проекту</td>
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
                <li>Користувач має права на додавання учасників до проєкту</li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>Результат</th>
        <td>Система видаляє учасника з проєкту</td>
    </tr>
    <tr>
        <th>Виключні ситуації</th>
        <td>
            <ul>
                <li>Система не знайшла учасника (MemberNotFoundException)</li>
                <li>Система не знайшла проєкт (ProjectNotFoundException)</li>
                <li>Користувач має недостатньо прав для видалення учасника (AccessDeniedException)</li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>Основний сценарій</th>
        <td>
            <ol>
                <li>Користувач відкриває проект.</li>
                <li>Користувач вибирає учасника для видалення.</li>
                <li>Користувач натискає кнопку "Видалити".</li>
                <li>Система перевіряє права на видалення.</li>
                <li>Система видаляє учасника з проекту.</li>
            </ol>
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

|Користувач (керівник проєкту)|
start
:Відкриває проект;
:Вибирає учасника для видалення;
:Натискає кнопку "Видалити";

|Система|
:Перевіряє права на видалення;
note right #ffaaaa
<b> Можливі виключні ситуації:
<b> MemberNotFoundException - система не знайшла учасника
<b> ProjectNotFoundException - система не знайшла проєкт
<b> AccessDeniedException - недостатньо прав для видалення
end note
:Видаляє учасника з проекту;

|Користувач|
:Отримує підтвердження про успішне видалення учасника;
stop

@enduml

</center>



<table>
    <tr>
        <th>ID</th>
        <th id="CreateBoard"><code>CreateBoard</code></th>
    </tr>
    <tr>
        <th>Назва</th>
        <td>Створити дошку</td>
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
                <li>Користувач має права на створення дошки</li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>Результат</th>
        <td>Система створює дошку</td>
    </tr>
    <tr>
        <th>Виключні ситуації</th>
        <td>
            <ul>
                <li>Користувач не ввів назву дошки (NullInstanceException)</li>
                <li>Користувач ввів недопустиму назву дошки (InvalidBoardNameException)</li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>Основний сценарій</th>
        <td>
            <ol>
                <li>Користувач натискає кнопку "Створити дошку".</li>
                <li>Користувач вводить назву дошки (можливе NullInstanceException).</li>
                <li>Система перевіряє введені дані (можливе InvalidBoardNameException).</li>
                <li>Система створює нову дошку.</li>
                <li>Користувач отримує доступ до дошки.</li>
            </ol>
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

|Користувач (керівник проєкту)|
start;
: Натискає кнопку "Створити дошку";
: Вводить назву дошки;

|Система|
: Перевіряє введені дані;
note right #ffaaaa
<b> Можливі виключення:
<b> NullInstanceException
<b> InvalidBoardNameException
end note
: Створює нову дошку;

|Користувач|
: Отримує доступ до дошки;
stop;

@enduml

</center>

<table>
    <tr>
        <th>ID</th>
        <th id="EditBoard"><code>EditBoard</code></th>
    </tr>
    <tr>
        <th>Назва</th>
        <td>Редагувати дошку</td>
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
                <li>Користувач має права на редагування дошки</li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>Результат</th>
        <td>Система оновила дані дошки</td>
    </tr>
    <tr>
        <th>Виключні ситуації</th>
        <td>
            <ul>
                <li>Система не знайшла дошку (BoardNotFoundException)</li>
                <li>Користувач має недостатньо прав для редагування (AccessDeniedException)</li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>Основний сценарій</th>
        <td>
            <ol>
                <li>Користувач відкриває дошку.</li>
                <li>Користувач натискає кнопку "Редагувати".</li>
                <li>Користувач вносить зміни.</li>
                <li>Система перевіряє права на редагування (можливе AccessDeniedException).</li>
                <li>Система зберігає зміни.</li>
            </ol>
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

|Користувач (керівник проєкту)|
start;
: Відкриває дошку;
: Натискає кнопку "Редагувати";
: Вносить зміни;

|Система|
: Перевіряє права на редагування;
note right #ffaaaa
<b> Можливі виключення:
<b> AccessDeniedException
<b> BoardNotFoundException
end note
: Зберігає зміни;

|Користувач|
: Отримує оновлену дошку;
stop;

@enduml

</center>

<table>
    <tr>
        <th>ID</th>
        <th id="DeleteBoard"><code>DeleteBoard</code></th>
    </tr>
    <tr>
        <th>Назва</th>
        <td>Видалити дошку (Delete Board)</td>
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
                <li>Користувач має права на видалення дошки</li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>Результат</th>
        <td>Система видаляє дошку</td>
    </tr>
    <tr>
        <th>Виключні ситуації</th>
        <td>
            <ul>
                <li>Система не знайшла дошку (BoardNotFoundException)</li>
                <li>Користувач має недостатньо прав для видалення (AccessDeniedException)</li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>Основний сценарій</th>
        <td>
            <ol>
                <li>Користувач відкриває дошку.</li>
                <li>Користувач натискає кнопку "Видалити".</li>
                <li>Система перевіряє права на видалення (можливе AccessDeniedException).</li>
                <li>Система видаляє дошку.</li>
                <li>Користувач отримує підтвердження про успішне видалення.</li>
            </ol>
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

|Користувач (керівник проєкту)|
start;
: Відкриває дошку;
: Натискає кнопку "Видалити";

|Система|
: Перевіряє права на видалення;
note right #ffaaaa
<b> Можливі виключення:
<b> AccessDeniedException
<b> BoardNotFoundException
end note
: Видаляє дошку;

|Користувач|
: Отримує підтвердження про видалення;
stop;

@enduml

</center>

<table>
    <tr>
        <th>ID</th>
        <th id="BanUser"><code>BanUser</code></th>
    </tr>
    <tr>
        <th>Назва</th>
        <td>Заборонити користувача</td>
    </tr>
    <tr>
        <th>Учасники</th>
        <td>Адміністратор, користувач, система</td>
    </tr>
    <tr>
        <th>Передумови</th>
        <td>
            <ul>
                <li>Система авторизувала адміністратора</li>
                <li>Система не заборонила користувача</li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>Результат</th>
        <td>Система забороняє доступ користувачу</td>
    </tr>
    <tr>
        <th>Виключні ситуації</th>
        <td>
            <ul>
                <li>Система не знайшла користувача (UserNotFoundException)</li>
                <li>Адміністратор має недостатньо прав для заборони (InsufficientPermissionsException)</li>
                <li>Система вже заборонила користувача (UserBannedException)</li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>Основний сценарій</th>
        <td>
            <ol>
                <li>Адміністратор вибирає користувача зі списку.</li>
                <li>Адміністратор натискає кнопку "Заборонити користувача".</li>
                <li>Система перевіряє права адміністратора (можливе InsufficientPermissionsException).</li>
                <li>Система перевіряє користувача на заборону (можливе UserBannedException).</li>
                <li>Система забороняє користувача (можливе UserNotFoundException).</li>
                <li>Користувач отримує повідомлення про заборону.</li>
            </ol>
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

|Адміністратор|
start;
: Вибирає користувача зі списку;

: Натискає "Заборонити користувача";

|Система|
: Перевіряє права адміністратора;

note right #ffaaaa
<b> Можливе виключення:
<b> InsufficientPermissionsException
end note

: Перевіряє, чи користувач вже заборонений;

note right #ffaaaa
<b> Можливе виключення:
<b> UserBannedException
end note

: Забороняє користувача;

note right #ffaaaa
<b> Можливе виключення:
<b> UserNotFoundException
end note

|Користувач|
: Отримує повідомлення про заборону;

stop;

@enduml

</center>


<table>
    <tr>
        <th>ID</th>
        <th id="UnbanUser"><code>UnbanUser</code></th>
    </tr>
    <tr>
        <th>Назва</th>
        <td>Дозволити користувача</td>
    </tr>
    <tr>
        <th>Учасники</th>
        <td>Адміністратор, користувач, система</td>
    </tr>
    <tr>
        <th>Передумови</th>
        <td>
            <ul>
                <li>Система авторизувала користувача</li>
                <li>Система заборонила доступ користувачу</li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>Результат</th>
        <td>Система дозволяє доступ користувачу</td>
    </tr>
    <tr>
        <th>Виключні ситуації</th>
        <td>
            <ul>
                <li>Система не знайшла користувача (UserNotFoundException)</li>
                <li>Адміністратор має недостатньо прав для дозволення (InsufficientPermissionsException)</li>
                <li>Система не заборонила доступ користувачу (UserNotBannedException)</li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>Основний сценарій</th>
        <td>
            <ol>
                <li>Адміністратор вибирає забороненого користувача зі списку.</li>
                <li>Адміністратор натискає кнопку "Дозволити користувача".</li>
                <li>Система перевіряє права адміністратора (можливе InsufficientPermissionsException).</li>
                <li>Система перевіряє користувача на заборону (можливе UserNotBannedException).</li>
                <li>Система дозволяє користувача.</li>
                <li>Користувач отримує повідомлення про дозвіл.</li>
            </ol>
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

|Адміністратор|
start;
: Вибирає забороненого користувача зі списку;

: Натискає "Дозволити користувача";

|Система|
: Перевіряє права адміністратора;

note right #ffaaaa
<b> Можливе виключення:
<b> InsufficientPermissionsException
end note

: Перевіряє, чи користувач заборонений;



note right #ffaaaa
<b> Можливе виключення:
<b> UserNotBannedException
end note

: Дозволяє користувача;

note right #ffaaaa
<b> Можливе виключення:
<b> UserNotFoundException
end note

|Користувач|
: Отримує повідомлення про дозвіл;

stop;

@enduml

</center>


<table>
    <tr>
        <th>ID</th>
        <th id="SupportAnswer"><code>SupportAnswer</code></th>
    </tr>
    <tr>
        <th>Назва</th>
        <td>Відповісти у технічній підтримці</td>
    </tr>
    <tr>
        <th>Учасники</th>
        <td>Адміністратор, користувач, система</td>
    </tr>
    <tr>
        <th>Передумови</th>
        <td>Система авторизувала адміністратора</td>
    </tr>
    <tr>
        <th>Результат</th>
        <td>Система відправляє відповідь користувачу</td>
    </tr>
    <tr>
        <th>Виключні ситуації</th>
        <td>
            <ul>
                <li>Адміністратор не ввів текст відповіді (NullAnswerException)</li>
                <li>Користувача не знайдено (UserNotFoundException)</li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>Основний сценарій</th>
        <td>
            <ol>
                <li>Адміністратор відкриває питання користувача у службі підтримки.</li>
                <li>Адміністратор вводить текст відповіді.</li>
                <li>Система перевіряє введені дані (можливе NullAnswerException).</li>
                <li>Система відправляє відповідь користувачу (можливе UserNotFoundException).</li>
                <li>Користувач отримує повідомлення з відповіддю.</li>
            </ol>
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

|Адміністратор|
start;
: Відкриває питання користувача у службі підтримки;

: Вводить текст відповіді;

|Система|
: Перевіряє текст відповіді;

note right #ffaaaa
<b> Можливе виключення:
<b> NullAnswerException
end note

: Відправляє відповідь користувачу;

note right #ffaaaa
<b> Можливе виключення:
<b> UserNotFoundException
end note

|Користувач|
: Отримує повідомлення з відповіддю;

stop;

@enduml

</center>