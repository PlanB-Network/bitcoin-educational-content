---
name: Jade Plus - Green
description: Lako konfigurišite Jade Plus sa Green
---
![cover](assets/cover.webp)


Jade Plus je Bitcoin-only Hardware Wallet dizajniran od strane Blockstream-a. To je naslednik klasičnog Jade-a, sa softverskim poboljšanjima, više opcija i redizajniranim ergonomijom za intuitivniju upotrebu. Ova nova verzija se može pohvaliti veličanstvenim 1.9-inčnim LCD ekranom, sa širim spektrom boja od svog prethodnika. Dugmad i navigacija kroz meni su takođe optimizovani.


Jade Plus se može koristiti na više načina: putem USB-C žičane veze, u "*Air-Gap*" režimu sa micro SD karticom (potreban adapter), putem Bluetooth-a ili čak razmenom QR kodova zahvaljujući integrisanoj kameri. Ovaj Hardware Wallet radi na baterije.


Dostupan je od $149.99 u osnovnoj crnoj verziji, a cena može porasti do $20 za verzije "*Genesis Grey*" ili "*Lunar Silver*". Jade Plus je stoga zanimljiv izbor, sa naprednim funkcionalnostima koje su uporedive sa onima vrhunskih hardverskih novčanika kao što su Coldcard Q ili Passport V2, ali po prilično niskoj ceni, bliskoj modelima srednjeg ranga.


![JADE-PLUS-GREEN](assets/fr/01.webp)


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

U ovom vodiču ćemo postaviti i koristiti Jade Plus sa Blockstreamovom Green Wallet mobilnom aplikacijom putem Bluetooth veze. Ova postavka je idealna za početnike. Ako tražite napredniji pristup, preporučujem da pogledate ovaj vodič gde koristimo Jade Plus sa Sparrow Wallet u režimu QR kodova:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

## Model bezbednosti Jade Plus


Jade Plus koristi bezbednosni model zasnovan na "virtuelnom sigurnosnom elementu", materijalizovanom kroz "slepi orakl". U konkretnim terminima, ovaj mehanizam kombinuje PIN koji bira korisnik, tajnu smeštenu na Jade i tajnu koju drži orakl (server koji održava Blockstream), kako bi se kreirao AES-256 ključ raspodeljen između dva entiteta. Tokom inicijacije, ECDH Exchange osigurava komunikaciju sa oraklom i šifruje frazu za oporavak na Hardware Wallet. U praktičnim terminima, kada želite da pristupite seed za potpisivanje transakcija, potrebno vam je pristup:




- Do samog uređaja Jade Plus;
- Da biste OTKLJUČALI uređaj, unesite PIN;
- I tajni proročišta.


Glavna prednost ovog pristupa je odsustvo jedne tačke kvara na nivou hardvera, jer ako napadač ikada dobije pristup vašem Jade-u, ekstrakcija ključeva zahteva istovremeno kompromitovanje Jade-a i orakla. Ovaj model takođe znači da je Jade Plus potpuno open-source, izbegavajući ograničenja povezana sa korišćenjem pravog fizičkog secure Elements, kao što su oni korišćeni na Ledger, na primer.


Nedostatak ovog sistema je što upotreba Jade Plus zavisi od orakla koji održava Blockstream. Ako ovaj orakl postane nedostupan, više nije moguće koristiti Hardware Wallet direktno sa PIN-om. Međutim, to ne znači da su vaši bitkoini izgubljeni, jer se i dalje mogu povratiti pomoću vaše fraze za oporavak, koju možete uneti u Jade Plus u "*stateless*" režimu. Da biste zaobišli ovu zavisnost, možete takođe konfigurisati i upravljati sopstvenim orakl serverom.


## Raspakivanje Jade Plus


Kada primite svoj Jade Plus, proverite da li su kutija i Seal u dobrom stanju kako biste se uverili da vaš paket nije otvoren.


![JADE-PLUS-GREEN](assets/fr/02.webp)


U kutiji ćete pronaći :




- Le Jade Plus;
- USB-C kabl;
- Kartice za beleženje vaše Mnemonic fraze kao reči ili kao "*CompactSeedQR*";
- Neka uputstva za upotrebu ;
- Kabl;
- Neke nalepnice.


![JADE-PLUS-GREEN](assets/fr/03.webp)


Uređaj ima 4 navigaciona dugmeta:




- Dugme u donjem desnom uglu uključuje Jade;
- Veliko dugme na prednjoj strani uređaja koristi se za odabir stavke;
- Dva mala dugmeta na vrhu omogućavaju vam navigaciju levo i desno;
- Takođe možete odabrati stavku istovremenim klikom na dva dugmeta na vrhu uređaja.


![JADE-PLUS-GREEN](assets/fr/04.webp)


## Postavljanje novog Bitcoin Wallet


Kliknite na dugme za pokretanje.


![JADE-PLUS-GREEN](assets/fr/05.webp)


Kliknite na "*Setup Jade*".


![JADE-PLUS-GREEN](assets/fr/06.webp)


Izaberite "Begin Setup". Opcija "*Advanced Setup*" radi isto, ali sa pristupom naprednim podešavanjima.


![JADE-PLUS-GREEN](assets/fr/07.webp)


Zatim kliknite na "*Create a New Wallet*" da generate novi seed.


![JADE-PLUS-GREEN](assets/fr/08.webp)


Kliknite na dugme "*Continue*" da biste prikazali vašu novu frazu za oporavak.


![JADE-PLUS-GREEN](assets/fr/09.webp)


Vaš Jade Plus prikazuje vašu 12-rečnu Mnemonic frazu. **Ovaj Mnemonic vam daje potpuni, neograničeni pristup svim vašim bitcoinima. Svako ko poseduje ovu frazu može ukrasti vaša sredstva, čak i bez fizičkog pristupa vašem Jade Plus. 12-rečna fraza vraća pristup vašim bitcoinima u slučaju gubitka, krađe ili loma vašeg Jade-a. Stoga je veoma važno da je pažljivo sačuvate i skladištite na sigurnom mestu.


Možete ga napisati na kartonu koji je priložen u kutiji, ili za dodatnu sigurnost, preporučujem graviranje na bazi od nerđajućeg čelika kako biste ga zaštitili od požara, poplave ili urušavanja.


![JADE-PLUS-GREEN](assets/fr/10.webp)


Za više informacija o pravilnom načinu čuvanja i upravljanja vašom Mnemonic frazom, toplo preporučujem da pratite ovaj drugi vodič, posebno ako ste početnik:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

***Očigledno, nikada ne smete deliti ove reči na Internetu, kao što ja radim u ovom uputstvu. Ovaj uzorak Wallet će biti korišćen samo na Testnet i biće obrisan na kraju uputstva


Kliknite na strelicu na desnoj strani ekrana da prikažete sledeće reči.


![JADE-PLUS-GREEN](assets/fr/11.webp)


Kada sačuvate svoju frazu, Jade Plus traži da je potvrdite. Izaberite tačnu reč prema redosledu koristeći dugmad na vrhu uređaja, i kliknite na centralno dugme da pređete na sledeću reč.


![JADE-PLUS-GREEN](assets/fr/12.webp)


## Povezivanje Jade Plus sa Green Wallet


U ovom vodiču, koristićemo aplikaciju Green Wallet za upravljanje Wallet hostovanim na Jade Plus. Ova metoda je posebno pogodna za početnike. Ako želite detaljnije da upravljate svojim Bitcoin Wallet, možete koristiti i Sparrow Wallet, što ćemo obraditi u posebnom vodiču:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

Za uputstva o instalaciji i podešavanju aplikacije Blockstream Green, pogledajte prvi deo ovog drugog vodiča:


https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

Jednom kada ste u aplikaciji Blockstream Green, kliknite na dugme "*Configure a new Wallet*".


![JADE-PLUS-GREEN](assets/fr/13.webp)


Odaberite "*On Hardware Wallet*".


![JADE-PLUS-GREEN](assets/fr/14.webp)


Aktivirajte Bluetooth na svom pametnom telefonu, a zatim kliknite na dugme "*Povežite svoj Jade*".


![JADE-PLUS-GREEN](assets/fr/15.webp)


Autorizujte aplikaciju Green za pristup Bluetooth vezama.


![JADE-PLUS-GREEN](assets/fr/16.webp)


Aplikacija traži vaš Jade Plus.


![JADE-PLUS-GREEN](assets/fr/17.webp)


Na Jade Plus, kliknite na meni "*Bluetooth*".


![JADE-PLUS-GREEN](assets/fr/18.webp)


Izaberite svoj uređaj na Green aplikaciji.


![JADE-PLUS-GREEN](assets/fr/19.webp)


Potvrdite kod za uparivanje na vašem Jade Plus.


