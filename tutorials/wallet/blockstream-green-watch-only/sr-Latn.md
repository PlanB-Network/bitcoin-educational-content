---
name: Blockstream Green - Samo za gledanje
description: Watch-only wallet konfiguracija
---
![cover](assets/cover.webp)


U ovom vodiču ćete otkriti kako lako postaviti "samo za gledanje" Wallet na mobilnom uređaju koristeći aplikaciju Blockstream Green.


## Šta je Watch-only wallet?


Wallet samo za čitanje, ili "Watch-only wallet", je vrsta softvera dizajnirana da omogući korisniku da posmatra transakcije povezane sa jednim ili više specifičnih Bitcoin javnih ključeva, bez pristupa odgovarajućim privatnim ključevima.


Ova vrsta aplikacije čuva samo podatke potrebne za praćenje Bitcoin Wallet, posebno za pregled njegovog stanja i istorije transakcija, ali nema pristup privatnim ključevima. Kao rezultat toga, nemoguće je trošiti Bitcoine koje drži Wallet na aplikaciji samo za gledanje.


![GREEN-WATCH-ONLY](assets/fr/01.webp)


Watch-only se generalno koristi u kombinaciji sa Hardware Wallet. Ovo omogućava da se privatni ključevi Wallet čuvaju sigurno, na hardveru koji nije povezan na Internet i ima vrlo malu površinu napada, čime se privatni ključevi izoluju od potencijalno ranjivih okruženja. S druge strane, watch-only aplikacija isključivo čuva prošireni javni ključ (`xpub`, `zpub`, itd.) Bitcoin Wallet. Ovaj roditeljski ključ ne može se koristiti za pronalaženje povezanih privatnih ključeva, i stoga se ne može koristiti za trošenje Bitcoina. Međutim, omogućava izvođenje javnih ključeva dece i primanje adresa. Zahvaljujući poznavanju sigurnih adresa Wallet od strane Hardware Wallet, watch-only aplikacija može pratiti ove transakcije na Bitcoin mreži, omogućavajući korisniku da prati svoj saldo i generate nove adrese za primanje, bez potrebe da svaki put povezuje svoj Hardware Wallet.


U ovom vodiču, želeo bih da vas upoznam sa jednim od najpopularnijih rešenja za mobilne uređaje samo za gledanje Wallet: **Blockstream Green**.


![GREEN-WATCH-ONLY](assets/fr/02.webp)


## Predstavljamo Blockstream Green


Blockstream Green je softverska aplikacija dostupna na mobilnim uređajima i desktop računarima. Ranije poznata kao Green Address, ovaj Wallet je postao Blockstream projekat nakon akvizicije 2016. godine.


Green je veoma jednostavna aplikacija za korišćenje, što je čini posebno pogodnom za početnike. Nudi niz funkcija, kao što su upravljanje Hot novčanicima, hardverskim novčanicima i Liquid Sidechain novčanicima.


U ovom vodiču, fokusiraćemo se isključivo na kreiranje Watch-only wallet. Da biste istražili druge upotrebe Green, molimo vas da pogledate naše druge posvećene vodiče:


https://planb.network/tutorials/wallet/desktop/blockstream-green-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da

https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

## Instalacija i konfiguracija aplikacije Blockstream Green


Prvi korak je naravno preuzimanje aplikacije Green. Idite u svoju prodavnicu aplikacija:



- [Za Android](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet);
- [Za Apple](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590).

![GREEN-WATCH-ONLY](assets/fr/03.webp)


