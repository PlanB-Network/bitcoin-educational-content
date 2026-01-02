---
name: Plan nasleđivanja Bitcoin
description: Kako preneti bitkoine svojim voljenima
---

![cover](assets/cover.webp)



Prenos bitkoina predstavlja veliki tehnički izazov koji mnogi vlasnici zanemaruju. Za razliku od tradicionalnih bankarskih sredstava, gde finansijska institucija može preneti sredstva pravim vlasnicima, Bitcoin funkcioniše bez posrednika. Vaši voljeni nikada neće moći da pristupe vašim sredstvima bez neophodnih tehničkih informacija, bez obzira na njihovu pravnu legitimnost.



Ovaj vodič vas vodi kroz kreiranje tehničkog plana nasleđa. Naučićete kako funkcionišu on-chain mehanizmi za automatski prenos, kako da dokumentujete vaše konfiguracije i kako da izaberete prava rešenja kako biste osigurali da vaše Bitcoin nasleđe ostane dostupno vašim voljenima.



## Zašto je plan tehničkog nasleđa neophodan



Bitcoin se zasniva na fundamentalnom kriptografskom principu: ko god drži privatne ključeve kontroliše sredstva. Ovaj suverenitet postaje velika ranjivost kada vlasnik nestane bez prenosa potrebnih informacija.



Bitcoin plan nasledstva mora ispuniti dva naizgled kontradiktorna cilja: omogućiti vašim voljenima pristup vašim sredstvima kada za to dođe vreme, dok sprečava bilo koga drugog da im pristupi pre vremena. Ova delikatna ravnoteža oslanja se na izvorne programske mogućnosti Bitcoin.



Tehnička složenost dodaje dodatni sloj poteškoća. Vaši naslednici će morati da manipulišu konceptima kao što su fraze za oporavak, opisi portfolija ili putanje derivacije. Bez adekvatne pripreme, čak i naslednik sa dobrim namerama rizikuje da napravi nepovratne greške.



## Kako funkcioniše nasleđivanje on-chain



Bitcoin koristi svoj skriptni jezik za kodiranje uslova potrošnje direktno u transakcijama. on-chain nasledstvo koristi ovu programabilnost da kreira alternativne puteve oporavka koji se aktiviraju automatski.



### Vremenske brave



Vremenske brave su osnovni mehanizam nasleđivanja Bitcoin. Omogućavaju da sredstva budu zaključana dok se ne ispuni vremenski uslov.



**CLTV (CheckLockTimeVerify)**: Ova apsolutna vremenska zabrana proverava da li je određeno vreme (datum ili visina bloka) dostignuto pre nego što se odobri trošenje. Na primer, "ova sredstva se mogu potrošiti tek nakon bloka 900000" ili "posle 1. januara 2026". Prednost CLTV-a je što omogućava duge odgode (nekoliko godina), ali je datum fiksiran i primenjuje se identično na sve UTXO-e u portfoliju. Da biste zadržali kontrolu nad svojim sredstvima, morate periodično kreirati novi portfolio sa produženim datumom isteka i preneti svoja sredstva na njega.



**CSV (CheckSequenceVerify)**: Ova relativna vremenska brava proverava da li je prošao određeni broj blokova od kada je UTXO kreiran. Na primer, "ova sredstva se mogu potrošiti tek nakon 52560 blokova (~1 godina) od prijema". Prednost CSV-a je što svaki UTXO ima svoj nezavisni brojač. Svaki put kada izvršite transakciju, novo kreirani UTXO-i resetuju svoj vremenski limit. Međutim, tehničko ograničenje od 65535 blokova (~maksimalno 15 meseci) ograničava moguće vremenske okvire. Ovaj pristup je prirodniji za svakodnevnu upotrebu, jer vaša normalna aktivnost automatski pomera rokove.



### Višestruki putevi trošenja



Portfelj nasledstva kombinuje nekoliko putanja trošenja u svakoj adresi:





