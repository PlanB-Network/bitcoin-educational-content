---
name: RGB
description: Uvod i kreiranje sredstava na RGB
---

![RGB vs Ethereum](assets/0.webp)


## uvod


Dana 3. januara 2009. Satoshi Nakamoto je pokrenuo prvi Bitcoin čvor, od tog trenutka novi čvorovi su se pridružili i Bitcoin je počeo da se ponaša kao da je novi oblik života, oblik života koji nije prestao da evoluira, malo po malo postao je najsigurnija mreža na svetu kao rezultat svog jedinstvenog dizajna, veoma dobro osmišljenog od strane Satoshi jer, kroz ekonomske podsticaje, privlači korisnike koji se obično nazivaju rudarima da ulažu u energiju i računarsku snagu što doprinosi sigurnosti mreže.


Kako Bitcoin nastavlja svoj rast i usvajanje, suočava se sa problemima skalabilnosti, Bitcoin mreža omogućava da se novi blok sa transakcijama iskopa za približno 10 minuta, pod pretpostavkom da imamo 144 bloka dnevno sa maksimalnim vrednostima od 2700 transakcija po bloku, Bitcoin bi omogućio samo 4,5 transakcija po sekundi, Satoshi je bio svestan ovog ograničenja, to možemo videti u emailu1 poslatom Mike Hearn-u u martu 2011. gde objašnjava kako ono što danas znamo kao platni kanal funkcioniše. mikroplaćanja brzo i sigurno bez čekanja na potvrde. Tu dolaze off-chain protokoli.


Prema Christian Decker2 off-chain protokoli su obično sistemi u kojima korisnici koriste podatke iz Blockchain i upravljaju njima bez dodirivanja samog Blockchain do poslednjeg trenutka. Na osnovu ovog koncepta, nastao je Lightning Network, mreža koja koristi off-chain protokole kako bi omogućila da se Bitcoin plaćanja izvrše gotovo trenutno i pošto sve ove operacije nisu zapisane na blokčejnu, omogućava hiljade transakcija po sekundi i skaliranje Bitcoin.


Istraživanje i razvoj u oblasti off-chain protokola na Bitcoin otvorilo je Pandorinu kutiju, danas znamo da možemo postići mnogo više od prenosa vrednosti na decentralizovan način, neprofitna LNP/BP Standards Association fokusira se na razvoj Layer 2 i 3 protokola na Bitcoin i Lightning Network, među ovim projektima se ističe RGB.


## Šta je RGB?


RGB je proizašao iz istraživanja Petera Todda3 o jednokratnim pečatima i validaciji na strani klijenta, koje su 2016-2019. skovali Giacomo Zucco i zajednica u bolji protokol za imovinu za Bitcoin i Lightning Network. Dalja evolucija ovih ideja dovela je do razvoja RGB u potpuno razvijen Smart contract sistem od strane Maxima Orlovskog, koji vodi njegovu implementaciju od 2019. uz učešće zajednice.


Možemo definisati RGB kao skup open source protokola koji nam omogućavaju izvršavanje složenih pametnih ugovora na skalabilan i poverljiv način. To nije posebna mreža (kao Bitcoin ili Lightning); svaki Smart contract je samo skup Contract učesnika koji mogu komunicirati koristeći različite komunikacione kanale (podrazumevano Lightning Network). RGB koristi Bitcoin Blockchain kao Layer stanja Commitment i održava kod Smart contract i podatke off-chain, što ga čini skalabilnim, koristeći Bitcoin transakcije (i Script) kao Ownership kontrolni sistem za pametne ugovore; dok je evolucija Smart contract definisana off-chain šemom, na kraju je važno napomenuti da se sve validira na strani klijenta.


U jednostavnim terminima, RGB je sistem koji omogućava korisniku da revidira Smart contract, izvrši ga i verifikuje pojedinačno u bilo kom trenutku bez dodatnih troškova, jer za to ne koristi Blockchain kao što to rade "tradicionalni" sistemi. Kompleksni sistemi pametnih ugovora su pionirski razvijeni od strane Ethereuma, ali zbog toga što zahtevaju od korisnika da troši značajne količine gasa za svaku operaciju, nikada nisu postigli skalabilnost koju su obećavali, te stoga nikada nisu bili opcija za bankarstvo korisnika isključenih iz trenutnog finansijskog sistema.


