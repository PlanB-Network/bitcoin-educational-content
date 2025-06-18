---
name: RGB Lightning Node
description: Kako da pokrenem RGB-kompatibilni Lightning čvor sa RLN?
---
![cover](assets/cover.webp)


U ovom vodiču korak po korak, naučićete kako da postavite Lightning RGB čvor u Regtest okruženju. Videćemo kako da kreiramo RGB tokene i cirkulišemo ih u kanalima.


## Projekat RLN


Bitfinexov RGB tim radi od 2022. godine na obogaćivanju RGB ekosistema razvijanjem kompletne tehnološke platforme. Umesto da teži ka jednom komercijalnom proizvodu, njegovi napori su usmereni na omogućavanje dostupnosti open-source softverskih komponenti, doprinos specifikacijama RGB protokola i kreiranje referenci za implementaciju.


Među značajnim doprinosima Bitfinexa ekosistemu RGB nalazi se [*RGBlib* biblioteka](https://github.com/RGB-Tools/RGB-lib), napisana u Rust i dostupna putem veza u Kotlinu i Pythonu, koja uveliko pojednostavljuje razvoj RGB aplikacija enkapsulirajući složene mehanizme validacije i angažovanja.


Tim Bitfinex je takođe dizajnirao mobilni RGB Wallet, pod nazivom "[*Iris Wallet*](https://iriswallet.com/)", dostupan na Androidu. Ovaj Wallet integriše upotrebu RGB proxy servera za lako upravljanje off-chain razmenama podataka (*pošiljkama*) za *Client-side Validation* na RGB.


Bitfinex je takođe razvio projekat `RGB-lightning-node` (RLN). Ovo je Rust daemon zasnovan na Fork od `Rust-lightning` (LDK), modifikovan da uzme u obzir postojanje RGB sredstava u kanalu. Kada se kanal otvori, može se specificirati prisustvo RGB tokena, i svaki put kada se stanje kanala ažurira, kreira se State Transition koji odražava distribuciju tokena u Lightning izlazima. Ovo omogućava :




- Otvorite Lightning kanale u USDT, na primer;
- Usmerite ove tokene kroz mrežu, pod uslovom da rute imaju dovoljnu likvidnost;
- Iskoristi Lightning-ovu kaznenu i timelock logiku bez modifikacije: jednostavno Anchor tranziciju u dodatnom izlazu Commitment Transaction.


RLN kod je još uvek u alfa fazi: preporučujemo da ga koristite samo u **regtest** ili na **Testnet**.


## RGB protokol podsetnik


RGB je protokol koji radi na vrhu Bitcoin i emulira funkcionalnost Smart contract i upravljanje digitalnim sredstvima, bez preopterećenja Blockchain na kojem se zasniva. Za razliku od konvencionalnih On-Chain pametnih ugovora (kao na primer na Ethereum-u), RGB se oslanja na "*Client-side Validation*" sistem: većina podataka i istorija statusa se razmenjuje i skladišti isključivo od strane učesnika koji su uključeni, dok Bitcoin Blockchain samo hostuje male kriptografske obaveze (putem mehanizama kao što su *Tapret* ili *Opret*). U RGB protokolu, Bitcoin Blockchain stoga služi samo kao server za vremensko označavanje i sistem zaštite Double-spending.


RGB Contract je strukturiran kao evoluciona mašina stanja. Počinje sa Genesis koji definiše početno stanje (opisujući, na primer, Supply, oznaku ili druge metapodatke) prema strogo tipiziranom i kompajliranom Schema. Prelazi stanja i, ako je potrebno, proširenja stanja se zatim primenjuju da modifikuju ili prošire ovo stanje. Svaka operacija, bilo da se radi o prenosu fungibilnih sredstava (RGB20) ili kreiranju jedinstvenih sredstava (RGB21), uključuje *Jednokratne Pečate*. Oni povezuju Bitcoin UTXO-e sa off-chain stanjima i sprečavaju dvostruko trošenje, dok obezbeđuju poverljivost i skalabilnost.


Da biste saznali više o tome kako funkcioniše RGB protokol, preporučujem da pohađate ovaj sveobuhvatan kurs obuke:


https://planb.network/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

## Instalacija Lightning čvora kompatibilnog sa RGB


Da bismo kompajlirali i instalirali binarni fajl `RGB-lightning-node`, počinjemo kloniranjem repozitorijuma i njegovih podmodula, zatim pokrećemo:


```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```


![RLN](assets/fr/01.webp)




- Opcija `--recurse-submodules` takođe klonira neophodne pod-uređaje (uključujući modifikovanu verziju `Rust-lightning`);
- Opcija `--shallow-submodules` ograničava dubinu kloniranja kako bi se ubrzalo preuzimanje, dok i dalje omogućava pristup ključnim commit-ovima.


Iz korenskog direktorijuma projekta, pokrenite sledeću komandu da biste kompajlirali i instalirali binarni fajl :


```bash
cargo install --locked --debug --path .
```


![RLN](assets/fr/02.webp)




- `--locked` osigurava da se verzija zavisnosti poštuje;
- `--debug` nije obavezan, ali može vam pomoći da se fokusirate (možete koristiti `--release` ako više volite) ;
- `--path .` govori `cargo install` da instalira iz trenutnog direktorijuma.


Na kraju ove komande, izvršni fajl `RGB-lightning-node` biće dostupan u vašem `$CARGO_HOME/bin/`. Uverite se da je ova putanja u vašem `$PATH` kako biste mogli da pozovete komandu iz bilo kog direktorijuma.


## Preduuslovi


Da bi funkcionisao, `RGB-lightning-node` daemon zahteva prisustvo i konfiguraciju:




- Čvor `bitcoind`**


Svaka RLN instanca će morati komunicirati sa `bitcoind` kako bi emitovala i pratila svoje On-Chain transakcije. Autentifikacija (login/lozinka) i URL (host/port) će morati biti obezbeđeni za daemon.




- Indekser** (Electrum ili Esplora)


daemon mora biti u mogućnosti da navede i istraži On-Chain transakcije, posebno da pronađe UTXO na kojem je sredstvo usidreno. Moraćete da navedete URL vašeg Electrum servera ili Esplora.




- An RGB** proxy


Proxy server je komponenta (opciono, ali se toplo preporučuje) za pojednostavljenje Exchange od RGB *pošiljki* između Lightning vršnjaka. Još jednom, URL mora biti naveden.


ID-ovi i URL-ovi se unose kada je daemon *otključan* putem API-ja.


## Pokretanje regtesta


Za jednostavnu upotrebu, postoji skripta `regtest.sh` koja automatski pokreće, putem Dockera, skup servisa: `bitcoind`, `electrs` (indekser), `RGB-proxy-server`.


![RLN](assets/fr/03.webp)


Ovo vam omogućava pokretanje lokalnog, izolovanog, unapred konfigurisanog okruženja. Kreira i uništava kontejnere i direktorijume podataka pri svakom ponovnom pokretanju. Počećemo pokretanjem :


```bash
./regtest.sh start
```


Ovaj skript će :




- Kreirajte direktorijum `docker/` za čuvanje ;
- Pokreni `bitcoind` u regtest, kao i indeksator `electrs` i `RGB-proxy-server` ;
- Sačekajte dok sve ne bude spremno za korišćenje.


![RLN](assets/fr/04.webp)


Zatim ćemo pokrenuti nekoliko RLN čvorova. U posebnim terminalima pokrenite, na primer (za pokretanje 3 RLN čvora):


```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```


![RLN](assets/fr/05.webp)




- Parametar `--network regtest` označava korišćenje regtest konfiguracije;
- `--daemon-listening-port` označava na kom REST portu će Lightning čvor slušati za API pozive (JSON);
- `--ldk-peer-listening-port` specificira koji Lightning P2P port treba slušati;
- `dataldk0/`, `dataldk1/` su putanje do direktorijuma za skladištenje (svaki čvor skladišti svoje informacije zasebno).


Sada možete izvršavati komande na vašim RLN čvorovima iz vašeg pregledača, zahvaljujući API-ju. Konkretno, ovde možete *otključati* demone. Jednostavno otvorite pregledač na istom računaru kao i vaši čvorovi, i unesite URL :


```url
https://rgb-tools.github.io/rgb-lightning-node/
```


Da bi čvor otvorio kanal, prvo mora imati bitkoine na Address generisanom sledećom komandom (za čvor br. 1, na primer):


```bash
curl -X POST http://localhost:3001/address
```


Odgovor će vam pružiti Address.


![RLN](assets/fr/06.webp)


Na `bitcoind` Regtestu, kopaćemo nekoliko bitkoina. Pokreni :


```bash
./regtest.sh mine 101
```


![RLN](assets/fr/07.webp)


Pošalji sredstva na čvor Address generisan iznad:


```bash
./regtest.sh sendtoaddress <address> <amount>
```


![RLN](assets/fr/08.webp)


Zatim iskopaj blok da potvrdiš transakciju:


```bash
./regtest.sh mine 1
```


![RLN](assets/fr/09.webp)


## Testnet launch (without Docker)


Ako želite testirati realističniji scenarij, možete pokrenuti RLN čvorove na Testnet umesto u Regtest, usmeravajući ih ka javnim servisima ili servisima koje kontrolišete:


```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```


Podrazumevano, ako konfiguracija nije pronađena, daemon će pokušati da koristi:




- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-RPC`


Sa prijavom :




- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `password`


Takođe možete prilagoditi ove Elements putem `init`/`unlock` API-ja.


## Izdavanje RGB tokena


Da bismo izdali token, počećemo kreiranjem "bojivih" UTXO-a:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```


![RLN](assets/fr/10.webp)


Naravno, možete prilagoditi redosled. Da bismo potvrdili transakciju, mi iskopavamo :


```bash
./regtest.sh mine 1
```


Sada možemo kreirati RGB sredstvo. Komanda će zavisiti od tipa sredstva koje želite da kreirate i njegovih parametara. Ovde kreiram NIA (*Non Inflatable Asset*) token nazvan "PBN" sa Supply od 1000 jedinica. `precision` vam omogućava da definišete deljivost jedinica.


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "PBN",
"name": "Plan B Network",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```


![RLN](assets/fr/11.webp)


Odgovor uključuje ID novokreirane imovine. Zapamtite da zabeležite ovaj identifikator. U mom slučaju, to je:


```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```


![RLN](assets/fr/12.webp)


Zatim ga možete preneti na On-Chain ili ga alocirati u Lightning kanal. Upravo to ćemo uraditi u sledećem odeljku.


## Otvaranje kanala i prenos RGB sredstva


Prvo morate povezati svoj čvor sa peer-om na Lightning Network koristeći komandu `/connectpeer`. U mom primeru, kontrolišem oba čvora. Tako da ću preuzeti javni ključ mog drugog Lightning čvora sa ovom komandom:


```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```


Komanda vraća javni ključ mog čvora br. 2 :


```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```


![RLN](assets/fr/13.webp)


Dalje, otvorićemo kanal specificiranjem relevantne imovine (`PBN`). Komanda `/openchannel` vam omogućava da definišete veličinu kanala u satoshijima i opcionalno uključite imovinu RGB. Zavisi od toga šta želite da kreirate, ali u mom slučaju, komanda je :


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```


Saznajte više ovde:




- `peer_pubkey_and_opt_addr`: Identifikator čvora sa kojim želimo da se povežemo (javni ključ koji smo ranije pronašli);
- `capacity_sat`: Ukupni kapacitet kanala u satoshima ;
- `push_msat`: Iznos u milisatošijima koji se inicijalno prenosi vršnjaku kada se kanal otvori (ovde odmah prenosim 10,000 Sats kako bi on mogao kasnije da izvrši RGB prenos);
- `asset_amount`: Iznos RGB sredstava koja će biti posvećena kanalu ;
- `asset_id` : Jedinstveni identifikator RGB sredstva uključenog u kanal;
- `public`: Označava da li kanal treba da bude javan za rutiranje na mreži.


![RLN](assets/fr/14.webp)


Da bi se potvrdila transakcija, 6 blokova se rudari:


```bash
./regtest.sh mine 6
```


![RLN](assets/fr/15.webp)


Kanal Lightning je sada otvoren i takođe sadrži 500 `PBN` tokena na strani čvora n°1. Ako čvor n°2 želi da primi `PBN` tokene, mora generate i Invoice. Evo kako to uraditi:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```


Sa :




- `amt_msat`: Invoice iznos u milisatošima (minimum 3000 Sats) ;
- `expiry_sec` : Invoice vrijeme isteka u sekundama ;
- `asset_id` : Identifikator RGB sredstva povezanog sa Invoice ;
- `asset_amount`: Iznos RGB sredstva koje treba preneti sa ovim Invoice.


Kao odgovor, dobićete RGB Invoice:


```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```


![RLN](assets/fr/16.webp)


Sada ćemo platiti ovaj Invoice sa prvog čvora, koji drži potreban novac sa `PBN` tokenom:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```


![RLN](assets/fr/17.webp)


Plaćanje je izvršeno. Ovo se može proveriti izvršavanjem komande :


```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```


![RLN](assets/fr/18.webp)


Evo kako da implementirate Lightning čvor modifikovan za prenos RGB sredstava. Ova demonstracija se zasniva na :




- Regtest okruženje (putem `./regtest.sh`) ili Testnet ;
- Čvor za Lightning mrežu (`RGB-lightning-node`) zasnovan na `bitcoind`, indeksator i `RGB-proxy-server` ;
- Niz JSON REST API-ja za otvaranje/zatvaranje kanala, izdavanje tokena, prenos sredstava putem Lightning-a, itd.


Zahvaljujući ovom procesu :




- Transakcije angažovanja munje uključuju dodatni izlaz (OP_RETURN ili Taproot) sa sidrenjem RGB tranzicije;
- Transferi se obavljaju na potpuno isti način kao tradicionalna Lightning plaćanja, ali uz dodatak RGB tokena;
- Više RLN čvorova može biti povezano za usmeravanje i eksperimentisanje sa plaćanjima preko više čvorova, pod uslovom da postoji dovoljna likvidnost u bitkoinima i imovini RGB na putu.


Ako ste našli ovaj vodič korisnim, bio bih veoma zahvalan ako stavite Green palac dole. Slobodno podelite ovaj članak na vašim društvenim mrežama. Hvala vam puno!


Preporučujem i ovaj drugi vodič u kojem objašnjavam kako koristiti alat RGB CLI razvijen od strane LNP/BP udruženja za kreiranje RGB Contract:


https://planb.network/tutorials/node/others/rgb-cli-1f8a28d4-fa99-4261-9d80-48275b496fd4