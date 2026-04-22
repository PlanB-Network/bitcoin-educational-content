---
name: Liquid Bootcamp Essentials
goal: Steknite sveobuhvatno razumevanje projekta Liquid Network i Elements, i naučite kako da implementirate napredna rešenja u poverljivim transakcijama, tokenizaciji i decentralizovanoj mrežnoj arhitekturi.
objectives: 

  - Razumeti osnove Liquid arhitekture i njen odnos sa Bitcoin.
  - Naučite kako da konfigurišete i upravljate Liquid čvorovima koristeći Elements softver.
  - Istražite upotrebu poverljivih transakcija i izdavanje sredstava na Liquid Network.
  - Razumite poslovne i tehničke aspekte Liquid za primenu na tržištima kapitala.

---

# Uvođenje u Liquid mrežu


Upustite se u obrazovno putovanje osmišljeno da pruži duboko razumevanje projekta Liquid Network i Elements. Ovaj bootcamp kombinuje teoriju i praksu kako bi vas naučio tehničkim, arhitektonskim i poslovnim osnovama neophodnim za implementaciju i korišćenje mogućnosti Liquid. Od poverljivih transakcija do dizajna ekosistema, ovaj kurs je idealan za one koji žele da prošire svoje znanje o naprednim alatima unutar ekosistema Bitcoin.


Sa prezentacijama stručnjaka iz industrije, kurs pokriva teme kao što su arhitektura Liquid, primene tokenizacije, tehnički koncepti Elements, i inovativni slučajevi upotrebe kao što je Breez SDK. Dizajniran da bude pristupačan za početnike i korisnike srednjeg nivoa, kurs takođe nudi vrednost iskusnim programerima koji žele da ovladaju Liquid kao platformom za optimizaciju svojih projekata.

+++

# Uvod


<partId>9f8a83d5-27e0-4e6d-af12-6cd6eb667291</partId>


## Pregled kursa


<chapterId>3192ee7d-255b-4c4f-ba18-e08c5ab98577</chapterId>


Dobrodošli na Liquid Bootcamp, sveobuhvatnu obuku osmišljenu da vas opremi znanjem i veštinama za efikasno korišćenje projekata Liquid Network i Elements. Ovaj kurs nudi sveobuhvatno istraživanje jedinstvenih karakteristika Liquid, uključujući Confidential Transactions, izdavanje sredstava i njegovu federativnu mrežnu arhitekturu, dok takođe uvodi osnovne pojmove Elements, softvera koji pokreće Liquid.


Tokom boot camp-a, istraživaćete praktične primene Liquid Network, od postavljanja i upravljanja čvorovima do razumevanja njegove upotrebe u Bitcoin kapitalnim tržištima i tokenizaciji. Uz prezentacije stručnjaka iz industrije, takođe ćete steći uvid u napredne teme kao što su HTLC-ovi, Breez SDK i Blockstream AMP projekat.


Ovaj bootcamp je prvobitno održan kao događaj uživo, prateći strukturirani raspored (kao što je prikazano na slici) dizajniran za sesije uživo. Međutim, za ovu adaptaciju kursa, sadržaj je reorganizovan kako bi bolje odgovarao online formatu i olakšao razumevanje studentima. Novi redosled osigurava logičan napredak od osnovnih koncepata do naprednijih i tehničkih tema, čime se maksimizira iskustvo učenja.


Ovo putovanje je strukturirano da primi učesnike sa različitim nivoima stručnosti, nudeći kombinaciju teorijskog znanja i praktičnog iskustva. Do kraja ovog boot camp-a, imaćete solidno razumevanje arhitekture Liquid, njegove integracije sa Bitcoin, i kako da koristite njegove inovativne funkcije za izgradnju i optimizaciju finansijskih rešenja.


Zaronite u svet Liquid sidechain-a i oslobodite njegov pun potencijal odmah!

# Osnovi


<partId>6dd86449-c0f7-4e51-9252-5f135cf019df</partId>


## Liquid Arhitektura


<chapterId>4bca9c70-d54d-4e9a-b2db-17c3a6fa655b</chapterId>


:::video id=ff6899d2-b47f-4c3d-983d-3bd66d2be59d:::

### Liquid Network Arhitektura i Konsenzus Model


