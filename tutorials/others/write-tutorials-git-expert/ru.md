---
name: Вклад - учебник по Git (продвинутый)
description: Руководство для опытных пользователей, предлагающее учебник по плану ₿ Сеть с Git
---
![cover](assets/cover.webp)

Прежде чем следовать этому руководству по добавлению нового учебника, вам необходимо выполнить несколько предварительных шагов. Если вы еще не сделали этого, ознакомьтесь сначала с этим вводным уроком, а затем вернитесь сюда:

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2
У вас уже есть :


- Выберите тему для своего учебника;
- Свяжитесь с командой Plan ₿ Network через [группу Telegram](https://t.me/PlanBNetwork_ContentBuilder) или paolo@planb.network ;
- Выберите инструменты для внесения средств.

В этом руководстве для опытных пользователей Git мы кратко опишем ключевые шаги и основные рекомендации по созданию нового плана ₿ Сетевого учебника. Если вы не знакомы с Git и GitHub, я рекомендую вам воспользоваться одним из этих двух других, более подробных руководств, которые расскажут вам шаг за шагом:


- Промежуточный уровень (GitHub Desktop)** :

https://planb.network/tutorials/others/contribution/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

- Новички (веб-интерфейс)** :

https://planb.network/tutorials/others/contribution/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79
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

```bash
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

```bash
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

```bash
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
Voici le détail des champs obligatoires :
- **id** : Un UUID (_Universally Unique Identifier_) permettant d’identifier de manière unique le tutoriel. Vous pouvez le générer avec [un outil en ligne](https://www.uuidgenerator.net/version4). La seule contrainte est que cet UUID soit aléatoire pour ne pas avoir de conflit avec un autre UUID sur la plateforme ;
- **project_id** : L'UUID de l’entreprise ou de l’organisation derrière l’outil présenté dans le tutoriel [depuis la liste des projets](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Par exemple, si vous réalisez un tutoriel sur le logiciel Green Wallet, vous pouvez trouver ce `project_id` dans le fichier suivant : `bitcoin-educational-content/resources/projects/blockstream/project.yml`. Cette information est ajoutée dans le fichier YAML de votre tutoriel parce que Plan ₿ Network maintient une base de données de toutes les entreprises et organisations opérant sur Bitcoin ou des projets connexes. En ajoutant le `project_id` de l'entité liée à votre tutoriel, vous créez un lien entre les deux éléments ;
- **tags** : 2 ou 3 mots-clés pertinents liés au contenu du tutoriel, choisis exclusivement [dans la liste des tags de Plan ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md) ;
- **category** : La sous-catégorie correspondant au contenu du tutoriel, selon la structure du site Plan ₿ Network (par exemple pour les wallets : `desktop`, `hardware`, `mobile`, `backup`) ;
- **level** : Le niveau de difficulté du tutoriel, parmi :
- `beginner`
- `intermediate`
- `advanced`
- `expert`
- **professor** : Votre `contributor_id` (mots BIP39) tel qu'affiché sur [votre profil professeur](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors) ;
- **original_language** : La langue d’origine du tutoriel (par exemple `fr`, `en`, etc.) ;
- **proofreading** : Informations sur le processus de relecture. Remplissez la première partie, car la relecture de votre propre tutoriel compte comme une première validation :
- **language** : Code de langue de la relecture (par exemple `fr`, `en`, etc.).
- **last_contribution_date** : Date du jour.
- **urgency** : Laissez vide.
- **contributors_id** : Votre ID GitHub.
- **reward** : Laissez vide.
Pour davantage de détails sur votre identifiant de professeur, reportez-vous au tutoriel correspondant :
https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
```

id: e84edaa9-fb65-48c1-a357-8a5f27996143

project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8

теги:


  - кошельки
  - программное обеспечение
  - ключи

категория: мобильные

уровень: начинающий

кредиты:

профессор: pretty-private

# Вычитка метаданных

original_language: fr

корректура:


  - язык: французский

last_contribution_date: 2024-11-20

срочность:

contributors_id:


      - LoicPandul

награда:

```
### 5 - Rédigez le contenu
- Complétez les propriétés du fichier Markdown avec :
- Le titre (`name`).
- Une courte description (`description`).
- Ajoutez l’image de couverture en haut du tutoriel avec la syntaxe Markdown (remplacez "green" par le nom de l’outil présenté) :
```

![cover-green](assets/cover.webp)

```
- Rédigez le contenu du tutoriel en Markdown :
- Utilisez des titres bien structurés (`##`), des listes et des paragraphes.
- Insérez des visuels avec la syntaxe Markdown :
```

![nom-image](assets/en/001.webp)

```
- Placez les schémas et images dans le sous-dossier de langue correspondant, dans `/assets`.
### 6 - Enregistrez et soumettez le tutoriel
- Enregistrez vos modifications localement en créant un commit avec un message descriptif.
- Poussez les changements sur votre fork GitHub.
```

# Создайте фиксацию с описательным сообщением

git commit -m "Добавить учебник по зеленому кошельку"

# Насадите модификации на вилку

git push origin tuto-green-wallet-loic

```
- Une fois terminé, créez une Pull Request (PR) sur GitHub pour proposer l’intégration de vos modifications.
- Ajoutez un titre et une brève description à la PR. Mentionnez le numéro d’issue correspondant dans le commentaire.
### 7 - Relecture et fusion
- Attendez la validation ou les retours d’un administrateur.
- Si nécessaire, effectuez des corrections et poussez de nouveaux commits.
```

# Создайте коммит с описанием внесенных исправлений

git commit -m "Исправления после пересмотра учебника по зеленому кошельку"

# Нажимайте на вилку с коррекцией

git push origin tuto-green-wallet-loic

```
- Une fois la PR fusionnée, vous pouvez supprimer votre branche de travail.
## Normes de création de contenu
- **Formatage supporté sur la plateforme** :
- Markdown classique : listes, liens, images, citations, gras, italique, etc.
- LaTeX (en bloc uniquement, pas inline) : délimité par `$$`.
- Code inline : Syntaxe avec un seul backtick.
- Blocs de code : Syntaxe avec trois backtick, par exemple :
```

print("Hello, Bitcoin!")

```