---
name: COLDCARD Q - Napredno
description: Korišćenje naprednih opcija COLDCARD Q
---
![cover](assets/cover.webp)


U prethodnom vodiču pokrili smo početnu konfiguraciju COLDCARD Q i njegove osnovne funkcije za početnike. Ako ste tek primili svoj COLDCARD Q i još ga niste postavili, preporučujem da počnete s tim vodičem pre nego što nastavite ovde:


https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

Ovaj novi vodič je posvećen naprednim opcijama COLDCARD Q, dizajniranim za napredne i paranoične korisnike. Zapravo, COLDCARD-i se razlikuju od drugih hardverskih novčanika po mnogim naprednim sigurnosnim funkcijama. Naravno, ne morate koristiti sve ove opcije. Samo odaberite one koje odgovaraju vašoj sigurnosnoj strategiji.


**Upozorenje**, nepravilna upotreba nekih od ovih naprednih opcija može dovesti do gubitka vaših bitkoina ili uništenja vašeg Hardware Wallet. Stoga vam toplo preporučujem da pažljivo pročitate savete i objašnjenja za svaku opciju.


Pre nego što počnete, uverite se da imate pristup fizičkoj rezervnoj kopiji vaše Mnemonic fraze od 12 ili 24 reči, i proverite njenu validnost putem sledećeg menija: `Advanced/Tools > Danger Zone > seed Functions > View seed Words`.


![CCQ](assets/fr/01.webp)


## BIP39 passphrase


Ako ne znate šta je BIP39 passphrase, ili vam nije potpuno jasno kako funkcioniše, toplo preporučujem da unapred pogledate ovaj vodič, koji pokriva teorijske osnove potrebne za razumevanje rizika povezanih sa korišćenjem passphrase:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Imajte na umu da kada jednom postavite passphrase na vaš Wallet, vaš Mnemonic sam po sebi neće biti dovoljan da ponovo dobijete pristup vašim bitcoinima. Biće vam potrebni i Mnemonic i passphrase. Štaviše, moraćete da unesete passphrase svaki put kada otključavate vaš COLDCARD Q. Ovo poboljšava sigurnost tako što fizički pristup COLDCARD-u i poznavanje PIN-a postaju nedovoljni bez passphrase.


Na COLDCARD uređajima, imate dve opcije za upravljanje vašim passphrase:


1. **Klasičan unos:** Ručno unosite passphrase svaki put kada koristite svoj Hardware Wallet, baš kao i sa drugim hardverskim novčanicima. COLDCARD Q pojednostavljuje ovaj zadatak svojim punim tastaturom.


2. **Možete izabrati da šifrujete svoj passphrase i skladištite ga na microSD kartici. U tom slučaju, moraćete da ubacite microSD u COLDCARD Q svaki put kada ga koristite. Imajte na umu da će ovaj microSD raditi samo na vašem COLDCARD Q i nije rezervna kopija. Stoga je veoma važno da takođe čuvate kopiju svog passphrase na fizičkom mediju, kao što je papir ili metal.


Da biste postavili svoj BIP39 passphrase, pristupite meniju "*passphrase*".


![CCQ](assets/fr/02.webp)


Unesite svoj passphrase koristeći tastaturu. Obavezno izaberite jak passphrase (dug i nasumičan) i napravite fizičku rezervnu kopiju.


![CCQ](assets/fr/03.webp)


Jednom kada postavite svoj passphrase, COLDCARD Q će vam prikazati otisak glavnog ključa novog Wallet povezanog sa ovim passphrase. Obavezno sačuvajte ovaj otisak. Kada ponovo unesete svoj passphrase prilikom korišćenja uređaja u budućnosti, moći ćete da proverite da li se prikazani otisak podudara sa onim koji ste sačuvali. Ova provera osigurava da niste napravili grešku prilikom unosa vašeg passphrase.


![CCQ](assets/fr/04.webp)


Sada možete pritisnuti "*ENTER*" da primenite ovaj passphrase na vašu Mnemonic frazu i aktivirate novi Wallet. Ako želite da sačuvate ovaj passphrase na microSD, ubacite karticu u odgovarajući slot i pritisnite "*1*".


