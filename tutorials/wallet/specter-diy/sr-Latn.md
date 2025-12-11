---
name: Specter DIY
description: Vodič za postavljanje Specter DIY
---

![cover](assets/cover.webp)


## Specter-DIY


> Cypherpunks pišu kod. Znamo da neko mora pisati softver za zaštitu privatnosti, i pošto ne možemo imati privatnost osim ako svi ne učestvujemo, mi ćemo ga pisati.

*Manifest Cypherpunk - Eric Hughes - 9. mart 1993.*


Ideja projekta je da se izgradi hardver wallet od komponenata dostupnih na tržištu.

Iako imamo ekstenzionu ploču koja sve stavlja u lep form-faktor i pomaže vam da izbegnete bilo kakvo lemljenje, nastavićemo da podržavamo i održavamo kompatibilnost sa standardnim komponentama.


![image](assets/fr/01.webp)


Takođe želimo da projekat ostane fleksibilan tako da može raditi na bilo kojem drugom skupu komponenti uz minimalne izmene. Možda želite da napravite hardver wallet na drugačijoj arhitekturi (RISC-V?), sa audio modemom kao komunikacionim kanalom - trebalo bi da budete u mogućnosti da to uradite. Trebalo bi da bude lako dodati ili promeniti funkcionalnost Specter-a i trudimo se da apstrahujemo logičke module koliko god možemo.


QR kodovi su podrazumevani način na koji Specter komunicira sa hostom. QR kodovi su prilično praktični i omogućavaju korisniku da kontroliše prenos podataka - svaki QR kod ima veoma ograničen kapacitet i komunikacija se odvija jednosmerno. I to je airgapped - ne morate povezivati wallet sa računarom u bilo kom trenutku.


Za tajno skladištenje podržavamo agnostički režim (wallet zaboravlja sve tajne kada se isključi), nepromišljeni režim (čuva tajne u flešu mikrokontrolera aplikacije) i secure element integracija dolazi uskoro.


