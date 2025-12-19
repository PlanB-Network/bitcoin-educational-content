---
name: Jade DIY
description: Pretvorite razvojnu ploču od $15 u potpuno funkcionalan Bitcoin hardver wallet
---

![cover](assets/cover.webp)


## Bitcoin Hardware Wallet - Početnička Izgradnja


**Publika:** Zainteresovani graditelji sa malo ili nimalo iskustva u ugrađenim sistemima.


**Trajanje:** 2 sata (fleksibilno)


**Ishodi:** Do kraja, studenti će:



- Prepoznajte bezbednosni model DIY hardverskih novčanika u odnosu na komercijalne uređaje.
- Sastavite uređaj za potpisivanje zasnovan na mikrokontroleru.
- Flešuj open-source firmver i verifikuj kontrolni zbir izgradnje.
- Potpišite i emitujte mainnet transakciju koristeći njihov novi uređaj.


---

## Apstrakt


Ova dvodnevna radionica uči početnike kako da izgrade funkcionalni Bitcoin hardver wallet flešovanjem open-source Jade firmware-a na $15 LilyGO T-Display ploču. Studenti transformišu generički razvojni hardver u uređaj za potpisivanje uporediv sa komercijalnim novčanicima koji koštaju $150, učeći osnove bezbednosti kroz praktično iskustvo, a ne samo teoriju.


### Filozofija


Izrada sopstvenog uređaja za potpisivanje nije samo ušteda novca—radi se o razumevanju tehnologije koja štiti vaš Bitcoin. Ova radionica prihvata "bezbednost kroz razumevanje" umesto poverenja u crne kutije. Nabavkom komponenti, flešovanjem open-source firmvera i generisanjem entropije sami, studenti smanjuju rizik u lancu snabdevanja dok uče da kritički procenjuju bezbednosne tvrdnje. Cilj je informisana autonomija: studenti treba da razumeju i moć i ograničenja svog DIY uređaja u poređenju sa ojačanim komercijalnim alternativama.


---

## Konceptni priručnik (15 min)


### Šta je samostalno čuvanje i zašto je važno?


Bitcoin je stvoren da ukloni potrebu za pouzdanim trećim stranama, poput banaka i korporacija iz našeg monetarnog sistema. Umesto korišćenja poverenja, bitcoin koristi matematiku, fiziku i kriptografiju kako bi omogućio svakome moć da poseduje i kontroliše svoj novac bez potrebe za bilo čijim odobrenjem.


Način na koji ovo funkcioniše je da bitcoin postoji na globalnoj digitalnoj knjizi zvanoj blockchain, poznatoj i kao bitcoin timechain, koja je javna i transparentna knjiga vođena računarima, umesto centralizovane knjige kao što je bankovni račun.


Važno je razumeti da, kako biste premestili bitcoin sa jednog mesta na drugo, morate potpisati tu transakciju onim što se zove privatni ključ. Zamislite to kao otključavanje trezora lozinkom i premeštanje bitcoina u nečiji drugi trezor. Bitcoin vam daje moć da sami držite ključeve tog trezora, umesto da se oslanjate na banku da premesti vaš novac za vas.


Uz veliku moć dolazi velika odgovornost, izgubite ključeve i vaša sredstva su zauvek izgubljena. Na ovaj način, možete misliti o ključevima trezora kao o samom novcu. Iako ključevi nisu isto što i bitcoin, oni su mehanizam za premeštanje vaših sredstava i stoga ih je izuzetno važno zaštititi. Zato kažemo "nema vaših ključeva, nema vaših novčića".