![JADE-PLUS-GREEN](assets/fr/20.webp)


Green vam nudi test da osigurate da je vaš žad originalan. Kliknite na dugme da to učinite.


![JADE-PLUS-GREEN](assets/fr/21.webp)


Potvrdi na Jade.


![JADE-PLUS-GREEN](assets/fr/22.webp)


Green potvrđuje da je vaš uređaj originalan.


![JADE-PLUS-GREEN](assets/fr/23.webp)


## Postavljanje PIN koda


Kliknite na dugme "*Continue*" da izaberete PIN kod za Jade.


![JADE-PLUS-GREEN](assets/fr/24.webp)


PIN kod otključava vaš Jade. Stoga je zaštita protiv neovlašćenog fizičkog pristupa. Ovaj PIN kod nije uključen u izvođenje kriptografskih ključeva vašeg Wallet. Dakle, čak i bez pristupa ovom PIN kodu, posedovanje vaše 12-reči Mnemonic fraze omogućiće vam da ponovo dobijete pristup vašim bitcoinima. Preporučujemo da izaberete PIN kod koji je što je moguće nasumičniji. I budite sigurni da sačuvate ovaj kod na posebnom mestu od onog gde je vaš Jade uskladišten (npr. u menadžeru lozinki).


Izaberite 6-cifreni PIN kod na vašem Jade uređaju, koristeći desne i leve tastere za pomeranje kroz cifre, a srednji taster za potvrdu unosa cifre.


![JADE-PLUS-GREEN](assets/fr/25.webp)


Potvrdite svoj PIN drugi put.


![JADE-PLUS-GREEN](assets/fr/26.webp)


Vaš Bitcoin Wallet je kreiran.


![JADE-PLUS-GREEN](assets/fr/27.webp)


## Kreiraj Bitcoin nalog


Morate sada kreirati nalog unutar vašeg Wallet. Kliknite na dugme "*Create an account*".


![JADE-PLUS-GREEN](assets/fr/28.webp)


Izaberite "*Standard*" ako želite da kreirate klasični single-sig Wallet.


![JADE-PLUS-GREEN](assets/fr/29.webp)


Za više informacija o opciji "*2FA*", možete pratiti ovaj drugi vodič:


https://planb.network/tutorials/wallet/mobile/blockstream-green-2fa-37397d5c-5c27-44ad-a27a-c9ceac8c9df9

Vaš nalog je kreiran.


![JADE-PLUS-GREEN](assets/fr/30.webp)


Ako želite da personalizujete svoj Green Wallet, kliknite na tri male tačke u gornjem desnom uglu.


![JADE-PLUS-GREEN](assets/fr/31.webp)


Opcija "*Rename*" vam omogućava da prilagodite ime vašeg Wallet, što je posebno korisno ako upravljate sa nekoliko novčanika na istoj aplikaciji. Meni "*Unit*" vam omogućava da promenite osnovnu jedinicu vašeg Wallet. Na primer, možete odabrati da ga prikažete u satoshijima umesto u bitcoinima. Na kraju, meni "*Parameters*" vam daje pristup drugim opcijama. Ovde, na primer, možete pronaći vaš prošireni javni ključ i njegov opis, što je korisno ako planirate da postavite Watch-only wallet sa vašeg Jade.


![JADE-PLUS-GREEN](assets/fr/32.webp)


Da ponovo povežete svoj Jade nakon što ga isključite, pritisnite dugme za uključivanje/isključivanje na dnu uređaja. Na Green aplikaciji, odaberite svoj uređaj sa početne stranice:


![JADE-PLUS-GREEN](assets/fr/33.webp)


Zatim unesite PIN kod na vašem Jade-u i ponovo ćete biti povezani.


![JADE-PLUS-GREEN](assets/fr/34.webp)


