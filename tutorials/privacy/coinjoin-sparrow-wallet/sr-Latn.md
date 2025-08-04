---
name: CoinJoin - Sparrow novčanik
description: Kako izvršiti CoinJoin na Sparrow novčaniku?
---
![cover](assets/cover.webp)


***UPOZORENJE:** Nakon hapšenja osnivača Samourai novčanika i zaplene njihovih servera 24. aprila, alat Whirlpool više ne funkcioniše, čak ni za pojedince koji imaju svoj Dojo ili koriste Sparrow novčanik. Ipak, moguće je da bi ovaj alat mogao biti ponovo uspostavljen u narednim nedeljama ili pokrenut na drugačiji način. Štaviše, teorijski deo ovog članka ostaje relevantan za razumevanje principa i ciljeva coinjoin-a uopšte (ne samo Whirlpool-a), kao i za razumevanje efikasnosti Whirlpool modela.*


_Pažljivo pratimo razvoj ovog slučaja, kao i razvoj povezanih alata. Budite sigurni da ćemo ažurirati ovaj vodič čim nove informacije budu dostupne._


_Ovaj vodič je pružen isključivo u obrazovne i informativne svrhe. Ne podržavamo niti ohrabrujemo upotrebu ovih alata u kriminalne svrhe. Odgovornost je svakog korisnika da se pridržava zakona u svojoj jurisdikciji._


---

U ovom vodiču ćete naučiti šta je CoinJoin i kako ga izvesti koristeći Sparrow softverski novčanik i Whirlpool implementaciju.


## Šta je CoinJoin na Bitcoin-u?

**CoinJoin je tehnika koja prekida mogućnost praćenja bitkoina na Blockchain-u**. Oslanja se na kolaborativnu transakciju sa specifičnom strukturom istog imena: CoinJoin transakcija.


Coinjoins poboljšavaju privatnost Bitcoin korisnika komplikovanjem analize lanca za spoljne posmatrače. Njihova struktura omogućava spajanje više novčića od različitih korisnika u jednu transakciju, čime se zamagljuju tragovi i otežava određivanje veza između ulaznih i izlaznih adresa.


Princip CoinJoin-a zasniva se na kolaborativnom pristupu: nekoliko korisnika koji žele da mešaju svoje bitkoine deponuju identične iznose kao ulaze iste transakcije. Ti iznosi se zatim redistribuiraju kao izlazi jednake vrednosti svakom korisniku. Na kraju transakcije, postaje nemoguće povezati određeni izlaz sa poznatim korisnikom na ulazu. Ne postoji direktna veza između ulaza i izlaza, što prekida asocijaciju između korisnika i njihovog UTXO-a, kao i istoriju svake kovanice.

![coinjoin](assets/notext/1.webp)


Primer CoinJoin transakcije (nije od mene): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://Mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)


Da bi se izveo CoinJoin uz osiguranje da svaki korisnik zadrži kontrolu nad svojim sredstvima u svakom trenutku, proces počinje konstrukcijom transakcije od strane koordinatora, koji je zatim prenosi svakom učesniku. Svaki korisnik zatim potpisuje transakciju nakon što proveri da li mu odgovara. Svi prikupljeni potpisi se konačno integrišu u transakciju. Ako korisnik ili koordinator pokuša da preusmeri sredstva, kroz modifikaciju izlaza CoinJoin transakcije, potpisi će biti nevažeći, što će dovesti do odbijanja transakcije od strane čvorova.


Postoji nekoliko CoinJoin implementacija, kao što su Whirlpool, JoinMarket, ili Wabisabi, od kojih svaka ima za cilj upravljanje koordinacijom među učesnicima i povećanje efikasnosti CoinJoin transakcija.


U ovom vodiču fokusiramo se na **Whirlpool** implementaciju, koju smatram najučinkovitijim rešenjem za izvođenje coinjoin-a na Bitcoin-u. Iako je dostupna na nekoliko novčanika, ovaj vodič isključivo istražuje njenu upotrebu sa Sparrow desktop softverskim novčanikom.

## Zašto izvoditi CoinJoin na Bitcoin-u?


Jedan od početnih problema sa bilo kojim peer-to-peer sistemom plaćanja je dvostruko trošenje: kako sprečiti zlonamerne pojedince da više puta troše iste monetarne jedinice bez pribegavanja centralnom autoritetu za arbitražu?


Satoshi Nakamoto je pružio rešenje za ovu dilemu kroz Bitcoin protokol, peer-to-peer elektronski platni sistem koji funkcioniše nezavisno od bilo koje centralne vlasti. U svom white paper-u, on naglašava da je jedini način da se potvrdi odsustvo dvostrukog trošenja osiguravanje vidljivosti svih transakcija unutar platnog sistema.


Da bi se osiguralo da je svaki učesnik svestan transakcija, one moraju biti javno objavljene. Tako se rad Bitcoin-a oslanja na transparentnu i distribuiranu infrastrukturu, omogućavajući bilo kojem operateru čvora da verifikuje celokupne lance elektronskih potpisa i istoriju svake kovanice, od njenog stvaranja od strane rudara.


Transparentna i distribuirana priroda Bitcoin-ovog Blockchain znači da svaki korisnik mreže može pratiti i analizirati transakcije svih drugih učesnika. Kao posledica toga, anonimnost na nivou transakcija je nemoguća. Međutim, anonimnost je očuvana na nivou individualne identifikacije. Za razliku od tradicionalnog bankarskog sistema gde je svaki račun povezan sa ličnim identitetom, na Bitcoin-u, sredstva su povezana sa parovima kriptografskih ključeva, čime se korisnicima nudi oblik pseudoanonimnosti iza kriptografskih identifikatora.


