---
name: Kali
description: Инсталиране на Kali Linux на VirtualBox, като зареждаща USB памет или като двойно зареждане, стъпка по стъпка.
---

![cover-kali](assets/cover.webp)



## Въведение



### Защо Kali Linux?



**Kali Linux** е дистрибуция на Linux, специализирана в областта на ИТ сигурността.


Ето защо използваме Kali Linux:





- Той е предварително конфигуриран с широк набор от инструменти за пентатестване (тестове за системна и мрежова сигурност).
- Той е с отворен код и безплатен**, така че можете да го използвате и модифицирате свободно.
- Той е **надежден и сигурен**, идеален за изучаване на киберсигурността.
- Тя ви позволява да научите как да използвате Linux в среда, готова за тестване.
- Тя може да се инсталира по различни начини: **VirtualBox**, **зареждащ се USB ключ** или **двойно зареждане**.



## Инсталиране и конфигуриране



### 1. Предварителни условия



**Необходимо оборудване:**





- 64-битов процесор** (Intel или AMD).
- минимум 8 GB RAM** (4 GB могат да бъдат достатъчни за лека инсталация или виртуална машина).
- 50 GB свободно дисково пространство**, за да инсталирате Kali Linux.
- Интернет връзка**, за да изтеглите ISO образа и актуализациите.
- Минимум 8 GB USB ключ** за създаване на зареждащ носител (ако искате да инсталирате Kali на компютър или да го тествате на Live USB).



Важно е да направите резервно копие на данните си, преди да инсталирате на съществуващ компютър.



### 2. Изтегляне





