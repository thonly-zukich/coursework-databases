# Запити зацікавлених осіб

## Вступ

<p>Цей документ містить відомості для тих, хто хоче ознайомитися з проєктом <strong>SigmaTasking</strong>. У ньому наведено ключову інформацію про цільову аудиторію продукту, основні терміни, що використовуються у процесі створення програмного забезпечення, описані бізнес-процеси, а також сформульовані вимоги до таких аспектів:</p>
    <ul>
        <li><a href="#функціональність">Функціональність</a></li>
        <li><a href="#практичність">Практичність</a></li>
        <li><a href="#надіиність">Надійність</a></li>
        <li><a href="#продуктивність">Продуктивність</a></li>
        <li><a href="#експлуатаціина-придатність">Експлуатаційнапридатність</a></li>
    </ul>

### Мета 

<p>Документ спрямований на визначення вимог і побажань від різних груп користувачів та зацікавлених сторін, а також специфікацій стосовно функціональності, зручності, надійності, продуктивності й підтримки. Це допоможе в розробці сучасного та ефективного програмного рішення для управління завданнями.</p>

### Контекст

<p>У цьому документі описується робота з різними типами проєктів – як комерційними, так і некомерційними, що використовують платформу <b>SigmaTasking</b>. Він розкриває ключові переваги нашого інструменту для управління завданнями і процесами.</p>


### Основні визначення та скорочення
<p><a href="https://what.com.ua/iakist-programnogo-zabezpechen/4/" target="_blank">ISO 9126</a> — міжнародний стандарт для оцінки якості програмного забезпечення. Він складається з чотирьох частин, що охоплюють такі аспекти:</p>
    <ul>
        <li>Зовнішні показники</li>
        <li>Внутрішні показники</li>
        <li>Модель якості</li>
        <li>Показники якості ПЗ</li>
    </ul>
    <p><a href="https://uk.wikipedia.org/wiki/Unified_Modeling_Language" target="_blank">UML (Unified Modeling Language)</a> — мова моделювання, яка є важливою складовою уніфікованого процесу розробки програмного забезпечення. UML є відкритим стандартом, що застосовує графічні елементи для створення абстрактних моделей систем, відомих як UML-моделі.</p>
    <p><a href="https://www.dstu.dp.ua/Portal/Data/3/19/3-19-kl26.pdf" target="_blank">FURPS</a> — це абревіатура, що визначає такі характеристики програмного забезпечення:</p>
    <ul>
        <li>Функціональність (Functionality)</li>
        <li>Зручність використання (Usability)</li>
        <li>Надійність (Reliability)</li>
        <li>Продуктивність (Performance)</li>
        <li>Підтримуваність (Supportability)</li>
    </ul>
    <p><a href="https://uk.wikipedia.org/wiki/%D0%97%D0%B0%D1%86%D1%96%D0%BA%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D1%96_%D1%81%D1%82%D0%BE%D1%80%D0%BE%D0%BD%D0%B8" target="_blank">Зацікавлені сторони</a> — це фізичні та юридичні особи, які мають обґрунтований інтерес до діяльності організації. Вони залежать від її функціонування або можуть впливати на неї.</p>
    <p><a href="https://pidru4niki.com/1471121353661/ekonomika/analiz_biznes-protsesiv_pidpriyemstva" target="_blank">Бізнес-процеси</a> — це процеси, які визначаються цілями та завданнями діяльності підприємства. Вони забезпечують реалізацію всіх видів діяльності, пов’язаних з виробництвом товарів або наданням послуг.</p>






У даному пункті перечисленні не всі визначення, частина з них знаходяться <a href="/coursework-databases/requirements/state-of-the-art.html#основні-визначення">тут</a>.


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

