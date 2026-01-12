---
name: Kali
description: การติดตั้ง Kali Linux บน VirtualBox, เป็น USB stick ที่สามารถบูตได้, หรือเป็นการบูตคู่, ทีละขั้นตอน.
---

![cover-kali](assets/cover.webp)



## บทนำ



### ทำไมต้องเป็น Kali Linux?



**Kali Linux** เป็นการแจกจ่าย Linux ที่เชี่ยวชาญด้านความปลอดภัยทาง IT


นี่คือเหตุผลที่เราใช้ Kali Linux:





- มีการกำหนดค่าล่วงหน้าด้วยเครื่องมือทดสอบการเจาะระบบที่หลากหลาย (การทดสอบความปลอดภัยของระบบและเครือข่าย)
- มันเป็น **โอเพ่นซอร์สและฟรี** ดังนั้นคุณสามารถใช้และแก้ไขได้อย่างอิสระ
- มันเป็น **ที่เชื่อถือได้และปลอดภัย** เหมาะสำหรับการเรียนรู้เกี่ยวกับความปลอดภัยทางไซเบอร์
- มันช่วยให้คุณเรียนรู้วิธีการใช้ Linux ในสภาพแวดล้อมที่พร้อมสำหรับการทดสอบ
- สามารถติดตั้งได้หลายวิธี: **VirtualBox**, **USB key ที่สามารถบูตได้**, หรือ **dual boot**.



## การติดตั้งและการกำหนดค่า



### 1. ข้อกำหนดเบื้องต้น



**อุปกรณ์ที่จำเป็น:**





- โปรเซสเซอร์ 64 บิต** (Intel หรือ AMD)
- 8 GB RAM ขั้นต่ำ** (4 GB อาจเพียงพอสำหรับการติดตั้งแบบเบาหรือ VM)
- พื้นที่ดิสก์ว่าง 50 GB** เพื่อติดตั้ง Kali Linux.
- การเชื่อมต่ออินเทอร์เน็ต** เพื่อดาวน์โหลดไฟล์ ISO และอัปเดตต่างๆ
- ต้องใช้ USB key ขนาดขั้นต่ำ 8 GB** เพื่อสร้างสื่อที่สามารถบูตได้ (หากคุณต้องการติดตั้ง Kali บนพีซีหรือทดสอบบน Live USB)



สิ่งสำคัญคือต้องสำรองข้อมูลของคุณก่อนที่จะติดตั้งบนพีซีที่มีอยู่



### 2. ดาวน์โหลด





