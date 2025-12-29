---
name: Nasleđe
description: Bitcoin portfolio sa integrisanim mehanizmom nasleđivanja putem Taproot skripti
---

![cover](assets/cover.webp)



Prenos bitkoina u slučaju smrti ili nesposobnosti predstavlja veliki izazov za svakog vlasnika kripto-imovine. Bez odgovarajućeg plana nasleđivanja, ova sredstva postaju nepopravljiva za vaše voljene.



Heritage pruža elegantan odgovor implementacijom mehanizma "dead-man switch" direktno na Bitcoin blockchainu. Ovaj open-source wallet omogućava konfiguraciju uslova sukcesije za on-chain: ako vlasnik ne izvrši daljnje transakcije tokom definisanog perioda, unapred određeni alternativni ključevi mogu osloboditi sredstva.



## Šta je nasleđe?



Heritage je Bitcoin portfolio koje izvorno integriše mehanizam nasleđivanja putem Taproot skripti. Razvijen pod MIT licencom od strane Jérémie Rodona, ovaj softver otvorenog koda garantuje transparentnost i trajnost.



Nasleđe koristi Taproot skripte kodirane u Bitcoin adresama. Svaki UTXO integriše dve vrste uslova potrošnje:





- Primarni put** : Vlasnik može trošiti svoje bitkoine u bilo koje vreme sa svojim primarnim ključem
- Alternativni putevi**: Za svakog određenog naslednika, skripta kombinuje njegov javni ključ sa vremenskom bravom



Svaka transakcija vlasnika automatski odlaže datum aktivacije klauzula o nasleđivanju. U slučaju produžene neaktivnosti (smrt, nesposobnost), uslovi se automatski aktiviraju.



## Heritage usluga (opciono)



Heritage nudi dve opcije korišćenja:



**Uradi sam (besplatno)**: Samo open-source aplikacija. Sve upravljate autonomno sa svojim čvorom. Ova opcija nudi ugrađeni pristup za backup, ugrađeno nasleđivanje i ekskluzivnu kontrolu nad vašim bitcoinima. Međutim, morate sami kreirati upozorenja (kalendar, podsetnici) kako ne biste zaboravili da obnovite svoje vremenske brave, i nema automatskih obaveštenja za vaše naslednike.



**Koristite uslugu (0,05% godišnje)** : btc-heritage.com usluga dodaje funkcije za pojednostavljenje upravljanja:




- Automatski podsetnici pre isteka vaših rokova
- Automatska obaveštenja naslednicima kako bi ih vodila kroz proces oporavka
- Prioritetna podrška
- Pojednostavljeno upravljanje deskriptorima



Naknada: 0,05% od upravljanog iznosa godišnje, minimum 0,5 mBTC/god. Prva godina besplatna.



Usluga ostaje ne-kustodijalna: vaši privatni ključevi nikada ne napuštaju vaš uređaj. Heritage ne može pristupiti vašim sredstvima.



## Heritage CLI



Za napredne korisnike koji preferiraju terminal, Heritage nudi alat za komandnu liniju (CLI) za detaljnu kontrolu i rad na mašinama bez mrežnog povezivanja.



![Page Heritage CLI](assets/fr/03.webp)



