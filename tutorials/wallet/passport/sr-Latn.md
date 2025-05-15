---
name: Pasoš - Fondacija
description: Konfigurisanje i korišćenje Passport Hardware Wallet u ručnom režimu
---
![cover](assets/cover.webp)


Pasoš je Bitcoin-samo Hardware Wallet, dizajniran od strane Foundation Devices, američke kompanije osnovane u aprilu 2020. u Bostonu.


Pasoš "*Batch 2*" predstavljen u ovom vodiču je naslednik "*Founder's Edition*". Ističe se svojim premium dizajnom, ekranom visoke rezolucije u boji i ergonomskom fizičkom tastaturom. Radi u "*Air-Gap*" režimu, osiguravajući da privatni ključevi vašeg Wallet ostanu potpuno izolovani, sa mogućnošću komunikacije putem MicroSD kartice ili QR kodova. Uređaj je opremljen uklonjivom, punjivom Nokia BL-5C baterijom kapaciteta 1200 mAh. Ova neproprietarna baterija se lako može zameniti, jer je BL-5C model široko dostupan u prodavnicama.


Što se tiče povezivanja, Passport je opremljen MicroSD portom, USB-C portom za punjenje i zadnjom kamerom za skeniranje QR kodova.


Što se tiče bezbednosti, Passport uključuje sigurnosni element, a izvorni kod uređaja je potpuno otvorenog koda. Nudi sve funkcije koje se očekuju od dobrog Bitcoin Hardware Wallet. Imajte na umu da Passport još uvek ne podržava miniscript, ali je ova funkcija planirana za drugi kvartal 2025. godine.


Po ceni od $199, Passport je pozicioniran kao vrhunski Hardware Wallet, konkurišući modelima Coldcard Q, Jade Plus, Tezor Safe 5 i Ledger-ovim modelima najvišeg ranga.


![Image](assets/fr/01.webp)


Da biste upravljali svojim sigurnim Wallet na Passport-u, imate nekoliko opcija. Ovaj Hardware Wallet je kompatibilan sa većinom Wallet softvera za upravljanje na tržištu, uključujući Sparrow Wallet, Specter Desktop, Nunchuk, Keeper, među ostalima. U ovom vodiču, naučićemo kako da ga koristimo sa Sparrow Wallet.


Ako ste početnik, najlakša opcija je da koristite svoj Passport sa izvornom Envoy aplikacijom, koju je razvila Foundation. Da biste saznali kako koristiti Envoy sa svojim Passport-om, pogledajte ovaj drugi vodič :


https://planb.network/tutorials/wallet/mobile/envoy-3ae5d6c7-623b-45b3-bb34-abcf9572b7cb

## Otvaranje pasoša


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
- Dugme za potvrdu (5);
- Direkcioni taster (6);
- Dugme za uključivanje/isključivanje (7);
- Pokazatelj statusa (8);
- MicroSD port (9) ;
- Dugme za promenu režima aA1 (10) ;
- Zadnja kamera.


![Image](assets/fr/03.webp)


## Početni pasoš


Pritisnite dugme za uključivanje/isključivanje sa strane uređaja da biste ga pokrenuli.


![Image](assets/fr/04.webp)


Pritisnite dugme za potvrdu da biste pristupili sledećem meniju.


![Image](assets/fr/05.webp)


U ovom vodiču ćemo koristiti Sparrow Wallet za upravljanje Passport-zaštićenim Wallet. Izaberite "*Manual Setup*".


![Image](assets/fr/06.webp)


Zatim prihvatite uslove korišćenja.


![Image](assets/fr/07.webp)


Sledeći korak je da proverite svoj uređaj. Ovo potvrđuje autentičnost vašeg Pasošа i osigurava da nije bio izmenjen tokom transporta. Od vas će biti zatraženo da skenirate QR kod.


![Image](assets/fr/08.webp)


