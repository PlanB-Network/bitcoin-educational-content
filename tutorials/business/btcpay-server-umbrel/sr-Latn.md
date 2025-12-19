---
name: BTCPay Server - Umbrel
description: Instaliranje i korišćenje BTCPay Server-a na Umbrel-u za prihvatanje Bitcoin i Lightning
---

![cover](assets/cover.webp)



U ekosistemu Bitcoin, prihvatanje plaćanja predstavlja veliki izazov za trgovce i preduzeća. Tradicionalna rešenja, bilo da su bankarska (kreditne kartice, Stripe, PayPal) ili čak Bitcoin (BitPay, Coinbase Commerce), nameću posrednike koji naplaćuju značajne naknade, prikupljaju vaše osetljive poslovne podatke i mogu blokirati ili cenzurisati vaše transakcije po svojoj volji. Ova zavisnost je u suprotnosti sa osnovnim principima Bitcoin o decentralizaciji, poverljivosti i finansijskoj suverenosti.



BTCPay Server se pojavljuje kao open-source odgovor na ovaj problem. Ovaj samostalno hostovani procesor plaćanja pretvara vaš sopstveni Bitcoin čvor u profesionalnu infrastrukturu, bez posrednika, bez dodatnih naknada za obradu i bez kompromisa po pitanju privatnosti. Razvijan od strane globalne zajednice saradnika od 2017. godine, BTCPay Server vam omogućava da primate Bitcoin i Lightning uplate direktno u vaše novčanike, zadržavajući punu kontrolu nad vašim sredstvima u svakom trenutku.



Tradicionalno, instalacija BTCPay Server-a zahteva napredne tehničke veštine: konfiguraciju Linux servera, majstorstvo Docker-a, upravljanje SSL sertifikatima i mrežnu sigurnost. Umbrel revolucionira ovaj pristup sa instalacijom na jedan klik direktno integrisanom sa vašim Bitcoin i Lightning čvorom. Ovo pojednostavljenje čini ono što je ranije bilo rezervisano za iskusne tehničare dostupnim svima.



**Važno je razumeti**: BTCPay Server na Umbrel-u radi po default-u samo na vašoj lokalnoj mreži. Možete kreirati fakture, prihvatati Lightning i Bitcoin uplate, i upravljati vašim knjigovodstvom sa bilo kog uređaja povezanog na vašu kućnu mrežu (računar, pametni telefon, tablet). Ova konfiguracija je idealna za naplatu usluga uživo, upravljanje plaćanjima licem u lice, ili korišćenje BTCPay Server-a sa vaše lokalne mreže. S druge strane, za integraciju BTCPay Server-a u online prodavnicu koja je javno dostupna na Internetu, biće potrebna dodatna konfiguracija sa javnom izloženošću (ovaj problem ćemo pokriti na kraju tutorijala).



Ovaj vodič vas vodi kroz kompletnu instalaciju BTCPay Server-a na Umbrel, konfigurisanje vašeg Bitcoin wallet i Lightning čvora, kreiranje i plaćanje faktura, i upravljanje računovodstvenim izveštavanjem. Otkrićete kako efikasno koristiti BTCPay Server na vašoj lokalnoj mreži, a zatim ćemo pogledati rešenja za javni prikaz ako želite da ga integrišete sa e-commerce sajtom.



## Preduslovi



Da biste pratili ovaj vodič, potrebno je da imate ispravno instaliran i konfigurisan Umbrel. Ako to već niste uradili, molimo vas da pogledate naš vodič o instalaciji Umbrela.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Vaš Bitcoin Core čvor mora biti potpuno sinhronizovan sa blokčejnom (100% u Umbrel-ovoj Bitcoin aplikaciji). Ova početna sinhronizacija obično traje između 3 dana i 2 nedelje, u zavisnosti od vašeg hardvera i internet konekcije.