<table border="1">
    <tr>
        <th>ID</th>
        <td>BanUser</td>
    </tr>
    <tr>
        <th>Назва</th>
        <td>Заборонити користувача (Ban User)</td>
    </tr>
    <tr>
        <th>Учасники</th>
        <td>Адміністратор, система</td>
    </tr>
    <tr>
        <th>Передумови</th>
        <td>Адміністратор авторизований у системі</td>
    </tr>
    <tr>
        <th>Результат</th>
        <td>Користувач заборонений та не може входити в систему</td>
    </tr>
    <tr>
        <th>Виключні ситуації</th>
        <td>Користувача не знайдено (UserNotFoundException), недоступні права (InsufficientPermissionsException)</td>
    </tr>
    <tr>
        <th>Основний сценарій</th>
        <td>
            1. Адміністратор вибирає користувача зі списку.<br>
            2. Адміністратор натискає кнопку "Заборонити користувача".<br>
            3. Система перевіряє права адміністратора (можливе InsufficientPermissionsException).<br>
            4. Система забороняє користувача.<br>
            5. Користувач отримує повідомлення про заборону (можливе UserNotFoundException).
        </td>
    </tr>
</table>

<table border="1">
    <tr>
        <th>ID</th>
        <td>UnbanUser</td>
    </tr>
    <tr>
        <th>Назва</th>
        <td>Дозволити користувача (Unban User)</td>
    </tr>
    <tr>
        <th>Учасники</th>
        <td>Адміністратор, система</td>
    </tr>
    <tr>
        <th>Передумови</th>
        <td>Адміністратор авторизований у системі</td>
    </tr>
    <tr>
        <th>Результат</th>
        <td>Користувач дозволений та може знову входити в систему</td>
    </tr>
    <tr>
        <th>Виключні ситуації</th>
        <td>Користувача не знайдено (UserNotFoundException), недоступні права (InsufficientPermissionsException)</td>
    </tr>
    <tr>
        <th>Основний сценарій</th>
        <td>
            1. Адміністратор вибирає забороненого користувача зі списку.<br>
            2. Адміністратор натискає кнопку "Дозволити користувача".<br>
            3. Система перевіряє права адміністратора (можливе InsufficientPermissionsException).<br>
            4. Система дозволяє користувача.<br>
            5. Користувач отримує повідомлення про дозвіл.
        </td>
    </tr>
</table>

<table border="1">
    <tr>
        <th>ID</th>
        <td>WriteToSupport</td>
    </tr>
    <tr>
        <th>Назва</th>
        <td>Написати в службу підтримки (Write to Support)</td>
    </tr>
    <tr>
        <th>Учасники</th>
        <td>Користувач, система</td>
    </tr>
    <tr>
        <th>Передумови</th>
        <td>Користувач зареєстрований та авторизований у системі</td>
    </tr>
    <tr>
        <th>Результат</th>
        <td>Повідомлення відправлено до служби підтримки</td>
    </tr>
    <tr>
        <th>Виключні ситуації</th>
        <td>Не введено текст повідомлення (NullInstanceException), недопустимий формат (InvalidMessageFormatException)</td>
    </tr>
    <tr>
        <th>Основний сценарій</th>
        <td>
            1. Користувач відкриває форму для зв'язку зі службою підтримки.<br>
            2. Користувач вводить текст повідомлення (можливе NullInstanceException).<br>
            3. Система перевіряє введені дані (можливе InvalidMessageFormatException).<br>
            4. Система відправляє повідомлення до служби підтримки.<br>
            5. Користувач отримує підтвердження про відправлення повідомлення.
        </td>
    </tr>
</table>

<table border="1">
    <tr>
        <th>ID</th>
        <td>Usability</td>
    </tr>
    <tr>
        <th>Назва</th>
        <td>Оцінка експлуатаційної придатності (Evaluate Usability)</td>
    </tr>
    <tr>
        <th>Учасники</th>
        <td>Користувач, система</td>
    </tr>
    <tr>
        <th>Передумови</th>
        <td>Користувач зареєстрований та авторизований у системі</td>
    </tr>
    <tr>
        <th>Результат</th>
        <td>Оцінка експлуатаційної придатності системи</td>
    </tr>
    <tr>
        <th>Виключні ситуації</th>
        <td>Не введено коментар (NullInstanceException), недопустимий формат оцінки (InvalidRatingFormatException)</td>
    </tr>
    <tr>
        <th>Основний сценарій</th>
        <td>
            1. Користувач переходить до розділу "Оцінка експлуатаційної придатності".<br>
            2. Користувач вибирає рейтинг та вводить коментар (можливе NullInstanceException).<br>
            3. Система перевіряє введені дані (можливе InvalidRatingFormatException).<br>
            4. Система зберігає оцінку та коментар.<br>
            5. Користувач отримує підтвердження про успішне збереження оцінки.
        </td>
    </tr>
