---
name: CoinJoin - Samourai novčanik
description: Kako izvršiti CoinJoin na Samourai novčaniku?
---
![cover](assets/cover.webp)


***UPOZORENJE:** Nakon hapšenja osnivača Samourai novčanika i zaplene njihovih servera 24. aprila, alat Whirlpool više ne funkcioniše, čak ni za pojedince koji imaju sopstveni Dojo ili koriste Sparrow novčanik. Ipak, postoji mogućnost da bi ovaj alat mogao biti ponovo uspostavljen u narednim nedeljama ili pokrenut na drugačiji način. Štaviše, teorijski deo ovog članka ostaje relevantan za razumevanje principa i ciljeva coinjoin-a uopšte (ne samo Whirlpool-a), kao i za razumevanje efikasnosti Whirlpool modela.*


_Pažljivo pratimo razvoj ovog slučaja kao i razvoj povezanih alata. Budite sigurni da ćemo ažurirati ovaj vodič čim nove informacije budu dostupne._


_Ovaj vodič je pružen isključivo u obrazovne i informativne svrhe. Ne podržavamo niti ohrabrujemo korišćenje ovih alata u kriminalne svrhe. Odgovornost je svakog korisnika da se pridržava zakona u svojoj jurisdikciji._


---

> *Bitcoin novčanik za ulice*

U ovom vodiču ćete naučiti šta je CoinJoin i kako ga izvršiti koristeći softver Samourai novčanika i Whirlpool implementaciju.


## Šta je CoinJoin na Bitcoin-u?

**CoinJoin je tehnika koja prekida mogućnost praćenja bitcoina na Blockchain-u**. Oslanja se na kolaborativnu transakciju sa specifičnom strukturom istog imena: CoinJoin transakcija.


Coinjoins poboljšavaju privatnost Bitcoin korisnika komplikovanjem analize lanca za spoljne posmatrače. Njihova struktura omogućava spajanje više novčića od različitih korisnika u jednu transakciju, čime se zamagljuju tragovi i otežava određivanje veza između ulaznih i izlaznih adresa.


CoinJoin princip je zasnovan na kolaborativnom pristupu: nekoliko korisnika koji žele da mešaju svoje bitkoine deponuju identične iznose kao ulaze iste transakcije. Ti iznosi se zatim redistribuiraju kao izlazi jednake vrednosti svakom korisniku. Na kraju transakcije, postaje nemoguće povezati određeni izlaz sa poznatim korisnikom u ulazu. Ne postoji direktna veza između ulaza i izlaza, čime se prekida asocijacija između korisnika i njihovog UTXO, kao i istorija svakog "novčića".

![coinjoin](assets/notext/1.webp)


Primer CoinJoin transakcije (nije od mene): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://Mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)


Da bi se izveo CoinJoin uz osiguranje da svaki korisnik u svakom trenutku zadrži kontrolu nad svojim sredstvima, proces počinje konstrukcijom transakcije od strane koordinatora, koji je zatim prenosi učesnicima. Svaki korisnik zatim potpisuje transakciju nakon što proveri da mu odgovara. Svi prikupljeni potpisi se konačno integrišu u transakciju. Ako korisnik ili koordinator pokuša da preusmeri sredstva, menjajući izlaze CoinJoin transakcije, potpisi će biti nevažeći, što će dovesti do odbijanja transakcije od strane čvorova.


Postoji nekoliko CoinJoin implementacija, kao što su Whirlpool, JoinMarket ili Wabisabi, od kojih svaka ima za cilj upravljanje koordinacijom među učesnicima i povećanje efikasnosti CoinJoin transakcija.

U ovom vodiču, bavićemo se **Whirlpool** implementacijom, koju smatram najefikasnijim rešenjem za izvođenje coinjoin-a na Bitcoin. Iako je dostupna na nekoliko novčanika, u ovom vodiču ćemo isključivo istražiti njenu upotrebu sa mobilnom aplikacijom Samourai novčanika, bez Dojo-a.


## Zašto izvoditi coinjoins na Bitcoin-u?

Jedan od početnih problema sa bilo kojim peer-to-peer sistemom plaćanja je dvostruko trošenje: kako sprečiti zlonamerne pojedince da iste monetarne jedinice troše više puta bez pribegavanja centralnom autoritetu za arbitražu?


Satoshi Nakamoto je pružio rešenje za ovu dilemu putem Bitcoin protokola, peer-to-peer elektronskog sistema plaćanja koji funkcioniše nezavisno od bilo koje centralne vlasti. U svom white paper-u, on ističe da je jedini način da se potvrdi odsustvo dvostrukog trošenja osiguravanje vidljivosti svih transakcija unutar sistema plaćanja.


Da bi se garantovalo da je svaki učesnik svestan transakcija, one moraju biti javno objavljene. Stoga, rad Bitcoin-a se oslanja na transparentnu i distribuiranu infrastrukturu, omogućavajući svakom operateru čvora da verifikuje celokupnost lanaca elektronskih potpisa i istoriju svake kovanice, od njenog stvaranja od strane rudara (eng. Miner).


Transparentna i distribuirana priroda Bitcoin-ovog Blockchain-a znači da bilo koji korisnik mreže može pratiti i analizirati transakcije svih drugih učesnika. Kao rezultat toga, anonimnost na nivou transakcija je nemoguća. Međutim, anonimnost se čuva na nivou individualne identifikacije. Za razliku od tradicionalnog bankarskog sistema gde je svaki račun povezan sa ličnim identitetom, na Bitcoin-u, sredstva su povezana sa parovima kriptografskih ključeva, čime se korisnicima nudi oblik pseudonimnosti iza kriptografskih identifikatora.


Dakle, poverljivost na Bitcoin-u je ugrožena kada spoljni posmatrači uspeju da povežu određene UTXO-e sa identifikovanim korisnicima. Kada se ova povezanost uspostavi, postaje moguće pratiti njihove transakcije i analizirati istoriju njihovih bitkoina. CoinJoin je upravo tehnika razvijena da prekine sledljivost UTXO-a, čime se Bitcoin korisnicima na nivou transakcija nudi određeni nivo poverljivosti.


