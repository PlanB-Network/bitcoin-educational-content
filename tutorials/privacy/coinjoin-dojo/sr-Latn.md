---
name: CoinJoin - Dojo
description: Kako izvesti CoinJoin sa sopstvenim Dojo-om?
---
![cover](assets/cover.webp)


***UPOZORENJE:** Nakon hapšenja osnivača Samourai novčanika i zaplene njihovih servera 24. aprila, alat Whirlpool više ne funkcioniše, čak ni za pojedince koji imaju sopstveni Dojo ili koriste Sparrow novčanik. Ipak, moguće je da bi ovaj alat mogao biti ponovo uspostavljen u narednim nedeljama ili ponovo pokrenut na drugačiji način. Štaviše, teoretski deo ovog članka ostaje relevantan za razumevanje principa i ciljeva coinjoin-a uopšte (ne samo Whirlpool-a), kao i za razumevanje efikasnosti Whirlpool modela.*


_Pažljivo pratimo razvoj ovog slučaja kao i razvoj povezanih alata. Budite sigurni da ćemo ažurirati ovaj vodič čim nove informacije budu dostupne._


_Ovaj vodič je namenjen isključivo za obrazovne i informativne svrhe. Ne podržavamo niti podstičemo upotrebu ovih alata u kriminalne svrhe. Odgovornost je svakog korisnika da poštuje zakone u svojoj jurisdikciji._


---

U ovom vodiču ćete naučiti šta je CoinJoin i kako ga izvesti koristeći Samourai novčanik softver i Whirlpool implementaciju, koristeći sopstveni Dojo. Po mom mišljenju, ova metoda je trenutno najbolja za mešanje vaših bitkoina.


## Šta je CoinJoin na Bitcoin-u?

**CoinJoin je tehnika koja prekida mogućnost praćenja bitcoina na Blockchain-u**. Oslanja se na kolaborativnu transakciju sa specifičnom strukturom istog imena: CoinJoin transakcija.


Coinjoins poboljšavaju privatnost Bitcoin korisnika komplikovanjem analize lanca za spoljne posmatrače. Njihova struktura omogućava spajanje više novčića od različitih korisnika u jednu transakciju, čime se zamagljuju tragovi i otežava određivanje veza između ulaznih i izlaznih adresa.


Princip CoinJoin-a zasniva se na kolaborativnom pristupu: nekoliko korisnika koji žele da mešaju svoje bitkoine deponuju identične iznose kao ulaze iste transakcije. Ti iznosi se zatim preraspodeljuju kao izlazi jednake vrednosti svakom korisniku. Na kraju transakcije, postaje nemoguće povezati određeni izlaz sa poznatim korisnikom na ulazu. Ne postoji direktna veza između ulaza i izlaza, što prekida asocijaciju između korisnika i njihovog UTXO-a, kao i istoriju svake "novčića".

![coinjoin](assets/notext/1.webp)


Primer CoinJoin transakcije (nije od mene): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://Mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)


Da bi se izvršio CoinJoin uz osiguranje da svaki korisnik u svakom trenutku zadrži kontrolu nad svojim sredstvima, proces počinje tako što koordinator konstruira transakciju, a zatim je prenosi učesnicima. Svaki korisnik zatim potpisuje transakciju nakon što potvrdi da mu odgovara. Svi prikupljeni potpisi se konačno integrišu u transakciju. Ako korisnik ili koordinator pokuša da preusmeri sredstva, kroz modifikaciju izlaza CoinJoin transakcije, potpisi će biti nevažeći, što će dovesti do odbijanja transakcije od strane čvorova.


Postoji nekoliko CoinJoin implementacija, kao što su Whirlpool, JoinMarket ili Wabisabi, od kojih svaka ima za cilj upravljanje koordinacijom među učesnicima i povećanje efikasnosti CoinJoin transakcija.

U ovom vodiču, bavićemo se **Whirlpool** implementacijom, koju smatram najefikasnijim rešenjem za izvođenje coinjoin-a na Bitcoin-u. Iako je dostupno na nekoliko novčanika, u ovom vodiču ćemo se isključivo fokusirati na upotrebu sa mobilnom aplikacijom Samourai Wallet, bez Dojo servisa.


## Zašto raditi coinjoin na Bitkoin-u?

Jedan od početnih problema sa bilo kojim peer-to-peer sistemom plaćanja je dvostruko trošenje: kako sprečiti zlonamerne pojedince da iste monetarne jedinice troše više puta bez pribegavanja centralnom autoritetu za arbitražu?


Satoshi Nakamoto je pružio rešenje za ovu dilemu kroz Bitcoin protokol, peer-to-peer elektronski platni sistem koji funkcioniše nezavisno od bilo koje centralne vlasti. U svom white paper-u, on naglašava da je jedini način da se potvrdi odsustvo dvostrukog trošenja osiguravanje vidljivosti svih transakcija unutar platnog sistema.


Kako bi se osiguralo da je svaki učesnik svestan transakcija, one moraju biti javno objavljene. Stoga, rad Bitcoin-a se oslanja na transparentnu i distribuiranu infrastrukturu, omogućavajući svakom operateru čvora da verifikuje celokupne lance elektronskih potpisa i istoriju svake kovanice, od njenog stvaranja od strane rudara (eng. miner).


Transparentna i distribuirana priroda Bitcoin-ovog blockchain-a znači da svaki korisnik mreže može pratiti i analizirati transakcije svih drugih učesnika. Kao rezultat toga, anonimnost na nivou transakcija je nemoguća. Međutim, anonimnost je očuvana na nivou individualne identifikacije. Za razliku od tradicionalnog bankarskog sistema gde je svaki račun povezan sa ličnim identitetom, na Bitcoin-u, sredstva su povezana sa parovima kriptografskih ključeva, čime se korisnicima nudi oblik pseudonimnosti iza kriptografskih identifikatora.