- Glavna putanja** : Vlasnik može trošiti svoja sredstva u bilo koje vreme sa svojim glavnim ključem, bez vremenskih ograničenja.
- Put oporavka**: Jedan ili više alternativnih ključeva mogu trošiti sredstva tek nakon što protekne određeno vreme.



Svaka transakcija koju izvrši vlasnik "osvežava" UTXO, stvarajući nove izlaze sa resetovanim vremenskim zaključavanjima. Ovaj mehanizam osigurava da, sve dok vlasnik ostaje aktivan, putevi oporavka nikada ne aktiviraju.



### Miniscript i Taproot



**Miniscript** je strukturirani jezik koji su razvili Andrew Poelstra, Pieter Wuille i Sanket Kanjalkar, a koji olakšava pisanje i analizu složenih Bitcoin skripti. Omogućava vam da sastavite čitljive i proverljive uslove potrošnje, što je ključno za konfiguracije nasleđivanja koje uključuju više ključeva i vremenske zaključavanja.



**Taproot** (aktiviran u novembru 2021) značajno poboljšava nasleđivanje on-chain. Zahvaljujući svojoj strukturi stabla (MAST), na blokčejnu se otkriva samo korišćeni uslov trošenja. Ako vlasnik normalno troši svoja sredstva, uslovi nasleđivanja ostaju nevidljivi. Ova poverljivost takođe smanjuje troškove transakcija za složene puteve.



## Kritična važnost deskriptora



Za nasleđene portfelje, fraza za oporavak (seed) nije dovoljna za vraćanje pristupa sredstvima. **Deskriptor** postaje ključni element.



Opisivač je string koji iscrpno opisuje strukturu portfolija: uključeni javni ključevi, uslovi trošenja, putanje derivacije i podešena vremenska zaključavanja. Evo pojednostavljenog primera:



```
wsh(or_d(pk([fingerprint/path]xpub...),and_v(v:pkh([fingerprint/path]xpub...),older(52560))))
```



Ovaj opis kaže: "ili glavni ključ može potrošiti odmah, ili ključ za oporavak može potrošiti nakon 52560 blokova".



Hajde da razložimo ovaj primer:




- `wsh()` : Witness Script Hash, označava tip adrese (P2WSH)
- or_d()`: "ili" uslov sa podrazumevanom granom
- pk([fingerprint/path]xpub...)`: Glavni javni ključ sa svojim otiskom prsta i putanjom derivacije
- and_v()`: "and" uslov kombinovanja ključa za oporavak sa vremenskom bravom
- `older(52560)`: Relativna vremenska blokada od 52560 blokova



**Bez deskriptora, čak i sa svim frazama za oporavak, vaši naslednici neće moći da obnove portfelj.** Standardni portfelj može se obnoviti samo iz seed jer prati standardizovane putanje derivacije (BIP44, BIP84). Nasleđeni portfelj, s druge strane, koristi prilagođene skripte koje se ne mogu pogoditi. Rezervna kopija deskriptora (ili konfiguracioni fajl koji je izvezla vaša softverska aplikacija) mora pratiti fraze za oporavak u vašem planu nasledstva.



## Dokumentarni delovi plana nasledstva



Iza tehničkih mehanizama, efikasan plan zaostavštine počiva na tri stuba dokumentacije.



### Pismo o nasleđu



Ovo lično pismo je ulazna tačka vašeg plana. Napisano za vaše naslednike, objašnjava kontekst i mere predostrožnosti koje treba preduzeti.



Vaše pismo mora sadržati eksplicitna pravila bezbednosti:




- Ne žurite, odvojite vreme da naučite pre nego što premestite sredstva
- Nikada ne saopštavajte kompletnu frazu za oporavak jednoj osobi
- Nikada ne unosite frazu za oporavak u neverifikovani softverski program ili računar.
- Čuvajte se prevara i ljudi koji nude netraženu pomoć.
- Potražite savet od najmanje dve osobe kojima verujete pre nego što donesete bilo kakvu odluku.



Ovo pismo takođe sadrži kontakt podatke vašeg notara i lokaciju vašeg testamenta. Nikada ne bi trebalo da sadrži fraze za oporavak ili lozinke.



### Direktorijum pouzdanih kontakata



Nijedan naslednik ne bi trebalo da se suoči sa oporavkom bitkoina sam. Ovaj direktorijum navodi ljude koji mogu pružiti tehničku ili pravnu pomoć.



Za svaki kontakt, dokumentuj: puno ime, odnos sa tobom, ulogu u planu, nivo poverenja, Bitcoin veštine, i potpune kontakt detalje. Osnovno pravilo: tvoji naslednici treba uvek da se konsultuju sa najmanje dve različite osobe pre donošenja bilo koje važne odluke.



### Bitcoin inventar imovine



Ovaj odeljak mapira sve vaše bitkoine sa tehničkim informacijama potrebnim za njihovo povraćanje.



Za svaki portfolio, dokument:




- Tip portfolija**: hardver, softver, konfiguracija (single-sig, multisig, legacy)
- Lokacija uređaja**: fizička lokacija wallet hardvera
- Descriptor/lokacija konfiguracione datoteke**: kritično za napredne portfelje
- Lokacija fraze za oporavak**: odvojeno od deskriptora
- Pristupni kodovi**: gde se PIN-ovi i lozinke čuvaju
- Konfigurisana kašnjenja**: kada se aktiviraju putanje oporavka



## Tehnička rešenja dostupna



Nekoliko softverskih paketa implementira on-chain mehanizme nasleđivanja. Svaki ima svoje tehničke karakteristike.



### Liana



Liana je desktop softver (Linux, macOS, Windows) koji koristi Miniscript za kreiranje portfolija sa vremenski određenim putanjama oporavka. Projekat razvija Wizardsardine, koji je suosnovao Antoine Poinsot (Bitcoin Core saradnik).



**Tehnička arhitektura**: Liana po defaultu kreira P2WSH portfolije (SegWit native) sa podrškom za Taproot koja je dostupna u zavisnosti od kompatibilnosti vašeg wallet hardvera. Arhitektura se zasniva na glavnoj putanji i jednoj ili više putanja za oporavak. Generisani deskriptor kodira sve uslove i mora biti sačuvan.



**Timelocks used**: Liana koristi relativne vremenske brave (CSV), ograničene na 65535 blokova (~15 meseci). Da biste zadržali kontrolu, morate izvršiti transakciju osvežavanja pre nego što vremenska brava istekne.



**Integracija hardvera wallet**: BitBox02, Blockstream Jade, Coldcard, Ledger, Specter DIY i drugi uređaji su kompatibilni za potpisivanje transakcija.



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

### Bitcoin Keeper



Bitcoin Keeper je mobilna aplikacija (iOS, Android) koja kombinuje multisig i vremenska zaključavanja putem svojih "Poboljšanih trezora". Mobilni pristup sa integrisanim uputstvima čini je dostupnom manje tehnički potkovanim korisnicima.



**Tehnička arhitektura**: Poboljšani trezori koriste Miniscript za kreiranje multisig konfiguracija gde se dodatni ključevi aktiviraju nakon definisanih kašnjenja. Nasledni ključ se dodaje postojećem kvorumu, dok hitni ključ može potpuno zaobići multisig.



**Timelocks used**: Bitcoin Keeper koristi apsolutne vremenske brave (CLTV), omogućavajući vremenske periode duže od 15 meseci. Datum aktivacije se postavlja prilikom kreiranja wallet i primenjuje se na sve UTXO-e. Aplikacija uključuje funkciju "revaulting" koja automatski upravlja osvežavanjem: korisnik jednostavno prati vođene korake, bez potrebe da ručno kreira novi wallet.



**Dodatne funkcije**: Integrisani dokumenti o nasledstvu, Canary novčanici za detekciju kompromitovanja ključeva i podsetnici za osvežavanje.



https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-7f2a160b-10b6-4cc5-8820-514ee2eb1599

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

### Nasleđe



Heritage je desktop aplikacija koja koristi Taproot skripte za kodiranje uslova nasleđivanja. Upotreba Taproot nudi poboljšanu poverljivost, jer neiskorišćene putanje ostaju nevidljive na blockchain-u.



**Tehnička arhitektura**: Svaka Heritage adresa integriše glavni put i alternativne puteve za svakog naslednika, sa progresivnim vremenskim okvirima. Hijerarhijska struktura omogućava definisanje lične rezervne kopije na 6 meseci i porodičnih naslednika na 12-15 meseci.



**Načini korišćenja**: Samostalna verzija sa sopstvenim čvorom (besplatno) ili upravljana usluga dodavanja podsetnika i obaveštenja naslednicima (0,05%/godišnje).



https://planb.academy/tutorials/wallet/desktop/heritage-0549701f-2619-4037-ad05-44982be73ef4

## Proces oporavka naslednika



Razumevanje procesa oporavka pomaže u pripremi efikasnog plana. Ovde su tehnički koraci koje naslednik treba da prati.



### Zahtevi za oporavak



Naslednik treba:


1. **Opisni ili konfiguracioni fajl** originalnog portfolija (JSON ili tekstualni format, u zavisnosti od softvera)


2. **Njegova fraza za oporavak** (ona povezana sa ključem nasleđa, obično 12 ili 24 reči)


3. **Kompatibilan softver** (Liana, Bitcoin Keeper, Heritage, ili Sparrow/Specter za standardne deskriptore)


4. **Povezivanje sa čvorom Bitcoin** radi provere statusa vremenskog zaključavanja i emitovanja transakcije



### Koraci oporavka



1. **Instalirajte softver** na sigurnom uređaju i konfigurišite vezu sa Bitcoin mrežom (lični čvor ili Electrum server)


2. **Uvezite deskriptor** da rekonstruišete strukturu portfolija. Softver će automatski generate sve korišćene adrese.


3. **Vratite ključ nasleđivanja** iz fraze za oporavak. Softver će proveriti da li ovaj ključ odgovara jednom od ključeva ovlašćenih u deskriptoru.


4. **Sinhronizujte portfelj** da biste otkrili sve UTXO-e i njihove uslove trošenja


5. **Proveri isteka vremenske brave**: softver će naznačiti za svaki UTXO da li je put oporavka aktivan


6. **Kreirajte transakciju oporavka** na adresu koju kontroliše isključivo naslednik (idealno novi pojedinačni wallet)


7. **Potpiši i emituj** transakciju na Bitcoin mreži



Ako vremenska brava još nije istekla, naslednik će morati da sačeka. Softver će prikazati datum ili blok od kojeg oporavak postaje moguć. Tokom ovog perioda čekanja, sredstva ostaju sigurna na blockchainu.



### Tačke na koje naslednik treba da obrati pažnju



Naslednik mora obratiti posebnu pažnju na :




- Proverite autentičnost preuzetog softvera** (kontrolne sume, potpisi)
- Nikada ne delite svoju frazu za oporavak** sa bilo kim ko nudi pomoć
- Posavetujte se sa najmanje dve osobe kojima verujete** pre nego što sprovedete oporavak
- Prenesi sredstva na jednostavan portfolio** koji on potpuno kontroliše nakon oporavka



## Najbolje prakse



### Razdvajanje informacija



Nikada ne čuvajte sve informacije na jednom mestu. Opisivač mora biti odvojen od fraza za oporavak, koje su zauzvrat odvojene od PIN kodova. Ova distribucija otežava pristup napadaču, dok ostaje rekonstituisana od strane vaših legitimnih naslednika.



### Testovi oporavka



Pre nego što položite značajna sredstva, testirajte ceo proces oporavka sa malim iznosom. Proverite da li možete da obnovite portfolio iz opisa i fraza za oporavak na praznom uređaju. Dokumentujte korake za vaše naslednike.



### Održavanje vremenske brave



Planirajte osvežavanje vaših vremenskih zaključavanja pre nego što isteknu. Za vremensko zaključavanje od 12 meseci, obavite transakciju svakih 9-10 meseci. Softver obično nudi podsetnike ili funkcije automatskog osvežavanja.



### Ažuriranje plana



Vaša Bitcoin konfiguracija se razvija. Svaka značajna promena (novi portfolio, modifikacija rokova, dodavanje naslednika) mora biti odražena u vašoj dokumentaciji. Uspostavite godišnju rutinu pregleda.



## Biranje vašeg pristupa



Izbor između različitih rešenja zavisi od vašeg tehničkog profila i vaših specifičnih potreba.



**Liana** je pogodan za korisnike desktop računara koji preferiraju open source softver sa potpunom kontrolom putem sopstvenog čvora. Konfiguracija ostaje pristupačna zahvaljujući vođenom interfejsu. Relativni vremenski zaključavanja (CSV) pojednostavljuju održavanje, jer vaša normalna aktivnost automatski pomera rokove. Ograničenje: maksimalno kašnjenje od približno 15 meseci (65535 blokova).



**Bitcoin Keeper** cilja na mobilne korisnike koji traže intuitivan interfejs sa integrisanim pratećim dokumentima. Aplikacija nudi dve vrste specijalnih ključeva: Nasledni ključ (koji dodaje kvorum) i Hitni ključ (koji ga potpuno zaobilazi). Apsolutne vremenske brave (CLTV) omogućavaju rokove duže od 15 meseci, sa integrisanom funkcijom ponovnog zaključavanja koja pojednostavljuje osvežavanje. Plan Dijamantske ruke otključava napredne funkcije zaostavštine.



**Inheritance** je namenjen tehničkim korisnicima koji cene Taproot poverljivost i hijerarhijsko nasleđivanje sa progresivnim kašnjenjima. Struktura stabla Taproot skriva uslove nasleđivanja tokom normalnih transakcija, otkrivajući samo uslov korišćen tokom oporavka.



Sve tri solucije imaju jednu zajedničku stvar: zahtevaju periodično osvežavanje kako bi se sprečila preuranjena aktivacija puteva oporavka. Ovo ograničenje je i cena i garancija on-chain-ovog nepouzdanog nasleđa. Rasporedite redovne podsetnike i učinite ovo održavanje delom vaše Bitcoin rutine upravljanja.



## Zaključak



Tehnički Bitcoin nasleđeni plan kombinuje kriptografske mehanizme (vremenske brave, Miniscript, Taproot) sa rigoroznom dokumentacijom. Napredni novčanici omogućavaju vam da automatski prenesete svoje bitkoine nakon perioda neaktivnosti, bez intervencije treće strane.



Kritični elementi koje treba preneti svojim naslednicima su: deskriptor ili konfiguracioni fajl, njihova fraza za oporavak, detaljna uputstva za oporavak i kontakt podaci kompetentnih osoba koje im mogu pomoći.



Počnite tako što ćete izabrati tehničko rešenje koje odgovara vašem profilu, testirajte ga sa malom količinom, a zatim dokumentujte sve u strukturisanom planu. Početna složenost garantuje da će vaša Bitcoin imovina biti preneta sa punim poverenjem.



## Resursi



### Šablon plana nasledstva





- [Bitcoin Inheritance Plan Template (PDF)](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/resources/bet/seed-management-tools/assets/Bitcoin-Inheritance-Plan-Template.pdf) - Plan ₿ Network Dokumentacioni Šablon



### Tehničke reference





- [BIP-65 : OP_CHECKLOCKTIMEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki) - Specifikacija apsolutnih vremenskih zaključavanja (CLTV)
- [BIP-112 : OP_CHECKSEQUENCEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki) - Specifikacija relativnih vremenskih zaključavanja (CSV)
- [Miniscript Reference](https://bitcoin.sipa.be/miniscript/) - Zvanična Miniscript dokumentacija autora Pieter Wuille



### Zvanične veb stranice za rešenja





- [Liana Wallet](https://wizardsardine.com/liana/) - Wizardsardine
- [Bitcoin Keeper](https://bitcoinkeeper.app/) - Bithyve
- [Heritage Wallet](https://btc-heritage.com/) - Crypto7