- ไปที่ [kali.org/get-kali](https://www.kali.org/get-kali/#kali-platforms)
- เลือกไฟล์ ISO สำหรับแอปพลิเคชันของคุณ:
  - ติดตั้งภาพ** : สำหรับการติดตั้งบนพีซี
  - Virtual Image**: เพื่อติดตั้ง Kali บน VirtualBox หรือ VMware.
- ดาวน์โหลดไฟล์อิมเมจ ISO



![Page de téléchargement Kali](assets/fr/01.webp)



![Sélection de la version Kali](assets/fr/02.webp)



### 3. สร้าง USB key ที่สามารถบูตได้



คุณสามารถใช้เครื่องมือหลายอย่าง เช่น Balena Etcher :





- ดาวน์โหลดและติดตั้ง [Balena Etcher](https://etcher.balena.io/).



![Page de téléchargement Balena Etcher](assets/fr/03.webp)



![Installation de Balena Etcher](assets/fr/04.webp)





- เปิด Balena Etcher จากนั้นเลือกไฟล์ภาพ ISO ของ Kali
- เลือกคีย์ USB เป็นสื่อปลายทาง
- คลิก Flash และรอให้กระบวนการเสร็จสิ้น



![Utilisation de Balena Etcher](assets/fr/05.webp)



### 4. การติดตั้งและการรักษาความปลอดภัย Kali Linux



#### 4.1 การบูตจาก USB key





- ปิดคอมพิวเตอร์
- เสียบกุญแจ USB (ที่มี Kali Linux)
- เปิดคอมพิวเตอร์ของคุณ บนพีซีรุ่นใหม่ ระบบควรจะรู้จักคีย์บูต USB โดยอัตโนมัติ หากไม่เป็นเช่นนั้น ให้รีบูตโดยกดปุ่มเข้าถึง BIOS/UEFI ค้างไว้ (ปกติคือ F2, F12 หรือ Delete ขึ้นอยู่กับยี่ห้อ)
  - ในเมนู BIOS/UEFI ให้เลือก USB key ของคุณเป็นอุปกรณ์บูต
  - บันทึกและเริ่มใหม่.



#### 4.2 การเริ่มต้นการติดตั้ง



##### หน้าจอเริ่มต้น



เมื่อบูตจาก USB stick หน้าจอบูต Kali Linux ควรปรากฏขึ้น เลือกระหว่าง **การติดตั้งแบบกราฟิก** และ **การติดตั้งแบบข้อความ** ในตัวอย่างนี้ เราได้เลือกการติดตั้งแบบกราฟิก



![capture](assets/fr/06.webp)



หากคุณใช้ภาพ **Live** คุณจะเห็นโหมดอื่น **Live** ซึ่งเป็นตัวเลือกเริ่มต้นโดยค่าเริ่มต้นเช่นกัน



![Mode Live](assets/fr/07.webp)



##### การเลือกภาษา



เลือกภาษาที่คุณต้องการสำหรับการติดตั้งและระบบ



![Sélection de la langue](assets/fr/08.webp)



โปรดระบุสถานที่ตั้งทางภูมิศาสตร์ของคุณ



![Options d'accessibilité](assets/fr/09.webp)



##### การกำหนดค่าคีย์บอร์ด



เลือกการจัดวางแป้นพิมพ์ของคุณ มีช่องทดสอบให้ตรวจสอบว่าแป้นพิมพ์ตรงกับการตั้งค่าของคุณหรือไม่



![Configuration du clavier](assets/fr/10.webp)



##### การเชื่อมต่อเครือข่าย



การติดตั้งจะสแกนอินเทอร์เฟซเครือข่ายของคุณ ค้นหาบริการ DHCP จากนั้นแจ้งให้คุณป้อนชื่อโฮสต์สำหรับระบบของคุณ ในตัวอย่างด้านล่าง เราได้ป้อน **"kali "** เป็นชื่อโฮสต์



![Configuration réseau](assets/fr/11.webp)



คุณสามารถระบุชื่อโดเมนเริ่มต้นที่ระบบนี้จะใช้ได้ (ค่าสามารถดึงมาจาก DHCP หรือหากมีระบบปฏิบัติการที่มีอยู่ก่อนแล้ว)



![Choix du type d'installation](assets/fr/12.webp)



##### บัญชีผู้ใช้



ถัดไป สร้างบัญชีผู้ใช้สำหรับระบบ (ชื่อเต็ม, ชื่อผู้ใช้ และรหัสผ่านที่แข็งแรง)



![Création d'un utilisateur](assets/fr/13.webp)



![Mode d'installation](assets/fr/14.webp)



![Sélection des applications](assets/fr/15.webp)



##### เขตเวลา



เลือกพื้นที่ทางภูมิศาสตร์ของคุณเพื่อตั้งเวลาระบบ



![Sélection du fuseau horaire](assets/fr/16.webp)



##### ประเภทการแบ่งพาร์ติชัน



ตัวติดตั้งจะสแกนดิสก์ของคุณและแสดงตัวเลือกหลายตัวขึ้นอยู่กับการกำหนดค่าของคุณ



ในคู่มือนี้ เราเริ่มจาก **ดิสก์เปล่า** ซึ่งให้ **ตัวเลือกที่เป็นไปได้สี่ตัวเลือก**


เราจะเลือก **Guided - use entire disk** เนื่องจากที่นี่เรากำลังทำการติดตั้ง Kali Linux แบบครั้งเดียว (single boot) ซึ่งหมายความว่าจะไม่มีระบบปฏิบัติการอื่นใดถูกเก็บรักษาไว้ และสามารถลบข้อมูลในดิสก์ทั้งหมดได้



หากดิสก์ของคุณมีข้อมูลอยู่แล้ว อาจมีตัวเลือกเพิ่มเติม **Guided - use largest contiguous free space** ปรากฏขึ้น



ทางเลือกนี้ช่วยให้คุณติดตั้ง Kali Linux ได้โดยไม่ต้องลบข้อมูลที่มีอยู่ ทำให้เหมาะสำหรับการบูตคู่กับระบบอื่น



ในกรณีของเรา ดิสก์ว่างเปล่า ดังนั้นตัวเลือกนี้จึงไม่ปรากฏ



![Choix du partitionnement](assets/fr/17.webp)



เลือกดิสก์ที่จะทำการแบ่งพาร์ติชัน



![capture](assets/fr/18.webp)



ขึ้นอยู่กับความต้องการของคุณ คุณสามารถเลือกที่จะเก็บไฟล์ทั้งหมดของคุณไว้ในพาร์ติชันเดียว (พฤติกรรมเริ่มต้น) หรือมีพาร์ติชันแยกสำหรับหนึ่งหรือมากกว่าหนึ่งไดเรกทอรีระดับบนสุด



หากคุณไม่แน่ใจว่าต้องการอะไร ให้เลือกตัวเลือก **ไฟล์ทั้งหมดในพาร์ติชันเดียว**



![capture](assets/fr/19.webp)



![capture](assets/fr/20.webp)



จากนั้นคุณจะมีโอกาสสุดท้ายในการตรวจสอบการกำหนดค่าดิสก์ของคุณก่อนที่โปรแกรมการติดตั้งจะทำการเปลี่ยนแปลงที่ไม่สามารถย้อนกลับได้ เมื่อคุณคลิกที่ _Continue_ โปรแกรมการติดตั้งจะเริ่มทำงานและการติดตั้งจะเกือบเสร็จสมบูรณ์



![capture](assets/fr/21.webp)



##### LVM ที่เข้ารหัส



หากเปิดใช้งานตัวเลือกนี้ในขั้นตอนก่อนหน้า Kali Linux จะทำการลบข้อมูลในฮาร์ดดิสก์อย่างปลอดภัยก่อนที่จะขอรหัสผ่าน LVM จากคุณ



โปรดใช้รหัสผ่านที่แข็งแกร่ง มิฉะนั้นจะมีการแสดงคำเตือนเกี่ยวกับ passphrase ที่อ่อนแอ



##### ข้อมูลพร็อกซี



Kali Linux ใช้ที่เก็บเพื่อแจกจ่ายแอปพลิเคชัน คุณจะต้องป้อนข้อมูลพร็อกซีที่จำเป็นหากสภาพแวดล้อมของคุณใช้พร็อกซี



หากคุณ **ไม่แน่ใจ** ว่าควรใช้พร็อกซีหรือไม่ **ปล่อยว่างไว้** การกรอกข้อมูลเท็จจะทำให้ไม่สามารถเชื่อมต่อกับที่เก็บข้อมูลได้



![capture](assets/fr/22.webp)



##### เมตาเพ็ทส์



หากการเข้าถึงเครือข่ายยังไม่ได้รับการกำหนดค่า คุณจะต้อง **กำหนดค่าเพิ่มเติม** เมื่อได้รับการแจ้งเตือน



หากคุณกำลังใช้ภาพ **Live** ขั้นตอนถัดไปจะไม่แสดง



จากนั้นคุณสามารถเลือก [metapackages](https://www.kali.org/docs/general-use/metapackages/) ที่คุณต้องการติดตั้งได้ ตัวเลือกเริ่มต้นจะติดตั้งระบบ Kali Linux มาตรฐาน ดังนั้นคุณไม่จำเป็นต้องแก้ไขอะไรเลย



![capture](assets/fr/23.webp)



#### ข้อมูลเริ่มต้นธุรกิจ



จากนั้นยืนยันการติดตั้ง GRUB boot loader



![capture](assets/fr/24.webp)



##### เริ่มใหม่



สุดท้ายนี้ คลิก ดำเนินการต่อ เพื่อเริ่มต้นใหม่บนการติดตั้ง Kali Linux ของคุณ



![capture](assets/fr/25.webp)



#### 4.3 การอัปเดตและกำหนดค่า Kali Linux หลังการติดตั้ง



การอัปเดตระบบของคุณเป็นขั้นตอนสำคัญหลังจากการติดตั้งใหม่ คุณมีสองตัวเลือก:



##### ตัวเลือกที่ 1: ผ่านทางส่วนติดต่อผู้ใช้แบบกราฟิก (GUI)



Kali, เช่นเดียวกับ Debian/Ubuntu, มีตัวจัดการอัปเดตกราฟิกแบบบูรณาการ



1. คลิกที่ **เมนูหลัก** (ด้านบนซ้ายหรือด้านล่างขึ้นอยู่กับเดสก์ท็อปของคุณ)


2. เปิด **"Software Updater "**.


3. เครื่องมือนี้จะ :




    - ตรวจสอบแพ็คเกจที่จะอัปเดต
    - คุณจะเห็นรายการ (พร้อมขนาดและเวอร์ชัน)
    - ช่วยให้คุณเปิดตัวการอัปเดตได้ด้วยการคลิกเพียงครั้งเดียว


4. ป้อนรหัสผ่านผู้ดูแลระบบของคุณ (`sudo`) เมื่อมีการร้องขอ


5. ปล่อยให้ติดตั้งและรีสตาร์ทหากจำเป็น



##### ตัวเลือกที่ 2: ผ่านทางเทอร์มินัล



เปิดเทอร์มินัลและรัน :



```bash
# Mettre à jour les dépôts et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyage
sudo apt autoremove -y && sudo apt autoclean
```



ไม่แนะนำให้ใช้บัญชี **root** สำหรับงานประจำวัน ควรสร้างผู้ใช้ที่ไม่ใช่ root แทน



ในเทอร์มินัลของคุณ พิมพ์คำสั่งเหล่านี้:



```bash
sudo adduser yourname
sudo usermod -aG sudo yourname
```



ออกจากระบบและเข้าสู่ระบบอีกครั้งด้วยผู้ใช้ใหม่



มาสรุปงานพื้นฐานบางอย่างของ Kali Linux ในตารางกันเถอะ



### งานพื้นฐานภายใต้ Kali Linux



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

## บทสรุป



การติดตั้ง Kali Linux เป็นเพียงก้าวแรกในการค้นพบสภาพแวดล้อมที่ทรงพลังนี้ซึ่งอุทิศให้กับความปลอดภัยทางไซเบอร์ โดยการเรียนรู้การทำงานพื้นฐานและการจัดการระบบ ทุกคนสามารถเริ่มสำรวจเครื่องมือที่มีอยู่และเข้าใจการทำงานภายในของระบบ Linux ได้ Kali มอบแพลตฟอร์มการเรียนรู้ที่ยอดเยี่ยม ทั้งสำหรับการเสริมสร้างทักษะทางเทคนิคและการพัฒนาวัฒนธรรมที่แท้จริงของความปลอดภัยด้านไอที