---
name: Pop!_OS
description: Vodič za instalaciju Pop!_OS, Linux distribucije
---

![cover](assets/cover.webp)



## Uvod



Pop!OS je operativni sistem zasnovan na Linuxu koji je razvila **System76**, američki proizvođač specijalizovan za mašine za programere, dizajnere i napredne korisnike.



Dizajniran da ponudi moderno, stabilno, visokoperformansno okruženje, Pop!OS se ističe jednostavnim iskustvom, moćnim alatima i snažnim fokusom na produktivnost.



### Ko je System76?



System76 je američka kompanija osnovana 2005. godine sa sedištem u Denveru, specijalizovana za proizvodnju notebook računara, desktop računara i servera dizajniranih specifično za Linux.



Za razliku od tradicionalnih proizvođača, System76 razvija mašine dizajnirane da budu otvorene, popravljive i orijentisane ka softverskoj slobodi.



System76 ne pravi samo računare.



Kompanija takođe razvija :




- Pop!OS**, sopstveni operativni sistem zasnovan na Linuxu;
- COSMIC**, moderno, visokoperformantno desktop okruženje koje koristi Pop!OS ;
- Open Firmware**, open-source firmware zasnovan na Coreboot ;
- alatke za programere i dizajnere.



Cilj je ponuditi visokokvalitetnu integraciju hardvera i softvera, uporedivu sa Apple ekosistemom, ali potpuno otvorenu i usmerenu na Linux.



## Moderan, stabilan i pristupačan sistem



Pop!OS se gradi na temeljima Ubuntu, pružajući mu izvrsnu stabilnost, široku kompatibilnost sa hardverom i pristup ogromnom softverskom ekosistemu.


Pruža elegantan interfejs, COSMIC desktop, dizajniran da bude fluidan, intuitivan i prilagodljiv, čak i za nove korisnike.



## Idealna opcija za programere, dizajnere i zahtevne korisnike



Pop!OS je posebno cenjen od strane :





- razvijači (unapred instalirani alati, napredno upravljanje pločicama),
- korisnici sa Nvidia ili AMD grafičkim karticama,
- studenti i profesionalci koji traže pouzdan sistem,
- korisnici Windows-a koji žele jednostavan prelaz.



Uključuje automatsko pločanje, jasan softverski centar i integrisane alate za produktivnost kako bi svakodnevna upotreba bila lakša.



## Pop!OS istaknuto





- Optimizovane performanse** zahvaljujući redovnim ažuriranjima.
- Dve ISO verzije dostupne**: standardna i Nvidia-optimizovana.
- Poboljšana sigurnost** (LUKS enkripcija dostupna prilikom instalacije).
- Interface COSMIC** ergonomski i moderan.
- Visoko kompatibilan** sa Ubuntu i Flatpak softverom.



## Preuzmi POP!OS sigurno



### 1. Preduslovi



Pre nego što preuzmete i instalirate POP!OS, postoji nekoliko stvari koje treba da uradite kako biste pravilno pripremili instalaciono okruženje.



### Potrebna oprema





- Kompjuter kompatibilan**: Intel ili AMD procesor, Intel / AMD / Nvidia GPU.
- Najmanje 4 GB RAM-a** (8 GB preporučeno za udobno korišćenje).
- minimum 20 GB slobodnog prostora** (preporučeno 40 GB ili više).
- USB ključ od najmanje 4 GB** za kreiranje instalacionog medija.



### Internet konekcija



Stabilna veza je korisna za :





- preuzmi ISO sliku,
- instaliraj ažuriranja nakon instalacije.



Pop!OS može raditi bez veze, ali instalacija je mnogo lakša putem interneta.



### Bekap podataka



Ako Pop!OS treba da zameni ili koegzistira sa drugim sistemom (Windows, Ubuntu, itd.), preporučljivo je napraviti rezervnu kopiju važnih fajlova pre nego što nastavite.



### Proverite prisustvo Nvidia GPU-a (ako je primenljivo)



Za računare opremljene Nvidia grafičkom karticom, potrebno je preuzeti specijalnu ISO sliku koja uključuje Nvidia drajvere.


Ova provera je veoma jednostavna:





- konsultovanjem specifikacija računara,
- ili tako što ćete potražiti model grafičke kartice u postavkama sistema.



### Preuzmite sa zvanične veb stranice