![CCQ](assets/fr/05.webp)


Vaš passphrase je sada primenjen. Otisak ključa se pojavljuje na početnom ekranu i na vrhu ekrana.


![CCQ](assets/fr/06.webp)


Svaki put kada otključate svoj COLDCARD Q, moraćete da pristupite meniju "*passphrase*" i unesete svoj passphrase na isti način kao gore, kako biste ga primenili na Mnemonic sačuvan u uređaju i pristupili ispravnom Bitcoin Wallet.


![CCQ](assets/fr/07.webp)


Ako ste sačuvali passphrase na microSD kartici, svaki put kada ga koristite, umetnite je u COLDCARD i pristupite "*passphrase*" meniju. Vaš COLDCARD će učitati passphrase direktno sa microSD, tako da ga nećete morati unositi ručno. Kliknite na "*Restore Saved*".


![CCQ](assets/fr/08.webp)


Proverite da li su dužina i prvo slovo učitanog passphrase tačni.


![CCQ](assets/fr/09.webp)


Potvrdite da se otisak prsta prikazan podudara sa otiskom vašeg Wallet i kliknite na "*Restore*".


![CCQ](assets/fr/10.webp)


Imajte na umu da korišćenje passphrase znači da ćete morati da uvezete novi set ključeva izvedenih iz kombinacije vaše Mnemonic fraze i passphrase u vaš Wallet softver za upravljanje (kao što je Sparrow Wallet). Da biste to uradili, pratite korak "*Konfiguriši novi Wallet na Sparrow-u*" u ovom drugom uputstvu :


https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

## Otključavanje opcija


COLDCARD-i takođe imaju koristi od niza opcija za proces otključavanja uređaja. Hajde da saznamo više o ovim naprednim opcijama.


### Trik PIN-ovi


Trik PIN je sekundarni PIN kod koji se razlikuje od onog definisanog tokom početne konfiguracije uređaja. Ovaj kod se koristi za pokretanje specifičnih unapred konfigurisanih akcija čim se unese kada se COLDCARD uključi. Možete konfigurisati nekoliko Trik PIN-ova, od kojih je svaki povezan sa različitom akcijom. Ove funkcije vam omogućavaju da prilagodite vaš COLDCARD vašoj ličnoj bezbednosnoj strategiji. Posebno su korisne u slučajevima fizičke prinude, kao što je tokom pljačke (u zajednici Bitcoin obično se naziva "*napad sa ključem od $5*").


Da biste aktivirali Trick PIN i povezali ga sa radnjom, pristupite meniju `Settings > Login Settings > Trick PINs`.


![CCQ](assets/fr/11.webp)


Odaberite "*Add New Trick*".


![CCQ](assets/fr/12.webp)


Postavite PIN kod koji će biti povezan sa radnjom i zapamtite da ga sačuvate.


![CCQ](assets/fr/13.webp)


Zatim izaberite radnju koja će se automatski izvršiti svaki put kada unesete ovaj Trik PIN. Evo liste dostupnih radnji za PIN:




- "*Brick Self*: Ova akcija uništava oba COLDCARD Q čipa ako se unese Trick PIN, čineći uređaj potpuno neupotrebljivim. Tada će biti nemoguće preprodati, ponovo koristiti ili čak vratiti ga Coinkite-u. Uređaj će postati nepovratno zastareo. Ova funkcija se može koristiti u slučaju pljačke kako bi se napadaču pokazalo da nikada neće moći pristupiti vašim bitcoinima. **Napomena**: bez fizičke rezervne kopije vaše Mnemonic fraze i bilo koje passphrase, vaši bitcoini će biti trajno izgubljeni."


![CCQ](assets/fr/14.webp)