## Kako funkcioniše Whirlpool?

Whirlpool se izdvaja od drugih CoinJoin metoda korišćenjem "_ZeroLink_" transakcija, koje osiguravaju da ne postoji tehnička mogućnost povezivanja između svih ulaza i svih izlaza. Ovo savršeno mešanje se postiže kroz strukturu gde svaki učesnik doprinosi identičnim iznosom u ulazu (osim za rudarske naknade), čime se generišu izlazi savršeno jednakih iznosa.

Ovaj restriktivni pristup unosima daje Whirlpool CoinJoin transakcijama jedinstvenu karakteristiku: potpuni izostanak determinističkih veza između unosa i izlaza. Drugim rečima, svaki izlaz ima jednaku verovatnoću da bude pripisan bilo kojem učesniku, u poređenju sa svim ostalim izlazima u transakciji.

U početku, broj učesnika u svakom Whirlpool CoinJoin-u bio je ograničen na 5, sa 2 nova učesnika i 3 remiksera (ove pojmove ćemo objasniti kasnije). Međutim, povećanje naknada za on-chain transakcije primećeno 2023. godine podstaklo je Samourai timove da preispitaju svoj model kako bi poboljšali privatnost uz smanjenje troškova. Tako, uzimajući u obzir tržišnu situaciju naknada i broj učesnika, koordinator sada može organizovati coinjoin-ove koji uključuju 6, 7 ili 8 učesnika. Ove unapređene sesije nazivaju se "_Surge Cycles_". Važno je napomenuti da, bez obzira na konfiguraciju, uvek postoje samo 2 nova učesnika u Whirlpool coinjoin-ovima.


Dakle, Whirlpool transakcije karakteriše identičan broj ulaza i izlaza, koji mogu biti:


- 5 ulaza i 5 izlaza;

![coinjoin](assets/notext/2.webp)


- 6 ulaza i 6 izlaza;

![coinjoin](assets/notext/3.webp)


- 7 ulaza i 7 izlaza;

![coinjoin](assets/notext/4.webp)


- 8 ulaza i 8 izlaza.

![coinjoin](assets/notext/5.webp)

Model koji predlaže Whirlpool zasniva se na malim CoinJoin transakcijama. Za razliku od Wasabi i JoinMarket, gde robusnost anonseta zavisi od broja učesnika u jednom ciklusu, Whirlpool se oslanja na povezivanje nekoliko ciklusa male veličine.


U ovom modelu, korisnik plaća naknade samo prilikom svog prvog ulaska u bazen, što mu omogućava da učestvuje u mnoštvu remiksa bez dodatnih naknada. Novi učesnici su ti koji pokrivaju rudarske naknade za remiksere.


Sa svakim dodatnim coinjoin-om u kojem novčić učestvuje, zajedno sa svojim prethodno susretnutim parnjacima, skup anonimnosti (anonset) eksponencijalno raste. Cilj je, dakle, iskoristiti ove besplatne remikse koji, pri svakom pojavljivanju, doprinose jačanju gustine skupova anonimnosti (anonsetova) povezanih sa svakim pomešanim novčićem.


Whirlpool je dizajniran uzimajući u obzir dva važna zahteva:


- Pristupačnost implementacije na mobilnim uređajima, s obzirom na to da je Samourai novčanik prvenstveno aplikacija za pametne telefone;
- Brzina ciklusa remiksovanja za promovisanje značajnog povećanja anonseta.

Ove imperative su vodile programere Samourai novčanika u dizajnu Whirlpool-u, navodeći ih da ograniče broj učesnika po ciklusu. Premalo učesnika bi ugrozilo efikasnost CoinJoin-a, drastično smanjujući broj anonsetova generisanih svakim ciklusom, dok bi previše učesnika izazvalo probleme u upravljanju na mobilnim aplikacijama i ometalo tok ciklusa.

**Na kraju, nema potrebe imati veliki broj učesnika po CoinJoin-u na Whirlpool jer se anonseti postižu akumulacijom nekoliko ciklusa CoinJoin.**


[-> Saznajte više o Whirlpool anonsetima.](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)


### Bazeni i CoinJoin naknade

Da bi ovi višestruki ciklusi efikasno povećali anonsetove mešanih kovanica, mora se uspostaviti određeni okvir kako bi se ograničile količine UTXO koje se koriste. Whirlpool tako definiše različite bazene.


Bazen predstavlja grupu korisnika koji žele da mešaju UTXO-e zajedno, koji se slažu oko količine UTXO-a koju će koristiti za optimizaciju CoinJoin procesa. Svaki bazen određuje fiksnu količinu za UTXO, koju korisnik mora poštovati da bi učestvovao. Dakle, da biste izvršili coinjoins sa Whirlpool-om, potrebno je da izaberete bazen. Trenutno dostupni bazeni su sledeći:


- 0.5 bitcoina;
- 0.05 bitcoina;
- 0.01 bitcoina;
- 0.001 bitcoina (= 100,000 Sats).


Uključivanjem svojih bitkoina u pool, oni će biti podeljeni kako bi se generisali UTXO-i koji su potpuno homogeni sa onima drugih učesnika u pool-u. Svaki bazen ima maksimalno ograničenje; stoga, za iznose koji prelaze ovo ograničenje, bićete primorani ili da napravite dva odvojena unosa unutar istog bazena ili da se usmerite ka drugom bazenu sa većim iznosom:


| Bazen (bitcoin)| Maksimalan iznos po ulazu (bitcoin)|
|----------------|------------------------------------|
| 0.5            | 35                                 |
| 0.05           | 3.5                                |
| 0.01           | 0.7                                |
| 0.001          | 0.025                              |

