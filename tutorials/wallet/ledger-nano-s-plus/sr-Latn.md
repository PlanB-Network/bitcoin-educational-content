---
name: Ledger Nano S Plus
description: Postavljanje i korišćenje Ledger Nano S Plus
---
![cover](assets/cover.webp)


Hardware Wallet je elektronski uređaj posvećen upravljanju i zaštiti privatnih ključeva Bitcoin Wallet. Za razliku od softverskih novčanika (ili Hot novčanika) instaliranih na mašinama opšte namene koje su često povezane na Internet, hardverski novčanici omogućavaju fizičku izolaciju privatnih ključeva, smanjujući rizike od hakovanja i krađe.


Glavni cilj Hardware Wallet je da minimizira funkcionalnosti uređaja što je više moguće kako bi se smanjila njegova površina napada. Manja površina napada takođe znači manje potencijalnih vektora napada, tj. manje slabosti u sistemu koje napadači mogu iskoristiti za pristup bitcoinima.


Preporučuje se korišćenje Hardware Wallet za osiguranje vaših bitkoina, posebno ako posedujete značajne iznose, bilo u apsolutnoj vrednosti ili kao proporciju vaših ukupnih sredstava.


Hardverski novčanici se koriste u kombinaciji sa Wallet softverom za upravljanje na računaru ili pametnom telefonu. Ovaj softver upravlja kreiranjem transakcija, ali kriptografski potpis neophodan za validaciju ovih transakcija se vrši isključivo unutar Hardware Wallet. To znači da privatni ključevi nikada nisu izloženi potencijalno ranjivom okruženju.


Hardverski novčanici nude dvostruku zaštitu za korisnika: s jedne strane, štite vaše bitkoine od daljinskih napada držeći privatne ključeve van mreže, a s druge strane, obično nude bolju fizičku otpornost protiv pokušaja ekstrakcije ključeva. I upravo na osnovu ova 2 sigurnosna kriterijuma može se oceniti i rangirati različiti modeli dostupni na tržištu.


U ovom vodiču predlažem da otkrijemo jedno od ovih rešenja: **Ledger Nano S Plus**.


![NANO S PLUS LEDGER](assets/notext/01.webp)


## Uvod u Ledger Nano S Plus


Ledger Nano S Plus je Hardware Wallet koji proizvodi francuska kompanija Ledger, a prodaje se po ceni od 79 €.


![NANO S PLUS LEDGER](assets/notext/02.webp)


Nano S Plus je opremljen CC EAL6+ sertifikovanim čipom ("*secure element*"), koji vam nudi naprednu zaštitu od fizičkih napada na hardver. Ekran i dugmad su direktno kontrolisani od strane ovog čipa. Često se ističe kao kritika da kod ovog čipa nije open-source, što zahteva određeno poverenje u integritet ove komponente. Ipak, ovaj element je revidiran od strane nezavisnih stručnjaka.


Što se tiče upotrebe, Ledger Nano S Plus radi isključivo putem žičane USB-C veze.


Ledger se izdvaja od svojih konkurenata po uvek veoma brzom usvajanju novih funkcija Bitcoin, kao što su Taproot ili Miniscript, na primer, što je veoma cenjeno.

Nakon testiranja, smatram da je Ledger Nano S Plus odličan početni nivo Hardware Wallet. Nudi visok nivo sigurnosti po razumnoj ceni. Njegov glavni nedostatak u poređenju sa drugim uređajima u istom cenovnom rangu je činjenica da firmware kod nije open-source. Takođe, ekran Nano S Plus je relativno mali u poređenju sa skupljim modelima, kao što su Ledger Flex ili Coldcard Q1. Ipak, njegov Interface je veoma dobro dizajniran: uprkos dva dugmeta i malom ekranu, ostaje jednostavan za korišćenje, uključujući napredne funkcije kao što je BIP39 passphrase. Ledger Nano S Plus nema bateriju, Air-gap konekciju, kameru ili micro SD port, ali to je sasvim normalno za ovaj cenovni rang.


Po mom mišljenju, Ledger Nano S Plus je dobra opcija za osiguranje vašeg Bitcoin Wallet, i pogodan je za početnike i korisnike srednjeg nivoa. Međutim, u ovom cenovnom rangu, lično preferiram Trezor Safe 3, koji nudi otprilike iste opcije. Prednost Trezora, po mom mišljenju, je u upravljanju njegovim sigurnosnim elementom: Mnemonic fraza i ključevi se upravljaju isključivo otvorenim kodom, a ipak imaju koristi od zaštite čipa. Nedostatak Trezora je što su ponekad veoma spori u implementaciji novih funkcija za razliku od Ledger.


