---
name: RaspiBlitz
description: Vodič za postavljanje vašeg RaspiBlitz-a
---

![image](assets/0.webp)


RaspiBlitz je uradi-sam Lightning Node (LND i/ili Core Lightning) koji radi zajedno sa Bitcoin-Fullnode na RaspberryPi (1TB SSD) i lepim ekranom za jednostavno podešavanje i praćenje.


RaspiBlitz je prvenstveno namenjen učenju kako da pokrenete svoj čvor decentralizovano od kuće - jer: Nije tvoj čvor, nisu tvoja pravila. Otkrijte i razvijajte rastući ekosistem Lightning Network tako što ćete postati njegov punopravni deo. Napravite ga kao deo radionice ili kao vikend projekat sami.


![video](https://youtu.be/DTHlSPMz3ns)

RASPIBLITZ - Kako pokrenuti Lightning i Bitcoin Full node po BTC sesiji


# Parmanov Vodič za Postavljanje Raspiblitz-a


Raspiblitz je odličan sistem za pokretanje Bitcoin čvora i povezanih aplikacija. Preporučujem ovo i My Node čvor većini korisnika (Idealno je imati dva čvora za redundanciju.) Jedna od glavnih prednosti je da je Raspiblitz čvor „Besplatan softver otvorenog koda“, za razliku od MyNode ili Umbrel. Zašto je to važno? Vlad Costa objašnjava. Takođe možete pokrenuti RaspbiBlitz sa WiFi vezom umesto ethernet-a – ovde je dodatni vodič za to. (Nisam pronašao način da to uradim sa MyNode).


Možete kupiti gotov čvor sa priloženim mini ekranom, ili ga možete sami napraviti (nije vam potreban ekran).


Vodič na github stranici je odličan, ali možda previše detaljan za korisnika sa srednjim iskustvom. Moja uputstva će biti sažetija i nadam se lakša za praćenje.


U suštini, proces je veoma sličan procesu postavljanja MyNode čvora sa Raspberry Pi 4. Raspiblitz vodič predlaže da kupite monitor, ali vam zaista nije potreban, i ne bih ga preporučio. Čak vam nije potrebna dodatna tastatura ili miš. Samo pristupite terminal meniju uređaja putem računara na istoj kućnoj mreži, i koristite ssh komandu putem terminala. Ovo je moguće sa Linux/Mac (lako) i malo teže sa Windows.


## Korak 1: Kupite opremu.


Treba vam tačno ista oprema koja vam je potrebna za pokretanje MyNode čvora. Možete probati jedno ili drugo, jedina razlika je u podacima na micro SD kartici.



- Raspberry Pi 4, 4Gb memorije ili 8Gb (4Gb je sasvim dovoljno)
- Zvanični Raspberry Pi punjač (Veoma važno! Nemojte koristiti generičke, ozbiljno)
- Kućište za Pi. (FLIRC kućište je sjajno. Cela kutija je hladnjak i ne treba vam ventilator, koji može biti bučan)
- 32 Gb microSD kartica (treba vam jedna, ali nekoliko njih je korisno.)
- Čitač memorijskih kartica (većina računara neće imati slot za microSD karticu).
- Eksterni SSD 1Tb Hard drajv.
- Ethernet kabl (za povezivanje sa vašim kućnim ruterom).


Ne treba vam monitor (ili tastatura ili miš)


Napomena: Ovo je pogrešan Hard drajv: Ovo je prenosivi eksterni Hard drajv. Nije SSD. SSD je ključan. Zato je jeftin (Cena u AUD)


![image](assets/1.webp)


Ovo je pravi tip za dobiti:


![image](assets/2.webp)


Ovo je brže, ali nepotrebno skupo:


![image](assets/3.webp)


## Korak 2: Preuzmite Raspiblitz sliku


Idite na Raspiblitz github vebsajt i pronađite link za „preuzimanje slike“:


![image](assets/4.webp)


Sha-256 Hash preuzetog fajla je obezbeđen na vebsajtu. Menjaće se sa svakim ažuriranjem. Ako ne razumete o čemu se radi, trebalo bi, pa sam napisao vodič koji možete pročitati ovde.


![image](assets/5.webp)


## Korak 3: Verifikuj sliku


Pre nego što nastavite, ako ne znate kako da se krećete kroz sistem datoteka u komandnoj liniji, lako je naučiti, i trebalo bi.


Evo koristan video za Linux, ali važi i za Mac.


Za Windows, evo jednostavnog vodiča.


Mac/Linux


Sačekajte da se datoteka završi sa preuzimanjem (važno!), zatim sa otvorenim terminalom, navigirajte do mesta gde ste preuzeli datoteku i otkucajte sledeću komandu:

```bash
shasum -a 256 xxxxxxxxxxxxxx
```


gde je `xxxxxxxxxxxxxx` naziv fajla koji ste upravo preuzeli. Ako niste u direktorijumu gde se taj fajl nalazi, morate uneti punu putanju.


Računar razmišlja oko 20 sekundi. Proverite da li izlazna hash datoteka odgovara onoj preuzetoj sa vebsajta u prethodnom koraku. Ako je identična, možete nastaviti.

Prozori


Otvorite komandnu liniju i idite do mesta gde je datoteka preuzeta, i unesite ovu komandu:


```bash
certUtil -hashfile xxxxxxxxxxxxxxx SHA256
```


gde je `xxxxxxxxxxxxxx` naziv fajla koji ste upravo preuzeli. Ako niste u direktorijumu gde se taj fajl nalazi, morate uneti punu putanju.


Računar razmišlja oko 20 sekundi. Proverite da li izlazna hash datoteka odgovara onoj preuzetoj sa vebsajta u prethodnom koraku. Ako je identična, možete nastaviti.


## Korak 4: Flashujte SD karticu


Možete koristiti Balena Etcher za ovo. Preuzmite ga ovde.


Etcher je sam po sebi jasan za korišćenje. Ubacite svoju micro SD karticu i flešujte Raspiblitz softver (.img fajl) na SD karticu.


![image](assets/6.webp)


![image](assets/7.webp)


![image](assets/8.webp)


![image](assets/9.webp)


Jednom kada završite, disk više neće biti čitljiv. Možda ćete dobiti grešku od operativnog sistema, a disk bi trebalo da nestane sa radne površine. Izvucite karticu.


## Korak 5: Postavite Pi i umetnite SD karticu


Delovi (kućište nije prikazano):


![image](assets/10.webp)


![image](assets/11.webp)


Povežite ethernet kabl i USB konektor Hard drajva (još ne napajanje). Izbegavajte povezivanje na plave USB portove u centru. Oni su USB 3. Koristite USB 2 port, iako drajv može biti sposoban za USB 3 (pouzdanije je).


![image](assets/12.webp)


Micro SD kartica ide ovde:


![image](assets/13.webp)


Konačno, povežite napajanje:


![image](assets/14.webp)


## Korak 6: Pronađite IP Address od Pi


Nikada vam nije potreban monitor sa Raspiblitz-om. Međutim, potreban vam je drugi računar na kućnoj mreži. Ako vaš Pi nije povezan putem eterneta, a želite da se oslonite na WiFi, pronalaženje IP adrese zahteva određene računarske veštine. Ne mogu vam pomoći, izvinite. Potrebna vam je ethernet veza. (Problem dolazi od potrebe za pristupom monitoru i operativnom sistemu kako biste povezali WiFi i uneli lozinku.)


Proverite svoj ruter, za listu svih IP adresa svih povezanih uređaja.


Ukucao sam 192.168.0.1 u pregledač (uputstva koja su došla uz moj ruter), prijavio se i mogao sam da vidim svoj uređaj sa IP adresom 192.168.0.191. Napomena: ove IP adrese nisu javno vidljive na internetu (one prolaze prvo kroz ruter), već su samo identifikatori za uređaje na vašoj kućnoj mreži.


Pronalaženje IP-a je ključno.


**Napomena:** možete koristiti terminal na Mac ili Linux mašini da pronađete IP Address svih uređaja povezanih putem Ethernet-a na kućnoj mreži koristeći komandu “arp -a”. Izlaz nije tako lep kao ono što će ruter prikazati, ali sve informacije koje su vam potrebne su tu. Ako nije očigledno koji je Pi, koristite metodu pokušaja i greške.


## Korak 7: SSH u Pi


Zapamti da ubaciš SD karticu u Pi pre nego što ga uključiš. Sačekaj nekoliko minuta, a zatim na drugom Linux/Mac uređaju otvori terminal.


Za Mac/Linux, u terminalu otkucajte:


```bash
ssh admin@You_Pi's_IP_address
```


Za Windows, trebaće da instalirate putty da biste se ssh-ovali u Pi. Ukucajte istu komandu kao gore.


Prvi put kada to uradite, ili kad god promenite OS Pi-a zamenom SD kartice, možete, ali i ne morate dobiti ovu grešku…


![image](assets/15.webp)


Način da to popravite je da odete do mesta gde se nalazi datoteka „known_hosts“ (to vam piše u poruci o grešci) i da je obrišete. Komanda je "rm known_hosts"


Zatim, ponovite ssh komandu da se prijavite. Ovo će se desiti…


![image](assets/16.webp)


Da


Ako bude uspešno, bićete upitani za lozinku. Ovo nije za vaš računar, već za raspiblitz. Generička lozinka je "raspiblitz", a kasnije ćete je promeniti. Prozor terminala će postati plav i imaćete opcije menija kao stari DOS meniji. Krećite se pomoću strelica ili miša.


![image](assets/17.webp)


Pratite uputstva, postavite svoje lozinke, a zatim će detektovati vaš Hard drajv i dati vam opciju da ga formatirate ako je potrebno.


Zatim će vam biti postavljeno pitanje da li želite da kopirate Blockchain podatke iz drugog izvora ili da ih ponovo preuzmete. Kopiranje je proces učenja i uputstva su prilično dobra, i dobro ih je imati pri ruci….


![image](assets/18.webp)


Jednostavan, ali sporiji način je preuzimanje čitavog lanca ispočetka…


![image](assets/19.webp)


Puno teksta će se brzo pojaviti na ekranu terminala. Možda ćete ga pomešati sa procesom preuzimanja Blockchain, ali meni izgleda kao da generiše privatni ključ za komunikaciju.


Zatim se pojavljuju opcije osvetljenja.


![image](assets/20.webp)


Napravite novu lozinku za zaključavanje vašeg osvetljenja Wallet, zatim će biti kreiran novi Wallet i dobićete 24 reči koje treba da zapišete…


![image](assets/21.webp)


Obavezno zapišite i čuvajte na sigurnom mestu. Čuo sam za osobu koja to nije uradila jer nije planirala da koristi lightning, ali je onda godinu dana kasnije odlučila da ga koristi i otvorila kanale. Kada je shvatio da njegove reči nisu bile sačuvane, i sećam se da nije bilo moguće ponovo ih izvući iz uređaja, morao je da zatvori sve svoje kanale i počne ispočetka. On je prošao bez posledica, ali drugi možda neće biti te sreće.


Nakon toga, nekoliko minuta tekst se pomera niz terminalski prozor. Zatim…


![image](assets/22.webp)


Bićete odjavljeni iz ssh sesije. Ponovo se prijavite, ovog puta sa vašom novom lozinkom, lozinkom A. Kada se prijavite, bićete upitani za lozinku C da otključate vaš lightning Wallet.


Sada čekamo. Vidimo se za 2 nedelje. Možeš zatvoriti terminal, to ne utiče na Pi, to je samo komunikacioni prozor.


![image](assets/23.webp)


Ako iz bilo kog razloga želite da isključite Pi pre nego što Blockchain završi preuzimanje, to je u redu sve dok to uradite na ispravan način. Blockchain će nastaviti preuzimanje tamo gde je stao kada se ponovo povežete.


Pritisnite CTRL+c da izađete iz plavog ekrana. Pristupićete Linux terminalu Pi-ja. Ovde možete otkucati “menu” što učitava sledeći ekran, i odatle možete isključiti Pi.


![image](assets/24.webp)


KRAJ vodiča


Dakle, od sada je vaš čvor spreman za rad. Ako vam je i dalje potrebna pomoć u navigaciji dodatnim opcijama, pogledajte GitHub za više tutorijala i vodiča https://github.com/raspiblitz/raspiblitz#feature-documentation