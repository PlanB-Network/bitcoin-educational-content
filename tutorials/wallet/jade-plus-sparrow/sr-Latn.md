---
name: Jade Plus - Sparrow
description: Napredna konfiguracija Jade Plus sa Sparrow Wallet
---
![cover](assets/cover.webp)


Jade Plus je Bitcoin-only Hardware Wallet koji je dizajnirao Blockstream. To je naslednik klasičnog Jade-a, sa softverskim poboljšanjima, više opcija i redizajniranim ergonomijom za intuitivniju upotrebu. Ova nova verzija se može pohvaliti veličanstvenim 1.9-inčnim LCD ekranom, sa širim spektrom boja od svog prethodnika. Dugmad i navigacija kroz meni su takođe optimizovani.


Jade Plus se može koristiti na više načina: putem USB-C žičane veze, u "*Air-Gap*" režimu sa micro SD karticom (potreban adapter), putem Bluetooth-a ili čak razmenom QR kodova zahvaljujući integrisanoj kameri. Ovaj Hardware Wallet radi na baterije.


Dostupan je od $149.99 u osnovnoj crnoj verziji, a cena može porasti do $20 za verzije "*Genesis Grey*" ili "*Lunar Silver*". Jade Plus je stoga zanimljiv izbor, sa naprednim funkcionalnostima koje su uporedive sa onima vrhunskih hardverskih novčanika kao što su Coldcard Q ili Passport V2, ali po prilično niskoj ceni, bliskoj modelima srednjeg ranga.


![JADE-PLUS-SPARROW](assets/fr/01.webp)


Jade Plus je kompatibilan sa većinom Wallet softvera za upravljanje. Ovde je sažetak kompatibilnosti u trenutku pisanja (januar 2025):


| Desktop | Mobile | USB | Bluetooth | QR | JadeLink | Management software
| ------------------- | ------- | ------ | --- | ----------- | --- | -------- |
| Blockstream Green | 🟢 | 🟢 | 🟢 (Mobile) | 🟢 | 🔴 |
| Liana | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 |
| Sparrow | 🟢 | 🔴 | 🟢 | 🔴 | 🟢 | 🟢 |
| Nunchuk | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 |
| Specter | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 |
| BlueWallet | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 |
| Electrum | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 |
| Keeper | 🔴 | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 |

U ovom vodiču, postavićemo naprednu konfiguraciju Jade Plus sa desktop softverom Sparrow Wallet u režimu QR kodova. Ova konfiguracija je idealna za korisnike srednjeg ili naprednog nivoa. Ako tražite jednostavniji pristup za početnike, preporučujem da pogledate ovaj vodič gde koristimo Jade Plus sa Green Wallet preko Bluetooth veze:


https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0

## Model bezbednosti Jade Plus


Jade Plus koristi bezbednosni model zasnovan na "virtuelnom sigurnosnom elementu", materijalizovanom kroz "slepi orakl". U konkretnim terminima, ovaj mehanizam kombinuje PIN koji je izabrao korisnik, tajnu smeštenu na Jade i tajnu koju drži orakl (server koji održava Blockstream), kako bi se kreirao AES-256 ključ raspodeljen preko dva entiteta. Tokom inicijacije, ECDH Exchange osigurava komunikaciju sa oraklom i šifruje frazu za oporavak na Hardware Wallet. U praktičnim terminima, kada želite da pristupite seed radi potpisivanja transakcija, potrebno vam je pristup:




- Sam uređaj Jade Plus;
- Da biste otključali uređaj, unesite PIN;
- I tajni proročišta.


Glavna prednost ovog pristupa je odsustvo jedne tačke kvara na nivou hardvera, jer ako napadač ikada dobije pristup vašem Jade-u, ekstrakcija ključeva zahteva istovremeno kompromitovanje Jade-a i orakla. Ovaj model takođe znači da je Jade Plus potpuno open-source, izbegavajući ograničenja povezana sa korišćenjem pravog fizičkog secure Elements, kao što su oni korišćeni na Ledger, na primer.


