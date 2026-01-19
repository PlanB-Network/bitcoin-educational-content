---
name: Kali
description: Instaliranje Kali Linux-a na VirtualBox, kao USB stik za pokretanje ili kao dual boot, korak po korak.
---

![cover-kali](assets/cover.webp)



## Uvod



### Zašto Kali Linux?



**Kali Linux** je Linux distribucija specijalizovana za IT bezbednost.


Evo zašto koristimo Kali Linux:





- Unapred je konfigurisan sa širokim spektrom alata za pentesting (testovi bezbednosti sistema i mreže).
- To je **otvorenog koda i besplatno**, tako da ga možete slobodno koristiti i menjati.
- To je **pouzdano i sigurno**, idealno za učenje o sajber bezbednosti.
- Omogućava vam da naučite kako koristiti Linux u okruženju spremnom za testiranje.
- Može se instalirati na različite načine: **VirtualBox**, **bootabilni USB ključ** ili **dual boot**.



## Instalacija i konfiguracija



### 1. Preduslovi



**Oprema potrebna:**





- 64-bitni procesor** (Intel ili AMD).
- 8 GB RAM minimum** (4 GB može biti dovoljno za laku instalaciju ili VM).
- 50 GB slobodnog prostora na disku** za instalaciju Kali Linux-a.
- Internet konekcija** za preuzimanje ISO slike i ažuriranja.
- USB ključ od najmanje 8 GB** za kreiranje bootabilnog medija (ako želite instalirati Kali na PC ili ga testirati na Live USB-u).



Važno je napraviti rezervnu kopiju podataka pre instalacije na postojeći računar.



### 2. Preuzimanje