Dakle, poverljivost na Bitcoin-u je ugrožena kada spoljašnji posmatrači uspeju da povežu specifične UTXO-e sa identifikovanim korisnicima. Kada se ova veza uspostavi, postaje moguće pratiti njihove transakcije i analizirati istoriju njihovih bitkoina. CoinJoin je upravo tehnika razvijena da prekine sledljivost UTXO-a, čime se pruža određeni nivo poverljivosti korisnicima Bitcoin-a na nivou transakcija.


## Kako funkcioniše Whirlpool?

Whirlpool se izdvaja od drugih CoinJoin metoda korišćenjem "_ZeroLink_" transakcija, koje osiguravaju da ne postoji tehnička mogućnost povezivanja između svih ulaza i svih izlaza. Ovo savršeno mešanje se postiže kroz strukturu gde svaki učesnik doprinosi identičan iznos u ulazu (osim za rudarske naknade), čime se generišu izlazi savršeno jednakih iznosa.

Ovaj restriktivni pristup unosima daje transakcijama Whirlpool CoinJoin-a jedinstvenu karakteristiku: potpuni izostanak determinističkih veza između ulaza i izlaza. Drugim rečima, svaki izlaz ima jednaku verovatnoću da bude pripisan bilo kojem učesniku, u poređenju sa svim ostalim izlazima u transakciji.

U početku je broj učesnika u svakom Whirlpool CoinJoin-u bio ograničen na 5, sa 2 nova učesnika i 3 remiksera (ove pojmove ćemo objasniti kasnije). Međutim, povećanje naknada za on-chain transakcije primećeno 2023. godine podstaklo je Samourai timove da preispitaju svoj model kako bi poboljšali privatnost uz smanjenje troškova. Tako, uzimajući u obzir tržišnu situaciju naknada i broj učesnika, koordinator sada može organizovati coinjoin-e uključujući 6, 7 ili 8 učesnika. Ove unapređene sesije nazivaju se "_Surge Cycles_". Važno je napomenuti da, bez obzira na postavku, uvek postoje samo 2 nova učesnika u Whirlpool coinjoin-ima.


Dakle, Whirlpool transakcije karakteriše identičan broj ulaza i izlaza, koji mogu biti:


- 5 ulaza i 5 izlaza;

![coinjoin](assets/notext/2.webp)


- 6 ulaza i 6 izlaza;

![coinjoin](assets/notext/3.webp)


- 7 ulaza i 7 izlaza;

![coinjoin](assets/notext/4.webp)


- 8 ulaza i 8 izlaza.

![coinjoin](assets/notext/5.webp)

Model koji predlaže Whirlpool je stoga zasnovan na malim CoinJoin transakcijama. Za razliku od Wasabi i JoinMarket-a, gde robusnost anonseta zavisi od broja učesnika u jednom ciklusu, Whirlpool se oslanja na povezivanje više malih ciklusa.


U ovom modelu, korisnik plaća naknade samo prilikom prvog ulaska u bazen (eng. pool), što mu omogućava učešće u mnoštvu remiksa bez dodatnih naknada. Novi učesnici su ti koji pokrivaju rudarske naknade za remiksere.


Sa svakim dodatnim CoinJoin u kojem novčić učestvuje, zajedno sa svojim prethodno susretnutim parnjacima, anonsetovi će eksponencijalno rasti. Cilj je stoga iskoristiti ove besplatne remikse koji, sa svakim pojavljivanjem, doprinose poboljšanju gustine anonsetova povezanih sa svakim mešanim novčićem.


Whirlpool je dizajniran uzimajući u obzir dva važna zahteva:


- Pristupačnost implementacije na mobilnim uređajima, s obzirom na to da je Samourai novčanik prvenstveno aplikacija za pametne telefone;
- Brzina ciklusa remiksovanja za promovisanje značajnog povećanja anonseta.

Ove imperative su usmeravale izbore programera Samourai novčanika u dizajnu Whirlpool-a, navodeći ih da ograniče broj učesnika po ciklusu. Premalo učesnika bi ugrozilo efikasnost CoinJoin-a, drastično smanjujući broj anonsetova generisanih svakog ciklusa, dok bi previše učesnika izazvalo probleme u upravljanju na mobilnim aplikacijama i ometalo tok ciklusa.

**Na kraju, nema potrebe za velikim brojem učesnika po coinjoin-u na Whirlpool-u, jer se anonseti postižu kroz akumulaciju više Coinjoin ciklusa.**


[-> Saznajte više o Whirlpool anonsetima.](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)


### Bazeni i CoinJoin naknade

Da bi ovi višestruki ciklusi efikasno povećali anonsetse mešanih novčića, mora se uspostaviti određeni okvir kako bi se ograničile količine UTXO-a koje se koriste. Whirlpool tako definiše različite bazene.


Bazen predstavlja grupu korisnika koji žele da se mešaju zajedno, koji se slažu oko količine UTXO koju će koristiti da optimizuju CoinJoin proces. Svaki bazen određuje fiksnu količinu za UTXO, koju korisnik mora poštovati da bi učestvovao. Dakle, da biste izvršili coinjoins sa Whirlpool-om, potrebno je da izaberete bazen. Trenutno dostupni bazeni su sledeći:


- 0.5 bitcoina;
- 0.05 Bitcoin;
- 0.01 Bitcoin;
- 0.001 Bitcoin (= 100,000 Sats).