Kao što je ranije pomenuto, UTXO se smatra da pripada bazenu kada je spreman za integraciju u CoinJoin. Međutim, to ne znači da korisnik gubi vlasništvo nad njim. **Kroz različite cikluse mešanja, zadržavate potpunu kontrolu nad vašim ključevima i, samim tim, vašim bitcoinima.** Ovo je ono što razlikuje tehniku CoinJoin od drugih centralizovanih tehnika mešanja.


Da biste ušli u CoinJoin bazen, moraju se platiti naknade za uslugu kao i rudarske naknade. Naknade za uslugu su fiksne za svaki bazen i namenjene su za kompenzaciju timova odgovornih za razvoj i održavanje Whirlpool-a.

Naknade za korišćenje Whirlpool-a plaćaju se samo jednom prilikom ulaska u bazen. Nakon ovog koraka, imate priliku da učestvujete u neograničenom broju remiksa bez dodatnih naknada. Ovde su trenutne fiksne naknade za svaki bazen:


| Bazen (bitcoin)| Ulazna naknada (bitcoin)  |
|----------------|---------------------------|
| 0.5            | 0.0175                    |
| 0.05           | 0.00175                   |
| 0.01           | 0.0005 (50,000 sats)      |
| 0.001          | 0.00005 (5,000 sats)      |


Ove naknade su u suštini ulaznica za odabrani bazen, bez obzira na iznos koji uložite u CoinJoin. Dakle, bilo da se pridružite bazenu 0.01 sa tačno 0.01 BTC ili uđete sa 0.5 BTC, naknade će ostati iste u apsolutnoj vrednosti.


Pre nego što pređe na coinjoin-e, korisnik ima izbor između 2 strategije:


- Odlučite se za manji bazen kako biste minimizirali naknade za uslugu, znajući da će zauzvrat dobiti nekoliko malih UTXO-a;
- Ili preferirate veći bazen, pristajući da platite veće naknade kako biste završili sa smanjenim brojem UTXO-a veće vrednosti.


Opšte se savetuje da se ne spajaju različiti mešani UTXO-ovi nakon CoinJoin ciklusa, jer to može ugroziti stečenu poverljivost, posebno zbog Common-Input-Ownership Heuristike (CIOH). Stoga, može biti mudro izabrati veći bazen, čak i ako to znači plaćanje više, kako bi se izbeglo previše izlaza sa malom vrednošću UTXO-a. Korisnik mora odvagati ove kompromise kako bi izabrao bazen koji mu odgovara.


Pored naknada za uslugu, mora se uzeti u obzir i rudarska naknada svojstvena svakoj Bitcoin transakciji. Kao korisnik Whirlpool-a, bićete obavezni da platite rudarsku naknade za pripremnu transakciju (`Tx0`) kao i za prvi CoinJoin. Svi naredni remiksi će biti besplatni, zahvaljujući Whirlpool modelu koji se oslanja na plaćanje novih učesnika.


Zaista, u svakom Whirlpool CoinJoin-u, dva korisnika među unosima su novi učesnici. Ostali unosi dolaze od remiksera. Kao rezultat toga, rudarske naknade za sve učesnike u transakciji pokrivaju ova dva nova učesnika, koji će zatim takođe imati koristi od besplatnih remiksa:

![coinjoin](assets/en/6.webp)

Zahvaljujući ovom sistemu naknada, Whirlpool se zaista razlikuje od drugih CoinJoin usluga jer anonseti UTXO-a nisu proporcionalni ceni koju plaća korisnik. Tako je moguće postići znatno visoke nivoe anonimnosti plaćanjem samo ulazne naknade za bazen i rudarske naknada za dve transakcije (`Tx0` i početno mešanje).

Važno je napomenuti da će korisnik takođe morati da pokrije rudarske naknade za povlačenje svojih UTXO-a iz bazena nakon završetka njihovih višestrukih coinjoin-a, osim ako nisu odabrali opciju `mix to`, koju ćemo razmotriti u tutorijalu ispod.


### Nalozi unutar HD novčanika koje koristi Whirlpool

Da biste izvršili CoinJoin putem Whirlpool-a, novčanik mora generisati nekoliko različitih naloga. Nalog, u kontekstu HD (*Hijerarhijski Deterministički*) novčanika, predstavlja deo potpuno izolovan od drugih, pri čemu se ova separacija dešava na trećem nivou dubine hijerarhije novčanika, odnosno na nivou `xpub`.


HD novčanik može teoretski da izvede do `2^(32/2)` različitih naloga. Početni nalog, koji se koristi podrazumevano na svim Bitcoin novčanicima, odgovara indeksu `0'`.


Za novčanike prilagođene Whirlpool-u, kao što su Samourai ili Sparrow, koriste se 4 naloga kako bi se zadovoljile potrebe CoinJoin procesa:


- Račun **depozita**, identifikovan indeksom `0'`;
- Račun **bad bank ili loša banka** (ili doxxic kusur), identifikovan indeksom `2 147 483 644'`;
- Nalog **premix**, identifikovan indeksom `2 147 483 645'`;
- Nalog **postmix**, identifikovan indeksom `2 147 483 646'`.


Svaki od ovih naloga ispunjava specifičnu funkciju unutar CoinJoin procesa.


Svi ovi nalozi su povezani sa jednim seed-om, što omogućava korisniku da povrati pristup svim svojim bitcoinima koristeći svoju frazu za oporavak i, ako je primenljivo, svoj passphrase. Međutim, neophodno je specificirati softveru, tokom ove operacije oporavka, različite indekse naloga koji su korišćeni.


Hajde sada da pogledamo različite faze Whirlpool CoinJoin-a unutar ovih naloga.


### Različite faze coinjoin-a na Whirlpool-u

**Faza 1: Tx0**

Polazna tačka svakog Whirlpool CoinJoin-a je **depozitni** račun. Ovaj račun je onaj koji automatski koristite kada kreirate novi Bitcoin novčanik. Ovaj račun mora biti kreditiran bitcoinima koje neko želi da meša.