- "*Wipe seed*": Ovaj meni nudi nekoliko akcija za brisanje seed, tj. resetovanje COLDCARD-a bez njegovog uništavanja. Za razliku od opcije "*Brick Self*", biće moguće rekonfigurisati uređaj koristeći rezervnu kopiju vaše Mnemonic fraze. Međutim, bez ove kopije, vaši bitkoini će biti izgubljeni. Ovde su dostupne opcije:
 - "*Wipe & Reboot* : Uklanja seed i ponovo pokreće COLDCARD bez prikazivanja bilo kakvih informacija na ekranu.
 - "*Silent Wipe*": Tiho briše seed i otključava COLDCARD na nasumičnom lažnom Wallet kao da se ništa nije dogodilo.
 - "*Wipe -> Wallet*": Diskretno uklanja seed i otključava COLDCARD na unapred konfigurisanom sekundarnom Wallet, dizajniranom kao mamac. Ovaj Wallet može sadržati mali deo vaših Bitcoin ušteđevina kako bi zadovoljio napadača.
 - "*Reci Wiped, Stop*": Briše seed i prikazuje poruku `seed je wiped, Stop` na ekranu.


![CCQ](assets/fr/15.webp)




- "*Duress Wallet*": Ovom akcijom, Trick PIN kod otključava Wallet izveden iz seed koristeći BIP85. Ovaj sekundarni Wallet može se koristiti kao mamac da zadovolji napadača. COLDCARD se ponaša kao da je pravi Wallet, ali bez master PIN-a (različitog od Trick PIN-a), napadač nikada neće moći pristupiti pravom Wallet. Ova strategija je dizajnirana da navede ljude da veruju da je Wallet povezan sa Trick PIN-om jedini koji postoji.


![CCQ](assets/fr/16.webp)




- "*Login Countdown*": Ovaj meni grupiše radnje sa odbrojavanjem pre nego što se izvrše. **Upozorenje**, neke od njih mogu uništiti vaš uređaj ili dovesti do gubitka vaših bitkoina. Ovde su dostupne podakcije:
 - "*Wipe & Countdown* : Briše seed iz memorije COLDCARD-a, zatim pokreće odbrojavanje od jednog sata. Bez čuvanja vašeg Mnemonic ili passphrase, vaši bitkoini će biti izgubljeni. Ova opcija je dizajnirana da prevari napadača da pomisli da će uređaj biti otključan na kraju odbrojavanja, dok će u stvari biti vraćen na fabrička podešavanja.
 - "*Countdown & Brick*": Pokreće odbrojavanje od jednog sata, na kraju kojeg COLDCARD uništava svoja dva sigurna čipa, čineći ga trajno neupotrebljivim. Bez rezervne kopije, vaši bitkoini će biti izgubljeni. Ova akcija je dizajnirana da prevari napadača, koji misli da čeka otključavanje, dok se zapravo uređaj samouništava.
 - "*Just Countdown* : Pokreće jednostavno odbrojavanje od jednog sata, nakon čega se COLDCARD ponovo pokreće bez ikakvih daljih radnji. seed nije obrisan i uređaj ostaje netaknut. Pazite da ovu radnju ne pomešate sa opcijom "*Login Countdown*", koja se razmatra u narednim odeljcima, a koja dodaje odbrojavanje glavnom PIN-u dok omogućava pristup pravom Wallet.


![CCQ](assets/fr/17.webp)




- "*Look Blank*": Ova akcija čini da COLDCARD izgleda prazno, ostavljajući utisak da je seed obrisan. U stvarnosti, ništa se ne dešava i seed ostaje netaknut. Ovo simulira neiskorišćen ili resetovan COLDCARD.


![CCQ](assets/fr/18.webp)




- "*Just Reboot* : Kada se koristi Trick PIN, COLDCARD se jednostavno ponovo pokreće. Nijedna druga radnja se ne izvodi.


![CCQ](assets/fr/19.webp)




- "*Delta Mode*": Ova složena akcija, rezervisana za iskusne korisnike, dizajnirana je da se suprotstavi visoko sofisticiranim napadima pod prisilom, bilo od strane države ili rođaka sa privilegovanim informacijama. Kada je Delta Mode aktiviran, COLDCARD omogućava pristup pravom Wallet, omogućavajući napadaču da navigira i verifikuje da je to ispravan Wallet. Međutim, potpisi transakcija su blokirani, čime se sprečava bilo kakav transfer Bitcoin. Pored toga, pristup Mnemonic frazi je onemogućen i svaki pokušaj njenog preuzimanja će rezultirati njenim brisanjem. Da bi se povećala verodostojnost, Trick PIN korišćen sa Delta Mode mora deliti isti prefiks kao pravi PIN (da bi prikazao iste anti-phishing reči), ali sufiks mora biti drugačiji.


