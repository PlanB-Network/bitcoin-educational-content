---
name: Aqua
description: Bitcoin, Lightning i Liquid u jednom Wallet
---
![cover](assets/cover.webp)


Aqua je mobilna aplikacija koja olakšava kreiranje Hot Wallet za Bitcoin i Liquid, a takođe nudi mogućnost korišćenja Lightning-a bez složenosti upravljanja čvorom, zahvaljujući integrisanim zamjenama. Takođe omogućava upravljanje USDT stabilnim koinima na različitim mrežama.


Razvijena od strane kompanije JAN3 pod rukovodstvom Samsona Mow-a, aplikacija Aqua je prvobitno dizajnirana specifično za potrebe korisnika u Latinskoj Americi, iako je pogodna za bilo kog korisnika širom sveta. Posebno je interesantna za početnike i one koji svakodnevno koriste Bitcoin za svoja plaćanja.


U ovom vodiču ćemo saznati kako koristiti mnoge funkcije Aqua. Ali pre nego što to uradimo, hajde da odvojimo trenutak da razumemo šta je Sidechain na Bitcoin i kako Liquid funkcioniše, kako bismo u potpunosti shvatili vrednost Aqua.


![AQUA](assets/fr/01.webp)


## Šta je Sidechain?


Bitcoin protokol ima namerne tehničke ograničenja koja pomažu u održavanju decentralizacije mreže i osiguravaju da je bezbednost raspodeljena među svim korisnicima. Međutim, ova ograničenja ponekad mogu frustrirati korisnike, posebno tokom zagušenja zbog velikog broja istovremenih transakcija. Debata o skalabilnosti Bitcoin dugo je delila zajednicu, posebno tokom Rata o veličini bloka. Od ove epizode, unutar Bitcoin zajednice je široko prepoznato da skalabilnost mora biti osigurana rešenjima off-chain, na drugim Layer sistemima. Ova rešenja uključuju bočne lance, koji su i dalje relativno nepoznati i malo korišćeni u poređenju sa drugim sistemima kao što je Lightning Network.


Sidechain je nezavisni Blockchain koji radi paralelno sa glavnim Bitcoin Blockchain. Koristi Bitcoin kao obračunsku jedinicu, zahvaljujući mehanizmu zvanom "*two-way peg*". Ovaj sistem omogućava zaključavanje bitcoina na glavnom lancu kako bi se njihova vrednost reprodukovala na Sidechain, gde cirkulišu u obliku tokena podržanih originalnim bitcoinima. Ovi tokeni obično zadržavaju paritet vrednosti sa bitcoinima zaključanim na glavnom lancu, a proces se može obrnuti kako bi se sredstva povratila na Bitcoin.


Cilj sajdčejnova je da ponude dodatne funkcionalnosti ili tehnička poboljšanja, kao što su brže transakcije, niže naknade ili podrška za pametne ugovore. Ove inovacije ne mogu uvek biti direktno implementirane na Bitcoin Blockchain bez ugrožavanja njegove decentralizacije ili sigurnosti. Sajdčejnovi stoga omogućavaju testiranje i istraživanje novih rešenja uz očuvanje integriteta Bitcoin. Međutim, ovi protokoli često zahtevaju kompromise, posebno u smislu decentralizacije i sigurnosti, u zavisnosti od izabranog modela upravljanja i mehanizma konsenzusa.


## Šta je Liquid?


Liquid je federativni Sidechain overlay za Bitcoin, razvijen od strane Blockstream-a kako bi poboljšao brzinu transakcija, poverljivost i funkcionalnost. Koristi bilateralni mehanizam sidrenja uspostavljen na federaciji za zaključavanje bitcoina na glavnom lancu i kreiranje Liquid-bitcoina (L-BTC) zauzvrat, tokena koji cirkulišu na Liquid dok ostaju podržani originalnim bitcoinima.


![AQUA](assets/fr/02.webp)


Liquid Network se oslanja na federaciju učesnika, koju čine priznati entiteti iz ekosistema Bitcoin, koji validiraju blokove i upravljaju bilateralnim povezivanjem. Pored L-BTC, Liquid takođe omogućava izdavanje drugih digitalnih sredstava, kao što su USDT stablecoin i druge kriptovalute.


![AQUA](assets/fr/03.webp)


## Instalirajte aplikaciju Aqua


Prvi korak je, naravno, preuzimanje aplikacije Aqua. Idite u svoju prodavnicu aplikacija:



- [Za Android](https://play.google.com/store/apps/details?id=io.aquawallet.android);
- [Za Apple](https://apps.apple.com/us/app/Aqua-Wallet/id6468594241).

![AQUA](assets/fr/04.webp)


Za korisnike Androida, takođe imate opciju instaliranja aplikacije putem `.apk` fajla [dostupnog na njihovom GitHub-u](https://github.com/AquaWallet/Aqua-Wallet/releases).


![AQUA](assets/fr/05.webp)


Pokrenite aplikaciju, a zatim označite polje "*Pročitao/la sam i slažem se sa Uslovima korišćenja i Politikom privatnosti*".


![AQUA](assets/fr/06.webp)


## Kreiraj svoj Wallet na Aqua


Kliknite na dugme "*Create Wallet*".


![AQUA](assets/fr/07.webp)


I eto voilà, vaš Wallet je već kreiran!


![AQUA](assets/fr/08.webp)


Ali pre svega, pošto je ovo samostalno čuvanje Wallet, neophodno je napraviti fizičku rezervnu kopiju vašeg Mnemonic. **Ovaj Mnemonic vam daje potpuni, neograničeni pristup svim vašim bitcoinima**. Svako ko poseduje ovaj Mnemonic može ukrasti vaša sredstva, čak i bez fizičkog pristupa vašem telefonu.


Omogućava vam da povratite pristup vašim bitcoinima u slučaju gubitka, krađe ili oštećenja vašeg telefona. Stoga je veoma važno da ga pažljivo sačuvate na fizičkom mediju (ne digitalnom) i da ga skladištite na sigurnom mestu. Možete ga zapisati na parče papira, ili za dodatnu sigurnost, ako je u pitanju veliki Wallet, preporučujem da ga ugravirate na nosač od nerđajućeg čelika kako biste ga zaštitili od rizika od požara, poplave ili urušavanja (za Hot Wallet dizajniran da osigura malu količinu bitcoina, jednostavna papirna kopija je verovatno dovoljna).


Da biste to uradili, kliknite na meni Settings.


![AQUA](assets/fr/09.webp)


Zatim kliknite na "*View seed Phrase*". Napravite fizičku rezervnu kopiju ove fraze od 12 reči.


![AQUA](assets/fr/10.webp)


U istom meniju postavki, možete takođe promeniti jezik aplikacije i fiat valutu koja se koristi.


![AQUA](assets/fr/11.webp)


Pre nego što primite svoje prve bitkoine u vaš Wallet, **snažno vam savetujem da izvršite test praznog oporavka**. Zabeležite neke referentne informacije, kao što su vaš xpub ili prvo primanje Address, zatim obrišite vaš Wallet na Aqua aplikaciji dok je još uvek prazan. Zatim pokušajte da obnovite vaš Wallet na Aqua koristeći vaše papirne rezervne kopije. Proverite da li informacije o kolačićima generisane nakon obnove odgovaraju onima koje ste prvobitno zapisali. Ako odgovaraju, možete biti sigurni da su vaše papirne rezervne kopije pouzdane. Da biste saznali više o tome kako izvršiti test oporavka, molimo vas da pogledate ovaj drugi vodič:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

Ne možete to videti na mom ekranu jer koristim emulator, ali u podešavanjima ćete pronaći opciju za zaključavanje aplikacije pomoću biometrijskog sistema autentifikacije. Toplo preporučujem da omogućite ovu sigurnosnu funkciju jer, bez nje, bilo ko ko ima pristup vašem otključanom telefonu mogao bi da ukrade vaše bitkoine. Možete koristiti Face ID na iOS-u ili otisak prsta na Androidu. Ako ove metode zakažu tokom autentifikacije, i dalje možete pristupiti aplikaciji koristeći PIN kod vašeg telefona.


## Primite bitkoine na Aqua


Sada kada je vaš Wallet postavljen, spremni ste da primite svoj prvi Sats! Jednostavno kliknite na dugme "*Receive*" u meniju "*Wallet*".


![AQUA](assets/fr/12.webp)


Možete izabrati da primate bitkoine onchain, na Liquid, ili putem Lightning-a.


![AQUA](assets/fr/13.webp)


Za transakcije na lancu, Aqua će generate određeni prijemni Address gde možete primiti svoj Sats.


![AQUA](assets/fr/14.webp)


Slično, izborom Liquid, Aqua će vam pružiti Liquid Address.


![AQUA](assets/fr/15.webp)


Ako više volite da primate sredstva putem Lightning-a, prvo ćete morati da navedete željeni iznos.


![AQUA](assets/fr/16.webp)


Zatim kliknite na "*generate Invoice*".


![AQUA](assets/fr/17.webp)


Aqua će kreirati Invoice za primanje sredstava sa Lightning Wallet. Imajte na umu da će, za razliku od onchain i Liquid opcija, sredstva primljena putem Lightning-a biti automatski konvertovana u L-BTC na Liquid koristeći Boltz alat, pošto Aqua nije Lightning čvor. Ovaj proces vam omogućava da primate i šaljete sredstva putem Lightning-a, ali bez ikakvog skladištenja vaših bitcoina na Lightning-u.


![AQUA](assets/fr/18.webp)


Lično, počeću slanjem bitcoina putem Lightning-a na Aqua. Kada transakcija bude završena sa datim Invoice, dobijamo potvrdu.


![AQUA](assets/fr/19.webp)


Da biste pratili napredak zamene, vratite se na početnu stranicu vašeg Wallet i kliknite na nalog "*L2 Bitcoin*", koji prikazuje Lightning (putem zamene) i Liquid transakcije.


![AQUA](assets/fr/20.webp)


Ovde možete videti svoju transakciju i stanje vašeg L-BTC.


![AQUA](assets/fr/21.webp)


## Bitcoin zameni sa Aqua


Sada kada imate sredstva u vašem Aqua Wallet, možete ih direktno zameniti iz aplikacije, bilo da ih prenesete na glavni Bitcoin Blockchain, ili na Liquid. Takođe možete konvertovati vaše bitkoine u USDT stablecoin (ili druge). Da biste to uradili, idite na meni "*Marketplace*".


![AQUA](assets/fr/22.webp)


Kliknite na "*Swaps*".


![AQUA](assets/fr/23.webp)


U polju "*Transfer from*" izaberite sredstvo koje želite da trgujete. Trenutno posedujem samo L-BTC, tako da to biram.


![AQUA](assets/fr/24.webp)


U polju "*Transfer to*" izaberite ciljnu imovinu za vašu zamenu. Što se mene tiče, odlučio sam se za USDT na Liquid Network.


![AQUA](assets/fr/25.webp)


Unesite iznos koji želite da konvertujete.


![AQUA](assets/fr/26.webp)


Potvrdite klikom na "*Continue*".


![AQUA](assets/fr/27.webp)


Proverite da ste zadovoljni postavkama zamene, a zatim potvrdite prevlačenjem dugmeta "*Swap*" na dnu ekrana.


![AQUA](assets/fr/28.webp)


Vaša zamena je sada potvrđena.


![AQUA](assets/fr/29.webp)


Gledajući unazad na naš Wallet, možemo videti da sada imamo USDT na Liquid.


![AQUA](assets/fr/30.webp)


## Pošalji bitkoine sa Aqua


Sada kada imate bitkoine u vašem Aqua Wallet, možete ih poslati. Kliknite na dugme "*Send*".


![AQUA](assets/fr/31.webp)


Izaberite sredstvo koje želite poslati ili odaberite mrežu za obavljanje transakcije. Što se mene tiče, poslaću bitkoine putem Lightning-a.


![AQUA](assets/fr/32.webp)


Dalje, unesite informacije potrebne za slanje uplate: za onchain ili Liquid bitkoine, trebaće da unesete primajući Address; za Lightning, potreban je Invoice. Možete zalepiti ove informacije direktno u predviđeno polje ili koristiti ikonu QR koda da otvorite kameru i skenirate Address ili Invoice. Zatim kliknite na "*Continue*".


![AQUA](assets/fr/33.webp)


Kliknite "*Nastavi*" ponovo ako sve informacije izgledaju tačno.


![AQUA](assets/fr/34.webp)


Aqua vam zatim prikazuje rezime transakcije. Proverite da li su sve informacije tačne, uključujući odredište Address, troškove i iznos. Da biste potvrdili transakciju, prevucite dugme "*Slide to send*" na dnu ekrana.


![AQUA](assets/fr/35.webp)


Dobićete zatim potvrdu o isporuci.


![AQUA](assets/fr/36.webp)


Sada znate kako da koristite Aqua aplikaciju za primanje i trošenje sredstava na Bitcoin, Lightning i Liquid, sve sa jednog Interface.


Ako ste našli ovaj vodič korisnim, bio bih zahvalan ako biste ostavili Green palac ispod. Slobodno podelite ovaj članak na svojim društvenim mrežama. Hvala vam puno!


Takođe vam preporučujem da pogledate ovaj drugi sveobuhvatni vodič o mobilnoj aplikaciji Blockstream Green, koja je još jedno zanimljivo rešenje za postavljanje vašeg Liquid Wallet :


https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a
