---
name: Кали
description: Установка Kali Linux в VirtualBox, на загрузочный USB-накопитель или в режиме двойной загрузки - шаг за шагом.
---

![cover-kali](assets/cover.webp)



## Введение



### Почему именно Kali Linux?



**Kali Linux** - дистрибутив Linux, специализирующийся на IT-безопасности.


Вот почему мы используем Kali Linux:





- Он предварительно сконфигурирован с широким спектром инструментов для пентестинга (тестирования системной и сетевой безопасности).
- Это **открытый исходный код и бесплатный**, поэтому вы можете свободно использовать и изменять его.
- Это **надежный и безопасный**, идеальный вариант для изучения кибербезопасности.
- Это позволит вам научиться использовать Linux в тестовой среде.
- Его можно установить разными способами: **VirtualBox**, **загрузочный USB-носитель** или **двойная загрузка**.



## Установка и настройка



### 1. Пререквизиты



**Необходимое оборудование:**





- 64-разрядный процессор** (Intel или AMD).
- минимум 8 ГБ оперативной памяти** (для легкой установки или виртуальной машины может быть достаточно 4 ГБ).
- 50 ГБ свободного дискового пространства** для установки Kali Linux.
- Подключение к Интернету** для загрузки ISO-образа и обновлений.
- USB-носитель объемом не менее 8 ГБ** для создания загрузочного носителя (если вы хотите установить Kali на ПК или протестировать ее на Live USB).



Важно создать резервную копию данных перед установкой на существующий ПК.



### 2. Скачать