Termin samostalno čuvanje može zvučati zbunjujuće, ali sve što znači je držanje sopstvenih privatnih ključeva i kontrolisanje sopstvenog bitkoina. Ako ne držite taj ključ, verujete nekome drugom da ga drži za vas. Ako je vaš bitkoin u ETF-u ili na berzi (Mt. Gox, FTX, Coinbase, Binance, itd.), vi ne posedujete bitkoin, već potraživanje na bitkoin. Ovo uvodi sve vrste rizika, kao što su hakovanje berzi i gubitak vašeg bitkoina ili kompanije koje pozajmljuju vaš novac i daju vam samo deo u rezervi. Dodatno, pouzdane treće strane bi imale potpunu kontrolu nad vašim novcem i mogle bi ograničiti ili zamrznuti isplate.


![image](assets/fr/01.webp)


Sa samostalnim čuvanjem uklanjate poverenje iz jednačine. Niko ne može zamrznuti vaša sredstva ili odbiti transakciju, možete slati novac preko granica, bilo kome, u bilo koje vreme, i ne treba vam bankovni račun, lična karta, niti bilo čije odobrenje. Niko ne može da vas zaustavi, cenzuriše ili pokrade, otključavajući punu moć bitkoina kao novca slobode. Zato kažemo, sa bitkoinom možete biti sopstvena banka.


Bitcoin je stvoren da reši problem manipulacije poverenjem i novcem, kao izlaz iz našeg trenutnog sistema, ali izlaz funkcioniše samo ako uzmete ključeve. Zato je samostalno čuvanje tako važno.


### Šta je Wallet?


Termin wallet je pomalo pogrešan naziv i stoga može biti zbunjujući. Da, istina je da bitcoin wallet, kao i fizički wallet, čuva vrednost. Ali glavna razlika je u tome što bitcoin novčanici zapravo ne čuvaju nikakav bitcoin.


Bitcoin postoji samo kao unos u knjizi na javnom blockchain-u, ili unutar metaforičkih trezora u sajberprostoru. Zapamtite da za pomeranje bitcoina morate koristiti svoje ključeve da otključate trezor i premestite novčiće negde drugde, privatni ključevi su ono što se koristi za trošenje bitcoina. Kada obavite transakciju sa svojim wallet, vi zapravo samo koristite svoje ključeve da potpišete transakciju. Ovako pokazujete dokaz da posedujete novac i imate pravo da potrošite te novčiće.


Bitcoin novčanici zapravo samo čuvaju vaše privatne ključeve, tako da bi ih preciznije bilo nazvati privjescima za ključeve.


### Hot vs Cold Novčanici


Vruć wallet je softverska aplikacija na vašem telefonu ili računaru. Povezan je na internet, što ga čini lakšim za korišćenje i bržim za potpisivanje transakcija, ali to takođe znači da je više izložen hakerima, malverima i fišingu. Naziva se "vrućim" jer je povezan na internet, uključen i uključen. Primer bi bio telefon wallet ili pregledač wallet.


S druge strane, hladni wallet, ili hardverski wallet, je uređaj koji kreira i čuva vaš ključ van mreže. Ovo uklanja mogućnost da neko hakuje vaša sredstva i mnogo je sigurnije za dugoročne uštede, međutim, to je uređaj koji je potreban za potpisivanje svake transakcije i može biti manje praktičan.


### Hardware Wallet Model Pretnje


Hardverski novčanici postoje da reše osnovni problem: kako potpisati Bitcoin transakcije bez izlaganja vaših privatnih ključeva računaru povezanom na internet koji bi mogao biti ugrožen malverom ili udaljenim napadačima? Osnovni model pretnje pretpostavlja da je vaš svakodnevni laptop ili telefon potencijalno neprijateljski. Hardverski wallet stvara izolovano okruženje gde privatni ključevi nikada ne napuštaju uređaj, a potpisivanje transakcija se dešava u secure element ili mikrokontroleru koji samo prenosi potpis nazad na host računar, a ne i sam ključ. Čak i ako je vaš računar potpuno ugrožen, napadač ne može ukrasti vaš Bitcoin bez fizičkog pristupa uređaju i vašem PIN-u.