Stoga je poverljivost na Bitcoin-u ugrožena kada spoljni posmatrači uspeju da povežu specifične UTXO-e sa identifikovanim korisnicima. Kada se ova veza uspostavi, postaje moguće pratiti njihove transakcije i analizirati istoriju njihovih bitkoina. CoinJoin je upravo tehnika razvijena da prekine sledljivost UTXO-a, čime se nudi određeni nivo poverljivosti korisnicima Bitcoin-a na nivou transakcija.


## Kako funkcioniše Whirlpool?


Whirlpool se izdvaja od drugih CoinJoin metoda korišćenjem "_ZeroLink_" transakcija, koje osiguravaju da ne postoji tehnička veza između svih ulaza i svih izlaza. Ovo savršeno mešanje se postiže kroz strukturu gde svaki učesnik doprinosi identičnim iznosom u ulazu (osim za rudarske naknade), čime se generišu izlazi savršeno jednakih iznosa.


Ovaj restriktivni pristup ulazima daje Whirlpool CoinJoin transakcijama jedinstvenu karakteristiku: potpuni izostanak determinističkih veza između ulaza i izlaza. Drugim rečima, svaki izlaz ima jednaku verovatnoću da bude pripisan bilo kojem učesniku, u poređenju sa svim ostalim izlazima transakcije.

