---
name: Linux Mint

description: Postavite računar za Bitcoin transakcije
---

![image](assets/cover.webp)


## Šta nije u redu ako koristite običan računar?


Kada pravite Bitcoin transakcije, idealno je da vaš računar nema malver. Očigledno.


Ako čuvate svoju Bitcoin seed frazu (obično 12 ili 24 reči) van računara uz uređaj za potpisivanje (npr. Hardware Wallet – njegova glavna svrha), onda biste mogli pomisliti da nije toliko važno imati „čist“ računar – nije tačno.


Računar zaražen malverom može očitati vaše Bitcoin adrese, izlažući vaš saldo napadaču – ne mogu uzeti Bitcoin samo znajući Address, ali mogu videti koliko imate i na osnovu toga izračunati da li ste vredna meta. Takođe mogu nekako saznati gde živite, na primer, i izvući nokte ili decu od vas kako bi vas naterali da platite otkupninu.


## Koje je rešenje?


Podstičem većinu Bitcoinera da koriste namenski računar bez malvera (sa pristupom internetu) za obavljanje Bitcoin transakcija. Predlažem ljudima da koriste operativni sistem otvorenog koda kao što je Linux Mint, ali koristite Windows ili Mac ako morate – to je bolje nego koristiti običan, često korišćen računar koji neizbežno ima skriven malver.


Jedna prepreka na koju ljudi nailaze je instaliranje novog operativnog sistema na takvim računarima. Ovaj vodič je tu da pomogne u tome.


Postoji mnogo varijanti Linuxa i isprobao sam nekoliko. Moja preporuka za Bitcoinere je Linux Mint, jer je jednostavan za instalaciju, veoma brz (posebno pri pokretanju i gašenju), nije pretrpan (svaki dodatni softver je rizik), i retko mi se rušio ili ponašao čudno (u poređenju sa drugim verzijama kao što su Ubuntu i Debian).


Neki mogu biti veoma otporni prema novom operativnom sistemu, preferirajući Windows ili Mac OS. Razumem, ali Windows i Apple operativni sistemi su zatvorenog koda, tako da moramo verovati onome što rade; mislim da to nije dobra politika, ali nije sve ili ništa. Mnogo bih više voleo da ljudi koriste namenski sveže instaliran Windows ili Mac OS računar nego dobro korišćen računar (sa ko zna kakvim malverom koji se nakupio na njemu). Jedan korak bolje je koristiti sveže instaliran Linux računar, što ću i demonstrirati.


Ako ste nervozni zbog korišćenja Linux-a zbog nepoznatog, to je prirodno, ali isto tako je prirodno odvojiti malo vremena za učenje. Toliko informacija je dostupno na internetu. Evo odličnog kratkog videa koji uvodi osnove komandne linije i koji toplo preporučujem.

Izaberite računar


Počeću sa onim što mislim da je najbolja opcija. Zatim ću dati svoje mišljenje o alternativama.


Idealna opcija:


Moja preporuka, ako to možete priuštiti, i ako veličina vašeg Bitcoin steka to opravdava, jeste da nabavite potpuno nov laptop početnog nivoa. Najosnovniji model napravljen ovih dana je dovoljno dobar da se nosi sa onim za šta će biti korišćen. Specifikacije procesora i RAM-a nisu relevantne, jer će svi biti dovoljno dobri.


Izbegavajte:



- Bilo koja kombinacija tableta, uključujući Surface Pro
- Chromebookovi – često je kapacitet skladišta prenizak
- Bilo koji računar sa eMMC diskom; Ako ima SSD disk, to je savršeno
- Macovi – skupi su, a hardver se po mom iskustvu ne slaže dobro sa Linux operativnim sistemima.
- Bilo šta obnovljeno ili polovno (iako nije apsolutni prekid dogovora)


Umesto toga, potražite laptop sa Windows 11 (Trenutno je Windows 11 najnovije izdanje. Rešićemo se tog softvera, ne brinite.). Pretražio sam amazon.com za "Windows 11 Laptop" i pronašao ovaj dobar primer:


![image](assets/1.webp)


Cena ovog gore je dobra. Specifikacije su dovoljno dobre. Ima ugrađenu kameru koju možemo koristiti za QR kod PSBT transakcije (inače biste morali kupiti USB kameru za to). Ne brinite zbog činjenice da nije dobro prepoznatljiv brend (jeftin je). Ako želite bolji brend, koštaće vas, npr:


![image](assets/2.webp)


Neki od jeftinijih imaju samo 64Gb prostora na disku; nisam testirao laptopove sa tako malim diskovima – verovatno je u redu imati 64Gb, ali možda je na granici.


## Druge opcije – Repovi


