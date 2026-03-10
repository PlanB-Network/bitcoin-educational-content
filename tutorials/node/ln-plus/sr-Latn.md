---
name: Lightning Network+
description: Dobijte besplatnu dolaznu likvidnost sa kooperativnim otvaranjima na vašem Lightning čvoru
---

![cover](assets/cover.webp)



## Uvod



[LN+ (Lightning Network Plus)](https://lightningnetwork.plus/) je platforma zajednice dizajnirana da olakša saradnju između operatera Lightning Network čvorova. Njegov glavni cilj je poboljšanje povezanosti, likvidnosti i decentralizacije Lightning mreže, bez potrebe za centralizovanim posrednicima.



Ovaj vodič će se fokusirati na uslugu **"Swaps"**, koja je danas najčešće korišćena i strukturirajuća funkcija LN+. Takođe će biti predstavljene i druge usluge koje platforma nudi.



## Pregled LN+



### Šta je Lightning Network Plus?



Lightning Network Plus (LN+) je platforma zajednice za operatere Lightning čvorova koji žele da sarađuju direktno i dobrovoljno. Cilj joj je da olakša kreiranje korisnih, uravnoteženih i održivih Lightning kanala, dok izbegava potrebu za centralizovanim rešenjima ili nametnutim čvorištima.



LN+ je zasnovan na fundamentalnom principu: saradnja među vršnjacima, zasnovana na transparentnosti, reciprocitetu i reputaciji.



### LN+ usluge na prvi pogled



LN+ nudi nekoliko usluga dizajniranih za poboljšanje topologije i likvidnosti Lightning mreže, uključujući:





- Swaps**: uzajamno otvaranje kanala između operatera (glavna usluga).
- Prstenovi**: kružni kanali komunikacije između nekoliko učesnika.
- Zamene zasnovane na poverenju**: varijante koje se više oslanjaju na poverenje i istoriju učesnika.
- Društvene funkcije**: profili, komentari i sistem reputacije.



U preostalom delu ovog tutorijala, fokusiraćemo se isključivo na uslugu **Swaps**, koja je u centru trenutne upotrebe LN+.



## LN+ "Swaps" servis



### Definicija LN+ svapa



LN+ **swap** je dobrovoljni sporazum između dva operatera Lightning čvorova da međusobno otvore Lightning kanale ekvivalentnog (ili unapred dogovorenog) kapaciteta. Za razliku od konvencionalnog jednostranog otvaranja kanala, swap se zasniva na **eksplicitnoj reciprocitetu**.



U praksi :





- Otvarate kanal ka čvoru vašeg partnera.
- Vaš partner otvara kanal ka vašem čvoru.
- Obe strane vezuju sličnu količinu on-chain bitkoina.



### Koja je svrha zamena za operatere čvorova?



Swaps usluga rešava nekoliko ključnih problema sa kojima se susreću Lightning operateri:





- Poboljšana povezanost**: kreiranje korisnih dvosmernih kanala čim se otvore.
- Bolje upravljanje likvidnošću**: svaka strana ima i dolazni i odlazni kapacitet.
- Smanjen rizik od nepotrebnih kanala**: partner se podstiče da drži kanal otvorenim.
- Veća decentralizacija**: direktne veze između operatera, bez nametnutih čvorišta.



### Za koje profile čvorova su zamene korisne?



Zamene su posebno korisne za :





- Novi čvorovi koji žele brzo poboljšati svoju usmerivost.
- Posrednički operateri koji žele povećati gustinu svoje grafičke mreže kanala.
- Čvorovi usmereni na rutiranje koji žele da optimizuju svoju topologiju.



## Povežite svoj Lightning čvor sa LN+



### Tehnički zahtevi



Pre nego što počnete, biće vam potrebno :





- Radni Lightning čvor (LND, Core Lightning ili Eclair).
- Pristup interfejsu za upravljanje vašim čvorom.
- Dovoljan on-chain kapacitet za otvaranje kanala.



Idite na [Lightning Network](https://lightningnetwork.plus/) Plus vebsajt i kliknite na dugme `Login` u gornjem desnom uglu interfejsa.



![capture](assets/fr/03.webp)



### Autentifikacija putem potpisa poruke



Da biste se autentifikovali, potrebno je da potpišete poruku pomoću privatnog ključa vašeg Lightning čvora. Sa ThunderHub, ova operacija je veoma jednostavna.



Počnite kopiranjem poruke koju prikazuje LN+.



![capture](assets/fr/04.webp)



U ThunderHub, idite na karticu `Tools`, zatim kliknite na dugme `Sign` u odeljku `Messages`.



![capture](assets/fr/05.webp)



Nalepite poruku za autentifikaciju koju pruža LN+, zatim kliknite na `Potpiši`.



![capture](assets/fr/06.webp)



ThunderHub zatim potpisuje ovu poruku koristeći privatni ključ vašeg čvora. Kopirajte generisani potpis.



![capture](assets/fr/07.webp)



Nalepite ovaj potpis u odgovarajuće polje na LN+ sajtu, zatim kliknite na `Sign in`.



![capture](assets/fr/08.webp)



Sada ste povezani sa LN+ sa svojim Lightning čvorom. Ovaj proces omogućava LN+ da verifikuje da ste vi zakoniti vlasnik čvora koji tvrdite na njihovoj platformi.



![capture](assets/fr/09.webp)



Ako želite, možete personalizovati svoj LN+ profil, na primer dodavanjem kratke biografije.



## Učestvuj u postojećoj zameni



### Pristup ponudama zamene



Da biste učestvovali u otvaranju svog prvog kanala, idite na meni `Swaps` na vrhu interfejsa. Ovde ćete pronaći sve trenutno dostupne zamene, u zavisnosti od karakteristika vašeg čvora.



![capture](assets/fr/10.webp)



### Uslovi podobnosti



Da biste se pridružili postojećoj ponudi zamene, jednostavno izaberite odgovarajući oglas i registrujte se. Međutim, LN+ omogućava kreatoru zamene da definiše određene **uslove podobnosti**, kao što su :





- minimalan broj kanala već otvoren ;
- minimalni ukupni kapacitet čvora ;
- određene vrste veze prihvaćene.



### Nedavni čvorovi



Kao rezultat toga, posebno u ranim fazama korišćenja, moguće je da **malo ili nijedna ponuda nije dostupna** vašem čvoru. Ovo je uobičajena situacija za nove čvorove ili one koji još nisu povezani.



U mom slučaju, uprkos postojanju nekoliko otvorenih kanala, nijedna od ponuda nije ispunjavala potrebne kriterijume.



## Kreirajte svoju ponudu za zamenu



### Kada treba da kreirate svoj swap?



Kada ne postoji dostupna ponuda, kreiranje sopstvene zamene je često najbolje rešenje. To vam takođe omogućava da zadržite kontrolu nad parametrima zamene.



### Konfiguracija zamene



Kliknite na **Start Liquidity Swap**, zatim konfigurišite parametre vaše ponude:





- odaberite ukupan broj učesnika (3, 4 ili 5);
- naznačiti kapacitet kanala koji će biti otvoreni;
- definišite period obaveze tokom kojeg se učesnici slažu da neće zatvarati svoje kanale;
- navesti sve restrikcije koje se primenjuju na učesnike (minimalan broj kanala, minimalan ukupan kapacitet, tip prihvaćene konekcije).



![capture](assets/fr/11.webp)



### Objavljivanje i očekivanja učesnika



Kada su svi parametri uneti, kliknite na **Start Liquidity Swap** da objavite svoju ponudu. Sada samo treba da sačekate da se drugi operateri prijave.



![capture](assets/fr/12.webp)



## Finalizacija zamene



### Efikasno otvaranje kanala



Sada kada su sve zamene pozicija obavljene, svaki učesnik može videti, sa svog LN+ interfejsa, ka kojem čvoru treba da otvori Lightning kanal.



![capture](assets/fr/13.webp)



Na vašoj strani, otvorite kanal koristeći Node ID koji je obezbedio LN+ i poštujući naznačeni iznos. Ova operacija se može izvesti putem ThunderHub, drugog upravitelja Lightning čvora ili direktno putem osnovnog interfejsa vašeg čvora.



![capture](assets/fr/14.webp)



Kada se otvori, kanal se pojavljuje u odeljku kanala na čekanju.



![capture](assets/fr/15.webp)



### Potvrda u LN+



Zatim se vratite na LN+ da potvrdite da ste započeli otvaranje kanala, klikom na dugme `Channel Opening Started`.



![capture](assets/fr/16.webp)



### Kraj zamene



Kada svi učesnici otvore kanale na koje su se obavezali, zamena se smatra završenom.



## Reputacija i dobre komunikacione prakse



### LN+ sistem reputacije



LN+ uključuje sistem reputacije zasnovan na mišljenjima koja učesnici ostavljaju na kraju zamena. Ova mišljenja su javna i direktno utiču na sposobnost operatera da se pridruži ili kreira buduće zamene.



![capture](assets/fr/17.webp)



### Preporučene najbolje prakse



Kako bi se očuvala dobra reputacija i osiguralo nesmetano odvijanje zamena, preporučuje se da:





- poštujte rokove otvaranja kanala ;
- komunicirajte brzo u slučaju problema ili kašnjenja;
- koristite odeljak za komentare da razmenjujete mišljenja sa drugim učesnicima;
- ne zatvarati kanal pre kraja perioda obaveze.




![capture](assets/fr/18.webp)



### Zašto je reputacija centralna za LN+



LN+ je zasnovan na modelu dobrovoljne saradnje, bez jakih tehničkih ograničenja. Ugled je stoga glavni podsticaj za osiguranje pouzdanosti i poverenja učesnika.



## Ostale LN+ usluge



Pored Swaps, LN+ nudi i druge usluge dizajnirane za poboljšanje povezanosti i koordinacije između operatera Lightning čvorova. Rings** omogućavaju nekoliko učesnika da kreiraju petlju otvaranja kanala, čime se pojačava redundancija rutiranja i gustina Lightning grafa. Swaps zasnovani na poverenju** bazirani su na sličnim principima kao klasični swaps, ali nude veću fleksibilnost učesnicima koji već imaju uspostavljenu reputaciju na platformi.



LN+ takođe integriše društvene funkcije kao što su javni profili čvorova, komentari na zamene i sistem reputacije. Ovi alati nisu tehničke usluge per se, ali igraju centralnu ulogu u nesmetanom radu platforme, olakšavajući komunikaciju, koordinaciju i poverenje između operatera.



## Zaključak



LN+'s Swaps usluga je efikasan alat za poboljšanje povezanosti, likvidnosti i decentralizacije u Lightning mreži. Promovišući uzajamno, koordinisano otvaranje kanala, LN+ omogućava operaterima čvorova da ojačaju svoju topologiju, dok istovremeno promoviše odgovornu, decentralizovanu saradnju.