U početku, broj učesnika u svakom Whirlpool CoinJoin-u bio je ograničen na 5, sa 2 nova učesnika i 3 remiksera (ove pojmove ćemo objasniti kasnije). Međutim, porast [on-chain](https://planb.network/resources/glossary/onchain) transakcijskih naknada primećen 2023. godine naveo je Samourai timove da preispitaju svoj model kako bi poboljšali privatnost uz smanjenje troškova. Tako, uzimajući u obzir tržišnu situaciju naknada i broj učesnika, koordinator sada može organizovati coinjoin-ove uključujući 6, 7 ili 8 učesnika. Ove unapređene sesije nazivaju se "_Surge Cycles_". Važno je napomenuti da, bez obzira na postavku, uvek postoje samo 2 nova učesnika u Whirlpool coinjoin-ovima.


Stoga su Whirlpool transakcije karakterisane identičnim brojem ulaza i izlaza, koji mogu biti:


- 5 ulaza i 5 izlaza;

![coinjoin](assets/notext/2.webp)


- 6 ulaza i 6 izlaza;

![coinjoin](assets/notext/3.webp)


- 7 ulaza i 7 izlaza;

![coinjoin](assets/notext/4.webp)


- 8 ulaza i 8 izlaza.

![coinjoin](assets/notext/5.webp)

Model koji predlaže Whirlpool je stoga zasnovan na malim CoinJoin transakcijama. Za razliku od Wasabi i JoinMarket-a, gde robusnost anonsetova zavisi od broja učesnika u jednom ciklusu, Whirlpool se oslanja na povezivanje nekoliko ciklusa male veličine.


U ovom modelu, korisnik snosi troškove samo prilikom svog prvog ulaska u bazen, što mu omogućava da učestvuje u mnoštvu remiksa bez dodatnih troškova. Novi učesnici su ti koji snose rudarske troškove za remiksere.


Sa svakim dodatnim CoinJoin-om u kojem novčić učestvuje, zajedno sa svojim prethodno susretnutim vršnjacima, anonsetovi će eksponencijalno rasti. Cilj je stoga iskoristiti ove besplatne remikse koji, sa svakim pojavljivanjem, doprinose jačanju gustine anonsetova povezanih sa svakim mešanim novčićem.


Whirlpool je dizajniran uzimajući u obzir dva važna zahteva:


- Pristupačnost implementacije na mobilnim uređajima, s obzirom na to da je Samourai novčanik prvenstveno aplikacija za pametne telefone;
- Brzina ciklusa remiksovanja za promovisanje značajnog povećanja anonseta.


Ove imperative su vodile izbore programera Samourai novčanika u dizajnu Whirlpool-a, navodeći ih da ograniče broj učesnika po ciklusu. Premalo učesnika bi ugrozilo efikasnost CoinJoin-a, drastično smanjujući broj anonsetova generisanih u svakom ciklusu, dok bi previše učesnika izazvalo probleme u upravljanju na mobilnim aplikacijama i ometalo tok ciklusa.


**Na kraju, nema potrebe imati veliki broj učesnika po CoinJoin-u na Whirlpool-u jer se anonsetovi prave tokom akumulacije nekoliko CoinJoin ciklusa.**

[-> Saznajte više o Whirlpool anonsetima.](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

### CoinJoin bazeni i naknade

Da bi se osiguralo da višestruki ciklusi efikasno povećaju anonsetove mešanih novčića, mora se uspostaviti određeni okvir za ograničavanje količina korišćenih UTXO-a. Whirlpool definiše različite bazene u tu svrhu.


Bazen predstavlja grupu korisnika koji žele da mešaju svoje UTXO-e zajedno, koji se slažu oko količine UTXO-a koje će koristiti da optimizuju CoinJoin proces. Svaki bazen određuje fiksnu količinu za UTXO, kojoj korisnik mora da se pridržava da bi učestvovao. Dakle, da biste izvršili coinjoins sa Whirlpool-om, potrebno je da izaberete bazen. Trenutno dostupni bazeni su sledeći:


- 0.5 bitcoina;
- 0.05 bitcoina;
- 0.01 bitcoina;
- 0.001 bitcoina (= 100,000 Sats).


Uključivanjem svojih bitkoina u pool, oni će biti podeljeni kako bi se generisali UTXO-i koji su potpuno homogeni sa onima drugih učesnika u pool-u. Svaki bazen ima maksimalno ograničenje; stoga, za iznose koji prelaze ovo ograničenje, bićete primorani ili da napravite dva odvojena unosa unutar istog bazena ili da pređete u drugi bazen sa većim iznosom:


| Bazen (bitcoin)| Maksimalan iznos po ulazu (bitcoin)|
|----------------|------------------------------------|
| 0.5            | 35                                 |
| 0.05           | 3.5                                |
| 0.01           | 0.7                                |
| 0.001          | 0.025                              |

Kao što je ranije pomenuto, UTXO se smatra da pripada pool-u kada je spreman za integraciju u CoinJoin. Međutim, to ne znači da korisnik gubi vlasništvo nad njim. **Kroz različite cikluse mešanja, zadržavate punu kontrolu nad vašim ključevima i, samim tim, vašim bitcoinima.** Ovo je ono što razlikuje tehniku CoinJoin od drugih centralizovanih tehnika mešanja.


Da biste ušli u CoinJoin bazen, moraju se platiti naknade za uslugu kao i rudarske naknade. Naknade za uslugu su fiksne za svaki bazen i namenjene su da kompenzuju timove odgovorne za razvoj i održavanje Whirlpool-a. Za korisnike Sparrow novčanika, ove naknade prenose timovi Samourai na programere Sparrow-a.


Naknade za korišćenje Whirlpool-a plaćaju se jednokratno prilikom ulaska u bazen. Kada je ovaj korak završen, imate priliku da učestvujete u neograničenom broju remiksa bez dodatnih naknada. Ovde su trenutne fiksne naknade za svaki bazen:


| Bazen (bitcoin)| Ulazne naknade (bitcoin)  |
|----------------|---------------------------|
| 0.5            | 0.0175                    |
| 0.05           | 0.00175                   |
| 0.01           | 0.0005 (50,000 sats)      |
| 0.001          | 0.00005 (5,000 sats)      |


Ove naknade su u suštini ulaznica za odabrani bazen, bez obzira na iznos koji uložite u CoinJoin. Dakle, bilo da se pridružite bazenu 0.01 sa tačno 0.01 BTC ili uđete sa 0.5 BTC, naknade će ostati iste u apsolutnoj vrednosti.


Pre nego što nastavi sa coinjoin-ovima, korisnik stoga ima izbor između 2 strategije:


- Odlučite se za manji bazen kako biste minimizirali naknade za uslugu, znajući da će zauzvrat dobiti nekoliko malih UTXO-a;
- Ili preferirate veći bazen, pristajući da platite veće naknade kako biste završili sa smanjenim brojem UTXO-a veće vrednosti.


Opšte se savetuje da se ne spajaju različito mešani UTXO-ovi nakon CoinJoin ciklusa, jer to može ugroziti stečenu poverljivost, posebno zbog Common-Input-Ownership Heuristike (CIOH). Stoga bi moglo biti mudro odabrati veći bazen, čak i ako to znači plaćanje više, kako bi se izbeglo previše izlaza sa malim vrednostima UTXO-a. Korisnik mora odmeriti ove kompromise kako bi izabrao bazen koji mu odgovara.


Pored naknada za uslugu, moraće se uzeti u obzir i rudarske naknade svojstvene svakoj Bitcoin transakciji. Kao Whirlpool korisnik, bićete obavezni da platite rudarske naknade za pripremnu transakciju (`Tx0`) kao i za prvi CoinJoin. Svi naredni remiksi će biti besplatni, zahvaljujući Whirlpool modelu koji se oslanja na plaćanje novih učesnika.


Zaista, u svakom Whirlpool CoinJoin-u, dva korisnika među unosima su novi učesnici. Ostali unosi dolaze od remiksera. Kao rezultat toga, rudarske naknade za sve učesnike u transakciji pokrivaju ova dva nova učesnika, koji će zatim takođe imati koristi od besplatnih remiksa:

![coinjoin](assets/en/6.webp)

Zahvaljujući ovom sistemu naknada, Whirlpool se zaista razlikuje od drugih CoinJoin usluga jer anonseti UTXO-a nisu proporcionalni ceni koju plaća korisnik. Tako je moguće postići znatno visoke nivoe anonimnosti plaćanjem samo ulaznih naknada bazena i rudarskih naknada za dve transakcije (`Tx0` i početni miks).


Važno je napomenuti da će korisnik takođe morati da pokrije rudarske naknade za povlačenje svojih UTXO-a iz bazena nakon završetka njihovih višestrukih coinjoin-a, osim ako nisu odabrali opciju `mix to`, o čemu ćemo diskutovati u tutorijalu ispod.


### Nalozi unutar HD novčanika koje koristi Whirlpool

Da bi se izvršio CoinJoin putem Whirlpool-a, novčanik mora generisati nekoliko različitih naloga. Nalog, u kontekstu HD (Hijerarhijski Deterministički) novčanika, predstavlja deo koji je potpuno izolovan od ostalih, pri čemu se ova separacija dešava na trećem nivou dubine hijerarhije novčanika, odnosno na nivou `xpub`.

HD novčanik može teoretski izvesti do `2^(32/2)` različitih naloga. Početni nalog, koji se podrazumevano koristi na svim Bitcoin novčanicima, odgovara indeksu `0'`.


Za novčanike prilagođene Whirlpool-u, kao što su Samourai ili Sparrow, koriste se 4 naloga kako bi se zadovoljile potrebe CoinJoin procesa:


- Račun **depozita**, identifikovan indeksom `0'`;
- Račun **Bad bank ili loša banka** (or doxxic kusur), identifikovan indeksom `2 147 483 644'`;
- Nalog **premix**, identifikovan indeksom `2 147 483 645'`;
- Nalog **postmix**, identifikovan indeksom `2 147 483 646'`.


Svaki od ovih naloga ispunjava specifičnu funkciju unutar CoinJoin-a.


Svi ovi nalozi su povezani sa jednim seed-om, što omogućava korisniku da povrati pristup svim svojim bitcoinima koristeći svoju frazu za oporavak i, ako je primenljivo, svoj passphrase. Međutim, potrebno je navesti softveru, tokom ove operacije oporavka, različite indekse naloga koji su korišćeni.


Hajde sada da pogledamo različite faze Whirlpool CoinJoin-a unutar ovih naloga.


### Različite faze coinjoin-a na Whirlpool-u

**Faza 1: Tx0**

Početna tačka svakog Whirlpool CoinJoin-a je **depozitni** račun. Ovaj račun je onaj koji automatski koristite kada kreirate novi Bitcoin nočanik. Ovaj račun mora biti kreditiran bitcoinima koje želite da mešate.


`Tx0` predstavlja prvu fazu Whirlpool procesa mešanja. Cilj je pripremiti i izjednačiti UTXO-e za CoinJoin, tako što će ih podeliti u jedinice koje odgovaraju iznosu odabranog bazena, kako bi se osigurala homogenost mešanja. Izjednačeni UTXO-i se zatim šalju na **premix** nalog. Što se tiče razlike koja ne može ući u bazen, ona se odvaja u poseban nalog: **bad bank** (ili "doxxic kusur").


Ova početna transakcija Tx0 takođe služi za plaćanje servisnih naknada koje se duguju koordinatoru mešanja.  Za razliku od sledećih faza, ova transakcija nije kolaborativna; korisnik stoga mora preuzeti sve rudarske naknade:

![coinjoin](assets/en/7.webp)

U ovom primeru transakcije `Tx0`, ulaz od `372,000 Sats` sa našeg **depozitnog** računa je podeljen na nekoliko izlaznih UTXO-a, koji su raspoređeni na sledeći način:


- Iznos od `5,000 Sats` namenjen koordinatoru za usluge, koji odgovara ulasku u bazen od `100,000 Sats`;
- Tri UTXO-a pripremljena za mešanje, preusmerena na naš **premix** nalog i registrovana kod koordinatora. Ovi UTXO-i su izjednačeni na `108,000 Sats` svaki, kako bi pokrili rudarske naknade za njihovo buduće početno mešanje;
- Višak, koji ne može ući u bazen jer je premali, smatra se toksičnim kusurom. On se šalje na svoj specifičan račun. Ovde, ova promena iznosi `40,000 Sats`;
- Konačno, postoji `3,000 Sats` koji ne predstavljaju izlaz, već su rudarske naknade neophodne za potvrdu `Tx0`.


Na primer, ovde je pravi Tx0 Whirlpool (koji ne dolazi od mene): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://Mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)


**Korak 2: Toksičan kusur**

Višak, koji nije mogao biti integrisan u bazen, ovde ekvivalentan `40,000 Sats`, preusmeren je na račun **loše banke**, takođe nazvan "toksičan kusur", kako bi se osigurala stroga odvojenost od ostalih UTXO-a u novčaniku.


Ovaj UTXO je rizičan po privatnost korisnika jer nije samo vezan za svoju prošlost — a time moguće i za identitet vlasnika — već je uz to i označen kao da pripada korisniku koji je izvršio coinjoin.


Ako se ovaj UTXO spoji sa izmiksanim izlazima, potonji će izgubiti svu privatnost stečenu tokom CoinJoin ciklusa, naročito zbog CIOH (*Common-Input-Ownership-Heuristic*). Ako se spoji sa drugim toksičnim kusurom, korisnik rizikuje gubitak privatnosti jer će to povezati različite unose CoinJoin ciklusa. Stoga se mora tretirati sa oprezom. Način upravljanja ovim toksičnim UTXO-om biće detaljno opisan u poslednjem delu ovog članka, a budući tutorijali će dublje istražiti ove metode na PlanB mreži.


**Korak 3: Početno mešanje**

Nakon završetka `Tx0`, izjednačeni UTXO-i se šalju na **premix** nalog našeg novčanika, spremni da budu uvedeni u njihov prvi CoinJoin ciklus, koji se takođe naziva "početno mešanje". Ako, kao u našem primeru, `Tx0` generiše više UTXO-a namenjenih za mešanje, svaki od njih će biti integrisan u zaseban početni CoinJoin.

Na kraju ovih početnih mešanja, **premix** nalog će biti prazan, dok će naši novčići, nakon plaćanja rudarskih naknada za ovaj prvi CoinJoin, biti prilagođeni tačno na iznos definisan odabranim bazenom. U našem primeru, naši početni UTXO-i od `108 000 Sats` biće smanjeni na tačno `100 000 Sats`.

![coinjoin](assets/en/8.webp)

**Korak 4: Remiksi**

Nakon početnog mešanja, UTXO-i se prenose na **postmix** nalog. Ovaj nalog prikuplja već pomešane UTXO-e i one koji čekaju na ponovno mešanje. Kada je Whirlpool klijent aktivan, UTXO-i koji se nalaze na **postmix** nalogu automatski su dostupni za ponovno mešanje i biće nasumično odabrani da učestvuju u ovim novim ciklusima.


Kao podsetnik, remiksi su tada 100% besplatni: nisu potrebne dodatne naknade za uslugu ili rudarske naknade. Održavanje UTXO-a na **postmix** računu tako održava njihovu vrednost netaknutom, a istovremeno poboljšava njihove anonsetove. Zato je važno omogućiti ovim kovanicama da učestvuju u više CoinJoin ciklusa. To vas strogo ništa ne košta, a povećava njihove nivoe anonimnosti.


Kada odlučite da potrošite mešane UTXO-e, možete to učiniti direktno sa ovog **postmix** naloga. Preporučljivo je da mešane UTXO-e držite na ovom nalogu kako biste iskoristili besplatne remikse i sprečili ih da napuste Whirlpool krug, što bi moglo smanjiti njihovu privatnost.


Kao što ćemo videti u sledećem vodiču, postoji i opcija `mix to` koja nudi mogućnost automatskog slanja vaših mešanih novčića na drugi novčanik, kao što je neki hladni (offline) novčanik, nakon definisanog broja coinjoin-a.


Nakon što smo razgovarali o teoriji, pređimo na praksu uz vodič za korišćenje Whirlpool-a putem Sparrow desktop softverkog novčanika!


## Uputstvo: Whirlpool CoinJoin na Sparrow novčaniku

Postoji mnogo opcija za korišćenje Whirlpool-a. Prva koju želim da vam predstavim je opcija Sparrow novčanik, softver otvorenog koda za upravljanje Bitcoin novčanikom za PC.

Korišćenje Sparrow-a ima prednost što je prilično lako započeti, brzo se postavlja i ne zahteva nikakvu opremu osim računara i internet konekcije. Međutim, postoji značajan nedostatak: coinjoin-ovi će se dešavati samo kada je Sparrow pokrenut i povezan. To znači da, ako želite da mešate i ponovo mešate svoje bitkoine 24/7, moraćete stalno da držite računar uključenim.


### Instaliraj Sparrow novčanik

Da biste započeli, očigledno će vam biti potreban Sparrow softver. Možete ga direktno preuzeti sa [zvanične veb stranice](https://sparrowwallet.com/download/) ili na [njihovom GitHub-u](https://github.com/sparrowwallet/sparrow/releases).


Pre nego što instalirate softver, važno je da proverite potpis i integritet izvršnog fajla koji ste upravo preuzeli. Ako želite više detalja o procesu instalacije i verifikaciji Sparrow softvera, savetujem vam da pročitate ovaj drugi vodič: *[The Sparrow Wallet Guides](https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)*


### Kreiraj softverski novčanik

Nakon instalacije softvera, potrebno je nastaviti sa kreiranjem Bitcoin novčanika. Važno je napomenuti da je za učešće u coinjoins korišćenje softverskog novčanika(takođe nazvanog "vrućeg novčanika") neophodno. Stoga, **neće biti moguće izvršiti coinjoins sa novčanika osiguranim pomoću hardverskog novčanika**.


Iako nije imperativno, u slučaju da planirate mešati značajne količine, toplo se preporučuje da se odlučite za korišćenje jakog BIP39 passphrase za ovaj novčanik.


Da biste kreirali novi novčanik, otvorite Sparrow, zatim kliknite na karticu `File` i `New Wallet`.


![sparrow](assets/notext/9.webp)


Izaberite ime za ovaj novčanik, na primer: "CoinJoin Wallet". Kliknite na dugme `Create Wallet`.


![sparrow](assets/notext/10.webp)


Ostavite podrazumevana podešavanja, zatim kliknite na dugme `New or Imported Software Wallet`.


![sparrow](assets/notext/11.webp)


Kada pristupite prozoru za kreiranje novčanika, preporučujem odabir niza od 12 reči, jer je to sasvim dovoljno. Izaberite `Generate New` za generisanje nove fraze za oporavak, i kliknite na `Use passphrase` ako želite da dodate BIP39 passphrase. Važno je napraviti fizičku rezervnu kopiju vaših informacija za oporavak, bilo na papiru ili na metalnom nosaču, kako biste osigurali bezbednost vaših bitkoina.


![sparrow](assets/notext/12.webp)

Osigurajte valjanost vaše fraze za oporavak pre nego što kliknete na `Confirm Backup...`. Sparrow će vas zatim zamoliti da ponovo unesete vašu frazu kako bi potvrdio da ste je zabeležili. Kada je ovaj korak završen, nastavite klikom na `Create Keystore`.

![sparrow](assets/notext/13.webp)


Ostavite predloženu putanju derivacije kao podrazumevanu i pritisnite `Import Keystore`. U mom primeru, putanja derivacije se malo razlikuje jer koristim Testnet za ovaj vodič. Putanja derivacije koja bi trebalo da se pojavi za vas je sledeća:

```plaintext
m/84'/0'/0'
```


![sparrow](assets/notext/14.webp)


Nakon toga, Sparrow će prikazati detalje derivacije vašeg novog novčanika. U slučaju da ste postavili passphrase, preporučuje se da zabeležite vaš `Master fingerprint`. Iako ovaj identifikator glavnog ključa nije osetljiv podatak, biće vam koristan kasnije za verifikaciju da zaista pristupate ispravnom novčaniku i za potvrdu odsustva grešaka prilikom unosa vašeg passphrase.


Kliknite na dugme `Apply`.


![sparrow](assets/notext/15.webp)


Sparrow vas poziva da kreirate lozinku za vaš novčanik. Ova lozinka će biti potrebna za pristup putem Sparrow softverskom novčaniku. Izaberite jaku lozinku, napravite njenu rezervnu kopiju, a zatim kliknite na `Set Password`.


![sparrow](assets/notext/16.webp)


### Primanje bitkoina

Nakon kreiranja vašeg novčanika, inicijalno ćete imati jedan nalog, sa indeksom `0'`. Ovo je **depozitni** nalog o kojem smo govorili u prethodnim delovima. Ovo je nalog na koji ćete morati poslati bitkoine za mešanje.


Da biste to uradili, izaberite karticu `Receive` na levoj strani prozora. Sparrow će automatski generisati novu praznu adresu za primanje bitkoina.


![sparrow](assets/notext/17.webp)


Možete uneti oznaku za ovu adresu, a zatim poslati bitkoine da se izmešaju na njega.


![sparrow](assets/notext/18.webp)


### Pravljenje Tx0

Kada vaša transakcija bude potvrđena, možete zatim otići na karticu `UTXOs`.


![sparrow](assets/notext/19.webp)


Zatim, izaberite UTXO(e) koje želite da pošaljete u CoinJoin cikluse. Da biste istovremeno izabrali više UTXO-a, držite pritisnut `Ctrl` taster dok klikćete na UTXO-e po vašem izboru.


![sparrow](assets/notext/20.webp)


Zatim kliknite na dugme `Mix Selected` na dnu prozora. Ako se ovo dugme ne pojavljuje na vašem interfejsu, to je zato što ste na novčaniku osiguranom sa hardverskim novčanikom. Trebate koristiti softverski novčanik da biste izvršili coinjoin sa Sparrow-om.

![sparrow](assets/notext/21.webp)

Otvara se prozor koji objašnjava kako Whirlpool funkcioniše. Ovo je pojednostavljenje onoga što sam objasnio u prethodnim delovima. Kliknite na `Next` da nastavite.


![sparrow](assets/notext/22.webp)


Na sledećoj stranici možete uneti "SCODE" ako ga imate. SCODE je promotivni kod koji nudi popust na naknade za usluge bazena. Samourai novčanik povremeno pruža takve kodove svojim korisnicima tokom posebnih događaja. Savetujem vam da [pratite Samourai novčanik](https://twitter.com/SamouraiWallet) na društvenim mrežama kako ne biste propustili buduće SCODE-ove.


Na istoj stranici, takođe ćete morati da postavite stopu naknade za `Tx0` i vašu početnu mešavinu. Ovaj izbor će uticati na brzinu potvrde vaše pripremne transakcije i vašeg prvog CoinJoin-a. Zapamtite da ste odgovorni za rudarske naknade za `Tx0` i početnu mešavinu, ali nećete dugovati rudarske naknade za naredne remikse. Podesite klizač `Premix Priority` prema vašim preferencijama, zatim kliknite na `Next`.


![sparrow](assets/notext/23.webp)


U ovom novom prozoru, imaćete opciju da izaberete bazen u koji želite da uđete koristeći padajuću listu. U mom slučaju, nakon što sam inicijalno izabrao UTXO od `456 214 Sats`, moj jedini mogući izbor je bazen od `100 000 Sats`. Ovaj interfjs vas takođe obaveštava o naknadama za uslugu koje treba platiti, kao i o broju UTXO-a koji će biti integrisani u bazen. Ako vam uslovi deluju zadovoljavajuće, nastavite klikom na `Preview Premix`.


![sparrow](assets/notext/24.webp)


Nakon ovog koraka, Sparrow će vas zamoliti da unesete lozinku za vaš novčanik, onu koju ste postavili prilikom kreiranja u softveru. Kada unesete lozinku, pristupićete pregledu vaše `Tx0`. Na levoj strani vašeg prozora, videćete da je Sparrow generisao različite naloge potrebne za korišćenje Whirlpool-a (`Deposit`, `Premix`, `Postmix`, i `Badbank`). Takođe ćete imati priliku da pregledate strukturu vaše `Tx0` transakcije, sa različitim izlazima:


- Naknade za uslugu;
- Izjednačeni UTXO-ovi namenjeni za ulazak u bazen;
- Toksičan kusur (Doxxic kusur).


![sparrow](assets/notext/25.webp)


Ako vam transakcija odgovara, kliknite na `Broadcast Transaction` da biste emitovali vašu `Tx0` transakciju. U suprotnom, imate opciju da prilagodite parametre ovog `Tx0` tako što ćete odabrati `Clear` da obrišete unete podatke i započnete proces kreiranja ispočetka.


### Izvođenje Coinjoin-a

Jednom kada se Tx0 emituje, pronaći ćete svoje UTXO-ove spremne za mešanje na `Premix` nalogu.

![sparrow](assets/notext/26.webp)


Kada se `Tx0` potvrdi, vaši UTXO-ovi će biti registrovani kod koordinatora, i početna mešanja će automatski početi uzastopno.


![sparrow](assets/notext/27.webp)


Proverom `Postmix` naloga, primetićete UTXO-e koji su rezultat početnih mešanja. Ovi novčići će ostati spremni za naknadno ponovno mešanje, koje neće izazvati dodatne troškove.


![sparrow](assets/notext/28.webp)


U koloni `Mixes` moguće je videti broj coinjoin-a izvedenih za svaki od vaših novčića. Kao što ćemo videti u narednim odeljcima, ono što je zaista važno nije toliko broj remiksa sam po sebi, već povezani anonsetovi, iako su ova dva pokazatelja delimično povezana.


![sparrow](assets/notext/29.webp)


Da biste privremeno zaustavili coinjoin-ove, jednostavno kliknite na `Stop Mixing`. Imaćete opciju da nastavite operacije u bilo kom trenutku odabirom `Start Mixing`.


![sparrow](assets/notext/30.webp)


Da biste osigurali kontinuiranu dostupnost vaših UTXO-a za remixing, potrebno je da Sparrow softver bude aktivan. Zatvaranje softvera ili gašenje računara će pauzirati coinjoin-ove. Rešenje za zaobilaženje ovog problema je onemogućavanje funkcija spavanja putem postavki vašeg operativnog sistema. Pored toga, Sparrow nudi opciju za sprečavanje automatskog prelaska računara u stanje mirovanja, koju možete pronaći pod karticom `Tools` pod nazivom `Prevent Computer Sleep`.


![sparrow](assets/notext/31.webp)


### Dovršavanje coinjoin-a

Da biste potrošili svoje mešane bitkoine, imate nekoliko opcija. Najdirektniji metod je da pristupite `Postmix` nalogu i izaberete karticu `Send`.


![sparrow](assets/notext/32.webp)


U ovom odeljku, imaćete opciju da unesete adresu destinacije, iznos za slanje i naknade za transakciju, na isti način kao i za bilo koju drugu transakciju napravljenu sa Sparrow novčanikom. Ako želite, možete iskoristiti napredne funkcije privatnosti kao što je Stonewall, klikom na dugme `Privacy`.


![sparrow](assets/notext/33.webp)


[-> Saznajte više o Stonewall transakcijama.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)


Ako želite preciznije da odaberete koje novčiće ćete potrošiti, idite na karticu `UTXOs`. Izaberite UTXO-e koje želite da iskoristite, zatim pritisnite dugme `Send Selected` da pokrenete transakciju.


![sparrow](assets/notext/34.webp)

Konačno, opcija `Mix to...` dostupna na Sparrow omogućava automatsko uklanjanje odabranog UTXO iz CoinJoin ciklusa, bez dodatnih troškova. Ova funkcija omogućava određivanje broja remiksa nakon kojih UTXO neće biti reintegrisan u vaš `Postmix` nalog, već će biti direktno prebačen na drugi novčanik. Ova opcija se često koristi za automatsko slanje mešanih bitkoina na [hladni novčanik](https://planb.network/resources/glossary/cold-wallet).

Da biste koristili ovu opciju, počnite tako što ćete otvoriti novčanik primaoca zajedno sa vašim CoinJoin novčanikom unutar Sparrow softvera.


![sparrow](assets/notext/35.webp)


Zatim idite na karticu `UTXOs`, a zatim kliknite na dugme `Mix to...` na dnu prozora.


![sparrow](assets/notext/36.webp)


Otvara se prozor, započnite izborom novčanika odredišta sa padajuće liste.


![sparrow](assets/notext/37.webp)


Izaberite CoinJoin prag nakon kojeg će povlačenje biti automatski izvršeno. Ne mogu vam dati tačan broj remiksa koji treba da izvedete, jer to varira u zavisnosti od vaše lične situacije i ciljeva privatnosti, ali izbegavajte da izaberete suviše nizak prag. Preporučujem da konsultujete ovaj drugi članak kako biste saznali više o procesu remiksovanja: [REMIX - Whirlpool](https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa)


Možete ostaviti opciju `Index range` na njenoj podrazumevanoj vrednosti, `Full`. Ova funkcija omogućava mešanje istovremeno sa različitih klijenata, ali to nije ono što želimo da uradimo u ovom uputstvu. Da biste završili i aktivirali opciju `Mix to...`, pritisnite `Restart Whirlpool`.


![sparrow](assets/notext/38.webp)


Međutim, budite oprezni kada koristite opciju `Mix to`, jer uklanjanje mešanih novčića sa vašeg `Postmix` naloga može značajno povećati rizik od ugrožavanja vaše privatnosti. Razlozi za ovaj potencijal su detaljno opisani u sledećim odeljcima.


## Kako znati kvalitet naših CoinJoin ciklusa?

Da bi CoinJoin bio zaista efikasan, neophodno je da pokazuje dobru homogenost između količina ulaza i izlaza. Ova uniformnost pojačava broj mogućih interpretacija u očima spoljnog posmatrača, čime se povećava neizvesnost oko transakcije. Da bi se kvantifikovala ova neizvesnost generisana od strane CoinJoin-a, može se pribegavati izračunavanju entropije transakcije. Za detaljno istraživanje ovih indikatora, upućujem vas na tutorijal: [BOLTZMANN CALCULATOR](https://planb.network/tutorials/privacy/analysis/boltzmann-entropy-738e45af-18a6-4ce6-af1a-1bf58e15f1fe). Whirlpool model je prepoznat kao onaj koji donosi najveću homogenost u coinjoin-ima.

Zatim se procenjuje performanse nekoliko CoinJoin ciklusa na osnovu veličine grupa u kojima je novčić sakriven. Veličina ovih grupa definiše ono što se naziva anonsetima. Postoje dve vrste anonseta: prvi procenjuje dobijenu privatnost protiv retrospektivne analize (od sadašnjosti ka prošlosti) i drugi, protiv prospektivne analize (od prošlosti ka sadašnjosti). Za detaljno objašnjenje ova dva indikatora, pozivam vas da pogledate tutorijal: [Whirlpool STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)


## Kako upravljati postmixom?

Nakon izvođenja CoinJoin ciklusa, najbolja strategija je da zadržite svoje UTXO-e na **postmix** računu, čekajući njihovu buduću upotrebu. Čak je preporučljivo da ih ostavite da se neograničeno remiksuju dok ih ne budete trebali potrošiti.


Neki korisnici bi mogli razmotriti prebacivanje svojih mešanih bitkoina na hardverski novčanik. Ovo je moguće, ali je važno pažljivo pratiti preporuke Samourai novčanika kako se ne bi ugrozila stečena poverljivost.


Spajanje UTXO-a je najčešće napravljena greška. Potrebno je izbegavati kombinovanje mešanih UTXO-a sa nemešanim UTXO-ima u istoj transakciji, kako bi se izbegao CIOH (*Common-Input-Ownership-Heuristic*). Ovo zahteva pažljivo upravljanje vašim UTXO-ima unutar vašeg novčanika, posebno u smislu označavanja. Posle CoinJoin-a, spajanje UTXO-a je generalno loša praksa koja često dovodi do gubitka privatnosti kada se ne upravlja pravilno.


Takođe je važno biti oprezan pri konsolidaciji mešanih UTXO-a jednih s drugima. Umerene konsolidacije su zamislive ako vaši mešani UTXO-i imaju značajne anonsete, ali to će neizbežno smanjiti poverljivost vaših novčića. Osigurajte da konsolidacije nisu prevelike niti izvedene nakon nedovoljnog broja remiksa, jer to rizikuje uspostavljanje deduktivnih veza između vaših UTXO-a pre i posle CoinJoin ciklusa. U slučaju sumnje u vezi sa ovim manipulacijama, najbolja praksa je ne konsolidovati postmix UTXO-e, već ih prenositi jedan po jedan na vaš hardverski novčanik, generišući svaki put novu praznu adresu. Ponovo, zapamtite da pravilno označite svaki primljeni UTXO.

Takođe se savetuje da ne prebacujete svoje postmix UTXO-ove na novčanik koristeći neuobičajene skripte. Na primer, ako uđete u Whirlpool sa Multisig novčanikom koristeći `P2WSH` skripte, mala je verovatnoća da ćete biti pomešani sa drugim korisnicima koji imaju originalno isti tip novčanika. Ako povučete svoj postmix na ovaj isti Multisig novčanik, nivo privatnosti vaših mešanih bitkoina će biti znatno umanjen. Pored skripti, postoje mnogi drugi identifikatori novčanika koji vas mogu prevariti.

Kao i kod svake Bitcoin transakcije, takođe je važno ne koristiti ponovo adrese za primanje. Svaka nova transakcija treba da bude primljena na novu, praznu adresu.


Najjednostavnije i najsigurnije rešenje je da pustite svoje mešane UTXO-ove da ostanu u njihovom **postmix** nalogu, omogućavajući im da se ponovo mešaju i da ih koristite samo za trošenje. Samourai i Sparrow novčanici imaju dodatne zaštite protiv svih ovih rizika povezanih sa analizom lanca. Ove zaštite vam pomažu da izbegnete pravljenje grešaka.


## Kako upravljati doxxic kusurom?

Dalje, morate biti pažljivi u upravljanju doxxic kusurom, promenom koja nije mogla ući u CoinJoin bazen. Ovi toksični UTXO-i, koji su rezultat korišćenja Whirlpool-a, predstavljaju rizik za vašu privatnost jer uspostavljaju vezu između vas i CoinJoin korišćenja. Stoga je neophodno rukovati njima pažljivo i ne kombinovati ih sa drugim UTXO-ima, posebno mešanim UTXO-ima. Evo različitih strategija koje možete razmotriti za njihovo korišćenje:


- **Pomešajte ih u manjim bazenima:** Ako je vaš toksični UTXO dovoljno značajan da sam uđe u manji bazen, razmislite o mešanju. Ovo je često najbolja opcija. Međutim, ključno je ne spajati nekoliko toksičnih UTXO-a da biste pristupili bazenu, jer to može povezati vaše različite unose;
- **Označite ih kao "nepotrošive":** Drugi pristup je da ih više ne koristite, da ih označite kao "nepotrošive" na njihovom namenskom računu, i samo HODL. Ovo osigurava da ih slučajno ne potrošite. Ako vrednost Bitcoin poraste, mogu se pojaviti novi bazeni koji su pogodniji za vaše toksične UTXO-e;
- **Dajte donacije:** Razmislite o davanju donacija, čak i skromnih, programerima koji rade na Bitcoin-u i pratećem softveru. Takođe možete donirati organizacijama koje prihvataju BTC. Ako vam upravljanje toksičnim UTXO-ima deluje previše komplikovano, jednostavno ih se možete rešiti donacijom;
- **Kupovina poklon kartica:** Platforme kao što je [Bitrefill](https://www.bitrefill.com/) omogućavaju vam da razmenite bitkoine za poklon kartice koje se mogu koristiti kod različitih trgovaca. Ovo može biti način da se oslobodite toksičnih UTXO-a bez gubitka povezane vrednosti.
- **Konsolidujte ih na Monero:** Samourai novčanik sada nudi uslugu atomskih zamena između BTC i XMR. Ovo je idealno za upravljanje toksičnim UTXO-ima konsolidovanjem na Monero, bez ugrožavanja vaše privatnosti putem CIOH, pre nego što ih pošaljete nazad na Bitcoin. Međutim, ova opcija može biti skupa u smislu rudarskih naknada i premije zbog ograničenja likvidnosti.
- **Pošalji ih na Lightning mrežu:** Prenošenje ovih UTXO-a na Lightning mrežu radi smanjenja troškova transakcija je opcija koja bi mogla biti zanimljiva. Međutim, ova metoda može otkriti određene informacije u zavisnosti od vaše upotrebe Lightning-a i stoga bi trebalo da se praktikuje sa oprezom.


Detaljni tutorijali o implementaciji ovih različitih tehnika uskoro će biti dostupni na PlanB mreži.


**Dodatni resursi:**

[Sparrow novčanik video tutorial](https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

[Samourai novčanik video tutorial](https://planb.network/tutorials/wallet/mobile/samourai-46f88b20-5d1e-47e0-be53-237ff8737956)


- [Samourai novčanik Dokumentacija - Whirlpool](https://docs.samourai.io/Whirlpool/basic-concepts);
- [Niz na Twitteru o CoinJoins](https://twitter.com/SamouraiWallet/status/1489220847336308739);
- [Blog Post on CoinJoins](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin).