Pridruživanjem grupi sa svojim bitkoinima, oni će biti podeljeni tako da se generišu UTXO-ovi koji su potpuno homogeni sa onima ostalih učesnika u grupi. Svaki bazen ima maksimalno ograničenje; stoga, za iznose koji prelaze ovo ograničenje, bićete primorani ili da napravite dva odvojena unosa unutar istog bazena ili da pređete u drugi bazen sa većim iznosom:


| Bazen (bitcoin) | najveći dozvoljeni iznos po ulazu (bitcoin) |
|----------------|------------------------------------|
| 0.5            | 35                                 |
| 0.05           | 3.5                                |
| 0.01           | 0.7                                |
| 0.001          | 0.025                              |

Kao što je ranije pomenuto, UTXO se smatra da pripada pool-u kada je spreman da bude integrisan u CoinJoin. Međutim, to ne znači da korisnik gubi posed nad njim. **Kroz različite cikluse mešanja, zadržavate potpunu kontrolu nad vašim ključevima i, samim tim, vašim bitcoin-ima.** Ovo je ono što razlikuje CoinJoin tehniku od drugih centralizovanih tehnika mešanja.


Da biste ušli u CoinJoin bazen, moraju platiti naknade za uslugu kao i rudarske naknade. Naknade za uslugu su fiksne za svaki bazen i namenjene su za kompenzaciju timova odgovornih za razvoj i održavanje Whirlpool-a.

Naknade za korišćenje Whirlpool-a plaćaju se samo jednom prilikom ulaska u bazen. Nakon ovog koraka, imate priliku da učestvujete u neograničenom broju remiksa bez dodatnih naknada. Ovde su trenutne fiksne naknade za svaki bazen:


| Bazen (bitcoin) | Naknade (bitcoin)        |
|----------------|---------------------------|
| 0.5            | 0.0175                    |
| 0.05           | 0.00175                   |
| 0.01           | 0.0005 (50,000 sats)      |
| 0.001          | 0.00005 (5,000 sats)      |


Ove naknade u suštini funkcionišu kao ulaznica za odabrani bazen, bez obzira na iznos koji uložite u CoinJoin. Dakle, bilo da se pridružite bazenu 0.01 sa tačno 0.01 BTC ili uđete sa 0.5 BTC, naknade će ostati iste u apsolutnoj vrednosti.


Pre nego što pređe na coinjoins, korisnik stoga ima izbor između 2 strategije:


- Odlučite se za manji bazen kako biste minimizirali naknade za uslugu, znajući da će zauzvrat dobiti nekoliko malih UTXO-a;
- Ili preferirajte veći bazen, pristajući da platite veće naknade kako biste završili sa smanjenim brojem UTXO-a veće vrednosti.


Opšte se savetuje da se ne spajaju nekoliko mešanih UTXO-a nakon CoinJoin ciklusa, jer to može ugroziti stečenu poverljivost, posebno zbog Common-Input-Ownership Heuristike (CIOH). Stoga, može biti mudro izabrati veći bazen, čak i ako to znači plaćanje više, kako bi se izbeglo previše UTXO-a male vrednosti na izlazu. Korisnik mora odmeriti ove kompromise kako bi izabrao bazen koji preferira.


Pored naknada za uslugu, mora se uzeti u obzir i naknada rudarima svojstvena svakoj Bitcoin transakciji. Kao korisnik Whirlpool-a, bićete obavezni da platite rudarske naknade za pripremnu transakciju (`Tx0`) kao i za prvi CoinJoin. Svi naredni remiksi biće besplatni, zahvaljujući Whirlpool modelu koji se finansira iz uplata novih korisnika.


Zaista, u svakom Whirlpool CoinJoin-u, dva korisnika među unosima su novi učesnici. Ostali unosi dolaze od remiksera. Kao rezultat toga, rudarske naknade za sve učesnike u transakciji pokrivaju ova dva nova učesnika, koji će zatim takođe imati koristi od besplatnih remiksa:

![coinjoin](assets/en/6.webp)

Zahvaljujući ovom sistemu naknada, Whirlpool se zaista razlikuje od drugih CoinJoin usluga jer UTXO anonsetovi nisu proporcionalni ceni koju plaća korisnik. Tako je moguće postići znatno visoke nivoe anonimnosti plaćanjem samo ulazne naknade za bazen i rudarske naknade za dve transakcije (`Tx0` i početno mešanje).

Važno je napomenuti da će korisnik takođe morati da pokrije rudarske naknade za povlačenje svojih UTXO-a iz bazena nakon završetka njihovih višestrukih coinjoin-a, osim ako nisu odabrali opciju `mix to`, koju ćemo razmotriti u tutorijalu ispod.


### Nalozi unutar HD novčanika koje koristi Whirlpool

Da bi se izvršio CoinJoin putem Whirlpool-a, novčanik mora generisati nekoliko različitih naloga. Nalog, u kontekstu HD (*Hierarchical Deterministic*) novčanika, predstavlja deo potpuno izolovan od ostalih, pri čemu se ova separacija dešava na trećem nivou dubine hijerarhije novčanika, odnosno na nivou `xpub`.


HD novčanik može teoretski izvesti do `2^(32/2)` različitih naloga. Početni nalog, koji se koristi podrazumevano na svim Bitcoin novčanicima, odgovara indeksu `0'`.


Za novčanike prilagođene Whirlpool-u, kao što su Samourai ili Sparrow, koriste se 4 naloga kako bi se zadovoljile potrebe CoinJoin procesa:


- Račun **depozita**, označen indeksom `0'`;
- Račun **bad bank** (ili doxxic change), identifikovan indeksom `2 147 483 644'`;
- Nalog **premix**, identifikovan indeksom `2 147 483 645'`;
- Nalog **postmix**, identifikovan indeksom `2 147 483 646'`.


Svaki od ovih naloga ispunjava specifičnu funkciju unutar CoinJoin-a.