`Tx0` predstavlja prvi korak u Whirlpool procesu mešanja. Cilj mu je da pripremi i izjednači UTXO za CoinJoin, tako što ih deli na jedinice koje odgovaraju količini odabranog bazena, kako bi se osigurala homogenost mešavine. Izjednačeni UTXO se zatim šalju na **premix** nalog. Što se tiče razlike koja ne može ući u bazen, ona se odvaja na poseban nalog: **bad bank** (ili "doxxic kusur").

Ova početna transakcija Tx0 takođe služi za plaćanje servisnih naknada koje se duguju koordinatoru mešanja. Za razliku od sledećih koraka, ova transakcija nije kolaborativna; korisnik stoga mora preuzeti sve rudarske naknade:

![coinjoin](assets/en/7.webp)


U ovom primeru transakcije `Tx0`, ulaz od `372,000 Sats` sa našeg **depozitnog** računa je podeljen na nekoliko izlaza UTXO, koji su raspoređeni na sledeći način:


- Iznos od `5,000 Sats` namenjen koordinatoru za usluge, koji odgovara ulasku u fond od `100,000 Sats`;
- Tri UTXO-a pripremljena za mešanje, preusmerena na naš **premix** nalog i registrovana kod koordinatora. Ovi UTXO-i su izjednačeni na `108,000 Sats` svaki, da pokriju rudarsku naknade za njihovo buduće početno mešanje;
- Višak koji ne može ući u bazen, jer je premali, smatra se toksičnim kusurom. On se šalje na svoj specifičan račun. Ovde, ova promena iznosi `40,000 Sats`;
- Konačno, postoji `3,000 Sats` koji ne predstavljaju izlaz, već su rudarske naknade neophodne za potvrdu `Tx0`.


Na primer, ovde je pravi Whirlpool Tx0 (nije od mene): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://Mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)


**Korak 2: Doxxic kusur**

Višak koji nije mogao biti integrisan u bazen, ovde ekvivalentan `40,000 Sats`, preusmeren je na račun **loše banke**, takođe nazvan "doxxic kusur", kako bi se osigurala stroga odvojenost od ostalih UTXO-a unutar novčanika.


Ovaj UTXO je opasan za privatnost korisnika, jer ne samo da je još uvek povezan sa svojom prošlošću, i stoga moguće sa identitetom svog vlasnika, već je dodatno zabeleženo da pripada korisniku koji je izvršio CoinJoin.

Ako se ovaj UTXO spoji sa mešovitim izlazima, izgubiće svu poverljivost stečenu tokom CoinJoin ciklusa, naročito zbog Common-Input-Ownership-Heuristic (CIOH). Ako se spoji sa drugim doxxic kusurima, korisnik rizikuje gubitak poverljivosti jer će to povezati različite ulaze CoinJoin ciklusa. Stoga se mora pažljivo rukovati. Način upravljanja ovim toksičnim UTXO biće detaljno opisan u poslednjem delu ovog članka, a budući tutorijali će pokriti ove metode detaljnije na PlanB Network.


**Korak 3: Početno mešanje**

Nakon što je `Tx0` završena, izjednačeni UTXO-i se šalju na **premix** nalog našeg novčanika, spremni da budu uvedeni u njihov prvi CoinJoin ciklus, koji se takođe naziva "početno mešanje". Ako, kao u našem primeru, `Tx0` generiše više UTXO-a za mešanje, svaki od njih će biti integrisan u zaseban početni CoinJoin.


Na kraju ovih prvih mešanja, **premix** nalog će biti prazan, dok će naši novčići, nakon plaćanja rudarskih naknada za ovaj prvi CoinJoin, biti prilagođeni tačno na iznos definisan odabranim bazenom. U našem primeru, naši početni UTXO-i od `108 000 Sats` biće smanjeni tačno na `100 000 Sats`.

![coinjoin](assets/en/8.webp)

**Korak 4: Remiksi**

Nakon početnog mešanja, UTXO-ovi se prenose na **postmix** nalog. Ovaj nalog prikuplja već pomešane UTXO-ove i one koji čekaju na ponovno mešanje. Kada je Whirlpool klijent aktivan, UTXO-ovi u **postmix** nalogu su automatski dostupni za ponovno mešanje i biće nasumično odabrani da učestvuju u ovim novim ciklusima.


Kao podsetnik, remiksi su tada 100% besplatni: nisu potrebne dodatne naknade za uslugu ili rudarske naknade. Održavanje UTXO-a na **postmix** računu tako održava njihovu vrednost netaknutom i istovremeno poboljšava njihove anonsete. Zato je važno omogućiti ovim kovanicama da učestvuju u više CoinJoin ciklusa. To vas strogo ništa ne košta, a povećava nivoe njihove anonimnosti.


Kada odlučite da potrošite mešane UTXO-e, možete to učiniti direktno sa ovog **postmix** naloga. Preporučljivo je da mešane UTXO-e držite na ovom nalogu kako biste iskoristili besplatne remikse i izbegli njihovo napuštanje Whirlpool kruga, što bi moglo smanjiti njihovu poverljivost.


Kao što ćemo videti u sledećem vodiču, postoji i opcija `mix to` koja nudi mogućnost automatskog slanja vaših mešanih novčića na drugi novčanik, kao što je hladni ili offline novčanik, nakon definisanog broja coinjoin-ova.

Nakon što smo pokrili teoriju, zaronimo u praksu uz vodič za korišćenje Whirlpool-a putem Android aplikacije Samourai novčanika!


## Uputstvo: CoinJoin Whirlpool na Samourai novčaniku

Postoji mnogo opcija za korišćenje Whirlpool-a. Ona koju želim da predstavim ovde je opcija Samourai novčanika (bez Dojo), open-source Bitcoin novčanik aplikacija na Androidu.


Mešanje na Samourai bez Dojo-a ima prednost što je prilično lako za rukovanje, brzo za postavljanje i ne zahteva drugi uređaj osim Android telefona i internet konekcije.


Međutim, ova metoda ima dva značajna nedostatka:


- Coinjoins će se dešavati samo kada je Samourai pokrenut u pozadini i povezan. To znači da, ako želite da mešate i ponovo mešate svoje bitkoine 24/7, morate stalno držati Samourai uključenim;
- Ako koristite Whirlpool sa Samourai novčanikom bez brige o povezivanju sopstvenog Dojo-a, vaša aplikacija će morati da se poveže na server koji održavaju Samourai timovi, i otkrićete `xpub` vašeg novčanika njima. Ovi anonimni delovi informacija su neophodni da bi vaša aplikacija pronašla vaše transakcije.


Idealno rešenje za prevazilaženje ovih ograničenja je da upravljate sopstvenim Dojo-om povezanim sa Whirlpool CLI instancom na vašem ličnom Bitcoin čvoru. Na ovaj način, izbeći ćete bilo kakvo curenje informacija i postići potpunu nezavisnost. Iako je tutorijal prikazan ispod koristan za određene ciljeve ili za početnike, da biste zaista optimizovali vašu CoinJoin sesiju, preporučuje se korišćenje sopstvenog Dojo-a. Detaljan vodič za postavljanje ove konfiguracije uskoro će biti dostupan na PlanB Network-u.


### Instaliranje Samourai novčanika

Da biste započeli, očigledno će vam trebati aplikacija Samourai novčanik. Možete je preuzeti direktno sa zvanične veb stranice koristeći APK, sa njihovog GitLab-a, ili sa Google Play Store-a.


### Kreiranje softverskog novčanika

Nakon instalacije softvera, potrebno je da nastavite sa kreiranjem Bitcoin novčanika na Samourai. Ako već imate jedan, možete direktno preći na sledeći korak.


Nakon otvaranja aplikacije, pritisnite plavo dugme `Start`. Zatim će vam biti zatraženo da odaberete lokaciju u datotekama vašeg telefona gde će biti sačuvana enkriptovana rezervna kopija vašeg novog novčanika.


![samourai](assets/notext/9.webp)

Aktivirajte Tor klikom na odgovarajući prekidač. U ovoj fazi, takođe imate opciju da izaberete specifičan Dojo. Međutim, u ovom uputstvu, nastavićemo sa podrazumevanim Dojo-om; tako da možete ostaviti opciju onemogućenu. Kada je Tor povezan, pritisnite dugme `Create a new Wallet`.

![samourai](assets/notext/10.webp)


Samourai novčanik vas zatim podstiče da postavite BIP39 passphrase. Ova dodatna lozinka je veoma važna jer direktno utiče na derivaciju vaših privatnih ključeva. Potencijalni gubitak ovog passphrase doveo bi do nemogućnosti pristupa vašim bitcoinima, čineći ih nepovratno izgubljenim. Da biste obnovili vaš Samourai novčanik, neophodno je imati i vašu frazu za oporavak od 12 reči i passphrase.


Stoga je neophodno odabrati robustan passphrase i napraviti jednu ili više fizičkih kopija, na papiru ili na metalnom mediju, kako biste osigurali sigurnost svojih bitkoina. Nakon što završite ove zadatke, označite polje `I am aware that in case of loss....`, zatim pritisnite dugme `NEXT`.


![samourai](assets/notext/11.webp)


Morate zatim definisati PIN kod koji se sastoji od 5 do 8 cifara. Ovaj kod će obezbediti pristup vašem novčaniku na vašem telefonu. Biće zatražen svaki put kada želite da otvorite Samourai aplikaciju. Odaberite jak PIN kod i obavezno sačuvajte rezervnu kopiju. Nakon toga, možete pritisnuti dugme `NEXT`.


![samourai](assets/notext/12.webp)


Samourai će vas pozvati da ponovo unesete svoj PIN kod radi potvrde. Unesite ga, zatim pritisnite `FINALIZE`.


![samourai](assets/notext/13.webp)


Zatim ćete pristupiti svojoj frazi za oporavak koja se sastoji od 12 reči. Ova fraza vam omogućava da povratite svoj novčanik sa prethodno unetim passphrase. Preporučuje se da napravite jednu ili više kopija ove fraze na fizičkom mediju, kao što je papir ili metalni materijal, kako biste osigurali sigurnost svojih bitkoina u slučaju problema.


Nakon pravljenja ovih rezervnih kopija, bićete preusmereni na interfjes vašeg novog Samourai novčanika.


![samourai](assets/notext/14.webp)


Nudi vam se da dobijete svoj PayNym Bot. Možete ga zatražiti ako želite, iako nije neophodan za naš vodič.


![samourai](assets/notext/15.webp)

Pre nego što nastavite sa primanjem bitkoina na ovaj novi novčanik, preporučuje se da ponovo proverite validnost vaših rezervnih kopija novčanika (passphrase i fraza za oporavak). Da biste verifikovali passphrase, možete odabrati ikonu vašeg PayNym Bota koja se nalazi u gornjem levom uglu ekrana, zatim pratite putanju:

```plaintext
Settings > Troubleshooting > Passphrase/backup test
```


Unesite svoj passphrase da izvršite verifikaciju.


![samourai](assets/notext/16.webp)


Samourai će potvrditi da li je validno.


![samourai](assets/notext/17.webp)


Da biste verifikovali vašu rezervnu kopiju fraze za oporavak, pristupite ikoni vašeg PayNym Bota, koja se nalazi u gornjem levom uglu ekrana, i pratite ovaj put:

```plaintext
Settings > Wallet > Show 12-word recovery phrase
```


Samourai će prikazati prozor sa vašom frazom za oporavak. Uverite se da se tačno poklapa sa vašom fizičkom rezervnom kopijom.


Da biste otišli korak dalje i obavili potpuni test oporavka, zabeležite neki ključni podatak svog novčanika, poput jednog od xpub-ova, a zatim izbrišite novčanik (pod uslovom da je i dalje prazan). Cilj je pokušati obnoviti ovaj prazan novčanik koristeći samo vaše fizičke rezervne kopije. Ako je obnova uspešna, to ukazuje da su vaše rezervne kopije validne i pouzdane.