Za korisnike Androida, možete takođe instalirati aplikaciju putem `.apk` fajla [dostupnog na Blockstream-ovom GitHub-u](https://github.com/Blockstream/green_android/releases).


![GREEN-WATCH-ONLY](assets/fr/04.webp)


Pokrenite aplikaciju, zatim označite polje "Prihvatam uslove...*".


![GREEN-WATCH-ONLY](assets/fr/05.webp)


Kada prvi put otvorite Green, početni ekran se pojavljuje bez konfigurisanog Wallet. Kasnije, ako kreirate ili uvezete novčanike, oni će se pojaviti u ovom Interface. Pre nego što pređete na kreiranje Wallet, savetujem vam da prilagodite postavke aplikacije prema vašim potrebama. Kliknite na "Postavke aplikacije".


![GREEN-WATCH-ONLY](assets/fr/06.webp)


Opcija "*Poboljšana privatnost*", dostupna samo na Androidu, poboljšava privatnost onemogućavanjem snimaka ekrana i skrivanjem pregleda aplikacija. Takođe automatski zaključava pristup aplikaciji čim se vaš telefon zaključa, čineći vaše podatke težim za izlaganje.


![GREEN-WATCH-ONLY](assets/fr/07.webp)


Za one koji žele poboljšati svoju privatnost, aplikacija nudi opciju usmeravanja vašeg saobraćaja putem Tor-a, mreže koja šifrira sve vaše veze i otežava praćenje vaših aktivnosti. Iako ova opcija može malo usporiti rad aplikacije, toplo se preporučuje za zaštitu vaše privatnosti, posebno ako ne koristite svoj vlastiti kompletan čvor.


![GREEN-WATCH-ONLY](assets/fr/08.webp)


Za korisnike koji imaju svoj sopstveni kompletan čvor, Green Wallet nudi mogućnost povezivanja putem Electrum servera, garantujući potpunu kontrolu nad Bitcoin mrežnim informacijama i distribucijom transakcija.


![GREEN-WATCH-ONLY](assets/fr/09.webp)


Još jedna alternativna funkcija je opcija "*SPV Verification*", koja vam omogućava da direktno verifikujete određene Blockchain podatke i tako smanjite potrebu za poverenjem u podrazumevani čvor Blockstream-a, iako ova metoda ne pruža sve garancije Full node.


![GREEN-WATCH-ONLY](assets/fr/10.webp)


Kada prilagodite ova podešavanja svojim potrebama, kliknite na dugme "*Save*" i ponovo pokrenite aplikaciju.


![GREEN-WATCH-ONLY](assets/fr/11.webp)


## Kreiraj Watch-only wallet na Blockstream Green


Sada ste spremni da kreirate Watch-only wallet. Kliknite na dugme "*Get Started*".


![GREEN-WATCH-ONLY](assets/fr/12.webp)


Moći ćete da birate između nekoliko tipova Wallet. Za ovaj tutorijal, želimo da kreiramo Watch-only wallet, pa kliknite na odgovarajuće dugme.


![GREEN-WATCH-ONLY](assets/fr/13.webp)


Izaberite opciju "Single signature".


![GREEN-WATCH-ONLY](assets/fr/14.webp)


Zatim izaberite "*Bitcoin*". Što se mene tiče, radim ovaj tutorijal na Testnet Wallet, ali postupak ostaje identičan na Mainnet.


![GREEN-WATCH-ONLY](assets/fr/15.webp)


Bićete zamoljeni da navedete ili prošireni javni ključ („xpub“, „zpub“, itd.) ili deskriptor izlaznog skripta.


![GREEN-WATCH-ONLY](assets/fr/16.webp)


Stoga ćete morati da preuzmete ove informacije sa Wallet koji želite da pratite putem vašeg Watch-only wallet. Prošireni javni ključ nije osetljiv u smislu bezbednosti, jer ne omogućava pristup privatnim ključevima, ali je osetljiv za vašu poverljivost, jer otkriva sve vaše javne ključeve i samim tim sve vaše Bitcoin transakcije.


Recimo da koristite Sparrow Wallet za upravljanje vašim Wallet na Hardware Wallet, ove informacije ćete pronaći u odeljku "*Settings*". Pronalaženje ovih informacija zavisiće od softvera za upravljanje Wallet koji koristite, ali obično se nalazi u podešavanjima.


![GREEN-WATCH-ONLY](assets/fr/17.webp)


Kopirajte svoj prošireni javni ključ i unesite ga u aplikaciju Green, zatim kliknite na "Connect".


![GREEN-WATCH-ONLY](assets/fr/18.webp)


Tada ćete moći da vidite saldo povezan sa ovim ključem, kao i istoriju transakcija.


![GREEN-WATCH-ONLY](assets/fr/19.webp)


Klikom na "*Receive*", možete generate primiti Address za primanje bitcoina na vaš Hardware Wallet. Međutim, savetovao bih da ne koristite ovu opciju bez prethodne provere na ekranu Hardware Wallet da li ima privatni ključ povezan sa generisanim Address, pre nego što ga upotrebite za zaključavanje bitcoina. Ovo je dobra praksa koju treba slediti.


![GREEN-WATCH-ONLY](assets/fr/20.webp)


Opcija "*Balayer*" vam omogućava da ručno unesete privatni ključ kako biste direktno trošili sredstva iz vaše Green aplikacije. Osim u vrlo specifičnim slučajevima, ne preporučujem korišćenje ove funkcije, jer zahteva da otkrijete svoj privatni ključ na telefonu, koji je daleko ranjiviji na računarske napade nego vaš Hardware Wallet.


![GREEN-WATCH-ONLY](assets/fr/21.webp)


Dakle, sada znate kako lako postaviti Watch-only wallet na svom pametnom telefonu! To je zgodan alat za praćenje Wallet na Hardware Wallet bez potrebe za povezivanjem i otključavanjem svaki put.


Ako ste smatrali ovaj vodič korisnim, bio bih zahvalan ako biste ostavili Green palac ispod. Slobodno podelite ovaj članak na svojim društvenim mrežama. Hvala vam puno!


Takođe vam preporučujem da pogledate ovaj drugi sveobuhvatni vodič o aplikaciji Blockstream Green za postavljanje Hot Wallet:


https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143