Međutim, hardverski novčanici uvode sopstvene pretnje. Morate verovati da proizvođač nije uveo zadnja vrata, da lanac snabdevanja nije bio kompromitovan i da je generisanje slučajnih brojeva zaista slučajno. Fizički napadači mogu izvući ključeve putem napada bočnim kanalima ili manipulacijom čipom, a neko s privremenim pristupom mogao bi modifikovati vaš uređaj. Izgradnja sopstvenog hardvera wallet pomaže vam da razumete ove kompromise—donećete odluke o sigurnosnim elementima naspram mikro kontrolera opšte namene, kako da verifikujete transakcije na ekranu i kako da se zaštitite od udaljenih i fizičkih pretnji. Cilj nije savršena sigurnost, već razumevanje protiv kojih pretnji se štitite i koje ostaju.


### Ključni Koncepti



- Entropija i seed fraze:** Vaš wallet je siguran samo koliko i nasumičnost koja ga stvara. Kombinovaćemo generator slučajnih brojeva uređaja sa trikovima prilagođenim ljudima, poput bacanja kockica, pretvoriti tu entropiju u 12- ili 24-rečnu [BIP39 frazu](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki), i napustiti prostoriju sa pisanim ili metalnim rezervnim primerkom kojem verujete.
- Higijena seed fraze:** Tretirajte seed kao glavne ključeve vaših ušteda. Nikada ne kucajte reči na telefon ili računar—keyloggeri, snimci ekrana i cloud backupovi mogu je zauvek otkriti. Držite frazu van mreže, čuvajte je negde gde samo vi možete pristupiti, i vežbajte da je naglas pročitate pre nego što krenete.
- Sigurni element + mikrokontroler:** Zamislite secure element kao trezor, a mikrokontroler kao mozak. secure element čuva privatne ključeve uz otpornost na neovlašćeno rukovanje, dok mikrokontroler upravlja ekranom, dugmadima i logikom firmvera. Imajte na umu da hardverski novčanici koje danas pravimo nemaju secure element. To ne znači da su nesigurni, već samo da imaju jedan nivo zaštite manje.
- Poverenje u firmver:** Firmver je nevidljivi operativni sistem wallet. Uvek preuzimajte sa označenih izdanja, proverite objavljeni hash i razumite da reproduktivne izrade omogućavaju više ljudi da kompajliraju isti kod i dobiju potpuno isti binarni fajl. Ako se kontrolni zbir ne poklapa, ne potpisujete.


---

## Šta gradimo?


