---
name: Вклад - Самоучитель работы с GitHub Desktop (средний уровень)
description: Полное руководство по созданию учебника по Plan ₿ Network с помощью GitHub Desktop
---
![cover](assets/cover.webp)

Прежде чем следовать этому руководству по добавлению нового учебника, вы должны выполнить несколько предварительных шагов. Если вы еще не сделали этого, я приглашаю вас сначала ознакомиться с этим вводным уроком, а затем вернуться сюда:

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2
Вы уже сделали это:


- Выберите тему вашего учебника;
- Свяжитесь с командой Plan ₿ Network через [группу Telegram](https://t.me/PlanBNetwork_ContentBuilder) или paolo@planb.network;
- Выберите инструменты для внесения вклада.

В этом уроке мы рассмотрим, как добавить свой учебник в Plan ₿ Network, настроив локальную среду с помощью GitHub Desktop. Если вы уже умеете работать с Git, то этот очень подробный учебник может вам не понадобиться. Я бы рекомендовал обратиться к другому руководству, в котором я излагаю только основные принципы, без подробных пошаговых инструкций:


- Опытные пользователи**:

https://planb.network/tutorials/others/contribution/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410
Если вы предпочитаете не настраивать локальное окружение, следуйте другому руководству, предназначенному для новичков, где мы вносим изменения непосредственно через веб-интерфейс GitHub:


- Новички (веб-интерфейс)**:

https://planb.network/tutorials/others/contribution/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79
## Пререквизиты

Программное обеспечение, необходимое для выполнения данного руководства:


- [GitHub Desktop](https://desktop.github.com/);
- Редактор файлов в формате markdown, например [Obsidian](https://obsidian.md/);
- Редактор кода ([VSC](https://code.visualstudio.com/) или [Sublime Text](https://www.sublimetext.com/)).

![TUTO](assets/fr/01.webp)

Прежде чем приступить к изучению учебника, необходимо выполнить предварительные условия:


- Иметь аккаунт [GitHub](https://github.com/signup);
- Сделайте форк репозитория [Plan ₿ Network source repository](https://github.com/PlanB-Network/bitcoin-educational-content);
- Иметь [профиль профессора в Plan ₿ Network](https://planb.network/professors) (только если вы предлагаете полное учебное пособие).

Если вам нужна помощь в получении этих необходимых условий, вам помогут другие мои учебники:

https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb
Как только все будет готово и в вашем локальном окружении будет правильно настроен ваш собственный форк Plan ₿ Network, вы сможете приступить к добавлению учебника.

## 1 - Создайте новую ветку

Откройте браузер и перейдите на страницу вашего форка репозитория Plan ₿ Network. Это форк, который вы создали на GitHub. URL-адрес вашего форка должен выглядеть следующим образом: `https://github.com/[ваше имя пользователя]/bitcoin-educational-content`:

![TUTO](assets/fr/03.webp)

Убедитесь, что вы находитесь на основной ветке `dev`, затем нажмите на кнопку `Sync fork`. Если ваш форк не обновлен, GitHub предложит обновить вашу ветку. Выполните это обновление. Если же, наоборот, ваша ветка уже обновлена, GitHub сообщит вам об этом:

![TUTO](assets/fr/04.webp)

Откройте программу GitHub Desktop и убедитесь, что ваш форк правильно выбран в левом верхнем углу окна:

![TUTO](assets/fr/05.webp)

Нажмите на кнопку `Fetch origin`. Если ваш локальный репозиторий уже обновлен, GitHub Desktop не предложит никаких дополнительных действий. В противном случае появится опция `Pull origin`. Нажмите на эту кнопку, чтобы обновить локальный репозиторий:

![TUTO](assets/fr/06.webp)

Убедитесь, что вы действительно находитесь в основной ветке `dev`:

![TUTO](assets/fr/07.webp)

Выберите эту ветку, затем нажмите на кнопку `Новая ветка`:

![TUTO](assets/fr/08.webp)

Убедитесь, что новая ветка основана на исходном репозитории, а именно `PlanB-Network/bitcoin-educational-content`.

Назовите свою ветку так, чтобы из названия была понятна ее цель, используя тире для разделения каждого слова. Например, допустим, наша цель - написать учебник по использованию программного обеспечения Sparrow Wallet. В этом случае рабочую ветку, предназначенную для написания этого руководства, можно назвать: `tuto-sparrow-wallet-loic`. После ввода подходящего имени нажмите на `Создать ветку`, чтобы подтвердить создание ветки:

![TUTO](assets/fr/09.webp)

Теперь нажмите на кнопку `Publish branch`, чтобы сохранить новую рабочую ветку в вашем онлайн форке на GitHub:

![TUTORIAL](assets/fr/10.webp)

Теперь на рабочем столе GitHub вы должны оказаться в новой ветке. Это означает, что все изменения, сделанные локально на вашем компьютере, будут сохраняться исключительно в этой ветке. Кроме того, пока эта ветка остается выбранной на GitHub Desktop, файлы, видимые локально на вашем компьютере, соответствуют файлам этой ветки (`tuto-sparrow-wallet-loic`), а не основной ветки (`dev`).

![TUTORIAL](assets/fr/11.webp)

Для каждой новой статьи, которую вы хотите опубликовать, вам нужно будет создавать новую ветку из `dev`. Ветка в Git - это параллельная версия проекта, которая позволяет вносить изменения, не затрагивая основную ветку, пока работа не будет готова к слиянию.

## 2 - Добавление обучающих файлов

Теперь, когда рабочая ветка создана, пришло время интегрировать ваш новый учебник. У вас есть два варианта: использовать мой Python-скрипт, который автоматизирует создание необходимых документов, или создать каждый файл вручную. Мы рассмотрим шаги, которые необходимо выполнить для каждого варианта.

### С помощью моего скрипта Python

Вам нужно установить его на свою машину:


- Python 3.8 или выше;
- Необходимые зависимости для скрипта. Выполнить:

```bash
pip install customtkinter appdirs
```

Чтобы использовать сценарий, перейдите в папку, где он хранится. Скрипт находится в хранилище данных Plan ₿ Network по пути: `bitcoin-educational-content/scripts/tutorial-related/new-tutorial-creation/`.

Попав в папку, выполните команду:

```bash
python new-tutorial-creation.py
```

Откроется графический интерфейс пользователя (GUI). В первый раз вам нужно будет ввести всю необходимую информацию, но при последующих использованиях скрипта ваши личные данные будут запоминаться, что избавит вас от необходимости вводить их снова.

![TUTORIAL](assets/fr/37.webp)

Начните с указания локального пути, ведущего к папке `/tutorials` в вашем клоне репозитория (`.../bitcoin-educational-content/tutorials/`). Вы можете указать его вручную или нажать кнопку "Обзор", чтобы перейти через файловый проводник.

![TUTORIAL](assets/fr/38.webp)

Выберите язык, на котором вы будете писать учебник.

![TUTORIAL](assets/fr/39.webp)

Выберите основную категорию для своего учебника.

![TUTORIAL](assets/fr/40.webp)

Затем выберите соответствующую подкатегорию в зависимости от выбранной вами основной категории.

![TUTORIAL](assets/fr/41.webp)

Определите уровень сложности для учебника.

![TUTORIAL](assets/fr/42.webp)

Выберите имя каталога, специально созданного для вашего учебника. Имя этой папки должно отражать программное обеспечение, рассматриваемое в учебнике, с использованием тире для соединения слов. Например, папка может называться `red-wallet`:

![TUTO](assets/fr/43.webp)

`project_id` - это UUID компании или организации, стоящей за инструментом, представленным в учебнике, доступный [в списке проектов](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Например, для учебника по программному обеспечению Sparrow Wallet вы найдете этот `project_id` в файле: `bitcoin-educational-content/resources/projects/sparrow/project.yml`. Эта информация добавлена в YAML-файл вашего учебника, потому что Plan ₿ Network ведет базу данных компаний и организаций, активно работающих с Биткойном или связанными с ним проектами. Добавляя `project_id`, связанный с вашим учебником, вы создаете связь между вашим контентом и соответствующей организацией.

***Обновление:*** В новой версии скрипта вам больше не нужно вручную вводить `project_id`. Была добавлена функция поиска проекта по его названию и автоматического получения соответствующего `project_id`. Введите начало названия проекта в поле "Название проекта", чтобы найти его, затем выберите нужную компанию из выпадающего меню. Идентификатор `project_id` будет автоматически заполнен в поле ниже. При необходимости вы также можете указать его вручную.

![TUTO](assets/fr/44.webp)

Для тегов выберите 2 или 3 релевантных ключевых слова, связанных с содержанием вашего учебника, выбирая их исключительно [из списка тегов Plan ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md).

![TUTO](assets/fr/45.webp)

В поле "GitHub ID контрибьютора" введите свой GitHub ID.

![TUTO](assets/fr/46.webp)

В поле "ID профессора PBN" введите свой ID, используя слова из списка BIP39, как он отображается в [профиле вашего профессора](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors).

![TUTO](assets/fr/47.webp)

Для получения более подробной информации об идентификаторе профессора обратитесь к следующему руководству:

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
После того как вся информация введена и проверена, нажмите кнопку "Создать учебник", чтобы подтвердить создание файлов учебника. В результате локально будет создана папка с учебником и всеми необходимыми файлами в выбранной папке категории.

![TUTO](assets/fr/48.webp)

Теперь вы можете пропустить подраздел "Без моего Python-скрипта", а также шаг 3 "Заполнение YAML-файла", поскольку скрипт уже выполнил эти действия за вас автоматически. Переходите непосредственно к шагу 4 и начинайте писать свой учебник.

Для получения дополнительной информации об этом Python-скрипте вы также можете [ознакомиться с его README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).

### Без моего скрипта Python

Откройте файловый менеджер и перейдите в папку `bitcoin-educational-content`, которая представляет собой локальный клон вашего репозитория. Обычно она находится в папке `Documents\GitHub\bitcoin-educational-content`.

В этой директории необходимо найти соответствующую подпапку для размещения вашего учебника. Организация папок отражает различные разделы сайта Plan ₿ Network. В нашем примере, поскольку мы хотим добавить учебник по кошельку Sparrow, следует перейти по следующему пути: `bitcoin-educational-content\tutorials\wallet`, что соответствует разделу `WALLET` на сайте:

![TUTO](assets/fr/12.webp)

В папке `wallet` необходимо создать новую директорию, специально предназначенную для вашего учебника. Название этой папки должно напоминать о программном обеспечении, о котором пойдет речь в учебнике, обязательно соединяя слова тире. В моем примере папка будет называться `parrow-wallet`:

![TUTO](assets/fr/13.webp)

В эту новую папку, посвященную вашему учебнику, нужно добавить несколько элементов:


- Создайте папку `assets`, в которую будут помещены все иллюстрации, необходимые для вашего учебника;
- В этой папке `assets` необходимо создать подпапку, названную в соответствии с кодом языка, на котором написан учебник. Например, если учебник написан на английском языке, эта папка должна называться `en`. Поместите туда все визуальные материалы учебника (диаграммы, изображения, скриншоты и т.д.).
- Файл `tutorial.yml` должен быть создан для записи деталей, связанных с вашим учебным пособием;
- Необходимо создать файл в формате markdown для написания фактического содержания вашего учебника. Этот файл должен быть озаглавлен в соответствии с кодом языка, на котором он написан. Например, для учебника, написанного на французском языке, файл должен называться `fr.md`.

![TUTO](assets/fr/14.webp)

Вкратце, вот иерархия файлов, которые нужно создать:

```plaintext
bitcoin-educational-content/
└── tutorials/
└── wallet/ (to be modified with the correct category)
└── sparrow-wallet/ (to be modified with the name of the tutorial)
├── assets/
│   ├── en/ (to be modified according to the appropriate language code)
├── tutorial.yml
└── en.md (to be modified according to the appropriate language code)
```

## 3 - Заполните файл YAML

Заполните файл `tutorial.yml`, скопировав следующий шаблон:

```yaml
id: 

project_id: 

tags:
  - 
  - 
  - 

category: 

level: 

credits:
  professor: 

# Proofreading metadata

original_language:
proofreading:
  - language: 
    last_contribution_date:
    urgency:
    contributors_id:
      - 
    reward:
````

Вот подробная информация об обязательных полях:


- **id**: UUID (_Universally Unique Identifier_) для уникальной идентификации учебника. Вы можете сгенерировать его с помощью [онлайн-инструмента](https://www.uuidgenerator.net/version4). Единственное требование - чтобы этот UUID был случайным, чтобы избежать конфликта с другим UUID на платформе;
- **project_id**: UUID компании или организации, стоящей за инструментом, представленным в учебнике [из списка проектов] (https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Например, если вы создаете учебник по программному обеспечению Sparrow Wallet, вы можете найти этот `project_id` в следующем файле: `bitcoin-educational-content/resources/projects/sparrow/project.yml`. Эта информация добавлена в YAML-файл вашего учебника, потому что Plan ₿ Network ведет базу данных всех компаний и организаций, работающих с Биткойном или связанными с ним проектами. Добавляя `project_id` организации, связанной с вашим учебником, вы создаете связь между двумя элементами;
- **tags**: 2 или 3 релевантных ключевых слова, связанных с содержанием учебного пособия, выбранные исключительно [из списка тегов Plan ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);
- **category**: Подкатегория, соответствующая содержанию руководства, в соответствии со структурой сайта Plan ₿ Network (например, для кошельков: `desktop`, `hardware`, `mobile`, `backup`);
- **level**: Уровень сложности учебника, среди:
    - `beginner`
    - `intermediate`
    - `advanced`
    - `expert`
- **professor**: Ваш `contributor_id` (слова из BIP39), отображаемый в [профиле вашего профессора](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors);
- **original_language**: Язык оригинала учебника (например, `fr`, `en` и т.д.);
- **proofreading**: Информация о процессе вычитки. Заполните первую часть, так как вычитка собственного учебника считается первой проверкой:
    - **language**: Код языка корректуры (например, `fr`, `en` и т.д.).
    - **last_contribution_date**: Сегодняшняя дата.
    - **urgency**: Оставьте пустым.
    - **contributors_id**: Ваш идентификатор на GitHub.
    - **reward**: Оставьте пустым.

Для получения более подробной информации об идентификаторе профессора обратитесь к соответствующему учебному пособию:

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
Вот пример заполненного файла `tutorial.yml` для учебника по кошельку Blockstream Green:

```yaml
id: e84edaa9-fb65-48c1-a357-8a5f27996143
project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8
tags:
- wallets
- software
- keys
category: mobile
level: beginner
credits:
professor: pretty-private
# Proofreading metadata
original_language: fr
proofreading:
- language: fr
last_contribution_date: 2024-11-20
urgency:
contributors_id:
- LoicPandul
reward:
Once you have finished modifying your `tutorial.yml` file, save your document by clicking on `File > Save`:
![TUTO](assets/fr/16.webp)
You can now close your code editor.
## 4 - Fill in the Markdown File
Now, you can open your file that will host your tutorial, named with the code of your language, such as `fr.md`. Go to Obsidian, on the left side of the window, scroll through the folder tree until you find the folder of your tutorial and the file you are looking for:
![TUTO](assets/fr/18.webp)
Click on the file to open it:
![TUTO](assets/fr/19.webp)
We will start by filling in the `Properties` section at the top of the document.
![TUTO](assets/fr/20.webp)
Manually add and fill in the following code block:
```

---
name: [Название]
description: [Описание]
---
```
![TUTO](assets/fr/21.webp)
Fill in the name of your tutorial and a short description of it:
![TUTO](assets/fr/22.webp)
Then, add the path of the cover image at the beginning of your tutorial. To do this, note:
```

![cover-sparrow](assets/cover.webp)

```
This syntax will be useful whenever adding an image to your tutorial is necessary. The exclamation point indicates that it is an image, with the alternative text (alt) specified between the brackets. The path to the image is indicated between the parentheses:
![TUTO](assets/fr/23.webp)
## 5 - Add the Logo and Cover
Within the `assets` folder, you must add a file named `logo.webp`, which will serve as a thumbnail for your article. This image must be in `.webp` format and must respect a square dimension to harmonize with the user interface. You are free to choose the logo of the software covered in the tutorial or any other relevant image, provided that it is free of rights. In addition, also add an image titled `cover.webp` in the same place. This image will be displayed at the top of your tutorial. Ensure that this image, like the logo, respects usage rights and is suitable for the context of your tutorial:
## 6 - Writing the Tutorial and Adding Visuals
Continue writing your tutorial by drafting your content. When you want to integrate a subtitle, apply the appropriate markdown formatting by prefixing the text with `##`:
![TUTO](assets/fr/24.webp)
The language subfolder in the `assets` folder is used to store diagrams and visuals that will accompany your tutorial. As much as possible, avoid including text in your images to make your content accessible to an international audience. Of course, the software being presented will contain text, but if you add diagrams or additional indications on software screenshots, do so without text or, if it proves indispensable, use English.
![TUTO](assets/fr/25.webp)
To name your images, simply use numbers corresponding to their order of appearance in the tutorial, formatted with two digits (or three digits if your tutorial contains more than 99 images). For example, name your first image `01.webp`, your second `02.webp`, and so on.
Your images must be in `.webp` format exclusively. If needed, you can use [my image conversion software](https://github.com/LoicPandul/ImagesConverter).
![TUTO](assets/fr/26.webp)
To insert a diagram into your document, use the following Markdown command, making sure to specify the appropriate alternative text as well as the correct path of the image:
```

![sparrow](assets/fr/01.webp)

```