Liquid Network je federativni sidechain izgrađen na Elements kodnoj bazi, dizajniran da proširi mogućnosti Bitcoin dok se oslanja na njegovu osnovnu sigurnost. Za razliku od Bitcoin-ovog [Proof-of-Work](https://planb.academy/resources/glossary/proof-of-work), Liquid radi na modelu Federativnog [Konsenzusa](https://planb.academy/resources/glossary/consensus). Mrežu održava globalno distribuirana grupa članova, uključujući berze, trgovačke stolove i provajdere infrastrukture. Iz ovog članstva, petnaest "funkcionera" je odabrano da deluju kao potpisnici blokova.


Ovi funkcioneri proizvode [blokove](https://planb.academy/resources/glossary/block) na deterministički način u krugu, sa novim blokom koji se generiše svake minute. Ovo precizno vreme je u kontrastu sa Bitcoin-ovim probabilističkim intervalima od deset minuta. Da bi blok bio važeći, potrebni su potpisi najmanje 11 od 15 funkcionera (prag od dve trećine plus jedan). Ovaj mehanizam obezbeđuje Liquid sa "finalnošću od dva bloka," što znači da kada [transakcija](https://planb.academy/resources/glossary/transaction-tx) ima dve potvrde (otprilike dva minuta), matematički je nemoguće reorganizovati lanac. Ova brzina i sigurnost su kritični za arbitražu, automatizovano trgovanje i brzo međuburzovno poravnanje.


Federacija je dinamična. Kroz Dynamic Federation (Dynafed) protokol, mreža može rotirati funkcionere ili ažurirati parametre bez potrebe za hard [fork](https://planb.academy/resources/glossary/fork). Ovo omogućava sistemu da se razvija i zameni hardver ili članove neprimetno, dok održava kontinuirani rad.


### Confidential Transactions i Asset Management


Definišuća karakteristika Liquid je njegova izvorna podrška za Confidential Transactions (CT) i više sredstava. Na glavnom Bitcoin lancu, svi detalji transakcije—pošiljalac, primalac i iznos—su javni. U Liquid, CT koristi kriptografske obaveze da sakrije tip sredstva i iznos sa javne knjige, dok i dalje omogućava mreži da verifikuje da je transakcija validna (tj. da nije došlo do [inflacije](https://planb.academy/resources/glossary/inflation)). Samo učesnici koji poseduju ključeve za zaslepljivanje mogu videti specifične vrednosti, nudeći nivo komercijalne privatnosti koji je neophodan za institucije koje pomeraju velike pozicije.


Liquid tretira svu imovinu kao "domicilne" građane [blokčejna](https://planb.academy/resources/glossary/blockchain). Ovo uključuje Liquid Bitcoin (LBTC), stabilne kovanice kao što je USDT, i sigurnosne tokene. Izdavanje imovine ne zahteva složene pametne ugovore; to je osnovna funkcija protokola.


#### Regulisana imovina i AMP

Za imovinu koja zahteva usklađenost, kao što su sigurnosni tokeni, Liquid koristi Blockstream Asset Management Platform (AMP). Ovo uvodi sloj sa dozvolama gde transakcije zahtevaju drugi potpis od autorizacionog servera. Ovo omogućava izdavaocima da primenjuju pravila—kao što su Whitelisting ili KYC zahtevi—na granularnom nivou, kombinujući efikasnost blockchain-a sa regulatornim kontrolama tradicionalnih finansija.


### Dvosmerni Peg i Bezbednosna Infrastruktura


Veza između Liquid i Bitcoin održava se putem dvosmernog pega. Da bi se "peg-in" izvršio, korisnik šalje Bitcoin na generisanu adresu na mainchain. Ova sredstva su zaključana za 102 potvrde (otprilike 17 sati) kako bi se eliminisali rizici reorganizacije. Kada se potvrde, ekvivalentna količina LBTC se kreira na Liquid sajdčejnu.


Proces "peg-out" omogućava korisnicima da zamene LBTC za Bitcoin. Ovo zahteva spaljivanje LBTC i kriptografsku autorizaciju od strane federacije. Da bi se sprečila krađa, peg-out procesi su strogo kontrolisani od strane Peg-out Authorization Keys (PAKs) koje drže članovi federacije. Pored toga, sredstva se mogu odmah zameniti putem trećih provajdera kao što je SideSwap, zaobilazeći kašnjenje u poravnanju radi brže likvidnosti.


#### Hardverski sigurnosni moduli (HSM-ovi)

Bezbednost se strogo sprovodi putem hardvera. Funkcioneri ne čuvaju [privatne ključeve](https://planb.academy/resources/glossary/private-key) na standardnim serverima; umesto toga, koriste Hardverske Bezbednosne Module (HSM-ove). Ovi uređaji su fizički odvojeni od logike host servera i programirani su sa strogim pravilima. Na primer, HSM će odbiti da potpiše blok ako njegova visina nije veća od prethodnog, sprečavajući prepravke istorije. Ovaj "adversarijalni" model bezbednosti pretpostavlja da host server može biti kompromitovan, osiguravajući da ključevi ostanu bezbedni čak i ako je fizička lokacija ugrožena.


## Osnovi Elements


<chapterId>1e9cfbed-108e-4067-afb9-4cf950cb43d3</chapterId>


:::video id=5652dcb2-4303-484c-8be5-d98063b39c1c:::

### Elements: Osnova Liquid


Elements je open-source, blockchain platforma izvedena iz Bitcoin Core kodne baze. Proširuje funkcionalnost Bitcoin omogućavajući bočne lance—nezavisne blokčejnove koji mogu prenositi sredstva ka i od Bitcoin. Dok Bitcoin Core pokreće Bitcoin mrežu, Elements je softverski motor iza Liquid Network i drugih prilagođenih bočnih lanaca.


Odnos je jednostavan: Liquid je specifična "instanca" Elements sidechain-a, konfigurisana za proizvodnu upotrebu sa federativnim modelom konsenzusa. Programeri upoznati sa Bitcoin će smatrati Elements intuitivnim, jer zadržava isti RPC (Remote Procedure Call) interfejs i strukturu komandne linije (`elements-cli`, `elements-d`, `elements-qt`). Ključna razlika leži u konfiguraciji: postavljanje `chain=liquidv1` povezuje čvor na glavnu Liquid mrežu, dok `chain=elementsregtest` pokreće lokalno okruženje za regresiono testiranje gde programeri mogu generate blokove trenutno i testirati bez eksternih zavisnosti.


#### Izdavanje imovine

Istaknuta karakteristika Elements je izdavanje nativnih sredstava. Za razliku od Ethereuma, gde su tokeni složeni pametni ugovori, sredstva u Elements su prvoklasni građani kreirani putem jednostavne RPC komande (`issueasset`).


- Jedinstveni identifikatori:** Svaki resurs dobija jedinstveni 64-karakterni heksadecimalni ID.
- Tokeni za ponovo izdavanje:** Izdavaoci mogu opcionalno kreirati tokene za ponovo izdavanje, koji daju vlasniku pravo da kasnije kreira više te imovine (korisno za stabilne coine ili sigurnosne tokene).
- Registar imovine:** Pošto heksadecimalni ID-ovi nisu čitljivi za ljude, Registar imovine Blockstream mapira ove ID-ove na imena i tikere (npr. "USDT"), slično kao DNS za imovinu.


### Privatnost putem Confidential Transactions


Elements rešava jedno od glavnih ograničenja javnih blokčeinova: nedostatak komercijalne privatnosti. Na Bitcoin, svaki iznos transakcije je vidljiv svetu. Elements uvodi **Confidential Transactions (CT)**, koji kriptografski skriva iznos i tip imovine, dok i dalje omogućava mreži da verifikuje validnost transakcije.


Ovo se postiže korišćenjem **Pedersenovih obaveza** i **dokaza opsega**.


- Pedersen Commitments** zamenjuju vidljivu količinu kriptografskom obavezom. Zbog homomorfne enkripcije, validatori mogu proveriti da *Ulazne Obaveze = Izlazne Obaveze + Naknade* bez ikakvog uvida u stvarne vrednosti.
- Range Proofs** sprečavaju korisnika da stvori novac ni iz čega (npr. korišćenjem negativnih brojeva) tako što matematički dokazuju da je skrivena vrednost pozitivan ceo broj unutar važećeg opsega.


Spoljašnjem posmatraču, poverljiva transakcija prikazuje važeće ulaze i izlaze, ali skriva *šta* se šalje i *koliko*. Samo pošiljalac i primalac (koji poseduju ključeve za zaslepljivanje) mogu videti podatke u čistom tekstu.


### Razvoj i RPC Tok posla


Interakcija sa [čvorom](https://planb.academy/resources/glossary/node) Elements se prvenstveno obavlja putem njegovog JSON-RPC interfejsa. Ovo omogućava aplikacijama napisanim u Python-u, JavaScript-u ili Go-u da komuniciraju sa blockchain-om.



- Postavka:** Programer obično počinje u `regtest` režimu. Ovo omogućava trenutno generisanje blokova (`generateblock`) za trenutno potvrđivanje transakcija, zaobilazeći 1-minutno vreme bloka na živoj mreži.
- Komande:** Standardne Bitcoin komande kao što je `getblockchaininfo` su dostupne, zajedno sa Elements-specifičnim komandama kao što su `dumpblindingkey` (za reviziju CT-ova) ili `pegin` (za prebacivanje BTC-a u bočni lanac).
- Alias:** Da bi upravljali više čvorova (npr. "pošiljalac" i "primalac" za testiranje), programeri često koriste alias-e u shell-u kao što su `e1-cli` i `e2-cli` koji upućuju na različite direktorijume podataka, simulirajući [peer-to-peer](https://planb.academy/resources/glossary/peertopeer-p2p) mrežu na jednoj mašini.


Ova arhitektura omogućava programerima da izgrade sofisticirane finansijske aplikacije—kao što su platforme za hartije od vrednosti ili privatni platni prolazi—koristeći robusne i poznate alate Bitcoin ekosistema.


## Povezivanje Bitcoin slojeva


<chapterId>3ff2df4a-8995-4d5e-9b8a-cd114880e666</chapterId>


:::video id=31368c02-b979-44d7-b217-ceed96c7ca5c:::

### Cross-Layer Infrastructure and HTLCs


Ekosistem Bitcoin evoluirao je u višeslojnu arhitekturu, pri čemu Mainchain pruža poravnanje, Lightning nudi brzinu, a Liquid omogućava napredne mogućnosti imovine. Prenošenje vrednosti između ovih slojeva bez centralizovanih posrednika zahteva kriptografski primitiv bez poverenja: Hash Time Locked Contract ([HTLC](https://planb.academy/resources/glossary/htlc)).


HTLC kreira uslovni [kanal plaćanja](https://planb.academy/resources/glossary/payment-channel) koji povezuje nezavisne sisteme atomski. Funkcioniše kroz dva primarna ograničenja: **hash zaključavanje** i **vremensko zaključavanje**.


- Zaključavanje Hash:** Sredstva se mogu odmah potrošiti ako primalac otkrije tajnu "preimage" koja odgovara određenom kriptografskom [hešu](https://planb.academy/resources/glossary/hash-function).
- The Time Lock:** Ako primalac ne uspe da otkrije tajnu u okviru postavljenog vremenskog okvira (visina bloka), originalni pošiljalac može povratiti sredstva.


Ova struktura sa dvostrukim putem osigurava bezbednost. U zameni između slojeva, ista heš brava se koristi na obe mreže. Kada primalac otkrije tajnu da bi preuzeo sredstva na jednom sloju (npr. Liquid), ta tajna postaje vidljiva pošiljaocu, koji je zatim može koristiti da preuzme recipročna sredstva na drugom sloju (npr. Lightning). Ovo kriptografsko povezivanje garantuje da zamena ili uspešno završava za obe strane ili ne uspeva za obe, eliminišući rizik da jedna strana izgubi sredstva dok ih druga dobija.


### Nadogradnja Taproot i MuSig2


Legacy HTLCs ([SegWit](https://planb.academy/resources/glossary/segwit) v0) su dobro funkcionisali, ali su imali nedostatke u pogledu privatnosti i efikasnosti. Zahtevali su objavljivanje kompletne logike [skripte](https://planb.academy/resources/glossary/script) on-chain, što je činilo swap transakcije lako prepoznatljivim za analitičare blockchaina i skupljim zbog njihove veličine podataka. Uvođenje [Taproot](https://planb.academy/resources/glossary/taproot) (SegWit v1) i MuSig2 protokola je revolucionisalo ovu arhitekturu.


Taproot omogućava **Agregaciju Ključeva** putem MuSig2. Umesto otkrivanja složenog skripta sa više [javnih ključeva](https://planb.academy/resources/glossary/public-key), MuSig2 omogućava učesnicima zamene da kombinuju svoje ključeve u jedan agregirani javni ključ.


- Kooperativa "Key Path":** Ako se obe strane slože sa zamjenom (tzv. "srećan put"), one zajedno potpisuju transakciju. Za mrežu, ovo izgleda identično standardnom plaćanju sa jednim potpisom. Troši minimalan prostor u bloku i ne otkriva apsolutno nikakve informacije o uslovima zamjene.
- Adversarialni "Putanja Skripta":** Ako jedna strana postane neodgovorna ili zlonamerna, osnovni skript (koji sadrži hash/vremenske brave) se otkriva tek tada. Ovo je organizovano u [Merkle drvetu](https://planb.academy/resources/glossary/merkle-tree), omogućavajući poštenoj strani da otkrije samo određenu granu potrebnu za povraćaj sredstava, držeći ostatak logike ugovora skrivenim.


### Praktična Implementacija: Liquid-Lightning Swaps


U praksi, ovi protokoli omogućavaju besprekornu razmenu između slojeva Bitcoin. Tipična zamena Liquid-za-Lightning počinje kada klijent zatraži zamenu od provajdera usluga. Klijent obezbeđuje [Lightning fakturu](https://planb.academy/resources/glossary/invoice-lightning), a provajder zaključava ekvivalentni Liquid Bitcoin (L-BTC) u Taproot-omogućenu HTLC adresu.


Atomskost se sprovodi kada se uplata poravna. Da bi preuzeo L-BTC, pružalac usluga mora imati preimage. Oni dobijaju ovaj preimage samo kada uspešno plate klijentov Lightning račun. U trenutku kada je Lightning uplata finalizovana, preimage se otkriva, omogućavajući pružaocu da otključa Liquid sredstva.


#### Wallet Apstrakcija i UTXO Upravljanje

Za krajnje korisnike, ova složenost je potpuno apstrahovana. Moderni novčanici kao što je Aqua upravljaju generisanjem ključeva, kreiranjem faktura i procesima potpisivanja u pozadini. Korisnik jednostavno "plaća" Lightning fakturu koristeći svoj Liquid saldo. Iza kulisa, servis upravlja [UTXO](https://planb.academy/resources/glossary/utxo) konsolidacijom, periodično pomerajući male, nepreuzete ili refundirane izlaze kako bi održao [wallet](https://planb.academy/resources/glossary/wallet) efikasnost i minimizirao uticaj naknada tokom perioda velike saobraćajne gužve.


## Pregled Liquid Network


<chapterId>1968db03-2364-46c0-9670-9e9844289ca1</chapterId>


:::video id=0bac0a62-90f2-41da-ac7c-330c0604bc61:::

### Liquid Network Arhitektura i Konsenzus


Liquid Network funkcioniše kao federativni sidechain izgrađen na **Elements** kodnoj bazi. Dok Elements—fork od Bitcoin Core—pruža softversku osnovu, Liquid je implementacija produkcione mreže. Za razliku od Bitcoin-ovog Proof-of-Work, koji se oslanja na konkurentni [mining](https://planb.academy/resources/glossary/mining), Liquid koristi model **Federated Consensus**.


Mreža se održava od strane petnaest globalno raspoređenih "funkcionera." Ovi entiteti upravljaju specijalizovanim serverima koji obavljaju dve ključne uloge:

1.  **Proizvodnja Blokova:** Funkcioneri se smenjuju u kreiranju blokova prema determinističkom round-robin rasporedu, generišući novi blok tačno svake minute.

2.  **Potpisivanje bloka:** Da bi blok bio važeći, mora biti potpisan od strane najmanje 11 od 15 funkcionera.


Ovaj prag od 11-od-15 osigurava da mreža može tolerisati kvar do četiri čvora bez zaustavljanja. Primarna prednost ove razmene je **deterministička finalnost**. Dok se Bitcoin bavi verovatnoćama, Liquid postiže sigurnost poravnanja nakon dva bloka (otprilike dva minuta). Kada blok ima jednu potvrdu iznad sebe, lanac se ne može reorganizovati, što ga čini veoma efikasnim za arbitražu i brzo poravnanje.


### Confidential Transactions i Native Assets


Definišuća karakteristika Liquid je podrazumevana upotreba **Confidential Transactions (CT)**. Na Bitcoin mainchain, pošiljalac, primalac i iznos su javni. Liquid to poboljšava kriptografskim zaslepljivanjem iznosa i tipa sredstva, dok ostavlja adrese pošiljaoca i primaoca vidljivim za verifikaciju.


Da bi se osiguralo da korisnik ne može štampati novac (npr. slanjem negativnih iznosa), Liquid koristi **Pedersenova Obećanja** i **Dokaze O Rasponu**. Ovi kriptografski primitivni omogućavaju mreži da verifikuje da *Ulazi = Izlazi + Naknade* i da su sve vrednosti pozitivni celi brojevi, bez ikakvog otkrivanja specifičnih brojeva javnoj knjizi. Samo učesnici koji poseduju ključeve za zaslepljivanje mogu videti dekriptovane podatke.


#### Izdavanje imovine

Liquid tretira svu imovinu kao "native". Bilo da je u pitanju Liquid Bitcoin (L-BTC), stabilni novac kao USDT, ili hartija od vrednosti token, svi dele istu arhitekturu. Izdavanje imovine ne zahteva pametne ugovore—samo jednostavan RPC poziv.


- Neregulisana sredstva:** Može ih izdati bilo ko bez dozvole.
- Regulated Assets:** Korišćenjem Blockstream Asset Management Platform (AMP), izdavaoci mogu primeniti pravila usklađenosti (kao što su KYC/AML) zahtevajući drugi potpis od autorizacionog servera pre nego što se sredstvo može premestiti.


### Dvosmerni Peg i Dinamička Federacija


Most između Bitcoin i Liquid je **Two-Way Peg**. Omogućava korisnicima da prebace BTC na bočni lanac (Peg-in) i nazad na mainchain (Peg-out).


**Proces umetanja:**

Ovo je bez dozvole. Korisnik šalje BTC na adresu pod kontrolom federacije. Da bi se zaštitili od Bitcoin reorganizacija blokčejna, ova sredstva moraju čekati **102 potvrde** (približno 17 sati) pre nego što ekvivalentni L-BTC bude kreiran na sajdčejnu.


**Proces isplate:**

Da bi se vratilo na Bitcoin, L-BTC se spaljuje. Međutim, da bi se sprečila krađa osnovnih rezervi Bitcoin, peg-out procesi nisu potpuno automatizovani. Oni zahtevaju autorizaciju od strane člana koji poseduje **Peg-Out Authorization Key (PAK)**. Sredstva Bitcoin su sama po sebi osigurana u 11-od-15 multisignature wallet, sa ključevima koji se čuvaju u Hardware Security Modules (HSMs) koji su odvojeni od glavnih servera funkcionera.


**Dynamic Federation (Dynafed):**

Kako bi se osigurala dugovečnost, Liquid koristi Dynafed, protokol koji omogućava mreži da rotira funkcionere ili ažurira parametre bez tvrdog fork. Ako funkcioner treba da bude zamenjen, mreža emituje tranzicionu transakciju. Nakon dvonedeljnog perioda preklapanja, nova konfiguracija preuzima, omogućavajući federaciji da se neprimetno razvija uz održavanje kontinuiranog rada.


## Ekosistem i tržišta kapitala


<chapterId>5f4c0e50-b435-4b6c-b8b7-c55cc1a35431</chapterId>


:::video id=07e0b82f-2d60-4eb3-9b5d-2ccb7ad06e8a:::

### Liquid Network: Poslovna strategija i ekosistem


Liquid je više od tehničkog sidechain-a; to je infrastrukturni sloj fokusiran na poslovanje, dizajniran da se nosi sa složenim zahtevima tržišta kapitala koje Bitcoin mainchain ne može efikasno podržati. Dok [Lightning Network](https://planb.academy/resources/glossary/lightning-network) optimizuje za visokofrekventna, niskovredna plaćanja, Liquid cilja na transfer visokih vrednosti, izdavanje sredstava i međubankarsko poravnanje.


Ekosistem pokreće **Liquid Federacija**, konzorcijum od ~73 kompanije uključujući berze, trgovačke stolove i provajdere infrastrukture. Ovaj kolaborativni model odražava tradicionalne finansijske klirinške kuće, ali funkcioniše sa većom transparentnošću i značajno smanjenim vremenom poravnanja (2 minuta naspram T+2 dana).


### Tokenizacija stvarnih sredstava (RWA)


Osnovni poslovni slučaj za Liquid je "Tokenizacija"—predstavljanje stvarne vrednosti (akcije, obveznice, mining ugovori) kao digitalnih tokena na blockchain-u. Ovo nudi tri glavne prednosti:

1.  **24/7 Globalna tržišta:** Uklanjanje radnog vremena banaka i geografskih ograničenja.

2.  **Operativna Efikasnost:** Eliminisanje grešaka u usklađivanju putem zajedničke, nepromenljive knjige.

3.  **Atomsko poravnanje:** Smanjenje rizika druge ugovorne strane osiguravanjem da se isporuka dogodi istovremeno s plaćanjem.


#### Regulisana imovina i AMP

Većina institucionalnih sredstava ne može trgovati bez dozvole zbog zakonskih zahteva. **Platforma za upravljanje sredstvima (AMP)** je tehnički standard koji sprovodi ova pravila.


- Whitelisting:** Izdavaoci mogu ograničiti držanje i trgovanje na KYC-verifikovane adrese.
- Multisig Kontrola:** Akcije usklađenosti (poput zamrzavanja ukradenih sredstava ili ponovnog izdavanja izgubljenih tokena) upravljaju se putem višestrukog potpisa, osiguravajući da nijedan zaposleni ne može delovati samostalno.


Ova infrastruktura je danas aktivna. Platforme kao što je **Stalker** pružaju usluge tokenizacije od početka do kraja u Evropi, dok **Sideswap** deluje kao decentralizovana berza i nekustodijalni wallet, omogućavajući trgovinu od osobe do osobe za imovinu kao što su **Blockstream Mining Note (BMN)** i tokenizovane akcije MicroStrategy (CMSTR).


### Uspeh u stvarnom svetu: Studija slučaja Mayfell


Najubedljiviji dokaz korisnosti Liquid dolazi iz **Mayfell-a** u Meksiku. Na tržištu gde se tradicionalno finansiranje oslanja na papirne menice—koje su sklone gubitku, prevari i sporoj obradi—Mayfell je prebacio celu infrastrukturu na Liquid.



- Razmera:** Izdato preko 25.000 menica, što predstavlja vrednost od **$1.5 milijardi+**.
- Privatnost:** Korišćenjem Liquid-ovog Confidential Transactions, iznosi zajma su vidljivi samo zajmodavcu i zajmoprimcu, čuvajući komercijalnu privatnost dok revizorima omogućava proveru integriteta knjige.
- Uticaj:** Povezivanjem nebankarskih kreditora sa globalnim tržištima kapitala putem blockchain-a, Mayfell je smanjio troškove i proširio pristup kreditima za meksičke MSP-ove, pokazujući da vrednosna ponuda Liquid prevazilazi spekulativno trgovanje.


### Strateško pozicioniranje u odnosu na druge lance


Liquid se takmiči na prepunom tržištu platformi za tokenizaciju (Ethereum, Solana, itd.), ali ima posebne strateške prednosti:


- Regulatory Clarity:** Liquid koristi Bitcoin (L-BTC) kao svoj izvorni aset. Nema unapred iskopan token ili ICO, čime izbegava rizike "neregistrovanih hartija od vrednosti" koji muče druge L1 blokčejnove.
- Stabilnost:** Za razliku od Ethereumovog modela računa gde neuspele transakcije i dalje troše naknade za gas, Liquid-ov UTXO model je deterministički i pouzdan za finansijske podatke od suštinskog značaja.
- Privatnost:** Podrazumevana poverljivost je zahtev za većinu finansijskih institucija, funkcija koju Liquid nudi prirodno, a sa kojom javni lanci imaju poteškoća da implementiraju bez složenih dodataka.


Za programere, ovaj ekosistem nudi jasnu priliku: izgradnju alata (nadzorne table, novčanici, integracije usklađenosti) koji povezuju tradicionalne finansije sa sigurnim slojem poravnanja Bitcoin.


## Blockstream AMP


<chapterId>4f21a0a7-0dc0-44cf-8a3a-d9e2f8a3f05f</chapterId>


:::video id=f00822b4-dc1a-46ff-adfc-ff7c97a0024d:::

### Blockstream AMP: Kontrola dozvoljenih sredstava na Liquid


Blockstream AMP (Asset Management Platform) služi kao kritični infrastrukturni sloj na Liquid Network, dizajniran posebno za izdavače regulisanih digitalnih hartija od vrednosti i stabilnih kovanica. Dok Liquid obezbeđuje sloj bez dozvola sa izdavanjem nativnih sredstava, regulisani subjekti često zahtevaju strogi nadzor i mogućnosti usklađenosti. AMP premošćuje ovaj jaz uvodeći sloj kontrole sa dozvolama nad specifičnim sredstvima bez žrtvovanja prednosti privatnosti Liquid-ovog Confidential Transactions.


Osnovna vrednost platforme počiva na dve primarne sposobnosti: sveobuhvatna vidljivost izdavača i autorizacija transakcija. Za razliku od standardnih Liquid sredstava gde su iznosi i tipovi blinded svima osim učesnicima, AMP sredstva omogućavaju izdavaču da održava potpuno unblinded revizijski trag. Ova transparentnost je ključna za regulatorno izveštavanje i interne revizije. Nadalje, AMP sprovodi strogi model autorizacije kroz mehanizam sa-potpisivanja. Svaki prenos AMP sredstva zahteva potpis sa AMP servera. Ovo omogućava izdavačima da sprovode složena pravila off-chain—kao što su zamrzavanje računa, stavljanje na belu listu akreditovanih investitora, ili nametanje ograničenja prenosa—efikasno delujući kao centralizovani čuvar unutar decentralizovane mreže.


#### Operativni kompromisi

Ova arhitektura uvodi specifične kompromise. Sistem se oslanja na dostupnost AMP servera; ako server deluje kao ko-potpisnik i postane nedostupan, likvidnost imovine se zaustavlja. Pored toga, dok je privatnost između korisnika očuvana, investitori moraju prihvatiti da izdavalac ima potpuni uvid u njihove posede. Ovaj model je idealan za usklađene sigurnosne tokene, ali nije pogodan za [kriptovalute](https://planb.academy/resources/glossary/cryptocurrency) otporne na cenzuru.


### Evolucija arhitekture i putevi integracije


AMP ekosistem trenutno prelazi sa svoje prve iteracije na fleksibilniju, interoperabilnu arhitekturu "Verzija 2". Nasleđeni sistem je zahtevao od izdavača da održavaju potpuno sinhronizovane Elements čvorove i primoravao programere da se u velikoj meri oslanjaju na monolitni Green SDK. Iako funkcionalan, ovo je stvaralo visoke tehničke prepreke za ulazak i ograničavalo wallet izbore.


Arhitektura sledeće generacije fundamentalno pojednostavljuje ove zahteve prebacivanjem složenosti na server. U ovom novom modelu, AMP server obavlja teške zadatke konstrukcije transakcija, selekcije UTXO i kalkulacije naknada. On predstavlja izdavaču Delimično Potpisanu Elements Transakciju (PSET) koja zahteva samo potpis. Ovaj pristup "pametni server, glupi wallet" eliminiše potrebu da izdavači pokreću pune čvorove i omogućava korišćenje hardverskih novčanika i standardnih multisignature postavki za upravljanje trezorom.


Za programere, ova evolucija znači prelazak sa vlasničkih SDK-ova ka standardnim deskriptorima i PSET tokovima rada. Novčanici sada mogu registrovati multisignature deskriptore sa AMP serverom kako bi uspostavili prava autorizacije. Ovo usklađuje AMP razvoj sa širim Bitcoin wallet standardima, čineći integraciju dostupnom bilo kojoj aplikaciji sposobnoj za rukovanje PSBT/PSET formatima. Programerima koji danas grade se preporučuje korišćenje alata kao što je Liquid Wallet Kit (LWK), koji podržava ove moderne, na deskriptorima zasnovane arhitekture, osiguravajući da njihove aplikacije budu otporne na buduće promene novih AMP standarda.


### Ekosistem Liquid Wallet i Povjerljivost


Izrada aplikacija na Liquid zahteva navigaciju kroz složeniji stek nego standardni razvoj na Bitcoin zbog funkcija kao što su nativna sredstva i Confidential Transactions. Ekosistem je podržan slojevitom arhitekturom: biblioteke niskog nivoa kao što je `secp256k1-zkp` upravljaju kriptografskim primitivama, dok kompleti alata višeg nivoa upravljaju logikom wallet.


Istorijski gledano, Green Development Kit (GDK) je pružao sveobuhvatno, ali kruto rešenje. Moderna alternativa je Liquid Wallet Kit (LWK), koji nudi modularni pristup. LWK razdvaja zadatke u posebne module—samostalno upravljajući deskriptorima, potpisivanjem i komunikacijom sa hardverom—dajući programerima fleksibilnost da izgrade prilagođena rešenja bez opterećenja monolitne biblioteke.


#### Rukovanje sa Confidential Transactions

Najizazovniji izazov u ovom ekosistemu je upravljanje životnim ciklusom zaslepljivanja. U Liquid, izlazi transakcija su šifrovani koristeći razmenu ključeva Elliptic Curve Diffie-Hellman (ECDH). Pošiljalac koristi primaločev javni ključ za zaslepljivanje kako bi šifrirao iznose i tipove sredstava, generišući dokaz opsega koji potvrđuje validnost transakcije bez otkrivanja vrednosti.


Da bi wallet funkcionisao, mora uspešno da obrne ovaj proces. Kada wallet detektuje dolaznu transakciju, pokušava da ukloni slepilo sa izlaza koristeći svoj privatni ključ za slepilo. Ako se deljeni tajni ključ poklapa, wallet može dešifrovati vrednost i dodati je korisnikovom saldu. Ovaj proces je računarski intenzivan i zahteva precizno upravljanje faktorima slepila kako bi se osiguralo da su transakcije matematički izbalansirane, složenost koju alati poput LWK-a nastoje da apstrahuju za programera.


# Tehnički


<partId>53629f58-b9e0-4a10-8ab2-d51b047414f8</partId>

<chapterId>f1fdf2b0-4b6a-4ba7-812c-7586dcb36713</chapterId>


## Breez SDK - Nodeless


<chapterId>fb77442c-3d1e-427e-b2f5-16668ce4c643</chapterId>


:::video id=1a6289b5-fdae-4320-b5b1-41925150108c:::

### Uvod u Breez Liquid SDK


Breez Liquid SDK je samostalni, open-source alat dizajniran da premosti jaz između Liquid Network i šireg Bitcoin ekosistema. Njegova primarna misija je da apstrahuje složenosti upravljanja Lightning Network čvorovima i atomskih zamena, omogućavajući programerima da izgrade finansijske aplikacije bez trenja.


Izgrađen sa filozofijom "mobile-first", osnovna logika je napisana u Rust za performanse i sigurnost, ali koristi UniFFI (Unified Foreign Function Interface) da obezbedi nativne veze za Kotlin, Swift, Python, C#, Dart i Flutter. Ovo osigurava da programeri mogu integrisati funkcionalnost Bitcoin u svoje preferirano okruženje bez upravljanja niskonivo operacijama kriptografije.


**Podržane vrste transakcija:**

SDK funkcioniše sa Liquid kao svojom "osnovnom bazom." Izvrsno obavlja tri specifične operacije:

1.  **Liquid-do-Liquid:** Direktni on-chain transferi.

2.  **Liquid-do-Lightning:** Plaćanje Lightning faktura korišćenjem Liquid sredstava.

3.  **Liquid-do-Bitcoin:** Direktno prebacivanje sredstava na Bitcoin mainchain.


*Napomena: SDK ne podržava direktne Lightning-to-Lightning ili Bitcoin-to-Bitcoin transakcije. To je isključivo alat fokusiran na Liquid.*


### Arhitekture Plaćanja: Podmorske Zamene


Da bi se postigla interoperabilnost između Liquid, Lightning i Bitcoin bez centralizovanih kustosa, Breez se oslanja na **Submarine Swaps**. Ovo su atomske operacije gde transakcija ili uspešno završava na obe mreže ili ne uspeva na obe, osiguravajući da sredstva nikada ne budu izgubljena u tranzitu.


#### Lightning Send (Submarine Swap)

Kada korisnik plati Lightning fakturu, SDK emituje transakciju "zaključavanja" na Liquid Network. Ovo efektivno stavlja sredstva u escrow. Provajder zamene (Boltz) to detektuje, plaća Lightning fakturu, a zatim koristi preimage plaćanja (kriptografski račun) da preuzme zaključana Liquid sredstva.


#### Prijem munje (Obrnuta podmorska zamena)

Primanje Lightning-a je inverzni proces. Korisnik generiše fakturu, a provajder zamene zaključava sredstva na Lightning Network. SDK prati ovaj proces putem WebSockets-a. Kada je zaključavanje potvrđeno, SDK automatski izvršava transakciju potraživanja kako bi prebacio ekvivalentna sredstva u korisnikov Liquid wallet.


#### Cross-Chain Bitcoin

Za Liquid-do-Bitcoin transfere, arhitektura koristi mehanizam "dual-swap". Transakcije zaključavanja se dešavaju na oba lanca istovremeno. Pošiljalac potražuje sredstva na Bitcoin, dok primalac potražuje sredstva na Liquid. Ovo omogućava poverljivo povezivanje bez oslanjanja na federated peg-izlaze ili centralizovane berze.


### Developer Interface i Automatizovano Upravljanje


Breez SDK pojednostavljuje iskustvo programera kondenzovanjem složenih finansijskih tokova u standardizovani trostepeni proces: **Poveži, Pripremi i Izvrši**.


1.  **Connect:** Inicijalizuje wallet, sinhronizuje se sa blokčejnom koristeći Liquid Wallet Kit (LWK), i uspostavlja WebSocket konekcije za praćenje u realnom vremenu.

2.  **Pripremi:** Pre nego što se sredstva ulože, ovaj korak izračunava i vraća sve povezane mrežne naknade i troškove zamene, omogućavajući korisničkom interfejsu da korisniku prikaže jasan ukupan iznos.

3.  **Izvrši:** Ovaj korak konstruira transakciju, emituje je i inicira zamenu.


#### Automatizovani sigurnosni mehanizmi

Jedna od najvažnijih karakteristika SDK-a je **Automatizovano Upravljanje Povratom Novca**. U slučaju mrežnog kvara ili nesaradljivog partnera, sredstva bi teoretski mogla ostati zaglavljena u vremenski zaključanom ugovoru. SDK u potpunosti apstrahuje logiku oporavka. On prati stanje svake zamene; ako zamena ne uspe ili istekne, SDK automatski konstruira i emituje transakciju povrata kako bi vratio sredstva korisnikovom wallet.


Pored toga, SDK obrađuje **Rešavanje Metapodataka**. Spaja off-chain podatke o zameni (koje obezbeđuje Boltz zamenač) sa on-chain istorijom transakcija. Ovo osigurava da istorija transakcija korisnika bude čitljiva za ljude, prikazujući detalje faktura i kontekst plaćanja umesto samo sirovih heksadecimalnih heševa transakcija.


# Završni Deo


<partId>7ec65e6b-6e63-41b6-92ea-6a13bc77c3ff</partId>


## Recenzije i Ocene


<chapterId>e5f6348c-e207-40ae-8fef-6a068a6bf741</chapterId>


<isCourseReview>true</isCourseReview>

## Završni ispit


<chapterId>b13c4aa8-ced6-11f0-8515-afd3f381a001</chapterId>

<isCourseExam>true</isCourseExam>

## Zaključak


<chapterId>e30a5587-d74b-4360-87fb-bbf3de1b0ba8</chapterId>

<isCourseConclusion>true</isCourseConclusion>