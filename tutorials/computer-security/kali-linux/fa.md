---
name: کالی
description: نصب کالی لینوکس بر روی VirtualBox، به عنوان یک USB قابل بوت، یا به صورت دوگانه بوت، مرحله به مرحله.
---

![cover-kali](assets/cover.webp)



## مقدمه



### چرا کالی لینوکس؟



**کالی لینوکس** یک توزیع لینوکس تخصصی در امنیت فناوری اطلاعات است.


در اینجا دلیل استفاده ما از کالی لینوکس آمده است:





- از پیش با مجموعه گسترده‌ای از ابزارهای تست نفوذ (آزمون‌های امنیت سیستم و شبکه) پیکربندی شده است.
- این **متن‌باز و رایگان** است، بنابراین می‌توانید آزادانه از آن استفاده و آن را تغییر دهید.
- این **قابل اعتماد و امن** است، ایده‌آل برای یادگیری درباره امنیت سایبری.
- این به شما اجازه می‌دهد تا نحوه استفاده از لینوکس را در یک محیط آماده برای آزمون یاد بگیرید.
- می‌توان آن را به روش‌های مختلف نصب کرد: **VirtualBox**، **کلید USB قابل بوت**، یا **بوت دوگانه**.



## نصب و پیکربندی



### 1. پیش‌نیازها



**تجهیزات مورد نیاز:**





- پردازنده ۶۴ بیتی** (اینتل یا ای‌ام‌دی).
- حداقل 8 گیگابایت RAM** (4 گیگابایت ممکن است برای یک نصب سبک یا ماشین مجازی کافی باشد).
- فضای دیسک 50 گیگابایت** برای نصب کالی لینوکس.
- اتصال به اینترنت** برای دانلود تصویر ISO و به‌روزرسانی‌ها.
- یک فلش USB با حداقل ظرفیت 8 گیگابایت** برای ایجاد رسانه قابل بوت (اگر می‌خواهید کالی را روی یک رایانه نصب کنید یا آن را روی USB زنده آزمایش کنید).



مهم است که قبل از نصب بر روی یک رایانه موجود، از داده‌های خود نسخه پشتیبان تهیه کنید.



### ۲. دانلود





