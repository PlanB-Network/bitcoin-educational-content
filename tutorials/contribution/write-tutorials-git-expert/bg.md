---
name: Принос - Урок по Git (за напреднали)
description: Ръководство за напреднали потребители, предлагащо урок за Plan ₿ Academy с Git
---
![cover](assets/cover.webp)


Преди да проследите този урок за добавяне на нов урок, трябва да сте изпълнили няколко предварителни стъпки. Ако все още не сте го направили, моля, първо разгледайте този уводен урок, след което се върнете тук:


https://planb.academy/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Вече имате:



- Изберете тема за урока си;
- Свържете се с екипа на Plan ₿ Academy чрез [Telegram group](https://t.me/PlanBNetwork_ContentBuilder) или paolo@planb.network ;
- Изберете инструменти за принос.


В този урок за опитни потребители на Git ще обобщим накратко основните стъпки и основните насоки за предлагане на нов урок в Plan ₿ Academy. Ако не сте запознати с Git и GitHub, препоръчвам ви вместо това да следвате един от тези други 2 по-подробни урока, които ще ви преведат стъпка по стъпка:



- Междинен продукт (GitHub Desktop):


https://planb.academy/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957


- За начинаещи (уеб интерфейс):


https://planb.academy/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## Предлагани инструменти


За редактиране на файлове Markdown:



- Obsidian (безплатно, не с отворен код)
- Mark Text (безплатен, с отворен код)
- Zettlr (безплатно, с отворен код)
- Typora (Payware, ~15 евро, не е с отворен код)


За Git:



- Git (безплатен, с отворен код)
- GitHub Desktop (безплатно, с отворен код)
- Sourcetree (безплатно, не е с отворен код)


За редактиране на YAML файлове:



- Visual Studio Code (безплатно, с отворен код)
- Sublime Text (безплатен с ограничения, не е с отворен код)


Създаване на диаграми и визуализации:



- Canva (безплатна с платени опции, не е с отворен код)
- Inkscape (безплатно, с отворен код)
- Penpot (безплатно, с отворен код)


## Работни потоци


### 1 - Конфигуриране на локалната среда



- Трябва да разполагате със собствена fork на [хранилището на Plan ₿ Academy в GitHub](https://github.com/PlanB-Network/bitcoin-educational-content).
- Синхронизирайте главния клон (`dev`) на вашия fork с хранилището на изходния код.
- Актуализирайте локалния си клонинг.


```
# Clone your fork (if not already done)
git clone https://github.com/<your-username>/bitcoin-educational-content.git
cd bitcoin-educational-content

# Add the source repository as a remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git

# Fetch the latest changes from the source repository
git fetch upstream

# Switch to the main 'dev' branch
git checkout dev

# Merge the changes from the source repository's 'dev' branch into your fork
git merge upstream/dev

# Push the updates to your fork on GitHub
git push origin dev
```


### 2 - Създаване на нов клон



- Уверете се, че сте в клона `dev`.
- Създайте нов клон с описателно име (напр. `tuto-green-wallet-loic`).
- Публикувайте този клон във вашия онлайн регистър fork.


```
# Make sure you are on the 'dev' branch
git checkout dev

# Create a new branch with a descriptive name
git checkout -b tuto-green-wallet-loic

# Publish this branch to your online fork
git push -u origin tuto-green-wallet-loic
```


### 3 - Добавяне на документите за обучение


***Забележка:*** Можете да автоматизирате стъпки 3 и 4, като използвате [моя скрипт за графичен потребителски интерфейс на Python](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation). Стартирайте го директно от папката му в локалния си клонинг, след което попълнете необходимите полета в графичния потребителски интерфейс. За повече информация как да го инсталирате и използвате, вижте [README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).


Ако предпочитате да го направите ръчно, следвайте следните стъпки:



- Намерете подходящата папка в местното хранилище (например `tutorials/wallet`).
- Създайте директория, посветена на урока, с ясно име (напр. `green-wallet`). Това име на папката ще определи и URL пътя на урока. То трябва да бъде написано с малки букви, без специални знаци (освен тирета) и без интервали.
- Добавете следните елементи в тази директория:
    - Подпапка с име `assets`, съдържаща:
        - Две изображения `.webp`:
            - `logo.webp`: Логото на урока (квадратен формат с фон). Това лого трябва да представя представения софтуер или инструмент. Ако ръководството не е специфично за даден инструмент (например: общо ръководство за генериране на мнемонична фраза), можете да изберете подходяща визуална форма (например: обща икона).
            - `cover.webp`: Изображение на корицата, което се показва в началото на урока.
        - Подпапка, съдържаща кода на оригиналния език на учебника. Например, ако урокът е написан на английски език, тази подпапка трябва да се нарича `en'. Поставете всички визуални материали на урока (диаграми, изображения, снимки на екрана и т.н.) в тази папка.
    - Файл `tutorial.yml`, съдържащ метаданни (автор, тагове, категория, ниво на трудност и т.н.).
    - Файл Markdown, съдържащ урока, с име според кода на езика (например `fr.md`, `en.md` и т.н.).


```
# Navigate to the appropriate folder
cd tutorials/wallet

# Create the directory dedicated to the tutorial
mkdir green-wallet
cd green-wallet

# Create the 'assets' subfolder
mkdir -p assets

# Create the subfolder for the original language code (e.g., 'en' for English)
mkdir -p assets/en

# Create the metadata file and the Markdown tutorial file (e.g., 'en.md' for English)
touch tutorial.yml en.md
```


### 4 - Попълване на файла YAML



- Попълнете файла `tutorial.yml`, както следва:


```
id:

project_id:

tags:
-
-
-

category:

level:

professor_id:

# Proofreading metadata

original_language:
proofreading:
- language:
last_contribution_date:
urgency:
contributor_names:
-
reward:
```


Ето задължителните полета:



- id**: UUID (_Универсален уникален идентификатор_), който идентифицира уникално урока. Можете да го generate, като използвате [онлайн инструмент](https://www.uuidgenerator.net/version4). Единственото изискване е този UUID да е произволен, за да се избегнат конфликти с друг UUID в платформата;



- project_id**: UUID на компанията или организацията, която стои зад инструмента, представен в урока [от списъка с проекти](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Например, ако създавате урок за софтуера Green Wallet, можете да намерите този `project_id` в следния файл: `bitcoin-educational-content/resources/projects/blockstream/project.yml`. Тази информация е добавена към YAML файла на вашия урок, защото Plan ₿ Academy поддържа база данни на всички компании и организации, работещи по Bitcoin или свързани проекти. Като добавяте `project_id` на организацията, свързана с вашия урок, вие създавате връзка между двата елемента;



- тагове**: 2 или 3 релевантни ключови думи, свързани със съдържанието на урока, избрани изключително [от списъка с тагове на Plan ₿ Academy](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);



- категория**: Подкатегорията, съответстваща на съдържанието на урока, съгласно структурата на уебсайта на Plan ₿ Academy (например за портфейли: `desktop`, `hardware`, `mobile`, `backup`);



- ниво**: Нивото на трудност на урока, избрано от:
    - `начинаещ`
    - `intermediate`
    - `напреднали`
    - `expert`



- professor_id**: Вашият `professor_id` (UUID), както е показан в [профила на вашия професор](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors);



- original_language**: Оригиналният език на урока (напр., `fr`, `en` и т.н.);



- корекция**: Информация за процеса на коригиране. Попълнете първата част, тъй като коригирането на собствения ви учебник се счита за първо валидиране:
    - език**: Код на езика, на който е направена корекцията (напр. `fr`, `en` и др.).
    - last_contribution_date**: Дата от деня.
    - спешност**: 1
    - contributor_names**: Вашият идентификационен номер в GitHub.
    - награда**: 0


За повече подробности относно идентификатора на учителя, моля, вижте съответния урок:


https://planb.academy/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

```
id: e84edaa9-fb65-48c1-a357-8a5f27996143

project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8

tags:
- wallets
- software
- keys

category: mobile

level: beginner

professor_id: 6516474c-c190-41f2-b2ab-3d452ce7bdf0

# Proofreading metadata

original_language: fr
proofreading:
- language: fr
last_contribution_date: 2024-11-20
urgency: 1
contributor_names:
- LoicPandul
reward: 0
```


### 5 - Напишете съдържанието



- Попълнете свойствата на файла Markdown с:
    - Заглавието (`name`).
    - Кратко описание (`description`).
- Добавете заглавното изображение в горната част на урока, като използвате синтаксиса на Markdown (заменете "green" с името на показания инструмент):


```
![cover-green](assets/cover.webp)
```



- Напишете съдържанието на урока в Markdown:
    - Използвайте добре структурирани заглавия (`##`), списъци и параграфи.
    - Вмъкване на визуализации с помощта на синтаксиса на Markdown:


```
![nom-image](assets/en/001.webp)
```




- Поставете диаграмите и изображенията в подпапка на съответния език в `/assets`.


### 6 - Запазване и изпращане на урока



- Запазете промените си локално, като създадете commit с описателно съобщение.
- Изпратете промените в своя GitHub fork.


```
# Create a commit with a descriptive message
git commit -m "Added green-wallet tutorial"

# Push your changes to your fork
git push origin tuto-green-wallet-loic
```



- След като приключите, създайте заявка за изтегляне (PR) в GitHub, за да предложите интегрирането на вашите модификации.
- Добавете заглавие и кратко описание на PR. В коментара посочете съответния номер на изданието.


### 7 - Корекция и обединяване



- Изчакайте потвърждение или обратна връзка от администратор.
- Ако е необходимо, направете корекции и изпратете нови коммисии.


```
# Create a commit describing the corrections made
git commit -m "Corrections following the review of the green-wallet tutorial"

# Push the corrections to your fork
git push origin tuto-green-wallet-loic
```



- След като PR-ът бъде обединен, можете да изтриете работния клон.


## Стандарти за създаване на съдържание



- Форматиране, поддържано от платформата**:
    - Класически Markdown: списъци, връзки, изображения, кавички, удебелен шрифт, курсив и др.
    - LaTeX (само блоково, не inline): ограничено с `$$`.
    - Вграден код: Синтаксис с една задна чертичка.
    - Кодови блокове: Синтаксис с три задни тирета, например:


```
print("Hello, Bitcoin!")
```



- Илюстрации и диаграми**:
    - Всички изображения трябва да са във формат WebP. Използвайте този безплатен инструмент, за да ги конвертирате, ако е необходимо: [ImagesConverter](https://github.com/LoicPandul/ImagesConverter).
    - Именувайте визуализациите с 2 или 3 цифри (напр. `001.webp`, `002.webp`).
    - За уроци за мобилни устройства или хардуер wallet използвайте макети.
    - Използвайте само самостоятелно създадени или безплатни визуализации.
    - Уверете се, че те са подходящи и с високо качество.
- Графична харта**:
    - Шрифт: [IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans).
    - Colors Plan ₿ Академия:
        - Оранжево: `#FF5C00`
        - Черно: `#000000`
        - Бяло: `#FFFFFF`


Ако имате технически затруднения при изпращането на ръководство, моля, не се колебайте да помолите за помощ в [нашата специална група Telegram за принос](https://t.me/PlanBNetwork_ContentBuilder). Благодаря ви много!