Svi ovi nalozi su povezani sa jednim seed-om, što omogućava korisniku da povrati pristup svim svojim bitcoinima koristeći svoju frazu za oporavak i, ako je potrebno, svoj passphrase. Međutim, potrebno je specificirati softveru, tokom ove operacije oporavka, različite indekse naloga koji su korišćeni.


Hajde sada da pogledamo različite faze Whirlpool CoinJoin-a unutar ovih naloga.


### Različite faze coinjoin-a na Whirlpool-u

**Faza 1: Tx0**

Polazna tačka svakog Whirlpool CoinJoin-a je **depozitni** račun. Ovaj račun je onaj koji automatski koristite kada kreirate novi Bitcoin novčanik. Ovaj račun mora biti kreditiran bitcoinima koje neko želi da meša.

`Tx0` predstavlja prvi korak u procesu Whirlpool mešanja. Cilj mu je da pripremi i izjednači UTXO za CoinJoin, tako što ih deli na jedinice koje odgovaraju količini odabranog bazena, kako bi se osigurala homogenost mešanja. Izjednačeni UTXO se zatim šalju na **premix** nalog. Što se tiče razlike koja ne može ući u bazen, ona se odvaja na poseban nalog: **bad bank** (ili "doxxic change").

Ova početna transakcija Tx0 takođe služi za plaćanje servisnih naknada koordinatoru mešanja. Za razliku od sledećih koraka, ova transakcija nije kolaborativna; korisnik stoga mora snositi sve rudarske naknade:

![coinjoin](assets/en/7.webp)


U ovom primeru transakcije `Tx0`, ulaz od `372,000 Sats` sa našeg **depozitnog** računa je podeljen na nekoliko izlaznih UTXO-a, koji su raspoređeni na sledeći način:


- Iznos od `5,000 Sats` namenjen koordinatoru kao naknada za usluge, što odgovara ulasku u bazen od `100,000 Sats`;
- Tri UTXO-a pripremljena za mešanje, preusmerena na naš **premix** nalog i registrovana kod koordinatora. Ovi UTXO su izjednačeni na `108,000 Sats` svaki, da pokriju rudarske naknade za njihovo buduće početno mešanje;
- Višak koji ne može ući u bazen, jer je premali, smatra se toksičnim kusurom. On se šalje na svoj specifičan račun. Ovde, ova promena iznosi `40,000 Sats`;
- Konačno, postoji `3,000 Sats` koji ne predstavljaju izlaz, već su rudarske naknade neophodne za potvrdu `Tx0`.


Na primer, ovde je pravi Whirlpool Tx0 (nije od mene): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://Mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)


**Korak 2: Doxxic kusur**

Višak koji nije mogao biti integrisan u bazen, ovde ekvivalentan `40,000 Sats`, preusmeren je na račun **bad bank**, takođe nazvan "doxxic kusur", kako bi se osigurala stroga odvojenost od ostalih UTXO-a u novčaniku.


Ovaj UTXO je opasan za privatnost korisnika jer ne samo da je još uvek povezan sa svojom prošlošću, i stoga moguće sa identitetom svog vlasnika, već je dodatno zabeleženo da pripada korisniku koji je izvršio CoinJoin.

Ako se ovaj UTXO spoji sa mešovitim izlazima, izgubićete svu poverljivost stečenu tokom CoinJoin ciklusa, naročito zbog Common-Input-Ownership-Heuristic (CIOH). Ako se spoji sa drugim doxxic kusurima, korisnik rizikuje gubitak poverljivosti jer će to povezati različite ulaze CoinJoin ciklusa. Stoga se mora pažljivo rukovati. Način upravljanja ovim toksičnim UTXO biće detaljno opisan u poslednjem delu ovog članka, a budući tutorijali će detaljnije pokriti ove metode na PlanB Network-u.


**Korak 3: Početno mešanje**

Nakon što je `Tx0` završen, izjednačeni UTXO-i se šalju na **premix** nalog našeg novčanika, spremni da budu uvedeni u njihov prvi CoinJoin ciklus, koji se takođe naziva "početno mešanje". Ako, kao u našem primeru, `Tx0` generiše nekoliko UTXO-a namenjenih za mešanje, svaki od njih će biti integrisan u zaseban početni CoinJoin.


Na kraju ovih prvih mešanja, **premix** račun će biti prazan, dok će naši novčići, nakon plaćanja rudarske naknada za ovaj prvi CoinJoin, biti prilagođeni tačno na iznos definisan od strane izabranog bazena. U našem primeru, naši početni UTXO-i od `108 000 Sats` će biti smanjeni tačno na `100 000 Sats`.

![coinjoin](assets/en/8.webp)

**Korak 4: Remiksi**

Nakon početnog mešanja, UTXO-i se prenose na **postmix** nalog. Ovaj nalog prikuplja već pomešane UTXO-e i one koji čekaju na ponovno mešanje. Kada je Whirlpool klijent aktivan, UTXO-i koji se nalaze na **postmix** nalogu automatski su dostupni za ponovno mešanje i biće nasumično odabrani za učešće u ovim novim ciklusima.


Kao podsetnik, remiksi su tada 100% besplatni: nisu potrebne dodatne naknade za uslugu ili rudarske naknade. Održavanje UTXO-a na **postmix** računu tako održava njihovu vrednost netaknutom i istovremeno poboljšava njihove anonsete. Zato je važno omogućiti ovim kovanicama da učestvuju u više CoinJoin ciklusa. To vas strogo ništa ne košta, a povećava nivoe njihove anonimnosti.


Kada odlučite da potrošite mešane UTXO-e, možete to učiniti direktno sa ovog **postmix** naloga. Preporučljivo je da mešane UTXO-e držite na ovom nalogu kako biste iskoristili besplatne remikse i izbegli njihovo napuštanje Whirlpool-a, što bi moglo smanjiti njihovu poverljivost.