Da biste prihvatili trenutna Lightning plaćanja, takođe ćete morati instalirati LND (Lightning Network Daemon) na Umbrel. Pogledajte naš vodič o instalaciji i konfigurisanju LND na Umbrel ako želite omogućiti ovu funkciju.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Dozvolite najmanje 50 GB slobodnog prostora na disku za BTCPay Server, njegove baze podataka i Lightning podatke. Stabilna internet konekcija putem Ethernet kabla se snažno preporučuje kako bi se izbegli prekidi.



## Instaliranje BTCPay Servera na Umbrel



Sa Umbrel interfejsa (`umbrel.local`), pristupite App Store-u i potražite "BTCPay Server" u kategoriji Bitcoin.



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



Kliknite Instaliraj. Umbrel automatski proverava da li su Bitcoin Core i LND instalirani, zatim započinje implementaciju (2-5 minuta).



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



Kada instalirate, otvorite aplikaciju. Biće potrebno da kreirate administratorski nalog sa jakim akreditivima.



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



Kada vaš nalog bude kreiran, BTCPay Server će vas odmah pozvati da postavite vašu prvu prodavnicu. Izaberite naziv firme i odaberite referentnu valutu (EUR, USD ili BTC).



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## Pristupite BTCPay Serveru na vašoj lokalnoj mreži



BTCPay Server je dostupan sa bilo kog uređaja na vašoj lokalnoj mreži (WiFi ili Ethernet). Pristupite iz vašeg pregledača na :



```url
http://umbrel.local
```



Ili direktno na :



```url
http://umbrel.local:3003
```



**Remote access with Tailscale**: Da biste pristupili BTCPay Server-u sa bilo kog mesta na svetu, koristite Tailscale. Ovaj sigurni VPN vam omogućava da se povežete na vaš Umbrel kao da ste na vašoj lokalnoj mreži. Pogledajte naš vodič posvećen Tailscale-u na Umbrel-u.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Konfigurisanje vašeg Bitcoin portfolija



Da biste prihvatili uplate, potrebno je da konfigurišete Bitcoin wallet. BTCPay Server prikazuje opcije konfiguracije na kontrolnoj tabli.



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



Da biste konfigurisali wallet Bitcoin, idite na "Wallets" > "Bitcoin".



Imate dve opcije: kreirati novi portfolio direktno u BTCPay, ili uvesti postojeći portfolio. Za uvoz, dostupno je nekoliko metoda:




- Povežite hardver wallet** (preporučeno): Uvezite svoje javne ključeve putem aplikacije Vault
- Uvezi wallet datoteku** (preporučeno): Otpremite izvezenu datoteku iz vašeg portfolija
- Unesite prošireni javni ključ**: Ručno unesite svoj XPub/YPub/ZPub
- Skeniraj wallet QR kod** : Skeniraj QR kod iz BlueWallet, Cobo Vault, Passport ili Specter DIY
- Unesite wallet seed** (nije preporučeno) : Unesite svoju frazu za oporavak od 12 ili 24 reči



![Options de création de portefeuille](assets/fr/06.webp)



Za ovaj vodič, kreiraćemo novi Hot wallet: privatni ključ će stoga biti sačuvan na našem Umbrel serveru. U ovom slučaju, snažno vam savetujemo da redovno prebacujete sredstva na hladni wallet kako biste izbegli skladištenje velikih iznosa na serveru.



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



Jednom kada se konfiguriše, BTCPay Server potvrđuje da je vaš wallet spreman da prihvati on-chain uplate.



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Aktiviraj Lightning Network



Da biste prihvatili trenutna Lightning plaćanja, idite na Novčanici > Lightning. Zatim, pošto je vaš LND čvor već postavljen na Umbrel, jednostavno kliknite na dugme "Save" da biste potvrdili vezu između vašeg BTCPay Servera i vašeg Lightning čvora.



![Configuration du nœud Lightning](assets/fr/09.webp)



## Kreiraj i plati fakture



U interfejsu BTCPay Server, idite na Fakture > Kreiraj Invoice. Unesite iznos, dodajte opcionalni opis i kliknite Kreiraj.



