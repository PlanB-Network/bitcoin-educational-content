---
name: RGB CLI
description: Kako da kreiram i razmenim pametne ugovore na RGB-u?
---
![cover](assets/cover.webp)


U ovom vodiču, pratićemo korak-po-korak proces pisanja ugovora, koristeći alatku `RGB komandne linije` koju je kreirala LNP/BP asocijacija. Cilj je da se pokaže kako da se instalira i koristi CLI, kompajlira šema, uveze interfejs i implementacija interfejsa, a zatim izda RGB sredstvo (asset). Takođe ćemo pogledati osnovnu logiku, uključujući kompajlaciju i validaciju stanja. Na kraju ovog vodiča, trebali biste biti u mogućnosti da reprodukujete proces i kreirate svoje RGB ugovore.


## Podsetnik RGB protokola


RGB je protokol koji se nadograđuje na Bitcoin i oponaša funkcionalnost pametnih ugovora i upravljanje digitalnom imovinom, bez preopterećivanja blokčejna na kojem je zasnovan. Za razliku od konvencionalnih on-chain pametnih ugovora (kao na primer na Ethereumu), RGB se oslanja na "*Client-side Validation*" sistem: većina podataka i istorija statusa razmenjuju se i skladište isključivo od strane uključenih učesnika, dok Bitcoin Blockchain samo hostuje male kriptografske obaveze (putem mehanizama kao što su *Tapret* ili *Opret*). U RGB protokolu, Bitcoin Blockchain stoga služi samo kao server za vremensko označavanje i sistem zaštite od duple potrošnje (eng. double-spending).


RGB ugovor je strukturiran kao evoluciona mašina stanja. Počinje sa Genesis koji definiše početno stanje (opisujući, na primer, ponudu, oznaku ili druge metapodatke) prema strogo tipiziranom i kompajliranom šemom. Prelazi stanja i, ako je potrebno, proširenja stanja se zatim primenjuju kako bi se modifikovalo ili proširilo ovo stanje. Svaka operacija, bilo da se radi o prenosu zamenjivih sredstava (RGB20) ili kreiranju jedinstvenih sredstava (RGB21), uključuje *Jednokratne Pečate (eng. Single-use Seals)*. Oni povezuju Bitcoin UTXO-e sa off-chain stanjima i sprečavaju dvostruko trošenje, dok obezbeđuju poverljivost i skalabilnost.


Da biste saznali više o tome kako funkcioniše RGB protokol, preporučujem da pohađate ovaj sveobuhvatni kurs obuke:


https://planb.network/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

Interna logika RGB zasnovana je na Rust bibliotekama koje vi, kao programeri, možete uvesti u svoje projekte kako biste upravljali *Client-side Validation* delom. Pored toga, LNP/BP tim radi na povezivanju za druge jezike, ali to još nije završeno. Pored toga, druge entitete kao što je Bitfinex razvijaju svoje sopstvene integracione stekove, ali o njima ćemo govoriti u nekom drugom tutorijalu. Za sada, `RGB` CLI je zvanična referenca, čak i ako ostaje relativno neizbrušena.


## Instalacija i prezentacija RGB CLI alata 


Glavna komanda se jednostavno zove `RGB`. Dizajnirana je da podseća na `git`, sa skupom podkomandi za manipulaciju ugovorima, njihovo pokretanje, izdavanje sredstava i slično. Bitcoin novčsnik trenutno nije integrisan, ali će biti u predstojećoj verziji (0.11). Ova sledeća verzija će omogućiti korisnicima da kreiraju i upravljaju svojim novčanicima (putem deskriptora) direktno iz `RGB`, uključujući generisanje PSBT, kompatibilnost sa eksternim hardverom (npr. hardverskim novčanikom) za potpisivanje, i interoperabilnost sa softverom kao što je Sparrow. Ovo će pojednostaviti čitav scenario izdavanja i prenosa sredstava.