Tails je operativni sistem koji se pokreće sa USB fleš diska i privremeno preuzima hardver bilo kog računara. Koristi isključivo Tor konekcije, tako da bi trebalo da budete komforni sa korišćenjem Tor-a. Nijedan podatak koji zapišete u memoriju tokom vaše sesije se ne čuva na disku (svaki put počinje iznova) osim ako ne prilagodite podešavanja i kreirate opciju trajnog skladištenja (na USB fleš disku) – koju zaključavate lozinkom.


Nije loša opcija i besplatna je, ali je malo nezgrapna za našu svrhu. Instaliranje novog softvera na nju nije jednostavno. Jedna dobra karakteristika je što dolazi sa Electrum-om, ali loša strana toga je što ga niste sami instalirali. Uverite se da USB drajv koji koristite ima najmanje 8Gb.


Vaša fleksibilnost je smanjena ako koristite Tails. Možda nećete moći da pratite razne vodiče za podešavanje onoga što vam je potrebno i da to pravilno funkcioniše. Na primer, ako pratite moj vodič za instalaciju Bitcoin Core, potrebne su izmene da bi to radilo. Ne mislim da ću praviti vodič specifičan za Tails, tako da biste morali da razvijete svoje veštine i to uradite sami.


Takođe nisam siguran kako će hardverski novčanici funkcionisati sa ovim OS-om.


Rekavši sve ovo, Tails računar za Bitcoin transakcije je lepa dodatna opcija i sigurno će pomoći vašim ukupnim veštinama privatnosti da naučite koristiti Tails.


## Druge opcije – Live OS Boot


Ovo je vrlo slično Tails-u, osim što operativni sistem nije posvećen privatnosti. Osnovni način korišćenja je da flešujete USB drajv sa Linux operativnim sistemom po vašem izboru i naterate računar da se pokrene sa njega umesto sa internog drajva. Kako to uraditi je objašnjeno kasnije.


Prednost je što ste manje ograničeni i stvari će funkcionisati bez naprednih podešavanja.


Nisam siguran koliko dobro takav sistem izoluje malver na postojećem računaru od USB boot drajva koji koristite i koji sadrži novi operativni sistem. Verovatno obavlja dobar posao i verovatno nije tako dobar kao Tails. Pošto ne znam, moja preferencija je posvećeni laptop.

Druge opcije – Vaš sopstveni korišćeni laptop ili desktop računar


Korišćenje polovnog računara nije idealno, uglavnom zato što nisam upoznat sa unutrašnjim radom sofisticiranog malvera, niti da li je brisanje diska dovoljno da ga se rešim. Verovatno jeste, ali ne želim da potcenim koliko lukavi zlonamerni hakeri mogu biti. Ti možeš odlučiti, ja ne želim da se obavezujem.


Ako odlučite da koristite stari desktop umesto starog laptopa, to će biti u redu, osim što će zauvek zauzimati prostor za vaše verovatno retke Bitcoin transakcije; ne biste ga trebali koristiti za bilo šta drugo. Dok sa laptopom, možete ga jednostavno skloniti, pa čak i sakriti radi dodatne sigurnosti.


## Instaliranje Linux Mint-a na bilo koji računar


Ovo su uputstva za brisanje bilo kog operativnog sistema sa vašeg novog laptopa i instalaciju Linux Mint-a, ali ih možete prilagoditi za instalaciju gotovo bilo koje verzije Linux-a na gotovo bilo koji računar.


Mi ćemo koristiti bilo koji računar da flešujemo operativni sistem na neku vrstu memorijskog stika. Nije bitno koji memorijski stik, sve dok je kompatibilan sa USB portom, i predlažem minimum 16Gb.


Nabavi jednu od ovih stvari:


![image](assets/3.webp)


Ili možete koristiti nešto poput ovoga:


![image](assets/4.webp)


Zatim, idite na linuxmint.com


![image](assets/5.webp)


Pređite mišem preko menija Download na vrhu, a zatim kliknite na link, „Linux Mint 20.3“ ili koja god verzija je najnovija preporučena u trenutku kada to radite.


![image](assets/6.webp)


Postojaće nekoliko „ukusa“ za izbor. Izaberite „Cimet“ da biste pratili ovaj vodič. Kliknite na dugme Preuzmi.


![image](assets/7.webp)


Na sledećoj stranici, možete se pomeriti nadole da vidite ogledala (Ogledala su različiti serveri koji drže kopiju fajla koji želimo). Možete verifikovati preuzimanje koristeći SHA256 i gpg (preporučeno), ali ću preskočiti objašnjavanje toga ovde jer sam već napisao vodiče o tome.


![image](assets/8.webp)