- به [kali.org/get-kali](https://www.kali.org/get-kali/#kali-platforms) بروید.
- تصویر ISO را برای برنامه خود انتخاب کنید:
  - نصب تصویر** : برای نصب روی کامپیوتر.
  - تصویر مجازی**: برای نصب کالی بر روی VirtualBox یا VMware.
- تصویر ISO را دانلود کنید.



![Page de téléchargement Kali](assets/fr/01.webp)



![Sélection de la version Kali](assets/fr/02.webp)



### ۳. ایجاد یک کلید USB قابل بوت



می‌توانید از چندین ابزار استفاده کنید، مانند Balena Etcher :





- دانلود و نصب [Balena Etcher](https://etcher.balena.io/).



![Page de téléchargement Balena Etcher](assets/fr/03.webp)



![Installation de Balena Etcher](assets/fr/04.webp)





- بالنا اتچر را باز کنید، سپس تصویر ISO کالی را انتخاب کنید.
- انتخاب کلید USB به عنوان رسانه مقصد.
- روی "Flash" کلیک کنید و منتظر بمانید تا فرآیند به پایان برسد.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### ۴. نصب و ایمن‌سازی کالی لینوکس



#### ۴.۱ بوت شدن از طریق کلید USB





- کامپیوتر را خاموش کنید.
- USB کلید (حاوی Kali Linux) را وصل کنید.
- رایانه خود را روشن کنید. در رایانه‌های شخصی جدید، سیستم باید به طور خودکار کلید بوت USB را شناسایی کند. اگر اینطور نیست، با نگه داشتن کلید دسترسی به BIOS/UEFI (معمولاً F2، F12 یا Delete، بسته به برند) دوباره راه‌اندازی کنید.
  - در منوی BIOS/UEFI، کلید USB خود را به عنوان دستگاه بوت انتخاب کنید.
  - ذخیره و راه‌اندازی مجدد.



#### ۴.۲ راه‌اندازی نصب



##### صفحه شروع



هنگام بوت شدن از USB، صفحه بوت کالی لینوکس باید ظاهر شود. بین **نصب گرافیکی** و **نصب متنی** انتخاب کنید. در این مثال، ما نصب گرافیکی را انتخاب کرده‌ایم.



![capture](assets/fr/06.webp)



اگر از تصویر **Live** استفاده کنید، حالت دیگری به نام **Live** را مشاهده خواهید کرد که همچنین گزینه پیش‌فرض راه‌اندازی است.



![Mode Live](assets/fr/07.webp)



##### انتخاب زبان



زبان مورد نظر خود را برای نصب و سیستم انتخاب کنید.



![Sélection de la langue](assets/fr/08.webp)



لطفاً موقعیت جغرافیایی خود را مشخص کنید.



![Options d'accessibilité](assets/fr/09.webp)



##### پیکربندی صفحه‌کلید



طرح‌بندی صفحه‌کلید خود را انتخاب کنید. یک فیلد آزمایشی در دسترس است تا بررسی کنید که کلیدها با پیکربندی شما مطابقت دارند.



![Configuration du clavier](assets/fr/10.webp)



##### اتصال شبکه



نصب اکنون رابط‌های شبکه شما را اسکن می‌کند، به دنبال یک سرویس DHCP می‌گردد، سپس از شما می‌خواهد که یک نام میزبان برای سیستم خود وارد کنید. در مثال زیر، ما **"kali "** را به عنوان نام میزبان وارد کرده‌ایم.



![Configuration réseau](assets/fr/11.webp)



شما می‌توانید به‌صورت اختیاری یک نام دامنه پیش‌فرض ارائه دهید که این سیستم از آن استفاده خواهد کرد (مقادیر می‌توانند از DHCP بازیابی شوند یا اگر یک سیستم‌عامل از پیش موجود باشد).



![Choix du type d'installation](assets/fr/12.webp)



##### حساب‌های کاربری



سپس، حساب کاربری را برای سیستم ایجاد کنید (نام کامل، نام کاربری و یک رمز عبور قوی).



![Création d'un utilisateur](assets/fr/13.webp)



![Mode d'installation](assets/fr/14.webp)



![Sélection des applications](assets/fr/15.webp)



##### منطقه زمانی



منطقه جغرافیایی خود را برای تنظیم زمان سیستم انتخاب کنید.



![Sélection du fuseau horaire](assets/fr/16.webp)



##### نوع پارتیشن‌بندی



سپس نصب‌کننده دیسک‌های شما را اسکن کرده و بسته به پیکربندی شما چندین گزینه نمایش می‌دهد.



در این راهنما، ما از یک **دیسک خالی** شروع می‌کنیم که **چهار انتخاب ممکن** را ارائه می‌دهد.


ما قصد داریم **راهنما - استفاده از کل دیسک** را انتخاب کنیم، زیرا در اینجا ما یک نصب یکباره از کالی لینوکس (بوت تک) را انجام می‌دهیم. این به این معنی است که هیچ سیستم‌عامل دیگری حفظ نخواهد شد و کل دیسک می‌تواند پاک شود.



اگر دیسک شما قبلاً حاوی داده است، گزینه اضافی **راهنما - استفاده از بزرگترین فضای آزاد پیوسته** ممکن است نمایش داده شود.



این گزینه به شما اجازه می‌دهد تا کالی لینوکس را بدون حذف داده‌های موجود نصب کنید، که آن را برای بوت دوگانه با یک سیستم دیگر ایده‌آل می‌سازد.



در مورد ما، دیسک خالی است، بنابراین این گزینه ظاهر نمی‌شود.



![Choix du partitionnement](assets/fr/17.webp)



دیسک مورد نظر برای پارتیشن‌بندی را انتخاب کنید.



![capture](assets/fr/18.webp)



بسته به نیازهای شما، می‌توانید انتخاب کنید که همه فایل‌های خود را در یک پارتیشن واحد (رفتار پیش‌فرض) نگه دارید یا پارتیشن‌های جداگانه‌ای برای یک یا چند دایرکتوری سطح بالا داشته باشید.



اگر مطمئن نیستید چه می‌خواهید، گزینه **تمام فایل‌ها در یک پارتیشن** را انتخاب کنید.



![capture](assets/fr/19.webp)



![capture](assets/fr/20.webp)



سپس یک فرصت نهایی برای بررسی پیکربندی دیسک خود خواهید داشت قبل از اینکه برنامه نصب هرگونه تغییرات غیرقابل برگشتی را اعمال کند. پس از کلیک بر روی _ادامه_، برنامه نصب راه‌اندازی خواهد شد و نصب تقریباً کامل خواهد شد.



![capture](assets/fr/21.webp)



##### LVM رمزگذاری‌شده



اگر این گزینه در مرحله قبلی فعال شده باشد، کالی لینوکس اکنون قبل از درخواست رمز عبور LVM از شما، پاک‌سازی امن دیسک سخت را انجام خواهد داد.



لطفاً از یک رمز عبور قوی استفاده کنید، در غیر این صورت هشدار درباره passphrase ضعیف نمایش داده خواهد شد.



##### اطلاعات پروکسی



کالی لینوکس از مخازن برای توزیع برنامه‌ها استفاده می‌کند. اگر محیط شما از پروکسی استفاده می‌کند، باید اطلاعات پروکسی لازم را وارد کنید.



اگر **مطمئن نیستید** که از پروکسی استفاده کنید، **خالی بگذارید**. وارد کردن اطلاعات نادرست مانع اتصال به مخازن خواهد شد.



![capture](assets/fr/22.webp)



##### متاپتس



اگر دسترسی به شبکه پیکربندی نشده است، باید هنگام درخواست **پیکربندی بیشتری** انجام دهید.



اگر از تصویر **Live** استفاده می‌کنید، مرحله بعدی نمایش داده نخواهد شد.



سپس می‌توانید [متاپکیج‌ها](https://www.kali.org/docs/general-use/metapackages/)یی را که می‌خواهید نصب کنید، انتخاب کنید. گزینه‌های پیش‌فرض یک سیستم استاندارد کالی لینوکس را نصب خواهند کرد، بنابراین نیازی به تغییر چیزی نخواهید داشت.



![capture](assets/fr/23.webp)



#### اطلاعات استارت‌آپ



سپس نصب بارگذار بوت GRUB را تأیید کنید.



![capture](assets/fr/24.webp)



##### راه‌اندازی مجدد



در نهایت، روی ادامه کلیک کنید تا نصب جدید Kali Linux شما راه‌اندازی مجدد شود.



![capture](assets/fr/25.webp)



#### ۴.۳ به‌روزرسانی و پیکربندی کالی لینوکس پس از نصب



به‌روزرسانی سیستم شما یک گام مهم پس از نصب جدید است. شما دو گزینه دارید:



##### گزینه 1: از طریق رابط کاربری گرافیکی (GUI)



کالی، مانند دبیان/اوبونتو، یک مدیر به‌روزرسانی گرافیکی یکپارچه ارائه می‌دهد.



1. روی **منوی اصلی** کلیک کنید (بالا سمت چپ یا پایین بسته به دسکتاپ شما).


2. **"Software Updater "** را باز کنید.


۳. ابزار خواهد:




    - بسته‌هایی که باید به‌روزرسانی شوند را بررسی کنید.
    - شما لیستی (با اندازه‌ها و نسخه‌ها) خواهید دید.
    - به شما امکان می‌دهد تا با یک کلیک به‌روزرسانی را اجرا کنید.


۴. هنگامی که درخواست شد، رمز عبور مدیر خود را وارد کنید (`sudo`).


۵. اجازه دهید نصب شود و در صورت لزوم راه‌اندازی مجدد کنید.



##### گزینه 2: از طریق ترمینال



یک ترمینال باز کنید و اجرا کنید:



```bash
# Mettre à jour les dépôts et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyage
sudo apt autoremove -y && sudo apt autoclean
```



استفاده از حساب **ریشه** برای کارهای روزمره توصیه نمی‌شود؛ به جای آن یک کاربر غیر ریشه ایجاد کنید.



در ترمینال خود، این دستورات را تایپ کنید:



```bash
sudo adduser yourname
sudo usermod -aG sudo yourname
```



خروج کنید و با کاربر جدید دوباره وارد شوید.



بیایید برخی از وظایف پایه‌ای کالی لینوکس را در یک جدول خلاصه کنیم.



### وظایف پایه تحت کالی لینوکس



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

## نتیجه‌گیری



نصب کالی لینوکس تنها اولین گام در کشف این محیط قدرتمند اختصاص داده شده به امنیت سایبری است. با تسلط بر وظایف پایه و مدیریت سیستم، هر کسی می‌تواند شروع به کاوش در ابزارهای داخلی کرده و به درک عملکرد داخلی یک سیستم لینوکس بپردازد. کالی یک پلتفرم یادگیری عالی ارائه می‌دهد، هم برای تقویت مهارت‌های فنی و هم برای توسعه یک فرهنگ واقعی از امنیت فناوری اطلاعات.