Kao što ćemo videti u sledećem vodiču, postoji i opcija `mix to` koja nudi mogućnost automatskog slanja vaših mešanih novčića na drugi novčanik, kao što je hladni, offline novčanik, nakon definisanog broja coinjoin-a.

Nakon što smo pokrili teoriju, zaronimo u praksu uz vodič o korišćenju Whirlpool-a putem Android aplikacije Samourai novčanika, sinhronizovane sa Whirlpool CLI i GUI na vašem sopstvenom Dojo-u!

## Uputstvo: CoinJoin Whirlpool sa Vašim sopstvenim Dojo-om

Postoji mnogo opcija za korišćenje Whirlpool-a. Ona koju želim da predstavim ovde je opcija Samourai novčanika, open-source aplikacija za upravljanje Bitcoin novčanikom na Androidu, ali ovaj put **sa sopstvenim Dojo-om**.


Izvođenje coinjoin-a putem Samourai novčanika koristeći sopstveni Dojo je, po mom mišljenju, najefikasnija strategija za izvođenje coinjoin-a na Bitcoin-u do danas. Ovaj pristup zahteva početno ulaganje u smislu postavljanja, ali kada je jednom uspostavljen, nudi mogućnost kontinuiranog mešanja i ponovnog mešanja vaših bitcoina, 24 sata dnevno, 7 dana u nedelji, bez potrebe da vaša Samourai aplikacija bude stalno aktivna. Zaista, zahvaljujući Whirlpool CLI koji rade na Bitcoin čvoru, uvek ste spremni da učestvujete u coinjoin-ima. Samourai aplikacija vam zatim pruža priliku da trošite svoja pomešana sredstva u bilo koje vreme, gde god se nalazili, direktno sa vašeg pametnog telefona. Štaviše, ova metoda ima prednost što vas nikada ne povezuje sa serverima koje upravljaju Samourai timovi, čime se vaš `xpub` čuva od bilo kakvog spoljnog izlaganja.


Ova tehnika je stoga idealna za one koji traže maksimalnu privatnost i najviši kvalitet CoinJoin ciklusa. Međutim, zahteva da imate Bitcoin čvor na raspolaganju i, kao što ćemo kasnije videti, zahteva određeno podešavanje. Stoga je pogodnija za korisnike srednjeg do naprednog nivoa. Za početnike preporučujem da se upoznaju sa CoinJoin kroz ova dva druga tutorijala, koji pokazuju kako to uraditi iz Sparrow novčanika ili Samourai novčanika (bez Dojo):


