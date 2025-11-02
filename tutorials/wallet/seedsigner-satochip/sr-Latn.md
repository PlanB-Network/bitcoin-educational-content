---
name: Satochip x SeedSigner
description: Kako koristiti Satochip sa vašim SeedSigner-om?
---

![cover](assets/cover.webp)



*Zahvaljujući [Crypto Guide](https://www.youtube.com/@CryptoGuide/) za njegov Fork firmware SeedSigner-a za podršku pametnim karticama, koji ćemo koristiti u ovom vodiču



---

Satochip je Hardware Wallet u formatu pametne kartice, sa sigurnosnim elementom sertifikovanim na EAL6+ nivou, jednim od najviših sigurnosnih standarda. Dizajniran je i proizveden od strane belgijske kompanije istog imena: Satochip.



Po ceni od oko €25, Satochip se izdvaja od konkurencije zbog odličnog odnosa cene i kvaliteta. Zahvaljujući sigurnom čipu, pruža otpornost na fizičke napade. Štaviše, izvorni kod njegovog appleta je potpuno otvorenog koda, licenciran pod *AGPLv3*.



S druge strane, njegov format nameće određena funkcionalna ograničenja. Glavni nedostatak Satochip-a je odsustvo integrisanog ekrana: korisnici stoga moraju potpisivati transakcije naslepo, oslanjajući se isključivo na ekran svog računara.



Da bi se prevazišla ova slabost, posebno zanimljiva konfiguracija je korišćenje u kombinaciji sa SeedSigner-om. U ovom podešavanju, komunikacija više ne odvija direktno između računara i Satochip-a, već putem razmene QR kodova između računara i SeedSigner-a. SeedSigner tada deluje kao ekran poverenja: prikazuje informacije koje treba potpisati, dok sam potpis obavlja Satochip. Za razliku od konvencionalne upotrebe SeedSigner-a (ili čak upotrebe u kombinaciji sa Seedkeeper-om), seed se nikada ne učitava u SeedSigner. SeedSigner tako postaje ekran za Satochip, eliminišući rizike povezane sa slepim potpisivanjem.



Ako problem posmatramo s druge strane, korišćenje SeedSigner-a sa Satochip-om popunjava veliku prazninu u SeedSigner-u: mogućnost skladištenja i korišćenja seed unutar secure element.



Po mom mišljenju, ova konfiguracija nudi nekoliko prednosti u odnosu na konvencionalne hardverske novčanike:




- Satochip košta oko 25 €, a pošto je applet otvorenog koda, možete ga sami instalirati na praznu pametnu karticu. Zatim morate dodati cenu SeedSigner komponenti i ekstenzije za čitanje pametnih kartica: u zavisnosti od toga gde kupujete ovaj hardver, ukupna cena bi trebala biti između 70 € i 100 €.
- Sav softver uključen u postavljanje je otvorenog koda: SeedSigner firmware i Satochip applet.
- Imate koristi od sertifikovanog sigurnosnog elementa.
- Konfiguracija se može izvršiti potpuno samostalno, bez potrebe za hardverom koji je eksplicitno namenjen za upotrebu sa Bitcoin, što može pružiti oblik uverljive poricanja i otpornost na određene spoljne pretnje (uključujući, u zavisnosti od zemlje, pritisak države). Ovo je takođe zanimljivo rešenje ako je pristup komercijalnim hardverskim novčanicima ograničen ili nemoguć u vašem regionu.




## 1. Potrebni materijali



Da biste izvršili ovu postavku, biće vam potrebne sledeće stavke:




- Uobičajena oprema potrebna za klasični SeedSigner :
 - Raspberry Pi Zero sa GPIO pinovima,
 - 1.3" Waveshare ekran,
 - kompatibilna kamera,
 - microSD kartica.



![Image](assets/fr/01.webp)





- Komplet za proširenje SeedSigner, dostupan [u zvaničnoj Satochip prodavnici](https://satochip.io/product/seedsigner-extension-kit/), omogućava vam da čitate i pišete na pametnu karticu direktno sa vašeg SeedSigner-a. Druga opcija je korišćenje [eksternog čitača pametnih kartica](https://satochip.io/product/chip-card-reader/), koji se može povezati kablom na Micro-USB port na Raspberry Pi-ju. Međutim, nisam lično testirao ovo rešenje;
- [Satochip](https://satochip.io/product/satochip/), ili alternativno [prazna pametna kartica](https://satochip.io/product/card-for-diy-project/) na koju možete instalirati Satochip aplet (komplet za proširenje koji prodaje Satochip već uključuje praznu pametnu karticu). Satochipov komplet za proširenje takođe podržava format [SIM JavaCard](https://satochip.io/product/blank-sim-javacard-for-diy-project/). Dakle, možete se odlučiti za ovaj format ako vam više odgovara.



![Image](assets/fr/02.webp)



Za više detalja o opremi potrebnoj za sastavljanje SeedSigner-a, pogledajte Prvi deo ovog drugog vodiča:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Instaliraj firmware



Da biste koristili svoj SeedSigner sa Satochip-om, potrebno je da instalirate alternativni firmware, drugačiji od originalnog SeedSigner-a, kako biste podržali čitanje pametnih kartica. Za ovo, [preporučujem korišćenje Fork od "**3rdIteration**"](https://github.com/3rdIteration/seedsigner). Preuzmite [najnoviju verziju slike](https://github.com/3rdIteration/seedsigner/releases) (`.zip`) koja odgovara modelu Raspberry Pi koji koristite.



![Image](assets/fr/03.webp)



Ako već nemate, preuzmite softver [Balena Etcher] (https://etcher.balena.io/), zatim nastavite na sledeći način:




- Umetnite microSD karticu u vaš računar;
- Pokreni Etcher ;
- Izaberite `.zip` datoteku koju ste upravo preuzeli;
- Izaberite microSD karticu kao cilj;
- Kliknite na `Flash!`.



![Image](assets/fr/04.webp)



Sačekajte dok se proces ne završi: vaša microSD kartica je sada spremna za upotrebu. Sada možete preći na sklapanje vašeg uređaja.



Za više detalja o instalaciji firmvera i verifikaciji softvera (korak koji vam toplo preporučujem da preduzmete), pogledajte sledeći vodič:



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



Na kraju, ubacite microSD karticu koja sadrži firmware u bočni port na Raspberry Pi Zero.



![Image](assets/fr/09.webp)



Sada možete povezati svoj SeedSigner ili putem Micro-USB porta na Raspberry Pi Zero, ili putem USB-C porta na ekstenziji. Oba načina funkcionišu. Sačekajte nekoliko sekundi za pokretanje, zatim bi trebalo da se pojavi ekran dobrodošlice.



![Image](assets/fr/10.webp)



Za više detalja o početnom podešavanju vašeg SeedSigner-a, preporučujem da pogledate deo 4 sledećeg tutorijala:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb


## 4. Flešuj pametnu karticu sa Satochip appletom (opciono)



Ako već posedujete Satochip, možete preskočiti ovaj korak i preći direktno na korak 4. U ovom delu ćemo pogledati kako instalirati Satochip applet na praznu pametnu karticu (DIY metoda). Applet je jednostavno mali program koji radi na pametnoj kartici i omogućava nam upravljanje specifičnim funkcijama.



Da biste započeli, otvorite meni `Tools > Smartcard Tools` na vašem SeedSigner-u.



![Image](assets/fr/11.webp)



Zatim izaberite `DIY Tools > Install Applet`.



![Image](assets/fr/12.webp)



Umetnite svoju pametnu karticu u čitač SeedSigner, sa čipom okrenutim nadole, i izaberite `Satochip` applet.



![Image](assets/fr/13.webp)



Molimo budite strpljivi tokom instalacije: proces može potrajati nekoliko desetina sekundi.



![Image](assets/fr/14.webp)



Kada je aplet uspešno instaliran, možete preći na korak 4.



![Image](assets/fr/15.webp)




## 5. Kreiranje i čuvanje seed



### 5.1. generate seed



Sada kada vam sav hardver i softver rade ispravno, možete nastaviti sa kreiranjem vašeg Bitcoin portfolija. Da biste to uradili, priključite vaš SeedSigner, zatim generate vaš seed kao sa konvencionalnim SeedSigner-om, bilo bacanjem kockica ili fotografisanjem:




- Idite na meni `Alati > Kamera / Bacanje kockica`;
- Zatim pratite proces generisanja entropije prema izabranoj metodi;
- Na kraju, napravite rezervnu kopiju seed na fizičkom mediju i pažljivo proverite rezervnu kopiju.



![Image](assets/fr/16.webp)



Ako želite da vidite detalje ove procedure, molimo vas da pratite deo 5 ovog tutorijala:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

### 5.2. Čuvanje seed na Seedkeeper-u



Jednom kada je seed generisan, to je jedini put kada se nalazi u RAM-u SeedSignera. U mom slučaju, želim da ga sačuvam na [Seedkeeper](https://satochip.io/product/seedkeeper/), još jedan Satochip proizvod dizajniran za čuvanje tajni. Koristiću ovaj uređaj kao poslednju opciju, u slučaju gubitka mog Satochipa.



Strategija bekapa koja je ovde izabrana zavisi od vaših preferencija, ali je neophodno imati bar jednu kopiju vaše Mnemonic fraze, bilo na fizičkom mediju (papir ili metal) ili, kao ovde, u Seedkeeper-u. Takođe možete umnožiti broj bekapa po potrebi. Za više informacija o strategijama bekapa portfolija, predlažem da pročitate ovaj vodič:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Da biste napravili rezervnu kopiju vašeg seed na Seedkeeper-u, idite direktno na meni `Backup seed`.



![Image](assets/fr/17.webp)



Zatim umetnite svoj Seedkeeper u čitač pametnih kartica i izaberite `To SeedKeeper`.



![Image](assets/fr/18.webp)



Unesite svoj PIN da biste ga otključali.



![Image](assets/fr/19.webp)



Izaberite `Label` kako biste lako identifikovali vaše različite tajne pohranjene na Seedkeeper-u. Možete, na primer, jednostavno zadržati otisak prsta Wallet ili eksplicitno naznačiti `seed`. Izbor zavisi od vaših preferencija i rizika.



![Image](assets/fr/20.webp)



Ako se vaša strategija bekapa oslanja isključivo na ovaj Seedkeeper, toplo preporučujem da odmah izvršite test praznog oporavka, a zatim uporedite otiske prstiju kako biste proverili da li bekap funkcioniše.



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

PIN kod za Seedkeeper treba da bude što duži i nasumičan, kako bi se sprečili pokušaji brutalne sile u slučaju fizičkog kompromitovanja kartice. Takođe, trebalo bi da čuvate rezervnu kopiju ovog PIN koda, smeštenu na odvojenoj lokaciji od Seedkeeper-a. Bez ovog PIN-a, nećete moći da pristupite Mnemonic koji je uskladišten u Seedkeeper-u, i vaši bitkoini će zauvek biti izgubljeni.



### 5.3. Sačuvaj seed na Satochip



Sada kada je vaš portfolio generisan, sačuvan i proveren, prebacićemo ga na Satochip. Da biste to uradili, uverite se da je seed učitan u RAM SeedSignera. Zatim idite na `Tools > Smartcard Tools > Satochip Functions`.



![Image](assets/fr/21.webp)



Umetnite svoj Satochip u čitač pametnih kartica, zatim izaberite `Initialise with seed`.



![Image](assets/fr/22.webp)



Uređaj vas poziva da unesete Satochip PIN kod; pošto je kartica nova i neinicijalizovana, PIN još ne postoji. Unesite bilo koji kod da preskočite ovaj korak (nije blokirajući).



![Image](assets/fr/23.webp)



SeedSigner detektuje da vaš Satochip nije inicijalizovan. Kliknite `Razumem` da potvrdite.



![Image](assets/fr/24.webp)



Zatim možete postaviti Satochip PIN kod, od 4 do 16 karaktera. Da biste pojačali sigurnost vašeg Wallet, izaberite dug, nasumičan kod: to je jedina zaštita protiv fizičkog pristupa vašoj Mnemonic frazi.



Zapamtite da sačuvate ovaj PIN čim bude kreiran, bilo u sigurnom menadžeru lozinki ili na fizičkom mediju, u zavisnosti od vaše lične strategije. U potonjem slučaju, budite sigurni da nikada ne čuvate medij koji sadrži PIN na istom mestu kao vaš Satochip, inače će zaštita postati beskorisna. Važno je imati rezervnu kopiju: **bez ovog PIN-a, više nećete moći pristupiti vašem seed, i vaši bitkoini će biti trajno izgubljeni**.



![Image](assets/fr/25.webp)



SeedSigner vas zatim pita koji seed da uvezete u Satochip. Izaberite onaj čiji otisak prsta odgovara portfoliju koji ste upravo kreirali.



![Image](assets/fr/26.webp)



Vaš seed je sada importovan u Satochip.



![Image](assets/fr/27.webp)



Sada možete isključiti svoj SeedSigner.



Ako želite da koristite passphrase BIP39 za poboljšanje sigurnosti vašeg Wallet, molimo vas da pogledate deo 6 ovog tutorijala:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 6. Uvezi Wallet u Sparrow



Sada kada je vaš portfolio pokrenut, uvešćemo njegove javne informacije ("*keystore*") u Sparrow wallet ili neki drugi softver za upravljanje portfoliom. Ovaj softver će se koristiti za kreiranje, distribuciju i praćenje vaših transakcija. Međutim, neće biti u mogućnosti da ih potpiše, jer samo Satochip (i bilo koje rezervne kopije) sadrže privatne ključeve potrebne za ovu operaciju.



### 6.1 Priprema SeedSigner-a i Satochip-a



Umetnite microSD karticu koja sadrži operativni sistem, a zatim uključite vaš SeedSigner. Za sada, ne može ništa da uradi, jer još uvek ne zna vaš seed. Moraćete da počnete tako što ćete umetnuti Satochip u čitač pametnih kartica, pošto je to onaj koji drži vaš seed.



Sa početnog ekrana pristupite meniju `Tools > Smartcard Tools > Satochip Functions`.



![Image](assets/fr/28.webp)



Zatim kliknite na `Export Xpub`.



![Image](assets/fr/29.webp)



Odaberite tip portfolija. U našem slučaju, to je jedan portfolio: odaberite `Single Sig`.



![Image](assets/fr/30.webp)



Sledeći je izbor standarda skriptovanja. Izaberite najnoviji: `Native SegWit`.



![Image](assets/fr/31.webp)



Na kraju, izaberite `Koordinator`, tj. softver za upravljanje portfoliom koji želite da koristite. Ovde ćemo koristiti Sparrow wallet.



![Image](assets/fr/32.webp)



Pojavljuje se poruka upozorenja: ovo je potpuno normalno. Prošireni javni ključ (`xpub`) omogućava vam da vidite sve adrese izvedene iz vašeg seed (na prvom nalogu). Međutim, ne omogućava pristup vašim sredstvima: njegovo otkrivanje bi ugrozilo vašu privatnost, ali ne i sigurnost vaših bitkoina. Drugim rečima, omogućava vam da posmatrate svoje bilanse, ali ne i da ih trošite.



Kliknite na `Razumem`.



![Image](assets/fr/33.webp)



Zatim unesite PIN kod vašeg Satochip-a da ga otključate. Ovo je kod koji ste definisali i sačuvali u koraku 5.



![Image](assets/fr/34.webp)



Na kraju, kliknite na `Export Xpub` ako ste zadovoljni prikazanim informacijama.



![Image](assets/fr/35.webp)



SeedSigner zatim generiše vaš xpub u obliku dinamičkog QR koda, koji sadrži sve podatke potrebne za upravljanje vašim portfoliom u Sparrow wallet. Možete podesiti osvetljenost ekrana pomoću džojstika kako biste olakšali skeniranje QR koda.



### 6.2 Uvoz novog portfolija u Sparrow wallet



Uverite se da je Sparrow wallet softver instaliran na vašem računaru. Ako ne znate kako da ga preuzmete, proverite njegovu autentičnost i instalirajte ga ispravno, pogledajte naš kompletan vodič na tu temu :



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Na vašem računaru, otvorite Sparrow wallet, zatim u meniju kliknite `File → Import Wallet`.



![Image](assets/fr/36.webp)



Pomeri dole do `SeedSigner`, zatim izaberi `Skeniraj...`. Tvoja veb kamera će biti aktivirana: skeniraj dinamički QR kod prikazan na ekranu tvog SeedSigner-a.



![Image](assets/fr/37.webp)



Dodelite ime svom portfoliju, zatim kliknite na `Create Wallet`. Sparrow će vas zatim zamoliti da postavite lozinku kako biste zaključali lokalni pristup ovom Wallet. Izaberite jaku lozinku: ona štiti vaše podatke u Sparrow (javne ključeve, adrese, oznake i istoriju transakcija). Međutim, ova lozinka nije potrebna za obnavljanje Wallet u budućnosti: biće potrebna samo vaša Mnemonic fraza (i moguće vaš passphrase).



Preporučujem da sačuvate ovu lozinku u menadžeru lozinki, kako biste izbegli njen gubitak.



![Image](assets/fr/38.webp)



Vaš keystore je uspešno uvezen.



![Image](assets/fr/39.webp)



Sada proverite da li se `Master fingerprint` prikazan u Sparrow wallet poklapa sa onim koji je prethodno pronađen na vašem SeedSigner-u.



SeedSigner će zatim tražiti da skenirate nasumični prijemni Address sa vašeg Sparrow wallet kako biste potvrdili validnost uvoza.



![Image](assets/fr/40.webp)



Vaš Satochip (preko SeedSigner) i Sparrow wallet su sada sigurno povezani. Sparrow služi kao kompletan menadžment Interface, dok Satochip ostaje jedini uređaj sposoban za potpisivanje vaših transakcija. Sada ste spremni da primate i šaljete bitkoine u potpuno vazdušno izolovanoj konfiguraciji.



![Image](assets/fr/41.webp)



## 7. Primanje i slanje bitkoina



Vaš Satochip i Sparrow wallet su sada konfigurisani da rade zajedno. U ovom delu ćemo objasniti korak po korak kako primati i slati bitkoine u ovom režimu.



### 7.1 Primanje bitkoina



#### 7.1.1 Generisanje prijema Address



Na vašem računaru, otvorite Sparrow wallet i otključajte vaš `Satochip-SeedSigner` Wallet koristeći vašu lozinku. Proverite da li je softver povezan sa serverom (indikator u donjem desnom uglu). Zatim, u bočnoj traci, kliknite na `Receive`.



![Image](assets/fr/42.webp)



Pojavljuje se novi Bitcoin Address. Naći ćete:




- Address u tekstualnom formatu (počinje sa `bc1q...` ako koristite P2WPKH, kao u ovom primeru) ;
- Povezani QR kod ;
- Polje `Label`, korisno za praćenje vaših transakcija.



Toplo preporučujem da dodate oznaku svakom Bitcoin računu u vašem Wallet. Ovo će vam pomoći da lako identifikujete poreklo svakog UTXO i bolje upravljate svojom privatnošću. Da biste saznali više o ovoj važnoj temi, pogledajte posvećenu obuku na Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Da biste dodali oznaku, jednostavno unesite ime u polje `Label`, a zatim potvrdite.



Na primer:



```txt
Label : Sale of the Raspberry Pi Zero
```



Vaš Address je sada povezan sa ovom oznakom u svim Sparrow odeljcima.



![Image](assets/fr/43.webp)



#### 7.1.2 Address verifikacija na SeedSigner



Pre nego što obavestite platioca o prijemu Address, važno je proveriti da li pripada vašem seed. Ovaj korak osigurava da vaš Satochip može potpisivati transakcije povezane sa ovim Address. Takođe sprečava potencijalne napade gde bi Sparrow prikazao lažni Address. Imajte na umu da Sparrow radi u nesigurnom okruženju (vašem računaru), čija je površina napada mnogo veća od one kod vašeg Satochipa, koji je potpuno izolovan. Zato nikada ne bi trebalo slepo verovati adresama prikazanim u Sparrow pre nego što ih proverite na vašem Hardware Wallet.



U Sparrow, kliknite na QR kod Address da biste ga uvećali: zatim će biti prikazan preko celog ekrana.



![Image](assets/fr/44.webp)



Na vašem SeedSigner-u, umetnite Satochip u čitač, zatim iz glavnog menija izaberite `Skeniraj`. Skenirajte QR kod prikazan na vašem računaru, zatim izaberite `Koristi Satochip karticu`.



![Image](assets/fr/45.webp)



Zatim potvrdite tip skripte koji se koristi (u ovom slučaju, `Native SegWit`), unesite Satochip PIN kod da ga otključate i potvrdite informacije `xpub`.



![Image](assets/fr/46.webp)



Ako skenirani Address odgovara onom izvedenom iz vašeg seed, SeedSigner će prikazati poruku: `Address Verified`.



![Image](assets/fr/47.webp)



Možete tada biti sigurni da Address pripada vašem portfoliju.



#### 7.1.3 Prijem sredstava



Sada možete preneti ovaj Address u tekstualnom obliku ili putem njegovog QR koda osobi ili usluzi koja treba da vam pošalje Satss. Kada transakcija bude emitovana na mreži, pojaviće se u kartici `Transactions` Sparrow wallet.



![Image](assets/fr/48.webp)



### 7.2 Pošalji bitkoine



Slanje bitcoina pomoću Satochip-SeedSigner konfiguracije uključuje 3 koraka:




- Kreiranje transakcije u Sparrow ;
- Potpisivanje ove transakcije na Satochip-u, putem SeedSigner-a ;
- Konačno, transakcija se prenosi preko mreže sa Sparrow.



Sva razmena između dva uređaja odvija se isključivo putem QR kodova.



#### 7.2.1 Kreiranje transakcije u Sparrow



U Sparrow wallet, možete kreirati transakciju klikom na karticu `Send` u bočnoj traci s leve strane. Međutim, ja preferiram korišćenje kartice `UTXOs`, koja vam omogućava da vežbate *Coin Control*. Ova metoda nudi preciznu kontrolu nad potrošenim UTXO-ima, kako biste ograničili informacije otkrivene tokom vaših transakcija.



U kartici `UTXOs` izaberite novčiće koje želite da potrošite, zatim kliknite na `Send Selected`.



![Image](assets/fr/49.webp)



Zatim popunite polja za transakciju:




- U `Plati`, nalepi Address primaoca ili skeniraj njihov QR kod koristeći ikonu kamere ;
- U `Label`, dodajte oznaku za praćenje ovog troška;
- U polje `Amount` unesite iznos koji treba poslati;
- Na kraju, odaberite stopu punjenja prema trenutnim uslovima mreže (procene su dostupne na [Mempool.space](https://Mempool.space/)).



Kada popunite sva polja, pažljivo pregledajte informacije, zatim kliknite na `Create Transaction >>`.



![Image](assets/fr/50.webp)



Proverite detalje transakcije još jednom radi tačnosti, zatim kliknite na `Finalize Transaction for Signing`.



![Image](assets/fr/51.webp)



Transakcija je sada spremna, ali još uvek nije potpisana. Da biste prikazali [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/PSBT) kao QR kod, kliknite na `Prikaži QR`.



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



Ako je sve u redu, odaberite `Approve PSBT` da potpišete transakciju koristeći Satochip.



![Image](assets/fr/57.webp)



Kada je potpisivanje završeno, SeedSigner generiše novi QR kod koji sadrži potpisanu transakciju, spremnu za skeniranje od strane Sparrow.



#### 7.2.3 Emitovanje transakcije sa Sparrow



Sada kada je transakcija potpisana i validirana, ostaje samo da je emitujete na Bitcoin mreži kako bi je Miner mogao uključiti u BLOCK. U Sparrow, kliknite na `Scan QR`.



![Image](assets/fr/58.webp)



Prikažite QR kod prikazan na vašem SeedSigner-u (onaj koji sadrži potpisanu transakciju) kameri. Sparrow će zatim prikazati sve detalje transakcije. Napravite konačnu proveru da su sve informacije tačne, a zatim kliknite na "Broadcast Transaction" da biste je emitovali na Bitcoin mreži.



![Image](assets/fr/59.webp)



Vaša transakcija je sada preneta na mrežu. Možete pratiti njenu potvrdu u kartici `Transakcije` Sparrow wallet.



![Image](assets/fr/60.webp)



## 8. Vrati svoj Wallet nazad



Kao što smo videli u prethodnim odeljcima, u zavisnosti od vaše strategije bezbednosti, postoji nekoliko načina za pravljenje rezervne kopije vaše fraze za oporavak pored vašeg Satochip-a:




- Korišćenje klasičnog *SeedQR* sa SeedSigner ;
- Snimanjem fraze Mnemonic na fizički medij;
- Ili čuvanjem na Seedkeeper-u, kako je objašnjeno u odeljku 5.2.



U svakom slučaju, postoje 2 glavne situacije u kojima treba da intervenišete: gubitak Satochip-a ili gubitak SeedSigner-a. Hajde da pogledamo kako reagovati u svakom od ovih scenarija.



### 8.1. Preuzmite svoj Wallet sa Satochip



Ako još uvek imate svoj Satochip, ali vam je SeedSigner pokvaren ili izgubljen, situacija je prilično jednostavna za upravljanje, pošto je vaš Wallet još uvek u Satochip-u.



Najbolja opcija je preporučiti potrebne komponente i izgraditi novi SeedSigner od nule. Pošto je ovo uređaj "bez stanja", nije važno da li koristite isti ili drugi SeedSigner: sve dok možete umetnuti svoj Satochip, sve će raditi normalno.



Ako ne želite da ponovo izgradite jedan, možete koristiti svoj Satochip na klasičan način, tj. direktno sa svog računara, bez prolaska kroz SeedSigner. Ova metoda funkcioniše savršeno, ali značajno smanjuje sigurnost vašeg Bitcoin Wallet: gubite "*air-gapped*" izolaciju i sada morate potpisivati naslepo, pošto je SeedSigner delovao kao pouzdan ekran. Međutim, ovo može biti privremeno rešenje u hitnim slučajevima, ili ako niste u mogućnosti da ponovo izgradite SeedSigner.



Da biste to uradili, biće vam potreban USB čitač pametnih kartica ili NFC čitač. Otvorite Wallet koji želite da vratite u Sparrow, zatim idite na karticu `Settings` i kliknite na `Replace`.



![Image](assets/fr/61.webp)



Umetnite svoj Satochip u čitač pametnih kartica povezan s računarom, zatim kliknite na `Import` pored `Satochip`.



![Image](assets/fr/62.webp)



Konačno, unesite svoj PIN pametne kartice da biste je otključali. Zatim ćete moći pristupiti svom Wallet, kreirati transakcije i potpisivati ih direktno koristeći povezani Satochip.



### 8.2. Preuzmite svoj portfolio pomoću SeedSigner



Drugi, delikatniji scenario je kada izgubite pristup svom Satochip-u koji sadrži seed: bilo da je pokvaren, izgubljen, ukraden ili ste zaboravili njegov PIN kod. Ako je vaš Satochip ukraden ili izgubljen, toplo preporučujemo da, kada vam pristup sredstvima bude vraćen, odmah prebacite svoje bitkoine na potpuno novi Wallet, generisan sa drugačijim seed. Ovo osigurava da potencijalni napadač nikada ne može dobiti pristup vašim Satss-ima.



Da biste ponovo dobili pristup svom portfoliju i premestili svoja sredstva, jednostavno učitajte svoj seed u SeedSigner. U zavisnosti od medija za bekap koji ste koristili, imate nekoliko opcija:





- Unesite svoju Mnemonic frazu ručno u meniju `Seeds > Enter 12-word seed`.



![Image](assets/fr/63.webp)





- Skenirajte svoj *SeedQR* klikom na dugme `Scan` na početnoj stranici.



![Image](assets/fr/64.webp)





- Ili učitajte svoj seed iz Seedkeeper-a, putem menija `Seeds > From SeedKeeper` (ovo je metoda koju koristim u ovom vodiču). Jednostavno ćete morati uneti PIN kod Seedkeeper-a i odabrati tajnu koja će se koristiti kao seed na SeedSigner-u.



![Image](assets/fr/65.webp)



Jednom kada je seed učitan u SeedSigner, bez obzira na metodu koju koristite, moći ćete da potpišete jednu ili više skeniranih transakcija kako biste premestili svoje bitkoine na novi, nekompromitovani Wallet. Da biste saznali kako to da uradite, pogledajte deo 7.2 sledećeg tutorijala:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

Sada znate kako da koristite Satochip za sigurno upravljanje vašim Bitcoin portfoliom u kombinaciji sa SeedSigner.



Ako vas je ova postavka uverila, ne oklevajte da podržite projekte koji je omogućavaju:




- Kupovinom vaše opreme direktno [na Satochip vebsajtu](https://satochip.io/shop/);
- Doniranjem [projektu SeedSigner](https://seedsigner.com/donate/);
- Pretplatom na [Crypto Guide-ov YouTube kanal](https://www.youtube.com/@CryptoGuide/), koji vodi osoba koja održava GitHub repozitorijum u kojem se nalazi modifikovani firmver koji smo koristili u ovom vodiču.