![CCQ](assets/fr/20.webp)


Kada odaberete akciju, potvrdite svoj izbor.


![CCQ](assets/fr/21.webp)


Zatim možete pregledati sve konfigurisane Trick PIN-ove u posebnom meniju.


![CCQ](assets/fr/22.webp)


Odabirom postojećeg Trik PIN-a, možete proveriti povezanu radnju. Takođe ga možete sakriti pomoću "*Sakrij Trik*", čineći ga nevidljivim u meniju Trik PIN-a. Možete ga obrisati klikom na "*Obriši Trik*", ili promeniti PIN kod zadržavajući povezanu radnju pomoću "*Promeni PIN*".


![CCQ](assets/fr/23.webp)


Opcija "*Dodaj ako je pogrešno*", dostupna u meniju "*Trik PIN*", omogućava vam da konfigurišete specifičnu akciju koja se automatski pokreće nakon određenog broja netačnih pokušaja unosa glavnog PIN koda. Broj dozvoljenih pokušaja može se postaviti tokom konfiguracije.


### Pomešaj Ključeve


Opcija Scramble Keys omogućava vam da izmešate cifre prikazane na dugmićima tastature prilikom unosa vašeg PIN koda. Ova funkcija štiti poverljivost vašeg PIN koda, čak i u slučaju nadzora od strane ljudi ili kamera.


Da biste aktivirali ovu opciju, pristupite meniju `Settings > Login Settings > Scramble Keys`.


![CCQ](assets/fr/24.webp)


Odaberite opciju "*Scramble Keys*".


![CCQ](assets/fr/25.webp)


Od sada, kada otključate svoj COLDCARD Q, tasterima na tastaturi će svaki put kada ih koristite biti dodeljeni novi brojevi nasumično.


![CCQ](assets/fr/26.webp)


### Odbrojavanje za prijavu


Ova opcija vam omogućava da uvedete sistematsko odbrojavanje svaki put kada pokušate da otključate vaš COLDCARD. Može biti integrisana u vašu sigurnosnu strategiju tako što će odložiti pristup uređaju u slučaju krađe, ili nametanjem odlaganja pre potpisivanja transakcije, na primer da biste se zaštitili u slučaju pljačke. Međutim, ovo odbrojavanje se primenjuje na sve vaše upotrebe, uključujući kada legitimno koristite vaš COLDCARD, što vas takođe obavezuje na strpljenje. Pazite da ne pomešate ovu opciju sa akcijom "*Just Countdown*", koja se aktivira samo kada se koristi specifičan Trick PIN.


Da biste konfigurisali ovu opciju, pristupite meniju `Settings > Login Settings > Login Countdown`.


![CCQ](assets/fr/27.webp)


Odaberite vreme odbrojavanja. Na primer, ako odaberete 1 sat, moraćete da čekate 1 sat za svaki pokušaj otključavanja COLDCARD Q.


![CCQ](assets/fr/28.webp)


Svaki put kada otključate, bićete upitani da unesete svoj PIN kod.


![CCQ](assets/fr/29.webp)


Zatim sačekajte vreme postavljeno odbrojavanjem.


![CCQ](assets/fr/30.webp)


Na kraju odbrojavanja, moraćete ponovo da unesete svoj PIN da biste pristupili uređaju.


![CCQ](assets/fr/31.webp)


### Prijava na Kalkulator


Ova opcija vam omogućava da maskirate vaš COLDCARD kao kalkulator prilikom otključavanja. Da biste aktivirali ovu funkciju, pristupite meniju `Settings > Login Settings > Calculator Login`.


![CCQ](assets/fr/32.webp)


Aktivirajte opciju tako što ćete je odabrati.


![CCQ](assets/fr/33.webp)


