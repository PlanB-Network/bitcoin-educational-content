---
name: BTCPAY SERVER - Umbrel
description: Instaliranje i korišćenje BTCPAY SERVER na Umbrel za prihvatanje Bitcoin i Lightning
---

![cover](assets/cover.webp)



U ekosistemu Bitcoin, prihvatanje plaćanja predstavlja veliki izazov za trgovce i preduzeća. Tradicionalna rešenja, bilo da su bankarska (kreditne kartice, Stripe, PayPal) ili čak Bitcoin (BitPay, Coinbase Commerce), nameću posrednike koji naplaćuju značajne naknade, prikupljaju vaše osetljive poslovne podatke i mogu BLOCK ili cenzurisati vaše transakcije po svojoj volji. Ova zavisnost je u suprotnosti sa osnovnim principima Bitcoin decentralizacije, poverljivosti i finansijskog suvereniteta.



BTCPAY SERVER se pojavljuje kao open-source odgovor na ovaj problem. Ovaj samostalno hostovani procesor plaćanja pretvara vaš sopstveni Bitcoin čvor u profesionalnu infrastrukturu, bez posrednika, bez dodatnih naknada za obradu i bez kompromisa po pitanju privatnosti. Razvijen od strane globalne zajednice saradnika od 2017. godine, BTCPAY SERVER vam omogućava da primate Bitcoin i Lightning uplate direktno u vaše novčanike, zadržavajući punu kontrolu nad vašim sredstvima u svakom trenutku.



Tradicionalno, instalacija BTCPAY SERVER zahteva napredne tehničke veštine: konfiguraciju Linux servera, majstorstvo Dockera, upravljanje SSL sertifikatima i mrežnu sigurnost. Umbrel revolucionira ovaj pristup sa instalacijom na jedan klik direktno integrisanom sa vašim Bitcoin i LIGHTNING NODE. Ovo pojednostavljenje čini ono što je ranije bilo rezervisano za iskusne tehničare dostupnim svima.



**Važno je razumeti**: BTCPAY SERVER na Umbrel-u radi po defaultu samo na vašoj lokalnoj mreži. Možete kreirati fakture, prihvatati Lightning i Bitcoin uplate, i upravljati vašim knjigovodstvom sa bilo kog uređaja povezanog na vašu kućnu mrežu (računar, pametni telefon, tablet). Ova konfiguracija je idealna za naplatu usluga uživo, upravljanje plaćanjima licem u lice, ili korišćenje BTCPAY SERVER sa vaše lokalne mreže. S druge strane, za integraciju BTCPAY SERVER u online prodavnicu koja je javno dostupna na Internetu, biće potrebna dodatna konfiguracija sa javnom izloženošću (ovaj problem ćemo pokriti na kraju tutorijala).



Ovaj vodič vas vodi kroz kompletnu instalaciju BTCPAY SERVER na Umbrel, konfigurisanje vaših Bitcoin Wallet i LIGHTNING NODE, kreiranje i plaćanje faktura, i upravljanje računovodstvenim izveštavanjem. Saznaćete kako da efikasno koristite BTCPAY SERVER na vašoj lokalnoj mreži, a zatim ćemo razgovarati o rešenjima za javni prikaz ako želite da ga integrišete sa e-commerce sajtom.



## Preduslovi



Da biste pratili ovaj vodič, potrebno je da imate ispravno instaliran i konfigurisan Umbrel. Ako to već niste uradili, molimo vas da pogledate naš vodič o instalaciji Umbrela.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Vaš Bitcoin core čvor mora biti potpuno sinhronizovan sa Blockchain (100% u Umbrelovoj Bitcoin aplikaciji). Ova početna sinhronizacija obično traje između 3 dana i 2 nedelje, u zavisnosti od vašeg hardvera i Internet konekcije.



