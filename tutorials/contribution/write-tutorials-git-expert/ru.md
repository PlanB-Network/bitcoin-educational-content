---
name: Вклад - учебник по Git (продвинутый)
description: Руководство для опытных пользователей, предлагающее учебник по плану ₿ Сеть с Git
---
![cover](assets/cover.webp)

Прежде чем следовать этому руководству по добавлению нового учебника, вам необходимо выполнить несколько предварительных шагов. Если вы еще не сделали этого, ознакомьтесь сначала с этим вводным уроком, а затем вернитесь сюда:

https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

У вас уже есть :


- Выберите тему для своего учебника;
- Свяжитесь с командой Plan ₿ Network через [группу Telegram](https://t.me/PlanBNetwork_ContentBuilder) или paolo@planb.network ;
- Выберите инструменты для внесения средств.

В этом руководстве для опытных пользователей Git мы кратко опишем ключевые шаги и основные принципы создания нового плана ₿ Сетевой учебник. Если вы не знакомы с Git и GitHub, я рекомендую вам воспользоваться одним из двух других более подробных руководств, которые расскажут вам шаг за шагом:


- Промежуточный уровень (GitHub Desktop)** :

https://planb.network/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

- Новички (веб-интерфейс)** :

https://planb.network/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## Предлагаемые инструменты

Для редактирования файлов Markdown :


- Obsidian** (бесплатно, не с открытым исходным кодом)
- Mark Text** (бесплатно, с открытым исходным кодом)
- Zettlr** (бесплатно, с открытым исходным кодом)
- Typora** (платная программа, ~15 евро, не с открытым исходным кодом)

Для Git :


- Git** (бесплатно, с открытым исходным кодом)
- GitHub Desktop** (бесплатно, с открытым исходным кодом)
- Sourcetree** (бесплатно, не с открытым исходным кодом)

Для редактирования файлов YAML :


- Visual Studio Code** (бесплатно, с открытым исходным кодом)
- Sublime Text** (бесплатно с ограничениями, не с открытым исходным кодом)

Для создания диаграмм и визуальных эффектов:


- Canva** (бесплатно с платными опциями, не с открытым исходным кодом)
- Inkscape** (бесплатно, с открытым исходным кодом)
- Penpot** (бесплатно, с открытым исходным кодом)

## Рабочие процессы

### 1 - Настройка локальной среды


- У вас должен быть собственный форк [репозитория Plan ₿ Network на GitHub](https://github.com/PlanB-Network/bitcoin-educational-content).
- Синхронизируйте основную ветку (`dev`) вашего форка с репозиторием исходных текстов.
- Обновите локальный клон.

```
# Cloner votre fork (si ce n'est pas déjà fait)
git clone https://github.com/<votre-nom-utilisateur>/bitcoin-educational-content.git
cd bitcoin-educational-content
# Ajouter le dépôt source en tant que remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git
# Récupérer les dernières modifications depuis le dépôt source
git fetch upstream
# Se positionner sur la branche principale 'dev'
git checkout dev
# Fusionner les modifications de la branche 'dev' du dépôt source dans votre fork
git merge upstream/dev
# Pousser les mises à jour vers votre fork sur GitHub
git push origin dev
```

### 2 - Создайте новую ветку


- Убедитесь, что вы находитесь на ветке `dev`.
- Создайте новую ветку с описательным именем (например, `tuto-green-wallet-loic`).
- Опубликуйте эту ветку на своем онлайн-форке.

```
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b tuto-green-wallet-loic
# Publiez cette branche sur votre fork en ligne
git push -u origin tuto-green-wallet-loic
```

### 3 - Добавьте учебные документы

***Примечание:*** Вы можете автоматизировать шаги 3 и 4 с помощью [моего скрипта Python GUI](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation). Запустите его прямо из папки в локальном клоне, а затем заполните необходимые поля в графическом интерфейсе. Более подробную информацию о том, как его установить и использовать, вы найдете в [README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).

Если вы предпочитаете делать это вручную, выполните следующие действия:


- Найдите соответствующую папку в локальном хранилище (например, `tutorials/wallet`).
- Создайте директорию, предназначенную для учебника, с понятным именем (например, `green-wallet`). Это имя папки также будет определять URL-путь учебника. Оно должно быть в нижнем регистре, без специальных символов (кроме дефиса) и пробелов.
- Добавьте в этот каталог следующие элементы:
    - Вложенная папка с именем `assets`, содержащая :
        - Два изображения формата `.webp`:
            - `logo.webp`: Логотип учебника (квадратный формат с фоном). Этот логотип должен представлять программное обеспечение или инструмент. Если учебник не относится к какому-либо инструменту (например, общее руководство по созданию мнемонической фразы), вы можете выбрать подходящий визуальный образ (например, общий значок).
            - `cover.webp`: Изображение обложки, отображаемое в начале учебника.
        - Вложенная папка с кодом языка, на котором написан учебник. Например, если учебник написан на английском языке, эта папка должна называться `en'. Поместите в эту папку все визуальные материалы учебника (диаграммы, изображения, скриншоты и т. д.).
    - Файл `tutorial.yml`, содержащий метаданные (автор, теги, категория, уровень сложности и т.д.).
    - Файл в формате Markdown, содержащий учебник и названный в соответствии с кодом языка (например, `fr.md`, `en.md` и т.д.).

```
# Positionnez-vous dans le dossier approprié
cd tutorials/wallet
# Créez le répertoire dédié au tutoriel
mkdir green-wallet
cd green-wallet
# Créez le sous-dossier 'assets'
mkdir -p assets
# Créez le sous-dossier pour le code de la langue d’origine (exemple : 'en' pour l’anglais)
mkdir -p assets/en
# Créez les fichiers de métadonnées et le tutoriel Markdown (exemple : 'en.md' pour l’anglais)
touch tutorial.yml en.md
```

### 4 - Заполните файл YAML


- Заполните файл `tutorial.yml` следующим образом:

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

Вот обязательные поля:

- **id** : UUID (_Универсально уникальный идентификатор_), который позволяет уникально идентифицировать учебник. Вы можете сгенерировать его с помощью [онлайн-инструмента](https://www.uuidgenerator.net/version4). Единственное требование заключается в том, чтобы этот UUID был случайным, чтобы избежать конфликта с другим UUID на платформе;

- **project_id** : UUID компании или организации, стоящей за инструментом, представленным в учебнике [из списка проектов](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Например, если вы создаете учебник о программном обеспечении Green Wallet, вы можете найти этот `project_id` в следующем файле: `bitcoin-educational-content/resources/projects/blockstream/project.yml`. Эта информация добавляется в YAML файл вашего учебника, так как Plan ₿ Network поддерживает базу данных всех компаний и организаций, работающих с Биткоином или связанными проектами. Добавляя `project_id` связанной с вашим учебником сущности, вы создаете связь между этими элементами;

- **tags** : 2 или 3 ключевых слова, связанных с содержанием учебника, выбранных исключительно [из списка тегов Plan ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);

- **category** : Подкатегория, соответствующая содержанию учебника, в соответствии с структурой сайта Plan ₿ Network (например, для кошельков: `desktop`, `hardware`, `mobile`, `backup`);

- **level** : Уровень сложности учебника, выбираемый из:
    - `beginner`
    - `intermediate`
    - `advanced`
    - `expert`

- **professor_id** : Ваш `professor_id` (UUID), как указано в [вашем профиле преподавателя](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors);

- **original_language** : Оригинальный язык учебника (например, `fr`, `en`, и т. д.);

- **proofreading** : Информация о процессе корректуры. Заполните первую часть, так как корректура вашего собственного учебника считается первой проверкой:
    - **language** : Код языка корректуры (например, `fr`, `en`, и т. д.).
    - **last_contribution_date** : Дата текущего дня.
    - **urgency** : 1
    - **contributor_names** : Ваш GitHub ID.
    - **reward** : 0

Для получения более подробной информации об идентификаторе учителя обратитесь к соответствующему руководству:

https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

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

### 5 - Напишите содержание


- Заполните свойства файла Markdown с помощью :
    - Название (`name`).
    - Краткое описание (`description`).
- Добавьте изображение обложки в верхней части руководства, используя синтаксис Markdown (замените "green" на название показанного инструмента):

```
![cover-green](assets/cover.webp)
```


- Напишите содержание учебника в формате Markdown:
    - Используйте хорошо структурированные заголовки (`##`), списки и абзацы.
    - Вставка визуальных элементов с помощью синтаксиса Markdown :

```
![nom-image](assets/en/001.webp)
```


- Поместите диаграммы и изображения в подпапку соответствующего языка в `/assets`.

### 6 - Сохранить и отправить учебник


- Сохраните изменения локально, создав коммит с описательным сообщением.
- Внесите изменения в свой форк на GitHub.

```
# Créez un commit avec un message descriptif
git commit -m "Ajout du tutoriel green-wallet"
# Poussez vos modifications sur votre fork
git push origin tuto-green-wallet-loic
```


- После завершения работы создайте Pull Request (PR) на GitHub, чтобы предложить интеграцию ваших модификаций.
- Добавьте к PR заголовок и краткое описание. В комментарии укажите номер соответствующего выпуска.

### 7 - Вычитка и объединение


- Дождитесь подтверждения или обратной связи от администратора.
- Если необходимо, внесите исправления и выложите новые коммиты.

```
# Créez un commit décrivant les corrections apportées
git commit -m "Corrections suite à la revue du tutoriel green-wallet"
# Poussez les corrections sur votre fork
git push origin tuto-green-wallet-loic
```


- После слияния PR вы можете удалить свою рабочую ветку.

## Стандарты создания контента


- Форматирование, поддерживаемое платформой** :
    - Классический Markdown: списки, ссылки, изображения, кавычки, жирный шрифт, курсив и т.д.
    - LaTeX (только блок, не инлайн): разделены `$$`.
    - Встроенный код: Синтаксис с одним обратным знаком.
    - Кодовые блоки: Синтаксис с тремя обратными знаками, например :

```
print("Hello, Bitcoin!")
```


- Иллюстрации и диаграммы** :
    - Все изображения должны быть в формате WebP. При необходимости используйте этот бесплатный инструмент для их конвертации: [ImagesConverter](https://github.com/LoicPandul/ImagesConverter).
    - Назовите визуальные объекты с помощью 2 или 3 цифр (например, `001.webp`, `002.webp`).
    - Для уроков по мобильным или аппаратным кошелькам используйте макеты.
    - Используйте только созданные самостоятельно или безвозмездно визуальные материалы.
    - Убедитесь, что они актуальны и качественны.
- Графический устав** :
    - Шрифт: [Rubik](https://fonts.google.com/specimen/Rubik).
    - План цветов ₿ Сеть :
        - Оранжевый: `#FF5C00`
        - Черный: `#000000`
        - Белый: `#FFFFFF`

Если у вас возникли технические трудности с отправкой урока, пожалуйста, не стесняйтесь просить помощи в [нашей специальной группе Telegram для вкладов](https://t.me/PlanBNetwork_ContentBuilder). Большое спасибо!