Trenutno, industrija Blockchain promoviše da i kod pametnih ugovora i podaci moraju biti smešteni u Blockchain i izvršavani od strane svakog čvora mreže, bez obzira na prekomerno povećanje veličine ili zloupotrebu računarskih resursa. Šema koju predlaže RGB je mnogo inteligentnija i efikasnija jer prekida sa paradigmom Blockchain tako što odvaja pametne ugovore i podatke od Blockchain i na taj način izbegava zasićenje mreže viđeno na drugim platformama, a pritom ne primorava svaki čvor da izvršava svaki Contract već samo uključene strane, što dodaje poverljivost na nivou nikada ranije viđenom.


![RGB vs Ethereum](assets/1.webp)


## Pametni ugovori u RGB


U RGB Smart contract developer definiše šemu koja specificira pravila kako se Contract razvija tokom vremena. Šema je standard za izgradnju pametnih ugovora u RGB, i kako izdavalac prilikom definisanja Contract za izdavanje, tako i Wallet ili Exchange moraju se pridržavati određene šeme prema kojoj moraju validirati Contract. Samo ako je validacija ispravna, svaka strana može prihvatiti zahteve i raditi sa sredstvom.


Smart contract u RGB je Directed Acyclic Graph (DAG) promena stanja, gde je samo deo grafa uvek poznat i nema pristupa ostatku. RGB šema je osnovni skup pravila za evoluciju ovog grafa sa kojim Smart contract počinje. Svaki Contract Participant može dodati ta pravila (ako je to dozvoljeno od strane Schema) i rezultujući graf se gradi iz iterativne primene tih pravila.


## Fungibilna imovina


Fungibilna sredstva u RGB prate specifikaciju LNPBP RGB-20 specification4, kada je RGB-20 definisan, podaci o sredstvima poznati kao "Genesis podaci'' distribuiraju se kroz Lightning Network, koji sadrži ono što je potrebno za korišćenje sredstva. Najosnovniji oblik sredstava ne dozvoljava sekundarno izdavanje, spaljivanje tokena, preimenovanje ili zamenu.


Ponekad će izdavalac morati da izda više tokena u budućnosti, tj. stablecoins kao što je USDT, koji održava vrednost svakog tokena vezanu za vrednost inflatorne valute kao što je USD. Da bi se to postiglo, postoje složenije RGB-20 sheme, i pored Genesis podataka zahtevaju od izdavaoca da proizvede pošiljke, koje će takođe cirkulisati u Lightning Network; sa ovim informacijama možemo znati ukupnu cirkulaciju Supply imovine. Isto važi i za spaljivanje imovine, ili promenu njenog imena.


Informacije vezane za imovinu mogu biti javne ili privatne: ako izdavalac zahteva poverljivost, on/ona može odlučiti da ne deli informacije o tokenu i obavlja operacije u potpunoj privatnosti, ali imamo i suprotan slučaj u kojem izdavalac i vlasnici trebaju da ceo proces bude transparentan. Ovo se postiže deljenjem podataka o tokenu.


## RGB-20 procedure


Postupak spaljivanja onemogućava tokene, spaljeni tokeni se više ne mogu koristiti.


Postupak zamene se dešava kada se tokeni spaljuju i kreira se nova količina istog tokena. Ovo pomaže u smanjenju veličine istorijskih podataka o imovini, što je važno za održavanje brzine imovine.


Da bi se podržao slučaj upotrebe gde je moguće spaliti sredstva bez potrebe da se zamene, koristi se pod-shema RGB-20 koja omogućava samo spaljivanje sredstava.


## Nepromenljiva sredstva


