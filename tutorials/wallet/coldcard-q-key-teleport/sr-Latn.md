---
name: COLDCARD Q - Key Teleport
description: Šta je Key Teleport i kako ga koristiti?
---

![cover](assets/cover.webp)




![video](https://www.youtube.com/watch?v=Bg0r0DQVcDg)




![video](https://www.youtube.com/watch?v=BRpBiK-F8VU)



Šta je funkcija **Key Teleport** koju nudi Coinkite sa svojim vodećim uređajem ColdCardQ?



**Key Teleport** vam omogućava siguran prenos poverljivih podataka između 2 ColdCardQ uređaja. Kanal za prenos čak ne mora biti šifrovan i može biti javan.



Ovo se može koristiti za prenos:





- gW-0 fraze (ColdCard Q-ova seed master ili tajne pohranjene u ColdCardQ-ovom [seed Vault-u](https://coldcard.com/docs/temporary-seeds/#seed-vault).
- **poverljive beleške i lozinke**: ovo može biti bilo koja tajna ili čitav direktorijum [Secure Notes & Passwords](https://coldcard.com/docs/secure_notes/) na vašem ColdCardQ.
- rezervna kopija celog vašeg **ColdCardQ**: ColdCardQ koji prima ovu rezervnu kopiju ne sme imati seed Master da bi ovo funkcionisalo.
- gW-3 (**Delimično potpisane Bitcoin transakcije**) kao deo šeme sa više potpisa.



Ovo zahteva da ste nadogradili [firmver uređaja na verziju v1.3.2Q](https://coldcard.com/docs/upgrade/) ili višu.



## Kako da koristim Key Teleport?



### 1- Da prenesete bilo koju vrstu podataka



Ovde ćemo pogledati prenos seed rečenica, beleški, lozinki ili celokupan prenos ColdCardQ bekapa. Slučaj prenosa PSBT za transakcije sa više potpisa biće obrađen kasnije.



#### Pripremite uređaj za primanje tajni



U meniju **"Advanced / Tools**" na vašem ColdCardQ, izaberite **"Key Teleport (start) "**.


Na sledećem ekranu, predložen je 8-cifreni lozinka, ovde "20420219". Moraćete da prenesete ovu lozinku pošiljaocu. Koristite SMS, na primer, da pošaljete ovu lozinku, ili vaš omiljeni sigurni sistem za razmenu poruka, ili čak glasovni poziv.



Zatim kliknite na dugme **"Enter**" na vašem ColdCardQ da pređete na sledeći korak.




![CCQ-key-teleport](assets/fr/01.webp)




QR kod se generiše na ekranu. Još jednom, potrebno je da ovaj QR kod prenesete "pošiljaocu" ColdCardQ. Najlakši način za to je putem video poziva.



**NEMOJTE SLATI OVAJ QR KOD PUTEM ISTOG KANALA PRENOSA KOJI JE KORIŠĆEN ZA SLANJE PRETHODNE 8-CIFRENE LOZINKE**.



![CCQ-key-teleport](assets/fr/02.webp)



*Za one koji su zainteresovani, hajde da pokušamo da razumemo osnovni mehanizam koji omogućava prenos tajni preko nesigurnih kanala*



*Ono što ovde zapravo radimo jeste iniciranje prenosa tajni putem Diffie-Hellman metode, pokrivene u BTC204 kursu koji sam uključio ispod*



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

*Trenutno imamo:*




- generisao efemerni par ključeva (javni/privatni odnosno Ka i ka sa Ka=G.ka, gde je G ECDH generator tačka), i **8-cifrenu lozinku**.
- koristio ovu lozinku za šifrovanje javnog ključa (Ka) putem AES-256-CTR, zatim preneo ovu lozinku putem komunikacionog kanala A do "šaljuće" ColdCardQ.
- konačno, preneli smo šifrovani paket pošiljaocu putem QR koda iznad, koristeći drugi komunikacioni kanal B različit od 1.



#### Pripremi uređaj koji će poslati tajne



Sa uređaja za slanje, kliknite na dugme **"QR "** da skenirate QR kod koji vam je poslao uređaj za prijem, zatim unesite 8-cifrenu lozinku koja vam je saopštena u prethodnom koraku putem zasebnog kanala. Sada smo spremni da počnemo sa slanjem podataka sa uređaja za "slanje".



**Molimo vas da ne unosite pogrešno 8-cifrenu lozinku, jer neće biti prikazana poruka o grešci i proces će se nastaviti. Međutim, konačni prenos podataka će propasti i moraćete da počnete ispočetka**.



![CCQ-key-teleport](assets/fr/03.webp)



*Za one radoznalije među vama, hajde da još jednom pogledamo čime se bavimo u smislu kriptografije i tajnog prenosa:*




- uvezli smo šifrovane podatke skeniranjem QR koda na uređaju za prijem.
- zatim smo ih dešifrovali koristeći 8-cifrenu lozinku koja nam je preneta putem sekundarnog kanala.
- stoga smo u posedu javnog ključa (Ka) koji je inicijalno generisao primalac.
- Zatim generate novi efemerni par ključeva (Kb/kb, sa Kb=G.kb) na uređaju za slanje, koji koristimo za primenu ECDH na Ka. Stoga izvodimo operaciju kb.Ka=Ks, gde se Ks naziva **"Ključ sesije"**.




Sada se od vas traži da izaberete prirodu tajni koje će se prenositi između 2 ColdCardQ uređaja (poverljive beleške, lozinka, potpuna rezervna kopija, seed-ovi sadržani u vašem trezoru, seed master uređaja).



![CCQ-key-teleport](assets/fr/04.webp)



Ovde će naša tajna biti kratka poruka izborom **"Brza tekstualna poruka "**. Ukucajte vašu poruku (za nas "Plan ₿ Academy rocks") zatim pritisnite **"ENTER "**.


Uređaj zatim generiše novu nasumičnu lozinku nazvanu **"Teleport Password "**, u primeru "NE XG BT SK".



![CCQ-key-teleport](assets/fr/05.webp)



Pritisnite **"ENTER "** i biće vam prikazan novi QR kod. Neka ga skenira uređaj koji prima. I na drugom komunikacionom kanalu, prenesite **"Teleport lozinku "** primaocu.



![CCQ-key-teleport](assets/fr/06.webp)



*Evo opet, za radoznale, tokom ove faze:*




- nakon odabira tajni za prenos, mi generate novu nasumičnu lozinku nazvanu **"Teleport Password"**.
- zatim šifrujemo tajne putem AES-256-CTR koristeći **"Ključ Sesije"**, "Ks", generisan u prethodnom koraku.
- mi prefiksujemo paket koji je već enkriptovan sa **"Ključ Sesije "** sa našim Kb javnim ključem, zatim dodajemo dodatni Layer AES-256-CTR enkripciju sa **"Teleport Lozinkom "**. Cela stvar je zatim enkodovana kao QR kod.




#### Finalizujte prenos tajni na uređaj koji prima



Pritisnite dugme **"QR "** da biste skenirali QR kod koji je predstavljen od strane uređaja za slanje putem visio kanala. Od vas će biti zatraženo da unesete vašu **"Teleport lozinku "** za nas "NE XG BT SK".



![CCQ-key-teleport](assets/fr/07.webp)





Podaci se zatim dešifruju i postaju razumljivi za uređaj koji ih prima. Poruka koja je primljena je zaista "Plan ₿ Academy rocks". To je sve.



![CCQ-key-teleport](assets/fr/08.webp)



*Šta se zapravo desilo tokom ove poslednje faze :*?




- dešifrovali smo podatke koje je poslao pošiljalac koristeći **"Teleport Password"**.
- stoga imamo javni ključ Kb i našu tajnu poruku šifrovanu pomoću **"Ključa Sesije"**, "Ks". Ali kako to možemo uraditi kada, kao primalac, ne znamo Ks, koji je kreirao pošiljalac?
- Moramo primeniti naš privatni ključ "ka" iz početnog koraka **"Pripremite uređaj koji će primiti podatke"** na javni ključ Kb.
- Zapravo, izračunavanjem ka.Kb = ka.kb.G=kb.ka.G=kb.Ka=Ks, pronalazimo Ks. Koji se konačno koristi za dešifrovanje tajne poruke.



### 2- Da prenesete PSBT na Multisig (napredno)



Ovo pretpostavlja da je vaš Wallet Multisig već kreiran i da je vaš ColdCardQ uređaj već unapred podešen da može da obavlja transakcije sa više potpisa. Ako to nije slučaj, objašnjenja su dostupna [ovde](https://coldcard.com/docs/Multisig/) na Coinkite vebsajtu.



Brzi podsetnik šta je multi-signature Wallet (Multisig).



Obično je za trošenje vaših Wallet sredstava potreban samo jedan privatni ključ da bi se otključali UTXO-i povezani sa vašim adresama.


U slučaju Wallet Multisig, može biti potrebno do 15 privatnih ključeva i stoga 15 potpisa da bi se sredstva potrošila. Ovo je poznato kao "M od N" portfelj, gde je N između 1 i 15, a M broj potpisa potrebnih da bi sredstva bila potrošiva. Na primer, Wallet Multisig 3 od 5 će zahtevati najmanje 3 potpisa od mogućih 5.



Izazov je onda koordinisati između potpisnika da potpišu "PSBT" za "Partially Signed Bitcoin Transaction" zauzvrat. U ovom kontekstu, "**Key Teleport**" se može koristiti za prenos PSBT između sa-potpisnika na jednostavan i poverljiv način. Jednostavan video poziv između sa-potpisnika će rešiti stvar.



Evo kako se to radi na Multisig 3 od 4.



**Potpisnik 1:**



Potpisnik 1 uvozi i potpisuje PSBT. Na kraju, klikne na **"T "** da koristi **"Key Teleport "** za prenos PSBT potpisniku 2.



![CCQ-key-teleport](assets/fr/09.webp)




Nakon što odaberete potpisnika 2 klikom na **"ENTER "**, biće obezbeđena "TELEPORT LOZINKA" (ovde JJ YC AB 6A), koja mora biti preneta potpisniku 2 putem drugog komunikacionog kanala. Na primer, SMS-om ili glasovnim pozivom, ali **ne** video pozivom.



Pritisnite **"ENTER "** ponovo i pojaviće se QR kod koji predstavlja PSBT potpisan sa 1, a zatim šifrovan pomoću "TELEPORT PASSWORD".



![CCQ-key-teleport](assets/fr/10.webp)



**Potpisnik 2:**



Potpisnik 2 skenira QR kod koji mu je predstavio potpisnik 1. Zatim unosi "TELEPORT LOZINKU" prenesenu preko sekundarnog komunikacionog kanala kako bi dešifrovao prenesene podatke.



Potpisnik 2 potpisuje transakciju, a zatim klikne na **"T "** da prenese PSBT potpisniku 3 putem "Key Teleport".


Jasno je da su 2 potpisa već primenjena. Sve što nedostaje je potpis potpisnika 3 da bi transakcija bila važeća. Izaberite potpisnika 3 klikom na **"ENTER "**.



![CCQ-key-teleport](assets/fr/11.webp)



I kreirana je nova "TELEPORT PASSWORD", nakon čega sledi QR kod koji kodira PSBT potpisan od strane 1 i 2, a zatim šifrovan ovom novom "TELEPORT PASSWORD" (GW YQ K3 LL).



![CCQ-key-teleport](assets/fr/12.webp)



**Potpisnik 3:**



Ponovite isti korak kao gore.


Potpisnik 3 skenira QR kod koji mu je predstavio potpisnik 2. Zatim unosi "TELEPORT LOZINKU" prenesenu sekundarnim komunikacionim kanalom.



Potpisnik 3 potpisuje transakciju i ovog puta, pošto su primenjena 3 od 4 potpisa, transakcija je označena kao finalizovana i spremna je za distribuciju putem različitih medija (SD kartica, NFC, QR itd.).



![CCQ-key-teleport](assets/fr/13.webp)



Ako je funkcija "Push Tx" na vašem ColdCardQ aktivirana, jednostavno pričvrstite vaš ColdCardQ na poleđinu bilo kog uređaja sa omogućenim NFC-om koji je povezan na internet (smartfon/tablet) kako biste emitovali transakciju preko Bitcoin mreže.



![CCQ-key-teleport](assets/fr/14.webp)



*Za PSBT transfere sa jednog potpisnika na drugog, "Key Teleport" se jednostavno koristi putem "Teleport Password" u svakoj fazi, koji šifrira PSBT dok se prenosi sa jednog potpisnika na drugog. Kako se preneti podaci ne mogu koristiti za krađu sredstava, nema potrebe za Diffie-Hellman kao što je slučaj kada se šalju visoko poverljive tajne (seed, lozinka itd...)*.



![CCQ-key-teleport](assets/fr/15.webp)



*Izvor: [ColdCard zvanična veb stranica](https://coldcard.com/)*