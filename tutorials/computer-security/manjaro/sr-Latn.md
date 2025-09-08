---
name: Manjaro
description: Olakšavanje pristupa moći Arch Linux-a
---
![cover](assets/cover.webp)



Arch Linux je popularan operativni sistem u mnogim oblastima, zahvaljujući svojoj robusnosti i stabilnosti. Međutim, može biti težak za početnike. Upravo zbog Address ovog problema je kreiran **Manjaro**: da ponudi moć Arch Linux-a, ali sa jednostavnijim, pristupačnijim iskustvom, zasnovanim na intuitivnom, lako za učenje Interface.



## Početak sa Manjarom



Jedna od najvećih prednosti Manjara je njegov **jednostavan i efikasan sistem ažuriranja**. Nema potrebe da ih ručno upravljate: Manjaro se brine o njima za vas! Ikonica u oblasti obaveštenja (lokacija varira u zavisnosti od izdanja) vas obaveštava kada je dostupno ažuriranje. Sve što treba da uradite je da pratite uputstva, a proces je brz i bez napora.



Manjaro takođe nudi **ogroman katalog aplikacija**. Pošto je Manjaro zasnovan na Arch Linux-u, ima direktan pristup njegovim zvaničnim repozitorijumima, bogatim raznovrsnim softverom, uključujući vlasničke aplikacije. Manjaro blago odlaže neka ažuriranja Arch Linux-a radi dodatnog testiranja; ovo poboljšava stabilnost po cenu blagog kašnjenja novih izdanja. A ako vam ovaj izbor nije dovoljan, možete pristupiti i **AUR-u (*Arch User Repository*)**, ogromnoj biblioteci koju upravlja zajednica. Ako program ne postoji u zvaničnim repozitorijumima, verovatno je dostupan u AUR-u.



Još jedna prednost Manjara je što je **mnogo manje gladan resursa** od sistema kao što su Windows ili macOS. Troši manje RAM-a i računarske snage, što ga čini idealnim izborom za starije ili manje moćne računare: vaša mašina dobija na fluidnosti i brzini, vraćajući joj drugu mladost.



Povrh svega, Manjaro je **potpuno besplatan**. Za razliku od Windows-a ili macOS-a, ne morate ništa plaćati da biste ga instalirali i iskoristili maksimalno. Na kraju, nudi **poboljšanu sigurnost** zahvaljujući redovnim, brzim ažuriranjima, ograničavajući izloženost ranjivostima. Njegova aktivna zajednica takođe osigurava da se svi problemi brzo isprave i predlože efikasna rešenja.



## Otkrijte Manjaro OS



Pre nego što počnete sa instalacijom Manjaro-a, važno je znati da je ova distribucija dostupna u nekoliko izdanja. Svako od ovih izdanja nudi jedinstveno radno okruženje koje utiče na vaš tok rada i potrošnju sistemskih resursa. Postoje tri glavna zvanična izdanja Manjaro-a.



![0_01](assets/fr/01.webp)





- **KDE Plasma** izdanje je najprilagodljivije. Ako tražite sistem koji je vizuelno elegantan i visokih performansi, KDE Plasma je odličan izbor. Ovo stabilno radno okruženje je idealno za korisnike koji žele potpunu kontrolu i prilagođeno iskustvo.





- Za mašine sa ograničenijim resursima, **Xfce** izdanje je idealno rešenje. Njegov Interface je lagan i intuitivan, garantujući nesmetan rad čak i na starijim računarima. Štaviše, njegov raspored podseća na Windows, što olakšava prelazak na Linux za nove korisnike.





- Konačno, **GNOME** izdanje nudi potpuno drugačiji pristup. Njegov pojednostavljeni dizajn naglašava produktivnost i organizaciju kroz virtuelne radne prostore. Ovaj radni tok fokusiran na aktivnosti posebno je privlačan korisnicima koji su već upoznati sa Linux-om i traže minimalističko, visoko efikasno okruženje.



### Druge Manjaro edicije



![0_02](assets/fr/02.webp)



Pored zvaničnih izdanja, Manjaro zajednica takođe nudi i druge verzije. Ova alternativna izdanja su dizajnirana da zadovolje specifične potrebe i nude različite radne okoline.



**Cinnamon** izdanje je odličan izbor ako tek počinjete i tražite poznati Interface. Dizajnirano je da bude jednostavno za korišćenje, dok zadržava klasične konvencije tradicionalnih kancelarijskih okruženja.