Da biste prihvatili trenutna Lightning plaćanja, takođe ćete morati instalirati LND (Lightning Network Daemon) na Umbrel. Pogledajte naš vodič o instaliranju i konfigurisanju LND na Umbrel ako želite omogućiti ovu funkciju.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Dozvolite najmanje 50 GB slobodnog prostora na disku za BTCPAY SERVER, njegove baze podataka i Lightning podatke. Stabilna internet konekcija putem Ethernet kabla se snažno preporučuje kako bi se izbegli prekidi veze.



## Instaliranje BTCPAY SERVER na Umbrel



Sa Umbrel Interface (`umbrel.local`), idi na App Store i potraži "BTCPAY SERVER" u kategoriji Bitcoin.



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



Kliknite Instaliraj. Umbrel automatski proverava da li su Bitcoin core i LND instalirani, zatim započinje implementaciju (2-5 minuta).



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



Kada instalirate, otvorite aplikaciju. Moraćete da kreirate administratorski nalog sa jakim akreditivima.



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



Kada vaš nalog bude kreiran, BTCPAY SERVER će vas odmah pozvati da postavite vašu prvu prodavnicu. Izaberite profesionalno ime i odaberite referentnu valutu (EUR, USD ili BTC).



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## Pristupite BTCPAY SERVER na vašoj lokalnoj mreži



BTCPAY SERVER je dostupan sa bilo kog uređaja na vašoj lokalnoj mreži (WiFi ili Ethernet). Pristupite iz vašeg pregledača na :



```url
http://umbrel.local
```



Ili direktno na :



```url
http://umbrel.local:3003
```



**Remote access with Tailscale**: Da biste pristupili BTCPAY SERVER sa bilo kog mesta na svetu, koristite Tailscale. Ovaj sigurni VPN vam omogućava da se povežete na vaš Umbrel kao da ste na vašoj lokalnoj mreži. Pogledajte naš vodič posvećen Tailscale-u na Umbrel-u.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Konfigurisanje vašeg Bitcoin portfolija



Da biste prihvatili uplate, potrebno je da konfigurišete Bitcoin Wallet. BTCPAY SERVER prikazuje opcije konfiguracije na kontrolnoj tabli.



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



Da biste konfigurisali Wallet Bitcoin, idite na "Wallets" > "Bitcoin".



Imate dve opcije: kreirati novi portfolio direktno u BTCPay, ili uvesti postojeći portfolio. Za uvoz, dostupno je nekoliko metoda:




- Povežite Hardware Wallet** (preporučeno): Uvezite svoje javne ključeve putem aplikacije Vault
- Uvezi Wallet datoteku** (preporučeno): Otpremi izvezenu datoteku iz svog portfolija
- Unesite prošireni javni ključ**: Ručno unesite svoj XPub/YPub/ZPub
- Skeniraj Wallet QR kod** : Skeniraj QR kod iz BlueWallet, Cobo Vault, Passport ili Specter DIY
- Unesite Wallet seed** (nije preporučeno) : Unesite svoju frazu za oporavak od 12 ili 24 reči



![Options de création de portefeuille](assets/fr/06.webp)



Za ovaj vodič, kreiraćemo novi Hot Wallet: privatni ključ će stoga biti sačuvan na našem Umbrel serveru. U ovom slučaju, snažno vam savetujemo da redovno premeštate sredstva na Cold Wallet kako biste izbegli čuvanje velikih iznosa na serveru.



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



Jednom kada je konfigurisan, BTCPAY SERVER potvrđuje da je vaš Wallet spreman da prihvati On-Chain uplate.



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Aktiviraj Lightning Network



Da biste prihvatili trenutna Lightning plaćanja, idite na Novčanici > Lightning. Zatim, pošto je vaš LND čvor već postavljen na Umbrel, jednostavno kliknite na dugme "Save" da biste potvrdili vezu između vašeg BTCPAY SERVER i vašeg LIGHTNING NODE.



![Configuration du nœud Lightning](assets/fr/09.webp)



## Kreiraj i plati fakture



U Interface BTCPAY SERVER, idite na Fakture > Kreiraj Invoice. Unesite iznos, dodajte opcionalni opis i kliknite Kreiraj.