- Перейдите по ссылке [kali.org/get-kali](https://www.kali.org/get-kali/#kali-platforms)
- Выберите образ ISO для вашего приложения:
  - Установочный образ** : для установки на ПК.
  - Виртуальный образ**: для установки Kali на VirtualBox или VMware.
- Загрузите образ ISO.



![Page de téléchargement Kali](assets/fr/01.webp)



![Sélection de la version Kali](assets/fr/02.webp)



### 3. Создайте загрузочный USB-носитель



Вы можете использовать несколько инструментов, например, Balena Etcher :





- Скачайте и установите [Balena Etcher](https://etcher.balena.io/).



![Page de téléchargement Balena Etcher](assets/fr/03.webp)



![Installation de Balena Etcher](assets/fr/04.webp)





- Откройте Balena Etcher, затем выберите образ Kali ISO.
- Выберите USB-носитель в качестве целевого носителя.
- Нажмите Flash и дождитесь окончания процесса.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### 4. Установка и обеспечение безопасности Kali Linux



#### 4.1 Загрузка с USB-носителя





- Выключите компьютер.
- Подключите USB-носитель (содержащий Kali Linux).
- Включите компьютер. На последних моделях ПК система должна автоматически распознать загрузочный USB-носитель. Если это не так, перезагрузитесь, удерживая клавишу доступа к BIOS/UEFI (обычно F2, F12 или Delete, в зависимости от марки).
  - В меню BIOS/UEFI выберите USB-носитель в качестве загрузочного устройства.
  - Сохраните и перезапустите.



#### 4.2 Запуск установки



##### Начальный экран



При загрузке с USB-накопителя должен появиться экран загрузки Kali Linux. Выберите между **графической установкой** и **текстовой установкой**. В данном примере мы выбрали графическую установку.



![capture](assets/fr/06.webp)



Если вы используете образ **Live**, вы увидите еще один режим, **Live**, который также является вариантом запуска по умолчанию.



![Mode Live](assets/fr/07.webp)



##### Выбор языка



Выберите предпочтительный язык для установки и системы.



![Sélection de la langue](assets/fr/08.webp)



Пожалуйста, укажите ваше географическое положение.



![Options d'accessibilité](assets/fr/09.webp)



##### Конфигурация клавиатуры



Выберите раскладку клавиатуры. Чтобы проверить, соответствуют ли клавиши вашей конфигурации, можно воспользоваться тестовым полем.



![Configuration du clavier](assets/fr/10.webp)



##### Сетевое подключение



Теперь установка просканирует ваши сетевые интерфейсы, найдет службу DHCP и предложит вам ввести имя хоста для вашей системы. В примере ниже мы ввели **"kali "** в качестве имени хоста.



![Configuration réseau](assets/fr/11.webp)



При желании можно указать доменное имя по умолчанию, которое будет использоваться этой системой (значения могут быть получены из DHCP или при наличии уже существующей операционной системы).



![Choix du type d'installation](assets/fr/12.webp)



##### Учетные записи пользователей



Затем создайте учетную запись пользователя для системы (полное имя, имя пользователя и надежный пароль).



![Création d'un utilisateur](assets/fr/13.webp)



![Mode d'installation](assets/fr/14.webp)



![Sélection des applications](assets/fr/15.webp)



##### Часовой пояс



Выберите географический регион для установки системного времени.



![Sélection du fuseau horaire](assets/fr/16.webp)



##### Тип перегородки



Затем программа установки сканирует ваши диски и отображает несколько вариантов в зависимости от конфигурации.



В этом руководстве мы начнем с **пустого диска**, что дает **четыре возможных варианта**.


Мы выберем **Guided - use entire disk**, поскольку здесь мы выполняем одноразовую установку Kali Linux (single boot). Это означает, что никакая другая операционная система не будет сохранена, а весь диск может быть стерт.



Если на диске уже есть данные, может появиться дополнительная опция **Указание - использовать наибольшее свободное пространство**.



Эта альтернатива позволяет установить Kali Linux без удаления существующих данных, что делает ее идеальной для двойной загрузки с другой системой.



В нашем случае диск пуст, поэтому эта опция не появляется.



![Choix du partitionnement](assets/fr/17.webp)



Выберите диск, который нужно разбить на разделы.



![capture](assets/fr/18.webp)



В зависимости от ваших потребностей вы можете хранить все файлы в одном разделе (поведение по умолчанию) или создать отдельные разделы для одного или нескольких каталогов верхнего уровня.



Если вы не уверены в своих силах, выберите вариант **Все файлы в одном разделе**.



![capture](assets/fr/19.webp)



![capture](assets/fr/20.webp)



У вас будет последняя возможность проверить конфигурацию диска, прежде чем программа установки внесет необратимые изменения. После того как вы нажмете кнопку _Continue_, программа установки запустится, и установка будет практически завершена.



![capture](assets/fr/21.webp)



##### Зашифрованный LVM



Если эта опция была включена на предыдущем шаге, Kali Linux теперь будет выполнять безопасное стирание жесткого диска, прежде чем запрашивать пароль LVM.



Пожалуйста, используйте надежный пароль, иначе будет выведено предупреждение о слабом passphrase.



##### Информация о доверенности



Kali Linux использует репозитории для распространения приложений. Вам нужно будет ввести необходимую информацию о прокси-сервере, если в вашей среде он используется.



Если вы **не уверены**, использовать ли прокси, **оставьте пустым**. Ввод ложной информации предотвратит подключение к хранилищам.



![capture](assets/fr/22.webp)



##### Metapets



Если доступ к сети не был настроен, при появлении запроса необходимо выполнить **дальнейшую настройку**.



Если вы используете изображение **Live**, следующий шаг не будет отображаться.



Затем вы можете выбрать [метапакеты](https://www.kali.org/docs/general-use/metapackages/), которые хотите установить. Опции по умолчанию установят стандартную систему Kali Linux, поэтому вам не придется ничего изменять.



![capture](assets/fr/23.webp)



#### Информация о начале работы



Затем подтвердите установку загрузчика GRUB.



![capture](assets/fr/24.webp)



##### Перезапустите



Наконец, нажмите кнопку Продолжить, чтобы перезапустить новую установку Kali Linux.



![capture](assets/fr/25.webp)



#### 4.3 Обновление и настройка Kali Linux после установки



Обновление системы - важный шаг после новой установки. У вас есть два варианта:



##### Вариант 1: Через графический интерфейс пользователя (GUI)



Kali, как и Debian/Ubuntu, предлагает интегрированный графический менеджер обновлений.



1. Нажмите на **главное меню** (слева вверху или внизу, в зависимости от рабочего стола).


2. Откройте **"Software Updater "**.


3. Инструмент будет :




    - Проверьте пакеты, которые необходимо обновить.
    - Вы увидите список (с размерами и версиями).
    - Позволяет запустить обновление одним щелчком мыши.


4. Введите пароль администратора (`sudo`), когда появится запрос.


5. Дайте ему установиться и при необходимости перезапустите.



##### Вариант 2: Через терминал



Откройте терминал и запустите :



```bash
# Mettre à jour les dépôts et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyage
sudo apt autoremove -y && sudo apt autoclean
```



Не рекомендуется использовать учетную запись **root** для повседневной работы; создайте вместо нее пользователя, не являющегося пользователем root.



В терминале введите эти команды:



```bash
sudo adduser yourname
sudo usermod -aG sudo yourname
```



Выйдите из системы и снова войдите в нее под новым пользователем.



Давайте сведем некоторые основные задачи Kali Linux в таблицу.



### Основные задачи в Kali Linux



| **Catégorie**              | **Tâche de base**                      | **Description / Objectif**                                 | **Méthode principale**                                       |
| -------------------------- | -------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| **Navigation système**     | Ouvrir le terminal                     | Accéder à la ligne de commande principale de Kali          | Cliquez sur l’icône du terminal ou utilisez `Ctrl + Alt + T` |
|                            | Parcourir les dossiers                 | Se déplacer dans l’arborescence du système                 | `cd /chemin/du/dossier`, `ls` pour lister les fichiers       |
|                            | Créer / supprimer un dossier           | Organiser les fichiers                                     | `mkdir nom_dossier`, `rm -r nom_dossier`                     |
| **Gestion des fichiers**   | Copier / déplacer un fichier           | Manipuler des fichiers dans le terminal                    | `cp fichier destination`, `mv fichier destination`           |
|                            | Supprimer un fichier                   | Libérer de l’espace disque                                 | `rm nom_du_fichier`                                          |
|                            | Afficher le contenu d’un fichier texte | Lire rapidement un fichier                                 | `cat fichier.txt`, `less fichier.txt`                        |
| **Gestion du système**     | Mettre à jour Kali Linux               | Installer les dernières versions et correctifs de sécurité | `sudo apt update && sudo apt full-upgrade -y`                |
|                            | Installer un logiciel                  | Ajouter un nouvel outil ou utilitaire                      | `sudo apt install nom_du_paquet`                             |
|                            | Supprimer un logiciel                  | Nettoyer le système                                        | `sudo apt remove nom_du_paquet`                              |
|                            | Nettoyer les dépendances inutiles      | Gagner de l’espace disque                                  | `sudo apt autoremove`                                        |
| **Réseau et Internet**     | Vérifier la connexion réseau           | Tester l’accès à Internet                                  | `ping google.com`                                            |
|                            | Identifier l’adresse IP                | Connaître sa configuration réseau                          | `ip a` ou `ifconfig`                                         |
|                            | Changer de réseau Wi-Fi                | Se connecter à un autre point d’accès                      | Icône réseau → Sélectionner le Wi-Fi voulu                   |
| **Comptes et permissions** | Exécuter une commande administrateur   | Obtenir les droits root temporairement                     | `sudo commande`                                              |
|                            | Créer un nouvel utilisateur            | Ajouter un compte local                                    | `sudo adduser nom_utilisateur`                               |
|                            | Modifier un mot de passe               | Sécuriser un compte                                        | `passwd`                                                     |
| **Apparence et confort**   | Changer le fond d’écran                | Personnaliser le bureau                                    | Clic droit sur le bureau → **Paramètres du bureau**          |
|                            | Modifier le thème / icônes             | Améliorer la lisibilité et l’esthétique                    | Paramètres → Apparence / Thèmes                              |
| **Outils Kali**            | Ouvrir le menu des outils              | Explorer les outils de test et de sécurité                 | Menu **Applications → Kali Linux**                           |
|                            | Lancer un outil (ex : nmap, wireshark) | Découverte pratique des utilitaires de sécurité            | `sudo nmap`, `wireshark`, etc.                               |
| **Aide et documentation**  | Obtenir de l’aide sur une commande     | Comprendre une commande avant de l’utiliser                | `man commande` ou `commande --help`                          |

## Заключение



Установка Kali Linux - это лишь первый шаг к знакомству с этой мощной средой, предназначенной для обеспечения кибербезопасности. Освоив базовые задачи и управление системой, каждый может начать изучать встроенные инструменты и понимать внутреннюю работу системы Linux. Kali представляет собой отличную платформу для обучения, как для закрепления технических навыков, так и для развития подлинной культуры ИТ-безопасности.