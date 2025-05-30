---
name: Sentinel Watch-Only
description: Šta je Watch-only wallet i kako ga koristiti?
---

![cover](assets/cover.webp)


---

**\*UPOZORENJE:** Nakon hapšenja osnivača Samourai Wallet i zaplene njihovih servera 24. aprila, aplikacija Sentinel nastavlja da funkcioniše, ali **obavezno je koristiti sopstveni Dojo** kako biste pristupili informacijama Blockchain i emitovali transakcije.\*


_Pažljivo pratimo razvoj ovog slučaja kao i razvoj povezanih alata. Budite sigurni da ćemo ažurirati ovaj vodič čim nove informacije budu dostupne._


_Ovaj vodič je pružen isključivo u obrazovne i informativne svrhe. Ne podržavamo niti ohrabrujemo korišćenje ovih alata u kriminalne svrhe. Odgovornost je svakog korisnika da se pridržava zakona u svojoj jurisdikciji._


---

> Čuvajte svoje privatne ključeve, privatnim.

U ovom članku istražujemo sve što treba da znate o watch-only novčanicima. Razgovaramo o tome kako funkcionišu i ispitujemo različite aplikacije dostupne na tržištu. Na kraju, nudimo detaljan vodič o jednoj od najpopularnijih Watch-only wallet aplikacija: Sentinel.


## Šta je Watch-only wallet?


Watch-only wallet, ili samo za čitanje Wallet, je vrsta softvera dizajnirana da omogući korisniku da posmatra transakcije povezane sa jednim ili više specifičnih Bitcoin javnih ključeva, bez pristupa odgovarajućim privatnim ključevima.


Ova vrsta aplikacije zadržava samo podatke neophodne za praćenje Bitcoin Wallet, uključujući pregled njegovog stanja i istorije transakcija, ali nema pristup privatnim ključevima. Stoga je nemoguće potrošiti bitkoine koji se nalaze u Wallet na aplikaciji samo za gledanje.

![watch-only](assets/en/1.webp)

Watch-only se generalno koristi u kombinaciji sa Hardware Wallet. Ovo omogućava skladištenje privatnih ključeva Wallet "Cold," na uređaju koji nije povezan na internet, što ima minimalnu površinu napada, izolujući privatne ključeve od potencijalno ranjivih okruženja. Watch-only aplikacija, s druge strane, isključivo skladišti prošireni javni ključ (`xpub`, `zpub`, itd.) Bitcoin Wallet. Ovaj roditeljski ključ ne dozvoljava otkrivanje povezanih privatnih ključeva i, shodno tome, ne dozvoljava trošenje bitkoina. Međutim, omogućava izvođenje javnih ključeva dece i primanje adresa. Sa znanjem o adresama Wallet osiguranih od strane Hardware Wallet, watch-only aplikacija može pratiti ove transakcije na Bitcoin mreži, nudeći korisniku mogućnost da prati svoj saldo i generate nove adrese za primanje, bez potrebe da svaki put povezuje svoj Hardware Wallet.


## Koji Watch-only wallet koristiti?