## Kako kupiti Ledger Nano S Plus?


Ledger Nano S Plus je dostupan za prodaju [na zvaničnom sajtu](https://shop.Ledger.com/products/Ledger-nano-s-plus). Da biste ga kupili u fizičkoj prodavnici, možete pronaći [listu sertifikovanih prodavaca](https://www.Ledger.com/reseller) na sajtu Ledger.


## Preduslovi


Kada primite svoj Ledger Nano, prvi korak je da proverite ambalažu kako biste se uverili da nije otvorena. Ako je oštećena, to bi moglo ukazivati na to da je Hardware Wallet kompromitovan i možda nije autentičan.


Po otvaranju, trebalo bi da pronađete sledeće stavke u kutiji:


- Ledger Nano S Plus;
- USB-C na USB-A kabl;
- Korisnički priručnik;
- Kartice za upisivanje vaše Mnemonic fraze.


Za ovaj vodič, biće vam potrebne 2 softverske aplikacije: Ledger Live za inicijalizaciju Ledger, i Sparrow Wallet za upravljanje vašim Bitcoin Wallet. Preuzmite [Ledger Live](https://www.Ledger.com/Ledger-live) i [Sparrow Wallet](https://sparrowwallet.com/download/) sa njihovih zvaničnih veb-sajtova.


![NANO S PLUS LEDGER](assets/notext/03.webp)

Za ova dva softverska programa, toplo preporučujem da proverite i njihovu autentičnost (pomoću GnuPG) i njihov integritet (preko Hash) pre nego što ih instalirate na svoj računar. Ako niste sigurni kako to da uradite, možete pratiti ovaj drugi vodič:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Kako inicijalizovati Ledger Nano?


Povežite svoj Nano sa računarom na kojem su instalirani Ledger Live i Sparrow Wallet. Da biste se kretali po Ledger, koristite levi taster za levo i desni taster za desno. Da biste izabrali ili potvrdili opciju, pritisnite oba tastera istovremeno.


![NANO S PLUS LEDGER](assets/notext/04.webp)


Pomerajte se kroz različite uvodne stranice, a zatim kliknite na 2 dugmeta da biste započeli.


![NANO S PLUS LEDGER](assets/notext/05.webp)


Izaberite opciju "*Setup as a new device*".


![NANO S PLUS LEDGER](assets/notext/06.webp)


Izaberite PIN kod koji će se koristiti za otključavanje vašeg Ledger. Ovo je zaštita protiv neovlašćenog fizičkog pristupa. Ovaj PIN kod ne igra ulogu u izvođenju kriptografskih ključeva vašeg Wallet. Dakle, čak i bez pristupa ovom PIN kodu, posedovanje vaše 24-reči Mnemonic fraze će vam omogućiti da ponovo dobijete pristup vašim bitcoinima.


![NANO S PLUS LEDGER](assets/notext/07.webp)


Preporučuje se odabrati 8-cifreni PIN, što je moguće nasumičniji. Takođe, obavezno sačuvajte ovaj kod na drugom mestu od onog gde je vaš Ledger Nano S Plus uskladišten (na primer, u menadžeru lozinki).


Koristite dugmad da se pomerate preko cifara, zatim izaberite svaku cifru klikom na oba dugmeta istovremeno.


![NANO S PLUS LEDGER](assets/notext/08.webp)


Unesite svoj PIN drugi put da ga potvrdite.


![NANO S PLUS LEDGER](assets/notext/09.webp)


Vaš Nano pruža uputstva o tome kako upravljati vašom frazom za oporavak.


**Ova Mnemonic fraza daje pun i neograničen pristup svim vašim bitcoinima**. Svako ko poseduje ovu frazu može ukrasti vaša sredstva, čak i bez fizičkog pristupa vašem Ledger. Fraza od 24 reči omogućava vam da povratite pristup vašim bitcoinima u slučaju gubitka, krađe ili oštećenja vašeg Ledger Nano. Stoga je veoma važno pažljivo je sačuvati i skladištiti na sigurnom mestu.


Možete to zapisati na kartonski papir koji ste dobili uz vaš Ledger, ili za veću sigurnost, preporučujem graviranje na medijumu od nerđajućeg čelika kako biste se zaštitili od rizika požara, poplava ili urušavanja.


Možete pregledati ova uputstva i preskočiti stranice klikom na desno dugme.


![NANO S PLUS LEDGER](assets/notext/10.webp)

Ledger će kreirati vašu Mnemonic frazu koristeći svoj generator slučajnih brojeva. Uverite se da niste posmatrani tokom ove operacije. Zapišite reči koje obezbeđuje Ledger na fizički medij po vašem izboru. U zavisnosti od vaše sigurnosne strategije, možete razmotriti pravljenje nekoliko potpunih fizičkih kopija fraze (ali važno je da je ne delite). Ključno je da reči budu numerisane i u sekvencijalnom redosledu.

***Očigledno, nikada ne biste trebali deliti ove reči na internetu, suprotno onome što radim u ovom uputstvu. Ovaj primer Wallet će biti korišćen samo na Testnet i biće obrisan nakon uputstva.***


![NANO S PLUS LEDGER](assets/notext/11.webp)


Da biste prešli na sledeće reči, kliknite desno dugme.


![NANO S PLUS LEDGER](assets/notext/12.webp)


Kada su sve reči zabeležene, kliknite na 2 dugmeta da pređete na sledeći korak.


![NANO S PLUS LEDGER](assets/notext/13.webp)


Kliknite na dva dugmeta "*Potvrdite vašu frazu za oporavak*", zatim izaberite reči vaše Mnemonic fraze redosledom kako biste potvrdili da ste ih ispravno zabeležili. Koristite leve i desne dugmiće za navigaciju između opcija, zatim izaberite tačnu reč klikom na 2 dugmeta. Nastavite ovaj postupak do 24. reči.


![NANO S PLUS LEDGER](assets/notext/14.webp)


Ako se fraza koju potvrđujete tačno poklapa sa onom koju vam je Ledger pružio u prethodnom koraku, možete nastaviti. Ako ne, to ukazuje da je vaša fizička kopija fraze Mnemonic netačna i potrebno je da ponovo pokrenete proces.


![NANO S PLUS LEDGER](assets/notext/15.webp)


I tu ga imate, vaš seed je pravilno kreiran na vašem Ledger Nano S Plus. Pre nego što nastavite sa kreiranjem novog Bitcoin Wallet iz ovog seed, hajde da zajedno istražimo postavke uređaja.


## Kako izmeniti postavke vašeg Ledger?


Da biste pristupili podešavanjima, držite pritisnuta 2 dugmeta nekoliko sekundi.


![NANO S PLUS LEDGER](assets/notext/16.webp)


Kliknite na meni "*Settings*".


![NANO S PLUS LEDGER](assets/notext/17.webp)


I odaberite "*General*".


![NANO S PLUS LEDGER](assets/notext/18.webp)


U meniju "*Language*" možete promeniti jezik prikaza.


![NANO S PLUS LEDGER](assets/notext/19.webp)


U meniju "*Brightness*" možete podesiti osvetljenost ekrana. Trenutno nas ne zanimaju ostala opšta podešavanja.


![NANO S PLUS LEDGER](assets/notext/20.webp)


Sada, idite na odeljak "*Bezbednost*" podešavanja.


![NANO S PLUS LEDGER](assets/notext/21.webp)


"*Promeni PIN*" vam omogućava da promenite svoj PIN kod.

![NANO S PLUS LEDGER](assets/notext/22.webp)

"*passphrase*" vam omogućava da postavite BIP39 passphrase. passphrase je opcionalna lozinka koja, u kombinaciji sa vašom frazom za oporavak, pruža dodatni Layer sigurnosti za vaš Wallet.


![NANO S PLUS LEDGER](assets/notext/23.webp)


Trenutno, vaš Wallet se generiše iz Mnemonic fraze koja se sastoji od 24 reči. Ova fraza za oporavak je veoma važna jer vam omogućava da povratite sve ključeve vašeg Wallet u slučaju gubitka. Međutim, ona predstavlja jednu tačku kvara (SPOF). Ako je kompromitovana, vaši bitkoini su u opasnosti. Tu dolazi passphrase. To je opcionalna lozinka, koju možete proizvoljno izabrati, koja se dodaje Mnemonic frazi kako bi se poboljšala sigurnost Wallet.


passphrase ne treba mešati sa PIN kodom. On igra ulogu u derivaciji vaših kriptografskih ključeva. Radi u tandemu sa Mnemonic frazom, menjajući seed iz kojeg se generišu ključevi. Dakle, čak i ako neko dobije vašu frazu od 24 reči, bez passphrase, ne može pristupiti vašim sredstvima. Korišćenje passphrase u suštini stvara novi Wallet sa različitim ključevima. Modifikovanje (čak i blago) passphrase će generate drugačiji Wallet.


passphrase je veoma moćan alat za poboljšanje sigurnosti vaših bitkoina. Međutim, veoma je važno razumeti kako funkcioniše pre nego što ga implementirate, kako biste izbegli gubitak pristupa vašem Wallet. Zato vam savetujem da se konsultujete sa ovim drugim posvećenim vodičem ako želite da postavite passphrase na vaš Ledger:


https://planb.network/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

Meni "*PIN lock*" omogućava vam da konfigurišete i aktivirate automatsko zaključavanje vašeg Ledger nakon određenog perioda neaktivnosti.


![NANO S PLUS LEDGER](assets/notext/24.webp)


Meni "*Screen saver*" omogućava vam da podesite režim spavanja vašeg Ledger Nano. Imajte na umu da čuvar ekrana ne zahteva unos PIN-a prilikom buđenja, osim ako opcija "*PIN lock*" nije aktivirana da odgovara režimu spavanja. Ova funkcija je posebno korisna za Ledger Nano X uređaje opremljene baterijom, kako bi se smanjila potrošnja energije.


![NANO S PLUS LEDGER](assets/notext/25.webp)


Konačno, meni "*Reset device*" omogućava vam da resetujete vaš Ledger. Nastavite sa ovim resetovanjem samo ako ste sigurni da ne sadrži ključeve koji osiguravaju bitkoine, jer biste mogli trajno izgubiti pristup vašim sredstvima. Ova opcija može biti korisna za izvođenje testa praznog oporavka, ali o tome ću govoriti malo kasnije.


![NANO S PLUS LEDGER](assets/notext/26.webp)

## Kako instalirati aplikaciju Bitcoin?


Pokrenite Ledger Live softver na vašem računaru, zatim povežite i otključajte vaš Ledger Nano. U Ledger Live, idite na meni "*My Ledger*". Bićete zamoljeni da autorizujete pristup vašem Nano uređaju.


![NANO S PLUS LEDGER](assets/notext/27.webp)


Potvrdite pristup na vašem Ledger klikom na dva dugmeta.


![NANO S PLUS LEDGER](assets/notext/28.webp)


Prvo, na Ledger Live, uverite se da se pojavljuje "*Genuine check*". Ovo potvrđuje da je vaš uređaj autentičan.


![NANO S PLUS LEDGER](assets/notext/29.webp)


Ako firmver vašeg Ledger Nano nije ažuriran, Ledger Live će automatski ponuditi da ga ažurira. Ako je potrebno, kliknite na "*Update firmware*", zatim na "*Install update*" da biste započeli instalaciju. Na vašem Ledger, kliknite na dva dugmeta da potvrdite, zatim sačekajte tokom instalacije.


Konačno, dodaćemo aplikaciju Bitcoin. Da bismo to uradili, na Ledger Live, kliknite na dugme "*Install*" pored "*Bitcoin (BTC)*".


![NANO S PLUS LEDGER](assets/notext/30.webp)


Aplikacija će se instalirati na vaš Nano.


![NANO S PLUS LEDGER](assets/notext/31.webp)


Od sada vam više neće biti potreban Ledger Live softver za redovno upravljanje vašim Wallet. Povremeno se možete vratiti na njega kako biste ažurirali firmware kada nove verzije budu dostupne. Za sve ostalo, koristićemo Sparrow Wallet, koji je mnogo sveobuhvatniji alat za efikasno upravljanje Bitcoin Wallet.


![NANO S PLUS LEDGER](assets/notext/32.webp)


## Kako postaviti novi Bitcoin Wallet sa Sparrow?


Otvorite Sparrow Wallet i preskočite uvodne stranice da biste pristupili početnom ekranu. Proverite da li ste ispravno povezani na čvor posmatrajući prekidač smešten u donjem desnom uglu ekrana.


![NANO S PLUS LEDGER](assets/notext/33.webp)


Preporučujem da koristite sopstveni Bitcoin čvor. U ovom uputstvu koristim javni čvor (žuti) jer sam na Testnet, ali za normalnu upotrebu, bolje je odlučiti se za lokalni Bitcoin Core (Green) ili Electrum server povezan sa udaljenim čvorom (plavi).


Kliknite na meni "*File*" zatim "*New Wallet*".


![NANO S PLUS LEDGER](assets/notext/34.webp)


Izaberite ime za ovaj Wallet, zatim kliknite na "*Create Wallet*".


![NANO S PLUS LEDGER](assets/notext/35.webp)


U padajućem meniju "*Script Type*", izaberite tip skripte koja će se koristiti za obezbeđivanje vaših bitkoina. Preporučujem da odaberete "*Taproot*", ili ako nije dostupno, "*Native SegWit*".


![NANO S PLUS LEDGER](assets/notext/36.webp)

Kliknite na dugme "*Connected Hardware Wallet*".

![NANO S PLUS LEDGER](assets/notext/37.webp)


Ako to već niste učinili, povežite svoj Ledger Nano S Plus sa računarom, otključajte ga pomoću PIN koda, a zatim otvorite aplikaciju "*Bitcoin*" klikom na 2 dugmeta jednom na Bitcoin logotipu.


*U ovom uputstvu koristim aplikaciju Bitcoin Testnet, ali postupak ostaje isti za Mainnet.*


![NANO S PLUS LEDGER](assets/notext/38.webp)


Na Sparrow-u, kliknite na dugme "*Scan*".


![NANO S PLUS LEDGER](assets/notext/39.webp)


Zatim kliknite na "*Importuj Keystore*".


![NANO S PLUS LEDGER](assets/notext/40.webp)


Sada možete videti detalje vašeg Wallet, uključujući prošireni javni ključ vašeg prvog naloga. Kliknite na dugme "*Apply*" da biste finalizirali kreiranje Wallet.


![NANO S PLUS LEDGER](assets/notext/41.webp)


Izaberite jaku lozinku za zaštitu pristupa Sparrow Wallet. Ova lozinka će osigurati bezbednost pristupa vašim Wallet podacima na Sparrow-u, što pomaže u zaštiti vaših javnih ključeva, adresa, oznaka i istorije transakcija od bilo kakvog neovlašćenog pristupa.


Savjetujem ti da sačuvaš ovu lozinku u menadžeru lozinki kako je ne bi zaboravio.


![NANO S PLUS LEDGER](assets/notext/42.webp)


I eto ga, vaš Wallet je sada kreiran!


![NANO S PLUS LEDGER](assets/notext/43.webp)


Pre nego što primite svoje prve bitkoine u vaš Wallet, **snažno vam savetujem da izvedete test oporavka na suvo**. Zapišite referentni podatak, kao što je vaš xpub, zatim resetujte vaš Ledger Nano dok je Wallet još uvek prazan. Nakon toga, pokušajte da obnovite vaš Wallet na Ledger koristeći vaše papirne rezervne kopije. Proverite da li se xpub generisan nakon obnove poklapa sa onim koji ste prvobitno zabeležili. Ako je tako, možete biti sigurni da su vaše papirne rezervne kopije pouzdane.


Da biste saznali više o tome kako izvesti test oporavka, savetujem vam da pogledate ovaj drugi vodič:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Kako primiti bitkoine sa Ledger Nano?


Kliknite na karticu "*Receive*".


![NANO S PLUS LEDGER](assets/notext/44.webp)


Povežite svoj Ledger Nano S Plus sa računarom, otključajte ga pomoću PIN koda, a zatim otvorite aplikaciju "*Bitcoin*".


![NANO S PLUS LEDGER](assets/notext/45.webp)

Pre nego što upotrebite Address koji obezbeđuje Sparrow Wallet, proverite ga na ekranu vašeg Ledger. Ova praksa vam omogućava da potvrdite da Address prikazan na Sparrow nije lažan i da Hardware Wallet zaista poseduje privatni ključ neophodan za trošenje bitkoina osiguranih ovim Address kasnije. Ovo vam pomaže da izbegnete nekoliko vrsta napada.

Da biste izvršili ovu verifikaciju, kliknite na dugme "*Display Address*".


![NANO S PLUS LEDGER](assets/notext/46.webp)


Uverite se da Address prikazan na vašem Ledger odgovara onom naznačenom na Sparrow Wallet. Takođe se preporučuje da izvršite ovu proveru neposredno pre nego što predate vaš Address pošiljaocu, kako biste bili sigurni u njegovu validnost. Možete koristiti dugmad za pregled celog Address.


![NANO S PLUS LEDGER](assets/notext/47.webp)


Zatim kliknite na "*Odobri*" ako su adrese zaista identične.


![NANO S PLUS LEDGER](assets/notext/48.webp)


Možete dodati "*Label*" da opišete izvor bitkoina koji će biti osiguran ovim Address. Ovo je dobra praksa koja vam pomaže da bolje upravljate svojim UTXO-ima.


![NANO S PLUS LEDGER](assets/notext/49.webp)


Za više informacija o označavanju, takođe vam savetujem da pogledate ovaj drugi vodič:


https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Zatim možete koristiti ovaj Address za primanje bitkoina.


![NANO S PLUS LEDGER](assets/notext/50.webp)


## Kako poslati bitkoine pomoću Ledger Nano?


Sada kada ste primili svoj prvi Sats u vašem Wallet osiguranom sa Nano S Plus, možete ih i trošiti! Povežite svoj Ledger sa računarom, otključajte ga, pokrenite Sparrow Wallet, a zatim idite na karticu "*Send*" da konstruirate novu transakciju.


![NANO S PLUS LEDGER](assets/notext/51.webp)


Ako želite da uradite "*kontrolu novčića*", što znači da specifično izaberete koje UTXO-e da potrošite u transakciji, idite na karticu "*UTXOs*". Izaberite UTXO-e koje želite da potrošite, zatim kliknite na "*Pošalji izabrano*". Bićete preusmereni na isti ekran kartice "*Pošalji*", ali sa vašim već izabranim UTXO-ima za transakciju.


![NANO S PLUS LEDGER](assets/notext/52.webp)


Unesite odredište Address. Takođe možete uneti više adresa klikom na dugme "*+ Dodaj*".


![NANO S PLUS LEDGER](assets/notext/53.webp)


Zabeleži "*Label*" da zapamtiš svrhu ovog troška.


![NANO S PLUS LEDGER](assets/notext/54.webp)


Izaberite iznos poslat na ovaj Address.


![NANO S PLUS LEDGER](assets/notext/55.webp)


Prilagodite stopu naknade za transakciju prema trenutnom tržištu.


![NANO S PLUS LEDGER](assets/notext/56.webp)

Proverite da su sva podešavanja vaše transakcije ispravna, zatim kliknite na "*Create Transaction*".

![NANO S PLUS LEDGER](assets/notext/57.webp)


Ako vam sve izgleda dobro, kliknite na "*Finalize Transaction for Signing*".


![NANO S PLUS LEDGER](assets/notext/58.webp)


Kliknite na "*Sign*".


![NANO S PLUS LEDGER](assets/notext/59.webp)


Kliknite na "*Sign*" pored vašeg Ledger Nano S Plus.


![NANO S PLUS LEDGER](assets/notext/60.webp)


Proverite postavke transakcije na ekranu vašeg Ledger, uključujući prijemnik koji prima Address, poslati iznos i iznos naknade.


![NANO S PLUS LEDGER](assets/notext/61.webp)


Ako vam sve izgleda dobro, pritisnite dva dugmeta na "*Sign transaction*" da potpišete.


![NANO S PLUS LEDGER](assets/notext/62.webp)


Vaša transakcija je sada potpisana. Proverite još jednom da li vam sve izgleda u redu, a zatim kliknite na "*Emituj transakciju*" da biste je emitovali na Bitcoin mreži.


![NANO S PLUS LEDGER](assets/notext/63.webp)


Možete ga pronaći na kartici "*Transactions*" u Sparrow Wallet.


![NANO S PLUS LEDGER](assets/notext/64.webp)


Čestitamo, sada ste upoznati sa osnovnom upotrebom Ledger Nano S Plus sa Sparrow Wallet! U budućem vodiču ćemo videti kako koristiti Ledger sa Liana za korišćenje Miniscript-a.


Ako ste smatrali da je ovaj vodič bio od pomoći, bio bih zahvalan ako biste mogli ostaviti palac gore ispod. Slobodno podelite ovaj članak na svojim društvenim mrežama. Hvala vam puno!


Takođe vam preporučujem da pogledate ovaj kompletan vodič za Ledger Flex:


https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a