ISO slika Pop!OS treba da se preuzme direktno sa zvanične stranice System76: [system76.com/pop](https://system76.com/pop/).



Ova stranica uvek nudi najnoviju verziju, prilagođenu vašem hardveru.



![capture](assets/fr/03.webp)



### Izaberite verziju: Standard ili Nvidia, ili Raspberry Pi (ARM64)



Pop!OS je dostupan u tri varijante:



### Standardna verzija



Preporučeno za računare koji koriste :





- intel ili AMD procesor;
- integrisana Intel ili AMD GPU;
- AMD Radeon grafička kartica.



![Utilisation de Balena Etcher](assets/fr/04.webp)



### Nvidia verzija



Preporučeno za računare opremljene Nvidia grafičkim karticama.


Ova slika već uključuje Nvidia drajvere, što olakšava instalaciju i smanjuje probleme sa grafikom.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### Raspberry Pi verzija (ARM64)



Za Raspberry Pi 4 i 400 (ARM procesor).


Prilagođena ARM arhitekturi, ovo je specifična verzija za ove mini-računare.



![Utilisation de Balena Etcher](assets/fr/06.webp)



## Kreiraj bootabilni USB ključ



Možete koristiti nekoliko alata, kao što je Balena Etcher :





- Preuzmite i instalirajte [Balena Etcher](https://etcher.balena.io/).



![Page de téléchargement Balena Etcher](assets/fr/07.webp)



![Installation de Balena Etcher](assets/fr/08.webp)





- Otvorite Balena Etcher, zatim izaberite Pop!OS ISO sliku.
- Izaberite USB ključ kao odredišni medij.
- Kliknite Flash i sačekajte da se proces završi.



![Utilisation de Balena Etcher](assets/fr/09.webp)



## Instaliranje i osiguravanje Pop!OS-a



### Pokretanje sa USB ključa





- Isključi računar.
- Priključite USB ključ (koji sadrži Pop!OS).
- Uključite računar. Na novijim računarima, sistem bi automatski trebalo da prepozna USB ključ za pokretanje. Ako to nije slučaj, ponovo pokrenite računar držeći pritisnut taster za pristup BIOS/UEFI (obično F2, F12 ili Delete, u zavisnosti od brenda).
  - U BIOS/UEFI meniju, izaberite vaš USB ključ kao uređaj za pokretanje.
  - Sačuvaj i ponovo pokreni.



### Pokretanje instalacije



Kada odaberete svoj USB ključ kao uređaj za pokretanje, vaš računar će se pokrenuti u Pop!OS Live okruženje.



Izaberite svoj jezik.



![Capture](assets/fr/10.webp)



Izaberite lokaciju.



![Capture](assets/fr/11.webp)



Izaberite jezik za unos sa tastature.



![Capture](assets/fr/12.webp)



Izaberite raspored tastature.



![Capture](assets/fr/13.webp)



Izaberite opciju `Clean Install` za standardnu instalaciju. Ovo je najbolja opcija za nove korisnike Linux-a, ali budite svesni da će obrisati sav sadržaj ciljanog diska. Alternativno, možete izabrati `Try Demo Mode` da nastavite testiranje Pop!OS u live okruženju.



![Capture](assets/fr/14.webp)



Odaberite `Custom (Advanced)` za pristup GParted. Ovaj alat vam omogućava konfiguraciju naprednih funkcija kao što su dual booting, kreiranje zasebne particije `/home`, ili postavljanje particije `/tmp` na drugi disk.



Kliknite `Erase and Install` da instalirate Pop!OS na izabrani disk.



![Capture](assets/fr/15.webp)



### Konfiguracija korisničkog naloga



Sledeći deo instalacionog programa će vas voditi kroz kreiranje korisničkog naloga kako biste se mogli prijaviti na vaš novi operativni sistem.



Puno ime: Marko Petrović  
Korisničko ime: markopetrovic



![Capture](assets/fr/16.webp)



Kada je nalog kreiran, bićete upitani da postavite novu lozinku.



![Capture](assets/fr/17.webp)



### Šifrovanje celog diska



Šifrovanje sistemskog diska nije neophodno, ali garantuje sigurnost korisničkih podataka u slučaju da neko dobije neovlašćen fizički pristup uređaju.



Disk se može enkriptovati korišćenjem vaše lozinke za prijavu tako što ćete označiti `Lozinka za enkripciju je ista kao lozinka korisničkog naloga`. Takođe možete odznačiti ovu opciju i izabrati `Postavi lozinku` na dnu. Izaberite `Ne enkriptuj` da biste ignorisali proces enkripcije diska.



![Capture](assets/fr/18.webp)



Ako ste izabrali dugme `Set Password`, videćete dodatni prompt za postavljanje lozinke za enkripciju.



Pređite na sledeći korak u instalacionom programu. Pop!OS će sada početi instalaciju na disku.



![Capture](assets/fr/19.webp)



Kada je instalacija završena, ponovo pokrenite računar i prijavite se da biste dovršili proces konfiguracije korisničkog naloga.



Ako ste promenili redosled pokretanja da biste dali prioritet vašem Live USB ključu pri pokretanju, potpuno isključite računar i uklonite instalacioni USB ključ. Ako ste u dual-boot režimu, pritisnite odgovarajuće tastere da biste pristupili konfiguraciji i izabrali disk koji sadrži Pop!OS instalaciju.



![Capture](assets/fr/20.webp)



### NVIDIA Grafika



Ako ste instalirali sa Intel/AMD ISO i vaš sistem ima diskretnu NVIDIA grafičku karticu, ili ako ste je dodali kasnije, biće potrebno da ručno instalirate drajvere za vašu karticu kako biste postigli optimalne performanse. Pokrenite sledeću komandu u terminalu da biste instalirali drajver:



```bash
sudo apt install system76-driver-nvidia
```



Takođe možete instalirati NVIDIA grafičke drajvere iz Pop!_Shop-a.



![Capture](assets/fr/20.webp)



## Instaliranje osnovnih alata



Pop!OS nudi širok spektar softvera putem svog Pop!Shop-a, ali mnogi osnovni alati se takođe mogu instalirati putem terminala sa `apt` ili `flatpak`. Evo kako da instalirate ključne alate za kompletno radno okruženje.



### Instalacija terminala



| Outil                        | Description                                | Commande d’installation                         |
| ---------------------------- | ------------------------------------------ | ----------------------------------------------- |
| Firefox                      | Navigateur web libre et populaire          | `sudo apt install firefox`                      |
| Brave                        | Navigateur web axé sur la confidentialité  | Installation via Pop!_Shop ou site officiel     |
| Visual Studio Code (VS Code) | Éditeur de code puissant pour développeurs | `flatpak install flathub com.visualstudio.code` |
| Git                          | Gestionnaire de versions                   | `sudo apt install git`                          |
| Flatpak                      | Gestionnaire de paquets alternatif         | `sudo apt install flatpak`                      |
| VLC                          | Lecteur multimédia polyvalent              | `sudo apt install vlc`                          |
| GNOME Terminal               | Terminal par défaut                        | Préinstallé sur Pop!OS                          |
| Curl                         | Outil de transfert de données en ligne     | `sudo apt install curl`                         |
| Wget                         | Téléchargement de fichiers via HTTP/FTP    | `sudo apt install wget`                         |
| Docker                       | Conteneurisation d’applications            | Installation via script officiel ou `apt`       |
| Node.js                      | Environnement JavaScript côté serveur      | Installation via `apt` ou NodeSource            |
| Python3                      | Langage de programmation                   | `sudo apt install python3 python3-pip`          |
| GIMP                         | Éditeur d’image avancé                     | `sudo apt install gimp`                         |
| Thunderbird                  | Client mail                                | `sudo apt install thunderbird`                  |
| Transmission                 | Client BitTorrent léger                    | `sudo apt install transmission-gtk`             |
| Htop                         | Moniteur de système interactif             | `sudo apt install htop`                         |

### Instalacija putem Pop! Shop (grafički interfejs)





- Otvorite **Pop!_Shop** iz glavnog menija.
- Koristite traku za pretragu da pronađete aplikacije koje želite (na primer, "Brave").
- Kliknite **Instaliraj** za svaku aplikaciju.
- Pop!_Shop automatski upravlja zavisnostima i ažuriranjima.



## Ažuriranje sistema



### Opcija 1: Preko grafičkog korisničkog interfejsa (GUI)



Pop!OS ima jednostavan, intuitivan grafički menadžer za ažuriranje.



1. Kliknite na **glavni meni** (ikona dole levo).


2. Otvorite **"Pop!_Shop "**.


3. U Pop!_Shop-u, kliknite na karticu **"Updates "**.


4. Sistem će automatski proveriti dostupne ažuriranja.


5. Kliknite na **"Update all "** da biste započeli instaliranje ažuriranja.


6. Unesite svoju lozinku ako se to zatraži.


7. Pustite da se proces završi, zatim ponovo pokrenite ako je potrebno.



### Opcija 2: Preko terminala



Otvorite terminal i upišite :



```bash
# Mettre à jour la liste des paquets et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyer les paquets inutiles
sudo apt autoremove -y && sudo apt autoclean
```



### Upravljanje korisnicima



Preporučujemo korišćenje standardnog korisničkog naloga sa sudo pravima za svakodnevne operacije.



Da biste kreirali novog korisnika :



```bash
sudo adduser votrenom && sudo usermod -aG sudo votrenom
```



Odjavite se, a zatim se ponovo prijavite sa ovim novim korisnikom.



### Upravljanje drajverima grafike





- Za Nvidia kartice, proverite da li su instalirani vlasnički drajveri:



```bash
sudo apt install system76-driver-nvidia
```





- Za AMD/Intel, drajveri su generalno uključeni po defaultu.



### Aktiviraj firewall (UFW)



Pop!OS ne blokira mrežni saobraćaj po defaultu. Aktivirajte UFW da poboljšate sigurnost:



```bash
sudo ufw enable && sudo ufw status verbose
```



### Konfiguriši automatska ažuriranja



Da bi sistem bio ažuriran bez ručne intervencije:



```bash
sudo apt install unattended-upgrades && sudo dpkg-reconfigure --priority=low unattended-upgrades
```



### Prilagodite izgled i ponašanje





- Otvorite **System settings** → **Appearance** da biste izabrali svetlu ili tamnu temu.
- Konfigurišite aktivne uglove, animacije i ekstenzije putem COSMIC menadžera.
- Prilagodite raspored radne površine kako biste optimizovali svoj tok rada.



### Konfiguriši automatsko pravljenje rezervne kopije



Pop!OS integriše alate kao što je Deja Dup za bekap:





- Pokreni **Backup** iz menija.
- Izaberite eksterni disk ili mrežnu lokaciju.
- Zakažite redovne rezervne kopije.



### Instaliranje korisnih GNOME/COSMIC ekstenzija



Evo nekoliko preporučenih ekstenzija za poboljšanje korisničkog iskustva:





- Dash to Dock**: traka sa aplikacijama uvek vidljiva.
- GSConnect**: sinhronizacija sa Androidom.
- Clipboard Indicator**: napredno upravljanje međuspremnikom.



Instalirajte ih putem :



```bash
sudo apt install gnome-shell-extensions
```



Zatim ih aktivirajte u podešavanjima.



### Optimizacija upravljanja memorijom i swap-om



Proverite status zamene:



```bash
swapon --show
```



Ako je potrebno, povećajte veličinu swap-a ili konfigurišite swap fajl :



```bash
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```



Dodajte to u datoteku `/etc/fstab` za automatsko montiranje.



## Upravljanje paketima i repozitorijumima



### Razumevanje izvora paketa



Pop!OS, baziran na Ubuntu, koristi uglavnom :





- Službeni Ubuntu** repozitorijumi: za najstabilniji softver.
- Repozitorijumi System76**: za drajvere, firmver i specifične alate.
- Flatpak**: pristup širokom spektru aplikacija u peskovniku.
- Snap** (opciono): još jedan univerzalni format paketa.



---

### Dodajte i upravljajte PPA repozitorijumima



Da biste instalirali softver koji se često ažurira, mogu se dodati određeni PPA-ovi (Personal Package Archives):



```bash
sudo add-apt-repository ppa:nom/ppa
sudo apt update
```



## Zaključak



Pop!OS je moderna, stabilna Linux distribucija pogodna i za početnike i za napredne korisnike.



Zahvaljujući svom intuitivnom COSMIC interfejsu i integrisanim alatima, nudi fluidno i produktivno iskustvo, bilo za razvoj, kreaciju ili svakodnevnu upotrebu.



Ovaj vodič pokriva ključne faze: priprema, preuzimanje, instalacija, početne postavke i osnovni alati.



Slobodno istražite Pop!OS dalje i prilagodite svoje okruženje kako biste ga maksimalno iskoristili.