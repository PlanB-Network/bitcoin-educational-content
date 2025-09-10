---
name: RGB
description: Uvod i kreiranje sredstava na RGB-u
---

![RGB vs Ethereum](assets/0.webp)


## uvod


Dana 3. januara 2009. Satoshi Nakamoto je pokrenuo prvi Bitcoin čvor, od tog trenutka novi čvorovi su se pridružili i Bitcoin je počeo da se ponaša kao da je novi oblik života, oblik života koji nije prestao da evoluira, malo po malo postao je najsigurnija mreža na svetu kao rezultat svog jedinstvenog dizajna, veoma dobro osmišljenog od strane Satoshija jer, kroz ekonomske podsticaje, privlači korisnike koji se obično nazivaju rudarima da ulažu u energiju i računarsku snagu što doprinosi sigurnosti mreže.


Kako Bitcoin nastavlja svoj rast i usvajanje, suočava se sa problemima skalabilnosti, Bitcoin mreža omogućava da se novi blok sa transakcijama iskopa za približno 10 minuta, pod pretpostavkom da imamo 144 bloka dnevno sa maksimalnim vrednostima od 2700 transakcija po bloku, Bitcoin bi omogućio samo 4,5 transakcija po sekundi, Satoshi je bio svestan ovog ograničenja, to možemo videti u emailu poslatom Mike Hearn-u u martu 2011. gde objašnjava kako ono što danas znamo kao platni kanal funkcioniše. mikroplaćanja brzo i sigurno bez čekanja na potvrde. Tu dolaze [off-chain](https://planb.network/resources/glossary/offchain) protokoli.


Prema Christian Deckeru off-chain protokoli su obično sistemi u kojima korisnici koriste podatke iz Blockchain-a i upravljaju njima bez dodirivanja samog Blockchain-a do poslednjeg trenutka. Na osnovu ovog koncepta, nastala je Lightning mreža, mreža koja koristi off-chain protokole kako bi omogućila da se Bitcoin plaćanja izvrše gotovo trenutno i pošto sve ove operacije nisu zapisane na blokčejnu, omogućava hiljade transakcija po sekundi i Bitcoin skaliranje.


Istraživanje i razvoj u oblasti off-chain protokola na Bitcoinu otvorili su Pandorinu kutiju; danas znamo da možemo postići mnogo više od samog prenosa vrednosti na decentralizovan način. Neprofitna organizacija LNP/BP Standards Association fokusira se na razvoj protokola drugog i trećeg sloja na Bitcoinu i Lightning mreži, a među tim projektima posebno se izdvaja RGB.


## Šta je RGB?

RGB je proizašao iz istraživanja Petera Todda o jednokratnim pečatima (single-use seals) i proveri na strani klijenta (client-side validation), koje su u periodu 2016–2019. Giacomo Zucco i zajednica razvili u napredniji protokol za tokene na Bitcoinu i Lightning mreži. Dalja evolucija ovih ideja dovela je do razvoja RGB-a u potpuno funkcionalan sistem pametnih ugovora, čiju implementaciju od 2019. predvodi Maksim Orlovski uz učešće zajednice.


RGB možemo definisati kao skup open-source protokola koji nam omogućavaju izvršavanje složenih pametnih ugovora na skalabilan i poverljiv način. To nije posebna mreža (poput Bitcoina ili Lightning mreže); svaki pametni ugovor je samo skup učesnika ugovora koji mogu međusobno komunicirati putem različitih komunikacionih kanala (podrazumevano preko Lightning mreže). RGB koristi Bitcoin blokčejn kao sloj za potvrdu stanja i održava kod pametnog ugovora i podatke van lanca (off-chain), što ga čini skalabilnim, koristeći Bitcoin transakcije (i Script) kao sistem kontrole vlasništva nad pametnim ugovorima; dok se evolucija pametnog ugovora definiše van lanca, na kraju je važno napomenuti da se sve proverava na strani klijenta.


Pojednostavljeno rečeno, RGB je sistem koji korisniku omogućava da u bilo kom trenutku pregleda pametni ugovor, izvrši ga i samostalno ga verifikuje, bez dodatnog troška, jer za to ne koristi blokčejn kao što to rade „tradicionalni“ sistemi. Ethereum je bio pionir složenih sistema pametnih ugovora, ali pošto zahteva da korisnik potroši značajne količine gasa za svaku operaciju, nikada nije postigao obećanu skalabilnost, pa samim tim nikada nije bio opcija za uključivanje korisnika isključenih iz postojećeg finansijskog sistema.


Trenutno blockchain industrija promoviše ideju da i kod pametnih ugovora i podaci moraju biti čuvani na blokčejnu i izvršavani od strane svakog čvora u mreži, bez obzira na prekomerno povećanje veličine ili neadekvatno korišćenje računarskih resursa. Šema koju predlaže RGB je znatno inteligentnija i efikasnija, jer prekida sa blokčejn paradigmom time što pametne ugovore i podatke odvaja od blokčejna i tako izbegava zagušenje mreže kakvo viđamo na drugim platformama. Istovremeno, ne primorava svaki čvor da izvršava svaki ugovor, već to rade samo uključene strane, čime se dodaje nivo poverljivosti kakav do sada nije postojao.


![RGB vs Ethereum](assets/1.webp)


## Pametni ugovori na RGB-u


U RGB pametnom ugovoru, programer definiše šemu koja određuje pravila po kojima se ugovor razvija tokom vremena. Šema predstavlja standard za izradu pametnih ugovora u RGB-u, i kako izdavalac prilikom definisanja ugovora za emisiju, tako i novčanik ili menjačnica moraju se pridržavati određene šeme prema kojoj validiraju ugovor. Samo ako je validacija ispravna, svaka strana može prihvatiti zahteve i raditi sa sredstvom.

Pametni ugovor u RGB-u je usmeren aciklični graf (DAG) promena stanja, pri čemu je uvek poznat samo deo grafa, dok ostatak nije dostupan. RGB šema je osnovni skup pravila od kojih pametni ugovor započinje svoj razvoj. Svaki učesnik ugovora može dodati ta pravila (ako je to dozvoljeno šemom), a nastali graf se gradi iterativnom primenom tih pravila.


## Zamenljiva sredstva


[Zamenljiva sredstva](https://planb.network/resources/glossary/fungibility) u RGB-u prate specifikaciju LNPBP RGB-20, kada je RGB-20 definisan, podaci o sredstvima poznati kao "početni podaci (genesis)" distribuiraju se kroz Lightning mrežu, koji sadrže ono što je potrebno za korišćenje sredstva. Najosnovniji oblik sredstava ne dozvoljava sekundarno izdavanje, spaljivanje tokena, preimenovanje ili zamenu.


Ponekad će izdavalac morati da izda više tokena u budućnosti, tj. stablecoins kao što je USDT, koji održava vrednost svakog tokena vezanu za vrednost inflatorne valute kao što je USD. Da bi se postigla ova složenija RGB-20 šema, pored početnih (genesis) podataka, zahteva se od izdavaoca da kreira consignmente (pošiljke), koji će takođe cirkulisati na Lightning mreži; sa ovim informacijama možemo znati ukupnu količinu sredstava u opticaju. Isto važi i za uništavanje (burning) sredstava ili promenu njihovog imena.


Informacije vezane za imovinu mogu biti javne ili privatne: ako izdavalac zahteva poverljivost, on/ona može odlučiti da ne deli informacije o tokenu i obavlja operacije u potpunoj privatnosti, ali imamo i suprotan slučaj u kojem izdavalac i vlasnici trebaju da ceo proces bude transparentan. Ovo se postiže deljenjem podataka o tokenu.


## RGB-20 procedure


Postupak spaljivanja onemogućava tokene, spaljeni tokeni se više ne mogu koristiti.


Postupak zamene se dešava kada se tokeni spaljuju i kreira se nova količina istog tokena. Ovo pomaže u smanjenju veličine istorijskih podataka o imovini, što je važno za održavanje brzine imovine.


Da bi se podržao slučaj upotrebe gde je moguće spaliti sredstva bez potrebe da se zamene, koristi se pod-shema RGB-20 koja omogućava samo spaljivanje sredstava.


## Nepromenljiva sredstva


Nenadoknadiva sredstva u RGB-u prate specifikaciju LNPBP RGB-21, kada radimo sa NFT-ovima imamo i glavni šematski plan i pod-šemu. Ove šeme imaju proceduru graviranja, koja nam omogućava da priložimo prilagođene podatke od strane vlasnika tokena, najčešći primer koji danas vidimo u NFT-ovima je digitalna umetnost povezana sa tokenom. Izdavalac tokena može zabraniti ovo graviranje podataka korišćenjem RGB-21 pod-šeme. Za razliku od drugih NFT blockchain sistema, RGB omogućava distribuciju medijskog sadržaja velikog formata koji je povezan sa tokenom na potpuno decentralizovan i na cenzuru otporan način, koristeći proširenje Lightning P2P mreže pod nazivom Bifrost, koje se takođe koristi za izgradnju mnogih drugih oblika RGB-specifičnih funkcionalnosti pametnih ugovora.


Pored zamenljivih sredstava i NFT-ova, RGB i Bifrost se mogu koristiti za proizvodnju drugih oblika pametnih ugovora, uključujući DEX-ove, likvidne bazene, algoritamske stabilne kovanice itd, o čemu ćemo pisati u budućim člancima.


## NFT u RGB-u u poređenju sa NFT-ovima na drugim platformama



- Nema potrebe za skupim Blockchain skladištem
- Nema potrebe za IPFS-om, umesto toga koristi se proširenje Lightning mreže (pod nazivom Bifrost) koje je u potpunosti šifrovano od kraja do kraja
- Nema potrebe za posebnim rešenjem za upravljanje podacima – ponovo, Bifrost preuzima tu ulogu
- Nema potrebe da se veruje veb-sajtovima da održavaju podatke za NFT tokene ili o izdatim sredstvima / ABI-jevima ugovora
- Ugrađena DRM enkripcija i upravljanje vlasništvom
- Infrastruktura za pravljenje rezervnih kopija pomoću Lightning mreže (Bifrost)
- Načini monetizacije sadržaja (ne samo prodaja samog NFT-a, već i pristup sadržaju, više puta)


## Zaključci


Od lansiranja Bitcoin-a, pre skoro 13 godina, bilo je mnogo istraživanja i eksperimentisanja u ovoj oblasti, i uspesi i greške su nam omogućili da malo bolje razumemo kako se decentralizovani sistemi ponašaju u praksi, šta ih zaista čini decentralizovanim i koje akcije ih obično vode ka centralizaciji, sve ovo nas je dovelo do zaključka da je prava decentralizacija retka i teško ostvariva pojava, prava decentralizacija je postignuta samo od strane Bitcoin-a i iz tog razloga fokusiramo naše napore da gradimo na njemu.


RGB ima svoju zečiju rupu unutar Bitcoin zečije rupe, dok padam kroz njih objaviću ono što sam naučio, u sledećem članku ćemo imati uvod u LNP i RGB čvorove i kako ih koristiti.



- 1 https://plan99.net/~mike/satoshi-emails/thread4.html
- 2 https://btctranscripts.com/chaincode-labs/chaincode-residency/2018-10-22-christian-decker-history-of-lightning/
- 3 https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2016-June/012773.html
- 4 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0020.md
- 5 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0021.md


# Tutorijal o RGB-čvoru 


## Uvod


U ovom vodiču objašnjavamo kako koristiti RGB-čvor za kreiranje zamenjivih tokena i kako ig preneti, ovaj dokument se zasniva na RGB-node demo i razlikuje se u tome što ovaj vodič koristi stvarne Testnet podatke i zbog toga, moramo izgraditi sopstvenu delimično potpisanu transakciju, na engleskom Partially Signed Bitcoin Transaction, PSBT od sada nadalje.


## Zahtevi


Preporučuje se korišćenje Linux distribucije, ovaj vodič je napisan koristeći Pop!OS, koji je zasnovan na Ubuntu i biće vam potrebno:



- cargo
- Bitcoin core
- git


Napomena: Ovaj tutorijal prikazuje izvršavanje komandi u Linux terminalu, da bismo razlikovali šta korisnik piše i odgovor koji dobija u terminalu, uključujemo $ koji simbolizuje bash prompt.


Trebaćeš da instaliraš neke zavisnosti:


```
$ sudo apt install -y build-essential pkg-config libzmq3-dev libssl-dev libpq-dev libsqlite3-dev cmake
```


Kompajliraj i pokreni


RGB-čvor je u toku rada (WIP), zato se moramo nalaziti u određenom commitu (3f3c520c19d84c66d430e76f0fc68c5a66d79c84) kako bismo ga mogli ispravno kompajlirati i koristiti, za to izvršavamo sledeće komande.


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


Među instaliranim binarnim datotekama možemo videti tri demona ili servisa (datoteke koje završavaju na d) i CLI (komandna linija), CLI nam omogućava interakciju sa glavnim rgbd daemon. Kako ćemo u ovom vodiču pokrenuti dva čvora, biće nam potrebna i dva klijenta, svaki mora da se poveže na svoj čvor, za to kreiramo dva aliasa.


```
alias rgb0-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data0 -n testnet"
alias rgb1-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data1 -n testnet"
```


Možemo samo pokrenuti alias-e ili ih dodati na kraj $HOME/.bashrc fajla i pokrenuti source $HOME/.bashrc.

Premisa


RGB-čvor ne obrađuje bilo kakvu funkcionalnost povezanu sa novčanikom, već samo izvršava zadatke specifične za RGB na podacima koji će biti obezbeđeni od strane spoljnog novčanika kao što je Bitcoin core. Konkretno, da bismo demonstrirali osnovni tok rada sa izdavanjem i prenosom, biće nam potrebno:



- issuance_utxo na koji će rgb-node-0 povezati (vezati) novoizdati aset.
- receive_utxo na koji će gde RGB-node-1 primati sredstvo
- change_utxo gde rgb-node-0 prima ostatak (change) aseta
- Delimično potpisana Bitcoin transakcija (tx.psbt) čiji će izlazni javni ključ biti prilagođen (tweaked) kako bi uključio obavezu (commitment) za prenos.


Koristićemo Bitcoin Core CLI i potrebno je da bitcoind daemon bude pokrenut na testnet mreži. Ovo će nam obezbediti interoperabilnost i na kraju ćemo moći da pošaljemo sopstvena sredstva drugom RGB korisniku koji je pratio ovaj tutorijal.


Radi jednostavnosti, dodaćemo ovaj alias na kraj naše ~/.bashrc datoteke.


```
alias bcli="bitcoin-cli -testnet"
```


Hajde da navedemo naše nepotrošene izlazne transakcije i izaberemo dve, jedna će biti issuance_utxo a druga change_utxo, nije bitno koja je koja, važno je da izdavalac ima kontrolu nad ova dva UTXO-a.


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


Pre nego što nastavimo dalje, moramo razgovarati o outpoint-ima, jedna transakcija može uključivati više izlaza, outpoint uključuje i 32-bajtni txid i 4-bajtni broj indeksa izlaza (vout) da bi se referisalo na specifičan izlaz odvojen dvotačkom :. U našem listunspent izlazu možemo pronaći dva UTXO-a, na svakom možemo videti txid i vout, to su izlazna issuance_utxo i change_utxo outpoint-i.


receive_utxo je UTXO kontrolisan od strane primaoca, u ovom slučaju ćemo koristiti e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 što je outpoint iz drugog novčanika.



- issuance_utxo: 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
- change_utxo: cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
- receive_utxo: e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0


Sada ćemo kreirati delimično potpisanu transakciju (tx.PSBT) čiji će izlaz biti prilagođen da uključi obavezu za transfer, zapamtite da zamenite txid i vout sa vašim sopstvenim, odredištna adresa nije zaista važna, može biti vaša ili može biti od druge osobe, nije važno gde ti Sats idu, ono što je važno je da koristimo issuance_utxo.


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


Već se nalazimo u $HOME/rgbdata, pokrećemo svaki čvor u različitim terminalima, gde je ~/.cargo/bin direktorijum u koji je cargo kopirao sve binarne datoteke nakon instalacije RGB-čvora.


```
$ rgbd -vvvv -b ~/.cargo/bin -d ./data0 -n testnet
$ rgbd -vvvv -b ~/.cargo/bin -d ./data1 -n testnet
```


## Izdavanje


Da bismo izdali sredstvo, pokrećemo rgb0-CLI sa podkomandama za izdavanje zamenjivih sredstva, zatim argumente, oznaku USDT, ime "USD Tether" i u alokaciji ćemo koristiti iznos izdavanja i issuance_utxo kao što vidimo ispod:


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


## Generiši zaslepljeni (eng. blinded) UTXO


Da bi primio novi USDT, RGB-node-1 treba da generiše zaslepljeni UTXO koji odgovara receive_utxo kako bi držao sredstvo.


```
$ rgb1-cli fungible blind e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

Blinded outpoint: utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf
Outpoint blinding secret: 1679197189805229975
```


Da bismo mogli prihvatiti transfere vezane za ovaj UTXO, biće nam potrebni originalni receive_utxo i blinding_factor.


## Prenos


Da bismo preneli određeni iznos imovine na RGB-node-1, potrebno je poslati ga na zaslepljeni UTXO, RGB-node-0 treba da kreira Consignment i objavu, i da je unese u Bitcoin transakciju. Zatim će nam biti potreban PSBT koji ćemo modifikovati da uključuje unos. Pored toga, opcije -i i -a omogućavaju nam da obezbedimo ulaznu tačku koja bi bila poreklo imovine i alokaciju gde ćemo primiti kusur, moramo to naznačiti na sledeći način @<change_utxo>.


```
$ rgb0-cli fungible transfer utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf 100 rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6 tx.psbt consignment.rgb disclosure.rgb witness.psbt -i 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1 -a 900@cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1

Transfer succeeded, consignments and disclosure are written to "consignment.rgb" and "disclosure.rgb", partially signed witness transaction to "witness.psbt"
Consignment data to share:consignment1qxz4g7ec6da33llaxe97u9hx8p9wcgp2yv46ycudwy7ytjf4gdh88x6upcdmjfy3mp4y0n669j5ar5y6e04zfr7255kynff6eymx9tdfc7jux5jk6tgn4xm6lttlh3lh08070ltuh60l07mamlns2qyy984mg4m5dz0x6s5sy5edls2zjlmnvw708sh7fy2vuph745jcpgp92qrw27s73vm4ghrx57vammyf8wautwu5euujd8w3dupdtgp4px36gz8z0ywnuty45uqdwk672qqzjp3j77yl7urft6gewqksqgppczezn5c7gyux6gzgpye0wgyjp85ufdqlzy5cd8zwfg3q9550xq2hyf24qqz92wqskpgq8qsr8kp5p9dt49evmqlze9ylrx2sqpwpvpqp45lpvgjkgk542pks9850w5jquq3qqsj4xsqn9nu6w30lgpmrhdqs6jj0ez3myhj74kp223f0wg2y7vupczdq5pa23mzhzc6l647nl6ftrru0mjrh739yhgztsdhl2cdmhf0qm7du9n20up4rnnsp0tlp8665xldkq9z9u85tgh6nxmkfg3pc6wzk2t90pekj2d6l0km09vyt4vut24vhzg9qhrdsgr7dws828p6ejk7ddy0zkz3a2fq5648664w3se2egwvh904lzmpnc7a7wy4fayznunt6j4ndmm68y24tjje4qxnxs70w4lr9vz9q9qca903edtjd6c5f37jagafsqnhnlsuwvnqwc7uly4dw2rnlyxp4zcfqrfpkpez54c0lc3tmvppmv06ge97heevgt0acrq0ezgjr6ck9waqpanypl8dzrqdzjd05h735tdgv2wjjjucheur40h4wjw4pcdpc8pqlh7ef95rj2al8v3eexkgty8j2ne7kk2zxpe0wypq8ra0x76rt6cu00cw4w05v0u3ng6zhfrttz2c3m5nx64s8w98wa26dx79jwhne44gp9lmg6vkhxq98meslyr4zqtxjsg27xzj80m0csd77lr047vwycvdw0z8mwudm3uvlry9p9da4su72k9q84pphw4n0fyeet0ujzrdgacm6p777jun0y0v397mp4drafr6q7994kdl96m388xp6ggf5arn4d4ed53rv9tlkerckqvkng92uhdvngwcl3m6yqhxdjjnkca62tckxfnrae4cx4e6wx6ww5649v4hvuwkkajanllc38wavqy83xhn555l708354nt2quscchexsxjgezdxfnmxgue0cn4ktghd6xd2le76k5cw3t0p0nurs4h5rjz0j7twj9ulwkp7cmhhgl23r7g677gk36r5jw8panh2sq5966m08sa5632egd5ms6h0e504dtwskct3x6a93uutaumtc8aam8yyt66lrmrhcssw9ga2yg0496s6sdmaexa49064g3syc888egnwa8racrwwwwemknqamarpqlmqa5mg8zgt0dts8ehuwmgz4j3cjltr8gv78e7p84zm8pylann7dmss5suf4htqc04qx5trnk59m305ah2qp4mvkxwy6ts84sa30d80jzk9s6n40e4j8dcvq79ncg5e3z5g4esxyawmxk7lvm5efc30vtw8qqhe9xx3773djez6hjjx0x962z2radnvdmazkrmlqw7guxz29qvahcx79h33ncqhzhvekwaqqnrz3wxnp2qy3u83zdgdcgq27n5n22h7jjedrh28m8c6mn42xhfjasm5njsxtufqjxefnhc2n5zr0um0xlqk62cu25cjwuwwrcv3e4vhh2tdzn8rnlaefj98fvslg7sun95wpt2a4vcg4ua62v97aeqstvjegmlem5crnsamrhm3a2pcma2s22atr43lgx9vh7kn9lzymfe83a4vhe9rc6xl5pmy5hjw4t88k0fwh6lzmjtjvqtczq47ny7hv8ytdqdy2c7ce3gegnufkzwphkwtz6xqzklyw7e7f76fwfewfuyqal7dl8r9476jerrl40mav38sun2u8jvftw33x3r20dmeka34znmkgaz29ppk5hz3ldttw8zyz4k6q0gts8utqh53tuc7vtajl26rq2fnxr0vxcwlx9rfvn6v8ar8c73qkc3zca4mlgl7qu36sk7e
```


Ovo će upisati tri nova fajla: consignment, disclosure i psbt koji uključuje izmenu (tweak). Ovaj psbt se naziva witness transakcija, a consignment se šalje ka rgb-node-1.


## Svedok transakcija (eng. witness transaction)


Witness Transaction treba potpisati i emitovati, za to je moramo ponovo kodirati u base64.


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


Emitujte to koristeći podkomandu sendrawtransaction da bi bilo potvrđeno u Blockchain-u.


```
$ bcli sendrawtransaction "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000"
8e3787fe40b5feb3044f892e739bdb4043e10de384255a915a37725811abc3fe
```


## Prihvati


Da bi prihvatio dolazni transfer, rgb-node-1 treba da je dobio fajl consignment od rgb-node-0, kao i receive_utxo i odgovarajući blinding_factor koji su generisani tokom procesa zaslepljivanja (eng. blinding) UTXO-a.


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


Pošto je receive_utxo bio zaslepljen (blinded) prilikom obavljanja transfera, platilac rgb-node-0 nema informaciju o tome gde je poslato 100 USDT, pa se lokacija ne prikazuje u knownAllocations.


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


Ali, kao što možete videti, rgb-node-0 ne može da vidi 900 jedinica promene sredstva (asset change) koje smo prosledili komandi za transfer pomoću argumenta -a. Da bi registrovao tu promenu, rgb-node-0 mora da prihvati disclosure.


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


Uspešno smo kreirali potpuno zamenljivo sredstvo i premestili ga iz jedne transakcije u drugu na privatan način. Ako proverimo potvrđenu transakciju u block explorer-u, ne bismo primetili ništa drugačije u odnosu na običnu transakciju, zahvaljujući tome što RGB koristi jednokratne pečate (single-use seals) za izmenu (tweak) transakcija. U ovom tekstu dajem uvod u način na koji RGB funkcioniše.


Ovaj post može imati greške, ako pronađete nešto molim vas da mi javite kako bih poboljšao ovaj vodič, sugestije i kritike su takođe dobrodošle, srećno hakovanje! 🖖