- Idi na [kali.org/get-kali](https://www.kali.org/get-kali/#kali-platforms)
- Izaberite ISO sliku za vašu aplikaciju:
  - Instaliraj Sliku** : za instalaciju na PC.
  - Virtuelna slika**: za instalaciju Kali na VirtualBox ili VMware.
- Preuzmi ISO sliku.



![Page de téléchargement Kali](assets/fr/01.webp)



![Sélection de la version Kali](assets/fr/02.webp)



### 3. Napravite USB ključ za pokretanje sistema



Možete koristiti nekoliko alata, kao što je Balena Etcher :





- Preuzmite i instalirajte [Balena Etcher](https://etcher.balena.io/).



![Page de téléchargement Balena Etcher](assets/fr/03.webp)



![Installation de Balena Etcher](assets/fr/04.webp)





- Otvorite Balena Etcher, zatim odaberite Kali ISO sliku.
- Izaberite USB ključ kao odredišni medij.
- Kliknite na Flash i sačekajte da se proces završi.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### 4. Instaliranje i osiguravanje Kali Linuxa



#### 4.1 Pokretanje sa USB ključa





- Isključi računar.
- Priključite USB ključ (koji sadrži Kali Linux).
- Uključite računar. Na novijim računarima, sistem bi automatski trebalo da prepozna USB ključ za pokretanje. Ako to nije slučaj, ponovo pokrenite računar držeći pritisnut taster za pristup BIOS/UEFI (obično F2, F12 ili Delete, u zavisnosti od brenda).
  - U BIOS/UEFI meniju, izaberite vaš USB ključ kao uređaj za pokretanje.
  - Sačuvaj i ponovo pokreni.



#### 4.2 Pokretanje instalacije



##### Ekran za pokretanje



Kada se pokreće sa USB memorije, trebalo bi da se pojavi Kali Linux ekran za pokretanje. Izaberite između **grafičke instalacije** i **tekstualne instalacije**. U ovom primeru, odlučili smo se za grafičku instalaciju.



![capture](assets/fr/06.webp)



Ako koristite sliku **Live**, videćete drugi režim, **Live**, koji je takođe podrazumevana opcija pri pokretanju.



![Mode Live](assets/fr/07.webp)



##### Izbor jezika



Izaberite željeni jezik za instalaciju i sistem.



![Sélection de la langue](assets/fr/08.webp)



Molim vas navedite vašu geografsku lokaciju.



![Options d'accessibilité](assets/fr/09.webp)



##### Konfiguracija tastature



Odaberite raspored tastature. Dostupno je testno polje da proverite da li tasteri odgovaraju vašoj konfiguraciji.



![Configuration du clavier](assets/fr/10.webp)



##### Mreža veza



Instalacija će sada skenirati vaše mrežne interfejse, tražiti DHCP uslugu, a zatim će vas zatražiti da unesete ime hosta za vaš sistem. U primeru ispod, uneli smo **"kali "** kao ime hosta.



![Configuration réseau](assets/fr/11.webp)



Možete opcionalno obezbediti podrazumevano ime domena koje će ovaj sistem koristiti (vrednosti se mogu preuzeti sa DHCP-a ili ako postoji prethodno instaliran operativni sistem).



![Choix du type d'installation](assets/fr/12.webp)



##### Korisnički nalozi



Zatim, kreirajte korisnički nalog za sistem (puno ime, korisničko ime i jaku lozinku).



![Création d'un utilisateur](assets/fr/13.webp)



![Mode d'installation](assets/fr/14.webp)



![Sélection des applications](assets/fr/15.webp)



##### Vremenska zona



Izaberite svoju geografsku oblast da biste podesili sistemsko vreme.



![Sélection du fuseau horaire](assets/fr/16.webp)



##### Tip particionisanja



Instalacioni program zatim skenira vaše diskove i prikazuje nekoliko opcija u zavisnosti od vaše konfiguracije.



U ovom vodiču, počinjemo od **praznog diska**, što daje **četiri moguće izbore**.


Odabraćemo **Guided - use entire disk**, jer ovde vršimo jednokratnu instalaciju Kali Linux-a (single boot). To znači da nijedan drugi operativni sistem neće biti zadržan i da se ceo disk može obrisati.



Ako vaš disk već sadrži podatke, može se prikazati dodatna opcija **Guided - use largest contiguous free space**.



Ova alternativa vam omogućava da instalirate Kali Linux bez brisanja postojećih podataka, što je idealno za dual boot sa drugim sistemom.



U našem slučaju, disk je prazan, tako da se ova opcija ne pojavljuje.



![Choix du partitionnement](assets/fr/17.webp)



Izaberite disk za particionisanje.



![capture](assets/fr/18.webp)



U zavisnosti od vaših potreba, možete odabrati da sve vaše fajlove čuvate na jednoj particiji (podrazumevano ponašanje) ili da imate odvojene particije za jedan ili više direktorijuma najvišeg nivoa.



Ako niste sigurni šta želite, izaberite opciju **Svi fajlovi u jednoj particiji**.



![capture](assets/fr/19.webp)



![capture](assets/fr/20.webp)



Imaćete još jednu priliku da proverite konfiguraciju diska pre nego što instalacioni program napravi bilo kakve nepovratne promene. Kada kliknete na _Nastavi_, instalacioni program će se pokrenuti i instalacija će biti skoro završena.



![capture](assets/fr/21.webp)



##### Šifrovani LVM



Ako je ova opcija bila omogućena u prethodnom koraku, Kali Linux će sada izvršiti sigurno brisanje tvrdog diska pre nego što vas zatraži LVM lozinku.



Molimo koristite jaku lozinku, inače će biti prikazano upozorenje o slabom passphrase.



##### Informacije o proxyju



Kali Linux koristi repozitorijume za distribuciju aplikacija. Moraćete uneti potrebne informacije o proxy-ju ako vaše okruženje koristi jedan.



Ako **niste sigurni** da li da koristite proxy, **ostavite prazno**. Unos netačnih informacija će sprečiti povezivanje sa repozitorijumima.



![capture](assets/fr/22.webp)



##### Metapets



Ako pristup mreži nije konfigurisan, biće potrebno **dalje konfigurisanje** kada se to zatraži.



Ako koristite **Live** sliku, sledeći korak neće biti prikazan.



Možete zatim odabrati [metapaket](https://www.kali.org/docs/general-use/metapackages/) koji želite instalirati. Podrazumevane opcije će instalirati standardni Kali Linux sistem, tako da nećete morati ništa da menjate.



![capture](assets/fr/23.webp)



#### Informacije o startapu



Zatim potvrdite instalaciju GRUB boot loader-a.



![capture](assets/fr/24.webp)



##### Ponovo pokreni



Na kraju, kliknite Continue da biste ponovo pokrenuli novu instalaciju Kali Linux-a.



![capture](assets/fr/25.webp)



#### 4.3 Ažuriranje i konfiguracija Kali Linux-a nakon instalacije



Ažuriranje vašeg sistema je važan korak nakon nove instalacije. Imate dve opcije:



##### Opcija 1: Preko grafičkog korisničkog interfejsa (GUI)



Kali, kao i Debian/Ubuntu, nudi integrisani grafički menadžer za ažuriranje.



1. Kliknite na **glavni meni** (gore levo ili dole u zavisnosti od vašeg desktopa).


2. Otvorite **"Software Updater "**.


3. Alat će :




    - Proverite pakete koje treba ažurirati.
    - Videćete listu (sa veličinama i verzijama).
    - Omogućava vam da pokrenete ažuriranje jednim klikom.


4. Unesite lozinku administratora (`sudo`) kada se to zatraži.


5. Dozvolite instalaciju i restartujte ako je potrebno.



##### Opcija 2: Preko terminala



Otvorite terminal i pokrenite :



```bash
# Mettre à jour les dépôts et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyage
sudo apt autoremove -y && sudo apt autoclean
```



Nije preporučljivo koristiti **root** nalog za svakodnevni rad; umesto toga, kreirajte korisnika bez root privilegija.



U vašem terminalu, otkucajte ove komande:



```bash
sudo adduser yourname
sudo usermod -aG sudo yourname
```



Odjavite se i ponovo prijavite sa novim korisnikom.



Hajde da sumiramo neke osnovne zadatke u Kali Linux-u u tabeli.



### Osnovni zadaci u Kali Linuxu



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

## Zaključak



Instaliranje Kali Linux-a je samo prvi korak u otkrivanju ovog moćnog okruženja posvećenog sajber bezbednosti. Savladavanjem osnovnih zadataka i upravljanja sistemom, svako može početi da istražuje ugrađene alate i razume unutrašnje funkcionisanje Linux sistema. Kali nudi odličnu platformu za učenje, kako za jačanje tehničkih veština, tako i za razvoj istinske kulture IT bezbednosti.