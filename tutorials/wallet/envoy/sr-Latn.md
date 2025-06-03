---
name: Izaslanik
description: Postavljanje i korišćenje Passport-a sa Envoy aplikacijom
---
![cover](assets/cover.webp)


Envoy je aplikacija za upravljanje Bitcoin Wallet koju je razvila Foundation. Posebno je dizajnirana za upotrebu sa Passport Hardware Wallet.


Pasoš "*Batch 2*" predstavljen u ovom vodiču sa Envoy aplikacijom je naslednik "*Founder's Edition*". Ističe se svojim premium dizajnom, ekranom visoke definicije u boji i ergonomskom fizičkom tastaturom. Radi u "*Air-Gap*" režimu, osiguravajući da privatni ključevi vašeg Wallet ostanu potpuno izolovani, sa mogućnošću komunikacije putem MicroSD kartice ili QR kodova. Uređaj je opremljen uklonjivom, punjivom Nokia BL-5C baterijom kapaciteta 1200 mAh. Ova neproprietarna baterija se lako može zameniti, jer je BL-5C model široko dostupan u prodavnicama.


Što se tiče povezivanja, Passport je opremljen MicroSD portom, USB-C portom za punjenje i zadnjom kamerom za skeniranje QR kodova.


U smislu bezbednosti, Passport uključuje sigurnosni element, a izvorni kod uređaja je potpuno otvorenog koda. Nudi sve funkcije koje se očekuju od dobrog Bitcoin Hardware Wallet. Imajte na umu da Passport još ne podržava miniscript, ali ova funkcija je planirana za drugi kvartal 2025. godine.


Po ceni od $199, Passport je pozicioniran kao vrhunski Hardware Wallet, konkurišući modelima Coldcard Q, Jade Plus, Tezor Safe 5 i Ledger-ovim modelima najvišeg ranga.


![Image](assets/fr/01.webp)


Da biste upravljali svojim sigurnim Wallet na Passportu, imate nekoliko opcija. Ovaj Hardware Wallet je kompatibilan sa većinom Wallet softvera za upravljanje na tržištu, uključujući Sparrow Wallet, Specter Desktop, Nunchuk, Keeper, između ostalih.


U ovom vodiču, koji je namenjen početnicima i korisnicima srednjeg nivoa, otkrićemo kako koristiti aplikaciju Envoy sa vašim Passportom. To je najlakši način da izvučete maksimum iz vašeg Hardware Wallet.


Ako ste napredni korisnik i želite da istražite složenije funkcije, preporučujem da pogledate ovaj drugi vodič gde konfigurišemo Passport sa Sparrow Wallet :


https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

## Raspakivanje pasoša


Kada primite svoj Pasoš, proverite da li su kutija i Seal na kartonu netaknuti kako biste potvrdili da paket nije otvoren. Softverska verifikacija autentičnosti i integriteta uređaja će takođe biti izvršena prilikom postavljanja.


![Image](assets/fr/02.webp)


Sadržaj kutije uključuje :




- Pasoš;
- Komad kartona za zapisivanje vaše Mnemonic fraze;
- USB-C kabl za punjenje ;
- MicroSD kartica ;
- Dva MicroSD na Lightning ili USB-C adaptera ;
- Nalepnice.


Na uređaju ćete pronaći :




- Tastatura (1) ;
- USB-C port (2);
- Dugme za brisanje (3);
- Dugme za povratak (4) ;
- dugme za potvrdu (5);
- Direkcioni taster (6);
- Dugme za uključivanje/isključivanje (7);
- pokazivač
- MicroSD port (9) ;
- Dugme za promenu režima aA1 (10) ;
- Zadnja kamera.


![Image](assets/fr/03.webp)


## Preuzmi Envoy aplikaciju


Idite u svoju prodavnicu aplikacija da preuzmete Envoy :




