---
name: Ubuntu
description: Potpuni vodič za instalaciju i korišćenje Ubuntu-a kao alternative za Windows
---
![cover](assets/cover.webp)


## Uvod


Operativni sistem (OS) je glavni softver koji upravlja svim resursima vašeg računara. Odabir alternativnog operativnog sistema kao što je Ubuntu može ponuditi mnoge prednosti u pogledu sigurnosti, troškova i privatnosti.


### Zašto Ubuntu?




- Poboljšana sigurnost** : Linux distribucije su poznate po svojoj sigurnosti i robusnosti
- Nulta cena**: Ubuntu i većina Linux distribucija su besplatni
- Velika zajednica**: Zajednica korisnika spremna da pomogne putem foruma i tutorijala
- Poštovanje privatnosti**: Otvoreni sistem za veću transparentnost
- Jednostavnost**: Korisnički prijatan Interface i lakoća korišćenja
- Bogat ekosistem** : Opsežan katalog softvera otvorenog koda
- Redovna podrška**: Sigurne ažuriranja od Canonical


## Instalacija i konfiguracija


### 1. Preduslovi


**Oprema potrebna:**




- USB ključ od najmanje 12 GB
- Računar sa najmanje 25 GB slobodnog prostora


### 2. Preuzmi




- Idi na [ubuntu.com/download](https://ubuntu.com/download)
- Izaberite stabilnu verziju (preporučeno LTS)
- Preuzmi ISO sliku


![Page de téléchargement Ubuntu](assets/fr/01.webp)


![Sélection de la version Ubuntu](assets/fr/02.webp)


### 3. Napravite USB ključ za pokretanje sistema


Možete koristiti nekoliko alata, kao što je Balena Etcher :




- Preuzmite i instalirajte [Balena Etcher](https://etcher.balena.io/)


![Page de téléchargement Balena Etcher](assets/fr/03.webp)


![Installation de Balena Etcher](assets/fr/04.webp)




- Otvorite Balena Etcher, zatim izaberite Ubuntu ISO sliku.
- Izaberite USB ključ kao odredišni medijum
- Kliknite na Flash i sačekajte da se proces završi


![Utilisation de Balena Etcher](assets/fr/05.webp)


### 4. Instaliranje i osiguranje Ubuntu-a


**4.1 Pokretanje sa USB memorijskog štapića**




- Isključi računar
- Priključite USB ključ (koji sadrži Ubuntu)
- Uključite računar. Na novijim računarima, sistem bi automatski trebalo da prepozna USB ključ za pokretanje. Ako to nije slučaj, ponovo pokrenite držeći pritisnut taster za pristup BIOS/UEFI (obično F2, F12, ili Delete, u zavisnosti od brenda)
 - U BIOS/UEFI meniju, izaberite vaš USB ključ kao uređaj za pokretanje.
 - Sačuvaj i ponovo pokreni


**4.2 Pokretanje instalacije** (na francuskom)


**Ekran za pokretanje**


Kada pokrenete sistem sa USB ključa, videćete ovaj ekran, koji vam omogućava da pokrenete Ubuntu.


![Écran de démarrage Ubuntu](assets/fr/06.webp)


**Izbor jezika


Izaberite željeni jezik za instalaciju i sistem.


![Sélection de la langue](assets/fr/07.webp)


**Opcije pristupačnosti


Konfigurišite opcije pristupačnosti ako je potrebno (čitač ekrana, visok kontrast, itd.).


![Options d'accessibilité](assets/fr/08.webp)


**Konfiguracija tastature


Odaberite raspored tastature. Dostupno je testno polje da proverite da li tasteri odgovaraju vašoj konfiguraciji.


![Configuration du clavier](assets/fr/09.webp)


**Mrežna veza**


Povežite se na svoju Wi-Fi ili žičanu mrežu kako biste preuzeli ažuriranja tokom instalacije.


![Configuration réseau](assets/fr/10.webp)


**Tip instalacije


Izaberite između "Isprobaj Ubuntu" (za testiranje bez instalacije) ili "Instaliraj Ubuntu".


![Choix du type d'installation](assets/fr/11.webp)


**Metod instalacije


Odaberite interaktivnu instalaciju.


![Mode d'installation](assets/fr/12.webp)


**Izbor aplikacije


Izaberite između podrazumevane instalacije ili proširenog izbora aplikacija.


![Sélection des applications](assets/fr/13.webp)


**Aplikacije trećih strana


Odlučite da li ćete instalirati dodatne drajvere i vlasnički softver.


![Installation applications tierces](assets/fr/14.webp)


**Tip particionisanja


Imate dve glavne opcije:




- "Obriši disk i instaliraj Ubuntu": koristi ceo disk za Ubuntu
- "Ručno instaliranje: kreirajte dual boot sa Windows-om ili prilagodite vaše particije


![Choix du partitionnement](assets/fr/15.webp)


**Kreiranje korisničkog naloga


Postavite svoje korisničko ime i lozinku za svoj Ubuntu nalog.


![Création du compte](assets/fr/16.webp)


**Vremenska zona


Izaberite svoju geografsku oblast da biste podesili sistemsko vreme.


![Sélection du fuseau horaire](assets/fr/17.webp)


**Rezime instalacije**


Proverite sve svoje izbore pre nego što započnete konačnu instalaciju. Kada kliknete na "Instaliraj", proces počinje.


![Résumé de l'installation](assets/fr/18.webp)


**4.3 Nadogradnja Ubuntu-a nakon instalacije** (na francuskom)


Ažuriranje vašeg sistema je važan korak nakon nove instalacije. Imate dve opcije:


**Opcija 1: Preko grafičkog korisničkog Interface**




- Pretraži "Softver i ažuriranja" u meniju aplikacija
- Aplikacija će automatski proveriti dostupna ažuriranja
- Pratite uputstva na ekranu da biste instalirali ažuriranja.


**Opcija 2: Preko Terminala




- Otvorite Terminal (Ctrl + Alt + T)
- Ukucajte sledeću komandu da proverite dostupna ažuriranja:


```bash
sudo apt update
```




- Unesite svoju lozinku kada se to zatraži
- Da biste instalirali ažuriranja, otkucajte :


```bash
sudo apt upgrade
```




- Potvrdite instalaciju tako što ćete otkucati 'Y' pa pritisnuti Enter


### 5. Otkrivanje osnovnih zadataka


**5.1 Pregledanje Interneta


Podrazumevano, često ćete pronaći Firefox u traci za pokretanje.


Pokreni Firefox i počni pretraživanje.


Ostali pregledači (Chrome, Brave, itd.) mogu se instalirati putem Software Manager-a ili putem .deb paketa.


**5.2 Obrada teksta


Ubuntu dolazi sa LibreOffice paketom (Writer za obradu teksta).


Da biste ga otvorili: Aktivnosti > Pretražite "LibreOffice Writer" ili kliknite na ikonu ako se pojavi na traci.


Možete kreirati, uređivati i sačuvati dokumente u različitim formatima (uključujući .docx).


**5.3 Instaliranje aplikacija


Menadžer softvera (nazvan "Ubuntu Software"): grafički Interface za pretragu i instalaciju aplikacija.


Iz Terminala, koristite komandu :


```bash
sudo apt install nom-du-paquet
```


Primer:


```bash
sudo apt install vlc
```


### 6. Zaključak i dodatni resursi


Sada ste spremni da svakodnevno koristite Ubuntu: osigurajte svoj sistem, pretražujte, obavljajte kancelarijski posao, instalirajte softver i održavajte svoj OS ažuriranim!


Da biste dodatno osigurali svoj digitalni život, preporučujemo da pogledate našu uslugu za šifrovanu razmenu poruka, koja je savršeno prilagođena zaštiti vaše privatnosti i dopunjuje vašu Ubuntu instalaciju:


https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2