### Primanje bitkoina

Nakon kreiranja vašeg novčanika, počećete sa jednim nalogom, identifikovanim indeksom `0'`. Ovo je **depozitni** nalog o kojem smo govorili u prethodnim delovima. Na ovaj nalog ćete morati da prebacite bitkoine namenjene za coinjoin transakcije.


Da biste to uradili, kliknite na plavi simbol `+` koji se nalazi u donjem desnom uglu ekrana.


![samourai](assets/notext/18.webp)


Zatim kliknite na zeleno dugme `Receive`.


![samourai](assets/notext/19.webp)


Samourai će automatski generisati novu praznu adresu za primanje bitkoina.


![samourai](assets/notext/20.webp)


Tu možete poslati bitkoine koje želite da izmiksujete.


![samourai](assets/notext/21.webp)


### Pravljenje Tx0

Kada je transakcija potvrđena, možemo započeti proces coinjoins. Da biste to uradili, kliknite na plavo dugme `+` u donjem desnom uglu ekrana.


![samourai](assets/notext/22.webp)


Zatim kliknite na `Whirlpool` u plavoj boji.


![samourai](assets/notext/23.webp)


Sačekajte dok se Whirlpool inicijalizuje i Samourai kreira potrebne naloge.


![samourai](assets/notext/24.webp)


Zatim ćete stići na početnu stranicu Whirlpool. Kliknite na `Start`.

![samourai](assets/notext/25.webp)

Izaberite UTXO sa **depozitnog** računa koji želite poslati u CoinJoin ciklusima, zatim kliknite na `Next`.


![samourai](assets/notext/26.webp)


U sledećem koraku, biće potrebno da izaberete nivo naknade koji ćete dodeliti `Tx0` za vaše prvo mešanje. Ovo podešavanje će odrediti brzinu kojom će vaš `Tx0` i vaš početni CoinJoin (ili početni coinjoins) biti potvrđeni. Imajte na umu da su rudarske naknade za `Tx0` i početni miks vaša odgovornost, ali nećete morati da plaćate rudarske naknade za naredne remikse. Imate izbor između opcija `Low`, `Normal`, ili `High`.


![samourai](assets/notext/27.webp)


U istom prozoru, imate opciju da izaberete bazen u koji ćete ući. S obzirom da sam inicijalno izabrao UTXO od `454,258 Sats`, moj jedini mogući izbor je bazen `100,000 Sats`. Ova stranica vam takođe prikazuje naknade za uslugu bazena, pored rudarskih naknada, što vam omogućava da znate ukupne troškove za ovaj CoinJoin ciklus. Ako vam sve odgovara, izaberite odgovarajući bazen i nastavite klikom na plavo dugme `VERIFY CYCLE DETAILS`.


![samourai](assets/notext/28.webp)


Zatim možete videti sve detalje vašeg CoinJoin ciklusa:


- broj UTXO-a koji će ući u bazen;
- različite nastale naknade;
- količina doxxic kusura...


Potvrdite informacije, zatim kliknite na zeleno dugme `START CYCLE`.


![samourai](assets/notext/29.webp)


Pojaviće se prozor koji vam nudi da označite toksični kusur nastao vašim ulaskom u CoinJoin ciklus kao "nepotrošiv". Odabirom `DA`, ovaj UTXO neće biti vidljiv u vašem novčaniku i ne može biti izabran za buduće transakcije. Međutim, ostaće dostupan na listi UTXO-a u vašem novčaniku, gde možete ručno promeniti njegov status. Preporučuje se da se odlučite za ovu opciju kako biste izbegli bilo kakvu grešku u rukovanju koja bi kasnije mogla ugroziti vašu privatnost. Ako izaberete `NE`, toksični kusur će ostati dostupan za korišćenje u vašem novčaniku. Ako želite da saznate više o upravljanju i korišćenju ovog toksičnog kusura, savetujem vam da pročitate poslednji deo ovog tutorijala.


![samourai](assets/notext/30.webp)


Samourai će zatim emitovati vašu Tx0.


![samourai](assets/notext/31.webp)


### Pravljenje coinjoin-a

Jednom kada je Tx0 emitovan, možete ga pronaći u kartici `Transactions` Whirlpool menija.


![samourai](assets/notext/32.webp)

Vaši UTXO-ovi spremni za mešanje nalaze se u kartici `Mixing in progress...`, koja odgovara nalogu **Premix**.

![samourai](assets/notext/33.webp)


Jednom kada `Tx0` bude potvrđena, vaši UTXO-ovi će biti automatski registrovani kod koordinatora, i početni miksevi će započeti sukcesivno na automatski način.


![samourai](assets/notext/34.webp)


Proverom kartice `Remixing`, koja odgovara nalogu **Postmix**, primetićete UTXO-e koji su rezultat početnih mešanja. Ovi novčići će ostati spremni za naknadno remiksovanje, koje neće izazvati dodatne troškove. Preporučujem da pogledate ovaj drugi članak kako biste saznali više o procesu remiksovanja i efikasnosti CoinJoin ciklusa: [REMIX - Whirlpool](https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa)


![samourai](assets/notext/35.webp)


Moguće je privremeno obustaviti remiksovanje UTXO-a pritiskom na dugme za pauzu koje se nalazi desno od njega. Da bi ponovo bio podoban za remiksovanje, jednostavno kliknite na isto dugme drugi put. Važno je napomenuti da samo jedan CoinJoin može biti izveden po korisniku i po bazenu istovremeno. Dakle, ako imate 6 UTXO-a od `100 000 Sats` spremnih za CoinJoin, samo jedan od njih može biti miksovan. Nakon miksovanja UTXO-a, Samourai novčanik nasumično bira novi UTXO iz vaše dostupnosti, kako bi diversifikovao i balansirao remiksovanje svake kovanice.


![samourai](assets/notext/36.webp)