Izaberite ogledalo koje vam je najbliže i kliknite na njegov link (tekst Green u koloni ogledala). Datoteka će početi sa preuzimanjem – verzija koju preuzimam je 2.1 gigabajta.


Jednom kada se preuzme, možete flešovati fajl na prenosivi memorijski uređaj i učiniti ga butabilnim. Da biste to uradili, najlakši način je da koristite Balena Etcher. Preuzmite i instalirajte ga ako ga nemate.


Zatim ga pokreni:


![image](assets/9.webp)


Kliknite na flash iz datoteke i izaberite LinuxMint datoteku koju ste preuzeli.


Zatim kliknite na Izaberi cilj. Uverite se da je memorijski uređaj priključen i da birate ispravan disk, inače možete uništiti sadržaj pogrešnog diska!


Nakon toga, izaberite Flash! Možda ćete morati uneti svoju lozinku. Kada se završi, verovatno neće biti moguće čitati drajv na vašem Windows ili Mac računaru jer je pretvoren u Linux uređaj. Samo ga izvucite.

Priprema ciljanog računara


Uključite novi laptop i dok se pokreće, držite pritisnut BIOS taster. To je obično F2, ali može biti F1, F8, F10, F11, F12 ili Delete. Pokušajte svaki dok ne uspete, ili pretražite internet za model vašeg računara i postavite pravo pitanje.


Npr. “BIOS taster Dell laptopovi”.


Svaki računar će imati drugačiji BIOS meni. Istražite i pronađite koji meni vam omogućava da konfigurišete redosled pokretanja. Za naše potrebe, želimo da računar pokuša da se pokrene sa USB povezanog uređaja (ako je neki povezan), pre nego što pokuša da se pokrene sa internog Hard diska (u suprotnom će se učitati Windows). Kada to postavite, možda ćete morati da sačuvate pre izlaska ili će se možda automatski sačuvati.


Ponovo pokrenite računar i trebalo bi da se učita sa USB memorijskog uređaja. Ne možemo instalirati Linux na interni disk i Windows će biti trajno uklonjen.


Kada dođete do sledećeg ekrana, izaberite “OEM install (for manufacturers)”. Ako umesto toga izaberete “Start Linux Mint”, dobićete Linux Mint sesiju učitanu sa memorijskog uređaja, ali kada isključite računar, nijedna vaša informacija neće biti sačuvana – to je u suštini privremena sesija kako biste mogli da je isprobate.


![image](assets/10.webp)


Bićete vođeni kroz grafički čarobnjak koji će vam postaviti nekoliko pitanja koja bi trebala biti jednostavna. Jedno će biti podešavanje jezika, drugo će biti vaša kućna internet mrežna veza i lozinka. Ako vam se ponudi instalacija dodatnog softvera, odbijte je. Kada dođete do pitanja o tipu instalacije, neki ljudi mogu oklevati – potrebno je da izaberete “Obriši disk i instaliraj Linux Mint”. Takođe, nemojte šifrovati disk i nemojte odabrati LVM.


Na kraju ćete stići do desktopa. U ovom trenutku, još uvek niste sasvim završili. Zapravo delujete kao proizvođač (tj. neko ko sklapa računar i postavlja Linux za kupca). Potrebno je da dvaput kliknete na ikonu na desktopu, „Install Linux Mint“, da biste ga finalizirali.


![image](assets/11.webp)


Zapamti da ukloniš memorijski stik, a zatim ponovo pokreni računar. Nakon ponovnog pokretanja, koristićeš operativni sistem prvi put kao novi korisnik. Čestitamo.


Jedna od prvih stvari koju treba uraditi (i raditi redovno) jeste održavanje sistema ažurnim.


Otvorite aplikaciju Terminal i upišite sledeće:


```bash
sudo apt-get update
```


pritisnite <enter>, potvrdite svoj izbor, a zatim ovu komandu:


```bash
sudo apt-get upgrade
```


pritisnite <enter> i potvrdite svoj izbor.


Neka radi svoje, može potrajati nekoliko minuta.


Dalje, voleo bih da instaliram Tor (osetljivo na velika i mala slova):


```bash
sudo apt-get install tor
```


**Profesionalni savet:** Takođe možete pokrenuti Linux Mint sa “OEM install” (Uverite se da ste povezani na internet, inače možete dobiti greške). Ako to uradite, kasnije treba da kliknete na ikonu “ship to end user” koja bi trebala biti na radnoj površini. Zatim ponovo pokrenete računar i pokrenete operativni sistem kao da prvi put otvarate računar.


Ovaj vodič je objasnio zašto vam može biti potreban posvećen računar za Bitcoin transakcije i kako instalirati novi Linux Mint operativni sistem na njega.