---
name: Blockstream Green - Liquid
description: Postavljanje Wallet na Liquid Network Sidechain
---
![cover](assets/cover.webp)


Bitcoin protokol ima namerna tehnička ograničenja koja pomažu u održavanju decentralizacije mreže i osiguravaju da je bezbednost raspodeljena među svim korisnicima. Međutim, ova ograničenja ponekad mogu frustrirati korisnike, naročito tokom zagušenja zbog velikog broja istovremenih transakcija. Debata o skalabilnosti Bitcoin dugo je delila zajednicu, posebno tokom Rata oko veličine bloka. Od ove epizode, unutar Bitcoin zajednice je široko prepoznato da skalabilnost mora biti osigurana rešenjima off-chain, na drugim Layer sistemima. Ova rešenja uključuju bočne lance, koji su i dalje relativno nepoznati i malo korišćeni u poređenju sa drugim sistemima kao što je Lightning Network.


Sidechain je nezavisni Blockchain koji radi paralelno sa glavnim Bitcoin Blockchain. Koristi Bitcoin kao obračunsku jedinicu, zahvaljujući mehanizmu zvanom "*two-way peg*". Ovaj sistem omogućava zaključavanje bitkoina na glavnom lancu kako bi se njihova vrednost reprodukovala na Sidechain, gde cirkulišu u obliku tokena podržanih originalnim bitkoinima. Ovi tokeni obično zadržavaju paritet vrednosti sa bitkoinima zaključanim na glavnom lancu, a proces se može obrnuti kako bi se sredstva povratila na Bitcoin.


Cilj sajdčejnova je da ponude dodatne funkcionalnosti ili tehnička poboljšanja, kao što su brže transakcije, niže naknade ili podrška za pametne ugovore. Ove inovacije ne mogu uvek biti direktno implementirane na Bitcoin Blockchain bez ugrožavanja njegove decentralizacije ili sigurnosti. Sajdčejnovi stoga omogućavaju testiranje i istraživanje novih rešenja uz očuvanje integriteta Bitcoin. Međutim, ovi protokoli često zahtevaju kompromise, posebno u smislu decentralizacije i sigurnosti, u zavisnosti od izabranog modela upravljanja i mehanizma konsenzusa.


Danas je najpoznatiji Sidechain verovatno Liquid. U ovom vodiču, prvo ću vam reći šta je Liquid, a zatim vas voditi kroz to kako da ga lako počnete koristiti sa aplikacijom Blockstream Green, kako biste mogli uživati u svim njegovim prednostima.


![LIQUID GREEN](assets/fr/01.webp)


## Šta je Liquid Network?


Liquid je federativni Sidechain overlay za Bitcoin, razvijen od strane Blockstream-a kako bi poboljšao brzinu transakcija, poverljivost i funkcionalnost. Koristi bilateralni mehanizam sidrenja uspostavljen na federaciji da zaključa bitkoine na glavnom lancu i stvori Liquid-bitkoine (L-BTC) zauzvrat, tokene koji cirkulišu na Liquid dok ostaju podržani originalnim bitkoinima.


![LIQUID GREEN](assets/fr/02.webp)


Liquid Network se oslanja na federaciju učesnika, koju čine priznati entiteti iz ekosistema Bitcoin, koji validiraju blokove i upravljaju bilateralnim povezivanjem. Pored L-BTC, Liquid takođe omogućava izdavanje drugih digitalnih sredstava, kao što su stabilni novčići i druge kriptovalute.


![LIQUID GREEN](assets/fr/03.webp)


## Predstavljamo Blockstream Green


Blockstream Green je Software Wallet dostupan na mobilnim uređajima i desktopu. Ranije poznat kao *Green Address*, ovaj Wallet je postao Blockstream projekat nakon njegove akvizicije 2016. godine.


Green je posebno jednostavna aplikacija za korišćenje, što je čini zanimljivom za početnike. Nudi sve osnovne funkcije dobrog Bitcoin Wallet, uključujući RBF (*Replace-by-fee*), opciju povezivanja sa Tor-om, mogućnost povezivanja sopstvenog čvora, SPV (*Simple Payment Verification*), označavanje i kontrolu novčića.


Blockstream Green takođe podržava Liquid Network, i to ćemo saznati u ovom vodiču. Ako želite da koristite Green za druge aplikacije, preporučujem da pogledate i ove druge vodiče:


https://planb.network/tutorials/wallet/desktop/blockstream-green-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da

https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143

