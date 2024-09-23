# Аналіз предметної області

## Вступ

<p><b>В даній лаборатоні присутні:</b></p>
<ul>
<li><a href="#основні-визначення">Основні визначення</a> </li>
<li><a href="#підходи-та-способи-вирішення-завдання">Підходи та способи вирішення завдання</a></li>
<li><a href="#порівняльна-характеристика-існуючих-засобів-вирішення-завдання">Порівняльна характеристика наявних засобів вирішення завдання</a></li>
<li><a href="#висновки">Висновки</a></li>
<li><a href="#посилання">Посилання на джерела</a></li>


</ul>


## Основні визначення

 [Система управління проєктами (Project management software, PMS)](https://uk.wikipedia.org/wiki/%D0%A1%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0_%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D1%96%D0%BD%D0%BD%D1%8F_%D0%BF%D1%80%D0%BE%D1%94%D0%BA%D1%82%D0%B0%D0%BC%D0%B8) - це набір інструментів, що допомагає команді планувати, розподіляти ресурси, координувати роботу та стежити за її виконанням.

[Проєкт (Project)](https://uk.wikipedia.org/wiki/%D0%9F%D1%80%D0%BE%D1%94%D0%BA%D1%82) - це набір завдань, спрямованих на досягнення конкретної мети або результату у встановлений термін та з використанням обмежених ресурсів. Успішність проєкту оцінюється тим, наскільки результат відповідає початковим вимогам.

[Методологія Agile (Agile Methodology)](https://brainrain.com.ua/uk/chto-takoe-agile-ua/) - це підхід до управління проєктами, що полягає в гнучкості, адаптації та поступовій реалізації завдань через короткі ітерації.

[Етапи проєкту (Project Phases)](https://flexi-project.com/uk/4-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%96-%D0%B5%D1%82%D0%B0%D0%BF%D0%B8-%D1%80%D0%B5%D0%B0%D0%BB%D1%96%D0%B7%D0%B0%D1%86%D1%96%D1%97-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D1%83/) - це конкретні стадії життєвого циклу проєкту, включаючи ініціацію, планування, виконання, моніторинг та закриття.

[Ризики проєкту (Project Risks)](https://pmb.com.ua/uk/slovar-terminov/upravlenie-riskami-proekta-project-risk-management/) - це ймовірні події або умови, які можуть вплинути на досягнення цілей проєкту як позитивно, так і негативно, тому їх слід передбачати і управляти ними PMI.

[Ресурси проєкту (Project Resources)](https://pmtips.com.ua/post/proektni-resursi) - це всі елементи, які необхідні для виконання проекту. До основних ресурсів відносяться: люди, матеріальні та фінансові ресурси та час.

[Артефакт (Artifact)](https://uk.wikipedia.org/wiki/%D0%90%D1%80%D1%82%D0%B5%D1%84%D0%B0%D0%BA%D1%82) - це об'єкт або документ, що є результатом процесу розробки і містить важливу інформацію для проєкту, наприклад, технічну документацію.

[Контроль версій (Version control)](https://uk.wikibooks.org/wiki/Pro_GIT/%D0%92%D1%81%D1%82%D1%83%D0%BF/%D0%9F%D1%80%D0%BE_%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D1%8C_%D0%B2%D0%B5%D1%80%D1%81%D1%96%D0%B9) - це система, яка постійно фіксує зміни в проєкті, щоб зберігати його попередні версії для майбутнього використання.

## Підходи та способи вирішення завдання


### Життєвий цикл розробки програмного забезпечення

<ol>
        <li>
            <strong> Життєвий цикл розробки ПО</strong>
            <p>Життєвий цикл розробки програмного забезпечення (Software Development Life Cycle - SDLC) — це процес створення ПЗ, який охоплює всі етапи, від початкового задуму до підтримки готового продукту. SDLC допомагає організувати розробку програмного забезпечення таким чином, щоб забезпечити якісне виконання проєкту в межах часу, бюджету та вимог.</p>
        </li>
        <li>
            <strong> основні етапи</strong>
            <p>Основні етапи SDLC включають:</p>
            <ul>
                <li>Аналіз вимог</li>
                <p>На даному етапі замовник надає всю необхідну інформацію для розробки продукту відповідно до своїх очікувань. Будь-які неясності вирішуються на цьому етапі. Бізнес-аналітик і керівник проєкту зустрічаються із замовником, щоб з'ясувати, що потрібно створити, хто кінцевий користувач, та яка мета продукту. Після збору вимог створюється документ SRS, який повинен бути зрозумілим для розробників і затвердженим замовником.</p>
                <li>Проєктування</li>
                <p>На цьому етапі вимоги, зібрані в документі SRS, використовуються як вхідні дані, і визначається архітектура програмного забезпечення, яка використовується для реалізації розробки системи.</p>
                <li>Розробка</li>
                <p>розробка починається після того, як розробник отримує проектний документ. Дизайн програмного забезпечення перекладається у вихідний код. На цьому етапі реалізуються всі компоненти програмного забезпечення.</p>
                <li>Тестування</li>
                <p>Тестування починається після завершення кодування. Програмне забезпечення тестується, а виявлені дефекти передаються розробникам для виправлення. Тестування триває, доки ПЗ не відповідатиме очікуванням замовника, з використанням документа SRS як стандарту.</p>
                <li>Впровадження</li>
                <p>Після тестування, його розгортають у виробничому середовищі або проводять перше UAT-тестування (User Acceptance testing), залежно від очікувань замовника</p>
                <li>Обслуговування та підтримка</li>
                <p>Після розгортання продукту у виробничому середовищі, підтримка продукту, тобто, якщо виникає якась проблема, яку потрібно виправити, або якщо потрібно зробити якесь покращення, здійснюється розробниками.</p>
            </ul>
        </li>
        <li><a href="https://www.maxzosim.com/content/images/2023/05/image-18.png">Фази життєвого циклу розробки програмного забезпечення</a></li>
        <p> <img src="https://www.maxzosim.com/content/images/2023/05/image-18.png"></p>
 </ol>
 

### Waterfall (каскадна модель)

  <p><b>Каскадна модель (Waterfall)</b> — один із найстаріших підходів до розробки ПЗ. Етапи виконуються послідовно, без повернень до попередніх.</p>
    <b>Плюси каскадної моделі</b>
    <ul>
        <li>Легкість управління проєктом</li>
        <li>Зрозумілі дедлайни та бюджет</li>
        <li>Проста організація тестування</li>
    </ul>
    <b>Мінуси каскадної моделі</b>
    <ul>
        <li>Висока вартість виправлення помилок на пізніх етапах</li>
        <li>Замовник бачить продукт лише після завершення розробки</li>
        <li>Велика кількість документації збільшує час на узгодження</li>
    </ul> 
    <p><img src="https://itexpert.work/wp-content/webp-express/webp-images/uploads/2022/06/kaskadna-model.jpg.webp" width="600px"></p>
    <p><a href="https://images.app.goo.gl/K6vdCS7QUMwftzabA">посилання на схему</a></p>
    
      


## Agile

**Agile** — це методологія управління проектами, яка акцентує увагу на співпраці, гнучкості та ітеративному розвитку. Основні принципи були вперше викладені в "Agile Manifesto" у 2001 році, і головною метою є підвищення ефективності команд через пріоритет взаємодії між людьми, працюючим продуктом та гнучкістю до змін.

### Основні принципи:

1. **Люди важливіші за процеси та інструменти**  
   Взаємодія та командна робота є пріоритетом, інструменти — лише засіб для досягнення мети.

2. **Продукт, що працює, важливіший за документацію**  
   Робочий продукт завжди має пріоритет перед складною та надмірною документацією.

3. **Співпраця із замовником важливіша за умови контракту**  
   Постійна комунікація з клієнтом дозволяє краще зрозуміти його потреби та адаптувати проект.

4. **Готовність до змін важливіша за дотримання плану**  
   Команди повинні бути гнучкими та адаптуватися до змін на будь-якому етапі проекту.

### Переваги Agile:

- **Клієнтська спрямованість**  
  Активна участь клієнта у процесі допомагає уникнути ризиків та полегшує прийняття рішень.

- **Гнучкість**  
  Швидка адаптація до змін у вимогах та умовах середовища.

- **Ефективність**  
  Оперативне виправлення помилок і швидкий вихід на ринок.

- **Покращена комунікація**  
  Постійний зворотний зв'язок забезпечує кращу координацію в команді.

### Недоліки Agile:

- **Додаткові вимоги до команди**  
  Необхідна висока кваліфікація, мотивація та самодисципліна учасників.

- **Нестійкість до змін**  
  Agile може бути неефективним для проектів, що мають жорсткі вимоги та фіксовані дедлайни.

- **Складність управління великими проектами**  
  У масштабних проектах управління може стати складнішим і вимагати більше ресурсів та часу.

### Traditional vs Agile
![Traditional vs Agile](https://www.kpipartners.com/hs-fs/hubfs/Imported_Blog_Media/traditional-vs-agile-1.png?width=800&name=traditional-vs-agile-1.png)
<div>
  <p>Схема Traditional vs Agile <a href="https://www.kpipartners.com/hs-fs/hubfs/Imported_Blog_Media/traditional-vs-agile-1.png?width=800&name=traditional-vs-agile-1.png">[6]</a></p>
</div>
### Scrum

<p>Scrum — це популярний фреймворк для управління проектами, особливо в сфері розробки програмного забезпечення. Його суть полягає у розбитті процесу на короткі цикли (ітерації), що називаються спринтами, тривалістю зазвичай 2–4 тижні. Після кожного спринта команда оцінює результати і коригує план дій. Scrum підкреслює важливість ролей (Scrum Master, Product Owner, команда розробників), подій (щоденні мітинги, огляди спринтів) та артефактів (бэклог продукту та спринта).</p>

        <h4>Плюси:</h4>
        <ul class="advantages">
            <li>Швидка реакція на зміни та постійне вдосконалення продукту.</li>
            <li>Висока залученість команди та замовника.</li>
            <li>Можливість регулярного отримання результатів після кожного спринта.</li>
        </ul>
        <h4>Мінуси:</h4>
        <ul class="disadvantages">
            <li>Може бути складним для великих команд.</li>
            <li>Потребує чіткого дотримання правил і дисципліни.</li>
            <li>Вимагає активної участі замовника.</li>
        </ul>

        <img src="https://miro.medium.com/v2/resize:fit:1083/1*h9iv87c9Lp5aGksmSrRB5g.png" alt="Схема Scrum">
        <p><a href="https://ru.wikipedia.org/wiki/Scrum" target="_blank">Докладніше про Scrum</a></p>

### Kanban

<p>Kanban — це візуальна система управління робочими процесами, спрямована на оптимізацію ефективності через постійне вдосконалення. Ключовим елементом є Kanban-дошка, де кожне завдання представлено карткою, яка переміщується між колонками («Заплановано», «В роботі», «Готово»). Основна мета — балансувати робоче навантаження та уникати перевантаження команди.</p>

        <h4>Плюси:</h4>
        <ul class="advantages">
            <li>Висока гнучкість та прозорість процесів.</li>
            <li>Легка візуалізація статусу кожного завдання.</li>
            <li>Підходить для процесів з непостійними або частими змінами.</li>
        </ul>
        <h4>Мінуси:</h4>
        <ul class="disadvantages">
            <li>Відсутність чітко структурованих ітерацій може ускладнити планування.</li>
            <li>Може бути менш ефективним у великих командах без належної організації.</li>
            <li>Потребує постійного моніторингу для забезпечення оптимальної роботи.</li>
        </ul>

        <img src="https://miro.medium.com/v2/resize:fit:1083/1*T8urfVVVAwlFtM5an-TBJg.png" alt="Схема Kanban">
        <p><a href="https://ru.wikipedia.org/wiki/Kanban" target="_blank">Докладніше про Kanban</a></p>

### Lean
 Lean (Lean manufacturing або Lean production) — це філософія управління, розроблена для підвищення ефективності виробництва через скорочення втрат. Lean фокусується на створенні максимальної цінності для клієнта при мінімальних витратах ресурсів шляхом усунення діяльності, яка не додає цінності. Lean походить з принципів, які були вперше застосовані компанією Toyota в їх системі виробництва (Toyota Production System, TPS).

**Основні принципи Lean:**
1. **Визначення цінності** з точки зору клієнта.
2. **Аналіз потоку створення цінності** — ідентифікація всіх кроків, що додають цінність.
3. **Побудова потоку** безперервного створення цінності.
4. **Витягування** продукції на вимогу (pull-system).
5. **Безперервне вдосконалення** — постійне усунення втрат (кайдзен).

**Переваги Lean:**
- **Зменшення витрат** за рахунок усунення непотрібних операцій та ресурсів.
- **Підвищення якості** продукції через фокус на процесах, що додають цінність.
- **Збільшення продуктивності** завдяки оптимізації робочих процесів.
- **Краща адаптивність** до змін ринкових умов через гнучкість виробництва.
- **Покращення взаємодії в команді** через залучення всіх працівників до процесу вдосконалення.

**Недоліки Lean:**
- **Високі початкові витрати на впровадження** — навчання персоналу, зміну організації виробництва.
- **Складність адаптації** для підприємств із складними виробничими процесами або нестабільним попитом.
- **Ризик надмірної оптимізації**, що може призвести до зниження гнучкості в умовах непередбачених ситуацій.
- **Потреба в постійній підтримці та вдосконаленні**, що може бути ресурсозатратним.


![Схема Lean](https://optim.tildacdn.one/tild3732-6639-4638-a234-333434373765/-/resize/1160x/-/format/webp/leanprinciples.jpg)

Джерело схеми: [Lean Institute](https://lean.org.ua/olean) 

### Спіральна модель

Спіральна модель (Spiral Model) — це методологія розробки програмного забезпечення, яка об'єднує ітеративний підхід з елементами класичних моделей. Модель була запропонована Баррі Бьомом у 1986 році.

Цикли розробки в спіральній моделі поділяються на 4 основні етапи:
1. **Визначення цілей, вимог та альтернатив** для кожної фази.
2. **Аналіз ризиків** і розробка стратегії їх зменшення.
3. **Реалізація та тестування** продукту або прототипу.
4. **Оцінка результатів** і планування наступної ітерації.

Процес проходить через кілька ітерацій, які відображаються у вигляді спіралі, поступово уточнюючи та вдосконалюючи продукт.


**Переваги спіральної моделі:**
- **Акцент на управлінні ризиками** дозволяє уникнути помилок і запобігти критичним проблемам на ранніх етапах.
- **Гнучкість і адаптивність** до змін вимог, що дозволяє легко інтегрувати нові ідеї або коригування.
- **Прототипування на ранніх етапах**, що допомагає користувачам краще зрозуміти кінцевий продукт.
- **Поетапний контроль** дозволяє замовникам і розробникам оцінювати прогрес і вносити корективи.

**Недоліки спіральної моделі:**
- **Високі витрати** через постійні оцінки ризиків і прототипування.
- **Складність управління** через необхідність постійного аналізу ризиків та їхнього контролю.
- **Тривалість розробки**, оскільки кожна фаза проходить через кілька ітерацій.
- **Не завжди підходить для малих проектів** через високі ресурси, які потрібні для аналізу ризиків і проведення ітерацій.


![Схема спіральної моделі](https://www.maxzosim.com/content/images/size/w1600/2023/02/image-112.png)

Джерело схеми: [Spiral Model](https://www.maxzosim.com/content/images/size/w1600/2023/02/image-112.png)

### RAD (Rapid Application Development)

RAD (Rapid Application Development) — це методологія розробки програмного забезпечення, яка проводиться в режимі реального часу, що дозволяє зробити вирішення завдання без потреби на конструктивному стилі аналізу та оцінюванні. RAD використовується для розробки програмного забезпечення шляхом швидкого створення прототипів, які використовуються для оцінки вимог користувачів та виправлення помилок.

**Основні принципи RAD:**
1. **Швидка розробка** — програмне забезпечення розробляється швидко, що дозволяє зробити вирішення завдання без потреби на конструктивному стилі аналізу та оцінюванні.
2. **Швидка виправлення помилок** — програмне забезпечення розробляється швидко, що дозволяє зробити вирішення завдання без потреби на конструктивному стилі аналізу та оцінюванні.
3. **Швидка оцінка вимог** — програмне забезпечення розробляється швидко, що дозволяє зробити вирішення завдання без потреби на конструктивному стилі аналізу та оцінюванні.
4. **Швидка поширення знань** — програмне забезпечення розробляється швидко, що дозволяє зробити вирішення завдання без потреби на конструктивному стилі аналізу та оцінюванні.

**Переваги RAD:**
- **Зменшення витрат** за рахунок усунення непотрібних операцій та ресурсів.
- **Підвищення якості роботи** через швидке створення прототипів та виправлення помилок.
- **Збільшення продуктивності** завдяки оптимізації робочих процесів.
- **Краща адаптивність** до змін вимог, що дозволяє легко інтегрувати нові ідеї або коригування.
- **Покращення взаємодії в команді** через залучення всіх працівників до процесу вдосконалення.

**Недоліки RAD:**
- **Високі витрати** через постійні оцінки ризиків і прототипування.
- **Складність управління** через необхідність постійного аналізу ризиків та їхнього контролю.
- **Тривалість розробки**, оскільки кожна фаза проходить через кілька ітерацій.
- **Не завжди підходить для малих проектів** через високі ресурси, які потрібні для аналізу ризиків і проведення ітерацій.

![Схема RAD](https://maybe.works/media/blogs/rapid-application-development-rad/1100x600.jpg)

Джерело схеми: [RAD - Rapid Application Development](https://maybe.works/media/blogs/rapid-application-development-rad/1100x600.jpg) 

### DevOps

<p> <b>DevOps</b> — низка практик, призначених для пожвавлення взаємодії розробників із фахівцями інформаційно-технологічного обслуговування та зближення їхніх робочих процесів одне з одним. Ґрунтується на думці про тісну взаємозалежність між розробкою та використанням програмного забезпечення і має на меті допомогти організаціям швидше створювати та оновлювати програмні продукти та послуги.</p> 
<h2>Переваги:</h2>
<ul>
    <li><strong>Швидкість розробки:</strong> Автоматизація процесів дозволяє швидше впроваджувати зміни.</li>
    <li><strong>Покращена співпраця:</strong> Зміцнення комунікації між командами розробки та експлуатації.</li>
    <li><strong>Частіше впровадження:</strong> Часті оновлення завдяки CI/CD.</li>
    <li><strong>Зниження ризиків:</strong> Виявлення проблем на ранніх етапах через автоматизацію тестування.</li>
    <li><strong>Ефективність ресурсів:</strong> Оптимізація використання ресурсів знижує витрати.</li>
</ul>

<h2>Недоліки:</h2>
<ul>
    <li><strong>Складність впровадження:</strong> Значні зміни в культурі та процесах можуть викликати опір.</li>
    <li><strong>Необхідність навичок:</strong> Потрібні нові знання в області автоматизації та CI/CD.</li>
    <li><strong>Ризик надмірної автоматизації:</strong> Може призвести до проблем без контролю якості.</li>
    <li><strong>Безпека:</strong> Інтеграція безпеки в процеси може бути складною.</li>
    <li><strong>Витрати на інструменти:</strong> Навчання та впровадження можуть бути дорогими.</li>
</ul>

<img src="https://img.freepik.com/premium-vector/devops-scheme-software-development-lifecycle-operations-concept-software-engineering-workflow-cycle-vector-illustration-devops-software-development-process_229548-2380.jpg" alt="Схема DevOps">

<p>Джерело схеми: <a href="https://img.freepik.com/premium-vector/devops-scheme-software-development-lifecycle-operations-concept-software-engineering-workflow-cycle-vector-illustration-devops-software-development-process_229548-2380.jpg">DevOps</a></p>



## Порівняльна характеристика існуючих засобів вирішення завдання

### [Notion](https://www.notion.so/)
**Notion** — це універсальна платформа, яка дозволяє не лише організовувати роботу над проектами, але й структурувати інформацію. Основною перевагою Notion є інтеграція кількох видів інструментів: від текстових документів і медіа до списків завдань і дошок Kanban. Користувачі можуть швидко налаштовувати робочий простір та працювати в реальному часі, додаючи та змінюючи дані спільно з колегами.

### [ClickUp](https://clickup.com/)
**ClickUp** — потужна система для управління проектами, яка підтримує велику кількість функцій, зокрема роботу із завданнями, документами, цілями та автоматизацією процесів. Інтерфейс легко налаштовується під потреби кожної команди, а також є можливість інтеграції з багатьма сторонніми сервісами. Завдяки своїй гнучкості ClickUp є чудовим вибором для різних організацій, які шукають універсальний інструмент для покращення робочого процесу.

### [GitHub Projects](https://github.com/features/project-management)
**GitHub Projects** — це рішення для тих, хто безпосередньо працює з GitHub. Інструмент дозволяє легко організовувати завдання через дошки, інтегруючись із системою GitHub Issues та pull requests. Це робить GitHub Projects чудовим вибором для розробників, які прагнуть зберігати весь процес розробки, від постановки завдань до виконання коду, в одному місці.

### [Trello](https://trello.com/)
**Trello** — проста у використанні платформа для керування проектами, яка використовує систему дошок і карток для відстеження завдань. Завдяки легкості та простоті інтерфейсу Trello особливо підходить для невеликих команд, які прагнуть швидко налаштувати процеси без додаткових складнощів. Водночас можливості інтеграції із зовнішніми сервісами роблять цю платформу гнучкою навіть для більших проектів.

### [JIRA](https://www.atlassian.com/software/jira)
**JIRA** — це один із найпопулярніших інструментів для управління проектами та відстеження проблем, що пропонує широкий функціонал для великих і малих команд. Інструмент від Atlassian зосереджений на проектуванні складних процесів, відстеженні дефектів та покращенні продуктивності команд, що працюють над розробкою програмного забезпечення.

### [Asana](https://asana.com/)
**Asana** — веб-застосунок для управління завданнями, який дозволяє командам зосередитися на продуктивності та співпраці. Відмінною рисою Asana є можливість адаптувати систему під різні типи проектів завдяки її потужному інтерфейсу для відстеження завдань, термінів і відповідальних осіб. Система підтримує інтеграції з іншими популярними інструментами, що дозволяє ефективно керувати проектами будь-якого масштабу.

### [Nifty](https://niftypm.com/)
**Nifty** — це хмарна платформа, яка поєднує можливості планування та відстеження прогресу в одному інтерфейсі. Інструмент дозволяє легко управляти завданнями та підвищувати продуктивність команди через гнучке налаштування робочих процесів, що особливо корисно для стартапів і команд, що швидко зростають.

### [Microsoft Project](https://www.microsoft.com/en-us/microsoft-365/project/project-management-software)
**Microsoft Project** — рішення для керування проектами, яке пропонує широкий спектр можливостей для планування, управління ресурсами та моніторингу прогресу. Ця система є популярним вибором серед великих компаній завдяки можливості інтеграції з іншими продуктами Microsoft та підтримці традиційних підходів до управління проектами.

 ### Порівняльна таблиця

<head>
    <style>
        th, td {
            text-align: center;
        }
    </style>
</head>

 <table>
    <thead>
        <tr>
            <th class="requirements">Вимоги</th>
            <th class="criteria">Критерії</th>
            <th class="our-project">SigmaTasking (Наш Проєкт)</th>
            <th class="project-1">GitHub Projects</th>
            <th class="project-2">Notion</th>
            <th class="project-3">JIRA</th>
            <th class="project-4">Asana</th>
            <th class="project-5">Nifty</th>
            <th class="project-6">Microsoft Project</th>
            <th class="project-7">Click Up</th>
            <th class="project-8">Monday.com</th> 
        </tr>
    </thead>
    <tbody>
        <tr>
        <!-- rowspawn = кількість критеріїв -->
        <!-- Якщо потрібно додати критерій, вставляємо цей код після останнього критерія
        <tr>
            <td class="criteria">-</td>
            <td class="our-project">-</td>
            <td class="project-1">-</td>
            <td class="project-2">-</td>
            <td class="project-3">-</td>
            <td class="project-4">-</td>
            <td class="project-5">-</td>
            <td class="project-6">-</td>
            <td class="project-7">-</td>
            <td class="project-8">-</td>
        </tr>
        -->
            <td class="requirements" rowspan=6>Functionality (функціональність)</td>
            <th class="criteria">Кросплатформеність</th>
    <td class="our-project">✖</td>
    <td class="project-1">✔</td>
    <td class="project-2">✔</td>
    <td class="project-3">✔</td>
    <td class="project-4">✔</td>
    <td class="project-5">✔</td>
    <td class="project-6">✔</td>
    <td class="project-7">✔</td>
    <td class="project-8">✔</td>
</tr>
<tr>
    <th class="criteria">Мобільна версія</th>
    <td class="our-project">✖</td>
    <td class="project-1">✖</td>
    <td class="project-2">✔</td>
    <td class="project-3">✔</td>
    <td class="project-4">✔</td>
    <td class="project-5">✔</td>
    <td class="project-6">✔</td>
    <td class="project-7">✔</td>
    <td class="project-8">✔</td>
</tr>
<tr>
    <th class="criteria">Наявність API</th>
    <td class="our-project">✖</td>
    <td class="project-1">✔</td>
    <td class="project-2">✖</td>
    <td class="project-3">✖</td>
    <td class="project-4">✔</td>
    <td class="project-5">✔</td>
    <td class="project-6">✔</td>
    <td class="project-7">✔</td>
    <td class="project-8">✔</td>
</tr>
<tr>
    <th class="criteria">Офлайн-доступ</th>
    <td class="our-project">✖</td>
    <td class="project-1">✖</td>
    <td class="project-2">✖</td>
    <td class="project-3">✖</td>
    <td class="project-4">✖</td>
    <td class="project-5">✖</td>
    <td class="project-6">✔</td>
    <td class="project-7">✔</td>
    <td class="project-8">✔</td>
</tr>
<tr>
    <th class="criteria">Миттєві повідомлення (чат)</th>
    <td class="our-project">✖</td>
    <td class="project-1">✖</td>
    <td class="project-2">✔</td>
    <td class="project-3">✖</td>
    <td class="project-4">✖</td>
    <td class="project-5">✖</td>
    <td class="project-6">✔</td>
    <td class="project-7">✔</td>
    <td class="project-8">✔</td>
</tr>
<tr>
    <th class="criteria">Призначення завдань учасникам</th>
    <td class="our-project">✖</td>
    <td class="project-1">✔</td>
    <td class="project-2">✔</td>
    <td class="project-3">✔</td>
    <td class="project-4">✔</td>
    <td class="project-5">✔</td>
    <td class="project-6">✔</td>
    <td class="project-7">✔</td>
    <td class="project-8">✔</td>
</tr>
        <!-- new requirement -->
        <tr>
            <td class="requirements" rowspan=6>Reliability (надійність)</td>
            <td class="criteria">-</td>
            <td class="our-project">-</td>
            <td class="project-1">-</td>
            <td class="project-2">-</td>
            <td class="project-3">-</td>
            <td class="project-4">-</td>
            <td class="project-5">-</td>
            <td class="project-6">-</td>
            <td class="project-7">-</td>
            <td class="project-8">-</td>
        </tr>
        <tr>
            <td class="criteria">-</td>
            <td class="our-project">-</td>
            <td class="project-1">-</td>
            <td class="project-2">-</td>
            <td class="project-3">-</td>
            <td class="project-4">-</td>
            <td class="project-5">-</td>
            <td class="project-6">-</td>
            <td class="project-7">-</td>
            <td class="project-8">-</td>
        </tr>
        <tr>
            <td class="criteria">-</td>
            <td class="our-project">-</td>
            <td class="project-1">-</td>
            <td class="project-2">-</td>
            <td class="project-3">-</td>
            <td class="project-4">-</td>
            <td class="project-5">-</td>
            <td class="project-6">-</td>
            <td class="project-7">-</td>
            <td class="project-8">-</td>
        </tr>
        <tr>
            <td class="criteria">-</td>
            <td class="our-project">-</td>
            <td class="project-1">-</td>
            <td class="project-2">-</td>
            <td class="project-3">-</td>
            <td class="project-4">-</td>
            <td class="project-5">-</td>
            <td class="project-6">-</td>
            <td class="project-7">-</td>
            <td class="project-8">-</td>
        </tr>
        <tr>
            <td class="criteria">-</td>
            <td class="our-project">-</td>
            <td class="project-1">-</td>
            <td class="project-2">-</td>
            <td class="project-3">-</td>
            <td class="project-4">-</td>
            <td class="project-5">-</td>
            <td class="project-6">-</td>
            <td class="project-7">-</td>
            <td class="project-8">-</td>
        </tr>
        <tr>
            <td class="criteria">-</td>
            <td class="our-project">-</td>
            <td class="project-1">-</td>
            <td class="project-2">-</td>
            <td class="project-3">-</td>
            <td class="project-4">-</td>
            <td class="project-5">-</td>
            <td class="project-6">-</td>
            <td class="project-7">-</td>
            <td class="project-8">-</td>
        </tr>
 <tr>
    <td class="Вимоги" rowspan=5><strong>Usability (зручність роботи)</strong></td>
    <td class="Критерії"><strong>User-friendly interface</strong></td>
    <td class="SigmaTasking (Наш Проєкт)">&#10004;</td>
    <td class="GitHub Projects">&#10004;</td>
    <td class="Notion">&#10004;</td>
    <td class="Trello">&#10004;</td>
    <td class="JIRA">&#10004;</td>
    <td class="Asana">&#10004;</td>
    <td class="Nift">&#10004;</td>
    <td class="Microsoft Project">&#10004;</td>
    <td class="Click Up">&#10004;</td>
</tr>
<tr>
    <td class="criteria"><strong>Багатомовність</strong></td>
    <td class="SigmaTasking (Наш Проєкт)">&#10004;</td>
    <td class="GitHub Projects">&#10008;</td>
    <td class="Notion">&#10004;</td>
    <td class="Trello">&#10008;</td>
    <td class="JIRA">&#10004;</td>
    <td class="Asana">&#10004;</td>
    <td class="Nift">&#10004;</td>
    <td class="Microsoft Project">&#10008;</td>
    <td class="Click Up">&#10004;</td>
</tr>
<tr>
    <td class="criteria"><strong>Інтеграція з Github</strong></td>
    <td class="SigmaTasking (Наш Проєкт)">&#10004;</td>
    <td class="GitHub Projects">&#10004;</td>
    <td class="Notion">&#10004;</td>
    <td class="Trello">&#10008;</td>
    <td class="JIRA">&#10004;</td>
    <td class="Asana">&#10008;</td>
    <td class="Nift">&#10004;</td>
    <td class="Microsoft Project">&#10008;</td>
    <td class="Click Up">&#10004;</td>
</tr>
<tr>
    <td class="criteria"><strong>Ведення паралельно кількох проєктів</strong></td>
    <td class="SigmaTasking (Наш Проєкт)">&#10004;</td>
    <td class="GitHub Projects">&#10008;</td>
    <td class="Notion">&#10004;</td>
    <td class="Trello">&#10004;</td>
    <td class="JIRA">&#10008;</td>
    <td class="Asana">&#10004;</td>
    <td class="Nift">&#10008;</td>
    <td class="Microsoft Project">&#10004;</td>
    <td class="Click Up">&#10008;</td>
</tr>
<tr>
    <td class="criteria"><strong>Доступ до дошки без реєстрації</strong></td>
    <td class="SigmaTasking (Наш Проєкт)">&#10008;</td>
    <td class="GitHub Projects">&#10008;</td>
    <td class="Notion">&#10008;</td>
    <td class="Trello">&#10008;</td>
    <td class="JIRA">&#10008;</td>
    <td class="Asana">&#10004;</td>
    <td class="Nift">&#10008;</td>
    <td class="Microsoft Project">&#10008;</td>
    <td class="Click Up">&#10004;</td>
</tr>

<tr>
    <td class="requirements" rowspan=6><strong>Reliability (надійність)</strong></td>
    <td class="criteria"><strong>Резервне копіювання</strong></td>
    <td class="our-project">&#10004;</td>
    <td class="project-1">&#10004;</td>
    <td class="project-2">&#10004;</td>
    <td class="project-3">&#10004;</td>
    <td class="project-4">&#10004;</td>
    <td class="project-5">&#10004;</td>
    <td class="project-6">&#10004;</td>
    <td class="project-7">&#10004;</td>
    <td class="project-8">&#10004;</td>
</tr>
<tr>
    <td class="criteria"><strong>Швидкість виправлення багів</strong></td>
    <td class="our-project">&#10004;</td>
    <td class="project-1">&#10004;</td>
    <td class="project-2">&#10004;</td>
    <td class="project-3">&#10004;</td>
    <td class="project-4">&#10004;</td>
    <td class="project-5">&#10004;</td>
    <td class="project-6">&#10004;</td>
    <td class="project-7">&#10004;</td>
    <td class="project-8">&#10004;</td>
</tr>
<tr>
    <td class="criteria"><strong>Приватні проєкти</strong></td>
    <td class="our-project">&#10004;</td>
    <td class="project-1">&#10004;</td>
    <td class="project-2">&#10004;</td>
    <td class="project-3">&#10008;</td>
    <td class="project-4">&#10004;</td>
    <td class="project-5">&#10004;</td>
    <td class="project-6">&#10008;</td>
    <td class="project-7">&#10004;</td>
    <td class="project-8">&#10004;</td>
</tr>
<tr>
    <td class="criteria"><strong>Історія зміни проєктів</strong></td>
    <td class="our-project">&#10004;</td>
    <td class="project-1">&#10004;</td>
    <td class="project-2">&#10004;</td>
    <td class="project-3">&#10008;</td>
    <td class="project-4">&#10004;</td>
    <td class="project-5">&#10004;</td>
    <td class="project-6">&#10004;</td>
    <td class="project-7">&#10004;</td>
    <td class="project-8">&#10004;</td>
</tr>
<tr>
    <td class="criteria"><strong>Протокол шифрування</strong></td>
    <td class="our-project">TLS</td>
    <td class="project-1">TLS</td>
    <td class="project-2">TLS</td>
    <td class="project-3">TLS</td>
    <td class="project-4">TLS</td>
    <td class="project-5">TLS</td>
    <td class="project-6">TLS</td>
    <td class="project-7">TLS</td>
    <td class="project-8">TLS</td>
</tr>
<tr>
    <td class="criteria"><strong>Багаторівнева автентифікація</strong></td>
    <td class="our-project">&#10004;</td>
    <td class="project-1">&#10004;</td>
    <td class="project-2">&#10004;</td>
    <td class="project-3">&#10004;</td>
    <td class="project-4">&#10004;</td>
    <td class="project-5">&#10004;</td>
    <td class="project-6">&#10004;</td>
    <td class="project-7">&#10004;</td>
    <td class="project-8">&#10004;</td>
</tr>
        <!-- new requirement -->
        <tr>
            <td class="requirements" rowspan=6>Performance (продуктивність)</td>
            <td class="criteria">-</td>
            <td class="our-project">-</td>
            <td class="project-1">-</td>
            <td class="project-2">-</td>
            <td class="project-3">-</td>
            <td class="project-4">-</td>
            <td class="project-5">-</td>
            <td class="project-6">-</td>
            <td class="project-7">-</td>
            <td class="project-8">-</td>
        </tr>
        <tr>
            <td class="criteria">-</td>
            <td class="our-project">-</td>
            <td class="project-1">-</td>
            <td class="project-2">-</td>
            <td class="project-3">-</td>
            <td class="project-4">-</td>
            <td class="project-5">-</td>
            <td class="project-6">-</td>
            <td class="project-7">-</td>
            <td class="project-8">-</td>
        </tr>
        <tr>
            <td class="criteria">-</td>
            <td class="our-project">-</td>
            <td class="project-1">-</td>
            <td class="project-2">-</td>
            <td class="project-3">-</td>
            <td class="project-4">-</td>
            <td class="project-5">-</td>
            <td class="project-6">-</td>
            <td class="project-7">-</td>
            <td class="project-8">-</td>
        </tr>
        <tr>
            <td class="criteria">-</td>
            <td class="our-project">-</td>
            <td class="project-1">-</td>
            <td class="project-2">-</td>
            <td class="project-3">-</td>
            <td class="project-4">-</td>
            <td class="project-5">-</td>
            <td class="project-6">-</td>
            <td class="project-7">-</td>
            <td class="project-8">-</td>
        </tr>
        <tr>
            <td class="criteria">-</td>
            <td class="our-project">-</td>
            <td class="project-1">-</td>
            <td class="project-2">-</td>
            <td class="project-3">-</td>
            <td class="project-4">-</td>
            <td class="project-5">-</td>
            <td class="project-6">-</td>
            <td class="project-7">-</td>
            <td class="project-8">-</td>
        </tr>
        <tr>
            <td class="criteria">-</td>
            <td class="our-project">-</td>
            <td class="project-1">-</td>
            <td class="project-2">-</td>
            <td class="project-3">-</td>
            <td class="project-4">-</td>
            <td class="project-5">-</td>
            <td class="project-6">-</td>
            <td class="project-7">-</td>
            <td class="project-8">-</td>
        </tr>
        <!-- new requirement -->
        <tr>
           <tr>
            <td class="requirements" rowspan=6>Supportability (підтримка)</td>
            <th class="criteria"><strong>Документація</strong></th>
            <td class="our-project">✖</td>
            <td class="project-1">✔</td>
            <td class="project-2">✔</td>
            <td class="project-3">✖</td>
            <td class="project-4">✔</td>
            <td class="project-5">✔</td>
            <td class="project-6">✔</td>
            <td class="project-7">✔</td>
            <td class="project-8">✔</td>
        </tr>
        <tr>
            <td class="criteria"><strong>Технічна підтримка</strong></td>
            <td class="our-project">✖</td>
            <td class="project-1">✖</td>
            <td class="project-2">✔</td>
            <td class="project-3">✖</td>
            <td class="project-4">✔</td>
            <td class="project-5">✔</td>
            <td class="project-6">✔</td>
            <td class="project-7">✔</td>
            <td class="project-8">✔</td>
        </tr>
        <tr>
            <td class="criteria"><strong>Форум/спільнота</strong></td>
            <td class="our-project">✖</td>
            <td class="project-1">✖</td>
            <td class="project-2">✔</td>
            <td class="project-3">✖</td>
            <td class="project-4">✔</td>
            <td class="project-5">✔</td>
            <td class="project-6">✔</td>
            <td class="project-7">✖</td>
            <td class="project-8">✔</td>
        </tr>
        <tr>
            <td class="criteria"><strong>Відеоуроки</strong></td>
            <td class="our-project">✖</td>
            <td class="project-1">✖</td>
            <td class="project-2">✔</td>
            <td class="project-3">✖</td>
            <td class="project-4">✖</td>
            <td class="project-5">✔</td>
            <td class="project-6">✔</td>
            <td class="project-7">✖</td>
            <td class="project-8">✔</td>
        </tr>
        <tr>
            <td class="criteria"><strong>Часті оновлення</strong></td>
            <td class="our-project">✖</td>
            <td class="project-1">✔</td>
            <td class="project-2">✔</td>
            <td class="project-3">✔</td>
            <td class="project-4">✔</td>
            <td class="project-5">✔</td>
            <td class="project-6">✔</td>
            <td class="project-7">✔</td>
            <td class="project-8">✔</td>
        </tr>
        <tr>
            <td class="criteria"><strong>Наявність FAQ</strong></td>
            <td class="our-project">✖</td>
            <td class="project-1">✔</td>
            <td class="project-2">✔</td>
            <td class="project-3">✖</td>
            <td class="project-4">✔</td>
            <td class="project-5">✔</td>
            <td class="project-6">✔</td>
            <td class="project-7">✔</td>
            <td class="project-8">✔</td>
        </tr>
    </tbody>
</table>



## Висновки

<p>Ринок інструментів для управління проєктами стикається з певними недоліками. Багато популярних сервісів не надають важливих функцій, як-от підтримка артефактів, що може бути вирішальним для певних користувачів або конкретних сценаріїв застосування.

Крім того, наявність ключових функцій лише в платних версіях платформ обмежує їхню доступність для невеликих компаній і індивідуальних розробників, що робить ці інструменти менш привабливими для широкої аудиторії.

Таким чином, розробка нової платформи, яка врахує ці прогалини та запропонує додаткові можливості, виглядає доцільною. Такий інструмент, орієнтований на реальні потреби користувачів і надання тих функцій, яких бракує іншим рішенням, має шанси здобути свою аудиторію та успіх на ринку.</p>

## Посилання

*[Розділ містить повний список всіх документів, про які згадується.]*
