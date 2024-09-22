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

*[Розділ містить опис того, про що йдеться в еій частині цього документу, що залишилася. 
Також тут описана структура документу.]*

## Характеристика ділових процесів

*[В цьому розділі визначаються зовнішні фактори, що впливають на бізнес (бізнес-актори), 
та внутрішні фактори (робітники), дається загальна характеристика діяльності бізнес-акторів 
та робітників, яка здійснюється за допомогою бізнесу.*

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

## Практичність

*[Usability (вимоги до зручності роботи)]*

## Надійність

*[Reliability (вимоги до надійності)]*

## Продуктивність

- Висока швидкість передачі даних між компонентами системи.
- Оптимізоване використання оперативної пам'яті та інтернет-ресурсів.
- Використання хмарних технологій для збільшення продуктивності.
- Підтримка багатопотокової обробки даних для підвищення ефективності.
- Гнучка настройка ресурсів для кожного окремого проекту.
- Підвищена пропускна здатність системи для обробки великих обсягів даних.


## Експлуатаційна придатність

*[Supportability (вимоги до підтримки)]*