Uzimamo generički hardver, LilyGo T-Display, i flešujemo Jade SDK firmver na njega. [Jade Plus](https://blockstream.com/jade/jade-plus/) je open-source wallet, koji obično košta $150:


![image](assets/fr/02.webp)


Danas ćemo umesto toga flešovati njihov firmver na hardver od $15.


### Šta Kupiti


![image](assets/fr/03.webp)



- LilyGO T-Display (16MB sa kućištem, model K164)** — [Naručite direktno od LilyGO](https://lilygo.cc/products/t-display?srsltid=AfmBOornob5U3FzZifuSwBBOdeXKcdPDqkYEnAVYKBLdzl0BPyNglGBR) za oko $15. Ova ESP32 ploča pruža ekran, dugmad i USB interfejs koji odražavaju Blockstream-ov Jade Plus. Ugrađeni ESP32 takođe uključuje Wi-Fi i Bluetooth radio; poslaćemo firmver koji ih drži onemogućenim, ali oni oblikuju vaš model pretnji jer zlonamerni kod može ponovo da ih uključi.
- USB-C kabl** — Ponesite kabl sposoban za prenos podataka kako biste mogli da flešujete firmver i napajate ploču direktno sa svog laptopa (potpuno u redu za korišćenje u učionici).


### Zašto napraviti svoj sopstveni Hardware Wallet?



- Uštedite približno $135 u odnosu na kupovinu komercijalnog uređaja.
- Izgradite udobnost sa flešovanjem firmvera, sigurnosnim elementima i higijenom wallet.
- Pokrenite dodatne uređaje za potpisivanje kako biste raspodelili uštede na više novčanika.
- Smanjite rizik u lancu snabdevanja tako što ćete sami nabavljati i sastavljati svaki komponent.
- Imajte na umu Loppovu mantru: suverenitet i pogodnost su uvek u sukobu.


## Fizičko postavljanje


### Pripremite Svoj Slučaj


Imate dve opcije za smeštaj vaše LilyGO T-Display ploče: 3D štampano kućište ili zvanično LilyGO kućište. Štampano kućište možete pronaći i odštampati sa [ovog modela](https://www.printables.com/model/119144-lilygo-ttgo-t-display-enclosure). Ono nudi laganu i prilagodljivu školjku za vaš uređaj.


![image](assets/fr/04.webp)


Alternativno, možete koristiti zvaničnu LilyGO futrolu, koja pruža nešto drugačije uklapanje i završnu obradu, nudeći robusniju zaštitu i uglađen izgled.


![image](assets/fr/05.webp)


Imajte na umu da se štampani i zvanični kućišta malo razlikuju u dizajnu i sastavljanju. Koju god opciju da izaberete, osigurajte da je ploča pravilno postavljena unutar kućišta kako biste izbegli labave veze ili oštećenja.


### Pregledaj Board


Pre nego što nastavite, pažljivo pregledajte svoju LilyGO T-Display ploču zbog bilo kakvih vidljivih oštećenja ili ostataka. Proverite da li su displej, dugmad i USB-C port čisti i bez prašine ili kapljica lema. Rukujte pločom pažljivo i pridržavajte se bezbednosnih mera protiv elektrostatičkog pražnjenja (ESD) tako što ćete se uzemljiti ili koristiti ESD narukvicu kako biste sprečili oštećenje osetljivih komponenti.


### Povežite se sa svojim laptopom


Koristeći USB-C kabl sposoban za prenos podataka, povežite LilyGO ploču sa svojim laptopom. Ova veza će obezbediti napajanje i omogućiti vam da flešujete firmver.


Na pokretanju, dočekaće vas sledeći ekran:


![image](assets/fr/06.webp)



Kada se uključi, LilyGO će prikazati testni ekran u boji koji prolazi kroz pune boje. Ovo potvrđuje da ekran i ploča funkcionišu ispravno pre nego što se učita firmver.


Kada se test boje završi, ekran će se postaviti u podrazumevano stanje, što ukazuje da je ploča spremna za sledeće korake u procesu izrade.


![image](assets/fr/07.webp)


## The Easy Way or the Hard Way


Postoje dva glavna pristupa za flešovanje vašeg wallet firmvera: lakši način i teži način. Lakši način koristi unapred konfigurisane alate ili veb-bazirane flešere koji automatski učitavaju firmver na vaš uređaj uz minimalan unos. Ova metoda je idealna za početnike koji žele brzu pobedu ili preferiraju da izbegnu složenosti debagovanja i interakcije sa komandnom linijom. Ona pojednostavljuje proces i omogućava vam brži početak rada, čineći ga dostupnim za one koji su novi u razvoju ugrađenih sistema ili hardverskih novčanika.


S druge strane, teži način uključuje ručno korišćenje alata komandne linije za flešovanje firmvera. Ovaj pristup zahteva verifikaciju potpisa i kontrolnih zbirova firmvera kako bi se osigurala autentičnost i integritet, pružajući vam dublje razumevanje procesa flešovanja i načina na koji firmver komunicira sa hardverom. Iako zahteva više truda i poznavanje terminalskih komandi, nudi veću kontrolu, transparentnost i poverenje u bezbednost vašeg uređaja.


Svaka metoda ima svoje kompromise: lakši način žrtvuje određeni stepen poverenja i razumevanja za brzinu i praktičnost, dok teži način zahteva više vremena i tehničkih veština, ali vas nagrađuje fleksibilnošću i jačim razumevanjem osnovne tehnologije. Instruktori bi trebalo da podstaknu studente da izaberu put koji najbolje odgovara njihovom nivou udobnosti i radoznalosti, podstičući i samopouzdanje i istraživanje.


## Lakoća


Najlakši način za flešovanje ESP32



- Idite na zvanični Blockstream Github: [https://github.com/Blockstream/jadediyflasher](https://github.com/Blockstream/jadediyflasher)


![image](assets/fr/08.webp)



- Možete preuzeti izvorni fajl i pokrenuti vebsajt lokalno, ali GitHub ga već hostuje na [https://blockstream.github.io/jadediyflasher/](https://blockstream.github.io/jadediyflasher/). GitHub direktno isporučuje HTML, CSS, JavaScript, itd. vašem pregledaču tako da možete flešovati uređaj bez instaliranja alata za programere.


![image](assets/fr/09.webp)



- Otvorite padajući meni (verovatno je podrazumevano podešen na `M5Stack Core2`) i izaberite vašu razvojnu ploču — za ovu klasu, odaberite `LILYGO T-Display`.


![image](assets/fr/10.webp)



- Kada kliknete na flash, ovo će se pojaviti. Da biste znali koji uređaj je LILYGO, isključite lilygo i ponovo ga uključite. COM port na kojem se lilygo pojavljuje i nestaje. Kliknite na COM port na koji je Jade priključen.


![image](assets/fr/11.webp)



- To je to, traka napretka bi trebalo da se pojavi i kada se završi, spremni ste da je postavite.


## Postavljanje Jade Wallet


Kada je firmware uspešno flešovan, vaš LilyGO T-Display je sada potpuno funkcionalan Jade hardver wallet. Ovaj deo će vas provesti kroz proces početnog podešavanja, od generisanja vaše seed fraze do povezivanja uređaja sa wallet softverom kao što su Sparrow ili Blockstream Green mobilna aplikacija.


### Početno pokretanje i podešavanje uređaja



- Uključite uređaj:** Dok je LilyGO još uvek povezan sa vašim laptopom putem USB-C, Jade firmware bi trebalo automatski da se pokrene. Videćete Jade logo na ekranu.



- Uđite u režim podešavanja:** Uređaj će vam prikazati početni meni. Koristite dva fizička dugmeta na ploči za navigaciju:
 - Levo dugme:** Pomeri gore/nazad
 - Desno dugme:** Pomeri dole/napred
 - Oba dugmeta istovremeno:** Izaberi/potvrdi



- Odaberite "Setup":** Idite na opciju Setup i pritisnite oba dugmeta da potvrdite. Uređaj će vas voditi kroz početni proces konfiguracije.


### Kreiranje Vašeg Wallet



- Izaberite "Begin Setup":** Uređaj će vas uputiti da započnete proces kreiranja wallet. Potvrdite vaš izbor.



- Odaberite "Kreiraj novi Wallet":** Biće vam ponuđene dve opcije:
 - Kreiraj Novi Wallet:** Generiše novu seed frazu (izaberite ovo za radionicu)
 - Vrati Wallet:** Oporavi postojeći wallet iz seed fraze (za napredne korisnike)



- Odaberite "Kreiraj novi Wallet" i potvrdite.



- Generiši entropiju:** Uređaj će koristiti svoj generator slučajnih brojeva za kreiranje kriptografske entropije. Ovaj proces traje nekoliko sekundi dok uređaj prikuplja nasumičnost iz više izvora.


### Beleženje Vaše Seed Fraze



- Zapišite svoju seed frazu:** Uređaj će sada prikazati 12 reči BIP39 seed fraze, jednu po jednu. Ovo je najkritičniji korak u celom procesu.


**Važne bezbednosne prakse:**


- Napišite svaku reč jasno na papir (koristite priložene seed kartice sa frazama ako su dostupne)
- Proveri svaku reč dok je pišeš
- Nikada ne fotografišite frazu seed svojim telefonom
- Nikada ne kucaj reči u bilo koji kompjuter ili telefon
- Čuvajte svoju seed frazu privatnom—ne delite ekran niti pokazujte drugima



- Potvrdite svoju seed frazu:** Nakon što zapišete svih 12 reči, uređaj će vas zamoliti da potvrdite nekoliko reči iz fraze kako biste se uverili da ste ih ispravno zabeležili. Koristite dugmad da izaberete tačnu reč za svaki upit.


**Profesionalni savet:** Pre nego što nastavite, vežbajte čitanje vaše seed fraze naglas (tiho, da drugi ne čuju). Ovo pomaže da uočite greške u rukopisu ili nejasnoće.


### Metod povezivanja



- Izaberite tip veze:** Jade firmware podržava dva načina povezivanja:
 - USB:** Žičana veza putem USB-C kabla (preporučeno za ovu radionicu)
 - Bluetooth:** Bežična veza sa mobilnim uređajima



- Odaberite **USB** za sada, jer je to najjednostavnija opcija za desktop wallet softver i ne uvodi bežične vektore napada.



- Imenovanje uređaja:** Jade će prikazati jedinstveni identifikator poput "Connect Jade A7D924". Ovaj identifikator pomaže vam da razlikujete više hardverskih novčanika ako napravite više od jednog. Zabeležite ovaj identifikator ako želite.


### Povezivanje sa Wallet Softverom


Sada imate dve glavne opcije za interfejs sa vašim novokreiranim hardverom wallet: mobilna aplikacija Blockstream Green (za korišćenje u pokretu) ili Sparrow Wallet (za korišćenje na desktopu sa naprednijim funkcijama). Za ovu radionicu, fokusiraćemo se na Sparrow Wallet, jer nudi bolji uvid u tehničke detalje Bitcoin transakcija.


#### Opcija 1: Blockstream Green Mobilna Aplikacija (Brzi Početak)


Ako želite brzo testirati svoj uređaj pomoću mobilnog uređaja:



- Preuzmite aplikaciju **Blockstream Green** iz App Store-a (iOS) ili Google Play-a (Android)
- Otvorite aplikaciju i izaberite "Connect Hardware Wallet"
- Izaberite "Jade" sa liste podržanih uređaja
- Povežite svoj Jade sa telefonom koristeći USB-C na USB-C kabl (ili USB-C na Lightning adapter za iPhone 15+).
- Pratite uputstva na ekranu da biste se povezali i kreirali svoj prvi wallet


**Napomena o Liquid:** Aplikacija Blockstream Green podržava i Bitcoin i Liquid (sidechain Bitcoin). Ako koristite funkcije Liquid, može vam biti zatraženo da "Izvezete glavni ključ za zaslepljivanje"—ovo omogućava aplikaciji da vidi iznose transakcija na Liquid mreži, koji su inače poverljivi. Za ovu radionicu, možete preskočiti funkcije Liquid i fokusirati se na standardne Bitcoin transakcije.


#### Opcija 2: Sparrow Wallet (Preporučeno za radionicu)


Sparrow Wallet je moćna desktop aplikacija koja vam pruža detaljnu kontrolu nad vašim Bitcoin transakcijama i besprekorno se povezuje sa vašim Jade hardverom wallet.


**Instalacija:**



- Preuzmite Sparrow Wallet sa zvaničnog sajta: [sparrowwallet.com](https://sparrowwallet.com)
- Proverite potpis preuzimanja (pogledajte Sparrow dokumentaciju za detalje)
- Instalirajte i pokrenite aplikaciju


**Povezivanje vašeg Jade sa Sparrow:**



- U Sparrow, idite na **File → New Wallet**
- Dajte svom wallet ime (npr. "Moj Jade Wallet")
- Kliknite **Connected Hardware Wallet**
- Sparrow bi trebalo automatski da detektuje vaš priključeni Jade uređaj
- Ako se to zatraži, potvrdite vezu na Jade ekranu pritiskom na oba dugmeta
- Odaberite željeni tip pisma:
 - Native Segwit (P2WPKH):** Preporučeno za početnike—najniže naknade, najšira kompatibilnost sa modernim novčanicima
 - Ugnježdeni Segwit (P2SH-P2WPKH):** Za kompatibilnost sa starijim uslugama
 - Taproot (P2TR):** Najnapredniji, nudi najbolju privatnost i najniže naknade, ali zahteva najnoviju podršku wallet
- Kliknite **Importuj Keystore** da biste završili povezivanje


**Konfigurisanje Server Konekcije za Sparrow:**


Pre nego što možete videti svoj saldo ili emitovati transakcije, Sparrow treba da se poveže sa Bitcoin čvorom kako bi preuzeo podatke sa blockchain-a. Imate nekoliko opcija, svaka sa različitim kompromisima između pogodnosti, privatnosti i poverenja:



- Javni Electrum Server (Najlakši, najmanje privatan):** Povezuje se na javni server kojim upravlja treća strana. Brz za postavljanje, ali server može videti adrese vašeg wallet i potencijalno ih povezati sa vašom IP adresom. Dobar za testiranje na testnetu.
 - U Sparrow, idite na **Tools → Preferences → Server**
 - Odaberite **Javni server** i izaberite server sa liste
 - Kliknite **Testiraj vezu** da biste verifikovali



- Bitcoin Core ili Knots Node (Najprivatniji, najviše posla):** Pokrenite svoj sopstveni puni Bitcoin čvor. Ovo je zlatni standard za privatnost i verifikaciju, jer sami validirate svaku transakciju i ne verujete serverima drugih. Međutim, zahteva preuzimanje celog blokčejna (~600GB) i održavanje sinhronizacije vašeg čvora.
 - Instaliraj i sinhronizuj Bitcoin Core ili Knots
 - U Sparrow, idite na **Tools → Preferences → Server**
 - Odaberite **Bitcoin Core ili Knots** i unesite detalje veze vašeg čvora



- Private Electrum Server (Dobra ravnoteža):** Hostujte sopstveni Electrum server (kao što je Fulcrum ili Electrs) povezan sa vašim Bitcoin Core ili Knots čvorom. Nudi potpunu privatnost bez potrebe da pokrećete Sparrow na istoj mašini kao vaš čvor.
 - Postavite Electrum server koji pokazuje na vaš Bitcoin Core ili Knots čvor
 - U Sparrow, idite na **Tools → Preferences → Server**
 - Odaberite **Private Electrum** i unesite URL vašeg servera


Za ovu radionicu, korišćenje **Public Electrum Server** je sasvim u redu za transakcije na testnetu. U produkcionom okruženju sa stvarnim sredstvima, želeli biste da razmotrite pokretanje sopstvenog čvora ili korišćenje pouzdanog privatnog servera za maksimalnu privatnost.


#### Opcija 3: Blockstream Green Desktop App (Brzi početak)


Blockstream Green je softver za završetak postavljanja JadeDIY i mora biti sa desktop verzijom.



- Preuzmite zvaničnu Blockstream aplikaciju — ovo je link ka njoj sa njihove veb stranice. Kada ste tamo kliknite [Preuzmi sada](https://blockstream.com/app/).


![image](assets/fr/12.webp)



- U zavisnosti od toga gde idu vaša preuzimanja, najverovatnije će datoteka biti u vašem folderu Preuzimanja. Proverite tamo i dvaput kliknite na izvršnu datoteku da biste instalirali softver.


![image](assets/fr/13.webp)



- Možda ćete morati da date administratorska prava da biste pokrenuli instalacioni program. Kada to uradite, pojaviće se prozor koji bi trebalo da izgleda kao na sledećoj slici — kliknite na **Next**.


![image](assets/fr/14.webp)



- Izaberite gde želite da instalirana aplikacija bude smeštena (lokacija sa vašim drugim programima ili negde gde je lako pronaći), zatim kliknite na **Dalje**.


![image](assets/fr/15.webp)



- Instalacioni program će tražiti ime prečice. Unesite jedno ili zadržite podrazumevano, zatim kliknite na **Next**.


![image](assets/fr/16.webp)



- Ako želite prečicu na radnoj površini, označite polje; u suprotnom kliknite **Dalje**.


![image](assets/fr/17.webp)



- Na kraju, kliknite na **Install** i sačekajte nekoliko minuta da se instalacija završi.


![image](assets/fr/18.webp)



- Traka napretka treba da se popuni do kraja.


![image](assets/fr/19.webp)



- Kada se završi, pojaviće se nova stranica — kliknite na **Finish**.


![image](assets/fr/20.webp)



- Pronađite svoju novoinstaliranu Blockstream aplikaciju (primer prikazan u Windows 11 Start meniju).


![image](assets/fr/21.webp)



- Kada ga pronađete, kliknite za pokretanje — treba da se pojavi početni ekran.


### Provera vaše postavke


Jednom kada se povežete sa Sparrow (ili drugom aplikacijom wallet):



- Proverite svoje adrese:** Sparrow će prikazati adrese za primanje izvedene iz vaše seed fraze. Možete verifikovati adresu na vašem Jade uređaju tako što ćete otići na karticu "Primanje" u Sparrow i kliknuti na "Prikaži Address"—adresa bi trebalo da se pojavi i na ekranu vašeg računara i na Jade displeju.



- Generiši adresu za primanje:** Klikni na karticu **Primanje** u Sparrow i kopiraj svoju prvu Bitcoin adresu za primanje.



- Spremni za transakcije:** Vaš hardver wallet je sada potpuno konfigurisan i spreman da prima i potpisuje Bitcoin transakcije. Pređite na sledeći odeljak da vežbate potpisivanje testnet transakcije.



---

### Brza kontrolna lista za postavljanje



- Jade firmware se uspešno pokreće
- Novi wallet kreiran sa 12-rečnom seed frazom
- Fraza semena jasno napisana i verifikovana
- Izabran je USB režim povezivanja
- Wallet softver (Sparrow) instaliran i povezan
- Veza sa serverom konfigurisana (javni Electrum za mainnet)
- Prva primljena adresa generisana i verifikovana na uređaju



---

**MIT Licenca**


**Autorska prava (c) 2025 The Bitcoin Network NYC**


Ovime se daje dozvola, bez naknade, bilo kojoj osobi koja dobije kopiju ovog softvera i pratećih dokumentacionih fajlova ("Softver"), da koristi Softver bez ograničenja, uključujući bez ograničenja prava na korišćenje, kopiranje, modifikovanje, spajanje, objavljivanje, distribuciju, podlicenciranje i/ili prodaju kopija Softvera, i da dozvoli osobama kojima je Softver dostavljen da to učine, pod sledećim uslovima:


Gore navedena obaveštenja o autorskim pravima i ovo obaveštenje o dozvoli moraju biti uključeni u sve kopije ili značajne delove Softvera.


SOFTVER SE PRUŽA "KAKAV JESTE", BEZ IKAKVE GARANCIJE, IZRIČITE ILI PODRAZUMEVANE, UKLJUČUJUĆI ALI NE OGRANIČAVAJUĆI SE NA GARANCIJE PRODAJNOSTI, POGODNOSTI ZA ODREĐENU NAMENU I NEKRŠENJA PRAVA. NI U KOM SLUČAJU AUTORI ILI VLASNICI AUTORSKIH PRAVA NEĆE BITI ODGOVORNI ZA BILO KAKAV ZAHTEV, ŠTETU ILI DRUGU ODGOVORNOST, BILO DA JE U PITANJU UGOVOR, DELIKT ILI NEŠTO DRUGO, KOJA PROIZILAZI IZ, IZ ILI U VEZI SA SOFTVEROM ILI UPOTREBOM ILI DRUGIM POSLOVANJEM U SOFTVERU.


---