- Na [Google Play Store](https://play.google.com/store/apps/details?id=com.foundationdevices.envoy);
- Na [App Store](https://apps.apple.com/us/app/envoy-by-foundation/id1584811818);
- Na [F-Cold](https://foundation.xyz/fdroid/).


![Image](assets/fr/50.webp)


Možete takođe preuzeti APK datoteku direktno [iz Foundation-ovog GitHub repozitorijuma](https://github.com/Foundation-Devices/envoy/releases).


![Image](assets/fr/51.webp)


Kada se aplikacija otvori, izaberite "*Upravljaj pasošem*".


![Image](assets/fr/52.webp)


Izaberite da li želite da aktivirate Tor vezu kako biste pojačali poverljivost, zatim pritisnite "*Nastavi*".


![Image](assets/fr/53.webp)


Izaberite "*Poveži postojeći Passport*" ako je vaš Passport već konfigurisan, ili "*Postavi novi Passport*" ako prvi put inicijalizujete vaš Hardware Wallet.


![Image](assets/fr/54.webp)


Prihvatite uslove korišćenja.


![Image](assets/fr/55.webp)


Zatim će vam biti zatraženo da potvrdite autentičnost pasoša. Kliknite na "*Next*".


![Image](assets/fr/56.webp)


## Početni pasoš


Pritisnite dugme za uključivanje/isključivanje na strani uređaja da biste ga pokrenuli.


![Image](assets/fr/04.webp)


Pritisnite dugme za potvrdu da biste pristupili sledećem meniju.


![Image](assets/fr/05.webp)


U ovom vodiču ćemo koristiti Envoy za upravljanje Wallet osiguranim putem Passport-a. Izaberite "*Envoy App*".


![Image](assets/fr/57.webp)


Kliknite na "*Continue on Envoy*".


![Image](assets/fr/58.webp)


Sledeći korak je da proverite svoj uređaj. Ovo potvrđuje autentičnost vašeg Pasošа i osigurava da nije bio izmenjen tokom transporta. Od vas će se tražiti da skenirate QR kod.


![Image](assets/fr/08.webp)


Skenirajte dinamičke QR kodove prikazane u aplikaciji sa vašim pasošem. Kada je skeniranje završeno, kliknite na "*Dalje*".


![Image](assets/fr/59.webp)


Zatim koristite svoj telefon da skenirate QR kod prikazan na vašem pasošu.


![Image](assets/fr/60.webp)


Ako se pojavi poruka "*Your Passport is secure*", to potvrđuje da je vaš Hardware Wallet originalan. Sada ga možete koristiti za osiguranje Bitcoin Wallet.


![Image](assets/fr/61.webp)


Potvrdite rezultat testa na vašem Pasoš-u.


![Image](assets/fr/14.webp)


## Postavljanje PIN koda


Sledeći korak je unos PIN koda. PIN kod otključava vaš Pasoš. Stoga pruža zaštitu protiv neovlašćenog fizičkog pristupa. PIN kod nije uključen u izvođenje kriptografskih ključeva vašeg Wallet. Dakle, čak i bez pristupa PIN kodu, posedovanje vaše 12- ili 24-reči Mnemonic fraze omogućiće vam da ponovo dobijete pristup vašim bitcoinima.


![Image](assets/fr/15.webp)


Preporučujemo da izaberete PIN kod koji je što je moguće nasumičniji. Takođe, obavezno sačuvajte ovaj kod na odvojenom mestu od mesta gde se čuva vaš pasoš (npr. u menadžeru lozinki).


Možete izabrati PIN kod između 6 i 12 cifara. Savetujem vam da ga napravite što dužim.


Koristite tastaturu da unesete svoj PIN broj. Kada završite, kliknite na dugme za potvrdu.


![Image](assets/fr/16.webp)


Potvrdite svoj PIN drugi put.


![Image](assets/fr/17.webp)


Vaš PIN kod je registrovan.


![Image](assets/fr/18.webp)


## Ažuriraj Passport firmware


Vaš Hardware Wallet predlaže da ažurirate njegov firmver. Preporučujem da odmah izvršite ažuriranje kako biste iskoristili poboljšanja i ispravke koje donose najnovije verzije. Da biste nastavili, kliknite na dugme za potvrdu sa desne strane.


![Image](assets/fr/19.webp)


Vaš pasoš je spreman da primi novi firmware putem MicroSD kartice.


![Image](assets/fr/20.webp)


### Bez aplikacije Envoy


Da biste to uradili, koristite MicroSD karticu uključenu u vaš Passport paket (ili neku drugu), i umetnite je u vaš računar. Preuzmite najnoviju verziju firmvera sa [sajta dokumentacije Foundation](https://docs.foundation.xyz/firmware-updates/passport/) ili [njihovog GitHub repozitorijuma](https://github.com/Foundation-Devices/passport2/releases).


![Image](assets/fr/21.webp)


Pre nego što ga instalirate na svoj uređaj, toplo vam savetujemo da proverite autentičnost i integritet preuzetog firmvera. Ako vam je potrebna pomoć oko toga, pogledajte ovaj vodič :


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

### Sa Envoy aplikacijom


Druga, jednostavnija opcija je da direktno koristite Envoy aplikaciju. Kliknite na "*Download Firmware*".


![Image](assets/fr/62.webp)


Koristite adapter isporučen uz vaš Passport da povežete MicroSD karticu sa vašim telefonom.


![Image](assets/fr/63.webp)


Izaberite MicroSD karticu u vašem istraživaču datoteka da biste sačuvali firmver.


![Image](assets/fr/64.webp)


Firmware je sada sačuvan. Uklonite MicroSD iz svog pametnog telefona i umetnite ga u Passport.


![Image](assets/fr/65.webp)


Passport istraživač datoteka će se otvoriti. Odaberite datoteku `vN.N.N-passport.bin`.


![Image](assets/fr/22.webp)


Kliknite na "*Select*".


![Image](assets/fr/23.webp)


Zatim potvrdite instalaciju firmvera.


![Image](assets/fr/24.webp)


Molimo sačekajte da se ažuriranje završi.


![Image](assets/fr/25.webp)


Kada se ažuriranje završi, unesite svoj PIN kod da otključate uređaj i nastavite sa konfiguracijom.


![Image](assets/fr/26.webp)


## Kreiraj novi Bitcoin Wallet


Sada je vreme da kreirate novi Bitcoin Wallet. Kliknite na dugme za potvrdu.


![Image](assets/fr/27.webp)


Da biste kreirali novi Wallet, kliknite na "*Create New seed*".


![Image](assets/fr/28.webp)


Možete birati između 12- ili 24-reči Mnemonic fraze. Bezbednost koju nude obe opcije je slična, tako da možete izabrati onu koju je najlakše sačuvati, tj. 12 reči.


![Image](assets/fr/29.webp)


Kliknite na "*Continue*".


![Image](assets/fr/30.webp)


Vaš pasoš će sada generate vaš "*Rezervni Kod*". Ovo je niz brojeva koji se mogu koristiti za dešifrovanje rezervne kopije vašeg Wallet sačuvane na MicroSD. Ovaj rezervni sistem, specifičan za Foundation uređaje, predstavlja dodatnu rezervnu kopiju vašoj Mnemonic frazi, ali nije kompatibilan sa drugim Bitcoin softverom.


Ako odlučite da koristite ovaj "*Rezervni Kod*", obavezno ga čuvajte na drugom mestu od vaše MicroSD kartice koja sadrži šifrovanu rezervnu kopiju vašeg Wallet. Međutim, možete odlučiti da ne koristite ovaj sistem ako smatrate da je dobra rezervna kopija vaše Mnemonic fraze dovoljna.


![Image](assets/fr/31.webp)


Unesite svoj "*Backup Code*" da potvrdite da ste ga ispravno sačuvali.


![Image](assets/fr/32.webp)


Ako je MicroSD umetnut, šifrovana rezervna kopija vašeg Wallet je sačuvana tamo.


![Image](assets/fr/33.webp)


Vaš pasoš će prikazati vašu 12-rečnu Mnemonic frazu. Ova Mnemonic vam daje potpuni, neograničeni pristup svim vašim bitkoinima. Svako ko poseduje ovu frazu može ukrasti vaša sredstva, čak i bez fizičkog pristupa vašem pasošu.


Fraza od 12 reči vraća pristup vašim bitkoinima u slučaju gubitka, krađe ili oštećenja vašeg Pasporta. Stoga je veoma važno da je pažljivo sačuvate i skladištite na sigurnom mestu.


Možete ga napisati na kartonu koji je priložen u kutiji, ili za dodatnu sigurnost, preporučujem graviranje na bazi od nerđajućeg čelika kako biste ga zaštitili od požara, poplave ili urušavanja.


Kliknite na dugme za potvrdu da vidite vašu Mnemonic frazu.


![Image](assets/fr/34.webp)


Za više informacija o pravilnom načinu čuvanja i upravljanja vašom Mnemonic frazom, toplo preporučujem da pratite ovaj drugi vodič, posebno ako ste početnik:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

naravno, nikada ne smete deliti ove reči na Internetu, kao što ja radim u ovom vodiču. Ovaj uzorak Wallet će se koristiti samo na Testnet i biće obrisan na kraju vodiča.**_


Napravite fizičku rezervnu kopiju ove rečenice.


![Image](assets/fr/35.webp)


Vaš pasoš je uspešno konfigurisan. Kliknite na dugme za potvrdu da nastavite.


![Image](assets/fr/36.webp)


## Postavljanje Wallet na Envoy


U ovom vodiču pokazaću vam kako da koristite Passport sa Envoy aplikacijom. Međutim, ovaj Hardware Wallet je takođe kompatibilan sa Sparrow Wallet, Keeper, BlueWallet, Nunchuk, Specter, i mnogim drugima...


![Image](assets/fr/66.webp)


Koristite aplikaciju Envoy da skenirate QR kod prikazan na vašem pasošu.


![Image](assets/fr/67.webp)


Vaši javni ključevi su sada uvezeni u aplikaciju. Kliknite na "*Validate receive Address*".


![Image](assets/fr/68.webp)


Koristite svoj Pasoš da skenirate Address prikazan na Envoy.


![Image](assets/fr/69.webp)


Vaš pasoš će potvrditi da li je Wallet uvezen na Envoy važeći. Potvrdite to u aplikaciji.


![Image](assets/fr/70.webp)


Sada možete pristupiti javnim informacijama vašeg Wallet na Envoy, ali da biste trošili bitkoine, moraćete koristiti vaš Passport.


![Image](assets/fr/71.webp)


## Otkrijte Passport menije


Vaš pasoš Interface ima tri glavna menija:




- "*Nalog*";
- "*Više*";
- "*Podešavanja*".


Da biste se kretali između ovih menija, koristite strelice levo i desno na upravljačkoj tabli.


### Meni *Account*


U meniju "*Account*" pronaći ćete glavne funkcije vašeg Bitcoin Wallet. Možete potpisati transakciju ili putem kamere ili putem MicroSD porta.


![Image](assets/fr/37.webp)


Podmeni "*Account Tools*" nudi opcije kao što su verifikacija Address, potpisivanje poruke ili konsultovanje adresa u vašem Wallet.


![Image](assets/fr/38.webp)


U podmeniju "*Manage Account*", možete povezati vaš Bitcoin Wallet sa softverom za upravljanje Wallet (što ćemo obraditi u narednim koracima ovog vodiča), ili pregledati i preimenovati vaš nalog.


![Image](assets/fr/39.webp)


### Više" meni


U meniju "*Više*", možete kreirati novi nalog na vašem Wallet, povezan sa istom Mnemonic frazom.


![Image](assets/fr/40.webp)


Možete takođe uneti BIP39 passphrase ili koristiti privremeni seed.


![Image](assets/fr/41.webp)


### Meni "Settings"


U meniju "*Settings*" pronaći ćete sve postavke za Wallet i uređaj.


![Image](assets/fr/42.webp)


Podmeni "*Device*" vam daje opcije za prilagođavanje osvetljenosti ekrana, postavljanje kašnjenja pre automatskog zaključavanja, promenu PIN koda ili preimenovanje uređaja.


![Image](assets/fr/43.webp)


Podmeni "*Backup*" omogućava vam da izvezete svoju šifrovanu Wallet rezervnu kopiju, proverite validnost postojeće rezervne kopije ili ponovo pronađete svoj "*Backup Code*".


![Image](assets/fr/44.webp)


Podmeni "*Firmware*" služi za ažuriranje firmvera vašeg Passport uređaja. Preporučujemo da redovno izvršavate ova ažuriranja kako biste iskoristili najnovije ispravke i funkcije.


![Image](assets/fr/45.webp)


Podmeni "*Bitcoin*" vam omogućava da promenite prikazanu jedinicu (BTC ili satoshi), upravljate mogućim Multisig Wallet, ili pređete na režim "*Testnet*".


![Image](assets/fr/46.webp)


U "*Napredno*", možete pregledati reči vaše Mnemonic fraze, izvršiti radnje na umetnutoj MicroSD kartici, resetovati vaš Passport na fabrička podešavanja ili izvršiti proveru autentičnosti, kao što je prethodno urađeno.


![Image](assets/fr/47.webp)


Možete aktivirati "*Sigurnosne Reči*", funkciju koja dodaje Layer sigurnosti prikazivanjem dve specifične reči prilikom otključavanja uređaja nakon unosa prva četiri broja PIN koda. Ove reči, koje se čuvaju tokom konfiguracije, osiguravaju da Pasoš nije zamenjen ili izmenjen. U slučaju bilo kakvog neslaganja u kasnijem periodu, savetujemo vam da ne koristite uređaj. Savetujem vam da aktivirate ovu opciju kako biste sprečili većinu rizika fizičkog kompromitovanja uređaja.


![Image](assets/fr/48.webp)


Konačno, podmeni "*Extensions*" vam omogućava da aktivirate funkcije specifične za određene upotrebe uređaja, kao što je Whirlpool CoinJoin protokol.


![Image](assets/fr/49.webp)


## Primite bitkoine


Sada kada je vaš Passport postavljen, spremni ste da primite svoj prvi Sats na vašem novom Bitcoin Wallet. Da biste to uradili, na Envoy-u kliknite na vaš "*Primary 0*" nalog.


![Image](assets/fr/72.webp)


Kliknite na dugme "*Receive*".


![Image](assets/fr/73.webp)


Vaša Envoy aplikacija prikazuje prvi dostupni prazan Address na vašem Wallet. Pre nego što ga upotrebite, hajde da proverimo Address na ekranu Pasoš da bismo se uverili da zaista pripada našem Bitcoin Wallet. U meniju "*Nalog*" vašeg Pasoša, izaberite "*Alati naloga*".


![Image](assets/fr/74.webp)


Kliknite na "*Verify Address*", zatim skenirajte QR kod prikazan na Envoy.


![Image](assets/fr/75.webp)


Uverite se da se Address prikazan na pasošu tačno poklapa sa onim prikazanim na Sparrow, i da se pojavljuje "*Verified*".


![Image](assets/fr/76.webp)


Sada ga možete koristiti za primanje bitkoina. Kada se transakcija emituje na mreži, pojaviće se na Envoy-u. Sačekajte dok ne dobijete dovoljno potvrda da biste smatrali transakciju konačnom.


![Image](assets/fr/77.webp)


## Pošalji bitkoine


Sada kada imate nekoliko Sats u vašem Wallet, možete ih takođe poslati. Da biste to uradili, kliknite na dugme "*Send*".


![Image](assets/fr/78.webp)


Unesite primaljaoca Address, bilo tako što ćete ga direktno nalepiti, ili skeniranjem QR koda kamerom vašeg pametnog telefona.


![Image](assets/fr/79.webp)


Odredite iznos koji želite poslati, zatim kliknite na "*Potvrdi*".


![Image](assets/fr/80.webp)


Odaberite naknadu za transakciju prema trenutnoj tržišnoj situaciji, zatim proverite informacije o transakciji. Ako je sve tačno, kliknite na "*Sign with Passport*".


![Image](assets/fr/81.webp)


Dodajte oznaku svojoj transakciji kako biste jasno evidentirali njenu svrhu.


![Image](assets/fr/82.webp)


Envoy zatim prikazuje PSBT (*Partially Signed Bitcoin Transaction*). Aplikacija je izgradila transakciju, ali još uvek nedostaju potpis(i) za otključavanje bitkoina korišćenih u ulazu. Ove potpise može izvršiti samo Passport, koji hostuje vaš seed dajući pristup privatnim ključevima potrebnim za potpisivanje transakcije.


![Image](assets/fr/83.webp)


Na vašem Pasoš-u, pristupite meniju "*Account*" i kliknite na "*Sign with QR Code*".


![Image](assets/fr/84.webp)


Skeniraj PSBT (*Partially Signed Bitcoin Transaction*) prikazan na Envoy.


![Image](assets/fr/85.webp)


Potvrdite da su prijemnik Address i poslata suma tačni, zatim pritisnite dugme za potvrdu.


![Image](assets/fr/86.webp)


Proveri Exchange Address. U mom primeru, nema ga, jer transakcija uključuje jedan izlaz.


![Image](assets/fr/87.webp)


Uverite se da je naknada ona koju ste izabrali.


![Image](assets/fr/88.webp)


Ako su sve informacije tačne, kliknite na dugme za potvrdu da biste potpisali transakciju.


![Image](assets/fr/89.webp)


Vaš pasoš vam prikazuje vašu potpisanu transakciju u obliku QR koda.


![Image](assets/fr/90.webp)


Na aplikaciji Envoy, kliknite na ikonu QR koda, zatim skenirajte PSBT prikazan na ekranu vašeg Passport-a.


![Image](assets/fr/91.webp)


Proverite detalje transakcije još jednom. Ako je sve tačno, pritisnite "*Pošalji transakciju*" da biste je emitovali na Bitcoin mreži.


![Image](assets/fr/92.webp)


Vaša transakcija sada čeka potvrdu. Status možete pratiti direktno sa svog naloga.


![Image](assets/fr/93.webp)


Čestitamo, sada znate kako da postavite i koristite Passport sa Envoy aplikacijom. Ako ste smatrali da je ovaj vodič koristan, bio bih zahvalan ako biste ostavili Green palac ispod. Slobodno podelite ovaj članak na vašim društvenim mrežama. Hvala što delite!


Za dodatne informacije, pogledajte naš vodič o Liana softveru:


https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04