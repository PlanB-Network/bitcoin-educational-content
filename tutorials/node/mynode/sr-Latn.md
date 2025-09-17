---
name: MyNode
description: Postavite svoj Bitcoin MyNode
---

![image](assets/0.webp)


[MyNode](https://mynodebtc.com/) je najlakši, najmoćniji način za pokretanje Bitcoin-a i Lightning čvora! Kombinujemo najbolji open-source softver sa našim interfejsom, upravljanjem i podrškom, kako biste mogli lako, privatno i bezbedno da koristite Bitcoin i Lightning.


## Tipovi Node postavki


Postoji razne Node postavke. MyNode je odličan. Dolazi sa mnogo aplikacija, a još više ako platite za premium verziju. Inače je veoma zamorno preuzimati sve te aplikacije sami. MyNode to čini prilično jednostavnim, kao što ćete videti.


Alternativna i slična opcija je RaspiBlitz. GUI nije tako lep, a aplikacije se dosta preklapaju sa aplikacijama koje dolaze sa MyNode, ali Raspiblitz je besplatan softver otvorenog koda (FOSS), dok MyNode nije baš. Još jedna razlika je što se MyNode pokreće u Docker kontejneru. Smatram da je Docker zastrašujuć i težak za rešavanje problema. Ovo je problem samo ako naiđete na greške ili bagove. Programer nudi pomoć za premium korisnike, a postoji i Telegram chat grupa.


RaspiBlitz je samo više programa instaliranih na Linuxu, bez Dockera. Spoljni Hard disk se lako može priključiti na drugi Linux računar sa Bitcoin Core-om, i možete krenuti, ako vam zatreba.


Još jedna opcija je da jednostavno instalirate Bitcoin Core i neku varijantu Electrum Servera (ima ih nekoliko) na operativni sistem. Imam vodiče za Linux (Raspberry Pi), Mac i Windows.


## Lista za kupovinu



- Raspberry Pi 4, 4Gb memorije ili 8Gb (4Gb je sasvim dovoljno)
- Zvanični Raspberry Pi punjač (Veoma važno! Nemojte koristiti generičke, ozbiljno)
- Kućište za Pi. FLIRC kućište je sjajno. Cela kutija je hladnjak i ne treba vam ventilator, koji može biti bučan.
- 16 Gb microSD kartica (potrebna vam je jedna, ali nekoliko njih može biti korisno)
- Čitač memorijskih kartica (većina računara neće imati slot za microSD karticu).
- Eksterni SSD 1Tb Hard drajv.

Napomena: SSD je ključan. ne koristite prenosivi eksterni Hard disk iako je jeftiniji


- Ethernet kabl (za povezivanje sa vašim kućnim ruterom)
- Ne treba vam monitor


## Preuzmi MyNode image


Idite na MyNode vebsajt


![image](assets/1.webp)


Kliknite `Download Now`


Preuzmite verziju za Raspberry Pi 4:


![image](assets/2.webp)


To je velika datoteka:


![image](assets/3.webp)


Preuzmi SHA 256 heševe


![image](assets/4.webp)


Otvorite terminal na Mac-u ili Linux-u ili Command Prompt za Windows. Ukucajte:


```bash
shasum -a 256 DOWNLOADEDFILENAME # <--- Mac/Linux
certUtil -hashfile DOWNLOADEDFILENAME SHA256 # <--- Windows
```


Računar razmišlja oko 20 sekundi. Zatim, proverite da li izlazna hash datoteka odgovara onoj preuzetoj sa vebsajta u prethodnom koraku. Ako je identična, možete nastaviti.

Flešuj SD karticu


## Preuzmite i instalirajte Balena Etcher


Nisam uspeo da pronađem digitalni potpis za ovo. Ako znate kako, molim vas da mi javite i ažuriraću ovaj članak.


Etcher je jednostavan za korišćenje. Ubacite svoju micro SD karticu i flešujte Raspberry Pi softver (.img fajl) na SD karticu.


![image](assets/5.webp)

![image](assets/6.webp)

![image](assets/7.webp)

![image](assets/8.webp)

![image](assets/9.webp)

![image](assets/10.webp)

![image](assets/11.webp)


Jednom kada završite, disk više neće biti čitljiv. Možda ćete dobiti grešku od operativnog sistema, a disk bi trebalo da nestane sa radne površine. Izvucite karticu.


## Postavite Pi i umetnite SD karticu


Delovi (kućište nije prikazano):


![image](assets/12.webp)

![image](assets/13.webp)


Povežite ethernet kabl i USB konektor Hard drajva (još ne napajanje). Izbegavajte povezivanje na plave USB portove u centru. Oni su USB 3. MyNode preporučuje korišćenje USB 2 porta, iako drajv može biti kompatibilan sa USB 3.


![image](assets/14.webp)


Micro SD kartica ide ovde:


![image](assets/15.webp)


Konačno, povežite napajanje:


![image](assets/16.webp)


## Pronađi IP adresu od Pi


Nikada vam nije potreban monitor za korišćenje MyNode-a. Međutim, potreban vam je drugi računar na kućnoj mreži. Ako vaš Pi nije povezan putem eterneta, a želite da se oslonite na WiFi, pronalaženje IP adrese zahteva visoke kompjuterske veštine. Ne mogu vam pomoći, žao mi je. Potrebna vam je ethernet veza. (Problem dolazi od potrebe za pristupom monitoru i operativnom sistemu kako biste se povezali na WiFi i uneli lozinku).


Proverite svoj ruter, za listu svih IP adresa svih povezanih uređaja.


Ukucao sam 192.168.0.1 u pregledač (uputstva koja su došla uz moj ruter), prijavio se i mogao da vidim uređaj „MyNode“ sa IP adresom 192.168.0.18. Imajte na umu da ove IP adrese nisu javno vidljive na internetu (one prolaze prvo kroz ruter), već su samo identifikatori za uređaje na vašoj kućnoj mreži.


Pronalaženje IP-a je ključno.


**Napomena:** možete koristiti terminal na Mac ili Linux mašini da pronađete IP adresu svih uređaja povezanih putem Ethernet-a na kućnoj mreži koristeći komandu “arp -a”. Izlaz nije tako lep kao ono što će ruter prikazati, ali sve potrebne informacije su tu. Ako nije očigledno koji je Pi, koristite metodu pokušaja i greške.


## SSH u Pi


Imate opciju da se prijavite na uređaj daljinski putem SSH komande, ali nije obavezno (jeste ako je RaspiBlitz Node). Pokazaću vam kako u svakom slučaju, jer je vrlo korisno.


Otvorite Mac ili Linux računar (za Windows, preuzmite putty, alat za SSH) i otkucajte:


```bash
ssh admin@192.168.0.18
```


Koristite sopstvenu IP adresu. Korisničko ime za MyNode uređaj je podrazumevano „admin“. Lozinka je podrazumevano „Bolt“.


Ako ste ranije koristili svoj Pi i menjali micro SD karticu, dobićete ovu grešku:


![image](assets/17.webp)


Šta treba da uradite je da navigirate do lokacije gde se nalazi datoteka “known_hosts” i da je obrišete. To je bezbedno. Poruka o grešci vam pokazuje putanju. Za mene je to bilo /Users/MyUserName/.ssh/


Ne zaboravi „.“ pre ssh, ovo označava da je to skriveni direktorijum.


Zatim ponovo pokušajte sa ssh komandom.


Ovaj put ćete videti ovaj izlaz:


![image](assets/18.webp)


Datoteka koju ste obrisali je obrisana i dodajete novi otisak prsta. Ukucajte yes i <enter>.


Bićete zamoljeni da unesete lozinku. Ona je „Bolt“


Sada imate pristup terminalu na MyNode Pi, bez monitora, i možete potvrditi da je sve učitano glatko.


![image](assets/19.webp)


## Pristup putem Web pregledača


Otvorite pregledač. To mora biti računar na vašoj kućnoj mreži, ne možete to uraditi spolja. Postoji način, ali to je teško. Nisam ga testirao.


Upišite IP adresu u prozor pretraživača. Ovo će se dogoditi:


![image](assets/20.webp)


Unesite lozinku „Bolt“ – promenite je kasnije.


Onda će se ovo desiti:


![image](assets/21.webp)


Izaberi Formatiraj Disk


![image](assets/22.webp)


Sada čekamo.


U nekom trenutku će vam biti postavljeno pitanje da li želite da unesete svoj ključ proizvoda ili da koristite besplatno „community edition“ — Pokazaću Premium izdanje. Preporučujem da platite za premium verziju ako to možete priuštiti, zaista vredi.


![image](assets/23.webp)


Videćete zatim napredak preuzetih blokova. To traje danima:


![image](assets/24.webp)


Bezbedno je isključiti mašinu tokom preuzimanja ako je potrebno. Idite na podešavanja i pronađite dugme za isključivanje mašine. Nemojte samo iščupati kabl, mogli biste oštetiti instalaciju ili Hard drajv.


Obavezno, na početku, idite na „Settings“ i onemogućite quicksync. Počeće početno preuzimanje blokova od početka.


![image](assets/25.webp)


Želeo sam da nastavim sa kreiranjem vodiča, tako da sam pripremio još jedan MyNode ranije. Ovako izgleda stranica kada je Blockchain sinhronizovan, i kada je nekoliko "aplikacija" omogućeno i sinhronizovano:


![image](assets/26.webp)


Imajte na umu da i Electrum Server treba da se sinhronizuje, tako da čim se Bitcoin Blockchain sinhronizuje, kliknite na dugme da započnete taj proces – traje dan ili dva. Sve ostalo se omogući za nekoliko minuta kada odaberete da ga omogućite. Možete kliknuti na stvari i istraživati. Nećete ništa pokvariti. Ako se nešto pokvari (to se meni desilo, ali mislim da je to zato što sam imao jeftine delove) moraćete ponovo da flešujete i počnete sa preuzimanjem iznova. Problem koji imam sa MyNode je da ako treba da "ponovo flešujete" morate ponovo da započnete Blockchain sinhronizaciju od početka. Postoje tehnički načini da se to zaobiđe, ali nije lako.


Ako želite da isprobate još jedan čvor, recimo RaspiBlitz, potreban vam je dodatni SSD eksterni Hard disk i još jedna micro SD kartica za flešovanje. U suprotnom, oprema je ista, samo što ne možete istovremeno pokretati MyNode i RaspiBlitz, očigledno. Ako to želite, vreme je da kupite još jedan Raspberry Pi.


Sada kada imate pokrenut čvor, koristite ga, nemojte ga samo pustiti da stoji i ne radi ništa za vas. Pratite moj članak (i video) o tome kako povezati vaš Electrum Desktop novčanik sa Electrum Serverom i Bitcoin Core-om ovde.