Da biste osigurali kontinuiranu dostupnost vaših UTXO-a za remixovanje, potrebno je da Samourai aplikacija bude aktivna u pozadini. Trebalo bi da vidite obaveštenje na vašem telefonu koje potvrđuje da Whirlpool radi. Zatvaranje aplikacije ili isključivanje telefona će pauzirati coinjoin-ove.


### Završavanje coinjoin-a

Da biste potrošili svoje mešane bitkoine, idite na **Postmix** nalog označen kao `Remixing` u Whirlpool meniju kartica.


![samourai](assets/notext/37.webp)


Kliknite na plavi Whirlpool logo koji se nalazi u donjem desnom uglu.


![samourai](assets/notext/38.webp)


Zatim kliknite na `Spend Mixed UTXOs`.


![samourai](assets/notext/39.webp)


Zatim možete uneti adresu primaoca i iznos za slanje, na isti način kao i za bilo koju drugu transakciju napravljenu sa Samourai novčanikom. Plava pozadina označava da se sredstva troše sa Whirlpool računa, a ne sa **depozitnog** računa.


![samourai](assets/notext/40.webp)


Klikom na 3 male tačke u gornjem desnom uglu, imate opciju da izaberete specifične UTXO-e.

![samourai](assets/notext/41.webp)

Klikom na beli kvadrat u gornjem desnom uglu prozora, možete skenirati QR kod prijemne adrese sa vašom kamerom.


![samourai](assets/notext/42.webp)


Unesite potrebne informacije za vašu transakciju troškova, zatim kliknite na plavo dugme `VERIFY TRANSACTION`.


![samourai](assets/notext/43.webp)


U sledećem koraku, imate opciju da izmenite stopu naknade povezanu sa vašom transakcijom. Takođe možete omogućiti opciju Stonewall označavanjem odgovarajućeg polja. Ako opcija Stonewall nije dostupna za izbor, to znači da vaš **Postmix** nalog ne sadrži UTXO dovoljne veličine da podrži ovu specifičnu strukturu transakcije.


[-> Saznajte više o Stonewall transakcijama.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)


Ako je sve po vašoj želji, kliknite na zeleno dugme `POŠALJI ... BTC`.


![samourai](assets/notext/44.webp)


Samourai će zatim nastaviti sa potpisivanjem vaše transakcije pre nego što je emituje na mreži. Samo treba da sačekate da bude dodata u blok od strane rudara.


![samourai](assets/notext/45.webp)


### Korišćenje SCODE-a

