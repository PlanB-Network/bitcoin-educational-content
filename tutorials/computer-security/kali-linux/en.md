---
name: Kali
description: Installing Kali Linux on VirtualBox, as a bootable USB stick, or as a dual boot, step by step.
---

![cover-kali](assets/cover.webp)


## Introduction


### Why Kali Linux?


**Kali Linux** is a Linux distribution specialized in IT security.

Here's why we use Kali Linux:



- It is preconfigured with a wide range of pentesting tools (system and network security tests).
- It's **open source and free**, so you can use and modify it freely.
- It's **reliable and secure**, ideal for learning about cybersecurity.
- It allows you to learn how to use Linux in a test-ready environment.
- It can be installed in different ways: **VirtualBox**, **bootable USB key**, or **dual boot**.


## Installation and configuration


### 1. Prerequisites


**Equipment required:**



- 64-bit processor** (Intel or AMD).
- 8 GB RAM minimum** (4 GB may be sufficient for a light installation or VM).
- 50 GB free disk space** to install Kali Linux.
- Internet connection** to download ISO image and updates.
- A minimum 8 GB USB key** to create bootable media (if you want to install Kali on a PC or test it on Live USB).


It is important to back up your data before installing on an existing PC.


### 2. Download



- Go to [kali.org/get-kali](https://www.kali.org/get-kali/#kali-platforms)
- Select the ISO image for your application:
  - Install Image** : for PC installation.
  - Virtual Image**: to install Kali on VirtualBox or VMware.
- Download the ISO image.


![Page de téléchargement Kali](assets/fr/01.webp)


![Sélection de la version Kali](assets/fr/02.webp)


### 3. Create a bootable USB key


You can use several tools, such as Balena Etcher :



- Download and install [Balena Etcher](https://etcher.balena.io/).


![Page de téléchargement Balena Etcher](assets/fr/03.webp)


![Installation de Balena Etcher](assets/fr/04.webp)



- Open Balena Etcher, then select the Kali ISO image.
- Select USB key as destination media.
- Click Flash and wait for the process to finish.


![Utilisation de Balena Etcher](assets/fr/05.webp)


### 4. Installing and securing Kali Linux


#### 4.1 Booting on the USB key



- Switch off the computer.
- Plug in the USB key (containing Kali Linux).
- Switch on your computer. On recent PCs, the system should automatically recognize the USB boot key. If this is not the case, reboot by holding down the BIOS/UEFI access key (usually F2, F12 or Delete, depending on the brand).
  - In the BIOS/UEFI menu, select your USB key as the boot device.
  - Save and restart.


#### 4.2 Launching the installation


##### Startup screen


When booting from the USB stick, the Kali Linux boot screen should appear. Choose between **graphical installation** and **text installation**. In this example, we've opted for graphical installation.


![capture](assets/fr/06.webp)


If you use the **Live** image, you'll see another mode, **Live**, which is also the default startup option.


![Mode Live](assets/fr/07.webp)


##### Language selection


Choose your preferred language for installation and the system.


![Sélection de la langue](assets/fr/08.webp)


Please specify your geographical location.


![Options d'accessibilité](assets/fr/09.webp)


##### Keyboard configuration


Select your keyboard layout. A test field is available to check that the keys correspond to your configuration.


![Configuration du clavier](assets/fr/10.webp)


##### Network connection


The installation will now scan your network interfaces, search for a DHCP service, then prompt you to enter a host name for your system. In the example below, we've entered **"kali "** as the host name.


![Configuration réseau](assets/fr/11.webp)


You can optionally provide a default domain name that this system will use (values can be retrieved from DHCP or if a pre-existing operating system exists).


![Choix du type d'installation](assets/fr/12.webp)


##### User accounts


Next, create the user account for the system (full name, username and a strong password).


![Création d'un utilisateur](assets/fr/13.webp)


![Mode d'installation](assets/fr/14.webp)


![Sélection des applications](assets/fr/15.webp)


##### Time zone


Select your geographical area to set the system time.


![Sélection du fuseau horaire](assets/fr/16.webp)


##### Partitioning type


The installer then scans your disks and displays several options depending on your configuration.


In this guide, we start from a **blank disk**, which gives **four possible choices**.

We're going to select **Guided - use entire disk**, as here we're performing a one-off installation of Kali Linux (single boot). This means that no other operating system will be retained, and the entire disk can be erased.


If your disk already contains data, an additional option **Guided - use largest contiguous free space** may be displayed.


This alternative allows you to install Kali Linux without deleting existing data, making it ideal for dual booting with another system.


In our case, the disk is empty, so this option does not appear.


![Choix du partitionnement](assets/fr/17.webp)


Select the disk to be partitioned.


![capture](assets/fr/18.webp)


Depending on your needs, you can choose to keep all your files in a single partition (default behavior) or have separate partitions for one or more top-level directories.


If you're not sure what you want, choose the **All files in a single partition** option.


![capture](assets/fr/19.webp)


![capture](assets/fr/20.webp)


You will then have one last opportunity to check your disk configuration before the installation program makes any irreversible changes. Once you've clicked on _Continue_, the installation program will launch and installation will be almost complete.


![capture](assets/fr/21.webp)


##### Encrypted LVM


If this option was enabled in the previous step, Kali Linux will now perform a secure hard disk erase before asking you for an LVM password.


Please use a strong password, otherwise a warning about a weak passphrase will be displayed.


##### Proxy information


Kali Linux uses repositories to distribute applications. You'll need to enter the necessary proxy information if your environment uses one.


If you're **not sure** whether to use a proxy, **leave blank**. Entering false information will prevent connection to the repositories.


![capture](assets/fr/22.webp)


##### Metapets


If network access has not been configured, you will need to **further configure** when prompted.


If you are using the **Live** image, the next step will not be displayed.


You can then select the [metapackages](https://www.kali.org/docs/general-use/metapackages/) you wish to install. The default options will install a standard Kali Linux system, so you won't need to modify anything.


![capture](assets/fr/23.webp)


#### Start-up information


Then confirm the installation of the GRUB boot loader.


![capture](assets/fr/24.webp)


##### Restart


Finally, click Continue to restart on your new Kali Linux installation.


![capture](assets/fr/25.webp)


#### 4.3 Updating and configuring Kali Linux after installation


Updating your system is an important step after a new installation. You have two options:


##### Option 1: Via graphical user interface (GUI)


Kali, like Debian/Ubuntu, offers an integrated graphical update manager.


1. Click on the **main menu** (top left or bottom depending on your desktop).

2. Open **"Software Updater "**.

3. The tool will :


    - Check the packages to be updated.
    - You'll see a list (with sizes and versions).
    - Allows you to launch the update with a single click.

4. Enter your administrator password (`sudo`) when prompted.

5. Let it install and restart if necessary.


##### Option 2: Via terminal


Open a terminal and run :


```bash
# Mettre à jour les dépôts et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyage
sudo apt autoremove -y && sudo apt autoclean
```


It is not advisable to use the **root** account for day-to-day work; create a non-root user instead.


In your terminal, type these commands:


```bash
sudo adduser yourname
sudo usermod -aG sudo yourname
```


Log out and log back in with the new user.


Let's summarize some basic Kali Linux tasks in a table.


### Basic tasks under Kali Linux


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

## Conclusion


Installing Kali Linux is just the first step in discovering this powerful environment dedicated to cybersecurity. By mastering basic tasks and system management, everyone can begin to explore the built-in tools and understand the inner workings of a Linux system. Kali offers an excellent learning platform, both for reinforcing technical skills and developing a genuine culture of IT security.