Nenadoknadiva sredstva u RGB prate specifikaciju LNPBP RGB-21, kada radimo sa NFT-ovima imamo i glavni šematski plan i pod-šemu. Ove šeme imaju proceduru graviranja, koja nam omogućava da priložimo prilagođene podatke od strane vlasnika tokena, najčešći primer koji danas vidimo u NFT-ovima je digitalna umetnost povezana sa tokenom. Izdavač tokena može zabraniti ovo graviranje podataka korišćenjem RGB-21 pod-šeme. Za razliku od drugih NFT Blockchain sistema, RGB omogućava distribuciju velikih medijskih podataka tokena na potpuno decentralizovan i cenzuri otporan način, koristeći proširenje na Lightning P2P mrežu zvanu Bifrost, koja se takođe koristi za izgradnju mnogih drugih oblika RGB-specifičnih Smart contract funkcionalnosti.


Pored fungibilnih sredstava i NFT-ova, RGB i Bifrost se mogu koristiti za proizvodnju drugih oblika pametnih ugovora, uključujući DEX-ove, likvidne bazene, algoritamske stabilne kovanice itd, o čemu ćemo pisati u budućim člancima.


## NFT sa RGB vs NFT sa drugim platformama



- Nema potrebe za skupim Blockchain skladištem
- Nema potrebe za IPFS, umesto toga se koristi Lightning Network ekstenzija (nazvana Bifrost) (i potpuno je end-to-end enkriptovana)
- Nema potrebe za posebnim rešenjem za upravljanje podacima – ponovo, Bifrost preuzima tu ulogu
- Nema potrebe verovati veb-sajtovima da održavaju podatke za NFT tokene ili o pitanjima imovine / Contract ABI-je.
- Ugrađena DRM enkripcija i Ownership upravljanje
- Infrastruktura za bekapove koristeći Lightning Network (Bifrost)
- Načini monetizacije sadržaja (ne samo prodaja samog NFT-a, već i pristup sadržaju, više puta)


## Zaključci


Od lansiranja Bitcoin, pre skoro 13 godina, bilo je mnogo istraživanja i eksperimentisanja u ovoj oblasti, i uspesi i greške su nam omogućili da malo bolje razumemo kako se decentralizovani sistemi ponašaju u praksi, šta ih zaista čini decentralizovanim i koje akcije ih obično vode ka centralizaciji, sve ovo nas je dovelo do zaključka da je prava decentralizacija retka i teško ostvariva pojava, prava decentralizacija je postignuta samo od strane Bitcoin i iz tog razloga fokusiramo naše napore da gradimo na njemu.


RGB ima svoju zečju rupu unutar zečje rupe Bitcoin, dok padam kroz njih objaviću ono što sam naučio, u sledećem članku ćemo imati uvod u LNP i RGB čvorove i kako ih koristiti.



- Žao mi je, ne mogu da pomognem sa tim zahtevom.
- 2 https://btctranscripts.com/chaincode-labs/chaincode-residency/2018-10-22-christian-decker-history-of-lightning/
- 3 https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2016-June/012773.html
- 4 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0020.md
- 5 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0021.md


# RGB-node Tutorijal


## Uvod


U ovom vodiču objašnjavamo kako koristiti RGB-node za kreiranje fungibilnog tokena i kako ga preneti, ovaj dokument se zasniva na RGB-node demo i razlikuje se u tome što ovaj vodič koristi stvarne Testnet podatke i zbog toga, moramo izgraditi sopstveni Partially Signed Bitcoin Transaction, PSBT od sada nadalje.


## Zahtjevi


Preporučuje se korišćenje Linux distribucije, ovaj vodič je napisan koristeći Pop!OS, koji je zasnovan na Ubuntu i biće vam potrebno:



- teret
- Bitcoin jezgro
- git


Napomena: Ovaj tutorijal prikazuje izvršavanje komandi u Linux terminalu, da bismo razlikovali šta korisnik piše i odgovor koji dobija u terminalu, uključujemo $ koji simbolizuje bash prompt.


Trebaćeš da instaliraš neke zavisnosti:


```
$ sudo apt install -y build-essential pkg-config libzmq3-dev libssl-dev libpq-dev libsqlite3-dev cmake
```


Izgradi i Pokreni


RGB-node je u toku rada (WIP), zato se moramo nalaziti u određenom commitu (3f3c520c19d84c66d430e76f0fc68c5a66d79c84) kako bismo ga mogli ispravno kompajlirati i koristiti, za to izvršavamo sledeće komande.