![Création d'une nouvelle facture](assets/fr/10.webp)



Zatim možete kliknuti na dugme "Checkout" da prikažete fakturu. BTCPay zatim generiše fakturu sa jedinstvenim QR kodom (BIP21) koji sadrži Bitcoin adresu i Lightning fakturu.



![Détails de la facture générée](assets/fr/11.webp)



Vaš kupac može skenirati QR kod sa bilo kojim kompatibilnim wallet.



![Page de paiement avec QR code](assets/fr/12.webp)



Jednom plaćen, račun postaje "Settled" za nekoliko sekundi za Lightning.



![Confirmation de paiement réussi](assets/fr/13.webp)



## Upravljanje i praćenje plaćanja



U odeljku "Izveštavanje", na kartici "Fakture", pronaći ćete kompletnu istoriju vaših faktura sa datumom, iznosom, statusom i metodom plaćanja. Možete je izvesti ako je potrebno.



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## Konfiguracija prodavnice



BTCPay Server vam omogućava upravljanje više prodavnica sa različitim parametrima. Svaka prodavnica predstavlja poseban poslovni entitet: e-trgovinsku prodavnicu, fizičku prodajnu tačku ili naplatu usluga.



U postavkama prodavnice, pronaći ćete nekoliko važnih odeljaka:



![Paramètres du magasin](assets/fr/15.webp)





- Opšta podešavanja**: Naziv prodavnice, referentna valuta (BTC, EUR, USD), vreme isteka fakture (podrazumevano 15 minuta), broj potrebnih potvrda na blokčejnu
- Stope**: Konfiguracija izvora deviznih kurseva i konverzija fiat/Bitcoin
- Izgled naplate**: Prilagodite izgled vaših stranica za naplatu (logo, boje, personalizovane poruke)
- Postavke e-pošte**: Konfiguracija obaveštenja e-poštom za primljene uplate
- Access Tokens**: Upravljanje API tokenima za e-commerce integracije (WooCommerce, Shopify, itd.)
- Korisnici**: Upravljajte pristupom korisnika prodavnici sa različitim nivoima dozvola (Vlasnik, Gost)
- Webhooks**: Konfiguracija webhook-a za sinhronizaciju u realnom vremenu sa vašim računovodstvenim ili ERP sistemom



BTCPay Server takođe nudi odeljak za dodatke kako bi proširio funkcionalnost sa e-commerce integracijama, sistemima prodajnih mesta i dodatnim alatima.



![Gestion des plugins](assets/fr/16.webp)



## Prednosti i ograničenja lokalne upotrebe



**Prednosti BTCPay Servera u odnosu na Umbrel** :




- Totalni suverenitet: ekskluzivna kontrola privatnih ključeva i sredstava, nijedna treća strana ne može zamrznuti ili cenzurisati vaše uplate
- Značajne uštede: samo Bitcoin mrežni troškovi (nekoliko centi na Lightningu) naspram 2-3% na tradicionalnim procesorima
- Maksimalna poverljivost: bez registracije, verifikacije identiteta ili deljenja podataka sa trećim kompanijama
- Arhitektura otvorenog koda garantuje transparentnost, mogućnost revizije i održivost putem velike zajednice programera.
- Laka instalacija putem Umbrela, bez potrebe za naprednim tehničkim veštinama



**Važna ograničenja** :




- Lokalna mreža samo**: BTCPay Server na Umbrel-u je dostupan samo sa vaše kućne mreže. Savršen za naplatu licem u lice, freelance usluge ili male fizičke biznise, ali nepogodan za javno dostupne online prodavnice.
- Puna tehnička odgovornost: održavanje čvora, redovni bekapi, praćenje povezivosti
- Upravljanje likvidnošću na Lightning mreži: otvaranje i upravljanje kanalima sa dovoljnim dolaznim kapacitetom
- Podrška je ograničena na dokumentaciju zajednice i forume, što zahteva više autonomije nego komercijalni odeljak za korisničku podršku.



Ovo ograničenje lokalne mreže je glavna prepreka za integraciju BTCPay Servera u e-commerce prodavnicu, gde kupci moraju biti u mogućnosti da pristupe stranicama za plaćanje sa bilo kog mesta na Internetu.



## Najbolje prakse i bezbednost



Aktivirajte automatske Umbrel rezervne kopije i sačuvajte kopiju na eksternim medijima (USB stik, tvrdi disk, enkriptovani oblak). Čuvajte vaše Bitcoin seedove (fraze za oporavak) na sigurnom, fizički odvojenom mestu. Napravite rezervnu kopiju LND channel.backup fajla za oporavak Lightning-a.



Redovno pratite sinhronizaciju Bitcoin Core, Lightning kanala i BTCPay Server odziv. Jednostavan nedeljni test: generate i platite račun za nekoliko satoshija. Održavajte Umbrel ažurnim (bezbednosne zakrpe, poboljšanja). Napravite rezervnu kopiju pre većih ažuriranja. Za profesionalnu upotrebu, razmislite o eksternom nadzoru (UptimeRobot) sa e-mail/SMS obaveštenjima.



## Izlaganje BTCPay Server javno za online prodavnicu



Da biste integrisali BTCPay Server u veb-baziranu e-commerce prodavnicu (WooCommerce, Shopify, itd.), vaši kupci moraju biti u mogućnosti da pristupe stranicama za plaćanje sa bilo kog mesta, a ne samo sa vaše lokalne mreže.



**Rešenje: Nginx Proxy Manager**



Možete izložiti BTCPay Server javno koristeći Nginx Proxy Manager (dostupan u Umbrel App Store-u). Ovo rešenje zahteva :




- Ime domena (klasično ili besplatno putem DuckDNS, No-IP, Afraid.org)
- Konfigurisanje prosleđivanja portova (portovi 80 i 443) na vašem ruteru
- Instalacija Nginx Proxy Manager-a, koji automatski upravlja SSL sertifikatima



Ova konfiguracija izlaže vaš server internetu i zahteva dodatnu pažnju (jake lozinke, 2FA, redovna ažuriranja). Pripremićemo poseban vodič koji detaljno opisuje ovaj kompletan postupak.



## Zaključak



BTCPay Server na Umbrel kombinuje snagu Bitcoin čvora sa jednostavnošću Umbrela kako bi stvorio samostalno hostovanu profesionalnu platnu infrastrukturu dostupnu svima. Ova finansijska suverenost dolazi sa odgovornošću za održavanje, ali Umbrel uveliko pojednostavljuje operativni teret u poređenju sa prednostima: eliminacija naknada za obradu, zaštita vaše privatnosti, otpornost na cenzuru i potpuna kontrola nad vašim sredstvima.



Korišćenje lokalne mreže već pokriva širok spektar aplikacija: naplata za freelance usluge, lična plaćanja, male fizičke prodavnice, ili jednostavno učenje i eksperimentisanje sa Bitcoin i Lightning u kontrolisanom okruženju. Za potrebe e-trgovine koje zahtevaju javnu izloženost, postoji rešenje Nginx Proxy Manager, ali zahteva dodatnu tehničku konfiguraciju, koju ćemo detaljno opisati u posebnom vodiču.



Bilo da vodite posao, tek započeti projekat ili jednostavno eksperimentišete, BTCPay Server na Umbrel-u nudi potpunu finansijsku autonomiju. Put počinje sa vašom prvom prodavnicom, vašom prvom fakturom, vašom prvom uplatom primljenom direktno u vašu suverenu infrastrukturu.



## Resursi



### Zvanična dokumentacija




- [Zvanična BTCPay Server veb stranica](https://btcpayserver.org)
- [Kompletna dokumentacija za BTCPay Server](https://docs.btcpayserver.org)
- [GitHub BTCPay Server](https://github.com/btcpayserver/btcpayserver)
- [Tailscale dokumentacija](https://tailscale.com/kb)


### Zajednica i podrška




- [Forum BTCPay Server](https://chat.btcpayserver.org)
- [Forum Umbrel](https://community.getumbrel.com)
- [Reddit r/BTCPayServer](https://reddit.com/r/BTCPayServer)