</table>


*Дається опис бізнес-сценаріїв взаємодії бізнес-акторів, робітників і, можливо, інформаційної системи за допомогою наступної
специфікації:*
   
<table style="border: 1px solid black; border-collapse: collapse;">
  <tr style="background-color: #d4f7dc;">
    <th style="border: 1px solid black; padding: 8px;">ID</th>
    <td style="border: 1px solid black; padding: 8px;">CreateBoard</td>
  </tr>
  <tr style="background-color: #d4f7dc;">
    <th style="border: 1px solid black; padding: 8px;">Назва</th>
    <td style="border: 1px solid black; padding: 8px;">Створити дошку (Create Board)</td>
  </tr>
  <tr>
    <th style="border: 1px solid black; padding: 8px;">Учасники</th>
    <td style="border: 1px solid black; padding: 8px;">Користувач (тимлід або розробник), система</td>
  </tr>
  <tr style="background-color: #d4f7dc;">
    <th style="border: 1px solid black; padding: 8px;">Передумови</th>
    <td style="border: 1px solid black; padding: 8px;">Користувач зареєстрований та авторизований у системі</td>
  </tr>
  <tr>
    <th style="border: 1px solid black; padding: 8px;">Результат</th>
    <td style="border: 1px solid black; padding: 8px;">Нова дошка створена та доступна для користування</td>
  </tr>
  <tr style="background-color: #d4f7dc;">
    <th style="border: 1px solid black; padding: 8px;">Виключні ситуації</th>
    <td style="border: 1px solid black; padding: 8px;">Користувач не ввів назву дошки (NullInstanceException), недопустима назва (InvalidBoardNameException)</td>
  </tr>
  <tr>
    <th style="border: 1px solid black; padding: 8px;">Основний сценарій</th>
    <td style="border: 1px solid black; padding: 8px;">
      <ol>
        <li>Користувач натискає кнопку "Створити дошку"</li>
        <li>Користувач вводить назву дошки (можливе NullInstanceException)</li>
        <li>Система перевіряє введені дані (можливе InvalidBoardNameException)</li>
        <li>Система створює нову дошку</li>
        <li>Користувач отримує доступ до дошки</li>
      </ol>
    </td>
  </tr>
</table>

<table style="border: 1px solid black; border-collapse: collapse;">
  <tr style="background-color: #d4f7dc;">
    <th style="border: 1px solid black; padding: 8px;">ID</th>
    <td style="border: 1px solid black; padding: 8px;">EditBoard</td>
  </tr>
  <tr style="background-color: #d4f7dc;">
    <th style="border: 1px solid black; padding: 8px;">Назва</th>
    <td style="border: 1px solid black; padding: 8px;">Редагувати дошку (Edit Board)</td>
  </tr>
  <tr>
    <th style="border: 1px solid black; padding: 8px;">Учасники</th>
    <td style="border: 1px solid black; padding: 8px;">Користувач (тимлід або розробник), система</td>
  </tr>
  <tr style="background-color: #d4f7dc;">
    <th style="border: 1px solid black; padding: 8px;">Передумови</th>
    <td style="border: 1px solid black; padding: 8px;">Користувач має права на редагування дошки</td>
  </tr>
  <tr>
    <th style="border: 1px solid black; padding: 8px;">Результат</th>
    <td style="border: 1px solid black; padding: 8px;">Зміни збережені</td>
  </tr>
  <tr style="background-color: #d4f7dc;">
    <th style="border: 1px solid black; padding: 8px;">Виключні ситуації</th>
    <td style="border: 1px solid black; padding: 8px;">Дошка не знайдена (BoardNotFoundException), відсутні права на редагування (AccessDeniedException)</td>
  </tr>
  <tr>
    <th style="border: 1px solid black; padding: 8px;">Основний сценарій</th>
    <td style="border: 1px solid black; padding: 8px;">
      <ol>
        <li>Користувач відкриває дошку</li>
        <li>Користувач натискає кнопку "Редагувати"</li>
        <li>Користувач вносить зміни в дошку</li>
        <li>Система перевіряє права на редагування (можливе AccessDeniedException)</li>
        <li>Система зберігає зміни</li>
      </ol>
    </td>
  </tr>