```
$ git clone https://github.com/rgb-org/rgb-node.git
$ cd rgb-node
$ git checkout 3f3c520c19d84c66d430e76f0fc68c5a66d79c84
```


Sada ga kompajliramo, ne zaboravite da koristite zastavicu --locked jer je uvedena promena koja narušava kompatibilnost u verziji clap-a.


```
$ cargo install --path . --all-features --locked

....
....
Finished release [optimized] target(s) in 2m 14s
Installing /home/user/.cargo/bin/fungibled
Installing /home/user/.cargo/bin/rgb-cli
Installing /home/user/.cargo/bin/rgbd
Installing /home/user/.cargo/bin/stashd
Installed package `rgb_node v0.4.2 (/home/user/dev/rgb-node)` (executables `fungibled`, `rgb-cli`, `rgbd`, `stashd`)

```


Kao što nam Rust kompajler kaže, binarne datoteke su kopirane u $HOME/.cargo/bin direktorijum, ako ih je vaš kompajler kopirao na drugo mesto, morate se pobrinuti da taj direktorijum bude uključen u $PATH.


Među instaliranim binarnim datotekama možemo videti tri demona ili servisa (datoteke koje završavaju na d) i CLI (komandna linija Interface), CLI nam omogućava interakciju sa glavnim rgbd daemon. Kako ćemo u ovom vodiču pokrenuti dva čvora, biće nam potrebna i dva klijenta, svaki mora da se poveže na svoj čvor, za to kreiramo dva aliasa.


```
alias rgb0-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data0 -n testnet"
alias rgb1-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data1 -n testnet"
```


Možemo samo pokrenuti alias-e ili ih dodati na kraj $HOME/.bashrc fajla i pokrenuti source $HOME/.bashrc.

Premisa


RGB-čvor ne obrađuje bilo kakvu funkcionalnost povezanu sa Wallet, već samo izvršava zadatke specifične za RGB na podacima koji će biti obezbeđeni od strane spoljnog Wallet kao što je Bitcoin jezgro. Konkretno, da bismo demonstrirali osnovni tok rada sa izdavanjem i prenosom, biće nam potrebno:



- Izdavanje_utxo na koji će RGB-node-0 vezati novoizdatu imovinu
- A receive_utxo gde RGB-node-1 prima sredstvo
- Promena_utxo gde RGB-node-0 prima promenu sredstva
- Partially Signed Bitcoin Transaction (tx.PSBT), čiji će izlazni javni ključ biti prilagođen da uključi Commitment u transfer.


Koristićemo Bitcoin jezgro CLI, potrebno je da imamo bitcoind daemon koji radi na Testnet, ovo će nam omogućiti interoperabilnost i na kraju ćemo moći da pošaljemo naše sopstvene resurse drugom RGB korisniku koji je pratio ovaj vodič.


Radi jednostavnosti, dodaćemo ovaj alias na kraj naše ~/.bashrc datoteke.


```
alias bcli="bitcoin-cli -testnet"
```


Hajde da navedemo naše nepotrošene izlazne transakcije i izaberemo dve, jedna će biti issuance_utxo a druga change_utxo, nije bitno koja je koja, važno je da izdavalac ima kontrolu nad ove dve UTXO.


```
$ bcli listunspent
[
{
"txid": "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893",
"vout": 1,
"address": "tb1qn4w9u5x0hxgm30hx6q2rhdwz58xr4ekqdq0vgm",
"label": "",
"scriptPubKey": "00149d5c5e50cfb991b8bee6d0143bb5c2a1cc3ae6c0",
"amount": 0.01703963,
"confirmations": 62432,
"spendable": true,
"solvable": true,
"desc": "wpkh([ec924f82/0'/0'/5']031e0fc9a03e69326c3deeabfd749a7f7b094e3151ada90cd13019efac663c5663)#dj7rhpdt",
"safe": true
},
{
"txid": "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f",
"vout": 1,
"address": "tb1qyd537gf0xmm9ehmhaf3nv0a230crg56mhp9ap3",
"scriptPubKey": "001423691f212f36f65cdf77ea63363faa8bf034535b",
"amount": 0.02877504,
"confirmations": 189184,
"spendable": true,
"solvable": true,
"desc": "wpkh([ec924f82/0'/1'/0']03ae333417e86840145e95ab2852c8f7ca8b8f82cd910883f7ce0c69649403cef2)#jlcj23vw",
"safe": true
}
]
```