Nedostatak ovog sistema je što upotreba Jade Plus zavisi od orakla koji održava Blockstream. Ako ovaj orakl postane nedostupan, više nije moguće koristiti Hardware Wallet direktno sa PIN-om. Međutim, to ne znači da su vaši bitkoini izgubljeni, jer se i dalje mogu povratiti korišćenjem vaše fraze za oporavak, koju možete uneti u Jade Plus u "*stateless*" režimu. Da biste zaobišli ovu zavisnost, možete takođe konfigurisati i upravljati sopstvenim orakl serverom.


Još jedna opcija za upravljanje vašim seed je jednostavno da ga ne registrujete na Jade Plus. U ovom slučaju, Jade postaje samo uređaj za potpisivanje. Tokom inicijalizacije, pored uobičajenog čuvanja fraze za oporavak kao reči, takođe ćete je sačuvati kao ručno generisan QR kod. Na ovaj način, svaki put kada koristite vaš Wallet, možete uvesti seed koristeći kameru vašeg Jade-a. Ovo može biti zanimljiva opcija za napredne korisnike, u zavisnosti od vaše sigurnosne strategije, ali morate biti pažljivi da sačuvate vaš seed i zaštitite ga, jer čak i kao QR kod, omogućio bi bilo kome da ukrade vaša sredstva. Pogledaćemo ovu opciju u ovom vodiču, ali nije obavezna.


## Raspakivanje Jade Plus


Kada primite svoj Jade Plus, proverite da li su kutija i Seal u dobrom stanju kako biste osigurali da vaš paket nije otvoren.


![JADE-PLUS-SPARROW](assets/fr/02.webp)


U kutiji ćete pronaći :




- Le Jade Plus;
- USB-C kabl;
- Kartice za beleženje vaše Mnemonic fraze kao reči ili kao "*CompactSeedQR*";
- Neka uputstva za upotrebu ;
- Kabl;
- Neke nalepnice.


![JADE-PLUS-SPARROW](assets/fr/03.webp)


Uređaj ima 4 navigaciona dugmeta:




- Dugme u donjem desnom uglu uključuje Jade;
- Veliko dugme na prednjoj strani uređaja koristi se za odabir stavke;
- Dva mala dugmeta na vrhu omogućavaju vam da se krećete levo i desno;
- Takođe možete odabrati stavku istovremenim klikom na dva dugmeta na vrhu uređaja.


![JADE-PLUS-SPARROW](assets/fr/04.webp)


## Postavljanje novog Bitcoin Wallet


Kliknite na dugme za pokretanje.


![JADE-PLUS-SPARROW](assets/fr/05.webp)


Kliknite na "*Setup Jade*".


![JADE-PLUS-SPARROW](assets/fr/06.webp)


Odaberite "Advanced Setup*".


![Image](assets/fr/07.webp)


Zatim kliknite na "*Create a New Wallet*" da generate novi seed. Možete birati između 12- ili 24-reči Mnemonic fraze. Sigurnost vašeg Wallet ostaje ekvivalentna sa obe opcije, tako da može biti pogodnije izabrati najjednostavniju opciju za čuvanje, tj. 12 reči.


![Image](assets/fr/08.webp)


Kliknite na dugme "*Continue*" da biste prikazali vašu novu frazu za oporavak.


![Image](assets/fr/09.webp)


Vaš Jade Plus prikazuje vašu 12-rečnu Mnemonic frazu. **Ovaj Mnemonic vam daje potpuni, neograničeni pristup svim vašim bitcoinima. Svako ko poseduje ovu frazu može ukrasti vaša sredstva, čak i bez fizičkog pristupa vašem Jade Plus uređaju. 12-rečna fraza vraća pristup vašim bitcoinima u slučaju gubitka, krađe ili oštećenja vašeg Jade uređaja. Stoga je veoma važno da je pažljivo sačuvate i skladištite na sigurnom mestu.


