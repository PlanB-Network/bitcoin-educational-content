---
name: Umbrel
description: Otkrijte i instalirajte Umbrel - Vaš Bitcoin čvor i kućni server
---

![cover](assets/cover.webp)



## Uvod



### Šta je Bitcoin čvor?



Bitcoin čvor je računar koji učestvuje u Bitcoin mreži pokretanjem Bitcoin Core softvera ili alternativnog klijenta. Njegova uloga je ključna za rad i bezbednost mreže:





- **Blockchain skladište**: Održava potpunu, ažuriranu kopiju Bitcoin Blockchain-a 
- **Verifikacija transakcije**: validira svaku transakciju i blok prema pravilima protokola
- **Širenje informacija**: Deli nove transakcije i blokove sa drugim čvorovima
- **Izgradnja konsenzusa**: Doprinosi primeni mrežnih pravila



Pokretanje sopstvenog Bitcoin čvora je ključni korak ka finansijskoj suverenosti, nudeći nekoliko ključnih prednosti:





- **Poverljivost**: Delite svoje transakcije bez otkrivanja vaših informacija trećim stranama
- **Otpor cenzuri**: Niko te ne može sprečiti da koristiš Bitcoin
- **Nezavisna verifikacija**: Nema potrebe da verujete čvorovima drugih ljudi da biste verifikovali svoje transakcije
- **Izgradnja konsenzusa**: Doprinesite primeni pravila Bitcoin mreže
- **Podrška mreži**: Postanite aktivni učesnik u distribuciji i decentralizaciji mreže



### Umbrel: Jednostavno rešenje za pokretanje Bitcoin čvora



Umbrel je operativni sistem otvorenog koda koji pojednostavljuje instalaciju i upravljanje Bitcoin čvorom. Takođe transformiše vaš računar u lični i privatni kućni server, olakšavajući hostovanje :





- Kompletnog Bitcoin čvora
- Bitcoin osnovnih aplikacija (Electrs, Mempool.space)
- Ostalih ličnih usluga (skladištenje u oblaku, striming, VPN, itd.)



Sa svojim elegantnim i intuitivnim korisničkim interfejsom, Umbrel čini samohostovane usluge dostupnim svima, dok zadržava potpunu kontrolu nad vašim podacima.



## Opcije instalacije Umbrel-a



Umbrel nudi dva glavna načina korišćenja njihovog rešenja: gotovu opciju (Umbrel Home) i besplatnu verziju otvorenog koda (UmbrelOS).



![Comparaison Umbrel Home et UmbrelOS](assets/fr/22.webp)



### Umbrel Home: Rešenje po principu "ključ u ruke"



Umbrel Home je unapred konfigurisan kućni server, posebno dizajniran za optimalno iskustvo. Ovo sve-u-jednom hardversko rešenje uključuje:



**Hardverske karakteristike**




- Procesor visokih performansi optimizovan za samostalno hostovanje
- Unapred instalirana SSD memorija velike brzine
- Tihi sistem hlađenja
- Kompaktan, elegantan dizajn
- Integrisani USB i Ethernet portovi



**Ekskluzivne pogodnosti**




- Instalacija plug-and-play: priključi i kreni
- Premium podrška sa posvećenom asistencijom
- Zagarantovane automatska ažuriranja
- Integrisani čarobnjak za migraciju
- Puna garancija na hardver
- Potpuna podrška za sve funkcionalnosti



**Cena**: €399 (cena može varirati u zavisnosti od sezone)



### UmbrelOS: Verzija otvorenog koda



UmbrelOS je besplatna, otvorena verzija Umbrel operativnog sistema. Ovo fleksibilno rešenje omogućava vam da koristite sopstveni hardver dok koristite osnovne funkcije Umbrel-a.



**Prednosti**




- Potpuno besplatno
- Otvoreni, proverljivi izvorni kod
- Sloboda izbora
- Napredne opcije prilagođavanja



**Podržane platforme**




- Raspberry Pi 5: Popularno i pristupačno rešenje
- X86 sistemi: Za standardne PC-je ili servere
- Virtuelna mašina: Za testiranje ili korišćenje na postojećoj infrastrukturi



**Ograničenja




- Postoji samo podrška zajednice
- Neke napredne funkcije rezervisane za Umbrel Home
- Više tehničke početne konfiguracije
- Performanse zavisi od izabranog hardvera



Ova verzija je idealna za :




- Tehničke korisnike
- One koji već poseduju kompatibilnu opremu
- Ljude koji žele da uče i eksperimentišu
- Programeri koji žele da doprinesu projektu



Zvanični linkovi za instalaciju :




