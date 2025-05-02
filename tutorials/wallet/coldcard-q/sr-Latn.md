---
name: COLDCARD Q
description: Postavljanje i korišćenje COLDCARD Q
---
![cover](assets/cover.webp)


Hardware Wallet je elektronski uređaj posvećen upravljanju i zaštiti privatnih ključeva Bitcoin Wallet. Za razliku od softverskih novčanika (ili Hot novčanika) instaliranih na mašinama opšte namene koje su često povezane na Internet, hardverski novčanici omogućavaju fizičku izolaciju privatnih ključeva, smanjujući rizik od piraterije i krađe.


Glavni cilj Hardware Wallet je da smanji funkcionalnost uređaja koliko god je to moguće kako bi se minimizirala njegova površina napada. Manja površina napada takođe znači manje potencijalnih vektora napada, tj. manje slabih tačaka u sistemu koje napadači mogu iskoristiti da bi dobili pristup bitcoinima.


Preporučljivo je koristiti Hardware Wallet za osiguranje vaših bitkoina, posebno ako držite velike količine, bilo u apsolutnoj vrednosti ili kao proporciju vaših ukupnih sredstava.


Hardverski novčanici se koriste zajedno sa Wallet softverom za upravljanje na računaru ili pametnom telefonu. Potonji upravlja kreiranjem transakcija, ali kriptografski potpis potreban da bi ove transakcije bile važeće obavlja se isključivo unutar Hardware Wallet. To znači da privatni ključevi nikada nisu izloženi potencijalno ranjivom okruženju.


Hardverski novčanici nude dvostruku zaštitu za korisnika: s jedne strane, štite vaše bitkoine od daljinskih napada držeći privatne ključeve van mreže, a s druge strane, generalno nude veću fizičku otpornost na pokušaje ekstrakcije ključeva. I upravo na osnovu ova 2 sigurnosna kriterijuma možemo suditi i klasifikovati različite modele na tržištu.


U ovom vodiču, želeo bih da vas upoznam sa jednim takvim rešenjem: **COLDCARD Q**.


---
Kako COLDCARD Q nudi mnoštvo funkcija, predlažem da njegovo korišćenje podelimo u 2 tutorijala. U ovom prvom tutorijalu, pogledaćemo početnu konfiguraciju i osnovne funkcije uređaja. Zatim, u drugom tutorijalu, razmotrićemo kako iskoristiti sve napredne opcije vašeg COLDCARD-a.


https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

---
## Predstavljamo COLDCARD Q


COLDCARD Q je Bitcoin-only Hardware Wallet razvijen od strane kanadske kompanije Coinkite, poznate po svojim prethodnim MK modelima. Q predstavlja njihov najnapredniji proizvod do sada i pozicioniran je kao ultimativni Bitcoin Hardware Wallet.


Što se tiče hardvera, COLDCARD Q je opremljen svim funkcijama potrebnim za optimalno korisničko iskustvo:




- Veliki LCD ekran pojednostavljuje navigaciju i rad;
- Puna QWERTY tastatura;
- Integrisana kamera za skeniranje QR kodova;
- Dva microSD slota ;
- Potpuno izolovana opcija napajanja putem tri AAA baterije (nisu uključene), ili putem USB-C kabla ;
- Dva Secure Elements od dva različita proizvođača za dodatnu sigurnost;
- Sposobnost komunikacije putem NFC-a.


Po mom mišljenju, COLDCARD Q ima samo dva nedostatka. Prvo, zbog svojih mnogih funkcija, prilično je glomazan, dimenzija skoro 13 cm dužine i 8 cm širine, što je skoro veličina malog pametnog telefona. Takođe je prilično debeo zbog odeljka za bateriju. Ako tražite manji, mobilniji Hardware Wallet, mnogo kompaktniji MK4 bi mogao biti bolja opcija. Drugi nedostatak je očigledno cena uređaja, koja iznosi **$239.99** na zvaničnom sajtu, tj. $72 više od MK4, što stavlja Q u direktnu konkurenciju sa premijum hardverskim novčanicima kao što su Ledger Flex ili Foundation's Passport.


![CCQ](assets/fr/001.webp)


Sa softverske strane, COLDCARD Q je jednako dobro opremljen kao i ostali uređaji kompanije Coinkite, sa nizom naprednih funkcija:




- Bacanje kockica do generate vaša sopstvena fraza za oporavak ;
- PIN kod ;
- Odbrojavanje do konačne blokade PIN-a ;
- BIP39 passphrase ;
- Konačni PIN za zaključavanje ;
- Odbrojavanje povezivanja ;
- SeedXOR;
- BIP85...


Ukratko, COLDCARD Q nudi poboljšano korisničko iskustvo u odnosu na MK4 i može biti idealan za korisnike srednjeg do naprednog nivoa koji traže veću jednostavnost korišćenja.


COLDCARD Q je dostupan za prodaju [na zvaničnom Coinkite vebsajtu](https://store.coinkite.com/store/coldcard). Takođe se može kupiti od prodavca.


## Priprema tutorijala


Kada primite svoj COLDCARD, prvi korak je da pregledate pakovanje kako biste se uverili da nije otvoreno. Ako je pakovanje oštećeno, to može ukazivati na to da je Hardware Wallet kompromitovan i možda nije originalan.


![CCQ](assets/fr/002.webp)


Kada otvorite kutiju, trebalo bi da pronađete sledeće stavke:




- COLDCARD Q u zapečaćenoj vrećici;
- Kartica za beleženje vaše Mnemonic fraze.


![CCQ](assets/fr/003.webp)


Proverite da torba nije bila otvorena ili oštećena. Takođe proverite da li se broj na vašoj torbi poklapa sa brojem na papiru unutar torbe. Sačuvajte ovaj broj za buduću upotrebu.


![CCQ](assets/fr/004.webp)


Ako više volite da napajate svoj COLDCARD bez povezivanja sa računarom (air-gap), umetnite tri AAA baterije u zadnji deo uređaja. Alternativno, možete ga povezati sa računarom putem USB-C kabla.


![CCQ](assets/fr/005.webp)


Za ovaj vodič, takođe će vam trebati Sparrow Wallet da upravljate vašim Bitcoin Wallet na vašem računaru. Preuzmite [Sparrow Wallet](https://sparrowwallet.com/download/) sa zvaničnog sajta. Snažno vam savetujem da proverite i njegovu autentičnost (sa GnuPG) i integritet (preko Hash) pre nego što nastavite sa instalacijom. Ako ne znate kako to da uradite, pratite ovaj vodič:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Izbor PIN koda


Sada možete uključiti svoj COLDCARD pritiskom na dugme u gornjem levom uglu.


![CCQ](assets/fr/006.webp)


Pritisnite dugme "*ENTER*" da prihvatite uslove korišćenja.


![CCQ](assets/fr/007.webp)


Vaš COLDCARD Q će zatim prikazati broj na vrhu ekrana. Uverite se da se ovaj broj poklapa sa onim na zapečaćenoj vrećici i na komadu plastike unutar vrećice. Ovo osigurava da vaš paket nije bio otvoren između vremena kada ga je Coinkite zapakovao i vremena kada ste ga vi otvorili. Pritisnite "*ENTER*" da nastavite.


![CCQ](assets/fr/008.webp)


Idite na meni "*Choose PIN Code*" i potvrdite sa dugmetom "*ENTER*".


![CCQ](assets/fr/009.webp)


Ovaj PIN kod se koristi za otključavanje vašeg COLDCARD-a. Stoga je zaštita protiv neovlašćenog fizičkog pristupa. Ovaj PIN kod nije uključen u derivaciju kriptografskih ključeva vašeg Wallet. Dakle, čak i bez pristupa ovom PIN kodu, posedovanje vaše Mnemonic fraze omogućiće vam da ponovo dobijete pristup vašim bitcoinima.


PIN kodovi za COLDCARD su podeljeni na dva dela: prefiks i sufiks, od kojih svaki može sadržati između 2 i 6 cifara, što ukupno čini od 4 do 12 cifara. Kada otključavate svoj COLDCARD, prvo ćete morati da unesete prefiks, nakon čega će vam uređaj prikazati 2 reči. Zatim unesite sufiks. Ove dve reči će vam biti date tokom ovog koraka konfiguracije i treba ih pažljivo sačuvati, jer će vam biti potrebne svaki put kada otključavate svoj COLDCARD. Ako se dve reči prikazane tokom otključavanja poklapaju sa onima koje ste sačuvali tokom konfiguracije, to će potvrditi da vaš uređaj nije kompromitovan od poslednje upotrebe.


Kliknite ponovo na "*Izaberite PIN*"


![CCQ](assets/fr/010.webp)


Potvrdite da ste pročitali upozorenja.


![CCQ](assets/fr/011.webp)


Sada ćete izabrati svoj PIN kod. Preporučujemo dug, nasumičan PIN kod. Uverite se da ovaj kod čuvate na drugom mestu od mesta gde je vaša COLDCARD kartica. Možete koristiti karticu koja je priložena u vašem paketu da zabeležite ovaj kod.


Unesite prefiks po vašem izboru, zatim pritisnite dugme "*ENTER*" da potvrdite prvi deo PIN koda.


![CCQ](assets/fr/012.webp)


Dve reči protiv fišinga će zatim biti prikazane na vašem ekranu. Sačuvajte ih pažljivo za buduću upotrebu. Možete koristiti karticu uključenu u vaš paket da ih zapišete.


![CCQ](assets/fr/013.webp)


Zatim unesite drugi deo svog PIN koda i pritisnite "*ENTER*".


![CCQ](assets/fr/014.webp)


Potvrdite svoj PIN tako što ćete ga uneti drugi put, proveravajući da se dve anti-phishing reči podudaraju sa onima koje ste ranije sačuvali.


![CCQ](assets/fr/015.webp)


Od sada, svaki put kada otključate svoj COLDCARD, zapamtite da proverite validnost dve reči protiv phishinga koje se pojavljuju na ekranu nakon što unesete prefiks svog PIN koda.


## Ažuriranje firmvera


Kada prvi put koristite svoj uređaj, važno je proveriti i ažurirati firmver. Da biste to uradili, pristupite meniju "*Advanced/Tools*".


![CCQ](assets/fr/016.webp)


**Važno:** Ako planirate da nadogradite svoj firmware i ovo nije vaš prvi put da koristite COLDCARD (tj. već imate Wallet kreiran na COLDCARD-u), uverite se da imate svoju Mnemonic frazu i da je funkcionalna (kao i opcionalnu passphrase, ako je primenljivo). Ovo je važno kako biste izbegli gubitak svojih bitkoina u slučaju problema tokom ažuriranja uređaja.


Odaberite "*Upgrade Firmware*".


![CCQ](assets/fr/017.webp)


Odaberite "*Prikaži verziju*".


![CCQ](assets/fr/018.webp)


Možete proveriti trenutnu verziju firmvera vašeg COLDCARD-a. Na primer, u mom slučaju, verzija je "*1.2.3Q*".


![CCQ](assets/fr/019.webp)


Proverite [na zvaničnom COLDCARD sajtu](https://coldcard.com/downloads) da li je dostupna novija verzija. Kliknite na "*Download*" da preuzmete novi firmware.


![CCQ](assets/fr/020.webp)


U ovom trenutku, snažno preporučujemo proveru integriteta i autentičnosti preuzetog firmvera. Da biste to uradili, preuzmite [dokument koji sadrži hešove svih verzija, potpisan od strane programera](https://raw.githubusercontent.com/Coldcard/firmware/master/releases/signatures.txt), verifikujte potpis sa [javnim ključem programera](https://keybase.io/dochex), i uverite se da se Hash naznačen u potpisanom dokumentu poklapa sa onim firmverom preuzetim sa sajta. Ako je sve ispravno, možete nastaviti sa ažuriranjem.


Ako niste upoznati sa ovim procesom verifikacije, preporučujem da pratite ovaj vodič:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Uzmite microSD karticu i prenesite firmware fajl (dokument u `.dfu`) na nju. Ubacite microSD karticu u jedan od portova vašeg COLDCARD-a.


![CCQ](assets/fr/021.webp)


Zatim, u meniju za ažuriranje firmvera, izaberite "*From MicroSD*".


![CCQ](assets/fr/022.webp)


Izaberite datoteku koja odgovara firmveru.


![CCQ](assets/fr/023.webp)


Potvrdite svoj izbor pritiskom na dugme "*ENTER*".


![CCQ](assets/fr/024.webp)


Molimo sačekajte dok se firmver ažurira.


![CCQ](assets/fr/025.webp)


Kada se ažuriranje završi, unesite svoj PIN kod da otključate uređaj.


![CCQ](assets/fr/026.webp)


Vaš firmver je sada ažuriran.


## COLDCARD Q parametri


Ako želite, možete istražiti postavke vašeg COLDCARD-a pristupom meniju "*Settings*".


![CCQ](assets/fr/027.webp)


U ovom meniju ćete pronaći razne opcije prilagođavanja, kao što su podešavanje osvetljenosti ekrana ili izbor podrazumevane jedinice mere.


![CCQ](assets/fr/028.webp)


Pogledaćemo ostala napredna podešavanja u sledećem vodiču:


https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

## Kreiranje Bitcoin Wallet


Sada je vreme za generate novi Bitcoin Wallet! Da biste to uradili, potrebno je da kreirate Mnemonic frazu. Na Coldcard-u, imate tri metode za generisanje ove fraze:




- Koristite samo interni generator slučajnih brojeva (TRNG);
- Koristite kombinaciju TRNG i bacanja kockica da dodate entropiju;
- Koristite samo bacanja kockica.


**Za početnike i korisnike srednjeg nivoa, preporučujemo korišćenje samo COLDCARD-ovog internog generatora slučajnih brojeva**


Ne preporučujem opciju samo kockica, jer loša izvedba može dovesti do rečenice sa nedovoljnom entropijom, ugrožavajući sigurnost vašeg Wallet.


Međutim, najbolja opcija je sigurno druga, koja kombinuje korišćenje TRNG sa spoljnim izvorom entropije. Ova metoda garantuje minimalnu entropiju ekvivalentnu onoj samog TRNG, i dodaje dodatni nivo sigurnosti u slučaju mogućeg kvara internog generatora (namernog ili ne). Odabirom ove opcije, koja kombinuje TRNG i bacanje kockica, imate veću kontrolu nad generisanjem rečenice, bez povećanja rizika u slučaju lošeg izvršenja sa vaše strane.


Kliknite na "*New seed Words*".


![CCQ](assets/fr/029.webp)


Možete izabrati dužinu svoje rečenice. Preporučujem da se odlučite za rečenicu od 12 reči, jer je manje složena za upravljanje i nudi jednaku Wallet sigurnost kao i rečenica od 24 reči.


![CCQ](assets/fr/030.webp)


COLDCARD će zatim prikazati vašu TRNG-generisanu frazu za oporavak. Ako želite da dodate dodatnu eksternu entropiju, pritisnite taster "*4*".


![CCQ](assets/fr/031.webp)


Ovo će vas odvesti na stranicu gde možete dodati entropiju bacanjem kockica. Napravite što više bacanja (preporučuje se minimum od 50, ali manje nije veliki problem jer već koristite entropiju TRNG-a), i zabeležite rezultate pomoću tastera "*1*" do "*6*". Kada završite, pritisnite "*ENTER*" da potvrdite.


![CCQ](assets/fr/032.webp)


Nova fraza Mnemonic će biti prikazana, na osnovu entropije koju ste upravo pružili i one TRNG-a.


**Upozorenje: Ovaj Mnemonic daje potpuni, neograničeni pristup svim vašim bitcoinima**. Svako ko poseduje ovu frazu može ukrasti vaša sredstva, čak i bez fizičkog pristupa vašoj COLDCARD. Fraza od 12 reči vraća pristup vašim bitcoinima u slučaju gubitka, krađe ili oštećenja vaše COLDCARD. Stoga je veoma važno da je pažljivo sačuvate i skladištite na sigurnom mestu.


Možete ga zapisati na karton koji ste dobili uz vaš COLDCARD, ili za dodatnu sigurnost, preporučujem da ga ugravirate na nosač od nerđajućeg čelika kako biste ga zaštitili od rizika od požara, poplave ili urušavanja. U svakom slučaju, nikada ga ne čuvajte na digitalnom mediju, inače biste mogli izgubiti svoje bitkoine.


Napišite reči prikazane na ekranu na fizički medij po vašem izboru. U zavisnosti od vaše bezbednosne strategije, možete razmotriti pravljenje nekoliko potpunih fizičkih kopija rečenice (ali pre svega, nemojte je deliti). Važno je da reči budu numerisane i u sekvencijalnom redosledu.


Očigledno, **nikada ne smete deliti ove reči** na Internetu, za razliku od ovog tutorijala. Ovaj uzorak Wallet će biti korišćen samo na Testnet i biće obrisan na kraju tutorijala.


Nakon što napišete reči, pritisnite "*ENTER*".


![CCQ](assets/fr/033.webp)


Da biste bili sigurni da ste ispravno sačuvali svoju frazu, sistem će vas zamoliti da potvrdite određene reči. Izaberite broj koji odgovara svakoj reči na tastaturi.


![CCQ](assets/fr/034.webp)


Vaš Wallet je sada kreiran! U gornjem desnom uglu ekrana možete videti otisak vašeg glavnog privatnog ključa. Pritisnite "*ENTER*".


![CCQ](assets/fr/035.webp)


Sada pristupate glavnom meniju vašeg COLDCARD-a.


![CCQ](assets/fr/036.webp)


## Postavljanje novog Wallet na Sparrow


Postoji nekoliko opcija za uspostavljanje komunikacije između Sparrow Wallet softvera i vašeg COLDCARD-a. Najjednostavnija je korišćenje USB-C kabla. Međutim, po defaultu, vaš COLDCARD ima onemogućenu komunikaciju putem kabla i NFC-a. Da biste ih ponovo aktivirali, idite na "*Settings*", zatim "*Hardware On/Off*", i aktivirajte željenu opciju komunikacije.


![CCQ](assets/fr/037.webp)


Ako želite da vaš COLDCARD bude potpuno izolovan od računara, možete se odlučiti za indirektnu komunikaciju "air-gap", koristeći QR kodove ili microSD karticu. Ovo je metoda koju ćemo koristiti u ovom vodiču.


Idite na "*Advanced/Tools*".


![CCQ](assets/fr/038.webp)


Odaberite "*Export Wallet*".


![CCQ](assets/fr/039.webp)


Zatim izaberite "*Sparrow Wallet*".


![CCQ](assets/fr/040.webp)


Pritisnite "*ENTER*" da generate konfiguracionu datoteku.


![CCQ](assets/fr/041.webp)


Zatim izaberite kako da pošaljete ovaj fajl Sparrow-u. U ovom primeru, ubacio sam microSD u slot "*A*", tako da ću izabrati dugme "*1*". Takođe možete prikazati informacije kao QR kod na ekranu vašeg COLDCARD-a pritiskom na dugme "*QR*", i skenirati ovaj QR kod pomoću veb kamere vašeg računara.


![CCQ](assets/fr/042.webp)


Pokreni Sparrow Wallet i preskoči uvodne stranice kako bi stigao do glavnog ekrana. Uveri se da si pravilno povezan na čvor proverom prekidača u donjem desnom uglu ekrana.


![CCQ](assets/fr/043.webp)


Preporučuje se da koristite sopstveni Bitcoin čvor. Za ovaj tutorijal, koristim javni čvor (žuti), jer sam na Testnet, ali za produkcijsku upotrebu, najbolje je koristiti Bitcoin Core lokalno (Green) ili Electrum server na udaljenom čvoru (plavi).


Pristupite meniju "*File*" i izaberite "*New Wallet*".


![CCQ](assets/fr/044.webp)


Nazovite svoj Wallet i kliknite na "*Create Wallet*".


![CCQ](assets/fr/045.webp)


U padajućem meniju "*Script Type*", izaberite tip skripte koji će obezbediti vaše bitkoine.


![CCQ](assets/fr/046.webp)


Kliknite na "*Airgapped Hardware Wallet*".


![CCQ](assets/fr/047.webp)


Pod karticom "*Coldcard*" kliknite na "*Scan...*" ako planirate da skenirate QR kod prikazan na vašem COLDCARD-u, ili na "*Import File...*" da uvezete fajl sa microSD kartice (ovo je `.json` fajl).


![CCQ](assets/fr/048.webp)


Nakon uvoza, proverite da li se "*Master fingerprint*" prikazan na Sparrow poklapa sa onim prikazanim na vašem COLDCARD-u. Potvrdite kreiranje klikom na "*Apply*".


![CCQ](assets/fr/049.webp)


Postavite jaku lozinku kako biste osigurali pristup vašem Sparrow Wallet. Ova lozinka će zaštititi vaše javne ključeve, adrese, oznake i istoriju transakcija od neovlašćenog pristupa.


Dobro je sačuvati ovu lozinku kako je ne biste zaboravili (npr. u menadžeru lozinki).


![CCQ](assets/fr/050.webp)


Vaš Wallet je sada postavljen na Sparrow Wallet.


![CCQ](assets/fr/051.webp)


Pre nego što primite svoje prve bitkoine u vaš Wallet, **snažno vam savetujem da izvršite test praznog oporavka**. Zapišite neke referentne informacije, kao što je vaš xpub, zatim resetujte vaš COLDCARD Q dok je Wallet još uvek prazan. Zatim pokušajte da obnovite vaš Wallet na COLDCARD koristeći vaše papirne rezervne kopije. Proverite da li se xpub generisan nakon obnove poklapa sa onim koji ste prvobitno zapisali. Ako se poklapa, možete biti sigurni da su vaše papirne rezervne kopije pouzdane.


Da biste saznali više o tome kako izvesti test oporavka, predlažem da pogledate ovaj drugi vodič:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Primite bitkoine


Da biste primili svoje prve bitkoine, počnite tako što ćete uključiti i otključati svoj COLDCARD.


![CCQ](assets/fr/052.webp)


Na Sparrow Wallet, kliknite na karticu "*Receive*".


![CCQ](assets/fr/053.webp)


Pre nego što upotrebite Address koji predlaže Sparrow Wallet, proverite ga na vašem COLDCARD ekranu. Ova praksa vam omogućava da potvrdite da Address prikazan na Sparrow nije lažan, i da Hardware Wallet zaista poseduje privatni ključ potreban za kasnije trošenje bitcoina osiguranih ovim Address. Ovo vam pomaže da izbegnete nekoliko vrsta napada.


Da biste izvršili ovu proveru, kliknite na meni "*Address Explorer*" na COLDCARD-u.


![CCQ](assets/fr/054.webp)


Odaberite tip skripte koju koristite na Sparrow-u. U mom slučaju, to je SegWit P2WPKH. Kliknem na to.


![CCQ](assets/fr/055.webp)


Zatim možete videti vaše različite izvedene adrese po redu.


![CCQ](assets/fr/056.webp)


Proveri sa Sparrow da li se Address poklapa. U mom slučaju, Address sa putanjom derivacije `m/84'/1'/0'/0/0` je zaista `tb1qwfwwvzssep4wyjg3vsgezmwa037ehvd4fhmjvr` i na Sparrow i na COLDCARD.


![CCQ](assets/fr/057.webp)


Još jedan način da verifikujete Ownership ovog Address je da skenirate njegov QR kod direktno na Sparrow sa vašeg COLDCARD-a. Na početnom ekranu vašeg COLDCARD-a, izaberite "*Scan Any QR Code*". Takođe možete koristiti taster "*QR*" na tastaturi.


![CCQ](assets/fr/058.webp)


Skenirajte QR kod Address prikazan na Sparrow Wallet.


![CCQ](assets/fr/059.webp)


Uverite se da se Address prikazan na vašem COLDCARD-u poklapa sa onim prikazanim na Sparrow-u. Zatim pritisnite dugme "*1*".


![CCQ](assets/fr/060.webp)


Address je tako uspešno potvrđen.


![CCQ](assets/fr/061.webp)


Sada možete dodati "*Label*" da opišete izvor bitkoina koji će biti osiguran ovim Address. Ovo je dobra praksa koja vam omogućava bolje upravljanje vašim UTXO-ima.


![CCQ](assets/fr/062.webp)


Za više informacija o etiketiranju, preporučujem i ovaj drugi vodič:


https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Zatim možete koristiti ovaj Address za primanje bitkoina.


![CCQ](assets/fr/063.webp)


## Pošalji bitkoine


Sada kada ste primili svoj prvi Sats u vašem COLDCARD-osiguranom Wallet, možete ih i potrošiti!


Kao i uvek, počnite tako što ćete uključiti i otključati vaš COLDCARD Q, zatim otvorite Sparrow Wallet i idite na karticu "*Send*" da pripremite novu transakciju.


![CCQ](assets/fr/064.webp)


Ako želite da "kontrolišete novčiće", tj. da specifično izaberete koje UTXO-ove želite da potrošite u transakciji, idite na karticu "*UTXOs*". Izaberite UTXO-ove koje želite da potrošite, zatim kliknite na "*Send Selected*". Bićete preusmereni na isti ekran u kartici "*Send*", ali sa vašim već izabranim UTXO-ovima za transakciju.


![CCQ](assets/fr/065.webp)


Unesite odredište Address. Takođe možete uneti više adresa klikom na dugme "*+ Dodaj*".


![CCQ](assets/fr/066.webp)


Napišite "*Oznaku*" da biste zapamtili svrhu ovog troška.


![CCQ](assets/fr/067.webp)


Izaberite iznos koji će biti poslat na ovaj Address.


![CCQ](assets/fr/068.webp)


Prilagodite stopu naknade vaše transakcije prema trenutnom tržištu.


![CCQ](assets/fr/069.webp)


Proverite da su svi parametri vaše transakcije tačni, zatim kliknite na "*Create Transaction*".


![CCQ](assets/fr/070.webp)


Ako vam sve odgovara, kliknite na "*Finalize Transaction for Signing*".


![CCQ](assets/fr/071.webp)


Kada izgradite svoju transakciju u Sparrow-u, vreme je da je potpišete sa vašim COLDCARD-om. Da biste preneli PSBT (nepotpisanu transakciju) na vaš uređaj, imate nekoliko opcija. Ako je omogućeno prenos podataka putem kabla, možete poslati transakciju direktno putem USB-C veze, baš kao i sa bilo kojim drugim Hardware Wallet. U tom slučaju, u Sparrow-u, morate kliknuti na dugme "*Sign*" u donjem desnom uglu. U mom primeru, ovo dugme je blokirano jer COLDCARD nije povezan kablom.


![CCQ](assets/fr/072.webp)


Ako želite da održite "air-gap" vezu bez direktnog kontakta između Hardware Wallet i vašeg računara, imate 2 opcije. Prva, i složenija, je korišćenje microSD kartice. Ubacite microSD karticu u vaš računar, zabeležite transakciju putem dugmeta "*Save Transaction*" na Sparrow-u, zatim prenesite ovu karticu u port na vašem COLDCARD-u.


![CCQ](assets/fr/073.webp)


Zatim pristupite meniju "*Ready To Sign*".


![CCQ](assets/fr/074.webp)


Pregledajte detalje transakcije na vašem COLDCARD-u, uključujući primanje Address, poslatu sumu i naknadu za transakciju.


![CCQ](assets/fr/075.webp)


Ako je sve ispravno, pritisnite dugme "*ENTER*" da potpišete transakciju.


![CCQ](assets/fr/076.webp)


Zatim vratite microSD u vaš računar i na Sparrow-u kliknite na "*Load Transaction*" da učitate potpisanu transakciju sa microSD-a. Tada ćete moći da izvršite konačnu proveru pre nego što je otpremite na Bitcoin mrežu.


![CCQ](assets/fr/077.webp)


Drugi metod potpisivanja sa vašim COLDCARD u Air-Gap, koji je mnogo jednostavniji od metode sa microSD, jeste skeniranje PSBT direktno putem kamere uređaja. Na Sparrow, izaberite "*Show QR*".


![CCQ](assets/fr/078.webp)


Na COLDCARD-u, izaberite "*Scan Any QR Code*". Takođe možete koristiti taster "*QR*" na tastaturi.


![CCQ](assets/fr/079.webp)


Koristite kameru COLDCARD-a da skenirate QR kod prikazan na Sparrow-u.


![CCQ](assets/fr/080.webp)


Detalji transakcije će se ponovo pojaviti radi verifikacije. Pritisnite "*ENTER*" da potpišete ako ste zadovoljni.


![CCQ](assets/fr/081.webp)


Vaš COLDCARD će zatim prikazati potpisanu transakciju kao QR kod. Koristite veb kameru vašeg računara da skenirate ovaj QR kod tako što ćete odabrati "*Scan QR*" na Sparrow.


![CCQ](assets/fr/082.webp)


Vaša potpisana transakcija je sada vidljiva na Sparrow. Proverite još jednom da je sve ispravno, a zatim kliknite na "*Broadcast Transaction*" da biste je emitovali na Bitcoin mreži.


![CCQ](assets/fr/083.webp)


Možete pratiti svoju transakciju u kartici "*Transakcije*" na Sparrow Wallet.


![CCQ](assets/fr/084.webp)


Čestitamo, sada ste upoznati sa osnovnom upotrebom COLDCARD Q sa Sparrow Wallet!


Ako ste smatrali ovaj vodič korisnim, bio bih veoma zahvalan ako biste ostavili Green palac ispod. Slobodno podelite ovaj vodič na vašim društvenim mrežama. Hvala vam puno!


Takođe vam preporučujem da pogledate ovaj drugi vodič u kojem diskutujemo o naprednim opcijama COLDCARD Q :


https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0