https://planb.network/tutorials/wallet/mobile/blockstream-green-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

## Instaliranje i konfiguracija aplikacije Blockstream Green


Prvi korak je naravno preuzimanje aplikacije Green. Idite u svoju prodavnicu aplikacija:



- [Za Android](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet);
- [Za Apple](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590).

![LIQUID GREEN](assets/fr/04.webp)


Za korisnike Androida, aplikaciju možete instalirati i putem `.apk` fajla [dostupnog na Blockstream-ovom GitHub-u](https://github.com/Blockstream/green_android/releases).


![LIQUID GREEN](assets/fr/05.webp)


Pokrenite aplikaciju, zatim označite polje "Prihvatam uslove...*".


![LIQUID GREEN](assets/fr/06.webp)


Kada prvi put otvorite Green, početni ekran se pojavljuje bez konfigurisanog Wallet. Kasnije, ako kreirate ili uvezete novčanike, oni će se pojaviti u ovom Interface. Pre nego što pređete na kreiranje Wallet, preporučujem da prilagodite postavke aplikacije prema vašim potrebama. Kliknite na "Postavke aplikacije".


![LIQUID GREEN](assets/fr/07.webp)


Opcija "*Poboljšana privatnost*", dostupna samo na Androidu, poboljšava privatnost onemogućavanjem snimaka ekrana i skrivanjem pregleda aplikacija. Takođe automatski zaključava pristup aplikaciji čim se vaš telefon zaključa, čineći vaše podatke težim za izlaganje.


![LIQUID GREEN](assets/fr/08.webp)


Za one koji žele poboljšati svoju privatnost, aplikacija nudi opciju usmeravanja vašeg saobraćaja putem Tor-a, mreže koja šifrira sve vaše veze i otežava praćenje vaših aktivnosti. Iako ova opcija može malo usporiti rad aplikacije, toplo se preporučuje za zaštitu vaše privatnosti, posebno ako ne koristite svoj sopstveni kompletan čvor.


![LIQUID GREEN](assets/fr/09.webp)


Za korisnike koji imaju svoj kompletan čvor, Green Wallet nudi opciju povezivanja putem Electrum servera, garantujući potpunu kontrolu nad informacijama mreže Bitcoin i širenjem transakcija. Ali ova funkcija je za klasične Bitcoin novčanike, tako da vam nije potrebna ako koristite Liquid.


![LIQUID GREEN](assets/fr/10.webp)


Još jedna alternativna funkcija je opcija "*SPV Verification*", koja vam omogućava da direktno verifikujete određene Blockchain podatke i tako smanjite potrebu za poverenjem u podrazumevani čvor Blockstream-a, iako ova metoda ne pruža sve garancije Full node. Opet, ovo će uticati samo na vaše onchain Bitcoin novčanike, ne na Liquid.


![LIQUID GREEN](assets/fr/11.webp)


Kada prilagodite ova podešavanja svojim potrebama, kliknite na dugme "*Save*" i ponovo pokrenite aplikaciju.


![LIQUID GREEN](assets/fr/12.webp)


## Kreiraj Liquid Wallet na Blockstream Green


Sada ste spremni da kreirate Liquid Wallet. Kliknite na dugme "*Get Started*".


![LIQUID GREEN](assets/fr/13.webp)


Možete birati između kreiranja lokalnog Software Wallet ili upravljanja Cold Wallet putem Hardware Wallet. Za ovaj vodič, fokusiramo se na kreiranje Hot Wallet na Liquid, tako da ćete morati odabrati opciju "*Na ovom uređaju*". Takođe možete koristiti kompatibilan Hardware Wallet, kao što je Blockstream Jade, za osiguranje vašeg Liquid Wallet.


![LIQUID GREEN](assets/fr/14.webp)


Zatim možete izabrati da obnovite postojeći Bitcoin Wallet ili da kreirate novi. Za potrebe ovog tutorijala, kreiraćemo novi Wallet. Međutim, ako treba da regenerišete postojeći Liquid Wallet iz njegove Mnemonic fraze, na primer nakon gubitka vašeg Hardware Wallet, moraćete da izaberete drugu opciju.


![LIQUID GREEN](assets/fr/15.webp)


Zatim možete birati između 12-reči ili 24-reči Mnemonic fraze. Ova fraza će vam omogućiti da povratite pristup vašem Wallet sa bilo kog kompatibilnog softvera u slučaju problema sa vašim telefonom. Trenutno, izbor 24-reči fraze ne nudi više sigurnosti od 12-reči fraze. Stoga preporučujem da izaberete 12-reči Mnemonic frazu.


Green će vam zatim pružiti vašu Mnemonic frazu. Pre nego što nastavite, uverite se da vas niko ne posmatra. Kliknite na "*Prikaži frazu za oporavak*" da biste je prikazali na ekranu.


![LIQUID GREEN](assets/fr/16.webp)


**Ovaj Mnemonic vam daje potpuni, neograničeni pristup svim vašim bitcoinima** Svako ko poseduje ovaj Mnemonic može ukrasti vaša sredstva, čak i bez fizičkog pristupa vašem telefonu.


Vraća pristup vašim bitcoinima u slučaju gubitka, krađe ili loma vašeg telefona. Zato je veoma važno da ga pažljivo napravite rezervnu kopiju **na fizičkom mediju (ne digitalnom)** i čuvate je na sigurnom mestu. Možete ga zapisati na parče papira, ili za dodatnu sigurnost, ako je ovo veliki Wallet, preporučujem graviranje na nosaču od nerđajućeg čelika kako biste ga zaštitili od rizika od požara, poplave ili urušavanja (za Hot Wallet dizajniran za osiguranje male količine bitcoina, jednostavna papirna kopija je verovatno dovoljna).


*Očigledno, nikada ne smete deliti ove reči na Internetu, kao što ja radim u ovom vodiču. Ovaj uzorak Wallet će biti korišćen samo na Liquid-ovom Testnet i biće obrisan na kraju vodiča.*


![LIQUID GREEN](assets/fr/17.webp)


Kada pravilno zabeležite svoju Mnemonic frazu na fizičkom mediju, kliknite na "*Nastavi*". Green Wallet će vas zatim zamoliti da potvrdite neke od reči u vašoj Mnemonic frazi kako bi se osiguralo da ste ih ispravno zabeležili. Popunite praznine nedostajućim rečima.


![LIQUID GREEN](assets/fr/18.webp)


Izaberite PIN kod svog uređaja, koji će se koristiti za otključavanje vašeg Green Wallet. Ovo je vaša zaštita protiv neovlašćenog fizičkog pristupa. Ovaj PIN kod nije uključen u izvođenje kriptografskih ključeva vašeg Wallet. Dakle, čak i bez pristupa ovom PIN kodu, posedovanje vaše Mnemonic fraze od 12 ili 24 reči omogućiće vam da ponovo dobijete pristup vašim bitcoinima.


Preporučujemo da izaberete 6-cifreni PIN kod koji je što je moguće nasumičniji. Obavezno sačuvajte ovaj kod kako ga ne biste zaboravili, inače ćete biti primorani da preuzmete svoj Wallet sa Mnemonic. Zatim možete dodati opciju biometrijske blokade kako ne biste morali unositi PIN svaki put kada ga koristite. Generalno govoreći, biometrija je daleko manje sigurna od samog PIN-a. Dakle, po defaultu, savetujem vam da ne postavljate ovu opciju otključavanja.


![LIQUID GREEN](assets/fr/19.webp)


Unesite svoj PIN drugi put da ga potvrdite.


![LIQUID GREEN](assets/fr/20.webp)


Sačekajte da vaš Wallet bude kreiran, zatim kliknite na dugme "*Create an account*".


![LIQUID GREEN](assets/fr/21.webp)


U okviru "*Active*" izaberite "*Liquid Bitcoin*". Zatim možete birati između standardnog Wallet sa jednim potpisom, koji ćemo koristiti u ovom vodiču, ili Wallet zaštićenog dvofaktorskom autentifikacijom (2FA).


![LIQUID GREEN](assets/fr/22.webp)


I to je to, vaš Liquid Wallet je kreiran korišćenjem Green aplikacije!


![LIQUID GREEN](assets/fr/23.webp)


Pre nego što primite svoje prve bitkoine na vaš Liquid Wallet, **snažno vam savetujem da izvršite test praznog oporavka**. Zabeležite neke referentne informacije, kao što su vaš xpub ili prvi prijemni Address, zatim obrišite vaš Wallet na Green aplikaciji dok je još uvek prazan. Zatim pokušajte da obnovite vaš Wallet na Green koristeći vaše papirne rezervne kopije. Proverite da li informacije o kolačićima generisane nakon obnove odgovaraju onima koje ste prvobitno zapisali. Ako odgovaraju, možete biti sigurni da su vaše papirne rezervne kopije pouzdane. Da biste saznali više o tome kako izvršiti test oporavka, molimo vas da pogledate ovaj drugi vodič:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Postavljanje vašeg Liquid Wallet


Ako želite da personalizujete svoj Wallet, kliknite na tri male tačke u gornjem desnom uglu.


![LIQUID GREEN](assets/fr/24.webp)


Opcija "*Preimenuj*" vam omogućava da prilagodite ime vašeg Wallet, što je posebno korisno ako upravljate sa nekoliko novčanika na istoj aplikaciji.


![LIQUID GREEN](assets/fr/25.webp)


Meni "*Unit*" vam omogućava da promenite osnovnu jedinicu vašeg Wallet. Na primer, možete odabrati da je prikažete u satoshijima umesto u bitcoinima.


![LIQUID GREEN](assets/fr/26.webp)


Meni "*Settings*" omogućava pristup raznim opcijama vašeg Bitcoin Wallet.


![LIQUID GREEN](assets/fr/27.webp)


Ovde ćete, na primer, pronaći svoj *opis*, koji može biti koristan ako planirate da postavite Watch-only wallet iz ovog Liquid Wallet.


![LIQUID GREEN](assets/fr/28.webp)


Takođe možete promeniti svoj Wallet PIN i aktivirati biometrijsku vezu.


![LIQUID GREEN](assets/fr/29.webp)


## Korišćenje vašeg Liquid Wallet


Sada kada je vaš Liquid Wallet postavljen, spremni ste da primite svoj prvi L-Sats!


Ako još uvek nemate L-BTC, imate nekoliko opcija. Prva je da vam neko direktno pošalje. Ako neko želi da vam plati u bitkoinima na Liquid, jednostavno im dajte prijemni Address. Druga opcija je da Exchange vaše bitkoine na lancu ili na Lightning Network za L-BTC. Da biste to uradili, možete koristiti [most kao što je Boltz](https://boltz.Exchange/). Jednostavno unesite vaš Liquid Address na sajtu, zatim izvršite uplatu ili putem Lightning Network ili na lancu.


![LIQUID GREEN](assets/fr/30.webp)


Da biste generate, Liquid i Address, kliknite na dugme "*Receive*".


![LIQUID GREEN](assets/fr/31.webp)


Green će zatim prikazati prvi prazan prijem Address u vašem Wallet. Možete ili skenirati povezani QR kod, ili direktno kopirati Address za slanje L-BTC.


![LIQUID GREEN](assets/fr/32.webp)


Kada se transakcija emituje na mreži, pojaviće se u vašem Wallet.


![LIQUID GREEN](assets/fr/33.webp)


Sačekajte dok ne dobijete dovoljno potvrda da biste transakciju smatrali konačnom. Na Liquid, potvrde bi trebalo da budu brze, jer se blok objavljuje svake minute.


![LIQUID GREEN](assets/fr/34.webp)


Sa L-Sats u vašem Liquid Wallet, sada ih možete takođe poslati. Kliknite na "*Send*".


![LIQUID GREEN](assets/fr/35.webp)


Na sledećoj stranici unesite primalacov Liquid Address. Možete ga uneti ručno ili skenirati njegov QR kod.


![LIQUID GREEN](assets/fr/36.webp)


Izaberite iznos plaćanja.


![LIQUID GREEN](assets/fr/37.webp)


Kliknite na "*Next*" da biste pristupili ekranu sažetka transakcije. Proverite da li su Address, iznos i naknade tačni.


![LIQUID GREEN](assets/fr/38.webp)


Ako sve bude u redu, pomerite dugme Green na dnu ekrana udesno da potpišete i emitujete transakciju na mreži Bitcoin.


![LIQUID GREEN](assets/fr/39.webp)


Vaša transakcija će se sada pojaviti na vašoj Bitcoin Wallet kontrolnoj tabli, čekajući potvrdu.


![LIQUID GREEN](assets/fr/40.webp)


A sada znate kako lako koristiti Liquid Sidechain sa aplikacijom Blockstream Green!


Ako ste našli ovaj vodič korisnim, bio bih zahvalan ako biste ostavili Green palac ispod. Slobodno podelite ovaj članak na svojim društvenim mrežama. Hvala vam puno!


Preporučujem vam da pogledate i ovaj drugi sveobuhvatni vodič o mobilnoj aplikaciji Blockstream Green za postavljanje onchain Bitcoin Hot Wallet :


https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143