Možete ga napisati na kartonu koji je priložen u kutiji, ili za dodatnu sigurnost, preporučujem graviranje na bazi od nerđajućeg čelika kako biste ga zaštitili od požara, poplave ili urušavanja.


![Image](assets/fr/10.webp)


Za više informacija o pravilnom načinu čuvanja i upravljanja vašom Mnemonic frazom, toplo preporučujem da pratite ovaj drugi vodič, posebno ako ste početnik:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

naravno, nikada ne smete deliti ove reči na Internetu, kao što to radim u ovom uputstvu. Ovaj uzorak Wallet će biti korišćen samo na Testnet i biće obrisan na kraju uputstva.**_


Kliknite na strelicu na desnoj strani ekrana da prikažete sledeće reči.


![Image](assets/fr/11.webp)


Kada sačuvate svoju frazu, Jade Plus će vas zamoliti da je potvrdite. Izaberite tačnu reč prema redosledu koristeći dugmad na vrhu uređaja, i kliknite na centralno dugme da pređete na sledeću reč.


![Image](assets/fr/12.webp)


Zatim imate 2 opcije. Kao što je objašnjeno u uvodu, možete izabrati da sačuvate svoj seed direktno na uređaju i koristite Blockstream-ov sistem zaštite "*Virtual Secure Element*" za pristup vašem Wallet (Opcija 1), ili sačuvati svoj seed kao QR kod i skenirati ga svaki put kada ga koristite (Opcija 2).


Za Opciju 1, izaberite "*Ne*", a za Opciju 2, izaberite "*Da*".


![Image](assets/fr/13.webp)


### Opcija 1: QR PIN Otključavanje


Ako ste izabrali opciju 1 (CompactSeedQR: "*Ne*"), bićete direktno preusmereni na izbor metode povezivanja. U ovom uputstvu, želimo da koristimo uređaj u Air-Gap režimu putem razmene QR kodova, zato izaberite "*QR*".


![Image](assets/fr/27.webp)


Kliknite na "*Continue*".


![Image](assets/fr/28.webp)


PIN kod se koristi za otključavanje vašeg Jade-a i pruža zaštitu protiv neovlašćenog fizičkog pristupa. Ovaj PIN kod nije uključen u derivaciju kriptografskih ključeva vašeg Wallet. Dakle, čak i bez pristupa ovom PIN kodu, posedovanje vaše 12-reči Mnemonic fraze omogućiće vam da ponovo dobijete pristup vašim bitcoinima. Preporučujemo da izaberete PIN kod koji je što je moguće nasumičniji. Takođe, obavezno sačuvajte ovaj kod na odvojenom mestu od mesta gde je vaš Jade uskladišten, kao što je u menadžeru lozinki.


Izaberite 6-cifreni PIN kod na vašem Jade uređaju, koristeći leve i desne tastere za pomeranje kroz cifre, a srednji taster za potvrdu svake cifre.


![Image](assets/fr/29.webp)


Potvrdite svoj PIN drugi put.


![Image](assets/fr/30.webp)


Kao što je objašnjeno u uvodu, vaš seed je sačuvan šifrovan na Jade Plus. Da biste ga dešifrovali, morate obezbediti:




- Važeći PIN kod (koji smo upravo postavili) ;
- Tajna proročišta koju održava Blockstream.


U ovom naprednom vodiču, koristićemo Sparrow Wallet za upravljanje našim Bitcoin Wallet. Međutim, za razliku od Blockstream-ovog Green Wallet softvera, Sparrow nema pristup oraklu na Blockstream-ovim serverima. Stoga ćemo koristiti Blockstream-ov vebsajt da preuzmemo tajnu orakla svaki put kada otključamo Jade Plus.


Posetite https://jadefw.blockstream.com/pinqr/index.html


Kliknite na "*Start QR Unlock*".


![Image](assets/fr/31.webp)


Kliknite na "*Done*", pošto ste već odabrali svoj PIN na Jade Plus.