Vaš Jade je otključan putem Blockstream-ovog "virtualnog sigurnosnog elementa" (pogledajte prvi deo ovog tutorijala). Ovo zahteva Bluetooth vezu sa Green aplikacijom. Ako naiđete na poteškoće sa Bluetooth vezom tokom otključavanja, pokušajte da razdvojite i ponovo povežete dva uređaja. Ako problem i dalje postoji, možete i dalje otključati vaš Jade odabirom opcije "*QR Scan*" i praćenjem uputstava dostupnih [na Blockstream sajtu](https://jadefw.blockstream.com/pinqr/index.html).


Pre nego što primite svoje prve bitkoine u vaš Wallet, **snažno vam savetujem da izvedete test praznog oporavka**. Zabeležite neke referentne informacije, kao što su vaš xpub ili prvi prijemni Address, zatim obrišite vaš Wallet na Green aplikaciji i na Jade Plus dok je još uvek prazan (`Opcije -> Uređaj -> Fabrika Reset`). Zatim pokušajte da obnovite vaš Wallet koristeći vaše papirne rezervne kopije Mnemonic fraze. Proverite da li informacije o kolačićima generisane nakon obnove odgovaraju onima koje ste prvobitno zapisali. Ako odgovaraju, možete biti sigurni da su vaše papirne rezervne kopije pouzdane. Da biste saznali više o tome kako izvesti test oporavka, molimo vas da pogledate ovaj drugi vodič :


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Primite bitkoine


Sada kada je vaš Bitcoin Wallet postavljen, spremni ste da primite svoj prvi Sats! Jednostavno kliknite na dugme "*Receive*" u Green aplikaciji.


![JADE-PLUS-GREEN](assets/fr/35.webp)


Green prikazuje prijem Address, ali pre nego što ga upotrebite, važno je proveriti ga na Jade kako biste potvrdili da zaista pripada našem Wallet. Da biste to uradili, kliknite na dugme "*Verify on device*".


![JADE-PLUS-GREEN](assets/fr/36.webp)


Proveri na Jade da li je Address isti kao na Green, zatim klikni na dugme da potvrdiš.


![JADE-PLUS-GREEN](assets/fr/37.webp)


Sada možete podeliti Address sa platiocem da biste primili bitkoine u vaš Wallet. Kada se transakcija emituje na mreži, pojaviće se u vašem Wallet. Sačekajte dok ne dobijete dovoljno potvrda da biste smatrali transakciju konačnom.


![JADE-PLUS-GREEN](assets/fr/38.webp)


## Pošalji bitkoine


Sa bitcoinima u vašem Wallet, sada možete i slati bitcoine. Kliknite na "*Pošalji*".


![JADE-PLUS-GREEN](assets/fr/39.webp)


Na sledećoj stranici unesite primalacov Address. Možete ga uneti ručno ili skenirati QR kod.


![JADE-PLUS-GREEN](assets/fr/40.webp)


Izaberite iznos plaćanja.


![JADE-PLUS-GREEN](assets/fr/41.webp)


Na dnu ekrana, možete odabrati stopu naknade za ovu transakciju. Imate izbor da pratite preporuke aplikacije ili da prilagodite svoje naknade. Što je naknada viša u odnosu na druge transakcije na čekanju, vaša transakcija će biti brže obrađena. Za informacije o tržištu naknada, posetite [Mempool.space](https://Mempool.space/) u sekciji "*Transaction Fees*".


![JADE-PLUS-GREEN](assets/fr/42.webp)


Kliknite na "*Next*" da biste pristupili ekranu sažetka transakcije. Proverite da li su Address, iznos i naknade tačni.


![JADE-PLUS-GREEN](assets/fr/43.webp)


Ako sve bude u redu, pomerite dugme Green na dnu ekrana udesno da potpišete i emitujete transakciju na mreži Bitcoin.


![JADE-PLUS-GREEN](assets/fr/44.webp)


Sada se od vas traži da potvrdite transakciju na Jade.


![JADE-PLUS-GREEN](assets/fr/45.webp)


Uverite se da je Address primaoca tačan. Kliknite na kvačicu da potvrdite.


![JADE-PLUS-GREEN](assets/fr/46.webp)


Proverite da li je iznos naplate tačan, zatim potvrdite.


![JADE-PLUS-GREEN](assets/fr/47.webp)


Vaša transakcija je potpisana i emitovana sa Green.


![JADE-PLUS-GREEN](assets/fr/48.webp)


Čestitamo, sada znate kako da postavite i koristite Jade Plus sa Blockstream Green mobilnom aplikacijom, putem Bluetooth veze. Ako ste smatrali da je ovaj vodič koristan, bio bih zahvalan ako biste ostavili Green palac ispod. Slobodno podelite ovaj članak na vašim društvenim mrežama. Hvala što delite!


Da biste stvari podigli na viši nivo, preporučujem ovaj vodič o Jade Plus, gde ga konfigurišemo sa Sparrow Wallet softverom u QR režimu. Takođe ćete naučiti kako da koristite napredna podešavanja vašeg Hardware Wallet:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262