Idite na [zvanični sajt za verifikaciju](https://validate.foundationdevices.com/) i izaberite "*Passport*".


![Image](assets/fr/09.webp)


Koristite kameru vašeg Passport-a da skenirate QR kod prikazan na sajtu.


![Image](assets/fr/10.webp)


Vaš uređaj će zatim prikazati 4 reči.


![Image](assets/fr/11.webp)


Unesite ove reči na veb-sajt da potvrdite autentičnost vašeg pasoša i kliknite na "*Validate*".


![Image](assets/fr/12.webp)


Ako se pojavi poruka "*Passed*", vaš Hardware Wallet je originalan. Sada ga možete koristiti za osiguranje Bitcoin Wallet.


![Image](assets/fr/13.webp)


Potvrdite rezultat testa na vašem Pasoš.


![Image](assets/fr/14.webp)


## Postavljanje PIN koda


Sledeći korak je unos PIN koda. PIN kod otključava vaš Pasoš. Stoga pruža zaštitu protiv neovlašćenog fizičkog pristupa. PIN kod nije uključen u izvođenje kriptografskih ključeva vašeg Wallet. Dakle, čak i bez pristupa PIN kodu, posedovanje vaše 12- ili 24-reči Mnemonic fraze omogućiće vam da ponovo dobijete pristup vašim bitcoinima.


![Image](assets/fr/15.webp)


Preporučujemo da izaberete PIN kod koji je što nasumičniji. Takođe, obavezno sačuvajte ovaj kod na mestu odvojenom od mesta gde se čuva vaš pasoš (npr. u menadžeru lozinki).


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


Da biste to uradili, koristite MicroSD karticu uključenu u vaš Passport paket (ili neku drugu), i umetnite je u vaš računar. Preuzmite najnoviju verziju firmvera sa [sajta za dokumentaciju Foundation](https://docs.foundation.xyz/firmware-updates/passport/) ili [njihovog GitHub repozitorijuma](https://github.com/Foundation-Devices/passport2/releases).


![Image](assets/fr/21.webp)


Pre nego što ga instalirate na svoj uređaj, toplo vam savetujemo da proverite autentičnost i integritet preuzetog firmvera. Ako vam je potrebna pomoć oko ovoga, pogledajte ovaj vodič :


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Nakon provere `.bin` fajla, postavite ga na vašu MicroSD karticu, zatim je ubacite u Passport. Passport istraživač fajlova će se otvoriti. Izaberite fajl `vN.N.N-passport.bin`.


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


Vaš pasoš će sada generate vaš "*Rezervni Kod*". Ovo je niz brojeva koji se mogu koristiti za dešifrovanje rezervne kopije vašeg Wallet sačuvane na MicroSD. Ovaj sistem rezervne kopije, specifičan za Foundation uređaje, predstavlja dodatnu rezervnu kopiju vašoj Mnemonic frazi, ali nije kompatibilan sa drugim Bitcoin softverom.


Ako odlučite da koristite ovaj "*Rezervni Kod*", obavezno ga čuvajte na drugom mestu od vaše MicroSD kartice koja sadrži šifrovanu rezervnu kopiju vašeg Wallet. Međutim, možete odlučiti da ne koristite ovaj sistem ako smatrate da je dobra rezervna kopija vaše Mnemonic fraze dovoljna.


![Image](assets/fr/31.webp)


Unesite svoj "*Backup Code*" da potvrdite da ste ga ispravno sačuvali.


![Image](assets/fr/32.webp)


Ako je MicroSD umetnut, šifrovana rezervna kopija vašeg Wallet je tamo sačuvana.


![Image](assets/fr/33.webp)


Vaš pasoš će prikazati vašu 12-rečnu Mnemonic frazu. Ova Mnemonic vam daje pun, neograničen pristup svim vašim bitkoinima. Svako ko poseduje ovu frazu može ukrasti vaša sredstva, čak i bez fizičkog pristupa vašem pasošu.


Fraza od 12 reči vraća pristup vašim bitkoinima u slučaju gubitka, krađe ili oštećenja vašeg Pasporta. Stoga je veoma važno da je pažljivo sačuvate i skladištite na sigurnom mestu.


Možete ga napisati na kartonu koji je isporučen u kutiji, ili za dodatnu sigurnost, preporučujem graviranje na bazi od nerđajućeg čelika kako biste ga zaštitili od požara, poplave ili urušavanja.


Kliknite na dugme za potvrdu da vidite vašu Mnemonic frazu.


![Image](assets/fr/34.webp)


Za više informacija o pravilnom načinu čuvanja i upravljanja vašom Mnemonic frazom, toplo preporučujem da pratite ovaj drugi vodič, posebno ako ste početnik:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

naravno, nikada ne smete deliti ove reči na Internetu, kao što ja radim u ovom uputstvu. Ovaj uzorak Wallet će biti korišćen samo na Testnet i biće obrisan na kraju uputstva.**_


Napravite fizičku rezervnu kopiju ove rečenice.


![Image](assets/fr/35.webp)


Vaš pasoš je uspešno konfigurisan. Kliknite na dugme za potvrdu da nastavite.


![Image](assets/fr/36.webp)


## Otkrivanje menija


Vaš pasoš Interface ima tri glavna menija:




- "*Nalog*";
- "*Više*";
- "*Postavke*".


Da biste se kretali između ovih menija, koristite strelice levo i desno na upravljačkoj tabli.


### Meni *Nalog*


U meniju "*Account*" pronaći ćete glavne funkcije vašeg Bitcoin Wallet. Možete potpisati transakciju ili putem kamere ili putem MicroSD porta.


![Image](assets/fr/37.webp)


Podmeni "*Account Tools*" nudi opcije kao što su verifikacija Address, potpisivanje poruke ili konsultovanje adresa u vašem Wallet.


![Image](assets/fr/38.webp)


U podmeniju "*Manage Account*", možete povezati svoj Bitcoin Wallet sa softverom za upravljanje Wallet (koji ćemo obraditi u narednim koracima ovog vodiča), ili pregledati i preimenovati svoj nalog.


![Image](assets/fr/39.webp)


### Više" meni


U meniju "*Više*", možete kreirati novi nalog na vašem Wallet, povezan sa istom Mnemonic frazom.


![Image](assets/fr/40.webp)


Takođe možete uneti BIP39 passphrase (pogledajte sledeći odeljak) ili koristiti privremeni seed.


![Image](assets/fr/41.webp)


### Meni "Settings"


U meniju "*Settings*" pronaći ćete sve postavke za Wallet i uređaj.


![Image](assets/fr/42.webp)


Podmeni "*Device*" vam daje opcije za prilagođavanje osvetljenosti ekrana, postavljanje kašnjenja pre automatskog zaključavanja, promenu PIN koda ili preimenovanje uređaja.


![Image](assets/fr/43.webp)


Podmeni "*Backup*" omogućava vam da izvezete svoju šifrovanu Wallet rezervnu kopiju, proverite validnost postojeće rezervne kopije ili ponovo pronađete svoj "*Backup Code*".


![Image](assets/fr/44.webp)


Podmeni "*Firmware*" služi za ažuriranje firmvera vašeg Passport uređaja. Preporučujemo da redovno vršite ova ažuriranja kako biste iskoristili najnovije ispravke i funkcije.


![Image](assets/fr/45.webp)


Podmeni "*Bitcoin*" vam omogućava da promenite prikazanu jedinicu (BTC ili satoshi), upravljate mogućim Multisig Wallet, ili pređete na režim "*Testnet*".


![Image](assets/fr/46.webp)


U "*Advanced*" možete pregledati reči vaše Mnemonic fraze, izvršiti radnje na umetnutoj MicroSD kartici, resetovati vaš Passport na fabrička podešavanja ili izvršiti proveru autentičnosti, kao što je prethodno urađeno.


![Image](assets/fr/47.webp)


Možete aktivirati "*Security Words*", funkciju koja dodaje Layer sigurnosti prikazivanjem dve specifične reči prilikom otključavanja uređaja nakon unosa prva četiri broja PIN koda. Ove reči, koje se čuvaju tokom konfiguracije, osiguravaju da Passport nije zamenjen ili izmenjen. U slučaju bilo kakvog neslaganja kasnije, savetujemo vam da ne koristite uređaj. Savetujem vam da aktivirate ovu opciju kako biste sprečili većinu rizika fizičkog kompromitovanja uređaja.


![Image](assets/fr/48.webp)


Konačno, podmeni "*Extensions*" vam omogućava aktiviranje funkcija specifičnih za određene upotrebe uređaja, kao što je Whirlpool CoinJoin protokol.


![Image](assets/fr/49.webp)


## Dodaj BIP39 passphrase


Pre nego što nastavite, ako želite, možete dodati BIP39 passphrase. BIP39 passphrase je opcionalna lozinka koju možete slobodno izabrati, i koja se dodaje vašoj Mnemonic frazi kako bi se pojačala Wallet sigurnost. Sa ovom funkcijom omogućen, pristup vašem Bitcoin Wallet će zahtevati i Mnemonic i passphrase. Bez bilo kojeg, bilo bi nemoguće povratiti Wallet.


Pre nego što konfigurišete ovu opciju na vašem Passport-u, preporučuje se da pročitate ovaj članak kako biste u potpunosti razumeli teorijski rad passphrase i izbegli greške koje bi mogle dovesti do gubitka vaših bitkoina:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Da biste ga aktivirali, idite na meni "*Više*" i kliknite na "*Unesite passphrase*".


![Image](assets/fr/50.webp)


Unesite svoj passphrase koristeći aA1 tastaturu i obavezno ga sačuvajte jedan ili više puta na fizičkom mediju (papir ili metal). Za primer koristim veoma slab passphrase, ali vi treba da izaberete jak, nasumičan passphrase, uključujući sve tipove karaktera i dovoljno dug (kao jaka lozinka).


![Image](assets/fr/51.webp)


Imajte na umu da su BIP39 lozinke osetljive na velika i mala slova, kao i na tipografske greške. Ako unesete passphrase koji je malo drugačiji od onog koji je prvobitno konfigurisan, Passport neće prijaviti grešku, ali će generisati drugi skup kriptografskih ključeva koji neće biti oni u vašem početnom Wallet.


Važno je, dakle, prilikom konfigurisanja, negde zabeležiti otisak prsta glavnog ključa koji će vam biti dat u sledećem koraku. Na primer, sa mojom passphrase `Plan B Network`, otisak prsta mog glavnog ključa je `745D526B`.


![Image](assets/fr/52.webp)


Svaki put kada otključate svoj Passport, moraćete da se vratite na ovaj meni da unesete svoj passphrase i primenite ga na svoj Wallet. Passport ne čuva passphrase.


Svaki put kada otključate, nakon što zapišete passphrase, proverite na ovom ekranu za potvrdu da li je otisak prsta isti kao onaj koji ste zapisali tokom konfiguracije. Ako jeste, vaš passphrase je tačan i pristupate ispravnom Bitcoin Wallet. Ako nije, nalazite se na pogrešnom Wallet i morate pokušati ponovo, pazeći da ne napravite greške pri unosu.


Pre nego što primite svoje prve bitkoine na vaš Wallet, **snažno vam savetujem da izvedete test praznog oporavka**. Zapišite neke referentne informacije, kao što su vaš xpub ili prvi prijemni Address, zatim obrišite vaš Wallet na Passport-u dok je još uvek prazan (`Settings -> Advanced -> Erase Passport`). Zatim pokušajte da obnovite vaš Wallet koristeći vaše papirne rezervne kopije Mnemonic fraze i bilo kojeg passphrase. Proverite da li informacije o kolačićima generisane nakon obnove odgovaraju onima koje ste prvobitno zapisali. Ako odgovaraju, možete biti sigurni da su vaše papirne rezervne kopije pouzdane. Da biste saznali više o tome kako izvesti test oporavka, molimo vas da pogledate ovaj drugi vodič :


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

![Image](assets/fr/53.webp)


## Konfigurisanje Wallet na Sparrow Wallet


U ovom vodiču, pokazaću vam naprednu upotrebu Passport-a sa Sparrow Wallet. Međutim, ovaj Hardware Wallet je takođe kompatibilan sa Envoy (aplikacija Foundation), Keeper, BlueWallet, Nunchuk, Specter, i mnogim drugima...


Počnite preuzimanjem i instaliranjem Sparrow Wallet [sa zvaničnog sajta](https://sparrowwallet.com/) na vašem računaru, ako to već niste učinili.


![Image](assets/fr/54.webp)


Obavezno proverite autentičnost i integritet softvera pre instalacije. Ako ne znate kako to da uradite, molimo vas da pogledate ovaj vodič:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Kada otvorite Sparrow Wallet, kliknite na karticu "*File*", zatim na "*New Wallet*".


![Image](assets/fr/55.webp)


Nazovite svoj Wallet, zatim kliknite na "*Create Wallet*".


![Image](assets/fr/56.webp)


Odaberite "*Airgapped Hardware Wallet*".


![Image](assets/fr/57.webp)


Kliknite na "*Skeniraj...*" pored opcije "*Pasoš*". Ovo će otvoriti vašu veb kameru.


![Image](assets/fr/58.webp)


Na vašem Hardware Wallet, idite na meni "*Account*", izaberite podmeni "*Manage Account*" i kliknite na "*Connect Wallet*".


![Image](assets/fr/59.webp)


Na padajućoj listi koja se pojavljuje, izaberite "*Sparrow*".


![Image](assets/fr/60.webp)


Zatim izaberite "*Single-sig*" za normalnu konfiguraciju, bez Multisig.


![Image](assets/fr/61.webp)


Odaberite opciju "*QR Code*".


![Image](assets/fr/62.webp)


Vaš pasoš će zatim generate dinamičke QR kodove. Koristite veb kameru vašeg računara da ih skenirate u Sparrow softver.


![Image](assets/fr/63.webp)


Trebalo bi da sada vidite vaš xpub i otisak prsta glavnog ključa, koji bi trebalo da se poklapa sa onim prikazanim na vašem Passport-u kada unesete vaš passphrase. Kliknite na dugme "*Apply*".


![Image](assets/fr/64.webp)


Postavite jaku lozinku kako biste osigurali pristup vašem Sparrow Wallet. Ova lozinka će zaštititi vaše javne ključeve, adrese, oznake i istoriju transakcija od neovlašćenog pristupa. Dobro je sačuvati ovu lozinku u menadžeru lozinki, kako je ne biste zaboravili.


![Image](assets/fr/65.webp)


Vaš pasoš zatim traži da skenirate prvu prijemnicu Address kako biste potvrdili da je uvoz uspešan.


![Image](assets/fr/66.webp)


U Sparrow-u, idite na karticu "*Receive*" i skenirajte QR kod prvog Address.


![Image](assets/fr/67.webp)


Ako je operacija uspešna, vaš pasoš će prikazati "*Verifikovano*".


![Image](assets/fr/68.webp)


Ovo potvrđuje da je uvoz bio uspešan.


![Image](assets/fr/69.webp)


## Primite bitkoine


Sada kada je vaš Passport postavljen, spremni ste da primite svoj prvi Sats na vašem novom Bitcoin Wallet. Da biste to uradili, na Sparrow-u kliknite na meni "*Receive*".


![Image](assets/fr/70.webp)


Sparrow će prikazati prvi prazan račun Address u vašem Wallet. Možete dodati oznaku.


![Image](assets/fr/71.webp)


Pre nego što ga upotrebimo, proverićemo Address na ekranu Passport-a da bismo se uverili da pripada našem Bitcoin Wallet. Na Sparrow-u, možete uvećati QR kod Address klikom na njega ako je potrebno. U meniju "*Account*" vašeg Passport-a, izaberite "*Account Tools*".


![Image](assets/fr/72.webp)


Kliknite na "*Verify Address*", zatim skenirajte QR kod prikazan na Sparrow Wallet.


![Image](assets/fr/73.webp)


Proverite da se Address prikazan na Pasoš tačno poklapa sa onim prikazanim na Sparrow, i da se pojavi "*Verified*".


![Image](assets/fr/74.webp)


Sada ga možete koristiti za primanje bitkoina. Kada se transakcija emituje na mreži, pojaviće se na Sparrow. Sačekajte dok ne dobijete dovoljno potvrda da biste smatrali transakciju konačnom.


![Image](assets/fr/75.webp)


## Pošalji bitkoine


Sada kada imate nekoliko Sats u vašem Wallet, možete ih takođe poslati. Da biste to uradili, kliknite na meni "*UTXOs*".


![Image](assets/fr/76.webp)


Odaberite UTXO-ove koje želite koristiti kao ulaze za ovu transakciju, zatim kliknite na "*Pošalji odabrano*".


![Image](assets/fr/77.webp)


Unesite primaoca Address, oznaku koja će vas podsetiti na svrhu transakcije i iznos koji želite poslati ovom Address.


![Image](assets/fr/78.webp)


Prilagodite stopu naknade prema trenutnim tržišnim uslovima, zatim kliknite na "*Create Transaction*".


![Image](assets/fr/79.webp)


Proverite da su svi parametri transakcije tačni, zatim kliknite na "*Finalize Transaction for Signing*".


![Image](assets/fr/80.webp)


Kliknite na "*Prikaži QR*" da biste prikazali PSBT (*Partially Signed Bitcoin Transaction*). Sparrow je napravio transakciju, ali joj još uvek nedostaju potpisi za otključavanje bitkoina korišćenih u ulazu. Ove potpise može izvršiti samo Passport, koji hostuje vaš seed dajući pristup privatnim ključevima potrebnim za potpisivanje transakcije.


![Image](assets/fr/81.webp)


Na vašem Pasoš-u, pristupite meniju "*Nalog*" i kliknite na "*Prijava putem QR koda*".


![Image](assets/fr/82.webp)


Skeniraj PSBT (*Partially Signed Bitcoin Transaction*) prikazan na Sparrow Wallet.


![Image](assets/fr/83.webp)


Potvrdite da su prijemnik Address i poslata suma tačni, zatim pritisnite dugme za potvrdu.


![Image](assets/fr/84.webp)


Proveri Exchange Address. U mom primeru, nema ih, jer transakcija uključuje jedan izlaz.


![Image](assets/fr/85.webp)


Uverite se da je naknada ona koju ste izabrali.


![Image](assets/fr/86.webp)


Ako su sve informacije tačne, kliknite na dugme za potvrdu da biste potpisali transakciju.


![Image](assets/fr/87.webp)


Na Sparrow Wallet, kliknite na "*Scan QR*" i skenirajte QR kod prikazan na vašem pasošu.


![Image](assets/fr/88.webp)


Vaša potpisana transakcija je sada spremna za emitovanje na Bitcoin mreži i uključivanje u blok od strane Miner. Ako je sve ispravno, kliknite na "*Broadcast Transaction*".


![Image](assets/fr/89.webp)


Vaša transakcija je emitovana i čeka potvrdu.


![Image](assets/fr/90.webp)


Čestitamo, sada znate kako da konfigurišete i koristite Passport. Ako ste smatrali da je ovaj vodič koristan, bio bih zahvalan ako biste ostavili Green palac ispod. Slobodno podelite ovaj članak na svojim društvenim mrežama. Hvala što delite!


Za dodatne informacije, pogledajte naš vodič o softveru Liana:


https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04