Za naprednije korisnike, postoje izdanja kao što su **i3 Window Manager** ili **Sway**. Mnogo lakši i brži, ipak zahtevaju dobro poznavanje komandne linije da bi bili potpuno konfigurisani i iskorišćeni. Ova okruženja su idealna za one koji žele potpunu kontrolu nad svojim sistemom i koji efikasnost stavljaju iznad svega.



## Tehnički zahtevi



Da bi Manjaro radio optimalno, vaš računar mora ispunjavati nekoliko minimalnih zahteva. Preporučujemo da imate najmanje:





- 64-bitni (x86_64)** procesor
- Preporučeno 4 GB RAM (minimum 2 GB)** (vidi dole)
- 30 GB diska (više ako kreirate posebnu particiju `/home`)**



## Instalacija Manjaro



Da biste preuzeli, idite na [zvaničnu Manjaro veb stranicu](https://manjaro.org/) i izaberite izdanje koje najbolje odgovara vašim potrebama. Kada preuzmete datoteku, potrebno je da napravite USB ključ za pokretanje sa Manjaro ISO slikom.



Zatim idite na veb-sajt softvera [Rufus] (https://rufus.ie/fr/) i preuzmite ga. Pokrenite program, priključite vaš USB ključ, izaberite Manjaro ISO sliku i započnite flešovanje. Sačekajte da se proces završi pre nego što uklonite ključ. Zatim možete restartovati vaš računar.



![0_03](assets/fr/03.webp)



Da biste instalirali Manjaro na vaš računar, prvo ga potpuno isključite. Zatim priključite USB ključ, ponovo uključite računar i pristupite boot meniju ili UEFI/BIOS firmveru pritiskom na **F2, F10, F12, Escape** ili **Delete** (u zavisnosti od proizvođača).



Zatim izaberite USB ključ kao uređaj za pokretanje kako biste započeli proces instalacije OS-a.



### Ekran za pokretanje



Prvi put kada pokrenete Manjaro sa USB ključa, bićete direktno preusmereni na meni za instalaciju. Pre pokretanja instalacije, možete promeniti raspored tastature ili jezik sistema.



Zatim izaberite opciju **Boot with open source drivers** da biste započeli instalaciju Manjaro-a. Ovi open-source drajveri su kompatibilni sa većinom hardvera i biće dovoljni u većini slučajeva. Ako imate NVIDIA grafičku karticu, na primer, ili zahtevate viši grafički performans, možete izabrati **Boot with proprietary drivers**, što koristi vlasničke drajvere.



![0_04](assets/fr/04.webp)



Sistem će se pokrenuti u **podrazumevanom režimu uživo**. Ovo vam omogućava da testirate funkcionalnost Manjara kako biste videli da li odgovara vašim potrebama pre nego što ga trajno instalirate. Kada budete spremni, kliknite na opciju **Install Manjaro Linux**.



Izaberite željeni jezik za instalaciju, zatim kliknite na **Dalje**.



![0_06](assets/fr/06.webp)



Zatim izaberite svoju lokaciju da biste postavili ispravnu vremensku zonu. U ovoj fazi, takođe možete promeniti jezik i format datuma.



![0_07](assets/fr/07.webp)



Izaberite raspored tastature. Dostupno je polje za testiranje kako biste proverili da li pritisnuti tasteri odgovaraju očekivanim karakterima.



![0_08](assets/fr/08.webp)



### Partitionisanje diska


Imate dve opcije za particionisanje vašeg diska.





- Prvi, i najjednostavniji, način je da obrišete ceo disk i instalirate Manjaro na njega.
- Druga omogućava **ručno particionisanje**.



![0_09](assets/fr/09.webp)



Za čistu instalaciju, preporučujemo kreiranje najmanje tri particije:





- Prva particija od **516 MB** (primarna) za **boot**.
- Druga **2 GB** (logička) particija za **swap**.
- Treća particija za vaše **lične podatke**.



Ako želite da instalirate drugi sistem paralelno, potrebno je da podelite ovu poslednju particiju i dodelite samo jedan deo Manjaru (najmanje **15 GB** kako biste garantovali pravilno funkcionisanje sistema).


### Kreiranje korisničkog naloga



Kreirajte korisnički nalog na sistemu popunjavanjem potrebnih informacija. Na kraju, postavite lozinku administratora (**root**). Ovaj administrator je **super-korisnik** sa punim pravima na sistemu i mogućnošću izvršavanja naprednih komandi.



![0_10](assets/fr/10.webp)



### Izaberite pravi kancelarijski paket



Manjaro vam omogućava da birate između **FreeOffice** i **LibreOffice**.





- LibreOffice** je potpuniji, sa širim spektrom softvera i naprednim funkcijama.
- FreeOffice**, s druge strane, je lakši i uključuje samo osnovne stvari: **TextMaker**, **PlanMaker** i **Presentations**.



![0_11](assets/fr/11.webp)



### Rezime konfiguracije



Ekran sažetka prikazuje sve parametre koje ste postavili. Možete se vratiti da izvršite izmene ako je potrebno, bez uticaja na ostala podešavanja koja ste već napravili.



Zatim kliknite na **Install** i potvrdite da biste započeli stvarnu instalaciju.



![0_12](assets/fr/12.webp)



![0_13](assets/fr/13.webp)



### Kraj instalacije



Na kraju procesa, označite polje **Restart now**, zatim kliknite na **Done**. Sistem će se ponovo pokrenuti i **Manjaro će biti spreman za upotrebu**.



![0_13](assets/fr/14.webp)



## Prvi koraci sa Manjarom



Instaliranje Manjaro-a je samo prvi korak. Da biste izvukli maksimum iz vašeg sistema, evo nekoliko korisnih stvari koje treba znati.



### Ažuriraj sistem



Manjaro u velikoj meri pojednostavljuje ažuriranja. Da biste ažurirali svoje pakete:



```shell
sudo pacman -Syu
```



Ova komanda preuzima i instalira najnovije dostupne verzije. Preporučujemo da je redovno pokrećete kako biste održali vaš sistem **sigurnim i stabilnim**.



### Konfigurisanje razvojnog okruženja



Da biste razvijali veb aplikacije na Manjaru, instalirajte osnovne alate jednim komandnim:



```shell
sudo pacman -S nodejs npm git yarn
```



Ova komanda instalira Node.js i npm za pokretanje i upravljanje vašim JavaScript i TypeScript projektima, Git za upravljanje verzijama, i Yarn kao alternativni menadžer paketa.



### Instaliranje Bitcoin Wallet



Da biste upravljali svojim bitcoinima na Manjaru, možete instalirati **Electrum**, lagani i sigurni Wallet :



```shell
sudo pacman -S electrum  # Install Electrum
```



Electrum vam omogućava da **primate i šaljete bitkoine** sa lakoćom, dok nudi napredne funkcije kao što su upravljanje sa više Wallet i zaštita passphrase. Za kompletan vodič o korišćenju Electrum-a, pogledajte naš posvećeni tutorijal koji objašnjava kako kreirati Wallet, osigurati vaša sredstva i izvršiti transakcije.



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

## Osiguravanje vašeg Manjaro sistema



Bezbednost je ključni aspekt svake Linux instalacije. Važno je da zaštitite poverljivost i integritet vaših podataka.



### Konfiguracija firewall-a



Manjaro uključuje UFW (*Uncomplicated Firewall*), program za upravljanje mrežnim filter vatrozidima, ali ga morate ručno aktivirati:



```bash
# Installation if not present
sudo pacman -S ufw

# Firewall activation
sudo systemctl enable ufw.enable

sudo ufw enable

# Allow SSH connections (optional)
sudo ufw allow ssh

# Check the status
sudo ufw status verbose
```



![verbose](assets/fr/15.webp)



### Upravljanje korisničkim dozvolama



1. **Kreiraj neprivilegovanog korisnika**



```shell
sudo useradd -m username
sudo passwd username
```



2. **Konfiguracija fajla Sudoers**



```shell
sudo EDITOR=nano visudo
```



Sada ste spremni da koristite Manjaro Linux na vašoj mašini. Zahvaljujući njegovoj **jednostavnoj instalaciji**, **lakim ažuriranjima** i **fleksibilnosti**, imaćete moćan, visokoperformansni sistem, pogodan za razvoj, svakodnevnu upotrebu i upravljanje vašim bitcoinima sa alatima kao što je Electrum.



Manjaro kombinuje **stabilnost, brzinu i sigurnost**, dok ostaje **potpuno besplatan**, što ga čini idealnim izborom za početnike i napredne korisnike. Odvojite vreme da istražite njegove različite funkcije i prilagodite svoje okruženje prema vašim potrebama. Ako želite više stručnosti i da otkrijete Arch Linux sistem, naš vodič je toplo preporučen.



https://planb.network/tutorials/computer-security/operating-system/arch-linux-7a3dc8a8-629b-4971-bb0d-4eab94f93973