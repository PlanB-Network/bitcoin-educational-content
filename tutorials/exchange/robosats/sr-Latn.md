---
name: Robosats

description: Kako koristiti Robosats
---

![cover](assets/cover.webp)


RoboSats (https://learn.robosats.com/) je jednostavan način za privatno Exchange Bitcoin za nacionalne valute. Pojednostavljuje peer-to-peer iskustvo i koristi lightning hold fakture kako bi se minimizovali zahtevi za skrbništvom i poverenjem.


![video](https://youtu.be/XW_wzRz_BDI)


## Vodič


**Napomena:** Ovaj vodič je sa Bitocin Q&A (https://bitcoiner.guide/robosats/). Sve zasluge idu njemu, možete ga podržati [ovde](https://bitcoiner.guide/contribute); BitcoinQ&A je takođe Bitcoin mentor. Kontaktirajte ga za mentorstvo!


![image](assets/0.webp)


RoboSats - Jednostavan i privatan Lightning zasnovan P2P Exchange


## Pre nego što počnete


### Stvari koje treba da znate


| Jargon       | Definition                                                                                                                                                                                     |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Robot        | Your automatically generated private trade identity. Do not re-use the same robot more than once as this can degrade your privacy.                                                             |
| Token        | A string of random characters used to generate your unique robot.                                                                                                                              |
| Maker        | A user who creates an offer to buy or sell Bitcoin.                                                                                                                                            |
| Taker        | A user who takes another user up on their offer to buy or sell Bitcoin.                                                                                                                        |
| Bond         | An amount of Bitcoin locked up by both peers as a pledge to play fair and complete their part of the trade. Bonds are typically 3% of the total trade amount and are powered by Hodl Invoices. |
| Trade Escrow | Used by the seller as a method of holding the trade amount of Bitcoin, again using Hodl Invoices.                                                                                              |
| Fees         | RoboSats charges 0.2% of the trade amount, which is split between both maker and taker. The taker pays 0.175% and the maker pays 0.025%.                                                       |

## Stvari koje treba da imate


### A Lightning Wallet


RoboSats je Lightning native, tako da će vam trebati Lightning Wallet da finansirate obveznicu i primite kupljeni Sats kao kupac. Trebalo bi da budete pažljivi pri odabiru vašeg Wallet, zbog tehnologije koja se koristi za funkcionisanje RoboSats-a, nisu svi kompatibilni.


Ako ste pokretač čvora, Zeus je daleko najbolja opcija. Ako nemate svoj čvor, toplo bih preporučio Phoenix, mobilni Wallet na više platformi sa jednostavnim podešavanjem i pristupom Lightning-u. Phoenix je korišćen u izradi ovog vodiča.


### Neki Bitcoin


Kupci i prodavci moraju da obezbede obveznicu pre nego što bilo kakva trgovina može da se obavi. Ovo je obično veoma mali iznos (~3% od iznosa trgovine), ali je ipak preduslov.


Koristeći RoboSats za kupovinu svog prvog Sats? Zašto ne biste zamolili prijatelja da vam pozajmi malu sumu potrebnu za početak!? Ako ste sami, evo nekoliko drugih sjajnih opcija da nabavite noKYC Sats za početak.


### Pristup RoboSats


Očigledno je da ćeš morati pristupiti RoboSats! Postoje četiri glavna načina na koja to možeš učiniti:


1. Preko Tor Browser-a (Preporučeno!)

2. Putem običnog web-pregledača (Nije preporučeno!)

3. Preko Android APK

4. Vaš sopstveni klijent


Ako ste novi u Tor pretraživaču, saznajte više i preuzmite ga [ovde](https://www.torproject.org/download/).


Brza napomena za iOS korisnike koji žele pristupiti RoboSats putem Tor-a sa svojih telefona. 'Onion Browser' nije Tor Browser. Umesto toga koristite Orbot + Safari i Orbot + DuckDuckGo.


## Kupovina Bitcoin


Sledeći koraci su sprovedeni u maju 2023. koristeći verziju 0.5.0, pristupano putem Tor pretraživača. Koraci bi trebali biti identični za korisnike koji pristupaju RoboSats putem Android APK-a.


U vreme pisanja, RoboSats je još uvek u fazi aktivnog razvoja, tako da se Interface može malo promeniti u budućnosti, ali osnovni koraci potrebni za završetak trgovine bi trebalo da ostanu uglavnom nepromenjeni.


**Napomena:** kada prvi put učitate RoboSats, dočekaće vas ova početna stranica. Kliknite na Start.


![image](assets/2.webp)


generate vaš token i sačuvajte ga na sigurnom mestu kao što je aplikacija za šifrovane beleške ili menadžer lozinki. Ovaj token se može koristiti za povratak vašeg privremenog ID-a robota u slučaju da se vaš pregledač ili aplikacija zatvori na pola puta kroz trgovinu.


![image](assets/3.webp)


Upoznajte svoj novi robotski identitet, a zatim kliknite Nastavi.


![image](assets/4.webp)


Kliknite na Ponude da pregledate knjigu narudžbi. Na vrhu stranice možete filtrirati prema vašim preferencijama. Obavezno obratite pažnju na procente obveznica i premiju preko prosečne Exchange stope.



- Izaberite oznaku 'Kupi'
- Izaberite svoju valutu
- Izaberite svoj(e) način(e) plaćanja


![image](assets/5.webp)


**Napomena:** kliknite na ponudu koju želite da prihvatite. Unesite iznos (u izabranoj fiat valuti) koji želite da kupite od prodavca, zatim konačno proverite detalje i kliknite na 'Prihvati narudžbinu'.


Ako prodavac nije online (označeno crvenom tačkom na njihovoj profilnoj slici), videćete upozorenje da trgovina može potrajati duže nego obično. Ako nastavite i prodavac ne nastavi na vreme, bićete obeštećeni sa 50% iznosa njihove garancije za vaše izgubljeno vreme.


![image](assets/6.webp)


Dalje, treba da zaključate svoju trgovinsku obavezu plaćanjem Invoice na ekranu. Ovo je zadržavanje Invoice koje zamrzava vaš Wallet. Biće naplaćeno samo ako ne uspete da ispunite svoju stranu trgovine.


![image](assets/7.webp)


U vašem Lightning Wallet, skenirajte QR kod i platite Invoice.


![image](assets/8.webp)


Dalje, u vaš Lightning Wallet generate i Invoice za prikazani iznos i zalepite u predviđeni prostor.


![image](assets/9.webp)


Sačekajte da prodavac zaključa iznos trgovine. Kada se to dogodi, RoboSats će automatski preći na sledeći korak gde će se otvoriti prozor za ćaskanje. Recite Zdravo i zatražite od prodavca informacije o plaćanju u fiat valuti. Kada ih dobijete, pošaljite uplatu putem izabranog metoda, a zatim to potvrdite u RoboSats. Sva komunikacija u RoboSats je PGP šifrovana, što znači da samo vi i vaš trgovinski partner možete čitati poruke.


![image](assets/10.webp)


Jednom kada prodavac potvrdi prijem uplate, RoboSats automatski oslobađa uplatu koristeći ranije obezbeđeni Invoice.


![image](assets/11.webp)


Kada je Invoice plaćen, trgovina je završena i vaša obveznica je otključana. Tada ćete videti rezime trgovine.


![image](assets/12.webp)


Proverite vaš Lightning Wallet za potvrdu da je Sats stigao.


![image](assets/13.webp)


## Dodatne funkcije


Pored očigledne kupovine i prodaje Bitcoin, RoboSats ima još nekoliko funkcija koje biste trebali znati.

Robot Garaža


Želite da imate više trgovina istovremeno, ali ne želite da delite isti identitet među njima? Nema problema! Kliknite na karticu Robot, generate dodatni Robot i kreirajte ili preuzmite vašu sledeću narudžbinu.


![image](assets/14.webp)


### Kreiranje Narudžbi


Pored prihvatanja tuđe ponude, možete kreirati svoju i čekati da vam dođe drugi Robot.



- Otvorite stranicu Kreiraj.
- Definišite da li je vaša narudžbina za kupovinu ili prodaju Bitcoin.
- Unesite iznos i valutu sa kojom želite da kupite/prodate.
- Unesite način(e) plaćanja koji ste spremni da koristite.
- Unesite % 'Premije preko tržišta' koju ste spremni prihvatiti. Imajte na umu da ovo može biti negativna cifra kako biste ponudili po nižoj ceni u odnosu na trenutnu tržišnu cenu.
- Kliknite Kreiraj Porudžbinu.
- Platite Lightning Invoice da zaključate svoj Maker Bond.
- Vaša narudžba je sada aktivna. Opustite se i sačekajte da je neko prihvati.


![image](assets/15.webp)


### On-Chain Isplate


RoboSats je fokusiran na Lightning, ali kupci imaju opciju da prime svoj Sats na On-Chain Bitcoin Address. Kupci mogu izabrati ovu opciju nakon zaključavanja svog depozita. Nakon odabira On-Chain, kupac će videti pregled naknada. Dodatne naknade za ovu uslugu uključuju:



- Naknada za zamenu koju prikuplja RoboSats - Ova naknada je dinamična i menja se u zavisnosti od toga koliko je Bitcoin mreža zauzeta.
- Naknada Mining za transakciju isplate - Ovo je podesivo od strane kupca.


![image](assets/16.webp)


### P2P Zamene


RoboSats omogućava korisnicima da zamene Sats u ili iz svog Lightning Wallet. Jednostavno kliknite na dugme za zamenu na vrhu stranice sa ponudama da biste videli trenutne ponude za zamenu.


Kao kupac ponude 'Swap In', šaljete On-Chain Bitcoin partneru i dobijate nazad Sats, umanjeno za oglašene naknade i/ili premije, na vaš Lightning Wallet. Kao kupac ponude 'Swap Out', šaljete Sats putem Lightning-a i dobijate Bitcoin, umanjeno za bilo koje naknade i/ili premije, na vaš On-Chain Address. Korisnici Samourai ili Sparrow Wallet takođe mogu koristiti Stowaway funkciju za završetak zamene.


Ponude za zamenu na RoboSats takođe mogu uključivati alternativne opcije vezane za Bitcoin, kao što su RBTC, LBTC i WBTC. Trebalo bi da budete izuzetno oprezni prilikom interakcije sa ovim tokenima jer svi dolaze sa različitim kompromisima. Vezani Bitcoin nije Bitcoin!


![image](assets/17.webp)


### Pokrenite sopstveni RoboSats klijent


Umbrel, Citadel i Start9 node operateri mogu instalirati svoj RoboSats klijent direktno na svoj čvor. Prednosti ovoga su navedene kao:



- Dramatično brže vreme učitavanja.
- Bezbednije: vi kontrolišete koju RoboSats klijent aplikaciju koristite.
- Pristupite RoboSats bezbedno sa bilo kog pregledača / uređaja. Nema potrebe koristiti TOR ako ste na lokalnoj mreži ili koristite VPN: vaš čvor backend obrađuje torifikaciju potrebnu za anonimizaciju.
- Omogućava kontrolu nad time na koji P2P tržišni koordinator se povezujete (podrazumevano je robosats6tkf3eva7x2voqso3a5wcorsnw34jveyxfqi2fu7oyheasid.onion)


![image](assets/18.webp)


## ČPP


### Mogu li biti prevaren?


Kao kupac, ako ste poslali fiat potreban za vašu stranu trgovine, ali prodavac ne uspe da vam oslobodi Sats, možete otvoriti spor. Ako tokom ovog procesa spora možete dokazati RoboSats arbitrima da ste poslali fiat, sredstva prodavca u escrow-u i njihov trgovinski depozit će biti oslobođeni vama.

Kako da otkažem trgovinu?


Trgovinu možete otkazati nakon postavljanja obveznice klikom na dugme za kolaborativno otkazivanje unutar menija za trgovinu. Ako vaš trgovinski partner pristane na otkazivanje, nećete imati nikakve troškove. Ali ako vaš trgovinski partner želi da završi trgovinu, a vi ipak odlučite da otkažete, izgubićete svoju trgovinsku obveznicu.


### Da li RoboSats radi sa ‘X’ metodom plaćanja?


U RoboSats-u nema ograničenja na metode plaćanja. Ako ne vidite ponude u željenoj metodi, kreirajte svoju ponudu koristeći je!


![image](assets/19.webp)


### Šta RoboSats saznaje o meni kada ga koristim?


Pod uslovom da koristite RoboSats putem Tor-a ili Android aplikacije, ništa uopšte! Saznajte više ovde.



- Tor štiti vašu mrežnu privatnost.
- PGP enkripcija čuva vašu trgovinsku prepisku privatnom.
- Bez naloga znači jedan robot po trgovini. To znači da RoboSats ne može povezati više trgovina s jednim entitetom.


Međutim, postoje neka ograničenja! Lightning je prilično privatan kao pošiljalac, ali ne i kao primalac. Ako primate na svoj Lightning čvor, vaš ID čvora se deli u vašim fakturama. Ovaj ID čvora daje svakome ko ga zna početnu tačku za pokušaj povezivanja vaše On-Chain aktivnosti. Ovo je takođe tačno ako korisnik odluči da primi svoju trgovinu putem On-Chain isplate.


Da bi se to ublažilo, korisnici mogu izabrati da koriste rešenje kao što je Proxy Wallet za Lightning ili CoinJoin za On-Chain.


### Federacija


Trenutno postoji jedan RoboSats koordinator kojim upravlja tim programera RoboSats-a. U Bitcoin, bilo koji oblik centralizacije predstavlja lakšu metu za vlade ili regulatore koji možda ne gledaju blagonaklono na određenu uslugu.


Pošto je RoboSats Open Source projekat, bilo ko može uzeti kod i pokrenuti sopstvenog koordinatora. Iako ovo donekle decentralizuje rizik od jednog cilja, takođe fragmentira već tanko tržište likvidnosti.


RoboSats tim to shvata i počeo je rad na federativnom modelu. Kao krajnji korisnik, ovo ne bi trebalo mnogo da promeni tok trgovine prikazan gore, ali će postojati dodatni prikazi ili ekrani za dodavanje ili uklanjanje različitih koordinatora koji se pojave.


KRAJ vodiča

https://bitcoiner.guide/robosats/