Ponekad, timovi Samourai novčanika nude "SCODE-ove". SCODE je promotivni kod koji omogućava popust na naknade za usluge bazena. Samourai novčanik povremeno nudi takve kodove svojim korisnicima tokom posebnih događaja. Savetujem vam [da pratite Samourai novčanik](https://twitter.com/SamouraiWallet) na društvenim mrežama kako ne biste propustili buduće SCODE-ove.


Da biste primenili SCODE na Samourai, pre nego što započnete novi CoinJoin ciklus, idite na Whirlpool meni i izaberite tri male tačke koje se nalaze u gornjem desnom uglu ekrana.


![samourai](assets/notext/46.webp)


Kliknite na `SCODE (promo kod) Whirlpool`.


![samourai](assets/notext/47.webp)


Unesite SCODE u prozor koji se otvorio, zatim potvrdite klikom na `OK`.


![samourai](assets/notext/48.webp)


Whirlpool će se automatski zatvoriti. Sačekajte da se Samourai učita, a zatim ponovo otvorite Whirlpool meni.


![samourai](assets/notext/49.webp)


Uverite se da je vaš SCODE pravilno registrovan tako što ćete još jednom kliknuti na tri male tačke, a zatim odabrati `SCODE (promo kod) Whirlpool`. Ako je sve u redu, spremni ste da započnete novi Whirlpool ciklus sa popustom na naknade za uslugu. Važno je napomenuti da su ovi SCODE-ovi privremeni: ostaju važeći nekoliko dana pre nego što postanu zastareli.


## Kako znati kvalitet naših CoinJoin ciklusa?

Da bi CoinJoin bio zaista efikasan, neophodno je da pokaže dobru uniformnost između količina ulaza i izlaza. Ova uniformnost pojačava broj mogućih interpretacija u očima spoljnog posmatrača, čime se povećava neizvesnost u vezi sa transakcijom. Da bi se kvantifikovala ova neizvesnost generisana od strane CoinJoin, može se pribegavati izračunavanju entropije transakcije.


Za detaljnu analizu ovih indikatora (model Whirlpool je prepoznat kao onaj koji donosi najviše homogenosti u coinjoins), upućujem vas na tutorijal: [BOLTZMANN CALCULATOR](https://planb.network/tutorials/privacy/analysis/boltzmann-entropy-738e45af-18a6-4ce6-af1a-1bf58e15f1fe)


Dalje se procenjuje performanse nekoliko CoinJoin ciklusa na osnovu obima grupa u kojima je novčić skriven. Veličina ovih grupa definiše ono što se naziva anonsetima. Postoje dve vrste anonseta: prvi procenjuje privatnost dobijenu protiv retrospektivne analize (od sadašnjosti ka prošlosti) i drugi, protiv prospektivne analize (od prošlosti ka sadašnjosti). Za detaljno objašnjenje ova dva indikatora, pozivam vas da pogledate tutorijal: [Whirlpool STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)


## Kako upravljati postmixom?

Nakon izvođenja CoinJoin ciklusa, najbolja strategija je da zadržite svoje UTXO-ove na **postmix** računu, čekajući njihovu buduću upotrebu. Čak je preporučljivo da ih ostavite da se neograničeno remixuju dok ih ne budete trebali potrošiti.


Neki korisnici bi mogli razmotriti prebacivanje svojih mešanih bitkoina na hardverski novčanik. Ovo je moguće, ali je važno pažljivo pratiti preporuke Samourai novčanika kako se ne bi ugrozila stečena poverljivost.


Spajanje UTXO-a predstavlja najčešće napravljenu grešku. Neophodno je izbegavati kombinovanje mešanih UTXO-a sa nemesanim UTXO-ima u istoj transakciji, kako bi se izbegao CIOH (*Common-Input-Ownership-Heuristic*). Ovo zahteva pažljivo upravljanje vašim UTXO-ima unutar vašeg novčanika, posebno u smislu označavanja. Posle CoinJoin-a, spajanje UTXO-a je generalno loša praksa koja često dovodi do gubitka poverljivosti kada se ne upravlja pravilno.

Takođe treba da budete oprezni u vezi sa konsolidacijom mešanih UTXO-a jednih sa drugima. Umerene konsolidacije su moguće ako vaši mešani UTXO-i imaju značajne anonsete, ali će to neizbežno smanjiti privatnost vaših novčića. Osigurajte da konsolidacije nisu prevelike niti izvedene nakon nedovoljnog broja remiksa, jer to rizikuje uspostavljanje deduktivnih veza između vaših UTXO-a pre i posle CoinJoin ciklusa. U slučaju sumnje u vezi sa ovim operacijama, najbolja praksa je da ne konsolidujete postmix UTXO-e, već da ih prenosite jedan po jedan na vaš hardverski novčanik, generišući svaki put novu praznu adresu. Još jednom, zapamtite da pravilno označite svaki primljeni UTXO.


Takođe se savetuje da ne prebacujete svoje postmix UTXO-ove na novčanik koristeći neuobičajene skripte. Na primer, ako uđete u Whirlpool sa Multisig novčanikom koristeći `P2WSH` skripte, mala je verovatnoća da ćete biti pomešani sa drugim korisnicima koji imaju isti tip novčanika originalno. Ako izađete iz svog postmixa na ovaj isti Multisig novčanik, nivo privatnosti vaših pomešanih bitkoina će biti znatno smanjen. Pored skripti, postoje mnogi drugi identifikatori novčanika koji vas mogu prevariti.


Kao i kod svake Bitcoin transakcije, takođe je prikladno ne koristiti ponovo adrese za primanje. Svaka nova transakcija mora biti primljena na novoj praznoj adresi.


Najjednostavnije i najsigurnije rešenje je da pustite svoje mešane UTXO-ove da ostanu u njihovom **postmix** nalogu, dopuštajući im da se ponovo mešaju i dodirujući ih samo za trošenje. Samourai i Sparrow novčanici imaju dodatne zaštite protiv svih ovih rizika povezanih sa analizom lanca. Ove zaštite vam pomažu da izbegnete pravljenje grešaka.


## Kako upravljati doxxic kusurom?

Dalje, morate biti pažljivi u upravljanju doxxic kusurom, kusurom koje ne može ući u CoinJoin bazen. Ovi toksični UTXO-i, koji su rezultat korišćenja Whirlpool-a, predstavljaju rizik za vašu privatnost jer uspostavljaju vezu između vas i korišćenja CoinJoin-a. Stoga je neophodno rukovati njima sa oprezom i ne kombinovati ih sa drugim UTXO-ima, posebno mešanim UTXO-ima. Evo različitih strategija koje treba razmotriti za njihovu upotrebu:


- **Pomešajte ih u manjim bazenima:** Ako je vaš toksični UTXO dovoljno velik da sam uđe u manji bazen, razmislite o njegovom mešanju. Ovo je često najbolja opcija. Međutim, ključno je ne spajati nekoliko toksičnih UTXO-a da biste pristupili bazenu, jer to može povezati vaše različite unose.
- **Označite ih kao "nepotrošive":** Drugi pristup je da ih prestanete koristiti, označite ih kao "nepotrošive" na njihovom posebnom računu, i samo HODL. Ovo osigurava da ih slučajno ne potrošite. Ako vrednost bitcoina poraste, mogu se pojaviti novi bazeni koji su pogodniji za vaše toksične UTXO-e;
- **Dajte donacije:** Razmislite o davanju donacija, čak i skromnih, programerima koji rade na Bitcoin-u i pratećem softveru. Takođe možete donirati organizacijama koje prihvataju BTC. Ako vam upravljanje toksičnim UTXO-ima deluje previše komplikovano, jednostavno ih se možete rešiti donacijom;
- **Kupite poklon kartice:** Platforme kao što je [Bitrefill](https://www.bitrefill.com/) omogućavaju vam da zamenite bitkoine za poklon kartice koje se mogu koristiti kod različitih trgovaca. Ovo može biti način da se rešite svojih toksičnih UTXO-a bez gubitka povezane vrednosti;
- **Konsolidujte ih na Monero:** Samourai novčanik sada nudi uslugu atomskih zamena između BTC i XMR. Ovo je idealno za upravljanje toksičnim UTXO-ima konsolidovanjem na Monero, bez ugrožavanja vaše privatnosti putem KYC-a, pre nego što ih pošaljete nazad na Bitcoin. Međutim, ova opcija može biti skupa u smislu rudarske naknada i premije zbog ograničene likvidnosti;
- **Pošaljite ih na Lightning mrežu:** Prenošenje ovih UTXO-a na Lightning mrežu kako biste iskoristili smanjene naknade za transakcije može biti zanimljiva opcija. Međutim, ova metoda može otkriti određene informacije u zavisnosti od vaše upotrebe Lightning-a i stoga bi trebalo da se praktikuje sa oprezom.


Detaljni tutorijali o implementaciji ovih različitih tehnika uskoro će biti dostupni na PlanB Network.


**Dodatni resursi:**

[Samourai novčanik video tutorial](https://planb.network/tutorials/wallet/mobile/samourai-46f88b20-5d1e-47e0-be53-237ff8737956)


- [Samourai novčanik dokumentacija - Whirlpool](https://docs.samourai.io/Whirlpool/basic-concepts);
- [Niz na Twitteru o coinjoin-ima](https://twitter.com/SamouraiWallet/status/1489220847336308739);
- [Blog post on coinjoins](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin).