### Instalacija putem Cargo-a


Alat instaliramo u Rustu pomoću:


```bash
cargo install rgb-contracts --all-features
```


(Napomena: Biblioteka (crate) se zove `RGB-contracts`, a instalirana komanda će biti nazvana `RGB`. Ako je biblioteka pod imenom `RGB` već postojala, moglo je doći do kolizije, stoga je naziv takav)


Instalacija kompajlira veliki broj zavisnosti (npr. parsiranje komandi, integracija sa Electrum-om, upravljanje zero-knowledge dokazima, itd.).


Kada je instalacija završena, :


```bash
rgb
```


Pokretanje `RGB` (bez argumenata) prikazuje listu dostupnih pod-komandi, kao što su `interfaces`, `Schema`, `import`, `export`, `issue`, `Invoice`, `transfer`, itd. Možete promeniti lokalni direktorijum za skladištenje (stash koji sadrži sve logove, šeme i implementacije), izabrati mrežu (Testnet, Mainnet) ili konfigurisati vaš Electrum server.


![RGB-CLI](assets/fr/01.webp)


### Prvi pregled kontrola


Kada pokrenete sledeću komandu, videćete da je `RGB20` interfejs već integrisan po defaultu:


```bash
rgb interfaces
```


Ako ovaj interfejs nije integrisan, kloniraj :


```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```


Sastavi ga:


```bash
cargo run
```


Zatim uvezite interfejs po vašem izboru:


```bash
rgb import interfaces/RGB20.rgb
```


![RGB-CLI](assets/fr/02.webp)


Međutim, obavešteni smo da nijedna šema još nije uvezena u softver. Takođe, u stash-u nema ugovora. Da biste to proverili, pokrenite komandu:

```bash
rgb schemata
```


Zatim možete klonirati repozitorijum da biste preuzeli određene šeme:


```bash
git clone https://github.com/RGB-WG/rgb-schemata
```


![RGB-CLI](assets/fr/03.webp)


Ovaj repozitorijum sadrži, u svom src/ direktorijumu, nekoliko Rust fajlova (na primer nia.rs) koji definišu šeme (NIA – Non Inflatable Asset, UDA – Unique Digital Asset, itd.). Za kompajliranje, zatim možete pokrenuti:


```bash
cd rgb-schemata
cargo run
```


Ovo generiše nekoliko `.RGB` i `.rgba` fajlova koji odgovaraju kompajliranim šemama. Na primer, naći ćete `NonInflatableAsset.RGB`.


### Uvoz šeme i implementacije interfejsa


Sada možete uvesti šemu u `RGB`:


```bash
rgb import schemata/NonInflatableAssets.rgb
```


![RGB-CLI](assets/fr/04.webp)


Ovo ga dodaje lokalnom stash-u. Ako pokrenemo sledeću komandu, vidimo da se sada pojavljuje Schema:


```bash
rgb schemata
```


## Kreiranje ugovora (izdavanje)


Postoje dva pristupa kreiranju nove imovine:




- Ili koristimo skriptu ili kod u Rustu koji gradi ugovor (eng. Contract) popunjavanjem šema (eng. Schema) polja (Global State, Owned States, itd.) i proizvodi `.RGB` ili `.rgba` fajl;
- Ili direktno koristite podkomandu `issue`, sa YAML (ili TOML) fajlom koji opisuje svojstva tokena.