- [Tutorial za Sparrow Wallet CoinJoin](https://planb.network/tutorials/privacy/on-chain/coinjoin-sparrow-wallet-84def86d-faf5-4589-807a-83be60720c8b)**;
- [Samourai Wallet CoinJoin tutorial (without Dojo)](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef)**.


### Razumevanje postavke

Za početak, trebat će vam Dojo! Dojo je implementacija Bitcoin čvora zasnovana na Bitcoin Core-u, koju su razvili timovi Samourai.


Da biste pokrenuli sopstveni Dojo, imate dve opcije: možete samostalno instalirati Dojo čvor ili iskoristiti Dojo kao dodatak uz neko drugo „čvor-u-kutiji (eng.node-in-box)“ rešenje za Bitcoin čvor.Trenutno, dostupne opcije su:


- [RoninDojo](https://ronindojo.io/), koji je Dojo obogaćen dodatnim alatima, uključujući asistenta za instalaciju i asistenta za administraciju. Detaljno opisujem proceduru za postavljanje i korišćenje RoninDojo-a u ovom drugom vodiču: [RONINDOJO V2](https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8);
- [Umbrel](https://umbrel.com/) sa aplikacijom "Samourai Server";
- [MyNode](https://mynodebtc.com/) sa aplikacijom "Dojo";
- [Nodl](https://www.nodl.eu/) sa aplikacijom "Dojo";
- [Citadel](https://runcitadel.space/) sa aplikacijom "Samourai".

![coinjoin](assets/notext/9.webp)

U našem okruženju koristićemo tri različita interfejsa:


- **Samourai novčanik**, u kojem će se nalaziti naš Bitcoin novčanik posebno namenjen za coinjoin-e Dostupan besplatno na Androidu, ova FOSS aplikacija vam omogućava da kontrolišete vaše mešanje UTXO-a unutar novčanika, posebno za trošenje vašeg postmix-a sa vašeg pametnog telefona;
- **Whirlpool CLI** (_Command Line Interface_), koji će raditi na čvoru koji hostuje Dojo. Ovaj softver će imati pristup ključevima vašeg Samourai novčanika. On je odgovoran za komunikaciju sa koordinatorom i kontinuirano upravljanje coinjoin-ima. Djeluje kao kopija vašeg Samourai novčanika na vašem čvoru, spreman da učestvuje u coinjoin-ima u bilo kojem trenutku;
- **Whirlpool GUI** (_Graphical User Interface_), grafički korisnički interfejs koji ćemo koristiti za praćenje aktivnosti Whirlpool CLI i pokretanje mešanja na daljinu. Whirlpool GUI pruža vizuelni prikaz operacija koje sprovode Whirlpool CLI. Ovaj softver mora biti instaliran na računaru odvojenom od Dojo-a. Za korisnike Umbrel, MyNode, Nodl i Citadel, Whirlpool GUI je obavezan. Međutim, sa RoninDojo, Whirlpool GUI interfejsa je već integrisan u web interfejs vašeg čvora putem aplikacije `Whirlpool`. Stoga, neće biti potrebno da ga instalirate na zaseban računar.


Po mom mišljenju, korišćenje RoninDojo-a predstavlja najbolje rešenje za izvođenje coinjoin-a sa Dojo-om. Pošto je ovaj softver za node-in-box u direktnom partnerstvu sa Samourai timovima, RoninDojo je mnogo više optimizovan za ovo. Štaviše, integracija Whirlpool GUI u web interfejs značajno pojednostavljuje proces podešavanja. U ovom vodiču, ipak ću objasniti kako to uraditi sa drugim rešenjima koja integrišu Dojo (Umbrel, Nodl, MyNode i Citadel).


### Priprema vašeg dojo-a

Da biste započeli, potrebno je da instalirate Dojo i dobijete QR kod ili link koji će vam omogućiti da se povežete sa njim na daljinu. Ovaj link je Tor adresa koja se završava sa `.onion`. Ako koristite RoninDojo, jednostavno idite na meni `Pairing` da biste pristupili ovim informacijama.

![coinjoin](assets/notext/10.webp)


Ispod `Samourai Dojo`, kliknite na dugme `Pair now`.


![coinjoin](assets/notext/11.webp)


Vaš QR kod za povezivanje i odgovarajući link će biti prikazani.


![coinjoin](assets/notext/12.webp)


Ako ste na Umbrel-u, idite u App Store i potražite aplikaciju `Samourai Server`. Nalazi se na kartici `Bitcoin`.


![coinjoin](assets/notext/13.webp)


Instaliraj aplikaciju.


![coinjoin](assets/notext/14.webp)


Nakon otvaranja aplikacije, imaćete pristup QR kodu za povezivanje sa vašim Dojo-om.


![coinjoin](assets/notext/15.webp)


Ako koristite drugi node-in-box softver kao što su MyNode, Citadel ili Nodl, proces je sličan kao kod Umbrel-a. Potrebno je instalirati Samourai ili Dojo aplikaciju kako biste dobili potrebne informacije za povezivanje sa vašim Dojo-om.


![coinjoin](assets/notext/16.webp)


### Priprema vašeg Samourai novčanika

Nakon što preuzmete informacije o povezivanju sa vašim Dojo-om, sada je vreme da postavite vaš novčanik za coinjoins. Postoje dva scenarija: ako još uvek nemate Samourai novčanik na vašem pametnom telefonu, proces je jednostavan, samo kreirajte novi.


S druge strane, ako već imate Samourai novčanik, moraćete ponovo instalirati aplikaciju da biste je povezali sa novim Dojo-om. Ovaj korak je neophodan jer se veza sa Dojo-om može uspostaviti samo pri prvom pokretanju aplikacije. Međutim, zahvaljujući automatski generisanom šifrovanom rezervnom fajlu od strane Samouraia na vašem telefonu, ova procedura je jednostavna i brza.


*Ako nikada niste koristili Samourai, možete preskočiti ove preliminarne korake i preći direktno na instalaciju aplikacije.*


Prvo i najvažnije, uverite se da je vaša Samourai novčanik aplikacija ažurirana. Da biste to uradili, proverite Google Play Store ili uporedite verziju vaše aplikacije u `Settings > Other` sa onom dostupnom na Samourai vebsajtu.


![coinjoin](assets/notext/17.webp)


Uverite se da imate svoju Samourai novčanik frazu za oporavak i da je čitljiva. Zatim, sprovedite test vašeg BIP39 passphrase tako što ćete otići na `Settings > Troubleshoot > passphrase/Backup test` da potvrdite njegovu tačnost.


![coinjoin](assets/notext/18.webp)

Unesite svoj passphrase, zatim proverite da li Samourai potvrđuje njegovu validnost.

![coinjoin](assets/notext/19.webp)


Ako je vaš passphrase nevažeći, ili ako nemate svoju frazu za oporavak, neophodno je odmah zaustaviti proceduru! **Rizikujete da izgubite svoje bitkoine tokom ove operacije.** U tom slučaju, savetuje se da prebacite svoja sredstva na drugi novčanik i započnete sa novim praznim Samourai novčanikom. Sledeće korake treba pratiti samo ako ste sigurni da imate sve potrebne informacije za rezervnu kopiju i da je vaš passphrase važeći.


Zatim nastavite sa kreiranjem šifrovane rezervne kopije vašeg novčanika i kopirajte je u svoj clipboard. Da biste izvršili ovu operaciju, kliknite na tri male tačke koje se nalaze u gornjem desnom uglu ekrana, zatim izaberite `Export Wallet backup`.


![coinjoin](assets/notext/20.webp)


**Od ovog koraka nadalje, nemojte kopirati ništa drugo u svoj clipboard!** Apsolutno je neophodno da zadržite svoju kopiranu rezervnu kopiju.


Ako ste pravilno izvršili prethodne korake, sada možete bezbedno obrisati svoj Samourai novčanik. Da biste to uradili, idite na: `Settings > Wallet > Secure erase the Wallet`.


![coinjoin](assets/notext/21.webp)


![coinjoin](assets/notext/22.webp)


*Ako nikada niste koristili Samourai i instalirate aplikaciju od početka, možete nastaviti tutorijal od ovog koraka.*


Vaša Samourai aplikacija je sada resetovana. Otvorite aplikaciju i nastavite sa koracima podešavanja kao da je koristite prvi put.


![coinjoin](assets/notext/23.webp)


U sledećem koraku, pristupićete stranici posvećenoj konfigurisanju vašeg Dojo-a. Izaberite opciju `Dojo`, zatim unesite podatke za prijavu vašeg Dojo-a. Da biste to uradili, imate opciju da skenirate informacije pritiskom na `Scan QR`.


![coinjoin](assets/notext/24.webp)


*Za nove korisnike Samourai-a, biće potrebno da kreiraju novčanik od nule. Ako vam je potrebna pomoć, možete se konsultovati sa uputstvima za postavljanje novog Samourai novčanika [u ovom vodiču, posebno u odeljku "Kreiranje softverskog novčanika"](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef)*


Ako nastavljate sa restauracijom već postojećeg Samourai novčanika, izaberite `Restore existing Wallet`, zatim odaberite `I have a Samourai backup file`.


![coinjoin](assets/notext/25.webp)

Normalno, uvek bi trebalo da imate vašu datoteku za oporavak u clipboard-u. Zatim kliknite na `PASTE` da ubacite vašu datoteku u određenu lokaciju. Da biste je dešifrovali, biće potrebno da unesete BIP39 passphrase vašeg novčanika u odgovarajuće polje, koje se nalazi odmah ispod. Da završite, kliknite na `FINISH`.

![coinjoin](assets/notext/26.webp)


Bićete preusmereni na vaš Samourai novčanik koji će, ovog puta, biti povezan sa vašim sopstvenim Dojo-om.


![coinjoin](assets/notext/27.webp)


### Instaliranje Whirlpool GUI

Sada je vreme da instalirate Whirlpool GUI, grafički korisnički interfej koji će vam omogućiti da upravljate svojim CoinJoin ciklusima sa vašeg uobičajenog računara. Za korisnike RoninDojo-a, ovaj korak nije neophodan jer se upravljanje coinjoin-ima može obaviti direktno putem web interfejsa u `Apps > Whirlpool`. Međutim, ako koristite drugo Bitcoin "node-in-box" rešenje, neophodno je da nastavite sa ovom instalacijom.

![coinjoin](assets/notext/28.webp)

Idite na svoj lični računar i preuzmite Whirlpool softver sa zvaničnog Samourai Wallet sajta, odabirom verzije koja odgovara vašem operativnom sistemu.


![coinjoin](assets/notext/29.webp)


Pre pokretanja Whirlpool GUI, neophodno je instalirati JAVA 8 ili višu verziju na vašem računaru. Za ovo, [možete instalirati OpenJDK](https://adoptium.net/).

![coinjoin](assets/notext/30.webp)

Takođe je neophodno imati Tor daemon ili Tor Browser operativan u pozadini na vašem računaru. Uverite se da pokrenete Tor pre svake Whirlpool GUI sesije korišćenja. Ako Tor još nije instaliran na vašem uređaju, [možete ga preuzeti i instalirati sa zvanične stranice projekta](https://www.torproject.org/download/), zatim se uverite da ga pokrenete u pozadini.


![coinjoin](assets/notext/31.webp)


Kada je JDK instaliran na vašem sistemu i Tor pokrenut u pozadini, možete pokrenuti Whirlpool GUI.


![coinjoin](assets/notext/32.webp)


Iz Whirlpool GUI, kliknite na `Advanced: Remote CLI` da povežete vaš Whirlpool CLI koji je na vašem Dojo-u. Biće vam potreban Tor adresa vašeg Whirlpool CLI.


![coinjoin](assets/notext/33.webp)


Da biste locirali svoju Tor adresu na Umbrel-u i drugim "node-in-box" rešenjima, jednostavno pokrenite Samourai Server ili Dojo aplikaciju (naziv može varirati u zavisnosti od korišćenog softvera). Tor adresa će biti direktno vidljiv na stranici aplikacije.

![coinjoin](assets/notext/34.webp)

U Whirlpool GUI unesite Tor adresu koji ste ranije dobili u polje `CLI Address`. Zadržite prefiks `http://`, ali nemojte dodavati port `:8899` na kraju. Zalepite samo adresu kako vam je dostavljena.

![coinjoin](assets/notext/35.webp)


U polje Tor Proxy unesite `socks5://127.0.0.1:9050` ako koristite Tor daemon, ili `socks5://127.0.0.1:9150` ako je u pitanju Tor pregledač. Kada se prvi put povezujete na Whirlpool CLI putem Whirlpool GUI, moguće je ostaviti polje za API ključ prazno. Ako ovo nije vaša prva konekcija, molimo unesite vaš API ključ u predviđeni prostor. Ovaj ključ se može pronaći na istoj stranici kao i vaša Tor adresa.


![coinjoin](assets/notext/36.webp)


Kada popunite sve, kliknite na dugme `Connect`. Molimo sačekajte, povezivanje može potrajati nekoliko minuta.


![coinjoin](assets/notext/37.webp)


### Uparivanje vašeg Samourai novčanika sa Whirlpool GUI-em

*Za korisnike RoninDojo-a, možete nastaviti tutorijal ovde.*


Sada ćemo upariti Samourai novčanik koji smo ranije konfigurisali sa Whirlpool GUI softverom, ili direktno sa RoninDojo za one koji koriste ovaj softver. Bilo da koristite Whirlpool GUI ili RoninDojo, bićete zamoljeni da nalepite ili skenirate informacije za uparivanje vašeg Samourai novčanika.


![coinjoin](assets/notext/38.webp)


Da biste pronašli ove informacije, idite na postavke vašeg novčanika.


![coinjoin](assets/notext/39.webp)


Kliknite na `Transactions`, zatim na `Pair to Whirlpool GUI`.


![coinjoin](assets/notext/40.webp)


Samourai će vam zatim pružiti potrebne informacije za uspostavljanje veze. Budite pažljivi, ovi podaci su osetljivi! Možete ih preneti na svoj računar bilo kopiranjem direktno ili skeniranjem prikazanog QR koda, koristeći veb kameru vašeg računara nakon što kliknete na simbol QR koda.


![coinjoin](assets/notext/41.webp)


Nakon izvođenja ove operacije, u Whirlpool GUI, izaberite `Initialize GUI`. Molimo sačekajte, jer ovaj korak može potrajati trenutak.


![coinjoin](assets/notext/42.webp)


Bilo da koristite Whirlpool GUI ili RoninDojo, bićete upitani da unesete passphrase vašeg Samourai novčanika. Unesite ga u predviđeno polje, zatim pritisnite dugme `Login` da nastavite.


![coinjoin](assets/notext/43.webp)


Zatim ćete stići na početnu stranicu Whirlpool CLI


![coinjoin](assets/notext/44.webp)


### Pokretanje coinjoin-a iz Whirlpool GUI

*Za korisnike RoninDojo-a, proces koji treba pratiti je identičan. Interfejs Whirlpool aplikacije integrisane u RoninDojo nudi iste opcije i funkcionalnosti kao Whirlpool GUI softver na desktopu. Stoga, možete pratiti ova uputstva na isti način.*

Sada kada je sve postavljeno, spremni ste da počnete sa mešanjem vaših bitkoina. Da biste to uradili, prebacite bitkoine koje želite da mešate na **Deposit** račun vašeg Samourai novčanika. Ova operacija se može izvesti direktno putem aplikacije Samourai novčanika ili na Whirlpool GUI. Sa glavne stranice, kliknite na dugme `+ Deposit` koje se nalazi u gornjem levom uglu.


![coinjoin](assets/notext/45.webp)


Whirlpool GUI će generate adresu za primanje. Takođe će prikazati minimalni iznos potreban za učešće u svakom CoinJoin bazenu. Ovaj iznos varira u zavisnosti od tržišnih naknada. Preporučljivo je uplatiti iznos nešto veći od minimalno potrebnog, jer ako se rudarske naknade ne smanje, vaš UTXO možda neće biti prihvaćen u željenom bazenu. Stoga, pošaljite svoje bitkoine na navedenu adresu. Da biste dobili novu adresu, jednostavno kliknite na dugme `Renew address`.


![coinjoin](assets/notext/46.webp)


Kada je depozit potvrđen, moći ćete ga videti u **Depozit** nalogu na Whirlpool GUI.


![coinjoin](assets/notext/47.webp)


Da biste započeli CoinJoin cikluse, izaberite UTXO-ove koje želite da mešate i pritisnite dugme `Premix`. Budite pažljivi: ako izaberete nekoliko različitih UTXO-ova u isto vreme, oni će biti kombinovani tokom `TX0` pripremne transakcije. Ovo spajanje može dovesti do smanjenja privatnosti, posebno ako UTXO-ovi dolaze iz različitih izvora, zbog Common Input Ownership Heuristike (CIOH).


![coinjoin](assets/notext/48.webp)


Stranica za konfiguraciju Whirlpool se otvara. Možete izabrati bazen u koji želite da uđete. Takođe izaberite rudarske naknade za `TX0` i prve coinjoins. Na dnu ove stranice, rezime će vam prikazati količinu doxxic kusura kao i količinu i broj UTXO-a koji će biti izjednačeni i uključeni u CoinJoin cikluse. Ako ste zadovoljni ovom konfiguracijom, pritisnite dugme `Premix` da započnete CoinJoin cikluse.

![coinjoin](assets/notext/49.webp)


Jednom kada je `TX0` kreirana, moći ćete da vidite svoje izjednačene UTXO-e u nalogu **Premix**, čekajući potvrdu. Da biste omogućili da se vaši novčići automatski mešaju 24 sata dnevno, 7 dana u nedelji, preporučujem aktiviranje opcije `Automatically mix premix & postmix`. Ovu funkciju ćete pronaći u kartici `Configuration`, koja se nalazi levo od vašeg Whirlpool GUI prozora.

![coinjoin](assets/notext/50.webp)

Nakon pokretanja coinjoin-a, možete izaći iz Whirlpool GUI kao i iz Samourai novčanika. Samo vaš čvor treba ostati povezan kako biste mogli učestvovati u kontinuiranim coinjoin-ima. Međutim, preporučljivo je periodično proveravati napredak vaših CoinJoin ciklusa. Ako primetite da vaši UTXO-i više nisu birani za CoinJoin neko vreme, to može ukazivati na grešku. U tom slučaju, idite na Whirlpool CLI i izaberite `Start` da ponovo pokrenete vašu dostupnost za coinjoin-e.


![coinjoin](assets/notext/51.webp)


Vaši mešani UTXO-i su vidljivi sa **Postmix** naloga na Whirlpool GUI. Pored toga, imate opciju da ih direktno pregledate i potrošite putem Whirlpool interfejsa na vašem Samourai novčaniku. Da biste pristupili ovom meniju, kliknite na plavi `+` na dnu ekrana, a zatim izaberite `Whirlpool`.


![coinjoin](assets/notext/52.webp)


Whirlpool nalozi su lako prepoznatljivi na Samourai novčaniku po svojoj plavoj boji. Ovo vam omogućava da trošite svoje mešane UTXO-ove sa bilo kog mesta i u bilo koje vreme, direktno sa vašeg pametnog telefona.


![coinjoin](assets/notext/53.webp)


Da biste pratili svoje automatske coinjoin-e, takođe preporučujem postavljanje watch-only novčanika putem aplikacije Sentinel. Dodajte ZPUB vašeg **Postmix** naloga i pratite napredak vaših CoinJoin ciklusa u realnom vremenu. Ako želite da razumete kako koristiti Sentinel, preporučujem da pogledate ovaj drugi vodič na PlanB Network: [**SENTINEL WATCH-ONLY**](https://planb.network/tutorials/wallet/mobile/sentinel-9876f960-e964-4d20-8a6e-36231de1f4d9)
