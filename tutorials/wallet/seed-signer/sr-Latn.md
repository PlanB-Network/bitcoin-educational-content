---
name: SeedSigner

description: Postavljanje vašeg seed potpisivača
---

![cover](assets/cover.webp)


## Materijal:


**Raspberry Pi Zero (verzija 1.3)**


Za potpuno izolovano rešenje, obavezno koristite verziju 1.3 bez WiFi ili Bluetooth mogućnosti, ali bilo koji Raspberry Pi 2/3/4 ili Zero model će raditi.


Napomena: Raspberry Pi obično ne dolazi sa pričvršćenim pinovima; pinovi će ili morati biti zalemljeni, ili se može koristiti nešto što se zove „GPIO Hammer“.

GPIO Hammer


Ako vaše lemljenje nije baš na nivou, ili još uvek nemate lemilicu, možete koristiti "GPIO Hammer" kao alternativu lemljenju.


**Šešir LCD WaveShare 1,3 inča sa ekranom 240 × 240 piksela**


WaveShare LCD Hat 1.3″ 240×240 pxl LCD


**Napomena:** Pažljivo odaberite Waveshare ekran; uverite se da kupujete model koji ima rezoluciju od 240×240 piksela.


**Modul kamere kompatibilan sa Pi Zero**


Raspberry Pi Camera Aokin/AuviPal 5MP 1080p sa OV5647 senzorom Video Camera Module; drugi brendovi sa OV5647 senzor modulom bi takođe trebali raditi, ali možda neće biti kompatibilni sa Orange Pill kućištem.


**Napomena:** Trebaće vam traka kabl za kameru koji je specifično kompatibilan sa Raspberry Pi Zero.


**MicroSD kartica sa najmanje 4 GB kapaciteta**


opsežni resursi: https://seedsigner.com/explainers/


## Softver:


Instalacija softvera


1. Preuzmite najnoviju datoteku “seedsigner_x_x_x.img.zip”

najnovije izdanje

2. Raspakujte datoteku “seedsigner_x_x_x.img.zip”

3. Koristite Balena Etcher ili sličan alat da upišete raspakovanu .img datoteku slike na microSD karticu

BALENA ETCHER

4. Instalirajte microSD karticu u SeedSigner.

SeedSigner GPG Javni Ključ

seedsigner_pubkey.gpg


## Video tutorijal


_vodič preuzet od Southerbitcoiner, kreirao Cole_


### Zbirka video vodiča koji pokrivaju SeedSigner: open source, DIY Hardware Wallet/Uređaj za potpisivanje


![image](assets/1.webp)


SeedSigner je Bitcoin uređaj za potpisivanje koji možete izgraditi od nule. Zvuči teško, ali ova serija od 4 dela bi vam trebala pomoći :) Predlažem da pogledate deo 1 i 2, a zatim odlučite da li želite koristiti desktop (pogledajte deo 3) ili mobilni uređaj (pogledajte deo 4).


Sve što treba da znate biće ispod. Drugi korisni linkovi uključuju SeedSignerov vebsajt, njihov Github, njihov Keybase, najnovije izdanje i hardverske zahteve.


### Deo 1: Kako napraviti SeedSigner:


U ovom videu pokazujem kako preuzeti i verifikovati SeedSigner softver, koji delovi su potrebni i kako sastaviti vaš SeedSigner.


![video](https://youtu.be/mGmNKYOXtxY)


### Deo 2: Testiranje vašeg SeedSignera


Pre nego što sam koristio svoj SeedSigner, uradio sam nekoliko testova kako bih se uverio da ne radi ništa zlonamerno. Mislio sam da podelim i ovaj korak. Evo kako da proverite da li vaš SeedSigner ispravno izvozi Wallet (xpub), kako da proverite matematiku SeedSignera za bacanje kockica, i kako da proverite bip-85 child seeds SeedSignera.


![video](https://youtu.be/34W1IyTyXZE)


### Deo 3: Kako koristiti SeedSigner sa Sparrow Wallet (desktop)


SeedSigner je sposoban za generisanje seed-ova i potpisivanje Bitcoin transakcija. Ali sam po sebi, nije sposoban za kreiranje transakcija. Potrebno je da koristite Wallet "koordinator" sa vašim SeedSigner-om. Ovako se koristi Sparrow Wallet sa vašim SeedSigner-om:


![video](https://youtu.be/IQb8dh-VTOg)


Deo 4: Kako koristiti SeedSigner sa Blue Wallet (mobilni)


SeedSigner može generisati seed-ove i potpisivati Bitcoin transakcije. Ali sam po sebi, nije sposoban da kreira transakcije. Potrebno je da koristite Wallet "koordinator" sa vašim SeedSigner-om. Ovako se koristi Blue Wallet sa vašim SeedSigner-om:


![video](https://youtu.be/x0Ee35Ct0r4)


To su za sada svi SeedSigner vodiči! Javite mi ako mislite da nešto nedostaje. Ovo su na mom spisku za potencijalne video snimke:



- SeedSigner ukupni pregled. Da li je dobar izbor za uređaj za potpisivanje? Prednosti/mane?
- Kako koristiti Bip-85 sa SeedSigner-om
- Kako biti ujak Džim sa SeedSigner-om


Našli ste ovo korisnim? Razmislite o slanju napojnice kako biste pomogli u finansiranju budućih video zapisa:

https://www.southernbitcoiner.com/donate/