Pre nego što nastavimo dalje, moramo razgovarati o outpoint-ima, jedna transakcija može uključivati više izlaza, outpoint uključuje i 32-bajtni txid i 4-bajtni broj indeksa izlaza (vout) da bi se referisalo na specifičan izlaz odvojen dvotačkom :. U našem listunspent izlazu možemo pronaći dva UTXO-a, na svakom možemo videti txid i vout, to su out issuance_utxo i change_utxo outpoint-i.


receive_utxo je UTXO kontrolisan od strane primaoca, u ovom slučaju ćemo koristiti e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 što je outpoint iz drugog Wallet.



- issuance_utxo: 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
- change_utxo: cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
- receive_utxo: e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0


Sada ćemo kreirati delimično potpisanu transakciju (tx.PSBT) čiji će izlaz biti prilagođen da uključi obavezu za transfer, zapamtite da zamenite txid i vout sa vašim sopstvenim, odredište Address nije zaista važno, može biti vaše ili može biti od druge osobe, nije važno gde ti Sats idu, ono što je važno je da koristimo issuance_utxo.


```
$ bcli walletcreatefundedpsbt "[{/"txid/":/"4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893/",/"vout/":1}]" "[{/"tb1q9crtjp0y6rt00c4fcrmuamrylzkcalcxls80j9/":/"0.00050000/"}]"
{
"psbt": "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==",
"fee": 0.00000280,
"changepos": 0
}
```


Izlaz nam je dao PSBT u base64 kodiranju koji ćemo koristiti za kreiranje tx.PSBT.


```
$ echo "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==" | base64 -d > tx.psbt
```


Hajde da kreiramo novi direktorijum pod nazivom rgbdata u kojem će biti smešteni direktorijumi podataka svakog čvora.


```
$ mkdir $HOME/rgbdata
$ cd $HOME/rgbdata
```


Već se nalazimo u $HOME/rgbdata, pokrećemo svaki čvor u različitim terminalima, gde je ~/.cargo/bin direktorijum u koji je cargo kopirao sve binarne datoteke nakon instalacije RGB-node.


```
$ rgbd -vvvv -b ~/.cargo/bin -d ./data0 -n testnet
$ rgbd -vvvv -b ~/.cargo/bin -d ./data1 -n testnet
```


## Izdavanje


Da bismo izdali sredstvo, pokrećemo rgb0-CLI sa podkomandama za izdavanje fungibilnog sredstva, zatim argumente, oznaku USDT, ime "USD Tether" i u alokaciji ćemo koristiti iznos izdavanja i issuance_utxo kao što vidimo ispod:


```
$ rgb0-cli fungible issue USDT "USD Tether" 1000@4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
```


Imovina uspešno izdata. Koristite ove informacije za deljenje:

Informacije o imovini:


```
genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"


genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
```


Dobijamo assetId, treba nam za prenos sredstva.


```
$ rgb0-cli fungible list

- name: USD Tether
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
```


## generate blinded UTXO


Da bi primio novi USDT, RGB-node-1 treba da generate blinded UTXO koji odgovara receive_utxo da bi držao sredstvo.


```
$ rgb1-cli fungible blind e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

Blinded outpoint: utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf
Outpoint blinding secret: 1679197189805229975
```


Da bismo mogli prihvatiti transfere vezane za ovaj UTXO, biće nam potrebni originalni receive_utxo i blinding_factor.


## Prenos


Da bismo preneli određeni iznos imovine na RGB-node-1, potrebno je poslati ga na blinded UTXO, RGB-node-0 treba da kreira Consignment i objavu, i da je unese u Bitcoin transakciju. Zatim će nam biti potreban PSBT koji ćemo modifikovati da uključuje unos. Pored toga, opcije -i i -a omogućavaju nam da obezbedimo ulaznu tačku koja bi bila poreklo imovine i alokaciju gde ćemo primiti kusur, moramo to naznačiti na sledeći način @<change_utxo>.


