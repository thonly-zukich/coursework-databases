# Запити зацікавлених осіб

## Вступ

*[Вступ повинен містити короткий огляд всього документу.]*

### Мета 

*[Визначення мети цієї сукупності вимог. Зазвичай такою метою є створення та впровадження 
 інформаційної системи відповідного призначення.]*

### Контекст

*[Короткий опис того, з якими проектами пов'язаний цей документ, на що він впливає.]*


### Основні визначення та скорочення

*[Розділ містить визначення всіх термінів та скорочень, необхідних для правильного
тлумачення вимог. Можна зробити посилання на документ, в якому поданий аналіз предметної області.]*


### Посилання

*[Розділ містить повний список всіх документів, про які згадується.]*


## Короткий зміст

* [Характеристика ділових процесів](#характеристика-ділових-процесів)  
    * [Sing up User](#SignUpUser)  
    * [Log in User](#LogInUser)  
    * [Edit User](#EditUser)  
    * [Delete User](#DeleteUser)  
    * [Create Project](#CreateUser)  
    * [Edit Project](#EditProject)  
    * [Delete Project](#DeleteProject)  
    * [Add Member to Project](#AddMemberToProject)  
    * [Remove Member from Project](#RemoveMemberFromProject)   
    * [Create Board](#CreateBoard)  
    * [Edit Board](#EditBoard)  
    * [Delete Board](#DeleteBoard)   
    * [Create Task](#CreateTask)  
    * [Edit Task](#EditTask)  
    * [Delete Task](#DeleteTask)   
    * [Ban User](#BanUser)  
    * [Unban User](#UnbanUser)   
    * [Write to Support](#WriteToSupport) 
 * [Короткий огляд продукту](#короткий-огляд-продукту)
 * [Функціональність](#функціональність)
    * [Інтерфейс звичайного користувача](#інтерфейс-звичайного-користувача)
    * [Інтерфейс керівника проєкту](#інтерфейс-керівника-проєкту)
    * [Інтерфейс адміністратора](#інтерфейс-адміністратора)
* [Практичність](#практичність)
* [Надійність](#надійність)
* [Продуктивність](#продуктивність)
* [Експлуатаційна придатність](#експлуатаційна-придатність)

## Характеристика ділових процесів

*[В цьому розділі визначаються зовнішні фактори, що впливають на бізнес (бізнес-актори), 
та внутрішні фактори (робітники), дається загальна характеристика діяльності бізнес-акторів 
та робітників, яка здійснюється за допомогою бізнесу.*

Бізнес-актори:  
Керівник проєкту  
Учасник проєкту  

Бізнес-робітники:  
Адміністратор  




<table>
    <tr>
        <th>ID</th>
        <th id="SignUpUser"><code>SignUpUser</code></th>
    </tr>
    <tr>
        <td>Назва</td>
        <td>Створити користувача</td>
    </tr>
    <tr>
        <td>Учасники</td>
        <td>Користувач, система</td>
    </tr>
    <tr>
        <td>Передумови</td>
        <td>Користувач не зареєстрований в системі</td>
    </tr>
    <tr>
        <td>Результат</td>
        <td>Створення облікового запису користувача</td>
    </tr>
    <tr>
        <td>Виключні ситуації</td>
        <td>
            <ul>
                <li>Не введене ім'я користувача (NullUsernameException)</li>
                <li>Не введена пошта (NullEmailException)</li>
                <li>Не введений пароль (NullPasswordException)</li>
                <li>Користувач з таким ім'ям вже існує (UserAlreadyExistsException)</li>
                <li>Вказаний неправильний формат пошти (WrongEmailFormatException)</li>
                <li>Пароль недостатньо сильний (менше 8 символів, не містить букв і цифр) (WeakPasswordException)</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>Основний сценарій</td>
        <td>
            <ol>
                <li>Користувач натискає на кнопку "Зареєструватись"</li>
                <li>Користувач заповнює поля реєстрації (ім'я користувача, пошта, пароль)</li>
                <li>Система перевіряє введені поля на валідність</li>
                <li>Користувач натискає на кнопку "Створити"</li>
                <li>Система створює обліковий запис користувача</li>
                <li>Користувач автоматично входить в систему</li>
            </ol>
        </td>
    </tr>
</table>



<table>
    <tr>
        <th>ID</th>
        <th id="LogInUser"><code>LogInUser</code></th>
    </tr>
    <tr>
        <td>Назва</td>
        <td></td>
    </tr>
    <tr>
        <td>Учасники</td>
        <td></td>
    </tr>
    <tr>
        <td>Передумови</td>
        <td></td>
    </tr>
    <tr>
        <td>Результат</td>
        <td></td>
    </tr>
    <tr>
        <td>Виключні ситуації</td>
        <td></td>
    </tr>
    <tr>
        <td>Основний сценарій</td>
        <td></td>
    </tr>
</table>



<table>
    <tr>
        <th>ID</th>
        <th id="EditUser"><code>EditUser</code></th>
    </tr>
    <tr>
        <td>Назва</td>
        <td></td>
    </tr>
    <tr>
        <td>Учасники</td>
        <td></td>
    </tr>
    <tr>
        <td>Передумови</td>
        <td></td>
    </tr>
    <tr>
        <td>Результат</td>
        <td></td>
    </tr>
    <tr>
        <td>Виключні ситуації</td>
        <td></td>
    </tr>
    <tr>
        <td>Основний сценарій</td>
        <td></td>
    </tr>
</table>



<table>
    <tr>
        <th>ID</th>
        <th id="DeleteUser"><code>DeleteUser</code></th>
    </tr>
    <tr>
        <td>Назва</td>
        <td></td>
    </tr>
    <tr>
        <td>Учасники</td>
        <td></td>
    </tr>
    <tr>
        <td>Передумови</td>
        <td></td>
    </tr>
    <tr>
        <td>Результат</td>
        <td></td>
    </tr>
    <tr>
        <td>Виключні ситуації</td>
        <td></td>
    </tr>
    <tr>
        <td>Основний сценарій</td>
        <td></td>
    </tr>
</table>



<table>
    <tr>
        <th>ID</th>
        <th id="CreateProject"><code>CreateProject</code></th>
    </tr>
    <tr>
        <td>Назва</td>
        <td></td>
    </tr>
    <tr>
        <td>Учасники</td>
        <td></td>
    </tr>
    <tr>
        <td>Передумови</td>
        <td></td>
    </tr>
    <tr>
        <td>Результат</td>
        <td></td>
    </tr>
    <tr>
        <td>Виключні ситуації</td>
        <td></td>
    </tr>
    <tr>
        <td>Основний сценарій</td>
        <td></td>
    </tr>
</table>



<table>
    <tr>
        <th>ID</th>
        <th id="EditProject"><code>EditProject</code></th>
    </tr>
    <tr>
        <td>Назва</td>
        <td></td>
    </tr>
    <tr>
        <td>Учасники</td>
        <td></td>
    </tr>
    <tr>
        <td>Передумови</td>
        <td></td>
    </tr>
    <tr>
        <td>Результат</td>
        <td></td>
    </tr>
    <tr>
        <td>Виключні ситуації</td>
        <td></td>
    </tr>
    <tr>
        <td>Основний сценарій</td>
        <td></td>
    </tr>
</table>



<table>
    <tr>
        <th>ID</th>
        <th id="DeleteProject"><code>DeleteProject</code></th>
    </tr>
    <tr>
        <td>Назва</td>
        <td></td>
    </tr>
    <tr>
        <td>Учасники</td>
        <td></td>
    </tr>
    <tr>
        <td>Передумови</td>
        <td></td>
    </tr>
    <tr>
        <td>Результат</td>
        <td></td>
    </tr>
    <tr>
        <td>Виключні ситуації</td>
        <td></td>
    </tr>
    <tr>
        <td>Основний сценарій</td>
        <td></td>
    </tr>
</table>



<table>
    <tr>
        <th>ID</th>
        <th id="AddMemberToProject"><code>AddMemberToProject</code></th>
    </tr>
    <tr>
        <td>Назва</td>
        <td></td>
    </tr>
    <tr>
        <td>Учасники</td>
        <td></td>
    </tr>
    <tr>
        <td>Передумови</td>
        <td></td>
    </tr>
    <tr>
        <td>Результат</td>
        <td></td>
    </tr>
    <tr>
        <td>Виключні ситуації</td>
        <td></td>
    </tr>
    <tr>
        <td>Основний сценарій</td>
        <td></td>
    </tr>
</table>



<table>
    <tr>
        <th>ID</th>
        <th id="RemoveMemberFromProject"><code>RemoveMemberFromProject</code></th>
    </tr>
    <tr>
        <td>Назва</td>
        <td></td>
    </tr>
    <tr>
        <td>Учасники</td>
        <td></td>
    </tr>
    <tr>
        <td>Передумови</td>
        <td></td>
    </tr>
    <tr>
        <td>Результат</td>
        <td></td>
    </tr>
    <tr>
        <td>Виключні ситуації</td>
        <td></td>
    </tr>
    <tr>
        <td>Основний сценарій</td>
        <td></td>
    </tr>
</table>



<table>
    <tr>
        <th>ID</th>
        <th id="CreateBoard"><code>CreateBoard</code></th>
    </tr>
    <tr>
        <td>Назва</td>
        <td></td>
    </tr>
    <tr>
        <td>Учасники</td>
        <td></td>
    </tr>
    <tr>
        <td>Передумови</td>
        <td></td>
    </tr>
    <tr>
        <td>Результат</td>
        <td></td>
    </tr>
    <tr>
        <td>Виключні ситуації</td>
        <td></td>
    </tr>
    <tr>
        <td>Основний сценарій</td>
        <td></td>
    </tr>
</table>



<table>
    <tr>
        <th>ID</th>
        <th id="EditBoard"><code>EditBoard</code></th>
    </tr>
    <tr>
        <td>Назва</td>
        <td></td>
    </tr>
    <tr>
        <td>Учасники</td>
        <td></td>
    </tr>
    <tr>
        <td>Передумови</td>
        <td></td>
    </tr>
    <tr>
        <td>Результат</td>
        <td></td>
    </tr>
    <tr>
        <td>Виключні ситуації</td>
        <td></td>
    </tr>
    <tr>
        <td>Основний сценарій</td>
        <td></td>
    </tr>
</table>



<table>
    <tr>
        <th>ID</th>
        <th id="DeleteBoard"><code>DeleteBoard</code></th>
    </tr>
    <tr>
        <td>Назва</td>
        <td></td>
    </tr>
    <tr>
        <td>Учасники</td>
        <td></td>
    </tr>
    <tr>
        <td>Передумови</td>
        <td></td>
    </tr>
    <tr>
        <td>Результат</td>
        <td></td>
    </tr>
    <tr>
        <td>Виключні ситуації</td>
        <td></td>
    </tr>
    <tr>
        <td>Основний сценарій</td>
        <td></td>
    </tr>
</table>



<table>
    <tr>
        <th>ID</th>
        <th id="CreateTask"><code>CreateTask</code></th>
    </tr>
    <tr>
        <td>Назва</td>
        <td></td>
    </tr>
    <tr>
        <td>Учасники</td>
        <td></td>
    </tr>
    <tr>
        <td>Передумови</td>
        <td></td>
    </tr>
    <tr>
        <td>Результат</td>
        <td></td>
    </tr>
    <tr>
        <td>Виключні ситуації</td>
        <td></td>
    </tr>
    <tr>
        <td>Основний сценарій</td>
        <td></td>
    </tr>
</table>



<table>
    <tr>
        <th>ID</th>
        <th id="EditTask"><code>EditTask</code></th>
    </tr>
    <tr>
        <td>Назва</td>
        <td></td>
    </tr>
    <tr>
        <td>Учасники</td>
        <td></td>
    </tr>
    <tr>
        <td>Передумови</td>
        <td></td>
    </tr>
    <tr>
        <td>Результат</td>
        <td></td>
    </tr>
    <tr>
        <td>Виключні ситуації</td>
        <td></td>
    </tr>
    <tr>
        <td>Основний сценарій</td>
        <td></td>
    </tr>
</table>



<table>
    <tr>
        <th>ID</th>
        <th id="DeleteTask"><code>DeleteTask</code></th>
    </tr>
    <tr>
        <td>Назва</td>
        <td></td>
    </tr>
    <tr>
        <td>Учасники</td>
        <td></td>
    </tr>
    <tr>
        <td>Передумови</td>
        <td></td>
    </tr>
    <tr>
        <td>Результат</td>
        <td></td>
    </tr>
    <tr>
        <td>Виключні ситуації</td>
        <td></td>
    </tr>
    <tr>
        <td>Основний сценарій</td>
        <td></td>
    </tr>
</table>



<table>
    <tr>
        <th>ID</th>
        <th id="BanUser"><code>BanUser</code></th>
    </tr>
    <tr>
        <td>Назва</td>
        <td></td>
    </tr>
    <tr>
        <td>Учасники</td>
        <td></td>
    </tr>
    <tr>
        <td>Передумови</td>
        <td></td>
    </tr>
    <tr>
        <td>Результат</td>
        <td></td>
    </tr>
    <tr>
        <td>Виключні ситуації</td>
        <td></td>
    </tr>
    <tr>
        <td>Основний сценарій</td>
        <td></td>
    </tr>
</table>



<table>
    <tr>
        <th>ID</th>
        <th id="UnbanUser"><code>UnbanUser</code></th>
    </tr>
    <tr>
        <td>Назва</td>
        <td></td>
    </tr>
    <tr>
        <td>Учасники</td>
        <td></td>
    </tr>
    <tr>
        <td>Передумови</td>
        <td></td>
    </tr>
    <tr>
        <td>Результат</td>
        <td></td>
    </tr>
    <tr>
        <td>Виключні ситуації</td>
        <td></td>
    </tr>
    <tr>
        <td>Основний сценарій</td>
        <td></td>
    </tr>
</table>



<table>
    <tr>
        <th>ID</th>
        <th id="WriteToSupport"><code>WriteToSupport</code></th>
    </tr>
    <tr>
        <td>Назва</td>
        <td></td>
    </tr>
    <tr>
        <td>Учасники</td>
        <td></td>
    </tr>
    <tr>
        <td>Передумови</td>
        <td></td>
    </tr>
    <tr>
        <td>Результат</td>
        <td></td>
    </tr>
    <tr>
        <td>Виключні ситуації</td>
        <td></td>
    </tr>
    <tr>
        <td>Основний сценарій</td>
        <td></td>
    </tr>
</table>




## Короткий огляд продукту

*[Визначається границя системи та категорії її користувачів. Дається загальна характеристика категорій користувачів
системи]*

*[Нижче йде опис FURPS:]*


## Функціональність

*[Functionality (функциональні вимоги)]*  
*[Короткий опис]*

### Інтерфейс звичайного користувача

*[Опис того, що може робити звичайний користувач]*

### Інтерфейс керівника проєкту

*[Опис того, що може робити керівник проєкту]*

### Інтерфейс адміністратора

*[Опис того, що може робити адміністратор]*


## Практичність

*[Usability (вимоги до зручності роботи)]*  
*[Орієнтуйтеся на критерії з таблиці та додайте ще]*

## Надійність

*[Reliability (вимоги до надійності)]*  
*[Орієнтуйтеся на критерії з таблиці та додайте ще]*

## Продуктивність

*[Performance (вимоги до продуктивності)]*  
*[Орієнтуйтеся на критерії з таблиці та додайте ще]*

## Експлуатаційна придатність

*[Supportability (вимоги до підтримки)]*  
*[Орієнтуйтеся на критерії з таблиці та додайте ще]*