Trenutno, najopsežnija aplikacija samo za gledanje je [Sentinel](https://sentinel.watch/), koju su razvili timovi u Samourai Wallet. Ona obuhvata sve osnovne funkcije za dobar Watch-only wallet:



- Podrška za proširene ključeve, javne ključeve i adrese;
- Mogućnost organizovanja više naloga ili novčanika u kolekcije;
- Generisanje adresa za primanje bitkoina na nečiji Hardware Wallet bez potrebe za njegovim direktnim korišćenjem;
- Sposobnost konstruisanja i emitovanja transakcija van mreže;
- Opcija za povezivanje na sopstveni Bitcoin čvor;
- Integracija Tora za poboljšanu privatnost.

Jedinstveni nedostaci Sentinel-a leže u činjenici da je aplikacija dostupna isključivo za Android i ne podržava novčanike sa višestrukim potpisima. Dakle, ako posedujete Android uređaj i vaš Wallet je klasičan sa jednim potpisom, preporučujem Sentinel.

Za one koji žele pratiti multi-signature Wallet, Blue Wallet je jedina aplikacija za koju znam da nudi samo za gledanje mod za ove tipove novčanika, i dostupna je na Android i iOS.


Za korisnike iOS-a koji traže alternativu za Sentinel, [Green Wallet](https://blockstream.com/Green/) ili [Blue Wallet](https://bluewallet.io/watch-only/) mogu biti opcije, iako njihova funkcionalnost samo za gledanje nije tako sveobuhvatna kao kod Sentinel-a.

![watch-only](assets/notext/2.webp)


## Kako koristiti Sentinel Watch-only wallet?


### Instalacija i podešavanje


Počnite instaliranjem aplikacije Sentinel. To možete učiniti ili sa Google Play Store-a ili korišćenjem [APK-a dostupnog za preuzimanje na zvaničnom sajtu](https://sentinel.watch/download/).


![watch-only](assets/notext/3.webp)


Po prvom otvaranju aplikacije, imate izbor između:



- `Poveži se sa Dojo`;
- `Poveži se na Samouraijev server`.


Dojo, razvijen od strane Samourai tima, je puna Bitcoin nod verzija koja se može instalirati samostalno ili dodati jednim klikom na node-in-box rešenja kao što su [Umbrel](https://umbrel.com/) i [RoninDojo](https://ronindojo.io/).


[**-> Otkrijte kako instalirati RoninDojo v2 na Raspberry Pi.**](https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8)


Ako imate svoj Dojo, možete ga povezati u ovoj fazi. Time ćete ostvariti najviši nivo privatnosti prilikom provere informacija o transakcijama na vašoj Bitcoin mreži.


![watch-only](assets/notext/4.webp)


Inače, moguće je odabrati Samourai-jev podrazumevani server. Takođe možete izabrati da li želite da se povežete putem Tor-a ili ne.


![watch-only](assets/notext/5.webp)


Zatim ćete stići na glavnu stranicu Sentinel.


![watch-only](assets/notext/6.webp)


Da biste započeli, možete postaviti aplikaciju. Kliknite na tri male tačke u gornjem desnom uglu, zatim na `Settings`.


![watch-only](assets/notext/7.webp)

Odabirom opcije `User PIN code`, imate mogućnost da postavite lozinku za osiguranje pristupa vašem Watch-only wallet. Takođe imate mogućnost da promenite referentnu valutu za konvertovanje vaših salda u fiat valutu, ili čak da sakrijete fiat vrednosti aktiviranjem opcije `Hide fiat values`. Za povećanu sigurnost, možete aktivirati opciju `Disable Screenshots`, koja sprečava bilo kakve snimke ekrana vaše Sentinel aplikacije i tako izbegava bilo kakvo otkrivanje informacija na spoljašnjem ekranu.

![watch-only](assets/notext/8.webp)


U ovom meniju podešavanja, takođe imate opciju da napravite rezervnu kopiju vašeg Sentinel-a.


### Korišćenje Watch-only wallet


Sa početne stranice, pritisnite plavo dugme `NEW` da dodate novi prošireni javni ključ za praćenje. Zatim imate opciju da skenirate QR kod vašeg ključa, ili da direktno nalepite ključ (`xpub`, `zpub`...) izborom `Paste Pubkey`.


![watch-only](assets/notext/9.webp)


Generalno, `xpub` vašeg Wallet je direktno dostupan putem Wallet softvera za upravljanje koji koristite. Na primer, ako upravljate svojim Hardware Wallet pomoću Sparrow-a, ove informacije se nalaze u kartici `Settings`, u odeljku `Keystore`.


![watch-only](assets/notext/10.webp)


Nakon unosa proširenog javnog ključa u Sentinel, aplikacija vam nudi da kreirate novu kolekciju. Kolekcija predstavlja skup proširenih javnih ključeva organizovanih zajedno. Ova opcija vam daje mogućnost ne samo da navedete sve vaše `xpubs`, već i da ih klasifikujete na uredan način. Na primer, ako imate Samourai Wallet sa više naloga (depozit, premix, postmix...), možete okupiti sve te naloge pod `Samourai` kolekcijom. Za novčanike koje upravljate za svoju porodicu, možete kreirati kolekciju nazvanu `Family`.


Odaberite `Create new collection`. Zatim unesite ime za prošireni ključ koji ste upravo integrisali. Na primer, ako skeniram račun depozita mog Samourai Wallet, nazvao bih ovaj ključ `Deposit`. Kliknite na `SAVE` da završite.


![watch-only](assets/notext/11.webp)


Zatim, dodelite ime ovoj kolekciji i pritisnite ikonu za validaciju koja se nalazi u gornjem desnom uglu ekrana da biste sačuvali kolekciju. Vaša kolekcija je sada vidljiva na početnom ekranu Sentinela.


![watch-only](assets/notext/12.webp)


Ako želite dodati još jedan prošireni javni ključ, ponovo kliknite na `NEW` i unesite vaš ključ.


![watch-only](assets/notext/13.webp)

Bićete zatim upitani da izaberete kolekciju u koju želite da integrišete ovaj ključ, ili da kreirate novu. Na primer, u mom slučaju, postavio sam kolekciju specifično za moj Ledger Wallet.

![watch-only](assets/notext/14.webp)


Da biste detaljno videli proširene ključeve kolekcije, jednostavno kliknite na nju. Zatim možete navigirati kroz različite kartice da biste pregledali istoriju transakcija.


![watch-only](assets/notext/15.webp)


Iz kolekcije, dodirom na tri male tačke u gornjem desnom uglu, zatim na `View Unspent Outputs`, možete pristupiti listi UTXO-a koje drži praćeni Wallet.


![watch-only](assets/notext/16.webp)


### Slanje i primanje Bitcoina sa Sentinel


Kao i kod svakog dobrog Watch-only wallet, Sentinel omogućava da generate prima adrese za primanje bitcoina na praćenom Wallet. Ali Sentinel takođe nudi još jednu naprednu funkciju: kreiranje i emitovanje Partially Signed Bitcoin Transaction (PSBT). Tako Wallet koji drži privatne ključeve može potpisati ovu transakciju, koja, kada je potpisana, može biti emitovana na Bitcoin mreži od strane Sentinela. Hajde da vidimo kako da uradimo sve ovo.


**Oprez, ne preporučuje se primanje bitkoina na prijemni Address koji nije verifikovan od strane samog Wallet.** Ako Wallet koji drži privatne ključeve, kao što je Hardware Wallet, nije eksplicitno potvrdio da je određeni Address povezan sa njim, slanje bitkoina na taj Address je rizična praksa. Zaista, bez ove potvrde, nema garancije da Address zaista pripada vašem Wallet. Stoga, prijemna funkcionalnost Watch-only wallet treba da se koristi sa oprezom, imajući u vidu da sredstva poslana mogu potencijalno biti izgubljena.


Da biste primili bitkoine putem Sentinel-a, izaberite kolekciju od interesa, zatim kliknite na karticu koja odgovara proširenom javnom ključu prema kojem želite da prebacite sredstva.


![watch-only](assets/notext/17.webp)


Na kraju, kliknite na ikonu strelice u donjem levom uglu ekrana. Sentinel zatim generiše prazan prijemni Address za vas. Možete ga kopirati ili skenirati pomoću QR koda.


![watch-only](assets/notext/18.webp)


Da biste izvršili transakciju trošenja sa generate na PSBT iz Sentinel-a, idite na prošireni ključ Wallet sa kojeg želite izvršiti uplatu. Uzmimo, na primer, moj depozitni račun na mom Samourai Wallet. Zatim kliknite na ikonu strelice koja se nalazi u donjem desnom uglu ekrana.


![watch-only](assets/notext/19.webp)


Unesite sve parametre povezane sa vašom transakcijom:



- Unesite primaočev Address (klikom na ikonu QR koda, imate opciju da skenirate ovaj Address);
- Navedite iznos za slanje na ovaj Address;
- Odredite naknade za transakciju.


Kada popunite sva potrebna polja za vašu transakciju, pritisnite dugme `COMPOSE UNSIGNED TRANSACTION`.


![watch-only](assets/notext/20.webp)


Pristupićete zatim PSBT, koji predstavlja konstruisanu ali nepotpisanu Bitcoin transakciju, pošto Sentinel nema pristup vašim privatnim ključevima. Imate opciju da kopirate ovu transakciju, izvezete je kao `.PSBT` fajl, ili da je skenirate putem animiranog QR koda.


![watch-only](assets/notext/21.webp)


Zatim, idite na svoj Wallet koji ima privatne ključeve za potpisivanje transakcije (Samourai, Hardware Wallet...).


![watch-only](assets/notext/22.webp)


Jednom kada je transakcija potpisana, možete se vratiti na Sentinel da je emitujete. Da biste to uradili, iz glavnog menija kliknite na tri male tačke u gornjem desnom uglu, a zatim na `Emituj transakciju`.


![watch-only](assets/notext/23.webp)


Imate opciju da unesete vaš potpisani PSBT na tri različita načina:



- Lepljenjem direktno iz vašeg međuspremnika;
- Uvozom iz `.PSBT` datoteke;
- Skeniranjem putem QR koda.


![watch-only](assets/notext/24.webp)


Jednom kada je potpisana transakcija uneta u sivi okvir, možete kliknuti na dugme Green `BROADCAST TRANSACTION` da biste je emitovali na Bitcoin mreži. Sentinel će vam dati svoj txid.


![watch-only](assets/notext/25.webp)