![Création d'une nouvelle facture](assets/fr/10.webp)



Zatim možete kliknuti na dugme "Checkout" da prikažete Invoice. BTCPay zatim generiše Invoice sa jedinstvenim QR kodom (BIP21) koji sadrži Bitcoin Address i Lightning Invoice.



![Détails de la facture générée](assets/fr/11.webp)



Vaš kupac može skenirati QR kod sa bilo kojim kompatibilnim Wallet.



![Page de paiement avec QR code](assets/fr/12.webp)



Jednom plaćen, Invoice postaje "Settled" za nekoliko sekundi za Lightning.



![Confirmation de paiement réussi](assets/fr/13.webp)



## Upravljanje i praćenje plaćanja



U odeljku "Izveštavanje", kartica "Fakture", pronaći ćete kompletnu istoriju vaših faktura, sa datumom, iznosom, statusom i metodom plaćanja. Možete je izvesti ako je potrebno.



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## Konfiguracija prodavnice



BTCPAY SERVER vam omogućava upravljanje više prodavnica sa različitim parametrima. Svaka prodavnica predstavlja poseban poslovni entitet: e-commerce prodavnicu, fizičku prodajnu tačku ili naplatu usluga.



U postavkama prodavnice, pronaći ćete nekoliko važnih sekcija:



![Paramètres du magasin](assets/fr/15.webp)





- Opšta podešavanja**: Naziv prodavnice, referentna valuta (BTC, EUR, USD), vreme isteka Invoice (podrazumevano 15 minuta), broj potrebnih potvrda za Blockchain
- Stope**: Konfiguracija izvora stopa Exchange i konverzije fiat/Bitcoin
- Izgled naplate**: Prilagodite izgled vaših stranica za naplatu (logo, boje, personalizovane poruke)
- Postavke E-pošte**: Konfiguracija obaveštenja e-poštom za primljene uplate
- Pristupni Tokeni**: API token upravljanje za e-commerce integracije (WooCommerce, Shopify, itd.)
- Korisnici**: Upravljajte pristupom korisnika prodavnici sa različitim nivoima dozvola (Vlasnik, Gost)
- Webhooks**: Konfiguracija webhook-a za sinhronizaciju u realnom vremenu sa vašim računovodstvenim ili ERP sistemom



BTCPAY SERVER takođe nudi odeljak Plugins za proširenje funkcionalnosti sa integracijama za e-trgovinu, sistemima prodajnih mesta i dodatnim alatima.



![Gestion des plugins](assets/fr/16.webp)



## Prednosti i ograničenja lokalne upotrebe



**Prednosti BTCPAY SERVER na Umbrel** :




- Totalni suverenitet: ekskluzivna kontrola privatnih ključeva i sredstava, nijedna treća strana ne može zamrznuti ili cenzurisati vaše uplate
- Značajne uštede: samo Bitcoin mrežni troškovi (nekoliko centi na Lightning-u) naspram 2-3% na tradicionalnim procesorima
- Maksimalna poverljivost: bez registracije, verifikacije identiteta ili deljenja podataka sa trećim kompanijama
- Arhitektura otvorenog koda garantuje transparentnost, mogućnost revizije i održivost putem velike zajednice programera.
- Laka instalacija putem Umbrela, bez potrebe za naprednim tehničkim veštinama



**Važna ograničenja** :




- Lokalna mreža samo**: BTCPAY SERVER na Umbrel je dostupan samo sa vaše kućne mreže. Savršeno za naplatu licem u lice, freelance usluge ili male fizičke biznise, ali nepogodno za online prodavnice koje su javno dostupne na Internetu.
- Puna tehnička odgovornost: održavanje čvora, redovni bekapi, praćenje povezivosti
- Upravljanje likvidnošću na Lightning mreži: otvaranje i upravljanje kanalima sa dovoljnim dolaznim kapacitetom
- Podrška ograničena na dokumentaciju zajednice i forume, što zahteva više autonomije nego komercijalni odeljak za korisničku podršku



Ovo LAN ograničenje je glavna prepreka za integraciju BTCPAY SERVER u e-commerce prodavnicu, gde kupci moraju imati mogućnost pristupa stranicama za plaćanje sa bilo kog mesta na Internetu.



## Najbolje prakse i bezbednost



Aktivirajte automatske Umbrel rezervne kopije i sačuvajte kopiju na eksternim medijima (USB stik, Hard disk, enkriptovani oblak). Čuvajte vaše Bitcoin seedove (fraze za oporavak) na sigurnom, fizički odvojenom mestu. Sačuvajte LND channel.backup fajl za Lightning oporavak.



Redovno pratite sinhronizaciju Bitcoin core, Lightning kanale i odgovor BTCPAY SERVER. Jednostavan nedeljni test: generate i platite račun za nekoliko satoshija. Održavajte Umbrel ažurnim (bezbednosne zakrpe, poboljšanja). Napravite rezervnu kopiju pre većih ažuriranja. Za profesionalnu upotrebu, razmislite o eksternom nadzoru (UptimeRobot) sa obaveštenjima putem e-pošte/SMS-a.



## Prikaži BTCPAY SERVER javno za online prodavnicu



Da biste integrisali BTCPAY SERVER u veb-baziranu e-commerce prodavnicu (WooCommerce, Shopify, itd.), vaši kupci treba da mogu pristupiti stranicama za plaćanje sa bilo kog mesta, a ne samo sa vaše lokalne mreže.



**Rešenje: Nginx Proxy Manager**



Možete izložiti BTCPAY SERVER javno koristeći Nginx Proxy Manager (dostupan u Umbrel App Store-u). Ovo rešenje zahteva :




- Ime domena (klasično ili besplatno putem DuckDNS, No-IP, Afraid.org)
- Konfigurisanje prosleđivanja portova (portovi 80 i 443) na vašem ruteru
- Instalacija Nginx Proxy Manager-a, koji automatski upravlja SSL sertifikatima



Ova konfiguracija izlaže vaš server internetu i zahteva dodatnu pažnju (jake lozinke, 2FA, redovna ažuriranja). Pripremićemo poseban vodič koji detaljno opisuje ovu kompletnu proceduru.



## Zaključak



BTCPAY SERVER na Umbrel kombinuje snagu Bitcoin čvora sa jednostavnošću Umbrela kako bi stvorio samostalno hostovanu profesionalnu platnu infrastrukturu dostupnu svima. Ovaj finansijski suverenitet dolazi sa odgovornošću za održavanje, ali Umbrel uveliko pojednostavljuje operativni teret u poređenju sa prednostima: eliminacija naknada za obradu, zaštita vaše privatnosti, otpornost na cenzuru i potpuna kontrola nad vašim sredstvima.



Lokalna mreža već pokriva širok spektar primena: naplata za freelance usluge, plaćanja licem u lice, male fizičke prodavnice, ili jednostavno učenje i eksperimentisanje sa Bitcoin i Lightning u kontrolisanom okruženju. Za potrebe e-trgovine koje zahtevaju javnu izloženost, postoji rešenje Nginx Proxy Manager, ali zahteva dodatnu tehničku konfiguraciju, koju ćemo detaljno objasniti u posebnom vodiču.



Bilo da vodite posao, početni projekat ili jednostavno eksperimentišete, BTCPAY SERVER na Umbrel-u nudi potpunu finansijsku autonomiju. Put počinje sa prvom prodavnicom, prvim Invoice, prvim plaćanjem primljenim direktno u vašu suverenu infrastrukturu.



## Resursi



### Službena dokumentacija




- [BTCPAY SERVER official website](https://btcpayserver.org)
- [Kompletna BTCPAY SERVER dokumentacija](https://docs.btcpayserver.org)
- [GitHub BTCPAY SERVER](https://github.com/btcpayserver/btcpayserver)
- [Tailscale dokumentacija](https://tailscale.com/kb)


### Zajednica i podrška




- [Forum BTCPAY SERVER](https://chat.btcpayserver.org)
- [Forum Umbrel](https://community.getumbrel.com)
- [Reddit r/BTCPayServer](https://reddit.com/r/BTCPayServer)