Naš glavni fokus je postavljanje multisignature sa drugim hardverskim novčanicima, ali wallet može takođe raditi kao pojedinačni potpisnik. Pokušavamo da ga učinimo kompatibilnim sa Bitcoin Core gde možemo - PSBT za nepotpisane transakcije, wallet deskriptori za uvoz/izvoz multisig novčanika. Da bismo lakše komunicirali sa Bitcoin Core, takođe radimo na [Specter Desktop aplikaciji](https://github.com/cryptoadvance/specter-desktop) - malom python flask serveru koji komunicira sa vašim Bitcoin Core čvorom.


Većina firmvera je napisana u MicroPython-u što čini kod lakim za reviziju i promene. Koristimo [secp256k1](https://github.com/bitcoin-core/secp256k1) biblioteku iz Bitcoin Core za proračune eliptičke krive i [LittlevGL](https://lvgl.io/) biblioteku za GUI.


## Odricanje odgovornosti


Projekat je značajno sazreo, do te mere da je nivo bezbednosti Specter-DIY sada uporediv sa komercijalnim hardverskim novčanicima na tržištu. Implementirali smo siguran bootloader koji verifikuje nadogradnje firmvera, tako da možete biti sigurni da samo potpisani firmver može biti učitan na uređaj nakon inicijalnog podešavanja. Međutim, za razliku od komercijalnih uređaja za potpisivanje, bootloader mora biti ručno instaliran od strane korisnika i nije postavljen u fabrici proizvođača uređaja. Stoga, obratite posebnu pažnju tokom inicijalne instalacije firmvera i osigurajte da ste verifikovali PGP potpise i flešovali firmver sa sigurnog računara.


Ako nešto ne radi, otvorite problem ovde ili postavite pitanje u našoj [Telegram grupi](https://t.me/+VEinVSYkW5TUl5Ai).


## Lista za kupovinu za Specter-DIY


Ovde opisujemo šta kupiti, a u sledećem delu sklapanja objašnjavamo kako ga sastaviti i nekoliko napomena o ploči - džamperi za napajanje, USB portovi itd.


### Odbor za otkrića


Glavni deo uređaja je razvojna ploča:



- STM32F469I-DISCO developer board (i.e. from [Mouser](https://eu.mouser.com/ProductDetail/STMicroelectronics/STM32F469I-DISCO?qs=kWQV1gtkNndotCjy2DKZ4w==) or [Digikey](https://www.digikey.com/product-detail/en/stmicroelectronics/STM32F469I-DISCO/497-15990-ND/5428811))
- Mini**USB kabl
- Standardni MicroUSB kabl za komunikaciju preko USB-a


Opcionalno, ali preporučeno:


- [Waveshare QR code skener](https://www.waveshare.com/barcode-scanner-module.htm) sa dugim pin headerima kao [ovi](https://eu.mouser.com/ProductDetail/Samtec/DW-02-10-T-S-571?qs=sGAEpiMZZMvlX3nhDDO4AE5PKXAQeC6NPk%2FcLBS9yKI%3D) ili [ovi](https://www.amazon.com/gp/product/B015KA0RRU/) za povezivanje skenera sa pločom (potrebna su 4 pin headera).


Trenutno radimo na ekstenzionoj ploči koja uključuje slot za pametnu karticu, skener QR koda, bateriju i 3D štampano kućište, ali ne uključuje glavni deo — discovery ploču koju treba da naručite posebno. Na ovaj način napad na lanac snabdevanja i dalje nije problem jer se sigurnosno kritične komponente kupuju iz nasumične prodavnice elektronike.


Možete početi koristiti Specter čak i bez dodatnih komponenti, ali ćete moći komunicirati s njim preko USB-a ili ugrađenog SD slota za kartice. Korišćenje Spectera preko USB-a znači da nije izolovan od mreže, pa gubite važnu sigurnosnu osobinu.


### QR skener


Za skener QR koda imate nekoliko opcija.


**Opcija 1. Preporučeno.** Razumno dobar skener od Waveshare (40$)


[Waveshare skener](https://www.waveshare.com/barcode-scanner-module.htm) - trebaćeš pronaći način kako da ga lepo montiraš, možda koristiti neku vrstu Arduino Prototype shield-a i malo lepljive trake.


Nije potrebno lemljenje, ali ako imate veštine lemljenja, možete učiniti da wallet izgleda mnogo lepše ;)


**Opcija 2.** Veoma dobar skener od Mikroe, ali prilično skup (150$):


[Barcode Click](https://www.mikroe.com/barcode-click) + [Adapter](https://www.mikroe.com/arduino-uno-click-shield)


**Opcija 3.** Bilo koji drugi QR skener


Možete pronaći neke jeftine skenere u Kini. Njihov kvalitet često nije baš sjajan, ali možete pokušati. Možda čak i ESPcamera može obaviti posao. Potrebno je samo povezati napajanje, UART (pinove D0 i D1) i okidač na D5.


**Opcija 4.** Nema skenera.


Onda možete koristiti samo Specter sa USB / SD karticom.


Osim ako ne napravite sopstveni komunikacioni modul koji koristi nešto drugo umesto QR kodova - audiomodem, bluetooth ili bilo šta drugo. Čim može biti pokrenut i poslati podatke preko serijskog porta, možete raditi šta god želite.


### Opcioni komponente


Ako dodate mali powerbank ili bateriju i punjač/booster, vaš wallet postaje potpuno samostalan ;)



## Skupština Specter-DIY



![video](https://youtu.be/1H7FqG_FmCw)


### Povezivanje Waveshare skenera bar kodova


wallet firmver će konfigurisati skener za vas prilikom prvog pokretanja, tako da nije potrebna ručna prekonfiguracija.


Evo kako povezati skener sa pločom:


![image](assets/fr/02.webp)


Radi praktičnosti možete kupiti Arduino Protype shield i zalemiti i montirati sve na njega (tj. [ovaj](https://www.digikey.com/catalog/en/partgroup/proto-shield-rev3-uno-size/79347))


### Upravljanje napajanjem


Na gornjoj strani ploče nalazi se džamper koji definiše odakle će uzimati napajanje. Možete promeniti položaj džampera i izabrati izvor napajanja da bude jedan od USB portova ili VIN pin i tamo povezati eksternu bateriju (treba da bude 5V).


### Kućište za "uradi sam"


Pogledajte fasciklu [enclosures](https://github.com/cryptoadvance/specter-diy/tree/master/docs/enclosures).


### Budite kreativni!


Sastavite svoj Specter-DIY i pošaljite nam slike (napravite pull request ili nas kontaktirajte).


Pogledajte [Galeriju](https://github.com/cryptoadvance/specter-diy/blob/master/docs/pictures/gallery/README.md) sa Specterima koje je sastavila zajednica!




## Instaliranje kompajliranog koda


Sa sigurnim bootloader-om početna instalacija firmvera je malo drugačija. Nadogradnje su lakše i ne zahtevaju povezivanje hardvera wallet sa računarom.


![video](https://youtu.be/eF4cgK_L6T4)


### Treptanje početnog firmvera


**Napomena** Ako ne želite da koristite binarne datoteke iz izdanja, pogledajte [dokumentaciju bootloader-a](https://github.com/cryptoadvance/specter-bootloader/blob/master/doc/selfsigned.md) koja objašnjava kako da ga kompajlirate i konfigurišete da koristi vaše javne ključeve umesto naših.



- Ako nadograđujete sa verzija ispod `1.4.0` ili prvi put učitavate firmware, koristite `initial_firmware_<version>.bin` sa stranice [releases](https://github.com/cryptoadvance/specter-diy/releases).
 - Proverite potpis datoteke `sha256.signed.txt` koristeći [Stepanov PGP ključ](https://stepansnigirev.com/ss-specter-release.asc)
 - Proverite hash datoteke `initial_firmware_<version>.bin` u odnosu na hash pohranjen u `sha256.signed.txt`
- Ako nadograđujete sa praznog bootloader-a ili vidite poruku o grešci bootloader-a da firmware nije važeći, pogledajte sledeći odeljak - Flashovanje potpisanog Specter firmware-a.
- Proverite da je džamper za napajanje na vašoj discovery ploči u STLK položaju.
- Povežite discovery ploču sa računarom putem **miniUSB** kabla na vrhu ploče.
    - Ploča bi trebalo da se pojavi kao uklonjivi disk pod nazivom `DIS_F469NI`.
- Kopirajte datoteku `initial_firmware_<version>.bin` u koren datotečnog sistema `DIS_F469NI`.
- Kada ploča završi sa flešovanjem firmvera, ploča će se resetovati i ponovo pokrenuti u bootloader. Bootloader će proveriti firmver i pokrenuti se u glavni firmver. Ako vidite poruku o grešci da firmver nije pronađen - pratite uputstva za ažuriranje i učitajte firmver putem SD kartice.
- Sada možete prebaciti džamper za napajanje gde želite i napajati ploču iz powerbank-a ili baterije.


Bljeskanje početnog firmvera putem kopiranja i lepljenja `.bin` fajla ponekad ne uspe - često zbog kabla ili ako povežete uređaj preko USB čvorišta. U ovom slučaju možete pokušati još nekoliko puta (obično uspe nakon 2-3 pokušaja).


Ako stalno ne uspeva, možete koristiti [stlink](https://github.com/stlink-org/stlink/releases/latest) alat otvorenog koda. Instalirajte ga i ukucajte u vaš terminal: `st-flash write <path/to/initial_firmare.bin> 0x8000000`. Obično radi mnogo pouzdanije.


### Ažuriranje firmvera



- Preuzmite `specter_upgrade_<version>.bin` sa [izdanja](https://github.com/cryptoadvance/specter-diy/releases).
- Kopirajte ovaj binarni fajl u root direktorijum SD kartice (FAT-formatirana, maksimalno 32 GB)
 - Uverite se da je samo jedna datoteka `specter_upgrade***.bin` u glavnom direktorijumu
- Umetnite SD karticu u SD slot na discovery ploči i uključite ploču.
- Bootloader će flešovati firmver i obavestiće vas kada bude gotovo.
- Ponovo pokrenite ploču - sada ćete videti Specter-DIY interfejs, predložiće vam da odaberete svoj PIN kod


Kad god izađe novo izdanje, samo preuzmite `specter_upgrade_<version>.bin` iz izdanja, prebacite ga na SD karticu i nadogradite uređaj kao u prethodnom koraku. Bootloader će osigurati da samo potpisani firmware može biti učitan na ploču.


### Kako saznati verziju firmvera


Idite na meni `Device settings` - prikazaće broj verzije ispod naslova ekrana.


## Koristite Specter-DIY wallet



![video](https://youtu.be/Oysg-hhBusc)



![video](https://youtu.be/XfMr7B_uUIk)



![video](https://youtu.be/BzBlh_knIww)



## Sigurnost Specter-DIY


### Hardver


Prikaz je kontrolisan od strane aplikacionog MCU-a.


Integracija sigurnosnog elementa još uvek nije tu - trenutno se tajne takođe čuvaju na glavnom MCU. Ali možete koristiti wallet bez čuvanja tajne - potrebno je da unesete svoju frazu za oporavak svaki put. Zašto pamtiti dugi passphrase ako možete zapamtiti ceo mnemonik?


Uređaj koristi eksternu fleš memoriju za skladištenje nekih fajlova (QSPI), ali svi korisnički fajlovi su potpisani od strane wallet i proveravaju se prilikom učitavanja.


Funkcionalnost skeniranja QR koda je na zasebnom mikrokontroleru, tako da se sva obrada slike odvija izvan MCU kritičnog za sigurnost. Trenutno su USB i SD kartica još uvek pod upravljanjem glavnog MCU, pa nemojte koristiti SD karticu i USB ako želite smanjiti površinu napada.


### PIN zaštita (autentifikacija korisnika)


Tokom prvog pokretanja generiše se jedinstvena tajna na glavnom MCU. Ova tajna vam omogućava da proverite da uređaj nije zamenjen zlonamernim - kada unesete PIN kod, vidite listu reči koja će ostati ista dok je tajna prisutna.


Vaš PIN kod zajedno sa ovom jedinstvenom tajnom se koristi za generate dešifrovanje ključa za vaše Bitcoin ključeve (ako ih čuvate). Tako da ako napadač uspe da zaobiđe ekran za PIN, dešifrovanje će i dalje propasti.


Ako ste zaključali firmware (TODO: dodajte link sa uputstvima ovde) to će efikasno zaključati i tajnu, tako da ako napadač flešuje drugačiji firmware na ploču, tajna će biti izbrisana i moći ćete to prepoznati kada počnete unositi PIN kod - redosled reči će biti drugačiji.


### Generisanje fraze za oporavak


Ovo je jedan od najvažnijih delova wallet - da se ključ za generate sigurno. Da bismo to dobro uradili, koristimo više izvora entropije:



- TRNG mikrokontrolera. Vlasnički, sertifikovan i verovatno dobar, ali mu ne verujemo.
- Ekran osetljiv na dodir. Svaki put kada dodirnete ekran, merimo poziciju i trenutak kada se taj dodir dogodio (u taktovima mikrokontrolera na 180MHz).
- Ugrađeni mikrofoni - još ne. Ploča ima dva mikrofona, tako da hardver wallet može da vas sluša i meša ove podatke u bazen entropije.


Sva ova entropija se hešira zajedno i konvertuje u vašu frazu za oporavak. Rezultujuća entropija je uvek bolja od bilo kog pojedinačnog izvora.


### Logika visokog nivoa - novčanici


Specter funkcioniše kao skladište ključeva. Drži HD privatne ključeve koji mogu biti uključeni u novčanike. Novčanici su definisani njihovim deskriptorima. Takođe podržavamo miniscript.


Svaki wallet pripada određenoj mreži. To znači da ako ste uvezli wallet na `testnet`, on neće biti dostupan na `mainnet` ili `regtest` - potrebno je da se prebacite na ovu mrežu i uvezete wallet zasebno.


### Verifikacija transakcija


Sledeća pravila važe za transakcije koje će wallet potpisati:



- ako se pronađu mešani unosi iz različitih novčanika, korisnik se upozorava ([napad](https://blog.trezor.io/details-of-the-multisig-change-address-issue-and-its-mitigation-6370ad73ed2a))
- promene prikazuju ime wallet kojem su poslate
- da biste koristili multisig ili miniscript prvo morate da uvezete wallet dodavanjem wallet deskriptora (preko QR, USB ili SD kartice)


## Podrška deskriptorima


Svi uobičajeni Bitcoin opisi funkcionišu. Pored toga, imamo nekoliko proširenja:


### Više grana u opisima


Da biste uštedeli prostor u QR kodovima, dozvoljavamo dodavanje deskriptora sa više grana odjednom. Ako želite da koristite `wpkh(xpub/0/*)` za primanje adresa i `wpkh(xpub/1/*)` za adrese za kusur, možete ih kombinovati u jedan deskriptor: `wpkh(xpub/{0,1}/*)` - wallet će tretirati prvi indeks dela `{}` skupa kao granu za primanje adresa, a drugi kao adrese za kusur.


Takođe možete navesti više od dve grane, a indeksi grana mogu biti različiti za različite potpisnike, tako da je ovaj deskriptor veoma čudan, ali potpuno važeći:


```
wsh(sortedmulti(2,xpubA/{22,33,44}/*,xpubB/34/*/{1,8,6},pubkey3))
```


Ovde za primanje adrese broj 17 wallet će koristiti skriptu iz `wsh(sortedmulti(2,xpubA/22/17,xpubB/34/17/1,pubkey3))`.


Jedini uslov je da broj indeksa u svim skupovima bude isti (3 u gornjem slučaju).


### Podrazumevane izvedenice


Ako deskriptor sadrži master javne ključeve, ali ne sadrži džoker derivacije, podrazumevana derivacija `/{0,1}/*` će biti dodata svim proširenim ključevima u deskriptoru. Ako bar jedan od xpub-ova ima džoker derivaciju, deskriptor neće biti promenjen.


Opis `wpkh(xpub)` biće konvertovan u `wpkh(xpub/{0,1}/*)`.


### Miniscript


Specter podržava miniscript, ali ne podržava kompilaciju iz policy u miniscript (jer je to previše skupo). Izvodimo neke provere na miniscipt-u, tako da su samo `B` skripte dozvoljene na najvišem nivou i svi argumenti u pod-miniscript-ima moraju imati svojstva prema [specifikaciji](http://bitcoin.sipa.be/miniscript/).


Možete koristiti [bitcoin.sipa.be](http://bitcoin.sipa.be/miniscript/) da generate descriptor iz politike i zatim ga uvesti u wallet.


Na primer, politika "Mogu potrošiti sada, ili za 100 dana moja žena može potrošiti" može se konvertovati u wallet na sledeći način:


Politika: `or(9@pk(xpubA),and(older(14400),pk(B)))` (moj ključ je 9 puta verovatniji)


Miniscript: `or_d(pk(xpubA),and_v(v:pkh(xpubB),older(14400)))`


Descriptor: `wsh(or_d(pk(xpubA),and_v(v:pkh(xpubB),older(14400))))`


Kako ovde nemamo nikakve podrazumevane derivacije, podrazumevane derivacije `/{0,1}/*` će biti dodate na xpubs.



---

MIT Licenca


Copyright (c) 2019 cryptoadvance


---