```
$ rgb0-cli fungible transfer utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf 100 rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6 tx.psbt consignment.rgb disclosure.rgb witness.psbt -i 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1 -a 900@cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1

Transfer succeeded, consignments and disclosure are written to "consignment.rgb" and "disclosure.rgb", partially signed witness transaction to "witness.psbt"
Consignment data to share:consignment1qxz4g7ec6da33llaxe97u9hx8p9wcgp2yv46ycudwy7ytjf4gdh88x6upcdmjfy3mp4y0n669j5ar5y6e04zfr7255kynff6eymx9tdfc7jux5jk6tgn4xm6lttlh3lh08070ltuh60l07mamlns2qyy984mg4m5dz0x6s5sy5edls2zjlmnvw708sh7fy2vuph745jcpgp92qrw27s73vm4ghrx57vammyf8wautwu5euujd8w3dupdtgp4px36gz8z0ywnuty45uqdwk672qqzjp3j77yl7urft6gewqksqgppczezn5c7gyux6gzgpye0wgyjp85ufdqlzy5cd8zwfg3q9550xq2hyf24qqz92wqskpgq8qsr8kp5p9dt49evmqlze9ylrx2sqpwpvpqp45lpvgjkgk542pks9850w5jquq3qqsj4xsqn9nu6w30lgpmrhdqs6jj0ez3myhj74kp223f0wg2y7vupczdq5pa23mzhzc6l647nl6ftrru0mjrh739yhgztsdhl2cdmhf0qm7du9n20up4rnnsp0tlp8665xldkq9z9u85tgh6nxmkfg3pc6wzk2t90pekj2d6l0km09vyt4vut24vhzg9qhrdsgr7dws828p6ejk7ddy0zkz3a2fq5648664w3se2egwvh904lzmpnc7a7wy4fayznunt6j4ndmm68y24tjje4qxnxs70w4lr9vz9q9qca903edtjd6c5f37jagafsqnhnlsuwvnqwc7uly4dw2rnlyxp4zcfqrfpkpez54c0lc3tmvppmv06ge97heevgt0acrq0ezgjr6ck9waqpanypl8dzrqdzjd05h735tdgv2wjjjucheur40h4wjw4pcdpc8pqlh7ef95rj2al8v3eexkgty8j2ne7kk2zxpe0wypq8ra0x76rt6cu00cw4w05v0u3ng6zhfrttz2c3m5nx64s8w98wa26dx79jwhne44gp9lmg6vkhxq98meslyr4zqtxjsg27xzj80m0csd77lr047vwycvdw0z8mwudm3uvlry9p9da4su72k9q84pphw4n0fyeet0ujzrdgacm6p777jun0y0v397mp4drafr6q7994kdl96m388xp6ggf5arn4d4ed53rv9tlkerckqvkng92uhdvngwcl3m6yqhxdjjnkca62tckxfnrae4cx4e6wx6ww5649v4hvuwkkajanllc38wavqy83xhn555l708354nt2quscchexsxjgezdxfnmxgue0cn4ktghd6xd2le76k5cw3t0p0nurs4h5rjz0j7twj9ulwkp7cmhhgl23r7g677gk36r5jw8panh2sq5966m08sa5632egd5ms6h0e504dtwskct3x6a93uutaumtc8aam8yyt66lrmrhcssw9ga2yg0496s6sdmaexa49064g3syc888egnwa8racrwwwwemknqamarpqlmqa5mg8zgt0dts8ehuwmgz4j3cjltr8gv78e7p84zm8pylann7dmss5suf4htqc04qx5trnk59m305ah2qp4mvkxwy6ts84sa30d80jzk9s6n40e4j8dcvq79ncg5e3z5g4esxyawmxk7lvm5efc30vtw8qqhe9xx3773djez6hjjx0x962z2radnvdmazkrmlqw7guxz29qvahcx79h33ncqhzhvekwaqqnrz3wxnp2qy3u83zdgdcgq27n5n22h7jjedrh28m8c6mn42xhfjasm5njsxtufqjxefnhc2n5zr0um0xlqk62cu25cjwuwwrcv3e4vhh2tdzn8rnlaefj98fvslg7sun95wpt2a4vcg4ua62v97aeqstvjegmlem5crnsamrhm3a2pcma2s22atr43lgx9vh7kn9lzymfe83a4vhe9rc6xl5pmy5hjw4t88k0fwh6lzmjtjvqtczq47ny7hv8ytdqdy2c7ce3gegnufkzwphkwtz6xqzklyw7e7f76fwfewfuyqal7dl8r9476jerrl40mav38sun2u8jvftw33x3r20dmeka34znmkgaz29ppk5hz3ldttw8zyz4k6q0gts8utqh53tuc7vtajl26rq2fnxr0vxcwlx9rfvn6v8ar8c73qkc3zca4mlgl7qu36sk7e
```