</table>

<table style="border: 1px solid black; border-collapse: collapse;">
  <tr style="background-color: #d4f7dc;">
    <th style="border: 1px solid black; padding: 8px;">ID</th>
    <td style="border: 1px solid black; padding: 8px;">DeleteBoard</td>
  </tr>
  <tr style="background-color: #d4f7dc;">
    <th style="border: 1px solid black; padding: 8px;">Назва</th>
    <td style="border: 1px solid black; padding: 8px;">Видалити дошку (Delete Board)</td>
  </tr>
  <tr>
    <th style="border: 1px solid black; padding: 8px;">Учасники</th>
    <td style="border: 1px solid black; padding: 8px;">Користувач (тимлід або розробник), система</td>
  </tr>
  <tr style="background-color: #d4f7dc;">
    <th style="border: 1px solid black; padding: 8px;">Передумови</th>
    <td style="border: 1px solid black; padding: 8px;">Користувач має права на видалення дошки</td>
  </tr>
  <tr>
    <th style="border: 1px solid black; padding: 8px;">Результат</th>
    <td style="border: 1px solid black; padding: 8px;">Дошка видалена</td>
  </tr>
  <tr style="background-color: #d4f7dc;">
    <th style="border: 1px solid black; padding: 8px;">Виключні ситуації</th>
    <td style="border: 1px solid black; padding: 8px;">Дошка не знайдена (BoardNotFoundException), відсутні права на видалення (AccessDeniedException)</td>
  </tr>
  <tr>
    <th style="border: 1px solid black; padding: 8px;">Основний сценарій</th>
    <td style="border: 1px solid black; padding: 8px;">
      <ol>
        <li>Користувач відкриває дошку</li>
        <li>Користувач натискає кнопку "Видалити"</li>
        <li>Система перевіряє права на видалення (можливе AccessDeniedException)</li>
        <li>Система видаляє дошку</li>
        <li>Користувач отримує підтвердження про успішне видалення</li>
      </ol>
    </td>
  </tr>
</table>

*Кількість сценаріїв визначається у відповідності до специфіки завдання та необхідного 
рівня деталізації (зазвичай, 5-6 сценаріїв).*

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
<ul>
    <li>Чистий, мінімалістичний інтерфейс із зрозумілим дизайном, що не потребує додаткового навчання.</li>
    <li>Підтримка кількох мов для зручного використання користувачами з різних країн.</li>
    <li>Документація, яка легко сприймається і охоплює всі функції сервісу, водночас проста для вивчення.</li>
    <li>Можливість роботи на різних платформах (кросплатформеність).</li>
    <li>Функціональність гарячих клавіш для швидкого доступу до функцій.</li>
    <li>Механізми резервного копіювання (відновлення видалених даних і відновлення доступу до облікового запису).</li>
    <li>Використання візуальних інструментів для відображення прогресу, таких як схеми, графіки та діаграми.</li>
    <li>Опція відновлення пароля.</li>
    <li>Підтримка адаптації інтерфейсу до різних роздільних здатностей екранів.</li>
</ul>


## Надійність

*[Reliability (вимоги до надійності)]*  
*[Орієнтуйтеся на критерії з таблиці та додайте ще]*

## Продуктивність

- Висока швидкість передачі даних між компонентами системи.
- Оптимізоване використання оперативної пам'яті та інтернет-ресурсів.
- Використання хмарних технологій для збільшення продуктивності.
- Підтримка багатопотокової обробки даних для підвищення ефективності.
- Гнучка настройка ресурсів для кожного окремого проекту.
- Підвищена пропускна здатність системи для обробки великих обсягів даних.

## Експлуатаційна придатність

*[Supportability (вимоги до підтримки)]*  
*[Орієнтуйтеся на критерії з таблиці та додайте ще]*