- Отидете на [kali.org/get-kali](https://www.kali.org/get-kali/#kali-platforms)
- Изберете ISO образа за вашето приложение:
  - Инсталационно изображение** : за инсталиране на компютър.
  - Виртуално изображение**: за инсталиране на Kali на VirtualBox или VMware.
- Изтеглете ISO образа.



![Page de téléchargement Kali](assets/fr/01.webp)



![Sélection de la version Kali](assets/fr/02.webp)



### 3. Създаване на зареждащ USB ключ



Можете да използвате няколко инструмента, като например Balena Etcher :





- Изтеглете и инсталирайте [Balena Etcher](https://etcher.balena.io/).



![Page de téléchargement Balena Etcher](assets/fr/03.webp)



![Installation de Balena Etcher](assets/fr/04.webp)





- Отворете Balena Etcher, след което изберете ISO образа на Kali.
- Изберете USB ключ като носител на дестинацията.
- Щракнете върху Flash и изчакайте процесът да завърши.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### 4. Инсталиране и осигуряване на Kali Linux



#### 4.1 Стартиране от USB ключ





- Изключете компютъра.
- Включете USB ключа (съдържащ Kali Linux).
- Включете компютъра си. При последните компютри системата трябва автоматично да разпознае USB ключа за зареждане. Ако случаят не е такъв, рестартирайте компютъра, като задържите натиснат клавиша за достъп до BIOS/UEFI (обикновено F2, F12 или Delete, в зависимост от марката).
  - В менюто BIOS/UEFI изберете USB ключа като устройство за зареждане.
  - Запишете и рестартирайте.



#### 4.2 Стартиране на инсталацията



##### Екран за стартиране



При зареждане от USB паметта трябва да се появи екранът за зареждане на Kali Linux. Изберете между **графична инсталация** и **текстова инсталация**. В този пример сме избрали графична инсталация.



![capture](assets/fr/06.webp)



Ако използвате изображението **Live**, ще видите друг режим - **Live**, който е и опцията за стартиране по подразбиране.



![Mode Live](assets/fr/07.webp)



##### Избор на език



Изберете предпочитания от вас език за инсталацията и системата.



![Sélection de la langue](assets/fr/08.webp)



Моля, посочете географското си местоположение.



![Options d'accessibilité](assets/fr/09.webp)



##### Конфигурация на клавиатурата



Изберете клавиатурна подредба. Налично е поле за тест, за да проверите дали клавишите отговарят на вашата конфигурация.



![Configuration du clavier](assets/fr/10.webp)



##### Мрежова връзка



Сега инсталацията ще сканира мрежовите интерфейси, ще потърси услугата DHCP и ще ви подкани да въведете име на хост за вашата система. В примера по-долу сме въвели **"kali "** като име на хост.



![Configuration réseau](assets/fr/11.webp)



По желание можете да предоставите име на домейн по подразбиране, което тази система ще използва (стойностите могат да бъдат извлечени от DHCP или ако съществува вече съществуваща операционна система).



![Choix du type d'installation](assets/fr/12.webp)



##### Потребителски акаунти



След това създайте потребителски акаунт за системата (пълно име, потребителско име и силна парола).



![Création d'un utilisateur](assets/fr/13.webp)



![Mode d'installation](assets/fr/14.webp)



![Sélection des applications](assets/fr/15.webp)



##### Часова зона



Изберете географския си район, за да зададете системното време.



![Sélection du fuseau horaire](assets/fr/16.webp)



##### Тип разделяне



След това инсталаторът сканира дисковете и показва няколко опции в зависимост от конфигурацията.



В това ръководство започваме от **празен диск**, което дава **четири възможни избора**.


Ще изберем **Guided - use entire disk** (Ръководено - използване на целия диск**), тъй като тук извършваме еднократна инсталация на Kali Linux (единично зареждане). Това означава, че няма да бъде запазена друга операционна система и целият диск може да бъде изтрит.



Ако дискът ви вече съдържа данни, може да се покаже допълнителна опция **Guided - use largest contiguous free space** (Ръководство - използвайте най-голямото свободно пространство)**.



Тази алтернатива ви позволява да инсталирате Kali Linux, без да изтривате съществуващите данни, което я прави идеална за двойно зареждане с друга система.



В нашия случай дискът е празен, така че тази опция не се появява.



![Choix du partitionnement](assets/fr/17.webp)



Изберете диска, който ще бъде разделен на дялове.



![capture](assets/fr/18.webp)



В зависимост от нуждите си можете да изберете да съхранявате всички файлове в един дял (поведение по подразбиране) или да имате отделни дялове за една или повече директории от най-високо ниво.



Ако не сте сигурни какво искате, изберете опцията **Всички файлове в един дял**.



![capture](assets/fr/19.webp)



![capture](assets/fr/20.webp)



След това ще имате последна възможност да проверите конфигурацията на диска, преди инсталационната програма да направи необратими промени. След като щракнете върху _Continue_, инсталационната програма ще се стартира и инсталацията ще бъде почти завършена.



![capture](assets/fr/21.webp)



##### Криптиран LVM



Ако тази опция е била разрешена в предишната стъпка, Kali Linux вече ще извърши сигурно изтриване на твърдия диск, преди да ви попита за парола за LVM.



Моля, използвайте силна парола, в противен случай ще се покаже предупреждение за слаба passphrase.



##### Информация за пълномощното



Kali Linux използва хранилища за разпространение на приложения. Ще трябва да въведете необходимата информация за прокси сървъра, ако вашата среда използва такъв.



Ако не сте сигурни дали да използвате прокси, **оставете празно място**. Въвеждането на невярна информация ще попречи на връзката с хранилищата.



![capture](assets/fr/22.webp)



##### Metapets



Ако достъпът до мрежата не е конфигуриран, ще трябва да извършите **допълнителна конфигурация**, когато бъдете подканени.



Ако използвате изображението **Live**, следващата стъпка няма да бъде показана.



След това можете да изберете [метапакетите](https://www.kali.org/docs/general-use/metapackages/), които искате да инсталирате. Опциите по подразбиране ще инсталират стандартна система Kali Linux, така че няма да е необходимо да променяте нищо.



![capture](assets/fr/23.webp)



#### Информация за стартиране



След това потвърдете инсталирането на зареждащата програма GRUB.



![capture](assets/fr/24.webp)



##### Рестартиране на



Накрая щракнете върху Продължи, за да рестартирате новата инсталация на Kali Linux.



![capture](assets/fr/25.webp)



#### 4.3 Актуализиране и конфигуриране на Kali Linux след инсталиране



Актуализирането на системата е важна стъпка след нова инсталация. Имате две възможности:



##### Вариант 1: Чрез графичен потребителски интерфейс (GUI)



Kali, подобно на Debian/Ubuntu, предлага интегриран графичен мениджър за актуализации.



1. Щракнете върху **основното меню** (горе вляво или долу в зависимост от работния плот).


2. Отворете **"Software Updater "**.


3. Инструментът ще :




    - Проверете пакетите, които трябва да бъдат актуализирани.
    - Ще видите списък (с размери и версии).
    - Позволява ви да стартирате актуализацията с едно кликване.


4. Въведете паролата си за администратор (`sudo`), когато бъдете подканени.


5. Оставете го да се инсталира и рестартирайте, ако е необходимо.



##### Вариант 2: Чрез терминал



Отворете терминал и стартирайте :



```bash
# Mettre à jour les dépôts et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyage
sudo apt autoremove -y && sudo apt autoclean
```



Не е препоръчително да използвате акаунта **root** за ежедневна работа; вместо това създайте потребител, който не е root.



В терминала въведете тези команди:



```bash
sudo adduser yourname
sudo usermod -aG sudo yourname
```



Излезте и влезте отново с новия потребител.



Нека обобщим някои основни задачи на Kali Linux в таблица.



### Основни задачи под Kali Linux



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



Инсталирането на Kali Linux е само първата стъпка в откриването на тази мощна среда, посветена на киберсигурността. Като овладее основните задачи и управлението на системата, всеки може да започне да изследва вградените инструменти и да разбере вътрешната работа на една Linux система. Kali предлага отлична платформа за обучение, както за затвърждаване на техническите умения, така и за развиване на истинска култура на ИТ сигурност.