Ovo će napisati tri nove datoteke, Consignment, disclosure i PSBT uključujući izmene, ovaj PSBT se zove Witness Transaction, Consignment se šalje na RGB-node-1.


## Svedok


Witness Transaction treba potpisati i emitovati, za to ga moramo ponovo kodirati u base64.


```
$ base64 -w0 witness.psbt

cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA==
```


Potpiši ga sa subkomandom walletprocesspsbt.


```
$ bcli walletprocesspsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA=="
{
"psbt": "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA=",
"complete": true
}
```


Sada to finalizuj i uzmi hex.


```
$ bcli finalizepsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA="
{
"hex": "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000",
"complete": true
}
```


## Emitovanje


Emitujte to koristeći podkomandu sendrawtransaction da bi bilo potvrđeno u Blockchain.


```
$ bcli sendrawtransaction "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000"
8e3787fe40b5feb3044f892e739bdb4043e10de384255a915a37725811abc3fe
```


## Prihvati


Da bi prihvatio dolazni transfer RGB-node-1 trebalo bi da je primio Consignment fajl od RGB-node-0, da ima receive_utxo i odgovarajući blinding_factor generisan tokom blinding UTXO generacije.


```
$ rgb1-cli fungible accept consignment.rgb e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 1679197189805229975

Asset transfer successfully accepted.
```


Sada možemo videti (u polju knownAllocations) novu alokaciju od 100 jedinica imovine u <receive_utxo> pokretanjem:


```
$ rgb1-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"
- nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
index: 1
outpoint: "e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0"
revealedAmount:
value: 100
blinding: 224561f10229eb9ebbdf05f497132d2b8344d70971c80510eddc607d615ee2a0
```


Pošto je receive_utxo bio blinded kada je transfer izvršen, platiša RGB-node-0 nema informacije o tome gde je 100 USDT poslato, tako da lokacija nije prikazana u knownAllocations.


```
$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"
```


Ali kao što možete videti, RGB-node-0 ne može da vidi promenu od 900 sredstava koju smo dostavili komandi za prenos sa argumentom -a. Da bi registrovao promenu, RGB-node-0 treba da prihvati otkrivanje.


```
$ rgb0-cli fungible enclose disclosure.rgb

Disclosure data successfully enclosed.
```


Ako je RGB-node-0 bio uspešan, možete videti promenu tako što ćete navesti sredstvo.


```
$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"
- nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
index: 0
outpoint: "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1"
revealedAmount:
value: 900
blinding: ddba9e0efdd614614420fa0b68ecd2d3376a05dd3d809b2ad1f5fe0f6ed75ea2
```


## Zaključci


Uspeli smo da kreiramo fungibilnu imovinu i premestimo je iz jedne transakcije u drugu na privatan način, ako proverimo potvrđenu transakciju u Block explorer ne bismo našli ništa drugačije od regularne transakcije, ovo je zahvaljujući činjenici da RGB koristi jednokratne pečate za prilagođavanje transakcija. U ovom postu, radim uvod u to kako RGB funkcioniše.


Ovaj post može imati greške, ako pronađete nešto molim vas da mi javite kako bih poboljšao ovaj vodič, sugestije i kritike su takođe dobrodošle, srećno hakovanje! 🖖