Kompletna dokumentacija za CLI dostupna je na [btc-heritage.com/heritage-cli](https://btc-heritage.com/heritage-cli). Ovde ćete pronaći uputstva za preuzimanje, povezivanje sa servisom, kreiranje novčanika (sa Ledger ili lokalnim ključevima), upravljanje naslednicima i transakcijama.



Ovaj vodič se fokusira na Desktop aplikaciju, koja je pristupačnija većini korisnika.



## Heritage Desktop



Heritage Desktop je grafička aplikacija sa intuitivnim interfejsom koji vodi korisnika kroz svaki korak procesa konfiguracije.



### Preuzmi



Idite na [btc-heritage.com](https://btc-heritage.com) i kliknite na "Download application".



![Page d'accueil Heritage](assets/fr/01.webp)



Izaberite verziju koja odgovara vašem operativnom sistemu (Linux 64bita ili Windows 64bita). Binarni fajlovi nisu digitalno potpisani, što može izazvati sigurnosna upozorenja.



![Page de téléchargement](assets/fr/02.webp)



### Instalacija na Linux-u



Na Linuxu, aplikacija se distribuira u AppImage formatu. Pre nego što je možete pokrenuti, potrebno je da instalirate zavisnost `libfuse2`:



```bash
sudo apt install libfuse2
```



![Installation libfuse2](assets/fr/04.webp)



Zatim učinite datoteku izvršnom i pokrenite je:



```bash
chmod +x Heritage-GUI-vX.X.X.AppImage
./Heritage-GUI-vX.X.X.AppImage
```



### Prvo lansiranje



Prilikom prvog pokretanja, čarobnjak za uvod nudi vam tri izbora:



![Onboarding initial](assets/fr/05.webp)





- Postavljanje Heritage Wallet**: Kreirajte novi wallet sa heritage planom
- Nasledite bitkoine**: Povratite bitkoine kao naslednik
- Istraži samostalno**: Istraži funkcije bez pomoći



Odaberite "Setup an Heritage Wallet" da biste kreirali svoj prvi wallet.



### Bitcoin mrežna veza



Izaberite kako da se povežete na Bitcoin mrežu:



![Choix connexion](assets/fr/06.webp)





- Korišćenje Heritage Service**: Upravljana infrastruktura, jednostavnije za naslednike
- Korišćenje sopstvenog čvora**: Povežite se sa sopstvenim Bitcoin Core ili Electrum čvorom



Za ovaj vodič koristimo naš čvor.



### Upravljanje privatnim ključem



Izaberite kako da upravljate svojim privatnim ključevima:



![Gestion des clés](assets/fr/07.webp)





- Sa Ledger Hardverskim Uređajem** : Maksimalna sigurnost sa wallet hardverom (preporučeno)
- Lokalno skladištenje sa lozinkom**: Lokalno skladišteni ključevi sa zaštitom lozinkom
- Vratite postojeći wallet** : Vratite iz postojećeg seed



### Konfiguracija čvora



Ako koristite svoj čvor, aplikacija vas vodi kroz njegovu konfiguraciju. Uverite se da je vaš Bitcoin ili Electrum čvor:




- Instalirano i pokrenuto
- Sinhronizovano sa Bitcoin mrežom
- Konfigurisano za prihvatanje RPC konekcija (za Bitcoin Core)



![Configuration nœud](assets/fr/08.webp)



Kliknite na "Moj Bitcoin čvor je pokrenut i radi" kada je vaš čvor spreman.



### Status panel



Kliknite na "Status" u gornjem desnom uglu, zatim na "Open Configuration" da biste pristupili parametrima veze.



![Panneau Status](assets/fr/09.webp)



Postavite URL vašeg Electrum servera (npr. `umbrel.local:50001` ako koristite Umbrel).



![Configuration Electrum](assets/fr/10.webp)



### Kreiranje wallet



Kada se veza uspostavi, kliknite na "Create Wallet" u kartici WALLETS.



![Créer wallet](assets/fr/11.webp)



Iskačući prozor objašnjava podeljenu arhitekturu Heritage :



![Architecture split](assets/fr/12.webp)



1. **Key Provider (Offline)**: Upravljа vašim privatnim ključevima i potpisuje transakcije. Može biti Ledger ili wallet softver.


2. **Online Wallet**: Rukuje sinhronizacijom sa Bitcoin mrežom, kreiranjem adresa i emitovanjem transakcija.



Popunite obrazac za kreiranje :



![Formulaire création wallet](assets/fr/13.webp)





- Wallet Ime**: Jedinstveno ime za identifikaciju vašeg wallet
- Ključni Provajder**: Izaberite Lokalno Skladištenje Ključeva za ovaj tutorijal
- Novo/Obnovi**: Izaberite "Novo" za generate novi seed
- Broj reči**: 24 reči preporučeno za maksimalnu sigurnost



Unesite jaku lozinku i izaberite opcije za Online Wallet :



![Options Online Wallet](assets/fr/14.webp)





- Lokalni Čvor**: Koristi vaš sopstveni Electrum ili Bitcoin Core čvor
- Heritage Service**: Koristi Heritage uslugu (preporučeno za funkcije obaveštavanja)



Kliknite na "Create Wallet" da biste završili kreiranje.



### Interface from wallet



Vaš wallet je sada kreiran. Interfejs prikazuje :



![Interface wallet](assets/fr/15.webp)





- Ravnoteža
- SEND i RECEIVE dugmad
- Istorija transakcija
- Istorija konfiguracije nasleđa
- wallet adrese



### Stvaranje naslednika



Idite na karticu "HEIRS" da kreirate svoje naslednike.



![Page Heirs](assets/fr/16.webp)



Informativni iskačući prozor objašnjava:




- Naslednici su Bitcoin javni ključevi povezani sa pojedincima
- Svaki naslednik ima svoju mnemotehničku frazu
- Prvi naslednik treba da bude "Backup" za vas (u slučaju gubitka vašeg glavnog wallet)



#### Kreiranje rezervnog naslednika



Kliknite na "Create Heir" i imenujte ga "Backup".



![Création héritier Backup](assets/fr/17.webp)



Iskačući prozor objašnjava zašto je rečenica od 12 reči bez passphrase bezbedna za naslednike:


1. **Nema trenutnog pristupa**: Naslednički ključevi ne mogu pristupiti sredstvima dok vremenska brava ne istekne


2. **Detekcija kompromitacije**: Ako neko pristupi frazi, možete ažurirati konfiguraciju Heritage


3. **Dugoročna pristupačnost**: passphrase bi mogao biti zaboravljen nakon mnogo godina



Konfiguriši naslednika :



![Configuration héritier](assets/fr/18.webp)





- Ključni Provajder** : Lokalno Skladištenje Ključeva
- Novo**: Generiši novi seed
- Broj reči**: 12 reči



Finalizujte kreaciju :



![Finalisation héritier](assets/fr/19.webp)





- Tip Naslednika**: Prošireni Javni Ključ
- Izvoz u uslugu**: Opcionalno, omogućava automatsko obaveštavanje naslednika



Rezervni naslednik je sada kreiran:



![Héritier créé](assets/fr/20.webp)



#### Čuvanje mnemoničke fraze naslednika



Kliknite na Backup heir, a zatim na "Show Mnemonic" :



![Afficher mnemonic](assets/fr/21.webp)



**VAŽNO: Zapišite ovih 12 reči i čuvajte ih na sigurnom mestu. Ovo je ključ za povrat sredstava.



![Phrase mnémotechnique](assets/fr/22.webp)



#### Uklanjanje seed iz aplikacije



Kada zapišete frazu, pristupite parametrima naslednika (ikona zupčanika):



![Paramètres héritier](assets/fr/23.webp)



Koristite "Strip Heir Seed" da uklonite privatni ključ iz aplikacije. Potvrdite da ste sačuvali frazu.



![Strip Heir Seed](assets/fr/24.webp)



Ovo je sigurnosna mera: samo javni ključ ostaje u aplikaciji, što je dovoljno za konfigurisanje nasleđivanja.



#### Stvaranje drugog naslednika



Ponovite proces da biste kreirali drugog naslednika (npr. "Satoshi"). Sada ćete imati dva naslednika:



![Deux héritiers](assets/fr/25.webp)





- Backup**: Vaš lični ključ za hitne slučajeve
- Satoshi**: Određeni naslednik



### Konfiguracija nasleđa



Vratite se na svoj wallet i kliknite na ikonu Postavke:



![Paramètres wallet](assets/fr/26.webp)



U odeljku "Heritage Configuration" kliknite na "Create":



![Heritage Configuration](assets/fr/27.webp)



Postavite vremenska ograničenja za svakog naslednika:



![Configuration délais](assets/fr/28.webp)





- Backup**: 180 dana (6 meseci) - Datum dospeća: 2026-06-18
- Satoshi**: 455 dana (15 meseci) - Datum dospeća: 2027-03-20



**Važno**: Svaki naslednik mora imati duže kašnjenje od prethodnog. Prvi naslednik (Rezerva) će prvi imati pristup sredstvima.



Takođe konfiguriši :



![Configuration finale](assets/fr/29.webp)





- Referentni datum**: Datum početka za izračunavanje rokova isporuke
- Minimalno Kašnjenje Dospijeća**: Minimalno kašnjenje nakon transakcije (preporučeno 10 dana)



Kliknite na "Create" da biste potvrdili konfiguraciju.



Konfiguracija Heritage je sada aktivna:



![Configuration active](assets/fr/30.webp)



Prikazuje oba naslednika sa njihovim odgovarajućim rokovima i datumima isteka.



### Čuvanje deskriptora



**Važno**: Sačuvajte vaše wallet deskriptore. Bez njih, čak i sa mnemoničkom frazom, oporavak sredstava je nemoguć.



Kliknite na "Backup Descriptors" :



![Bouton Backup](assets/fr/31.webp)



Sačuvaj JSON datoteku koja sadrži tvoje Bitcoin deskriptore:



![Backup descripteurs](assets/fr/32.webp)



Ovu datoteku treba preneti vašim naslednicima, zajedno sa njihovim odgovarajućim mnemonik frazama.



### Primite bitkoine



Kliknite na "RECEIVE" da biste generate adresu za prijem:



![Recevoir bitcoins](assets/fr/33.webp)



Čestitamo! Vaš Heritage Wallet je spreman za primanje bitkoina. Svaka generisana adresa automatski uključuje vaše Heritage uslove.



Nakon primanja transakcije, vaš saldo je ažuriran:



![Solde mis à jour](assets/fr/34.webp)



Istorija prikazuje transakciju i povezanu Heritage konfiguraciju.



---

## Oporavak naslednika



Kada istekne određeno vreme, naslednik može povratiti sredstva.



### Preduslovi



Naslednik treba :


1. Njegova 12-rečenična mnemonička fraza


2. Originalna rezervna datoteka deskriptora wallet (JSON)



### Kreiranje naslednika Wallet



Na kartici "NASLEDSTVA", iskačući prozor vas podseća na ove preduslove:



![Page Heir Wallets](assets/fr/35.webp)



**Imajte na umu**: Bez rezervne datoteke deskriptora, pristup sredstvima je NEMOGUĆ, čak i sa ispravnom mnemoničkom frazom.



Kliknite na "Create Heir Wallet" :



![Créer Heir Wallet](assets/fr/36.webp)



Molim vas popunite obrazac:



![Formulaire Heir Wallet](assets/fr/37.webp)





- Heir Wallet Name**: Ime za identifikaciju ovog naslednika wallet
- Ključni Provajder** : Lokalno Skladištenje Ključeva
- Vrati**: Odaberite ovu opciju da unesete postojeću frazu



Unesite 12 reči mnemoničke fraze naslednika i konfigurišite Pružatelja Nasleđa:



![Entrée mnemonic](assets/fr/38.webp)





- Heritage Provider**: "Local" da koristite svoj čvor sa rezervnom datotekom



Učitaj JSON rezervnu datoteku i klikni na "Create Heir Wallet" :



![Chargement backup](assets/fr/39.webp)



### Interface Naslednik Wallet



Naslednik Wallet je kreiran. U početku, ako vremenska brava još nije istekla, nasledstvo nije dostupno:



![Pas d'héritage disponible](assets/fr/40.webp)



Kada kašnjenje istekne i sredstva budu sinhronizovana sa Bitcoin mrežom, pojavljuju se na listi nasledstava:



![Héritage disponible](assets/fr/41.webp)



Interfejs prikazuje :




- Tip ključa i otisak prsta
- Ukupna nasledna sredstva
- Trenutni iznos za trošenje (0 sat ako vremenska blokada još nije istekla)
- Datumi dospeća i isteka



Kada datum dospeća stigne, dugme "Spend" prenosi bitkoine na lični wallet.



---

## Najbolje prakse



### Čuvanje deskriptora



wallet opisi su neophodni za rekonstrukciju vaših Heritage adresa. **Bez opisa, čak i sa vašom mnemoničkom frazom, nećete moći pronaći vaša sredstva.



### Ključna sigurnost





- Koristite Ledger za glavni ključ ako je moguće
- Nikada ne čuvajte rečenice naslednika na istom mestu kao svoje sopstvene
- Širite informacije putem više medija i lokacija



### Dokumentacija za vaše voljene



Napišite jasna uputstva koja objašnjavaju svaki korak procesa oporavka. Vaši naslednici možda neće biti upoznati sa Bitcoin u kritičnom trenutku.



## Alternative



Postoje i druga rešenja za upravljanje prenosom vaših bitkoina, uključujući Liana i Bitcoin Keeper. Naše tutorijale ćete pronaći ispod:



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

## Zaključak



Nasleđe vam omogućava da planirate svoju Bitcoin sukcesiju na suveren način putem Desktop aplikacije. Implementacija zahteva promišljeno razmatranje odgovarajućih vremenskih okvira i obezbeđivanje tajni. Ne zaboravite da prenesete svojim naslednicima:




- Njihova fraza od 12 reči
- Datoteka rezervne kopije deskriptora
- Uputstva za oporavak



## Resursi





- [Heritage official website](https://btc-heritage.com)
- [Dokumentacija CLI](https://btc-heritage.com/heritage-cli)
- [GitHub Heritage CLI](https://github.com/crypto7world/heritage-cli)
- [GitHub Heritage Desktop](https://github.com/crypto7world/heritage-gui)