- [Instalacija na Raspberry Pi 5](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- [Instalacija na x86 sistemima](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-x86-Systems)
- [Instalacija virtuelne mašine](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Linux-VM)



U ovom vodiču, fokusiraćemo se na instalaciju UmbrelOS-a na Raspberry Pi 5, ali osnovni principi ostaju slični za druge platforme.



## Instaliranje Umbrel OS na Raspberry Pi 5



### Potrebne komponente



Za ovu instalaciju će vam trebati :





- Raspberry Pi 5 (4 GB ili 8 GB RAM)
- Zvanično napajanje za Raspberry Pi (ključan za stabilnost!)
- MicroSD kartica (minimum 32 GB)
- Čitač microSD kartica
- Eksterni SSD za skladištenje podataka
- Ethernet kabl
- USB kabl za povezivanje SSD-a



### Koraci instalacije



**Preuzmi UmbrelOS**



![Téléchargement UmbrelOS](assets/fr/01.webp)




- Posetite [zvaničnu veb stranicu](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- Preuzmite najnoviju verziju UmbrelOS za Raspberry Pi 5



**Balena Etcher** instalacija



![Téléchargement Balena Etcher](assets/fr/02.webp)




- Preuzmite i instalirajte [Balena Etcher](https://www.balena.io/etcher/) na vaš računar



**Priprema microSD** kartice



![Insertion carte microSD](assets/fr/03.webp)




- Umetnite svoju microSD karticu u čitač kartica na računaru.



**Upisivanje slike sistema**



![Flashage UmbrelOS](assets/fr/04.webp)




- Pokreni Balena Etcher
- Izaberite preuzetu UmbrelOS sliku
- Izaberite svoju microSD karticu kao odredište
- Kliknite na "Flash!" i sačekajte da se proces završi
- Bezbedno izbacite karticu



**instalacija microSD kartice**



![Installation microSD](assets/fr/05.webp)




- Umetnite microSD karticu u vaš Raspberry Pi 5



**Periferna veza**



![Connexion périphériques](assets/fr/06.webp)




- Povežite eksterni SSD na slobodan USB port
- Povežite Ethernet kabl između Pi uređaja i vašeg rutera.



**Uključi**



![Démarrage du Pi](assets/fr/07.webp)




- Povežite zvanično napajanje za Raspberry Pi
- Sačekajte nekoliko minuta da se sistem pokrene.



**Prvi pristup**



![Accès interface web](assets/fr/08.webp)




- Na uređaju povezanom na istu mrežu, otvorite svoj pregledač.
- Pristupite Umbrelovoj veb stranici na: `http://umbrel.local`



![Page d'accueil Umbrel](assets/fr/09.webp)



Ako `umbrel.local` ne radi, moraćete da pronađete IP adresu vašeg Raspberry Pi-ja na vašoj lokalnoj mreži. Možete:




- Konsultovati interfejs svog rutera
- Koristiti mrežni skener kao što je nmap
- Koristiti komandu `arp -a` u terminalu vašeg računara



## Prvi korak na Umbrel-u



Kada se vaš Umbrel pokrene i postane dostupan putem vašeg pregledača, pratite ove korake da biste započeli:



### Početna konfiguracija



**Kreiraj svoj nalog**



![Création compte](assets/fr/10.webp)




- Izaberite korisničko ime
- Postavite sigurnu lozinku
- Trebaće vam ovi kredencijali kako biste pristupili vašem Umbrel-u



**Potvrda naloga



![Confirmation compte](assets/fr/11.webp)




- Kliknite na "Next" da biste pristupili vašoj kontrolnoj tabli



**Upoznavanje sa interfejsom**



![Interface Umbrel](assets/fr/12.webp)




- Pristupite Umbrel App Store-u
- Otkrijte mnoge dostupne aplikacije
- Hajde da počnemo sa instaliranjem osnovnih aplikacija za Bitcoin



### Instaliranje Bitcoin aplikacija



**Bitcoin čvor**



![Bitcoin Node](assets/fr/13.webp)




- Prva aplikacija za instalaciju
- Preuzmi i proveri ceo Bitcoin Blockchain 



**Electrs**



![Installation Electrs](assets/fr/14.webp)




- Electrum server za povezivanje Bitcoin novčanika
- Sinhronizuje se sa vašim Bitcoin čvorom



**Mempool**



![Installation Mempool](assets/fr/15.webp)




- Interfejs za prikaz blokčejna
- Prati transakcije i blokove u realnom vremenu



## Praćenje transakcije sa Mempool.space



Mempool.space je open-source Blockchain explorer koji pruža vizualizaciju u realnom vremenu Bitcoin mreže. Omogućava vam praćenje vaših transakcija i razumevanje kako se transakcije šire na mreži.



### Razumevanje Mempool-a i potvrde



"Mempool" (memorijski bazen) je kao virtuelna čekaonica gde su sve nepotvrđene Bitcoin transakcije smeštene pre nego što budu uključene u blok. Evo kako se transakcija obrađuje:



1. **Emitovanje**: Kada pošaljete transakciju, ona se prvo emituje na Bitcoin mreži


2. **Čekanje u Mempool-u**: Čekanje da bude izabran od strane rudara na osnovu troškova transakcije


3. **Prva potvrda**: Rudar ga uključuje u blok (1. potvrda)


4. **Dodatne potvrde**: Svaki novi blok iskopan nakon onog koji sadrži vašu transakciju dodaje novu potvrdu



Preporučeni broj potvrda zavisi od iznosa :




- Za male iznose: 1-2 potvrde mogu biti dovoljne
- Za velike iznose: 6 potvrda se obično smatra veoma sigurnim



### Istraživanje interfejsa Mempool.space-a



1. **Početna stranica** daje vam pregled Bitcoin mreže:




   - Nedavno iskopani blokovi
   - Procene troškova za različite prioritete
   - Trenutno stanje Mempool-a



![Page d'accueil de Mempool.space avec visualisation des blocs et estimations de frais](assets/fr/23.webp)



2. **Pretraži transakciju**: Da biste pratili određenu transakciju, nalepite njen identifikator (txid) u traku za pretragu na vrhu stranice.



![Recherche d'une transaction dans Mempool.space](assets/fr/24.webp)



### Analiziraj detalje transakcije



Jednom kada vaša transakcija bude pronađena, Mempool.space vam predstavlja kompletnu analizu:



1. **Osnovne informacije** :




   - Status (potvrđeno ili ne)
   - Plaćeni troškovi (u Sats/vB)
   - Procenjeno vreme potvrde



![Détails des frais et statut de la transaction](assets/fr/25.webp)



2. **Struktura transakcije** :




   - Vizuelna reprezentacija ulaza i izlaza
   - Detaljna lista uključenih adresa
   - Preneseni iznosi



3. **Tehnički podaci** :




   - Težina transakcije
   - Virtuelna veličina
   - Format i korišćena verzija 
   - Ostali specifični metapodaci



![Informations techniques et structure des entrées/sorties](assets/fr/26.webp)



### Prednosti korišćenja Mempool.space na Umbrel-u



1. **Poverljivost**: Vaši zahtevi prolaze kroz vaš sopstveni čvor


2. **Nezavisnost**: Nema potrebe za oslanjanjem na uslugu treće strane


3. **Pouzdanost**: Pristup podacima čak i kada javni pregledači ne rade



Pomoću ove aplikacije možete efikasno pratiti svoje transakcije, razumeti kako naknade utiču na brzinu potvrde i steći bolje razumevanje kako Bitcoin mreža funkcioniše.



## Povezivanje Bitcoin novčanika na vaš čvor



### Konfiguracija Electrs



**Lokalna veza**



![Connexion locale](assets/fr/18.webp)




- Za korišćenje na vašoj lokalnoj mreži
- Brže i lakše za postavljanje



**Daljinska veza putem Tor-a**



![Connexion Tor](assets/fr/19.webp)




- Da pristupite svom čvoru sa bilo kog mesta
- Bezbednije i privatnije



### Povezivanje sa Sparrow novčanikom



**Pristup parametrima**



![Paramètres Sparrow](assets/fr/20.webp)




- Otvorite Sparrow novčanik
- Idite na Preferences > Server
- Kliknite na "Modify existing connection", u prevodu "Izmeni postojeću vezu"



**Izbor tipa veze**



Sparrow nudi tri režima povezivanja:



***Javni Server***




- Povezivanje na javne servere (npr. blockstream.info, Mempool.space)
- Jednostavno, ali manje privatno



***Bitcoin Core***




- Direktna veza sa Bitcoin čvorom
- Privatno ali sporije



***Privatni Electrum***




- Povežite se sa svojim Electrs serverom
- Kombinuje poverljivost i performanse



**Electrs** konfiguracija



Izaberite tip veze koristeći informacije prikazane u aplikaciji Electrs koju smo ranije videli:



U oba slučaja, ostavite opcije "Use SSL" i "Use proxy" neoznačenim.



**Lokalna veza**


Host: umbrel.local


Broj porta: 50001



**Daljinska veza (Tor)**


Host : [your-Address-onion]


Broj porta: 50001



Tor veza je neophodna ako želite pristupiti svom čvoru izvan vaše lokalne mreže.



![Configuration connexion](assets/fr/21.webp)


Za više informacija o softveru Sparrow Wallet, imamo sveobuhvatan vodič :


https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d
## Zaključak



Vaš Umbrel je sada spreman za korišćenje. Aktivno učestvujete u Bitcoin mreži dok zadržavate potpunu kontrolu nad vašim podacima. Slobodno istražite mnoge druge aplikacije dostupne u Umbrel App Store-u kako biste proširili mogućnosti vašeg kućnog servera.



## Korisni resursi



### Zvanična dokumentacija




- [Officialna Umbrel veb stranica](https://umbrel.com)
- [Umbrel dokumentacija](https://github.com/getumbrel/umbrel/wiki)
- [App Store Umbrel](https://apps.umbrel.com)



### Bitcoin aplikacije




- [Bitcoin Core](https://Bitcoin.org/fr/)
- [Electrs](https://github.com/romanz/electrs)
- [Mempool](https://Mempool.space)
- [Sparrow Wallet](https://sparrowwallet.com)



### Zajednica




- [Forum Umbrel](https://community.getumbrel.com)
- [GitHub Umbrel](https://github.com/getumbrel)
- [Twitter Umbrel](https://twitter.com/umbrel)