Možete pronaći primere u Rustu u fascikli `examples`, koji ilustruju kako izgraditi `ContractBuilder`, popuniti `Global State` (ime imovine, oznaka, Supply (ukupna ponuda), datum, itd.), odrediti [vlasničko stanje (eng. Owned State)](https://planb.network/resources/glossary/owned-state) (kojem UTXO-u pripada), zatim sve to kompajlirati u *Contract Consignment* koji možete izvesti, validirati i uvesti u stash.


Drugi način je ručno uređivanje YAML datoteke izmenom `ticker`, `name`, `Supply`, i tako dalje. Pretpostavimo da se datoteka zove `RGB20-demo.yaml`. Možete navesti :




- `spec`: oznaka, ime, preciznost ;
- `terms`: polje za pravna obaveštenja ;
- `issuedSupply` : iznos izdatog tokena ;
- `assignments`: označava Single-Use Seal (*Seal Definition*) i količinu koja je otključana.


Evo primera YAML datoteka za kreiranje:


```yaml
interface: RGB20Fixed
globals:
spec:
ticker: PBN
name: Plan B Network
details: "Pay attention: the asset has no value"
precision: 2
terms:
text: >
SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
media: ~
issuedSupply: 100000000
assignments:
assetOwner:
seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
amount: 100000000 # this is 1 million (we have two digits for cents)
```


![RGB-CLI](assets/fr/05.webp)


Zatim jednostavno pokrenite komandu :


```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```


![RGB-CLI](assets/fr/06.webp)


U mom slučaju, jedinstveni Schema identifikator (koji treba staviti u jednostruke navodnike) je `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` i nisam naveo izdavaoca. Dakle, moja narudžba je :


```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```


Ako ne znate Schema ID, pokrenite komandu :


```bash
rgb schemata
```


CLI odgovara da je novi [Contract](https://planb.network/resources/glossary/contrat-rgb) izdat i dodat u stash. Ako unesemo sledeću komandu, vidimo da sada postoji dodatni Contract, koji odgovara upravo izdatom:


```bash
rgb contracts
```


![RGB-CLI](assets/fr/07.webp)


Zatim, sledeća komanda prikazuje globalna stanja (ime, oznaka, Supply...) i listu [Owned States](https://planb.network/resources/glossary/owned-state), tj. alokacije (na primer, 1 milion `PBN` tokena definisanih UTXO-om `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`).


```bash
rgb state '<ContractId>'
```


![RGB-CLI](assets/fr/08.webp)


## Izvoz, uvoz i validacija


Da biste podelili ovaj Contract sa drugim korisnicima, može se izvesti iz stasha:


```bash
rgb export '<ContractId>' myContractPBN.rgb
```


![RGB-CLI](assets/fr/09.webp)


Datoteku `myContractPBN.RGB` može proslediti drugom korisniku, koji je može dodati svom stashu sa komandom :


```bash
rgb import myContractPBN.rgb
```


Na uvozu, ako je jednostavno *Contract Consignment*, dobićemo poruku "`Importing Consignment RGB`". Ako je veći *State Transition Consignment*, komanda će biti drugačija (`RGB accept`).


Da biste osigurali validnost, možete koristiti i lokalnu funkciju validacije. Na primer, možete pokrenuti :


```bash
rgb validate myContract.rgb
```


### Korišćenje, verifikacija i prikaz Stash-a


Kao podsetnik, Stash je lokalni inventar šema, interfejsa, implementacija i ugovora (Genesis + tranzicije). Svaki put kada pokrenete "import", dodajete element u Stash. Ovaj Stash se može detaljno pregledati komandom :


```bash
rgb dump
```


![RGB-CLI](assets/fr/10.webp)


Ovo će generate fasciklu sa detaljima celog Stash.


## Transfer i PSBT


Da biste izvršili transfer, potrebno je manipulisati lokalnim Bitcoin novčanikom da biste upravljali obavezama `Tapret` ili `Opret`.


### Generisanje fakture


U većini slučajeva, interakcija između učesnika u ugovoru (npr. Alice i Bob) odvija se putem generisanja fakture. Ako Alisa želi da Bob izvrši nešto (prenos tokena, ponovno izdavanje, akciju u DAO, itd.), Alisa kreira fakturu sa detaljima svojih instrukcija za Boba. Tako imamo :




- **Alisa** (izdavalac fakture) ;
- **Bob** (koji prima i izvršava fakturu).


Za razliku od drugih ekosistema, RGB faktura nije ograničena na pojam plaćanja. Može ugraditi bilo koji zahtev povezan sa ugovorom: opozvati ključ, glasati, kreirati gravuru (*gravura*) na NFT-u, itd. Odgovarajuća operacija može biti opisana u interfejsu ugovora.


Sledeća komanda generiše RGB fakturu:


```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```


Gde je:




- `$Contract`: Identifikator ugovora(*ContractId*) ;
- `$Interface`: Interface koji se koristi (npr. `RGB20`) ;
- `$ACTION`: naziv operacije navedene u interfjesu (za jednostavan prenos zamenljivog tokena, to može biti "Transfer"). Ako interfejs već pruža podrazumevanu akciju, ne morate je ponovo unositi ovde;
- `$STATE`: status podataka koji treba preneti (na primer, količina tokena ako se prenosi zamenljivi token);
- `$Seal`: korisnikov (Alisin) Single-Use Seal, tj. eksplicitna referenca na UTXO. Bob će koristiti ove informacije da izgradi Witness Transaction, a odgovarajući izlaz će zatim pripadati Alisi (u *blinded UTXO* ili nešifrovanom obliku).


Na primer, sa sledećim komandama


```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```


CLI će generate i fakturu kao:


```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```


Može se preneti Bobu putem bilo kog kanala (tekst, QR kod, itd.).


### Pravljenje transfera


Da biste izvršili transfer uz pomoć ove fakture:




- Bob (koji drži tokene u svom Stash) ima Bitcoin novčanik. On treba da pripremi Bitcoin transakciju (u obliku PSBT, npr. `tx.PSBT`) koja troši UTXO-e gde se nalaze potrebni RGB tokeni, plus jedan UTXO za valutu (Exchange) ;
- Bob izvršava sledeću komandu:


```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```




- Ovo generiše datoteku `Consignment.RGB` koja sadrži :
 - Istorija prelaza koja dokazuje Alisi da su tokeni autentični;
 - Nova tranzicija koja prenosi tokene na Alisin Single-Use Seal ;
 - Witness Transaction (nepotpisan).
- Bob šalje ovu datoteku `Consignment.RGB` Alisi (putem e-maila, servera za deljenje ili protokola RGB-RPC, Storm, itd.);
- Alisa prima `Consignment.RGB` i prihvata ga u svom Stash-u:


```bash
alice$ rgb accept consignment.rgb
```




- CLI proverava validnost tranzicije i dodaje je na Alisin Stash. Ako je nevažeća, komanda ne uspeva sa detaljnim porukama o grešci. U suprotnom, uspeva i izveštava da uzorak transakcije još nije emitovan na Bitcoin mreži (Bob čeka Alisino zeleno svetlo);
- Kao potvrdu, komanda `accept` vraća potpis (*payslip*) koji Alisa može poslati Bobu da mu pokaže da je verifikovala *Consignment*;
- Bob zatim može potpisati i objaviti (`--publish`) svoju Bitcoin transakciju:


```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```




- Čim se ova transakcija potvrdi On-Chain, vlasništvo nad sredstvima se smatra prenetim na Alisu. Alisin novčanik, prateći izmajnovane transakcije, vidi novi Owned State kako se pojavljuje u njenom Stash-u.


Sada znate kako da izdate i prenesete RGB ugovor. Ako vam je ovaj vodič bio koristan, bio bih veoma zahvalan ako biste kliknuli na zeleni palac ispod. Slobodno podelite ovaj članak na vašim društvenim mrežama. Hvala vam puno!


Takođe preporučujem ovaj drugi vodič u kojem objašnjavam kako pokrenuti Lightning čvor kompatibilan sa RGB za razmenu tokena gotovo trenutno:


https://planb.network/tutorials/node/others/rln-ffc02528-329b-4e16-bd83-873d0299feea