Od sada, svaki put kada se uređaj uključi, prikazaće se kalkulator sa osnovnim komandama.


![CCQ](assets/fr/34.webp)


Na primer, možete izračunati SHA256 Hash od "*Plan B Network*".


![CCQ](assets/fr/35.webp)


Da biste otključali COLDCARD iz režima kalkulatora, počnite unosom prefiksa vašeg PIN koda praćenog crticom. Na primer, ako je vaš PIN kod `00-00` (ovaj kod je slab i samo je primer, zato izaberite jak PIN kod), unesite `00-`. COLDCARD će zatim prikazati vaše dve reči protiv fišinga.


![CCQ](assets/fr/36.webp)


Zatim unesite svoj puni PIN kod, odvojen razmakom ili crticom, na primer: `00 00`.


![CCQ](assets/fr/37.webp)


COLDCARD će zatim izaći iz režima kalkulatora i otključati se normalno.


## Čisto uništavanje vašeg COLDCARD-a


Ako planirate da se otarasite svog COLDCARD Q, na primer zato što sada koristite drugi Hardware Wallet, važno je da pravilno uništite uređaj. Ovo osigurava da nijedna informacija vezana za vaš Wallet ne može biti povraćena od strane treće strane.


Postoje tri nivoa uništavanja informacija, u zavisnosti od vaših potreba. Pre nego što počnete, uverite se da je vaš Wallet uvezen u drugi Hardware Wallet, da imate pristup svim vašim sredstvima i, pre svega, da imate vašu Mnemonic frazu i bilo koji passphrase, koji su oba funkcionalna. Bez Wallet rezervne kopije, uništavanje vašeg COLDCARD-a će rezultirati gubitkom vaših bitkoina.


Prvi nivo uništenja sastoji se od brisanja samo seed. Ova opcija briše vašu Mnemonic frazu iz memorije COLDCARD-a, dok uređaj ostaje funkcionalan. Idealno je ako želite ponovo koristiti COLDCARD Q kasnije. Da biste izbrisali seed iz memorije, pristupite meniju `Advanced/Tools > Danger Zone > seed Functions > Destroy seed`.


![CCQ](assets/fr/38.webp)


Drugi nivo uništenja sastoji se od trajnog onemogućavanja dva sigurna čipa COLDCARD-a putem softvera. Ova akcija čini uređaj potpuno neupotrebljivim. Nećete ga moći preprodati, ponovo koristiti ili vratiti Coinkite-u: biće trajno uništen. Da biste nastavili, pratite korake opisane u prethodnom odeljku u vezi sa "*Brick Me*" PIN-om, a zatim namerno unesite ovaj PIN prilikom otključavanja COLDCARD-a.


Treći nivo uključuje fizičko uništavanje sigurnosnih komponenti vašeg COLDCARD Q uređaja. Kao i ranije, ovo će učiniti uređaj trajno neupotrebljivim. Da biste to uradili, koristite bušilicu da napravite rupu u dva čipa na gornjoj desnoj strani uređaja (kada je okrenut naopako), blizu natpisa "*SHOOT HERE*".


**Važne mere predostrožnosti** :




- Da biste izbegli rizik od električnog udara, uklonite baterije iz uređaja i isključite ga iz struje pre rukovanja.
- Sačekajte nekoliko minuta nakon isključivanja uređaja pre nego što počnete sa bušenjem.
- Nosite izolovane rukavice i zaštitne naočare kako biste osigurali svoju sigurnost.


![CCQ](assets/fr/39.webp)


Kada su čipovi probušeni, nemojte pokušavati ponovo povezati COLDCARD Q.


Čestitamo, sada ste upoznati sa naprednim opcijama COLDCARD Q!


Ako ste našli ovaj vodič korisnim, bio bih veoma zahvalan ako biste ostavili Green palac ispod. Slobodno podelite ovaj vodič na vašim društvenim mrežama. Hvala vam puno!


Takođe preporučujem ovaj drugi tutorijal, u kojem diskutujemo o korišćenju direktnog konkurenta CCQ, Ledger Flex :


https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a