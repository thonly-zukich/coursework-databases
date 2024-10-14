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
