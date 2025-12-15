---
name: Satochip x SeedSigner
description: Kako koristiti Satochip sa vašim SeedSigner-om?
---

![cover](assets/cover.webp)



*Zahvaljujući [Crypto Guide](https://www.youtube.com/@CryptoGuide/) za njegov fork firmware SeedSigner-a za podršku pametnim karticama, koji ćemo koristiti u ovom vodiču



---

Satochip je wallet pametna kartica-format hardver sa EAL6+ sertifikovanim sigurnosnim elementom, jednim od najviših sigurnosnih standarda. Dizajniran je i proizveden od strane belgijske kompanije istog imena: Satochip.



Po ceni od oko €25, Satochip se izdvaja od konkurencije zbog odličnog odnosa cene i kvaliteta. Zahvaljujući sigurnom čipu, pruža otpornost na fizičke napade. Štaviše, izvorni kod njegovog apleta je potpuno otvorenog koda, licenciran pod *AGPLv3*.



S druge strane, njegov format nameće određena funkcionalna ograničenja. Glavni nedostatak Satochip-a je odsustvo integrisanog ekrana: korisnici stoga moraju potpisivati transakcije naslepo, oslanjajući se isključivo na ekran svog računara.



Da bi se prevazišla ova slabost, posebno zanimljiva konfiguracija je korišćenje u kombinaciji sa SeedSigner-om. U ovom podešavanju, komunikacija više ne odvija direktno između računara i Satochip-a, već putem razmene QR kodova između računara i SeedSigner-a. SeedSigner tada deluje kao ekran poverenja: prikazuje informacije koje treba potpisati, dok sam potpis obavlja Satochip. Za razliku od konvencionalne upotrebe SeedSigner-a (ili čak upotrebe u kombinaciji sa Seedkeeper-om), seed nikada nije učitan u SeedSigner. SeedSigner tako postaje ekran za Satochip, eliminišući rizike povezane sa slepim potpisivanjem.



Ako problem posmatramo s druge strane, korišćenje SeedSigner-a sa Satochip-om popunjava veliku prazninu u SeedSigner-u: mogućnost čuvanja i korišćenja seed unutar secure element.



Po mom mišljenju, ova konfiguracija nudi nekoliko prednosti u odnosu na konvencionalne hardverske novčanike:




- Satochip košta oko €25, a pošto je applet open-source, možete ga sami instalirati na praznu pametnu karticu. Zatim treba dodati cenu SeedSigner komponenti i ekstenzije za čitanje pametnih kartica: u zavisnosti od toga gde kupujete ovaj hardver, ukupna cena bi trebala biti između €70 i €100.
- Sav softver uključen u postavku je otvorenog koda: SeedSigner firmware i Satochip applet.
- Imate koristi od sertifikovanog sigurnosnog elementa.
- Konfiguracija se može obaviti potpuno DIY, bez pribegavanja hardveru eksplicitno namenjenom za Bitcoin upotrebu, što može pružiti oblik uverljive poricljivosti i otpornosti na određene spoljne pretnje (uključujući, u zavisnosti od zemlje, pritisak države). Ovo je takođe zanimljivo rešenje ako je pristup komercijalnim hardverskim novčanicima ograničen ili nemoguć u vašem regionu.




## 1. Potrebni materijali



Da biste izvršili ovu postavku, biće vam potrebne sledeće stavke:




- Uobičajena oprema potrebna za klasični SeedSigner:
 - Raspberry Pi Zero sa GPIO pinovima,
 - 1.3" Waveshare ekran,
 - kompatibilna kamera,
 - microSD kartica.



![Image](assets/fr/01.webp)





- Komplet za proširenje SeedSigner, dostupan [u zvaničnoj Satochip prodavnici](https://satochip.io/product/seedsigner-extension-kit/), omogućava vam da čitate i pišete na pametnu karticu direktno sa vašeg SeedSigner-a. Druga opcija je korišćenje [eksternog čitača pametnih kartica](https://satochip.io/product/chip-card-reader/), koji se može povezati kablom na Micro-USB port na Raspberry Pi-ju. Međutim, nisam lično testirao ovo rešenje;
- [A Satochip](https://satochip.io/product/satochip/), ili alternativno [prazna pametna kartica](https://satochip.io/product/card-for-diy-project/) na koju možete instalirati Satochip applet (komplet za proširenje koji prodaje Satochip već uključuje praznu pametnu karticu). Satochipov komplet za proširenje takođe podržava format [SIM JavaCard](https://satochip.io/product/blank-sim-javacard-for-diy-project/). Dakle, možete se odlučiti za ovaj format ako vam više odgovara.



![Image](assets/fr/02.webp)



Za više detalja o opremi potrebnoj za sastavljanje SeedSignera, molimo pogledajte Prvi deo ovog drugog vodiča:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Instaliraj firmware



Da biste koristili svoj SeedSigner sa Satochip-om, potrebno je da instalirate alternativni firmware, drugačiji od originalnog SeedSigner-a, kako biste podržali čitanje pametnih kartica. Za ovo, [preporučujem korišćenje fork od "**3rdIteration**"](https://github.com/3rdIteration/seedsigner). Preuzmite [najnoviju verziju slike](https://github.com/3rdIteration/seedsigner/releases) (`.zip`) koja odgovara modelu Raspberry Pi koji koristite.



![Image](assets/fr/03.webp)



Ako već nemate, preuzmite softver [Balena Etcher] (https://etcher.balena.io/), zatim nastavite na sledeći način:




- Umetnite microSD karticu u vaš računar;
- Pokreni Etcher ;
- Izaberite `.zip` datoteku koju ste upravo preuzeli;
- Izaberite microSD karticu kao cilj;
- Kliknite na `Flash!`.



![Image](assets/fr/04.webp)



Sačekajte dok se proces ne završi: vaša microSD kartica je sada spremna za upotrebu. Sada možete preći na sklapanje vašeg uređaja.



Za više detalja o instalaciji firmvera i verifikaciji softvera (korak koji vam toplo preporučujem da preduzmete), pogledajte sledeći tutorijal:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Sastavljanje čitača pametnih kartica



Počnite instaliranjem kamere na Raspberry Pi Zero, pažljivo je umetnite u pin za kameru i zaključajte crnom zaklopkom. Zatim postavite Pi na dno kućišta, pazeći da poravnate portove sa odgovarajućim otvorima.



![Image](assets/fr/05.webp)



Zatim priključite čitač pametnih kartica na GPIO pinove Raspberry Pi Zero.



![Image](assets/fr/06.webp)



Prevucite plastični poklopac preko čitača pametnih kartica dok ne bude pravilno postavljen.



![Image](assets/fr/07.webp)



Zatim dodajte ekran na GPIO pinove ekstenzije.



![Image](assets/fr/08.webp)



Konačno, ubacite microSD karticu koja sadrži firmware u bočni port na Raspberry Pi Zero.



![Image](assets/fr/09.webp)



Sada možete povezati svoj SeedSigner ili preko Micro-USB porta na Raspberry Pi Zero, ili preko USB-C porta na ekstenziji. Oba opcije rade. Sačekajte nekoliko sekundi za pokretanje, zatim bi trebalo da se pojavi ekran dobrodošlice.



![Image](assets/fr/10.webp)



Za više detalja o početnom podešavanju vašeg SeedSigner-a, preporučujem da pogledate deo 4 sledećeg tutorijala:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb


## 4. Programirajte pametnu karticu sa Satochip appletom (opciono)



Ako već posedujete Satochip, možete preskočiti ovaj korak i preći direktno na korak 4. U ovom delu ćemo pogledati kako instalirati Satochip aplet na praznu pametnu karticu (uradi sam metoda). Aplet je jednostavno mali program koji radi na pametnoj kartici i omogućava nam upravljanje specifičnim funkcijama.



Da biste započeli, otvorite meni `Tools > Smartcard Tools` na vašem SeedSigner-u.



![Image](assets/fr/11.webp)



Zatim izaberite `DIY Tools > Install Applet`.



![Image](assets/fr/12.webp)



Umetnite svoju pametnu karticu u čitač SeedSigner, sa čipom okrenutim nadole, i odaberite `Satochip` aplet.



![Image](assets/fr/13.webp)



Molimo vas da budete strpljivi tokom instalacije: proces može potrajati nekoliko desetina sekundi.



![Image](assets/fr/14.webp)



Kada je aplet uspešno instaliran, možete preći na korak 4.



![Image](assets/fr/15.webp)




## 5. Kreiranje i čuvanje seed



### 5.1. Generiši seed



Sada kada vam sav hardver i softver rade ispravno, možete nastaviti sa kreiranjem vašeg Bitcoin portfolija. Da biste to uradili, priključite vaš SeedSigner, zatim generate vaš seed kao sa konvencionalnim SeedSigner-om, bilo bacanjem kockica ili fotografisanjem:




- Idite na meni `Alati > Kamera / Bacanje kockica`;
- Zatim pratite proces generisanja entropije prema odabranoj metodi;
- Na kraju, napravite rezervnu kopiju seed na fizičkom mediju i pažljivo proverite rezervnu kopiju.



![Image](assets/fr/16.webp)



Ako želite da vidite detalje ove procedure, molimo vas da pratite deo 5 ovog tutorijala:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

### 5.2. Čuvanje seed na Seedkeeper-u



Jednom kada je seed generisan, to je jedini trenutak kada se nalazi u RAM-u SeedSignera. U mom slučaju, želim da ga sačuvam na [Seedkeeper](https://satochip.io/product/seedkeeper/), još jedan Satochip proizvod dizajniran za čuvanje tajni. Koristiću ovaj uređaj kao poslednju opciju, u slučaju gubitka mog Satochipa.



Strategija bekapa izabrana ovde zavisi od vaših preferencija, ali je neophodno imati bar jednu kopiju vaše mnemoničke fraze, bilo na fizičkom mediju (papir ili metal) ili, kao ovde, u Seedkeeper-u. Takođe možete umnožiti broj bekapa po potrebi. Za više informacija o strategijama bekapa portfolija, predlažem da pročitate ovaj tutorijal :



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Da biste napravili rezervnu kopiju vašeg seed na Seedkeeper-u, idite direktno na meni `Backup Seed`.



![Image](assets/fr/17.webp)



Zatim umetnite svoj Seedkeeper u čitač pametnih kartica i izaberite `To SeedKeeper`.



![Image](assets/fr/18.webp)



Unesite svoj PIN da ga otključate.



![Image](assets/fr/19.webp)



Izaberite `Label` kako biste lako identifikovali različite tajne sačuvane na Seedkeeper-u. Možete, na primer, jednostavno zadržati otisak wallet ili eksplicitno naznačiti `Seed`. Izbor zavisi od vaših preferencija i rizika.



![Image](assets/fr/20.webp)



Ako se vaša strategija bekapa oslanja isključivo na ovaj Seedkeeper, toplo preporučujem da odmah sprovedete test praznog oporavka, a zatim uporedite otiske prstiju kako biste proverili da li bekap funkcioniše.



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

PIN kod za Seedkeeper treba da bude što duži i nasumičan, kako bi se sprečili pokušaji nasilnog probijanja u slučaju fizičkog kompromitovanja kartice. Takođe, trebalo bi da čuvate rezervnu kopiju ovog PIN koda, smeštenu na drugoj lokaciji od Seedkeeper-a. Bez ovog PIN-a, nećete moći da pristupite mnemoničkom zapisu u Seedkeeper-u, i vaši bitkoini će biti trajno izgubljeni.



### 5.3. Sačuvaj seed na Satochip



Sada kada je vaš portfolio generisan, sačuvan i verifikovan, prebacićemo ga na Satochip. Da biste to uradili, uverite se da je seed učitan u RAM SeedSignera. Zatim idite na `Tools > Smartcard Tools > Satochip Functions`.



![Image](assets/fr/21.webp)



Umetnite svoj Satochip u čitač pametnih kartica, zatim odaberite `Initialise with Seed`.



![Image](assets/fr/22.webp)



Uređaj vas poziva da unesete Satochip PIN kod; pošto je kartica nova i neinicijalizovana, PIN još ne postoji. Unesite bilo koji kod da preskočite ovaj korak (nije blokirajući).



![Image](assets/fr/23.webp)



SeedSigner detektuje da vaš Satochip nije inicijalizovan. Kliknite `Razumem` da potvrdite.



![Image](assets/fr/24.webp)



Zatim možete postaviti Satochip PIN kod, od 4 do 16 karaktera. Da biste pojačali sigurnost vašeg wallet, izaberite dug, nasumičan kod: to je jedina zaštita protiv fizičkog pristupa vašoj mnemonik frazi.



Zapamtite da sačuvate ovaj PIN čim bude kreiran, bilo u sigurnom menadžeru lozinki ili na fizičkom mediju, u zavisnosti od vaše lične strategije. U potonjem slučaju, budite sigurni da nikada ne čuvate medij koji sadrži PIN na istom mestu kao vaš Satochip, inače će zaštita postati beskorisna. Važno je imati rezervnu kopiju: **Bez ovog PIN-a, nećete moći pristupiti svom seed, i vaši bitkoini će zauvek biti izgubljeni**.



![Image](assets/fr/25.webp)



SeedSigner vas zatim pita koji seed da uvezete u Satochip. Izaberite onaj čiji otisak prsta odgovara portfoliju koji ste upravo kreirali.



![Image](assets/fr/26.webp)



Vaš seed je sada uvezen u Satochip.



![Image](assets/fr/27.webp)



Sada možete isključiti svoj SeedSigner.



Ako želite da koristite passphrase BIP39 za poboljšanje sigurnosti vašeg wallet, molimo vas da pogledate deo 6 ovog vodiča:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 6. Uvezi wallet u Sparrow



Sada kada je vaš portfolio pokrenut, uvešćemo njegove javne informacije ("*keystore*") u Sparrow Wallet ili neki drugi softver za upravljanje portfoliom. Ovaj softver će se koristiti za kreiranje, distribuciju i praćenje vaših transakcija. Međutim, neće biti u mogućnosti da ih potpiše, jer samo Satochip (i bilo koje rezervne kopije) drže privatne ključeve potrebne za ovu operaciju.



### 6.1 Priprema SeedSigner-a i Satochip-a



Umetnite microSD karticu koja sadrži operativni sistem, a zatim uključite vaš SeedSigner. Za sada, ne može ništa da uradi, jer još uvek ne zna vaš seed. Moraćete da počnete tako što ćete umetnuti Satochip u čitač pametnih kartica, pošto je to onaj koji drži vaš seed.



Sa početnog ekrana, pristupite meniju `Alati > Alati za pametne kartice > Satochip funkcije`.



![Image](assets/fr/28.webp)



Zatim kliknite na `Export Xpub`.



![Image](assets/fr/29.webp)



Odaberite tip portfolija. U našem slučaju, to je jedan portfolio: odaberite `Single Sig`.



![Image](assets/fr/30.webp)



Sledeći je izbor standarda skriptovanja. Izaberite najnoviji: `Native SegWit`.



![Image](assets/fr/31.webp)



Na kraju, izaberite `Koordinator`, tj. softver za upravljanje portfoliom koji želite da koristite. Ovde ćemo koristiti Sparrow Wallet.



![Image](assets/fr/32.webp)



Pojavljuje se poruka upozorenja: ovo je potpuno normalno. Prošireni javni ključ (`xpub`) omogućava vam da vidite sve adrese izvedene iz vašeg seed (na prvom nalogu). Međutim, ne omogućava pristup vašim sredstvima: njegovo otkrivanje bi ugrozilo vašu privatnost, ali ne i sigurnost vaših bitkoina. Drugim rečima, omogućava vam da posmatrate svoje bilanse, ali ne i da ih trošite.



Kliknite na `Razumem`.



![Image](assets/fr/33.webp)



Zatim unesite PIN kod vašeg Satochip-a da ga otključate. Ovo je kod koji ste definisali i sačuvali u koraku 5.



![Image](assets/fr/34.webp)



Na kraju, kliknite na `Export Xpub` ako ste zadovoljni prikazanim informacijama.



![Image](assets/fr/35.webp)



SeedSigner zatim generiše vaš xpub u obliku dinamičkog QR koda, koji sadrži sve podatke potrebne za upravljanje vašim portfoliom u Sparrow Wallet. Možete podesiti osvetljenost ekrana pomoću džojstika kako biste olakšali skeniranje QR koda.



### 6.2 Uvoz novog portfolija u Sparrow Wallet



Uverite se da je softver Sparrow Wallet instaliran na vašem računaru. Ako ne znate kako da ga preuzmete, proverite njegovu autentičnost i pravilno ga instalirajte, pogledajte naš kompletan vodič na tu temu :



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Na vašem računaru, otvorite Sparrow Wallet, zatim u meniju kliknite `File → Import Wallet`.



![Image](assets/fr/36.webp)



Pomeri dole do `SeedSigner`, zatim izaberi `Skeniraj...`. Tvoja veb kamera će biti aktivirana: skeniraj dinamički QR kod prikazan na ekranu tvog SeedSigner-a.



![Image](assets/fr/37.webp)



Dodelite ime svom portfoliju, zatim kliknite na `Create Wallet`. Sparrow će vas zatim zamoliti da postavite lozinku za zaključavanje lokalnog pristupa ovom wallet. Izaberite jaku lozinku: ona štiti vaše podatke u Sparrow (javne ključeve, adrese, oznake i istoriju transakcija). Međutim, ova lozinka nije potrebna za obnavljanje wallet u budućnosti: biće potrebna samo vaša mnemonička fraza (i moguće vaš passphrase).



Preporučujem da sačuvate ovu lozinku u menadžeru lozinki, kako biste izbegli njen gubitak.



![Image](assets/fr/38.webp)



Vaš keystore je uspešno uvezen.



![Image](assets/fr/39.webp)



Sada proverite da li se `Master fingerprint` prikazan u Sparrow Wallet poklapa sa onim koji je prethodno pronađen na vašem SeedSigner-u.



SeedSigner će zatim tražiti da skenirate nasumičnu adresu za primanje sa vašeg Sparrow wallet kako biste potvrdili validnost uvoza.



![Image](assets/fr/40.webp)



Vaš Satochip (preko SeedSigner) i Sparrow Wallet su sada sigurno povezani. Sparrow deluje kao kompletan upravljački interfejs, dok Satochip ostaje jedini uređaj sposoban za potpisivanje vaših transakcija. Sada ste spremni da primate i šaljete bitkoine u potpuno vazdušno izolovanoj konfiguraciji.



![Image](assets/fr/41.webp)



## 7. Primanje i slanje bitkoina



Vaš Satochip i Sparrow Wallet su sada konfigurisani da rade zajedno. U ovom odeljku ćemo objasniti korak po korak kako primati i slati bitkoine u ovom režimu.



### 7.1 Primanje bitkoina



#### 7.1.1 Generisanje adrese za prijem



Na vašem računaru, otvorite Sparrow Wallet i otključajte vaš `Satochip-SeedSigner` wallet koristeći vašu lozinku. Proverite da li je softver povezan sa serverom (indikator u donjem desnom uglu). Zatim, u bočnoj traci, kliknite na `Receive`.



![Image](assets/fr/42.webp)



Pojavljuje se nova Bitcoin adresa. Naći ćete:




- Adresa u tekstualnom formatu (počinje sa `bc1q...` ako koristite P2WPKH, kao u ovom primeru) ;
- Povezani QR kod ;
- Polje `Label`, korisno za praćenje vaših transakcija.



Toplo preporučujem da dodate oznaku svakom bitcoin priznanici u vašem wallet. Ovo će vam pomoći da lako identifikujete poreklo svakog UTXO i bolje upravljate svojom privatnošću. Da biste saznali više o ovoj važnoj temi, pogledajte posvećenu obuku na Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Da biste dodali oznaku, jednostavno unesite ime u polje `Label`, a zatim potvrdite.



Na primer:



```txt
Label : Sale of the Raspberry Pi Zero
```



Vaša adresa je sada povezana sa ovom oznakom u svim Sparrow odeljcima.



![Image](assets/fr/43.webp)



#### 7.1.2 Address verifikacija na SeedSigner



Pre nego što saopštite svoju adresu za primanje platiocu, važno je proveriti da li ona pripada vašem seed. Ovaj korak osigurava da će vaš Satochip moći da potpisuje transakcije povezane sa ovom adresom. Takođe sprečava potencijalne napade gde bi Sparrow prikazao lažnu adresu. Imajte na umu da Sparrow radi u nesigurnom okruženju (vašem računaru), čija je površina napada znatno veća od one kod vašeg Satochipa, koji je potpuno izolovan. Zato nikada ne bi trebalo slepo verovati adresama prikazanim u Sparrow pre nego što ih proverite na svom wallet hardveru.



U Sparrow, kliknite na QR kod adrese da ga uvećate: zatim će biti prikazan preko celog ekrana.



![Image](assets/fr/44.webp)



Na vašem SeedSigner-u, umetnite Satochip u čitač, zatim iz glavnog menija izaberite `Skeniraj`. Skenirajte QR kod prikazan na vašem računaru, zatim izaberite `Koristi Satochip karticu`.



![Image](assets/fr/45.webp)



Zatim potvrdite tip skripte koja se koristi (u ovom slučaju, `Native SegWit`), unesite Satochip PIN kod da ga otključate i potvrdite informacije o `xpub`.



![Image](assets/fr/46.webp)



Ako se skenirana adresa poklapa sa onom izvedenom iz vašeg seed, SeedSigner će prikazati poruku: `Address Verified`.



![Image](assets/fr/47.webp)



Možete tada biti sigurni da adresa pripada vašem portfoliju.



#### 7.1.3 Prijem sredstava



Sada možete poslati ovu adresu u tekstualnom obliku ili putem njenog QR koda osobi ili odeljenju koje treba da vam pošalje satse. Kada transakcija bude emitovana na mreži, pojaviće se u kartici `Transakcije` Sparrow Wallet.



![Image](assets/fr/48.webp)



### 7.2 Pošalji bitkoine



Slanje bitcoina pomoću Satochip-SeedSigner konfiguracije uključuje 3 koraka:




- Kreiranje transakcije u Sparrow ;
- Potpisivanje ove transakcije na Satochip-u, putem SeedSigner-a ;
- Konačno, transakcija se emituje preko mreže sa Sparrow.



Sva razmena između dva uređaja odvija se isključivo putem QR kodova.



#### 7.2.1 Kreiranje transakcije u Sparrow



U Sparrow Wallet, možete kreirati transakciju klikom na karticu `Send` u bočnoj traci s leve strane. Međutim, ja preferiram korišćenje kartice `UTXOs`, koja vam omogućava da vežbate *Coin Control*. Ova metoda nudi preciznu kontrolu nad potrošenim UTXO-ima, kako biste ograničili informacije otkrivene tokom vaših transakcija.



U kartici `UTXOs` izaberite novčiće koje želite da potrošite, zatim kliknite na `Send Selected`.



![Image](assets/fr/49.webp)



Zatim popunite polja transakcije:




- U `Plati`, nalepi adresu primaoca ili skeniraj njihov QR kod koristeći ikonu kamere ;
- U `Label`, dodajte oznaku za praćenje ovog troška;
- U polje `Amount` unesite iznos koji treba poslati;
- Konačno, izaberite stopu naplate u skladu sa trenutnim uslovima mreže (procene su dostupne na [mempool.space](https://mempool.space/)).



Kada popunite sva polja, pažljivo pregledajte informacije, zatim kliknite na `Create Transaction >>`.



![Image](assets/fr/50.webp)



Proverite detalje transakcije još jednom radi tačnosti, zatim kliknite na `Finalize Transaction for Signing`.



![Image](assets/fr/51.webp)



Transakcija je sada spremna, ali još nije potpisana. Da biste prikazali [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/psbt) kao QR kod, kliknite na `Prikaži QR`.



![Image](assets/fr/52.webp)



#### 7.2.2 Potpisivanje transakcije sa Satochip



Uključite svoj SeedSigner i umetnite svoj Satochip kao i obično. Sa početnog ekrana, izaberite `Scan`, zatim skenirajte QR kod prikazan na Sparrow.



![Image](assets/fr/53.webp)



Odaberite opciju `Use Satochip card`.



![Image](assets/fr/54.webp)



Unesite svoj PIN kod da otključate pametnu karticu.



![Image](assets/fr/55.webp)



SeedSigner detektuje da je ovo PSBT i prikazuje rezime transakcije:




   - Iznos poslat,
   - Adrese destinacije,
   - Povezani troškovi transakcije.



Kliknite na `Review Details` i pažljivo pregledajte sve informacije direktno na SeedSigner ekranu. Najvažnije tačke za proveru su poslati iznosi, odredišne adrese i naknade za transakciju.



![Image](assets/fr/56.webp)



Ako je sve u redu, izaberite `Approve PSBT` da potpišete transakciju koristeći Satochip.



![Image](assets/fr/57.webp)



Kada je potpisivanje završeno, SeedSigner generiše novi QR kod koji sadrži potpisanu transakciju, spremnu za skeniranje od strane Sparrow.



#### 7.2.3 Emitovanje transakcije sa Sparrow



Sada kada je transakcija potpisana i validirana, ostaje samo da je emitujete na Bitcoin mreži kako bi je rudar mogao uključiti u blok. U Sparrow, kliknite na `Skeniraj QR`.



![Image](assets/fr/58.webp)



Prikažite QR kod prikazan na vašem SeedSigner-u (onaj koji sadrži potpisanu transakciju) veb kameri. Sparrow će zatim prikazati sve detalje transakcije. Proverite da su sve informacije tačne, a zatim kliknite na "Emituj Transakciju" da biste je emitovali na Bitcoin mreži.



![Image](assets/fr/59.webp)



Vaša transakcija je sada preneta na mrežu. Možete pratiti njenu potvrdu u kartici `Transakcije` Sparrow Wallet.



![Image](assets/fr/60.webp)



## 8. Vratite svoj wallet



Kao što smo videli u prethodnim odeljcima, u zavisnosti od vaše sigurnosne strategije, postoji nekoliko načina za pravljenje rezervne kopije vaše fraze za oporavak pored vašeg Satochip-a:




- Korišćenje klasičnog *SeedQR* sa SeedSigner-om ;
- Snimanjem mnemoničke fraze na fizički medij;
- Ili čuvanjem na Seedkeeper-u, kako je objašnjeno u odeljku 5.2.



U svakom slučaju, postoje 2 glavne situacije u kojima treba da intervenišete: gubitak Satochip-a ili gubitak SeedSigner-a. Pogledajmo kako reagovati u svakoj od ovih situacija.



### 8.1. Preuzmite svoj wallet pomoću Satochip



Ako i dalje imate svoj Satochip, ali vam je SeedSigner pokvaren ili izgubljen, situacija je prilično jednostavna za upravljanje, jer je vaš wallet i dalje u Satochip-u.



Najbolja opcija je preporučiti potrebne komponente i izgraditi novi SeedSigner od nule. Kako je ovo uređaj "bez stanja", nije važno da li koristite isti ili drugi SeedSigner: sve dok možete umetnuti svoj Satochip, sve će raditi normalno.



Ako ne želite da ponovo izgradite jedan, možete takođe koristiti svoj Satochip na klasičan način, tj. direktno sa vašeg računara, bez prolaska kroz SeedSigner. Ova metoda funkcioniše savršeno, ali značajno smanjuje sigurnost vašeg Bitcoin wallet: gubite "*air-gapped*" izolaciju i sada morate potpisivati naslepo, pošto je SeedSigner delovao kao pouzdan ekran. Međutim, ovo može biti privremeno rešenje u hitnim slučajevima, ili ako niste u mogućnosti da ponovo izgradite SeedSigner.



Da biste to uradili, biće vam potreban USB čitač pametnih kartica ili NFC čitač. Otvorite wallet koji želite da vratite u Sparrow, zatim idite na karticu `Settings` i kliknite na `Replace`.



![Image](assets/fr/61.webp)



Umetnite svoj Satochip u čitač pametnih kartica povezan s računarom, zatim kliknite na `Import` pored `Satochip`.



![Image](assets/fr/62.webp)



Na kraju, unesite svoj PIN pametne kartice da biste je otključali. Zatim ćete moći pristupiti svom wallet, kreirati transakcije i potpisivati ih direktno koristeći povezani Satochip.



### 8.2. Preuzmite svoj portfolio pomoću SeedSigner



Drugi, delikatniji scenario je kada izgubite pristup svom Satochip-u koji sadrži seed: bilo da je pokvaren, izgubljen, ukraden ili ste zaboravili njegov PIN kod. Ako je vaš Satochip ukraden ili izgubljen, toplo preporučujemo da, kada vam pristup sredstvima bude vraćen, odmah prebacite svoje bitkoine na potpuno novi wallet, generisan sa drugačijim seed. Ovo osigurava da potencijalni napadač nikada ne može dobiti pristup vašim satss-ima.



Da biste ponovo dobili pristup svom portfoliju i premestili svoja sredstva, jednostavno učitajte svoj seed u SeedSigner. U zavisnosti od medija za bekap koji ste koristili, imate nekoliko opcija:





- Unesite svoju mnemoniku ručno u meniju `Seeds > Enter 12-word seed`.



![Image](assets/fr/63.webp)





- Skenirajte svoj *SeedQR* klikom na dugme `Scan` na početnoj stranici.



![Image](assets/fr/64.webp)





- Ili učitajte svoj seed iz Seedkeeper-a, putem menija `Seeds > From SeedKeeper` (ovo je metoda koju koristim u ovom vodiču). Jednostavno ćete morati uneti Seedkeeper PIN i odabrati tajnu koja će se koristiti kao seed na SeedSigner-u.



![Image](assets/fr/65.webp)



Kada se seed učita u SeedSigner, bez obzira na metodu koju koristite, moći ćete da potpišete jednu ili više skeniranih transakcija kako biste premestili svoje bitkoine na novi, nekompromitovani wallet. Da biste saznali kako to da uradite, pogledajte deo 7.2 sledećeg tutorijala:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

Sada znate kako da koristite Satochip za sigurno upravljanje vašim Bitcoin portfoliom u kombinaciji sa SeedSigner-om.



Ako vas je ova postavka uverila, ne oklevajte da podržite projekte koji je omogućavaju:




- Kupovinom vaše opreme direktno [na Satochip vebsajtu](https://satochip.io/shop/);
- Doniranjem [projektu SeedSigner](https://seedsigner.com/donate/);
- Pretplatom na [Crypto Guide-ov YouTube kanal](https://www.youtube.com/@CryptoGuide/), koji vodi osoba koja održava GitHub repozitorijum u kojem se nalazi modifikovani firmware koji smo koristili u ovom vodiču.