![Image](assets/fr/32.webp)


Koristite kameru svog računara da skenirate QR kodove prikazane na ekranu vašeg Jade uređaja.


![Image](assets/fr/33.webp)


Potvrdite na vašem Jade-u da biste pristupili sledećem ekranu.


![Image](assets/fr/34.webp)


Skenirajte QR kod sada vidljiv na vebsajtu da biste preuzeli tajnu proročišta.


![Image](assets/fr/35.webp)


Sada kada je vaš Wallet kreiran, možete preći na sledeće korake i preskočiti pododeljak "*Option 2: CompactSeedQR*".


![Image](assets/fr/36.webp)


Svaki put kada pokrenete, kliknite na "*QR Mode*".


![Image](assets/fr/37.webp)


Odaberite "*QR PIN Unlock*".


![Image](assets/fr/38.webp)


Unesite svoj PIN kod.


![Image](assets/fr/39.webp)


Zatim idite na [Blockstream vebsajt](https://jadefw.blockstream.com/pinqr/qrpin.html) da Exchange QR kodove sa orakulom.


![Image](assets/fr/40.webp)


Vaš Jade je sada otključan.


![Image](assets/fr/41.webp)


### Opcija 2: CompactSeedQR


Ako ste izabrali opciju 2 (CompactSeedQR: "*Da*"), kliknite ponovo na "*Da*".


![Image](assets/fr/14.webp)


Kliknite na "*Start*".


![Image](assets/fr/15.webp)


Možete koristiti bazu QR koda isporučenu u Jade Plus kutiji. Odaberite odgovarajuću kutiju u zavisnosti od toga da li ste se odlučili za rečenicu od 12 ili 24 reči. Takođe možete [odštampati šablon sa Blockstream vebsajta](https://help.blockstream.com/hc/article_attachments/41928319071769).


Vaš Jade Plus će prikazati svaku zonu vašeg QR koda.


![Image](assets/fr/16.webp)


Koristite olovku da obojite kvadrate i reprodukujete svoj seed kao QR kod. Budite precizni kako bi Jade Plus kamera mogla kasnije da ga skenira. Koristite strelicu da pređete na sledeće područje.


![Image](assets/fr/17.webp)


Kada završite, kliknite na "*Done*".


![Image](assets/fr/18.webp)


Skenirajte svoj ručno izrađeni QR kod pomoću Jade Plus da proverite njegovu validnost.


![Image](assets/fr/19.webp)


Ako je vaša papirna kopija tačna, kliknite na "*Nastavi*".


![Image](assets/fr/20.webp)


U ovom vodiču ćemo koristiti način povezivanja zasnovan isključivo na skeniranju QR koda, zato izaberite "*QR*".


![Image](assets/fr/21.webp)


Možete takođe izabrati da dodate PIN uz vašu CompactSeedQR rezervnu kopiju, kao u opciji 1. Ovo nudi dva načina pristupa vašem Wallet: ili putem PIN-a i Blockstream-ovog sistema "Virtual Secure Element", ili putem CompactSeedQR.


Ako se odlučite za opciju dvostrukog PIN-a, izaberite "*PIN*" i pratite iste korake kao u opciji 1 da postavite svoj PIN kod.


Ako želite da nastavite samo sa CompactSeedQR, izaberite "*SeedQR*".


![Image](assets/fr/22.webp)


Sada kada je vaš Wallet kreiran, možete preći na sledeće korake.


![Image](assets/fr/23.webp)


Svaki put kada pokrenete, kliknite na dugme "*QR Mode*", zatim "*Scan SeedQR*".


![Image](assets/fr/24.webp)


Koristite kameru uređaja da skenirate svoj sačuvani seed kao QR kod.


![Image](assets/fr/25.webp)


Vaš Jade je sada otključan.


![Image](assets/fr/26.webp)


## Dodajte BIP39 passphrase


BIP39 passphrase je opcionalna lozinka koju možete slobodno izabrati, i koja se dodaje vašoj Mnemonic frazi kako bi se pojačala Wallet sigurnost. Sa ovom funkcijom omogućen, pristup vašem Bitcoin Wallet će zahtevati i Mnemonic i passphrase. Bez bilo kojeg, bilo bi nemoguće povratiti Wallet.


Pre nego što konfigurišete ovu opciju na vašem Jade Plus, preporučuje se da pročitate ovaj članak kako biste u potpunosti razumeli teorijski rad passphrase i izbegli greške koje bi mogle dovesti do gubitka vaših bitkoina :


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Sa vašim Jade i dalje zaključanim (passphrase se može uneti samo kada uređaj nije otključan), pristupite meniju "*Opcije*".


![Image](assets/fr/42.webp)


Odaberite "*BIP39 passphrase*".


![Image](assets/fr/43.webp)


U opciji "*Frequency*" možete izabrati da li će vas Jade Plus pitati da unesete vaš passphrase svaki put kada se pokrene:




- "*Onemogućeno*" onemogućava upotrebu passphrase;
- „*Sledeće prijavljivanje samo*“ zahtevaće da se vratite na ovaj meni kako biste aktivirali zahtev za vaš passphrase pri sledećem pokretanju. Ova opcija vam omogućava da ne otkrivate njegovu upotrebu;
- "*Always Ask*" uzrokuje da Jade sistematski traži vaš passphrase svaki put kada se pokrene, čime se otkriva da je vaš Wallet zaštićen passphrase.


Izaberite opciju u skladu sa vašom bezbednosnom strategijom. Lično, biram "*Uvek pitaj*" za primer.


![Image](assets/fr/44.webp)


Zatim možete birati između dve metode za unos vašeg passphrase:




- "*Priručnik*: Virtuelna tastatura vam omogućava da unosite slova (velika i mala slova), brojeve i simbole, karakter po karakter. Ovo je standardna metoda za sve hardverske novčanike;
- "*WordList*": Specifična metoda koju je dizajnirao Blockstream za Jade, koja ubrzava unos passphrase i povećava njegov entropiju. Tokom unosa, sistem predlaže reči sa BIP39 liste, što olakšava otključavanje. Ova metoda automatski generiše rečenicu spajanjem odabranih reči, odvojenih razmacima (primer: `abandon ability able`).


Lično vam savetujem da koristite prvu metodu, jer je to standard koji ćete naći na svim drugim Wallet podrškama.


![Image](assets/fr/45.webp)


Zatim možete da se vratite na početni ekran i otključate svoj Wallet kao i obično, koristeći svoj PIN kod ili svoj CompactSeedQR (kao što je prikazano iznad). Zatim će vam biti zatraženo da unesete svoj passphrase.


![Image](assets/fr/46.webp)


Unesite ga na Jade tastaturu i obavezno napravite jednu ili više rezervnih kopija na fizičkim medijima (papir ili metal). Za primer koristim veoma slab passphrase, ali vi treba da izaberete jak, nasumičan passphrase koji uključuje sve tipove karaktera i dovoljno je dug (kao jaka lozinka).


![Image](assets/fr/47.webp)


Ako je vaš passphrase važeći, potvrdite.


![Image](assets/fr/48.webp)


Imajte na umu da su BIP39 lozinke osetljive na velika i mala slova, kao i na tipografske greške. Ako unesete passphrase koji je malo drugačiji od onog koji je prvobitno konfigurisan, Jade neće prijaviti grešku, već će izvesti drugi skup kriptografskih ključeva koji neće biti oni u vašem početnom Wallet.


Važno je, dakle, prilikom konfigurisanja, zabeležiti otisak vašeg glavnog ključa, koji se može naći u donjem desnom uglu ekrana. Na primer, sa mojim passphrase `PBN`, otisak mog glavnog ključa je `3AD1AE65`.


![Image](assets/fr/49.webp)


Svaki put kada otključate svoj Jade sa svojim passphrase, proverite da li je otisak prsta isti kao onaj koji ste uneli tokom konfiguracije. Ako jeste, vaš passphrase je ispravan i pristupate pravom Bitcoin Wallet. Ako nije, nalazite se na pogrešnom Wallet i treba da pokušate ponovo, pazeći da ne napravite greške pri unosu.


Pre nego što primite svoje prve bitkoine u vaš Wallet, **toplo vam savetujem da izvršite test praznog oporavka**. Zabeležite neke referentne informacije, kao što su vaš xpub ili prvi prijemni Address, zatim obrišite vaš Wallet na Jade Plus dok je još uvek prazan (`Options -> Device -> Factory Reset`). Zatim pokušajte da obnovite vaš Wallet koristeći vaše papirne rezervne kopije Mnemonic fraze i bilo kojeg passphrase. Proverite da li informacije o kolačićima generisane nakon obnove odgovaraju onima koje ste prvobitno zapisali. Ako odgovaraju, možete biti sigurni da su vaše papirne rezervne kopije pouzdane. Da biste saznali više o tome kako izvršiti test oporavka, pogledajte ovaj drugi vodič:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Konfigurisanje Wallet na Sparrow Wallet


U ovom vodiču predstavljam naprednu upotrebu Jade Plus koristeći Sparrow Wallet. Međutim, ovaj Hardware Wallet je kompatibilan sa mnogim drugim programima, kao što su Liana, Nunchuk, Specter, Green i Keeper. Ove kompatibilnosti variraju u pogledu konekcija: USB, Bluetooth ili QR kod (pogledajte tabelu u uvodu za detalje).


Počnite preuzimanjem i instaliranjem Sparrow Wallet [sa zvanične veb stranice](https://sparrowwallet.com/) na vašem računaru, ako to već niste učinili.


![Image](assets/fr/50.webp)


Obavezno proverite autentičnost i integritet softvera pre instalacije. Ako ne znate kako to da uradite, molimo vas da pogledate ovaj vodič:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Kada se otvori Sparrow Wallet, kliknite na karticu "*File*", zatim na "*New Wallet*".


![Image](assets/fr/51.webp)


Nazovite svoj Wallet, zatim kliknite na "*Create Wallet*".


![Image](assets/fr/52.webp)


Odaberite "*Airgapped Hardware Wallet*".


![Image](assets/fr/53.webp)


Kliknite na "*Skeniraj...*" pored opcije "*Jade*".


![Image](assets/fr/54.webp)


Otključajte svoj Jade Plus i, ako ga koristite, unesite svoj passphrase. Zatim idite na meni "*Options*", izaberite "*Wallet*" i kliknite na "*Export Xpub*".


![Image](assets/fr/55.webp)


Vaš Jade će prikazati vaš Keystore putem nekoliko QR kodova. Skenirajte ih na vašem uređaju koristeći Sparrow.


![Image](assets/fr/56.webp)


Trebalo bi da sada vidite vaš xpub i otisak prsta vašeg glavnog ključa, koji bi trebalo da se poklapa sa onim na vašem Jade Plus. Kliknite na "*Primeni*".


![Image](assets/fr/57.webp)


Postavite jaku lozinku kako biste osigurali pristup svom Sparrow Wallet. Ova lozinka će zaštititi vaše javne ključeve, adrese, oznake i istoriju transakcija od neovlašćenog pristupa. Preporučuje se da ovu lozinku sačuvate u menadžeru lozinki, kako je ne biste zaboravili.


![Image](assets/fr/58.webp)


Vaš Wallet je sada ispravno konfigurisan na Sparrow.


![Image](assets/fr/59.webp)


## Primite bitkoine


Sada kada je vaš Jade Plus konfigurisan, spremni ste da primite svoj prvi Sats na vašem novom Bitcoin Wallet. Da biste to uradili, na Sparrow-u kliknite na meni "*Receive*".


![Image](assets/fr/60.webp)


Sparrow će prikazati prvi prazan prijem Address u vašem Wallet.


![Image](assets/fr/61.webp)


Pre nego što ga upotrebimo, hajde da ga proverimo na ekranu Jade Plus kako bismo bili sigurni da pripada našem Bitcoin Wallet. Na Jade-u, kliknite na "*Scan QR*", zatim skenirajte QR kod Address prikazan na Sparrow.


![Image](assets/fr/62.webp)


Proverite da li se Address prikazan na ekranu vaše Jade poklapa sa onim prikazanim na Sparrow Wallet. Ako se poklapa, kliknite na oznaku za potvrdu da nastavite.


![Image](assets/fr/63.webp)


Vaš Hardware Wallet će zatim potvrditi da je ovaj Address deo vašeg Wallet i da poseduje pridruženi privatni ključ.


![Image](assets/fr/64.webp)


Ako je Address validiran od strane vašeg Jade-a, sada ga možete koristiti za primanje bitkoina. Kada se transakcija emituje na mreži, pojaviće se na Sparrow-u. Sačekajte dok ne dobijete dovoljno potvrda da biste smatrali transakciju konačnom.


![Image](assets/fr/65.webp)


## Pošalji bitkoine


Sada kada imate nekoliko Sats u vašem Wallet, možete ih i poslati. Da biste to učinili, kliknite na meni "*UTXOs*".


![Image](assets/fr/66.webp)


Odaberite UTXO-ove koje želite koristiti kao ulaze za ovu transakciju, zatim kliknite na "*Pošalji odabrano*".


![Image](assets/fr/67.webp)


Unesite primaoca Address, oznaku koja će vas podsećati na svrhu transakcije i iznos koji želite poslati na ovaj Address.


![Image](assets/fr/68.webp)


Prilagodite stopu naknade prema trenutnim tržišnim uslovima, zatim kliknite na "*Create Transaction*".


![Image](assets/fr/69.webp)


Proverite da su svi parametri transakcije tačni, zatim kliknite na "*Finalize Transaction for Signing*".


![Image](assets/fr/70.webp)


Kliknite na "*Show QR*" da prikažete PSBT (*Partially Signed Bitcoin Transaction*). Sparrow je napravio transakciju, ali joj još uvek nedostaju potpisi za otključavanje bitkoina korišćenih u ulazu. Ove potpise može izvršiti samo Jade Plus, koji hostuje vaš seed dajući pristup privatnim ključevima potrebnim za potpisivanje transakcije.


![Image](assets/fr/71.webp)


Na vašem Jade Plus, kliknite na "*Scan QR*" da skenirate PSBT prikazan na Sparrow.


![Image](assets/fr/72.webp)


Potvrdite da su isporuka Address i poslata količina tačni, zatim kliknite na strelicu da potvrdite.


![Image](assets/fr/73.webp)


Proverite da je iznos naknade onaj koji ste odabrali, zatim kliknite na ikonu kvačice u gornjem levom uglu Interface da biste potpisali transakciju.


![Image](assets/fr/74.webp)


Na Sparrow Wallet, kliknite na "*Scan QR*" i skenirajte QR kod prikazan na vašem Jade.


![Image](assets/fr/75.webp)


Vaša potpisana transakcija je sada spremna za emitovanje na Bitcoin mreži i uključivanje u blok od strane Miner. Ako je sve ispravno, kliknite na "*Broadcast Transaction*".


![Image](assets/fr/76.webp)


Vaša transakcija je emitovana i čeka potvrdu.


![Image](assets/fr/77.webp)


Čestitamo, sada znate kako da postavite i koristite Jade Plus u QR režimu. Ako vam je ovaj vodič bio koristan, bio bih zahvalan ako biste ostavili Green palac ispod. Slobodno podelite ovaj članak na vašim društvenim mrežama. Hvala što delite!


Da biste nastavili dalje, preporučujem ovaj drugi vodič o Jade Plus, gde ga konfigurišemo putem Bluetooth-a sa Green mobilnom aplikacijom:


https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0