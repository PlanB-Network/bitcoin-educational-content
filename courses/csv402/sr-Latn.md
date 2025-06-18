---
name: RGB protokol, od teorije do prakse
goal: Steknite veštine potrebne za razumevanje i korišćenje RGB
objectives: 

  - Razumeti osnovne koncepte RGB protokola
  - Savladajte principe obaveza Client-side Validation i Bitcoin
  - Naučite kako kreirati, upravljati i prenositi RGB ugovore
  - Kako upravljati Lightning čvorom kompatibilnim sa RGB


---
# Otkriće RGB protokola


Zaronite u svet RGB, protokola dizajniranog za implementaciju i sprovođenje digitalnih prava, u obliku ugovora i sredstava, zasnovanih na pravilima konsenzusa i operacijama Bitcoin Blockchain. Ovaj sveobuhvatni kurs obuke vodi vas kroz tehničke i praktične osnove RGB, od koncepata "Client-side Validation" i "Jednokratnih pečata", do implementacije naprednih pametnih ugovora.


Kroz strukturiran, korak-po-korak program, otkrićete mehanizme Client-side Validation, determinističke obaveze na Bitcoin i obrasce interakcije između korisnika. Naučite kako kreirati, upravljati i prenositi RGB tokene na Bitcoin ili Lightning Network.


Bilo da ste programer, entuzijasta Bitcoin ili jednostavno radoznali da saznate više o ovoj tehnologiji, ovaj kurs obuke će vam pružiti alate i znanje koje vam je potrebno da savladate RGB i izgradite inovativna rešenja na Bitcoin.


Kurs je zasnovan na seminaru uživo koji organizuje Fulgur'Ventures i predaju ga tri renomirana predavača i stručnjaci za RGB.


+++
# Uvod


<partId>c6f7a70f-d894-595f-8c0a-b54759778839</partId>


## Prezentacija kursa


<chapterId>cf2f087b-6c6b-5037-8f98-94fc9f1d7f46</chapterId>


Zdravo svima, i dobrodošli na ovaj kurs obuke posvećen RGB, sistemu validiranom na strani klijenta Smart contract koji radi na Bitcoin i Lightning Network. Struktura ovog kursa je dizajnirana da omogući detaljno istraživanje ove složene teme. Evo kako je kurs organizovan:


**Section 1: Teorija


Prvi deo je posvećen teorijskim konceptima potrebnim za razumevanje osnova Client-side Validation i RGB. Kao što ćete otkriti u ovom kursu, RGB uvodi niz tehničkih koncepata koji se obično ne viđaju u Bitcoin. U ovom delu ćete takođe pronaći rečnik sa definicijama svih termina specifičnih za RGB protokol.


**Section 2: Praksa


Drugi deo će se fokusirati na primenu teorijskih koncepata viđenih u odeljku 1. Naučićemo kako da kreiramo i manipulišemo RGB ugovorima. Takođe ćemo videti kako da programiramo sa ovim alatima. Ova prva dva odeljka predstavlja Maksim Orlovski.


**Section 3: Applications


Završni deo vodiće drugi govornici koji će predstaviti konkretne aplikacije zasnovane na RGB, kako bi istakli primere iz stvarnog života.


---
Ovaj kurs obuke je prvobitno nastao iz dvonedeljnog naprednog razvojnog bootcampa u Viareggiu, Toskana, koji je organizovao [Fulgur'Ventures](https://fulgur.ventures/). Prva nedelja, fokusirana na Rust i SDK-ove, može se pronaći u ovom drugom kursu:


https://planb.network/courses/9fbd8b57-f278-4304-8d88-a2d384eaff58

U ovom kursu, fokusiramo se na drugu nedelju bootcampa, koja se fokusira na RGB.


**Nedelja 1 - LNP402:**


![RGB-Bitcoin](assets/fr/001.webp)


**Nedelja 2 - Trenutni trening CSV402:**


![RGB-Bitcoin](assets/fr/002.webp)


Mnogo hvala organizatorima ovih kurseva uživo i 3 nastavnika koji su učestvovali:




- Maxim Orlovsky: *Ex Tenebrae sententia sapiens dominabitur astris. Cypher, AI, robotics, transhumanism. Creator of RGB, Prime, Radiant and lnp_bp, mycitadel_io & cyphernet_io* ;
- Hunter Trujilo: *Developer, Rust, Bitcoin, Lightning, RGB* ;
- Federico Tenga: *Radim svoj deo kako bih svet pretvorio u Cypherpunk distopiju. Trenutno radim na RGB u Bitfinexu*.


Pisani oblik ovog kursa obuke izrađen je korišćenjem 2 glavna resursa:




- Video snimci seminara Maxima Orlovskog, Huntera Trujila i Frederica Tenge na Lightning Bootcampu ;
- Dokumentacija RGB, čiju je izradu sponzorisao [Bitfinex](https://www.bitfinex.com/).


Spremni da zaronite u složen i fascinantan svet RGB? Hajde da krenemo!


# RGB u teoriji


<partId>80e797ee-3f33-599f-ab82-e82eeee08219</partId>


## Uvod u pojmove distribuiranog računarstva


<chapterId>f52f8af5-5d7c-588b-b56d-99b97176204b</chapterId>


:::video id=f27338bc-4210-4a2e-9b27-30278ed3282c:::


RGB je protokol dizajniran da primeni i sprovede digitalna prava (u obliku ugovora i sredstava) na skalabilan i poverljiv način, zasnovan na pravilima konsenzusa i operacijama Bitcoin Blockchain. Cilj ovog prvog poglavlja je da predstavi osnovne pojmove i terminologiju oko RGB protokola, posebno ističući njegove bliske veze sa osnovnim konceptima distribuiranog računarstva kao što su Client-side Validation i Jednokratni Pečati.


U ovom poglavlju istražujemo osnove **distribuiranih konsenzus sistema** i vidimo kako se RGB uklapa u ovu porodicu tehnologija. Takođe ćemo predstaviti glavne principe koji nam pomažu da razumemo zašto RGB teži da bude proširiv i nezavisan od sopstvenog konsenzus mehanizma Bitcoin, dok se oslanja na njega kada je to potrebno.


### Uvod


Distribuirano računarstvo, specifična grana računarstva, proučava protokole korišćene za distribuciju i obradu informacija na mreži čvorova. Zajedno, ovi čvorovi i pravila protokola čine ono što je poznato kao distribuirani sistem. Među osnovnim svojstvima koja karakterišu takav sistem su :




- **sposobnost nezavisne verifikacije i validacije** određenih podataka od strane svakog čvora;
- Mogućnost da čvorovi konstruiraju (u zavisnosti od protokola) kompletan ili delimičan prikaz informacija. Ovi prikazi su **stanja** distribuiranog sistema;
- Hronološki redosled operacija, tako da su podaci pouzdano vremenski obeleženi i postoji konsenzus o redosledu događaja (redosled stanja).


Posebno, pojam **konsenzusa** u distribuiranom sistemu pokriva dva aspekta:




- Prepoznavanje validnosti** promena stanja (prema pravilima protokola);
- **sporazum o redosledu** ovih promena stanja, što onemogućava prepravljanje ili poništavanje validiranih operacija a posteriori (ovo je takođe poznato u Bitcoin kao "zaštita od dvostrukog trošenja").


Prva funkcionalna, dozvola-slobodna implementacija mehanizma distribuiranog konsenzusa predstavljena je od strane Satoshi Nakamoto sa Bitcoin, zahvaljujući kombinovanoj upotrebi Blockchain strukture podataka i Proof-of-Work (PoW) algoritma. U ovom sistemu, kredibilitet istorije blokova zavisi od računarske snage koju mu posvećuju čvorovi (rudari). Bitcoin je stoga glavni i istorijski primer sistema distribuiranog konsenzusa otvorenog za sve (*permissionless*).


U svetu Blockchain i distribuiranog računarstva, možemo razlikovati dva fundamentalna paradigme: ***Blockchain*** u tradicionalnom smislu, i ***state channels***, čiji je najbolji primer u proizvodnji Lightning Network. Blockchain je definisan kao registar hronološki uređenih događaja, repliciran konsenzusom unutar otvorene, mreže bez dozvola. State channels, s druge strane, su peer-to-peer kanali koji omogućavaju dvema (ili više) učesnicima da održavaju ažurirano stanje off-chain, koristeći Blockchain samo prilikom otvaranja i zatvaranja ovih kanala.


U kontekstu Bitcoin, sigurno ste upoznati sa principima Mining, decentralizacijom i finalnošću transakcija na Blockchain, kao i kako funkcionišu platni kanali. Sa RGB, uvodimo novu paradigmu zvanu **Client-side Validation**, koja, za razliku od Blockchain ili Lightning, podrazumeva lokalno (na strani klijenta) čuvanje i validaciju prelaza stanja Smart contract. Ovo se takođe razlikuje od drugih "DeFi" tehnika (_rollups_, _plasma_, _ARK_, itd.), jer Client-side Validation se oslanja na Blockchain da spreči Double-spending i da ima sistem vremenskog pečatiranja, dok zadržava registar stanja i prelaza off-chain, samo sa uključenim učesnicima.


![RGB-Bitcoin](assets/fr/003.webp)


Kasnije ćemo takođe uvesti važan termin: pojam "**Stash**", koji se odnosi na skup podataka na strani klijenta potrebnih za očuvanje stanja Contract, jer ti podaci nisu globalno replicirani preko mreže. Na kraju ćemo razmotriti logiku iza RGB, protokola koji koristi Client-side Validation, i zašto dopunjuje postojeće pristupe (Blockchain i state kanale).


### Trileme u distribuiranom računarstvu


Da bismo razumeli kako Client-side Validation i RGB Address problemi nisu rešeni od strane Blockchain i Lightning, hajde da otkrijemo 3 glavna "trilema" u distribuiranom računarstvu:




- Skalabilnost, Decentralizacija, Privatnost** ;
- CAP** Teorema (Konzistentnost, Dostupnost, Tolerancija particije) ;
- CIA** trilema (Poverljivost, Integritet, Dostupnost).


#### 1. Skalabilnost, decentralizacija i poverljivost




- Blockchain (Bitcoin)**


Blockchain je visoko decentralizovan, ali nije veoma skalabilan. Štaviše, pošto je sve u globalnom, javnom registru, poverljivost je ograničena. Možemo pokušati da poboljšamo poverljivost tehnologijama nultog znanja (Confidential Transactions, mimblewimble šeme, itd.), ali javni lanac ne može sakriti grafikon transakcija.




- Lightning/State channels**


Državni kanali (kao kod Lightning Network) su skalabilniji i privatniji od Blockchain, jer se transakcije odvijaju off-chain. Međutim, obaveza javnog objavljivanja određenih Elements (transakcije finansiranja, topologija mreže) i praćenje mrežnog saobraćaja mogu delimično ugroziti poverljivost. Decentralizacija takođe trpi: rutiranje je intenzivno u pogledu gotovine, a glavni čvorovi mogu postati tačke centralizacije. Ovo je upravo fenomen koji počinjemo da primećujemo na Lightning-u.




- Client-side Validation (RGB)**


Ovaj novi paradigm je još skalabilniji i poverljiviji, jer ne samo da možemo integrisati tehnike dokaza znanja bez otkrivanja, već ne postoji globalni grafikon transakcija, pošto niko ne drži ceo registar. S druge strane, to takođe podrazumeva određeni kompromis u decentralizaciji: izdavalac Smart contract može imati centralnu ulogu (kao "Contract deployer" u Ethereumu). Međutim, za razliku od Blockchain, sa Client-side Validation, skladištite i validirate samo ugovore koji vas interesuju, što poboljšava skalabilnost izbegavanjem potrebe za preuzimanjem i verifikacijom svih postojećih stanja.


![RGB-Bitcoin](assets/fr/004.webp)


#### 2. CAP Teorem (Konzistentnost, Dostupnost, Tolerancija particionisanja)


Teorema CAP naglašava da je nemoguće da distribuirani sistem istovremeno zadovolji konzistentnost (*Consistency*), dostupnost (*Availability*) i toleranciju particionisanja (*Partition tolerance*).




- Blockchain**


Blockchain favorizuje doslednost i dostupnost, ali se ne snalazi dobro sa particionisanjem mreže: ako ne možete videti blok, ne možete delovati i imati isti pregled kao cela mreža.




- Munja** (in French)


Sistem državnih kanala ima dostupnost i toleranciju particionisanja (pošto dva čvora mogu ostati povezana međusobno čak i ako je mreža fragmentirana), ali ukupna konzistentnost zavisi od otvaranja i zatvaranja kanala na Blockchain.




- Client-side Validation (RGB)**


Sistem kao što je RGB nudi konzistentnost (svaki učesnik validira svoje podatke lokalno, bez nejasnoća) i toleranciju particionisanja (podatke čuvate autonomno), ali ne garantuje globalnu dostupnost (svako mora da se pobrine da ima relevantne delove istorije, a neki učesnici možda neće objaviti ništa ili će prestati da dele određene informacije).


![RGB-Bitcoin](assets/fr/005.webp)


#### 3. CIA trilema (Poverljivost, Integritet, Dostupnost)


Ova trilema nas podseća da poverljivost, integritet i dostupnost ne mogu svi biti optimizovani u isto vreme. Blockchain, Lightning i Client-side Validation se različito uklapaju u ovu ravnotežu. Ideja je da nijedan sistem ne može pružiti sve; neophodno je kombinovati nekoliko pristupa (Blockchain-ovo vremensko označavanje, Lightning-ov sinhroni pristup i lokalnu validaciju sa RGB) kako bi se dobio koherentan paket koji nudi dobre garancije u svakoj dimenziji.


![RGB-Bitcoin](assets/fr/006.webp)


### Uloga Blockchain i pojam shardinga


Blockchain (u ovom slučaju, Bitcoin) služi prvenstveno kao mehanizam za _vremensko označavanje_ i zaštitu protiv dvostrukog trošenja. Umesto umetanja kompletnih podataka Smart contract ili decentralizovanog sistema, jednostavno uključujemo **kriptografske obaveze** (_obaveze_) prema transakcijama (u smislu Client-side Validation, koje ćemo nazvati "tranzicije stanja"). Dakle :




- Oslobađamo Blockchain od velike količine podataka i logike;
- Svaki korisnik čuva samo istoriju potrebnu za svoj deo Contract (svoj "*Shard*"), umesto da replicira Global State.


Sharding je koncept koji je nastao u distribuiranim bazama podataka (npr. MySQL za društvene mreže kao što su Facebook ili Twitter). Da bi se rešio problem obima podataka i latencija sinhronizacije, baza podataka se segmentira u _shardove_ (SAD, Evropa, Azija, itd.). Svaki segment je lokalno konzistentan i samo delimično sinhronizovan sa ostalima.


Za pametne ugovore tipa RGB, mi Shard prema samim ugovorima. Svaki Contract je nezavisni _shard_. Na primer, ako posedujete samo USDT tokene, ne morate čuvati ili validirati celu istoriju drugog tokena kao što je USDC. Na Bitcoin, Blockchain ne radi _sharding_: imate globalni skup UTXO-a. Sa Client-side Validation, svaki učesnik zadržava samo Contract podatke koje drži ili koristi.


Stoga možemo zamisliti ekosistem na sledeći način:




- Blockchain (Bitcoin)** kao osnova koja osigurava potpunu replikaciju minimalnog registra i služi kao vremensko označavanje Layer;
- Lightning Network** za brzo, Confidential Transactions, i dalje zasnovan na bezbednosti i konačnom poravnanju Bitcoin Blockchain;
- RGB i Client-side Validation** da dodaju složeniju Smart contract logiku, bez zatrpavanja Blockchain ili gubitka poverljivosti.


![RGB-Bitcoin](assets/fr/007.webp)


Ova tri Elements formiraju trokutastu celinu, umesto linearnog niza "Layer 2", "Layer 3" i tako dalje. Munja se može direktno povezati sa Bitcoin, ili biti povezana sa Bitcoin transakcijama koje uključuju RGB podatke. Slično tome, "BiFi" upotreba (finansije na Bitcoin) može se kombinovati sa Blockchain, sa Munjom i sa RGB u skladu sa potrebama za poverljivošću, skalabilnošću ili Contract logikom.


![RGB-Bitcoin](assets/fr/008.webp)


### Pojam prelaza stanja


U bilo kom distribuiranom sistemu, cilj mehanizma validacije je da bude u stanju da **odredi validnost i hronološki redosled promena stanja**. Cilj je da se verifikuje da su pravila protokola poštovana i da se dokaže da ove promene stanja slede jedna za drugom u konačnom, neosporivom redosledu.


Da bismo razumeli kako ova validacija funkcioniše u kontekstu **Bitcoin** i, generalno, da bismo shvatili filozofiju iza Client-side Validation, hajde prvo da se osvrnemo na mehanizme Bitcoin i Blockchain, pre nego što vidimo kako se Client-side Validation razlikuje od njih i koje optimizacije omogućava.


![RGB-Bitcoin](assets/fr/009.webp)


U slučaju Bitcoin Blockchain, validacija transakcije zasniva se na jednostavnom pravilu:




- Svi mrežni čvorovi preuzimaju svaki blok i transakciju;
- Oni potvrđuju ove transakcije kako bi verifikovali tačnu evoluciju UTXO skupa (svi neutrošeni izlazi);
- Oni skladište ove podatke (u obliku blokova) kako bi se istorija mogla ponovo reprodukovati ako je potrebno.


![RGB-Bitcoin](assets/fr/010.webp)


Međutim, ovaj model ima dva glavna nedostatka:




- Skalabilnost**: pošto svaki čvor mora da obradi, verifikuje i arhivira transakcije svih korisnika, postoji očigledno ograničenje kapaciteta transakcija, posebno povezano sa maksimalnom veličinom bloka (1 MB u proseku na svakih 10 minuta za Bitcoin, isključujući kolačiće);
- Privatnost**: sve se emituje i skladišti javno (iznosi, odredišne adrese, itd.), što ograničava poverljivost razmena.


![RGB-Bitcoin](assets/fr/012.webp)


U praksi, ovaj model funkcioniše za Bitcoin kao osnovu Layer (Layer 1), ali može postati nedovoljan za složenije upotrebe koje istovremeno zahtevaju visok protok transakcija i određeni stepen poverljivosti.


Client-side Validation se zasniva na suprotnoj ideji: umesto da cela mreža mora da validira i čuva sve transakcije, svaki učesnik (klijent) će validirati samo deo istorije koji se tiče njega ili nje:




- Kada osoba primi sredstvo (ili bilo koju drugu digitalnu imovinu), potrebno je samo da zna i verifikuje lanac operacija (tranzicija stanja) koji vodi do tog sredstva i da dokaže njegovu legitimnost;
- Ova sekvenca operacija, od ***Genesis*** (početno izdanje) do najnovije transakcije, formira aciklični usmereni graf (DAG) ili Shard, tj. deo celokupne istorije.


![RGB-Bitcoin](assets/fr/013.webp)


Istovremeno, tako da ostatak mreže (ili preciznije, osnovni Layer, kao što je Bitcoin) može zaključati konačno stanje bez uvida u detalje ovih podataka, Client-side Validation se oslanja na pojam ***Commitment***.


*Commitment* je kriptografski Commitment, obično _hash_ (na primer SHA-256) umetnut u Bitcoin transakciju, koji dokazuje da su privatni podaci uključeni, bez otkrivanja tih podataka.


Zahvaljujući ovim _obavezama_, možemo dokazati:




- Postojanje informacija (pošto je posvećeno Hash) ;
- Anteriornost ove informacije (jer je usidrena i vremenski označena u Blockchain, sa datumom i redosledom blokova).


Međutim, tačan sadržaj nije otkriven, čime se čuva njegova poverljivost.


U konkretnim terminima, evo kako RGB State Transition funkcioniše:




- Pripremate novi State Transition (npr. prenos RGB tokena);
- Vi generate kriptografski Commitment na ovu tranziciju i umetnite ga u Bitcoin transakciju (ove obaveze se nazivaju "*sidra*" u RGB protokolu);
- Suprotna strana (primalac) preuzima istoriju sa strane korisnika povezanu sa ovom imovinom i potvrđuje doslednost od kraja do kraja, od Genesis Smart contract do prelaza koji mu šaljete.


![RGB-Bitcoin](assets/fr/014.webp)


Client-side Validation nudi dve glavne prednosti:




- Skalabilnost:**


Obaveze (*commitments*) uključene u Blockchain su male (reda veličine nekoliko desetina bajtova). Ovo osigurava da prostor bloka nije zasićen, jer je potrebno uključiti samo Hash. Takođe omogućava da se off-chain protokol razvija, jer svaki korisnik treba da čuva samo svoj fragment istorije (svoj _stash_).




- Privatnost :**


Transakcije same po sebi (tj. njihov detaljan sadržaj) nisu objavljene On-Chain. Objavljeni su samo njihovi otisci (*Hash*). Dakle, iznosi, adrese i Contract logika ostaju privatni, a primalac može lokalno verifikovati validnost svog Shard pregledom svih prethodnih tranzicija. Nema razloga da primalac učini ove podatke javnim, osim u slučaju spora ili kada je potreban dokaz.


U sistemu kao što je RGB, više prelaza stanja iz različitih ugovora (ili različitih sredstava) može biti agregirano u jednu Bitcoin transakciju putem jedne _obaveze_. Ovaj mehanizam uspostavlja determinističku, vremenski označenu vezu između On-Chain transakcije i off-chain podataka (klijentski validirani prelazi), i omogućava da se više šardova istovremeno zabeleži u jednoj Anchor tački, dodatno smanjujući trošak i otisak On-Chain.


U praksi, kada je ova transakcija Bitcoin validirana, ona trajno "zaključava" stanje osnovnih ugovora, jer postaje nemoguće modifikovati Hash već upisan u Blockchain.


![RGB-Bitcoin](assets/fr/015.webp)


### Koncept Stash


**Stash** je skup podataka na strani klijenta koje učesnik mora apsolutno zadržati kako bi održao integritet i istoriju RGB Smart contract. Za razliku od Lightning kanala, gde se određena stanja mogu lokalno rekonstruisati iz deljenih informacija, Stash od RGB Contract nije repliciran drugde: ako ga izgubite, niko neće moći da ga obnovi za vas, jer ste vi odgovorni za svoj deo istorije. Zato je potrebno usvojiti sistem sa pouzdanim procedurama za bekap u RGB.


![RGB-Bitcoin](assets/fr/016.webp)


### Single-Use Seal: poreklo i rad


Kada prihvatate sredstvo kao što je valuta, dve garancije su ključne:




- Autentičnost primljenog predmeta;
- Jedinstvenost primljenog predmeta, kako bi se izbegli dvostruki troškovi.


Za fizičku imovinu, kao što je novčanica, fizičko prisustvo je dovoljno da se dokaže da nije duplirana. Međutim, u digitalnom svetu, gde su sredstva isključivo informativna, ova verifikacija je složenija, jer se informacije lako mogu umnožiti i duplirati.


Kao što smo ranije videli, otkrivanje istorije promena stanja od strane pošiljaoca omogućava nam da osiguramo autentičnost RGB tokena. Imajući pristup svim transakcijama od Genesis transakcije, možemo potvrditi autentičnost tokena. Ovaj princip je sličan onom kod Bitcoin, gde se istorija novčića može pratiti unazad do originalnog Coinbase Transaction kako bi se verifikovala njihova validnost. Međutim, za razliku od Bitcoin, ova istorija promena stanja u RGB je privatna i čuva se na strani klijenta.


Da bismo sprečili Double-spending od RGB tokena, koristimo mehanizam nazvan "**Single-Use Seal**". Ovaj sistem osigurava da svaki token, kada se jednom iskoristi, ne može biti prevarno ponovo upotrebljen.


Jednokratne plombe su kriptografski primitivni elementi, koje je 2016. godine predložio Peter Todd, slične konceptu fizičkih plombi: kada se Seal postavi na kontejner, postaje nemoguće otvoriti ga ili izmeniti bez nepovratnog razbijanja Seal.


![RGB-Bitcoin](assets/fr/018.webp)


Ovaj pristup, prenesen u digitalni svet, omogućava dokazivanje da se niz događaja zaista odigrao i da se više ne može naknadno menjati. Jednokratne plombe tako prevazilaze jednostavnu logiku `Hash + Timestamp`, dodajući pojam Seal koji se može zatvoriti **samo jednom**.


![RGB-Bitcoin](assets/fr/017.webp)


Da bi jednokratne plombe funkcionisale, potreban vam je medijum za dokazivanje publikacije koji je sposoban da dokaže postojanje ili odsustvo publikacije, i koji je teško (ako ne i nemoguće) falsifikovati kada su informacije već distribuirane. **Blockchain** (kao i Bitcoin) može ispuniti ovu ulogu, kao i papirne novine sa javnom cirkulacijom, na primer. Ideja je sledeća:




- Želimo dokazati da je određeni Commitment na poruci `h(m)` objavljen publici bez otkrivanja sadržaja poruke `m` ;
- Želimo dokazati da nijedna druga konkurentna poruka `h(m')` Commitment nije objavljena umesto `h(m)` ;
- Takođe želimo da budemo u mogućnosti da proverimo da li poruka `m` postoji pre određenog datuma.


Blockchain se idealno uklapa u ovu ulogu: čim je transakcija uključena u blok, cela mreža ima isti neoborivi dokaz njenog postojanja i sadržaja (barem delimično, pošto _obaveza_ može sakriti detalje dok dokazuje autentičnost poruke).


Single-Use Seal se stoga može posmatrati kao formalno obećanje da će poruka (još uvek nepoznata u ovoj fazi) biti objavljena jednom i samo jednom, na način koji mogu verifikovati sve zainteresovane strane.


Za razliku od jednostavnih _obaveza_ (Hash) ili vremenskih oznaka, koje potvrđuju datum postojanja, Single-Use Seal nudi dodatnu garanciju da **nema alternativnog Commitment** koji može koegzistirati: ne možete zatvoriti isti Seal dva puta, niti pokušati zameniti zapečaćenu poruku.


Sledeće poređenje pomaže da se razume ovaj princip:




- Kriptografski Commitment (Hash)**: Sa funkcijom Hash, možete se obavezati na deo podataka (broj) objavljivanjem njegovog Hash. Podaci ostaju tajni dok ne otkrijete pre-image, ali možete dokazati da ste ih unapred znali;
- Timestamp (Blockchain)**: Umetanjem ovog Hash u Blockchain, takođe dokazujemo da smo to znali u tačnom trenutku (onog uključivanja u blok);
- Single-Use Seal**: Sa pečatima za jednokratnu upotrebu, idemo korak dalje čineći Commitment jedinstvenim. Sa jednim Hash, možete stvoriti nekoliko kontradiktornih obaveza paralelno (problem doktora koji objavljuje "*To je dečak*" porodici i "*To je devojčica*" u svom ličnom dnevniku). Single-Use Seal eliminiše ovu mogućnost povezivanjem Commitment sa medijumom za dokazivanje objavljivanja, kao što je Bitcoin Blockchain, tako da trošak UTXO definitivno zapečati Commitment. Jednom potrošen, isti UTXO ne može biti ponovo potrošen da zameni Commitment.


|                                                                                  | Simple commitment (digest/hash) | Timestamps | Single-use seals |
| -------------------------------------------------------------------------------- | ------------------------------- | ---------- | ---------------- |
| Publishing the commitment does not reveal the message                           | Yes                             | Yes        | Yes              |
| Proof of the commitment date / existence of the message before a certain date  | Impossible                      | Possible   | Possible         |
| Proof that no alternative commitment can exist                                 | Impossible                      | Impossible | Possible         |

Jednokratne plombe funkcionišu u tri glavne faze:


**Seal Definition :**




- Alice unapred definiše pravila za objavljivanje Seal (kada, gde i kako će poruka biti objavljena);
- Bob prihvata ili priznaje ove uslove.


![RGB-Bitcoin](assets/fr/021.webp)


**Seal Zatvaranje :**




- U vreme izvršavanja, Alisa zatvara Seal objavljivanjem stvarne poruke (obično u obliku _obaveze_, npr. Hash);
- Takođe pruža **svedoka** (kriptografski dokaz) koji dokazuje da je Seal zatvoren i neopoziv.


![RGB-Bitcoin](assets/fr/019.webp)


**Seal Verifikacija :**




- Jednom kada je Seal zatvoren, Bob ga više ne može otvoriti: može samo proveriti da li je zatvoren;
- Bob prikuplja Seal, **svedoka** i poruku (ili njegov Commitment) kako bi se uverio da se sve poklapa i da nema konkurentskih pečata ili različitih verzija.


Proces se može sažeti na sledeći način:


```txt
# Défini par Alice, validé ou accepté par Bob
seal <- Define()
# Fermeture du sceau par Alice avec le message
witness <- Close(seal, message)
# Vérification par Bob
bool <- Verify(seal, witness, message)
```


Client-side Validation, međutim, ide korak dalje: ako definicija Seal sama po sebi ostaje izvan Blockchain, moguće je (u teoriji) da neko ospori postojanje ili legitimnost dotične Seal. Da bi se prevazišao ovaj problem, koristi se lanac međusobno povezanih Jednokratnih Pečata:




- Svaki zatvoreni Seal sadrži definiciju sledećeg Seal;
- Registrujemo ova zatvaranja (sa njihovim _obavezama_) unutar Blockchain (u Bitcoin transakciji);
- Dakle, svaki pokušaj izmene prethodnog Seal bi bio u suprotnosti sa istorijom ugrađenom u Bitcoin.


Ovo je tačno ono što RGB sistem radi:




- Objavljene poruke su _obaveze_ prema podacima validiranim na strani klijenta;
- Seal Definition je povezan sa Bitcoin UTXO ;
- Seal se zatvara kada se ovaj UTXO potroši ili kada se novi izlaz pripiše istom Commitment;
- Lanac transakcija koji troši ove UTXO-e odgovara dokazu o objavljivanju: svaka tranzicija ili promena stanja na RGB je tako usidrena u Bitcoin.


Da sumiramo:




- Definicija _pečata_ je UTXO koju nameravate da Seal budući Commitment;
- _Zatvaranje pečata_ se dešava kada potrošite ovaj UTXO, stvarajući transakciju koja sadrži Commitment;
- _svedok_ je sama transakcija, koja dokazuje da ste zatvorili Seal sa ovim sadržajem;
- Ne možete dokazati da Seal nije zatvoren (ne možete biti apsolutno sigurni da UTXO već nije potrošen ili neće biti potrošen u bloku koji još niste videli), ali možete dokazati da je zaista zatvoren.


Ova jedinstvenost je važna za Client-side Validation: kada validirate State Transition, proveravate da li odgovara jedinstvenom UTXO, koji prethodno nije potrošen u konkurentskom Commitment. Ovo je ono što garantuje odsustvo dvostrukog trošenja u off-chain pametnim ugovorima.


### Višestruke obaveze i koreni


RGB Smart contract možda će morati da potroši nekoliko jednokratnih pečata (nekoliko UTXO-a) istovremeno. Štaviše, jedna Bitcoin transakcija može referencirati nekoliko različitih ugovora, od kojih svaki zapečaćuje svoj State Transition. Ovo zahteva mehanizam **multi-Commitment** da bi se dokazalo, deterministički i jedinstveno, da nijedna od obaveza ne postoji u duplikatu. Tu dolazi do izražaja pojam **Anchor** u RGB: posebna struktura koja povezuje Bitcoin transakciju i jednu ili više klijentskih obaveza (tranzicije stanja), od kojih svaka potencijalno pripada različitom Contract. Detaljnije ćemo razmotriti ovaj koncept u narednom poglavlju.


![RGB-Bitcoin](assets/fr/023.webp)


Dva glavna GitHub repozitorijuma projekta (pod LNPBP organizacijom) grupišu osnovne implementacije ovih koncepata proučenih u prvom poglavlju:




- client_side_validation** : Sadrži Rust primitive za lokalnu validaciju ;
- single_use_seals**: Implementira logiku za definisanje i sigurno zatvaranje ovih pečata.


![RGB-Bitcoin](assets/fr/020.webp)


Imajte na umu da su ovi softverski blokovi agnostički prema Bitcoin; u teoriji, mogli bi se primeniti na bilo koji drugi medij za dokazivanje objavljivanja (drugi registar, časopis, itd.). U praksi, RGB se oslanja na Bitcoin za svoju robusnost i široki konsenzus.


![RGB-Bitcoin](assets/fr/021.webp)


### Pitanja iz javnosti


#### Ka širem korišćenju jednokratnih pečata


Peter Todd je takođe kreirao protokol _Open Timestamps_, a koncept Single-Use Seal je prirodno proširenje ovih ideja. Pored RGB, mogu se zamisliti i drugi slučajevi upotrebe, kao što je konstrukcija _sidechains_ bez pribegavanja _merge mining_-u ili predlozima vezanim za drivechain kao što je BIP300. Bilo koji sistem koji zahteva jedan Commitment može, u principu, iskoristiti ovu kriptografsku primitivu. Danas je RGB prva velika implementacija u punom obimu.


#### Problemi dostupnosti podataka


Pošto u Client-side Validation, svaki korisnik čuva svoj deo istorije, dostupnost podataka nije globalno zagarantovana. Ako izdavalac Contract zadrži ili opozove određene informacije, možda nećete biti svesni stvarne evolucije ponude. U nekim slučajevima (kao što su stablecoins), očekuje se da izdavalac održava javne podatke kako bi dokazao obim u opticaju, ali ne postoji tehnička obaveza da to učini. Stoga je moguće dizajnirati namerno neprozirne ugovore sa neograničenim Supply, što postavlja pitanja poverenja.


#### Sharding i izolacija Contract


Svaki Contract predstavlja izolovani _shard_: USDT i USDC, na primer, ne moraju deliti svoje istorije. Atomski swapovi su i dalje mogući, ali to ne uključuje spajanje njihovih registara. Sve se obavlja kriptografskim Commitment, bez otkrivanja celokupnog istorijskog grafa svakom učesniku.


### Zaključak


Videli smo gde se koncept Client-side Validation uklapa sa Blockchain i _state channels_, kako odgovara na trileme distribuiranog računarstva, i kako jedinstveno koristi Bitcoin Blockchain da izbegne Double-spending i za *time-stamping*. Ideja se zasniva na pojmu **Single-Use Seal**, omogućavajući kreiranje jedinstvenih obaveza koje ne možete ponovo trošiti po volji. Na ovaj način, svaki učesnik učitava samo istoriju koja je strogo neophodna, povećavajući skalabilnost i poverljivost pametnih ugovora dok zadržava sigurnost Bitcoin kao pozadinu.


Sledeći korak će biti da se detaljnije objasni kako se ovaj mehanizam Single-Use Seal primenjuje u Bitcoin (putem UTXO-a), kako se kreiraju i validiraju sidra, a zatim kako se kompletni pametni ugovori grade u RGB. Posebno ćemo se osvrnuti na pitanje višestrukih obaveza, tehnički izazov dokazivanja da Bitcoin transakcija istovremeno zapečaćuje višestruke prelaze stanja u različitim ugovorima, bez uvođenja ranjivosti ili dvostrukih obaveza.


Pre nego što se upustite u tehničke detalje drugog poglavlja, slobodno ponovo pročitajte ključne definicije (Client-side Validation, Single-Use Seal, sidra, itd.) i imajte na umu celokupnu logiku: nastojimo da pomirimo snage Bitcoin Blockchain (bezbednost, decentralizacija, vremensko označavanje) sa onima off-chain rešenja (brzina, poverljivost, skalabilnost), i upravo to RGB i Client-side Validation pokušavaju da postignu.


## Commitment Layer


<chapterId>cc2fe85a-9cc7-5b8c-a00a-c0a867241061</chapterId>


:::video id=73ddea2d-c243-479d-a3dc-12d7db8eef70:::


U ovom poglavlju ćemo pogledati implementaciju Client-side Validation i Jednokratnih Pečata unutar Bitcoin Blockchain. Predstavićemo glavne principe RGB-ovog **Commitment Layer** (Layer 1), sa posebnim fokusom na **TxO2** šemu, koju RGB koristi za definisanje i zatvaranje Seal u Bitcoin transakciji. Zatim ćemo diskutovati o dve važne tačke koje još nisu detaljno pokrivene:




- _determinističke Bitcoin obaveze_;
- Višestruke protokolarne obaveze.


To je kombinacija ovih koncepata koja nam omogućava da superponiramo nekoliko sistema ili ugovora na jedan UTXO i stoga jedan Blockchain.


Treba imati na umu da se opisane kriptografske operacije mogu primeniti, u apsolutnim terminima, na druge blokčejnove ili medije za objavljivanje, ali karakteristike Bitcoin (u smislu decentralizacije, otpornosti na cenzuru i otvorenosti za sve) čine ga idealnom osnovom za razvoj napredne programabilnosti kao što je ona koju zahteva **RGB**.


### Commitment šeme u Bitcoin i njihova upotreba od strane RGB


Kao što smo videli u prvom poglavlju kursa, Jednokratni pečati su opšti koncept: dajemo obećanje da ćemo uključiti Commitment (_commitment_) na specifično mesto u transakciji, i ovo mesto deluje kao Seal koji zatvaramo na poruci. Međutim, na Bitcoin Blockchain, postoji nekoliko opcija za izbor gde postaviti ovu _commitment_.


Da bismo razumeli logiku, prisetimo se osnovnog principa: da bismo zatvorili _jednokratni pečat_, trošimo zapečaćeno područje ubacivanjem _obaveze_ na datu poruku. U Bitcoin, ovo se može uraditi na nekoliko načina:




- Koristite javni ključ ili Address**


Možemo odlučiti da je određeni javni ključ ili Address _jednokratni pečat_. Čim se ovaj ključ ili Address pojavi On-Chain u transakciji, to znači da je Seal zatvoren sa određenom porukom.




- Koristite izlaz transakcije Bitcoin**


To znači da je _jednokratni pečat_ definisan kao precizan _outpoint_ (par txid + izlazni broj). Čim je ovaj _outpoint_ potrošen, Seal se zatvara.


Dok radeći na RGB, identifikovali smo najmanje 4 različita načina za implementaciju ovih zaptivki na Bitcoin:




- Definiši Seal putem javnog ključa i zatvori ga u _output_ ;
- Definiši Seal sa _outpoint_ i zatvori ga sa _output_ ;
- Definiši Seal putem vrednosti javnog ključa i zatvori ga u _input_ ;
- Definiši Seal putem _outpoint_-a, i zatvori ga u _input_-u.


| Schema Name | Seal Definition           | Seal Closure              | Additional Requirements                                        | Main Application            | Possible Commitment Schemes     |
| ----------- | ------------------------- | ------------------------- | -------------------------------------------------------------- | --------------------------- | -------------------------------- |
| PkO         | Public Key Value          | Transaction Output        | P2(W)PKH                                                       | None at the moment          | Keytweak, taptweak, opret       |
| TxO2        | Transaction Output        | Transaction Output        | Requires deterministic commitments on Bitcoin                  | RGBv1 (universal)           | Keytweak, tapret, opret         |
| PkI         | Public Key Value          | Transaction Input         | Taproot only & not compatible with legacy wallets              | Bitcoin-based identities    | Sigtweak, witweak               |
| TxO1        | Transaction Output        | Transaction Input         | Taproot only & not compatible with legacy wallets              | None at the moment          | Sigtweak, witweak               |


Nećemo ulaziti u detalje o svakoj od ovih konfiguracija, jer smo u RGB odlučili da koristimo **_outpoint_ kao definiciju Seal**, i da postavimo _commitment_ u izlaz transakcije koja troši ovaj _outpoint_. Stoga možemo uvesti sledeće pojmove za nastavak:




- "Seal Definition "** : Dati _outpoint_ (identifikovan sa txid + broj izlaza) ;
- "Seal zatvaranje" **: Transakcija koja troši ovaj _outpoint_, u kojoj je _commitment_ dodat poruci.


Ova šema je odabrana zbog svoje kompatibilnosti sa RGB arhitekturom, ali druge konfiguracije bi mogle biti korisne za različite namene.


"O2" u "TxO2" nas podseća da su i definicija i zatvaranje zasnovani na trošku (ili kreiranju) izlaza transakcije.


### Primer TxO2 dijagrama


Kao podsetnik, definisanje _jednokratnog pečata_ ne zahteva nužno objavljivanje On-Chain transakcije. Dovoljno je da, na primer, Alisa već ima neiskorišćen UTXO. Ona može odlučiti: "Ovaj _outpoint_ (već postojeći) je sada moj Seal". Ona to beleži lokalno (_klijent-strana_), i dokle god ovaj UTXO nije potrošen, Seal se smatra otvorenim.


![RGB-Bitcoin](assets/fr/024.webp)


Na dan kada želi da zatvori Seal (da signalizira događaj, ili da Anchor pošalje određenu poruku), troši ovaj UTXO u novoj transakciji (ova transakcija se često naziva "_witness transaction_" (nije povezano sa _segwit_, to je samo termin koji koristimo). Ova nova transakcija će sadržati _commitment_ na poruku.


![RGB-Bitcoin](assets/fr/025.webp)


Imajte na umu da u ovom primeru :




- Niko osim Boba (ili ljudi kojima Alisa odluči da otkrije ceo dokaz) neće znati da je određena poruka skrivena u ovoj transakciji;
- Svi mogu videti da je _outpoint_ potrošen, ali samo Bob ima dokaz da je poruka zapravo usidrena u transakciji.


Da bismo ilustrovali ovu TxO2 šemu, možemo koristiti _jednokratni pečat_ kao mehanizam za opoziv PGP ključa. Umesto objavljivanja sertifikata o opozivu na serverima, Alisa može reći: "Ovaj Bitcoin izlaz, ako se potroši, znači da je moj PGP ključ opozvan".


Alice stoga ima specifičan UTXO, sa kojim je određeno stanje ili podaci (poznati samo njoj) povezano lokalno (na strani klijenta).


Alice obaveštava Boba da ako se ovaj UTXO potroši, određeni događaj će se smatrati da se desio. Sa spoljašnje strane, sve što vidimo je Bitcoin transakcija; ali Bob zna da ova potrošnja ima skriveno značenje.


![RGB-Bitcoin](assets/fr/026.webp)


Kako Alice troši ovaj UTXO, ona zatvara Seal porukom koja ukazuje na njen novi ključ, ili jednostavno opoziv starog. Na ovaj način, svako ko prati On-Chain će videti da je UTXO potrošen, ali samo oni sa punim dokazom će znati da je to upravo opoziv PGP ključa.


![RGB-Bitcoin](assets/fr/027.webp)


Da bi Bob ili bilo ko drugi umešan mogao da proveri skrivenu poruku, Alisa mora da mu obezbedi off-chain informacije.


![RGB-Bitcoin](assets/fr/028.webp)


Alice stoga mora obezbediti Bobu:




- Poruka sama po sebi (na primer, novi PGP ključ) ;
- Kriptografski dokaz da je poruka bila uključena u transakciju (poznat kao _dodatni dokaz transakcije_ ili _sidro_).


![RGB-Bitcoin](assets/fr/029.webp)


Treća lica nemaju ove informacije. Oni samo vide da je UTXO potrošen. Povjerljivost je stoga osigurana.


Da bismo pojasnili strukturu, hajde da sumiramo proces u dve transakcije:




- Transakcija 1**: Ovo sadrži _definiciju pečata_, tj. _outpoint_ koji će služiti kao Seal.


![RGB-Bitcoin](assets/fr/031.webp)




- Transakcija 2**: Troši ovaj _outpoint_. Ovo zatvara Seal i, u istoj transakciji, ubacuje _commitment_ na poruku.


![RGB-Bitcoin](assets/fr/033.webp)


Stoga drugi transakciju nazivamo "_witness transaction_".


Da bismo ovo ilustrovali iz drugog ugla, možemo predstaviti dva sloja:




- The top Layer (Blockchain, public)**: everyone sees the transaction and knows that a _outpoint_ has been spent;
- Donji Layer (klijentska strana, privatno)** : samo Alisa (ili osoba na koju se odnosi) zna da ovaj trošak odgovara toj i toj poruci, putem kriptografskog dokaza i poruke koju čuva lokalno.


![RGB-Bitcoin](assets/fr/034.webp)


Ali kada se zatvara Seal, postavlja se pitanje gde bi _commitment_ trebalo umetnuti


U prethodnom delu smo ukratko pomenuli kako se model Client-side Validation može primeniti na RGB i druge sisteme. Ovde se bavimo delom o **determinističkim Bitcoin obavezama** i kako ih integrisati u transakciju. Ideja je razumeti zašto pokušavamo da ubacimo jedan Commitment u _transakciju svedoka_, i pre svega kako osigurati da ne može biti drugih neotkrivenih konkurentskih obaveza.


### Commitment lokacije u transakciji


Kada nekome date dokaz da je određena poruka ugrađena u transakciju, morate biti u mogućnosti da garantujete da ne postoji drugi oblik Commitment (druga, skrivena poruka) u istoj transakciji koji vam nije otkriven. Da bi Client-side Validation ostao robustan, potreban vam je **deterministički** mehanizam za postavljanje jedne _obaveze_ u transakciju koja zatvara _jednokratni pečat_.


Transakcija _svedoka_ troši čuveni UTXO (ili _definiciju pečata_) i ova potrošnja odgovara zatvaranju Seal. Tehnički gledano, znamo da se svaki outpoint može potrošiti samo jednom. Ovo je upravo ono što podržava otpornost Bitcoin na dvostruku potrošnju. Ali transakcija potrošnje može imati nekoliko _ulaza_, nekoliko _izlaza_, ili biti sastavljena na složen način (coinjoins, Lightning kanali, itd.). Stoga moramo jasno definisati gde da umetnemo _obavezu_ u ovu strukturu, nedvosmisleno i ujednačeno.


Koji god metod (PkO, TxO2, itd.), _obaveza_ se može umetnuti :




- U unosu** putem :
    - Sigtweak** (modifikuje `r` komponentu ECDSA potpisa, slično principu "Sign-to-Contract") ;
    - Witweak** (podatak _segregated witness_ transakcije je izmenjen).
- U Izlazu** putem :
    - Keytweak** (javni ključ primaoca je "prilagođen" sa porukom) ;
    - Opret** (poruka je postavljena u nepotrošivi izlaz `OP_RETURN`) ;
    - Tapret** (ili _Taptweak_), koji se oslanja na Taproot da umetne Commitment u skriptni deo Taproot ključa, čime se javni ključ deterministički modifikuje.


![RGB-Bitcoin](assets/fr/035.webp)


Evo detalja o svakoj metodi:


![RGB-Bitcoin](assets/fr/038.webp)


***Sig prilagodba (sign-to-Contract) :***


Raniji plan je uključivao iskorišćavanje nasumičnog dela potpisa (ECDSA ili Schnorr) za ugradnju _commitment_-a: ovo je tehnika poznata kao "**Sign-to-Contract**". Zamenjujete nasumično generisani Nonce sa Hash koji sadrži podatke. Na ovaj način, potpis implicitno otkriva vaš Commitment, bez dodatnog prostora u transakciji. Ovaj pristup ima nekoliko prednosti:




- Nema On-Chain preopterećenja (koristite isto mesto kao osnovni Nonce);
- U teoriji, ovo može biti prilično diskretno, jer je Nonce u početku nasumičan podatak.


Međutim, pojavila su se 2 glavna nedostatka:




- Multisig pre Taproot: kada imate nekoliko potpisnika, morate odlučiti koji potpis će nositi _obavezu_. Potpisi se mogu različito redoslediti, a ako potpisnik odbije, gubite kontrolu nad ishodom _obaveze_;
- MuSig i deljeni Nonce: sa Schnorr Multisig (*MuSig*), generisanje Nonce je algoritam sa više učesnika, i postaje praktično nemoguće pojedinačno prilagoditi Nonce.


U praksi, **sig tweak** takođe nije baš kompatibilan sa postojećim hardverom (hardverski novčanici) i formatima (Lightning, itd.). Dakle, ova sjajna ideja je Hard da se sprovede u praksi.


***Ključna izmena (pay-to-Contract) :***


**ključna izmena** preuzima istorijski koncept _plaćanja po ugovoru_. Uzimamo javni ključ `X` i menjamo ga dodavanjem vrednosti `H(poruka)`. Konkretno, ako je `X = x * G` i `h = H(poruka)`, tada će novi ključ biti `X' = X + h * G`. Ovaj izmenjeni ključ skriva Commitment u `poruka`. Vlasnik originalnog privatnog ključa može, dodavanjem `h` svom privatnom ključu `x`, dokazati da ima ključ za trošenje izlaza. U teoriji, ovo je elegantno, jer :




- _Obaveza_ se unosi bez dodavanja bilo kakvih dodatnih polja;
- Ne čuvate dodatne On-Chain podatke.


U praksi, međutim, nailazimo na sledeće poteškoće:




- Novčanici više ne prepoznaju standardni javni ključ, jer je on "podešen", tako da ne mogu lako povezati UTXO sa vašim uobičajenim ključem;
- Hardverski novčanici nisu dizajnirani da potpisuju ključem koji nije izveden iz njihove standardne derivacije;
- Morate prilagoditi svoje skripte, opise, itd.


U kontekstu RGB, ova putanja je bila zamišljena do 2021, ali se pokazalo da je previše komplikovano da bi funkcionisalo sa trenutnim standardima i infrastrukturom.


***Svedok prilagoditi :***


Još jedna ideja, koju su određeni protokoli kao što su _inscriptions Ordinals_ sproveli u praksi, jeste da se podaci postave direktno u `witness` sekciju transakcije (otuda izraz "witness tweak"). Međutim, ova metoda :




- Čini angažman odmah vidljivim (bukvalno nalepite sirove podatke u svedoka);
- Može biti podložno cenzuri (rudari ili čvorovi mogu odbiti da proslede ako je preveliko ili ima bilo koju drugu proizvoljnu karakteristiku);
- Troši prostor u blokovima, suprotno cilju diskrecije i lakoće RGB.


Pored toga, svedok je dizajniran da bude podložan skraćivanju u određenim kontekstima, što može učiniti da robusni dokazi budu složeniji.


***Otvorena povratna karta (opret) :***


Vrlo jednostavan u svom radu, `OP_RETURN` vam omogućava da sačuvate Hash ili poruku u specijalnom polju transakcije. Ali to je odmah otkriveno: svi vide da postoji _commitment_ u transakciji, i može biti cenzurisan ili odbačen, kao i dodavanje dodatnog izlaza. Pošto ovo povećava transparentnost i veličinu, smatra se manje zadovoljavajućim sa stanovišta Client-side Validation rešenja.


```txt
34-byte_Opret_Commitment =
OP_RETURN   OP_PUSHBYTE_32   <mpc::Commitment>
|_________| |______________| |_________________|

1-byte       1-byte         32 bytes
```


### Tapret


Konačna opcija je upotreba **Taproot** (uveden sa BIP341) sa šemom *Tapret*. *Tapret* je složeniji oblik determinističkog Commitment, koji donosi poboljšanja u pogledu otiska na Blockchain i poverljivosti za Contract operacije. Glavna ideja je sakriti Commitment u delu `Script Path Spend` [Taproot transakcije](https://github.com/Bitcoin/bips/blob/master/bip-0341.mediawiki).


![RGB-Bitcoin](assets/fr/036.webp)


Pre nego što opišemo kako se Commitment ubacuje u Taproot transakciju, pogledajmo **tačan oblik** Commitment, koji mora **imperativno** odgovarati nizu od 64 bajta [konstruisanom](https://github.com/BP-WG/bp-core/blob/master/dbc/src/tapret/mod.rs#L179-L196) na sledeći način:


```txt
64-byte_Tapret_Commitment =
OP_RESERVED ...  ... .. OP_RESERVED   OP_RETURN   OP_PUSHBYTE_33  <mpc::Commitment>  <Nonce>
|___________________________________| |_________| |______________| |_______________|  |______|
OP_RESERVED x 29 times = 29 bytes      1 byte         1 byte          32 bytes        1 byte
|________________________________________________________________| |_________________________|

TAPRET_SCRIPT_COMMITMENT_PREFIX = 31 bytes                    MPC commitment + NONCE = 33 bytes
```




- 29 bajtova `OP_RESERVED`, zatim `OP_RETURN`, pa `OP_PUSHBYTE_33`, čine 31-bajtni _prefiks_ deo;
- Sledeći dolazi 32-bajtni _commitment_ (obično Merkle Root iz **MPC**), kojem dodajemo 1 bajt **Nonce** (ukupno 33 bajta za ovaj drugi deo).


Dakle, 64-bajtni metod `Tapret` izgleda kao `Opret` kojem smo dodali prefiks od 29 bajtova `OP_RESERVED` i dodali dodatni bajt kao Nonce.


Da bi se održala fleksibilnost u pogledu implementacije, poverljivosti i skaliranja, Tapret šema uzima u obzir različite slučajeve upotrebe, u zavisnosti od zahteva:




- Jedinstvena inkorporacija Tapret Commitment u transakciju Taproot bez unapred postojećeg Script Path okvira;
- Integracija Tapret Commitment u Taproot transakciju koja je već opremljena Script Path-om.


Hajde da detaljnije pogledamo svaki od ova dva scenarija.


#### Tapret inkorporacija bez postojećeg Script Path


U ovom prvom slučaju, počinjemo od Taproot izlaznog ključa (*Taproot Output Key*) `Q` koji sadrži samo interni javni ključ `P` *(Internal Key*), bez pridruženog putanje skripte (*Script Path*):


![RGB-Bitcoin](assets/fr/047.webp)




- `P`: interni javni ključ za _Key Path Spend_.
- `G`: generišuća tačka eliptičke krive [secp256k1](https://en.Bitcoin.it/wiki/Secp256k1).
- t = tH_TWEAK(P)` je faktor prilagođavanja, izračunat putem _označenog heša_ (npr. `SHA-256(SHA-256(TapTweak) || P)`), u skladu sa [BIP86](https://github.com/Bitcoin/bips/blob/master/bip-0086.mediawiki#Address-derivation). Ovo dokazuje da nema skrivenog skripta.


Da biste uključili **Tapret** Commitment, dodajte **Putanju skripte potrošnje** sa **jedinstvenom skriptom**, na sledeći način:


![RGB-Bitcoin](assets/fr/048.webp)




- t = tH_TWEAK(P || Script_root)` zatim postaje novi faktor prilagođavanja, uključujući **Script_root**.
- `Script_root = tH_BRANCH(64-byte_Tapret_Commitment)` predstavlja koren ovog **skripta**, koji je jednostavno Hash tipa `SHA-256(SHA-256(TapBranch) || 64-byte_Tapret_Commitment)`.


Dokaz o uključenju i jedinstvenosti u Taproot stablu ovde se svodi na jedini interni javni ključ `P`.


#### Integracija Tapret-a u već postojeći Script Path


Drugi scenario se odnosi na složeniji `Q` Taproot** izlaz, koji već sadrži nekoliko skripti. Na primer, imamo stablo od 3 skripte:


![RGB-Bitcoin](assets/fr/049.webp)




- tH_LEAF(x)` označava normalizovanu označenu Hash funkciju skripta lista.
- a, B, C` predstavljaju skripte već uključene u Taproot strukturu.


Da bismo dodali Tapret Commitment, potrebno je umetnuti *nepotrošiv skript* na prvom nivou stabla, pomerajući postojeće skripte jedan nivo niže. Vizuelno, stablo postaje :


![RGB-Bitcoin](assets/fr/050.webp)




- tHABC` predstavlja označeni Hash najvišeg nivoa grupe `A, B, C`.
- tHT` predstavlja Hash skripta koji odgovara 64-bajtnoj `Tapret`.


Prema pravilima Taproot, svaka grana/list mora biti kombinovana prema leksikografskom Hash redosledu. Postoje dva moguća slučaja:




- `tHT` > `tHABC`: Tapret Commitment se pomera desno od drveta. Dokaz jedinstvenosti zahteva samo `tHABC` i `P` ;
- tHT` < `tHABC`**: Tapret Commitment je postavljen na levoj strani. Da bi se dokazalo da nema drugog Tapret Commitment sa desne strane, `tHAB` i `tHC` moraju biti otkriveni kako bi se pokazalo odsustvo bilo kojeg drugog takvog skripta.


Vizuelni primer za prvi slučaj (`tHABC < tHT`):


![RGB-Bitcoin](assets/fr/051.webp)


Primer za drugi slučaj (`tHABC > tHT`):


![RGB-Bitcoin](assets/fr/052.webp)


#### Optimizacija sa Nonce


Da bismo poboljšali poverljivost, možemo "rudarenjem" (tačniji termin bi bio "bruteforcing") doći do vrednosti `<Nonce>` (poslednji bajt od 64-bajtne `Tapret`) u pokušaju da dobijemo Hash `tHT` takav da `tHABC < tHT`. U ovom slučaju, Commitment je postavljen sa desne strane, čime se korisnik oslobađa potrebe da otkriva ceo sadržaj postojećih skripti kako bi dokazao jedinstvenost Tapreta.


Ukratko, `Tapret` nudi diskretan i deterministički način uključivanja Commitment u Taproot transakciju, uz poštovanje zahteva za jedinstvenost i nedvosmislenost koji su esencijalni za RGB's Client-side Validation i Single-Use Seal logiku.


#### Važeći izlazi


Za transakcije RGB Commitment, glavni zahtev za važeću šemu Bitcoin Commitment je sledeći: Transakcija (*Witness Transaction*) mora dokazivo sadržati jedan Commitment. Ovaj zahtev onemogućava konstruisanje alternativne istorije za podatke validirane na strani klijenta unutar iste transakcije. To znači da je poruka oko koje se _jednokratni pečat_ zatvara jedinstvena.


Da bi se ispunio ovaj princip, i bez obzira na broj izlaza u transakciji, zahtevamo da **jedan i samo jedan izlaz** može sadržati Commitment (*Commitment*). Za svaku od korišćenih šema (*Opret* ili *Tapret*), jedini validni izlazi koji mogu sadržati RGB _commitment_ su:




- Prvi izlaz `OP_RETURN` (ako je prisutan) za *Opret* šemu;
- Prvi Taproot izlaz (ako je prisutan) za šemu *Tapret*.


Imajte na umu da je sasvim moguće da transakcija sadrži jedan `Opret` Commitment i jedan `Tapret` Commitment u dva odvojena izlaza. Zahvaljujući determinističkoj prirodi Seal Definition, ove dve obaveze tada odgovaraju dvema različitim delovima podataka validiranim na strani klijenta.


### Analiza i praktični izbori u RGB


Kada smo započeli RGB, pregledali smo sve ove metode kako bismo odredili gde i kako postaviti _commitment_ u transakciji na deterministički način. Definisali smo neke kriterijume:




- Kompatibilnost sa različitim scenarijima (npr. Multisig, Lightning, hardverski novčanici, itd.);
- Uticaj na On-Chain prostor ;
- Teškoća implementacije i održavanja ;
- Poverljivost i otpornost na cenzuru.


| Method                                             | On-chain trace & size | Client-side size | Wallet Integration | Hardware Compatibility | Lightning Compatibility | Taproot Compatibility |
| -------------------------------------------------- | --------------------- | ---------------- | ------------------ | ---------------------- | ---------------------- | --------------------- |
| Keytweak (deterministic P2C)                      | 🟢                     | 🟡                 | 🔴                   | 🟠                     | 🔴 BOLT, 🔴 Bifrost     | 🟠 Taproot, 🟢 MuSig  |
| Sigtweak (deterministic S2C)                      | 🟢                     | 🟢                 | 🟠                   | 🔴                     | 🔴 BOLT, 🔴 Bifrost     | 🟠 Taproot, 🔴 MuSig  |
| Opret (OP_RETURN)                                 | 🔴                     | 🟢                 | 🟢                   | 🟠                     | 🔴 BOLT, 🟠 Bifrost     | -                     |
| Tapret Algorithm: top-left node                   | 🟠                     | 🔴                 | 🟠                   | 🟢                     | 🔴 BOLT, 🟢 Bifrost     | 🟢 Taproot, 🟢 MuSig  |
| Tapret Algorithm #4: any node + proof             | 🟢                     | 🟠                 | 🟠                   | 🟢                     | 🔴 BOLT, 🟢 Bifrost     | 🟢 Taproot, 🟢 MuSig  |
| Deterministic Commitment Scheme                               | Standard       | On-Chain Cost                                                                                                          | Proof Size on Client Side                                                                                       |
| ------------------------------------------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Keytweak (Deterministic P2C)                                  | LNPBP-1, 2     | 0 bytes                                                                                                                | 33 bytes (non-tweaked key)                                                                                       |
| Sigtweak (Deterministic S2C)                                  | WIP (LNPBP-39) | 0 bytes                                                                                                                | 0 bytes                                                                                                          |
| Opret (OP_RETURN)                                             | -              | 36 (v)bytes (additional TxOut)                                                                                         | 0 bytes                                                                                                          |
| Tapret Algorithm: top-left node                               | LNPBP-6        | 32 bytes in the witness (8 vbytes) for any n-of-m multisig and spending through script path                           | 0 bytes on scriptless scripts taproot ~270 bytes in a single script case, ~128 bytes if multiple scripts       |
| Tapret Algorithm #4: any node + uniqueness proof              | LNPBP-6        | 32 bytes in the witness (8 vbytes) for single script cases, 0 bytes in the witness in most other cases                | 0 bytes on scriptless scripts taproot, 65 bytes until the Taptree contains a dozen scripts                      |


| Layer                          | On-Chain Cost (Bytes/vbytes) | On-Chain Cost (Bytes/vbytes) | On-Chain Cost (Bytes/vbytes) | On-Chain Cost (Bytes/vbytes) | On-Chain Cost (Bytes/vbytes) | Client-Side Cost (Bytes) | Client-Side Cost (Bytes) | Client-Side Cost (Bytes) | Client-Side Cost (Bytes) | Client-Side Cost (Bytes) |
| ------------------------------ | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ------------------------ | ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| **Type**                       | **Tapret**                   | **Tapret #4**                | **Keytweak**                 | **Sigtweak**                 | **Opret**                    | **Tapret**               | **Tapret #4**            | **Keytweak**             | **Sigtweak**             | **Opret**                |
| Single-sig                     | 0                            | 0                            | 0                            | 0                            | 32                           | 0                        | 0                        | 32                       | 0?                       | 0                        |
| MuSig (n-of-n)                 | 0                            | 0                            | 0                            | 0                            | 32                           | 0                        | 0                        | 32                       | ? > 0                    | 0                        |
| Multi-sig 2-of-3               | 32/8                         | 32/8 or 0                    | 0                            | n/a                          | 32                           | ~270                     | 65                       | 32                       | n/a                      | 0                        |
| Multi-sig 3-of-5               | 32/8                         | 32/8 or 0                    | 0                            | n/a                          | 32                           | ~340                     | 65                       | 32                       | n/a                      | 0                        |
| Multi-sig 2-of-3 with timeouts | 32/8                         | 0                            | 0                            | n/a                          | 32                           | 64                       | 65                       | 32                       | n/a                      | 0                        |


| Layer                            | On-Chain Cost (vbytes) | On-Chain Cost (vbytes) | On-Chain Cost (vbytes) | Client-Side Cost (bytes) | Client-Side Cost (bytes) |
| -------------------------------- | ---------------------- | ---------------------- | ---------------------- | ------------------------ | ------------------------ |
| **Type**                         | **Base**               | **Tapret #2**          | **Tapret #4**          | **Tapret #2**            | **Tapret #4**            |
| MuSig (n-of-n)                   | 16.5                   | 0                      | 0                      | 0                        | 0                        |
| FROST (n-of-m)                   | ?                      | 0                      | 0                      | 0                        | 0                        |
| Multi_a (n-of-m)                 | 1+16n+8m               | 8                      | 8                      | 33 * m                   | 65                       |
| Branch MuSig / Multi_a (n-of-m)  | 1+16n+8n+8xlog(n)      | 8                      | 0                      | 64                       | 65                       |
| With timeouts (n-of-m)           | 1+16n+8n+8xlog(n)      | 8                      | 0                      | 64                       | 65                       |
| Method                                    | Privacy & Scalability | Interoperability | Compatibility | Portability | Complexity |
| ----------------------------------------- | ---------------------- | ---------------- | ------------- | ----------- | ---------- |
| Keytweak (Deterministic P2C)              | 🟢                      | 🔴               | 🔴            | 🟡          | 🟡         |
| Sigtweak (Deterministic S2C)              | 🟢                      | 🔴               | 🔴            | 🟢          | 🔴         |
| Opret (OP_RETURN)                         | 🔴                      | 🟠               | 🔴            | 🟢          | 🟢         |
| Algo Tapret: Top-left node                | 🟠                      | 🟢               | 🟢            | 🔴          | 🟠         |
| Algo Tapret #4: Any node + proof          | 🟢                      | 🟢               | 🟢            | 🟠          | 🔴         |






Tokom studije, postalo je jasno da nijedna od Commitment šema nije bila potpuno kompatibilna sa trenutnim Lightning standardom (koji ne koristi Taproot, _muSig2_ ili dodatnu _commitment_ podršku). U toku su napori da se modifikuje Lightning-ova konstrukcija kanala (*BiFrost*) kako bi se omogućilo umetanje RGB commitment-a. Ovo je još jedno područje gde treba da pregledamo strukturu transakcija, ključeve i način na koji se ažuriranja kanala potpisuju.


Analiza je pokazala da su, zapravo, druge metode (key tweak, sig tweak, witness tweak, itd.) predstavile druge oblike komplikacija:




- Ili imamo veliki On-Chain volumen;
- Ili postoji radikalna nekompatibilnost sa postojećim Wallet kodom;
- Ili je rešenje neizvodljivo u nekooperativnom Multisig.


Za RGB, posebno se izdvajaju dve metode: ***Opret*** i ***Tapret***, obe klasifikovane kao "Transaction Output", i kompatibilne sa TxO2 režimom koji koristi protokol.


### Višestruke Protokolne Obaveze - MPC


U ovom odeljku, razmatramo kako **RGB** upravlja agregacijom više ugovora (ili, preciznije, njihovih _transition bundles_) unutar jednog Commitment (*Commitment*) zabeleženog u Bitcoin transakciji putem determinističke šeme (prema `Opret` ili `Tapret`). Da bi se to postiglo, redosled Merkelizacije različitih ugovora odvija se u strukturi nazvanoj **MPC Tree** (_Multi Protocol Commitment Tree_). U ovom odeljku, razmotrićemo konstrukciju ovog MPC Tree, kako dobiti njegov koren, i kako više ugovora može deliti istu transakciju poverljivo i nedvosmisleno.


Multi Protocol Commitment (MPC) je dizajniran da zadovolji dve potrebe:




- Izgradnja `mpc::Commitment` Hash: ovo će biti uključeno u Bitcoin Blockchain prema šemi `Opret` ili `Tapret`, i mora odražavati sve promene stanja koje treba validirati;
- Istovremeno skladištenje više ugovora u jednoj _obavezi_, omogućavajući zasebna ažuriranja na više sredstava ili RGB ugovora koji se mogu upravljati u jednoj Bitcoin transakciji.


U konkretnim terminima, svaki _transition bundle_ pripada određenom Contract. Sve ove informacije su umetnute u **MPC Tree**, čiji koren (`mpc::Root`) se zatim ponovo hešira da bi se dobio `mpc::Commitment`. Upravo taj poslednji Hash se stavlja u Bitcoin transakciju (_witness transaction_), prema izabranom determinističkom metodu.


![RGB-Bitcoin](assets/fr/042.webp)


#### MPC Root Hash


Vrednost zapravo napisana On-Chain (u `Opret` ili `Tapret`) naziva se `mpc::Commitment`. Ovo se izračunava u obliku [BIP-341](https://github.com/Bitcoin/bips/blob/master/bip-0341.mediawiki), prema formuli :


```txt
mpc::Commitment = SHA-256(SHA-256(mpc_tag) || SHA-256(mpc_tag) || depth || cofactor || mpc::Root )
```


gde :




- `mpc_tag` je oznaka: `urn:ubideco:mpc:Commitment#2024-01-31`, odabrana prema [RGB konvencijama označavanja](https://github.com/RGB-WG/RGB-core/blob/master/doc/Commitments.md);
- `depth` (1 bajt) označava dubinu *MPC stabla* ;
- cofactor` (16 bits, in Little Endian) je parametar koji se koristi za promovisanje jedinstvenosti pozicija dodeljenih svakom Contract u stablu;
- `mpc::Root` je koren *MPC stabla*, izračunat prema procesu opisanom u narednom odeljku.


![RGB-Bitcoin](assets/fr/044.webp)


#### Izgradnja MPC stabla


Da bismo izgradili ovo MPC drvo, moramo osigurati da svaki Contract odgovara jedinstvenoj poziciji lista. Pretpostavimo da imamo:




- ugovori koji će biti uključeni, indeksirani sa `i` u `i = {0,1,..,C-1}` ;
- Za svaki Contract `c_i`, imamo identifikator `ContractId(i) = c_i`.


Zatim konstruiramo drvo širine `w` i dubine `d` tako da je `2^d = w`, sa `w > C`, tako da se svaki Contract može smestiti u zaseban _list_. Pozicija `pos(c_i)` svakog Contract u drvetu određena je sa :


```txt
pos(c_i) = c_i mod (w - cofactor)
```


gde je `koeficijent` ceo broj koji povećava verovatnoću dobijanja različitih pozicija za svaki Contract. U praksi, konstrukcija sledi iterativni proces:




- Počinjemo od minimalne dubine (`d=3` po konvenciji da sakrijemo tačan broj ugovora);
- Pokušavamo različite `koeficijente` (do `w/2`, ili maksimalno 500 zbog performansi);
- Ako ne uspemo da pozicioniramo sve ugovore bez sudara, povećavamo `d` i počinjemo ponovo.


Cilj je izbeći drveće koje je previše visoko, dok se rizik od sudara svodi na minimum. Imajte na umu da fenomen sudara prati logiku slučajne distribucije, povezanu sa [Paradoksom rođendana](https://en.wikipedia.org/wiki/Birthday_problem).


#### Nastanjeni listovi


Jednom kada su dobijene `C` različite pozicije `pos(c_i)` za ugovore `i = {0,1,..,C-1}`, svaki list se popunjava funkcijom Hash (*označeno Hash*):


```txt
tH_MPC_LEAF(c_i) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x10 || c_i || BundleId(c_i))
```


gde :




- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, je uvek izabran u skladu sa Merkle konvencijama RGB ;
- `0x10` identifikuje _ugovornu listu_ ;
- `c_i` je 32-bajtni Contract identifikator (izveden iz Genesis Hash);
- bundleId(c_i)` je 32-bajtni Hash koji opisuje skup `State Transitions` u odnosu na `c_i` (sakupljeni u *Transition Bundle*).


#### Nenaseljeno lišće


Preostali listovi, koji nisu dodeljeni Contract (tj. `w - C` listovi), popunjavaju se "dummy" vrednošću (_entropy leaf_) :


```txt
tH_MPC_LEAF(j) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x11 || entropy || j )
```


gde :




- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, je uvek izabran u skladu sa Merkle konvencijama RGB ;
- `0x11` označava _list entropije_ ;
- `entropy` je nasumična vrednost od 64 bajta, koju bira osoba koja gradi stablo;
- `j` je pozicija (u 32-bitnom Little Endian formatu) ovog lista u stablu.


#### MPC čvorovi


Nakon generisanja `w` listova (naseljenih ili ne), prelazimo na merkelizaciju. Bilo koji unutrašnji čvorovi se heširaju na sledeći način:


```txt
tH_MPC_BRANCH(tH1 || tH2) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || b || d || w || tH1 || tH2)
```


gde :




- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, je uvek izabran u skladu sa Merkle konvencijama RGB ;
- b` je _faktor grananja_ (8 bita). Najčešće, `b=0x02` jer je stablo binarno i potpuno;
- d` je dubina čvora u stablu;
- `w` je širina stabla (u 256-bitnom binarnom zapisu malog endian-a);
- tH1` i `tH2` su heševi čvorova potomaka (ili listova), već izračunati kao što je prikazano iznad.


Napredujući na ovaj način, dobijamo koren `mpc::Root`. Zatim možemo izračunati `mpc::Commitment` (kao što je objašnjeno gore) i umetnuti ga On-Chain.


Da bismo to ilustrovali, zamislimo primer gde je `C=3` (tri ugovora). Njihove pozicije su pretpostavljene kao `pos(c_0)=7`, `pos(c_1)=4`, `pos(c_2)=2`. Ostali listovi (pozicije 0, 1, 3, 5, 6) su _entropijski listovi_. Dijagram ispod prikazuje sekvencu heševa do korena sa:




- `BUNDLE_i` što predstavlja `BundleId(c_i)` ;
- `tH_MPC_LEAF(A)` i tako dalje, koji predstavljaju listove (neki za ugovore, drugi za entropiju) ;
- Svaka grana `tH_MPC_BRANCH(...)` kombinuje heševe svojih dvoje dece.


Konačni rezultat je **mpc::Root**, zatim `mpc::Commitment`.


![RGB-Bitcoin](assets/fr/053.webp)


#### Provera MPC osovine


Kada verifikator želi da osigura da je `c_i` Contract (i njegov `BundleId`) uključen u konačni `mpc::Commitment`, on jednostavno prima Merkle dokaz. Ovaj dokaz pokazuje čvorove potrebne za praćenje listova (u ovom slučaju, _list ugovora_ `c_i`) nazad do korena. Nema potrebe da se otkriva celo *MPC stablo*: ovo štiti poverljivost drugih ugovora.


U primeru, `c_2` verifikatoru je potreban samo međurezultat Hash (`tH_MPC_LEAF(D)`), dva `tH_MPC_BRANCH(...)`, dokaz pozicije `pos(c_2)` i vrednost `cofactor`. Zatim može lokalno rekonstruisati koren, ponovo izračunati `mpc::Commitment` i uporediti ga sa onim zapisanim u Bitcoin transakciji (unutar `Opret` ili `Tapret`).


![RGB-Bitcoin](assets/fr/054.webp)


Ovaj mehanizam osigurava da :




- Status u odnosu na `c_2` je zaista uključen u zbirni informativni blok (na strani klijenta);
- Niko ne može izgraditi alternativnu istoriju sa istom transakcijom, jer On-Chain _commitment_ ukazuje na jedan MPC root.


#### Rezime strukture MPC-a


Multi Protocol Commitment* (MPC) je princip koji omogućava RGB da objedini više ugovora u jednu Bitcoin transakciju, dok održava jedinstvenost obaveza i poverljivost u odnosu na druge učesnike. Zahvaljujući determinističkoj konstrukciji stabla, svakom Contract je dodeljena jedinstvena pozicija, a prisustvo "dummy" listova (*Entropy Leaves*) delimično prikriva ukupan broj ugovora koji učestvuju u transakciji.


Ceo Merkle Tree nikada nije uskladišten na klijentu. Mi jednostavno generate _Merkle putanju_ za svaki dotični Contract, koja se prenosi primaocu (koji zatim može validirati Commitment). U nekim slučajevima, možete imati nekoliko sredstava koja su prošla kroz isti UTXO. Tada možete spojiti nekoliko _Merkle putanja_ u takozvani _multi-protokol Commitment blok_, kako biste izbegli previše dupliranja podataka.


Svaki _Merkle dokaz_ je stoga lagan, posebno jer dubina stabla neće premašiti 32 u RGB. Postoji i pojam "Merkle blok", koji zadržava više informacija (poprečni presek, entropija, itd.), korisnih za kombinovanje ili razdvajanje nekoliko grana.


Zato je trebalo toliko vremena da se finalizuje RGB. Imali smo opštu viziju iz 2019: prebacivanje svega na klijentsku stranu, cirkulaciju tokena off-chain. Ali za detalje kao što su sharding za više ugovora, struktura Merkle Tree, kako rešiti kolizije i spojiti dokaze... sve je to zahtevalo iteracije.


### Sidra: globalna skupština


Nakon izgradnje naših obaveza (`Opret` ili `Tapret`) i našeg MPC (*Multi Protocol Commitment*), potrebno je da Address pojam **Anchor** u RGB protokolu. Anchor je struktura validirana na strani klijenta koja objedinjuje Elements potrebne za verifikaciju da Bitcoin Commitment zaista sadrži specifične ugovorne informacije. Drugim rečima, Anchor rezimira sve podatke potrebne za validaciju gore opisanih _obaveza_.


Anchor se sastoji od tri uređena polja:




- `txid`
- `MPC Dokaz`
- ekstra dokaz o transakciji - ETP


Svako od ovih polja igra ulogu u procesu validacije, bilo da se radi o rekonstrukciji osnovne Bitcoin transakcije ili dokazivanju postojanja skrivene Commitment (posebno u slučaju `Tapret`).


#### txid


Polje `txid` odgovara 32-bajtnoj oznaci transakcije Bitcoin koja sadrži `Opret` ili `Tapret` Commitment.


U teoriji, bilo bi moguće pronaći ovaj `txid` praćenjem lanca prelaza stanja koji sami ukazuju na svaki Witness Transaction, prateći logiku jednokratnih pečata. Međutim, da bi se olakšala i ubrzala verifikacija, ovaj `txid` je jednostavno uključen u Anchor, čime se validatoru štedi potreba da se vraća kroz celu istoriju off-chain.


#### MPC dokaz


Drugo polje, `MPC Proof`, odnosi se na dokaz da je ovaj određeni Contract (npr. `c_i`) uključen u _Multi Protocol Commitment_. To je kombinacija od :




- `pos_i`, pozicija ovog Contract u MPC stablu;
- koeficijent`, vrednost definisana za rešavanje kolizija pozicija;
- `Merkle Proof`, tj. skup čvorova i heševa korišćenih za rekonstrukciju MPC korena i verifikaciju da su Contract identifikator i njegov `Transition Bundle` posvećeni korenu.


Ovaj mehanizam je opisan u prethodnom odeljku o izgradnji *MPC Tree*, gde svaki Contract dobija jedinstveni list zahvaljujući :


```txt
pos(c_i) = c_i mod (w - cofactor)
```


Zatim se koristi deterministička šema merkelizacije za agregaciju svih listova (ugovori + entropija). Na kraju, `MPC Proof` omogućava da se koren lokalno rekonstruiše i uporedi sa `mpc::Commitment` uključujući On-Chain.


#### Dodatni dokaz transakcije - ETP


Treće polje, **ETP**, zavisi od tipa Commitment koji se koristi. Ako je Commitment tipa `Opret`, nije potreban dodatni dokaz. Validator pregleda prvi `OP_RETURN` izlaz transakcije i tamo direktno pronalazi `mpc::Commitment`.


**Ako je Commitment tipa `Tapret`**, mora se dostaviti dodatni dokaz pod nazivom *Dodatni dokaz transakcije - ETP*. Sadrži:




- Interni javni ključ (`P`) izlaza Taproot u kojem je *Commitment* ugrađen;
- Čvorovi partneri `Script Path Spend` (kada je Tapret *Commitment* umetnut u skriptu), kako bi se dokazala tačna lokacija ove skripte u stablu Taproot:
 - Ako je `Tapret` *Commitment* na desnoj grani, otkrivamo levi čvor (npr. `tHABC`),
 - Ako je `Tapret` *Commitment* na levoj strani, morate otkriti 2 čvora (npr. `tHAB` i `tHC`) da biste dokazali da nijedan drugi *Commitment* nije prisutan na desnoj strani.
- `Nonce` se može koristiti za „rudarenje“ najbolje konfiguracije, omogućavajući da se *Commitment* postavi desno od stabla (optimizacija dokaza).


Ovaj dodatni dokaz je suštinski važan jer, za razliku od `Opret`, `Tapret` Commitment je integrisan u strukturu Taproot skripta, što zahteva otkrivanje dela Taproot stabla kako bi se pravilno validirala lokacija *Commitment*.


![RGB-Bitcoin](assets/fr/045.webp)


**Anchors** stoga obuhvataju sve informacije potrebne za validaciju Bitcoin Commitment u kontekstu RGB. Oni ukazuju na relevantnu transakciju (`txid`) i dokaz pozicioniranja Contract (`MPC Proof`), dok upravljaju dodatnim dokazom (`ETP`) u slučaju `Tapret`. Na ovaj način, Anchor štiti integritet i jedinstvenost stanja off-chain osiguravajući da se ista transakcija ne može reinterpretirati za druge ugovorne podatke.


### Zaključak


U ovom poglavlju pokrivamo :




- Kako primeniti koncept jednokratnih pečata u Bitcoin (posebno putem _outpoint_);
- Različite metode za determinističko umetanje _commitment_-a u transakciju (Sig tweak, Key tweak, witness tweak, OP_RETURN, Taproot/Tapret) ;
- Razlozi zašto se RGB fokusira na Tapret obaveze;
- Upravljanje Multi-Contract putem _višestrukih protokola_, neophodno ako ne želite da izložite celu državu ili druge ugovore kada želite da dokažete određenu tačku;
- Takođe smo videli ulogu _Anchors_, koji sve spajaju (transakcija txid, Merkle Tree dokaz i Taproot dokaz) u jedan paket.


U praksi, tehnička implementacija je podeljena između nekoliko posvećenih Rust _sanduka_ (u _client_side_validation_, _commit-verify_, _bp_core_, itd.). Osnovne ideje su tu:


![RGB-Bitcoin](assets/fr/046.webp)


U sledećem poglavlju, pogledaćemo čisto off-chain komponentu RGB, naime Contract logiku. Videćemo kako RGB ugovori, organizovani kao delimično replikovane _konačne automatske mašine_, postižu mnogo veću izražajnost od Bitcoin skripti, dok čuvaju poverljivost svojih podataka.


## Uvod u pametne ugovore i njihova stanja


<chapterId>04a9569f-3563-5382-bf53-0c7069343ba0</chapterId>


:::video id=db4ee09f-1352-4ad1-9f7a-c962df7ea9fa:::


U ovom i sledećem poglavlju, razmotrićemo pojam **Smart contract** unutar okruženja RGB i istražiti različite načine na koje ovi ugovori mogu definisati i razvijati svoje *stanje*. Videćemo zašto RGB arhitektura, koristeći uređeni niz jednokratnih pečata, omogućava izvršavanje različitih tipova ***Contract operacija*** na skalabilan način i bez prolaska kroz centralizovani registar. Takođe ćemo razmotriti fundamentalnu ulogu ***Business Logic*** u oblikovanju evolucije Contract State.


### Pametni ugovori i digitalna prava nosioca


Cilj RGB je da obezbedi infrastrukturu za implementaciju pametnih ugovora na Bitcoin. Pod "Smart contract" podrazumevamo sporazum između nekoliko strana koji se automatski i računarski sprovodi, bez ljudske intervencije za sprovođenje klauzula. Drugim rečima, zakon Contract sprovodi softver, a ne pouzdana treća strana.


Ova automatizacija postavlja pitanje decentralizacije: kako se možemo osloboditi centralizovanog registra (npr. centralne platforme ili baze podataka) za upravljanje performansama Ownership i Contract? Originalna ideja, koju je preuzeo RGB, jeste povratak na način Ownership poznat kao "instrumenti donosioca". Istorijski gledano, određeni hartije od vrednosti (obveznice, akcije, itd.) su izdavane u obliku donosioca, omogućavajući svakome ko fizički poseduje dokument da ostvaruje svoja prava.


![RGB-Bitcoin](assets/fr/055.webp)


RGB primenjuje ovaj koncept na digitalni svet: prava (i obaveze) su inkapsulirana u podatke koji se manipulišu off-chain, a status ovih podataka potvrđuju sami učesnici. Ovo omogućava, a priori, mnogo veći stepen poverljivosti i nezavisnosti nego što to nude drugi pristupi zasnovani na javnim registrima.


### Uvod u Smart contract RGB status


Smart contract u RGB mogu se posmatrati kao mašine stanja, definisane sa:




- **Stanje**, tj. skup informacija koji odražava trenutnu konfiguraciju Contract;
- **Business Logic** (skup pravila), koji opisuje pod kojim uslovima i od strane koga država može biti izmenjena.


![RGB-Bitcoin](assets/fr/056.webp)


Važno je razumeti da ovi ugovori nisu ograničeni na jednostavan prenos tokena. Oni mogu obuhvatiti širok spektar aplikacija: od tradicionalnih sredstava (tokeni, akcije, obveznice) do složenijih mehanika (prava korišćenja, komercijalni uslovi, itd.). Za razliku od drugih blokčejnova, gde je Contract kod dostupan i izvršiv od strane svih, pristup RGB pristupu deli pristup i znanje o Contract učesnicima ("***Contract učesnici***"). Postoji nekoliko uloga:




- Izdavalac** ili tvorac Contract, koji definiše Genesis od Contract i njegove početne varijable;
- Strane sa pravima** (*Ownership*) ili drugim mogućnostima sprovođenja ;
- Posmatrači**, potencijalno ograničeni na pregled određenih informacija, ali koji ne mogu pokrenuti izmene.


Ova podela uloga doprinosi otpornosti na cenzuru, osiguravajući da samo ovlašćene osobe mogu komunicirati sa ugovornim stanjem. Takođe daje RGB mogućnost horizontalnog skaliranja: većina validacija se odvija van Blockchain, a samo kriptografski sidra (*commitments*) su upisana na Bitcoin.


### Status i Business Logic u RGB


Sa praktične tačke gledišta, Contract-ov **Business Logic** ima oblik pravila i skripti, definisanih u onome što RGB naziva **Schema**. Schema kodira :




- Državna struktura (koja polja su javna? Koja polja su u vlasništvu kojih strana?)
- Uslovi validnosti (šta se mora proveriti pre nego što se odobri ažuriranje stanja?);
- Autorizacije (ko može inicirati *State Transition*? Ko može samo posmatrati?).


U isto vreme, **Contract State** se često razlaže na dve komponente:




- A **Global State**: javni deo, potencijalno vidljiv svima (u zavisnosti od konfiguracije);
- Vlasnička Stanja**: privatni delovi, dodeljeni specifično vlasnicima putem UTXO-a referenciranih u Contract logici.


Kao što ćemo videti u narednim poglavljima, svako ažuriranje statusa (*Contract Operation*) mora se povezati sa Bitcoin _obavezom_ (putem `Opret` ili `Tapret`) i biti u skladu sa *Business Logic* skriptama da bi se smatralo važećim.


### Contract Operacije: stvaranje i evolucija države


U RGB univerzumu, ***Contract Operation*** je bilo koji događaj koji menja Contract iz **starog stanja** u **novo stanje**. Ove operacije slede sledeću logiku:




- Uzimamo na znanje trenutni status Contract;
- Primjenjujemo pravilo ili operaciju (a ***State Transition***, a ***Genesis*** ako je to prva država, ili a ***State Extension*** ako postoji javni *Valency* za ponovno pokretanje);
- Mi Anchor modifikaciju putem nove _obaveze_ na Blockchain, zatvarajući jednu _jednokratnu plombu_ i stvarajući drugu ;
- Nositelji prava proveravaju lokalno (*client-side*) da li tranzicija odgovara *Schema* i da li je povezana transakcija Bitcoin registrovana kao On-Chain.


![RGB-Bitcoin](assets/fr/057.webp)


Konačni rezultat je ažurirani Contract, sada sa drugačijim stanjem. Ova tranzicija ne zahteva da cela Bitcoin mreža bude zabrinuta za detalje, jer je samo mali kriptografski otisak ( _commitment_ ) zabeležen u Blockchain. Sekvenca jednokratnih pečata sprečava bilo kakav Double-spending ili dvostruku upotrebu Stanja.


### Operativni lanac: od Genesis do Terminal State


Da bismo ovo stavili u perspektivu, RGB Smart contract počinje sa **Genesis**, prvim stanjem. Nakon toga, razne Contract operacije slede jedna za drugom, formirajući DAG (*Directed Acyclic Graph*) operacija:




- Svaka tranzicija se zasniva na prethodnom stanju (ili nekoliko njih, u slučaju konvergentnih tranzicija);
- Hronološki red je zagarantovan uključivanjem svake tranzicije u Bitcoin Anchor, vremenski obeležene i nepromenljive zahvaljujući konsenzusu od strane Proof-of-Work ;
- Kada više nema operacija u toku, dostignuto je **Terminalno Stanje**: najnovije i najkompletnije stanje Contract.


![RGB-Bitcoin](assets/fr/012.webp)


Ova DAG topologija (umesto jednostavnog linearnog lanca) odražava mogućnost da se različiti delovi Contract mogu razvijati paralelno, sve dok se međusobno ne protivreče. RGB zatim vodi računa o izbegavanju bilo kakvih nedoslednosti putem *klijentske* verifikacije svakog uključenog učesnika.


### Rezime


Pametni ugovori u RGB uvode model digitalnih nosilaca instrumenata, decentralizovanih, ali usidrenih u Bitcoin za vremensko označavanje i garantovanje redosleda transakcija. Automatsko izvršavanje ovih ugovora zasniva se na :




- A **Contract State*, ukazujući trenutnu konfiguraciju Contract (prava, stanja, varijable, itd.);
- A **Business Logic** (*Schema*), definišući koje tranzicije su dozvoljene i kako moraju biti validirane;
- Contract Operacije**, koje ažuriraju ovo stanje korak po korak, zahvaljujući obavezama usidrenim u Bitcoin transakcijama.


U narednom poglavlju, detaljnije ćemo razmotriti konkretnu reprezentaciju ovih ***stanja*** i ***tranzicija stanja*** na nivou off-chain, i kako se oni odnose na UTXO-e i Jednokratne Pečate ugrađene u Bitcoin. Ovo će biti prilika da vidimo kako unutrašnji mehanizmi RGB, zasnovani na Client-side Validation, uspevaju da održe konzistentnost pametnih ugovora uz očuvanje poverljivosti podataka.


## RGB Contract operacije


<chapterId>78c44e88-50c4-5ec4-befe-456c1a9f080b</chapterId>


:::video id=1caec34d-f214-425b-a1a4-0a40ae7d3e0e:::


U ovom poglavlju ćemo pogledati kako operacije u pametnim ugovorima i prelazi stanja funkcionišu, ponovo unutar RGB protokola. Cilj će takođe biti da se razume kako nekoliko učesnika sarađuje kako bi preneli Ownership sredstva.


### Prelazi stanja i njihova mehanika


Opšti princip je i dalje kao kod Client-side Validation, gde podatke o stanju drži vlasnik, a primaoc ih validira. Međutim, specifičnost ovde kod RGB leži u činjenici da Bob, kao primalac, traži od Alise da uključi određene informacije u Contract podatke kako bi imao stvarnu kontrolu nad primljenom imovinom, putem skrivene reference na jedan od njegovih UTXO-a.


Da bismo ilustrovali proces *State Transition* (koji je jedna od fundamentalnih ***Contract Operacija*** u RGB), hajde da uzmemo korak-po-korak primer prenosa imovine između Alice i Boba:


**Početna situacija:**


Alisa ima ***Stash RGB*** lokalno validiranih podataka (*client-side*). Ovaj Stash se odnosi na jedan od njenih UTXO-a na Bitcoin. To znači da _definicija pečata_ u ovim podacima ukazuje na UTXO koji pripada Alisi. Ideja je omogućiti joj da prenese određena digitalna prava povezana sa sredstvom (npr. RGB tokeni) Bobu.


![RGB-Bitcoin](assets/fr/058.webp)


**Bob takođe ima UTXO-e :**


Bob, s druge strane, ima bar jedan svoj UTXO, bez direktne veze sa Alice-inim. U slučaju da Bob nema UTXO, i dalje je moguće izvršiti prenos na njega koristeći sam *Witness Transaction*: izlaz ove transakcije će tada uključivati Commitment (_commitment_) i implicitno povezati Ownership novog Contract sa Bobom.


![RGB-Bitcoin](assets/fr/059.webp)


**Izgradnja nove nekretnine (*New State*) :**


Bob šalje Alisi informacije kodirane u obliku ***Invoice*** (detaljnije ćemo razmotriti konstrukciju Invoice u kasnijim poglavljima), tražeći od nje da kreira novo stanje koje se pridržava pravila Contract. Ovo stanje će uključivati novi *Seal Definition* koji pokazuje na jedan od Bobovih UTXO-a. Na ovaj način, Bob dobija Ownership sredstava definisanih u ovom novom stanju, na primer određenu količinu RGB tokena.


![RGB-Bitcoin](assets/fr/060.webp)


**Priprema uzorka transakcije:**


Alice zatim kreira transakciju Bitcoin trošeći UTXO referenciran u prethodnom Seal (onaj koji ju je legitimisao kao nosioca). U izlazu ove transakcije, *Commitment* (putem `Opret` ili `Tapret`) je umetnut u Anchor novo RGB stanje. `Opret` ili `Tapret` obaveze su izvedene iz *MPC stabla* (kao što je viđeno u prethodnim poglavljima), koje može agregirati nekoliko tranzicija iz različitih ugovora.


**Prenos *Consignment* Bobu:**


Pre nego što emituje transakciju, Alisa šalje Bobu ***Consignment*** koji sadrži sve neophodne *klijentske* podatke (njegov *Stash*) i nove informacije o stanju u Bobovu korist. U ovom trenutku, Bob primenjuje RGB pravila konsenzusa:




- Ona potvrđuje sve RGB podatke sadržane u *Consignment*, uključujući novu državu koja mu daje Ownership sredstva;
- Oslanjajući se na *Anchors* uključene u *Consignment*, verifikuje se hronologija transakcija svedoka (od Genesis do najnovijeg prelaza) i validiraju se odgovarajuće obaveze u Blockchain.


**Završetak tranzicije:**


Ako je Bob zadovoljan, može dati svoje odobrenje (na primer, potpisivanjem *Consignment*). Alice tada može emitovati pripremljenu uzorak transakciju. Kada bude potvrđena, ovo zatvara Seal koji je prethodno držala Alice i formalizuje Ownership od strane Boba. Anti-Double-spending sigurnost se zatim zasniva na istom mehanizmu kao u Bitcoin: UTXO se troši, dokazujući da Alice više ne može ponovo da ga koristi.


![RGB-Bitcoin](assets/fr/061.webp)


Nova država sada referencira Bobov UTXO, dajući Bobu Ownership koji je prethodno držala Alisa. Izlaz Bitcoin gde su podaci RGB usidreni postaje neopoziv dokaz prenosa Ownership.


Primer minimalnog DAG-a (*Directed Acyclic Graph*), koji se sastoji od dve Contract operacije (**Genesis** pa ***State Transition***), može ilustrovati kako se RGB stanje (*klijent-strana* Layer, u crvenoj boji) povezuje sa Bitcoin Blockchain (*Commitment* Layer, u narandžastoj boji).


![RGB-Bitcoin](assets/fr/062.webp)


Pokazuje da Genesis definiše Seal (*Seal Definition*), zatim *State Transition* zatvara ovaj Seal kako bi kreirao novi u drugom UTXO.


U ovom kontekstu, evo nekoliko podsetnika o terminologiji:




- An ***Assignment*** kombinuje :
    - A ***Seal Definition*** (koji ukazuje na UTXO);
    - Owned States**, tj. podaci povezani sa Ownership (na primer, količina prenetih tokena).
- **Global State** objedinjuje opšte osobine Contract, vidljive svima, i osigurava globalnu doslednost evolucija.


Prelazi stanja**, opisani u prethodnom poglavlju, predstavljaju glavni oblik Contract Operation. Oni se odnose na jedno ili više prethodnih stanja (iz Genesis ili drugog State Transition) i ažuriraju ih u novo stanje.


![RGB-Bitcoin](assets/fr/063.webp)


Ovaj dijagram pokazuje kako se u *State Transition Bundle* nekoliko pečata može zatvoriti u jednoj uzorkovanoj transakciji, dok se istovremeno otvaraju novi pečati. Zaista, zanimljiva karakteristika RGB protokola je njegova sposobnost skaliranja: nekoliko tranzicija može biti agregirano u Transition Bundle, pri čemu je svaka agregacija povezana sa različitim listom *MPC stabla* (jedinstveni identifikator paketa). Zahvaljujući *Deterministic Bitcoin Commitment* (DBC) mehanizmu, cela poruka se ubacuje u `Tapret` ili `Opret` izlaz, dok se zatvaraju prethodni pečati i moguće definišu novi. `Anchor* služi kao direktna veza između Commitment pohranjenog u Blockchain i Client-side Validation strukture (*klijent-strana*).


U narednim poglavljima, pogledaćemo sve komponente i procese uključene u izgradnju i validaciju State Transition. Većina ovih Elements su deo RGB konsenzusa, implementiranog u **RGB Core Library**.


### Transition Bundle


Na RGB, moguće je objediniti različite State Transitions koje pripadaju istoj Contract (tj. dele isti **ContractId**, izveden iz Genesis **OpId**). U najjednostavnijem slučaju, kao između Alice i Boba u gornjem primeru, **Transition Bundle** sadrži samo jednu tranziciju. Ali podrška za operacije sa više platiša (kao što su coinjoins, otvaranje Lightning kanala, itd.) znači da nekoliko korisnika može kombinovati svoje State Transitions u jednom paketu.


Jednom prikupljeni, ovi prelazi su usidreni (mehanizmom MPC + DBC) u jednoj Bitcoin transakciji:




- Svaki State Transition je heširan i grupisan u Transition Bundle ;
- Transition Bundle je sam po sebi heširan i umetnut u list MPC stabla koji odgovara ovom Contract (BundleId);
- MPC stablo je konačno angažovano putem `Opret` ili `Tapret` u Witness Transaction, što tako zatvara potrošene pečate i definiše nove pečate.


Tehnički gledano, **BundleId** unet u MPC list dobija se iz označenog Hash primenjenog na strogu serijalizaciju polja *InputMap* paketa:


```txt
BundleId = SHA256( SHA256(bundle_tag) || SHA256(bundle_tag) || InputMap )
```


U kojem `bundle_tag = urn:lnp-bp:RGB:bundle#2024-02-03` na primer.


*InputMap* je struktura podataka koja navodi, za svaki unos `i` uzorka transakcije, referencu na *OpId* odgovarajućeg State Transition. Na primer:


```txt
InputMap =
N               input_0    OpId(input_0)    input_1    OpId(input_1)   ...    input_N-1  OpId(input_N-1)
|____________________| |_________||______________| |_________||______________|       |__________||_______________|
16-bit Little Endian   32-bit LE   32-byte hash
|_________________________| |_________________________|  ...  |___________________________|

MapElement1                MapElement2                       MapElementN
```




- `N` je ukupan broj unosa u transakciji koji se odnose na `OpId`;
- opId(input_j)` je identifikator operacije jedne od državnih tranzicija prisutnih u paketu.


Pozivanjem na svaki unos samo jednom i na uredan način, sprečavamo da se isti Seal potroši dva puta u dve simultane državne tranzicije.


### Generisanje stanja i aktivno stanje


Prelazi stanja se stoga mogu koristiti za prenos Ownership sredstva sa jedne osobe na drugu. Međutim, oni nisu jedine moguće operacije u RGB protokolu. Protokol definiše tri **Contract Operacije** :




- State Transition** ;
- Genesis** ;
- State Extension**.


Među njima, **Genesis** i **State Extension** se ponekad nazivaju "*Operacije generisanja stanja*", jer kreiraju nova stanja bez trenutnog zatvaranja bilo kojeg. Ovo je veoma važna tačka: **Genesis** i **State Extension** ne uključuju zatvaranje Seal. Umesto toga, oni definišu novi Seal, koji zatim mora biti potrošen od strane narednog **State Transition** da bi bio zaista validiran u istoriji Blockchain.


![RGB-Bitcoin](assets/fr/064.webp)


**Aktivno stanje** Contract često se definiše kao skup najnovijih stanja koja proizlaze iz istorije (DAG) transakcija, počevši od Genesis i prateći sve anker tačke u Bitcoin Blockchain. Bilo koja stara stanja koja su već zastarela (tj. povezana sa potrošenim UTXO-ima) više se ne smatraju aktivnim, ali ostaju ključna za proveru konzistentnosti istorije.


### Genesis


Genesis je početna tačka svakog RGB Contract. Kreira ga izdavalac Contract i definiše početne parametre, u skladu sa **Schema**. U slučaju RGB tokena, Genesis može specificirati, na primer :




- Broj originalno kreiranih tokena i njihovi vlasnici;
- Ukupni mogući plafon izdanja ;
- Bilo kakva pravila ponovnog izdavanja i koji učesnici ispunjavaju uslove.


Budući da je prva transakcija u Contract, Genesis ne referiše na bilo koje prethodno stanje, niti zatvara bilo koji Seal. Međutim, da bi se pojavila u istoriji i bila validirana, Genesis mora biti **potrošena** (zatvorena) od strane prvog State Transition (često transakcija skeniranja/automatskog trošenja ka samom izdavaocu, ili početna distribucija korisnicima).


### State Extension


Proširenja države** nude originalnu funkciju za pametne ugovore. Omogućavaju Redeem određena digitalna prava (*Valencies*) predviđena u definiciji Contract, bez trenutnog zatvaranja Seal. Najčešće se to odnosi na:




- Distribuirana pitanja tokena;
- Mehanizmi zamene sredstava ;
- Uslovne ponovne izdaje (koje mogu uključivati uništavanje drugih sredstava, itd.).


Tehnički gledano, State Extension referiše na *Redeem* (određeni tip RGB unosa) koji odgovara prethodno definisanom *Valency* (na primer, u Genesis ili drugom State Transition). On definiše novi Seal, dostupan osobi ili stanju koje od njega ima koristi. Da bi ovaj Seal postao efektivan, mora biti potrošen od strane narednog State Transition.


![RGB-Bitcoin](assets/fr/065.webp)


Na primer: Genesis stvara pravo izdavanja (*Valency*). Ovo pravo može biti iskorišćeno od strane ovlašćenog aktera, koji zatim gradi State Extension :




- Odnosi se na Valency (Redeem);
- Kreira novi *Assignment* (novi podaci *Owned State*) koji upućuje na UTXO ;
- Budući State Transition, izdat od strane vlasnika ovog novog UTXO, će zapravo preneti ili distribuirati novoizdate tokene.


### Komponente Contract Operation


Sada bih želeo da detaljno pogledam svaki od konstitutivnih delova Elements jednog **Contract Operation** u RGB. Contract Operation je akcija koja menja stanje Contract, i koja se validira na strani klijenta, na deterministički način, od strane legitimnog primaoca. Konkretno, videćemo kako Contract Operation uzima u obzir, s jedne strane, **staro stanje** (*Old State*) Contract, a s druge strane, definiciju **novog stanja** (*New State*).


```txt
+---------------------------------------------------------------------------------------------------------------------+
|  Contract Operation                                                                                                 |
|                                                                                                                     |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|  | Ffv |     | ContractId | SchemaId |      | TransitionType | ExtensionType |      | Testnet |     | AltLayers1 |  |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Metadata                                      |  | Global State                                               |  |
|  |                                               |  | +----------------------------------+                       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  | |          Structured Data            |       |  | | |  GlobalStateType  | |  Data  | |     ...     ...       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  |                                               |  | +----------------------------------+                       |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|                                                                                                                     +---------> OpId |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|  | Inputs                                        |  | Assignments                                                |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #1                                  | |  | | Assignment #1                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ + ---------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #2                                  | |  | | Assignment #2                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  |       ...           ...          ...          |  |     ...          ...             ...                       |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Redeems                                       |  | Valencies                                                  |  |
|  |                                               |  |                                                            |  |
|  | +------------------------------+              |  |                                                            |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
| OpId +--------------> PrevOpId | | ValencyType | |  ...   ...   |  |  | ValencyType |  | ValencyType |         ...              |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
|  | +------------------------------+              |  |                                                            |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |

+---------------------------------------------------------------------------------------------------------------------+
```


Ako pogledamo dijagram iznad, možemo videti da Contract Operation uključuje Elements koji se odnosi na **Novo stanje** i druge koji se odnose na ažurirano **Staro stanje**.


Elements **Nove Države** su :




- Assignments**, u kojima su definisani :
 - **Seal Definition**;
 - **Owned State**.
- **Global State**, koji se može modifikovati ili obogatiti;
- Valencies**, possibly defined in a State Transition or Genesis.


**Stara država** se referencira putem :




- Ulazi**, koji ukazuju na *Zadatke* prethodnih prelaza stanja (nisu prisutni u Genesis);
- Iskupljenja**, koja se odnose na prethodno definisane Valencije (samo u državnim ekstenzijama).


Pored toga, Contract Operation uključuje opštija polja specifična za operaciju:




- ffv` (*Fast-forward version*): 2-bajtni integer koji označava Contract verziju;
- transitionType` ili ExtensionType`: 16-bitni ceo broj koji specificira tip tranzicije ili ekstenzije, prema Business Logic;
- `ContractId`: 32-bajtni broj koji se odnosi na *OpId* Contract Genesis. Uključeno u Transitions i Extensions, ali ne u Genesis ;
- schemaId: prisutan samo u Genesis, ovo je 32-bajtni Hash koji predstavlja strukturu (*Schema*) Contract;
- Testnet`: Buleanski indikator koji pokazuje da li ste na Testnet ili Mainnet mreži. Samo Genesis;
- altlayers1`: varijabla koja identifikuje alternativni Layer (Sidechain ili drugi) korišćen za Anchor podatke pored Bitcoin. Prisutan samo u Genesis ;
- metadata": polje koje može čuvati privremene informacije, korisno za validaciju kompleksnog Contract, ali koje ne sme biti zabeleženo u konačnoj istoriji statusa.


Konačno, sva ova polja su kondenzovana prilagođenim procesom heširanja, kako bi se proizveo jedinstveni otisak, `OpId`. Ovaj `OpId` se zatim integriše u Transition Bundle, omogućavajući mu da bude autentifikovan i validiran unutar protokola.


Svaki *Contract Operation* je stoga identifikovan 32-bajtovnim Hash nazvanim `OpId`. Ovaj Hash se izračunava pomoću SHA256 Hash svih Elements koji čine operaciju. Drugim rečima, svaki *Contract Operation* ima svoj kriptografski Commitment, koji uključuje sve podatke potrebne za verifikaciju autentičnosti i konzistentnosti operacije.


An RGB Contract je zatim identifikovan pomoću `ContractId`, izvedenog iz Genesis `OpId` (pošto ne postoji operacija pre-Genesis). Konkretno, uzimamo Genesis `OpId`, obrćemo redosled bajtova i primenjujemo Base58 kodiranje. Ovo kodiranje čini `ContractId` lakšim za rukovanje i prepoznavanje.


### Metode i pravila ažuriranja statusa


**Contract State** predstavlja skup informacija koje protokol RGB mora pratiti za dati Contract. Sastoji se od:




- Jedan Global State**: ovo je javni, globalni deo Contract, vidljiv svima;
- Jedna ili više Vlasničkih Država**: svaki Owned State je povezan sa jedinstvenim Seal (i stoga sa UTXO na Bitcoin). Pravi se razlika između:
    - **Javne** Države u vlasništvu,
    - **Privatno** Vlasničke Države.


![RGB-Bitcoin](assets/fr/066.webp)


*Global State* je direktno uključen u *Contract Operation* kao jedan blok. *Vlasničke države* su definisane u svakom *Assignment*, zajedno sa *Seal Definition*.


Glavna karakteristika RGB je način na koji se Global State i Owned States modifikuju. Generalno postoje dve vrste ponašanja:




- Promenljiv**: kada je element stanja opisan kao promenljiv, svaka nova operacija zamenjuje prethodno stanje novim stanjem. Stari podaci se tada smatraju zastarelim;
- Akumuliranje**: kada je element stanja definisan kao akumulirajući, svaka nova operacija dodaje nove informacije prethodnom stanju, bez prepisivanja. Rezultat je neka vrsta akumulirane istorije.


Ako, u Contract, element stanja nije definisan kao promenljiv ili kumulativan, ovaj element će ostati prazan za naredne operacije (drugim rečima, nema novih verzija za ovo polje). To je Contract Schema (tj. kodirani Business Logic) koji određuje da li je stanje (Globalno ili Vlasničko) promenljivo, kumulativno ili fiksno. Kada je Genesis definisan, ova svojstva se mogu menjati samo ako to Contract sam dozvoljava, na primer putem specifičnog State Extension.


Tabela ispod ilustruje kako svaka vrsta Contract Operation može manipulisati (ili ne) Global State i Owned State:


|                              | Genesis | State Extension | State Transition |
| ---------------------------- | :-----: | :-------------: | :--------------: |
| **Addition of Global State** |    +    |        -        |        +         |
| **Mutation of Global State** |   n/a   |        -        |        +         |
| **Addition of Owned State**  |    +    |        -        |        +         |
| **Mutation of Owned State**  |   n/a   |       No        |        +         |
| **Addition of Valencies**    |    +    |        +        |        +         |


**`+`** : akcija je moguća ako Contract-ov Schema to dozvoljava.


**`-`**: operacija mora biti potvrđena naknadnim State Transition (samo State Extension ne zatvara Single-Use Seal).


Pored toga, vremenski obuhvat i prava na ažuriranje za svaku vrstu podataka mogu se razlikovati u sledećoj tabeli:


|                                 | Metadata                                 | Global State                                  | Owned State                                                                                                |
| ------------------------------- | ---------------------------------------- | --------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Scope**                       | Defined for a single Contract Operation | Defined globally for the contract            | Defined for each seal (*Assignment*)                                                                       |
| **Who can update it?**          | Non-updatable (ephemeral data)          | Operation issued by actors (issuer, etc.)    | Depends on the legitimate holder who owns the seal (the one who can spend it in a following transaction)  |
| **Temporal Scope**              | Only for the current operation          | State is established at the end of the operation | State is defined before the operation (by the *Seal Definition* of the previous operation)               |


### Global State


Global State se često opisuje kao "niko ne poseduje, svi znaju". Sadrži opšte informacije o Contract, koje su javno vidljive. Na primer, u Contract koji izdaje tokene, potencijalno sadrži :




- Tiker (simbolična skraćenica tokena): `ticker` ;
- Puno ime tokena: `name` ;
- Preciznost (broj decimalnih mesta): `precision` ;
- Početna ponuda (i/ili maksimalni limit tokena): `issuedSupply` ;
- Datum izdavanja: `created` ;
- Pravni podaci ili druge javne informacije: `podaci`.


Ovaj Global State može biti postavljen na javne resurse (web stranice, IPFS, Nostr, Torrent, itd.) i distribuiran zajednici. Takođe, ekonomski podsticaj (potreba za držanjem i prenosom ovih tokena, itd.) prirodno podstiče korisnike Contract da sami održavaju i šire ove podatke.


### Zadaci


*Assignment* je osnovna struktura za definisanje :




- Seal (*Seal Definition*), koji ukazuje na određeni UTXO;
- *Owned State*, tj. vlasništvo ili podaci povezani sa ovim Seal.


*Assignment* se može smatrati analogom izlaza transakcije Bitcoin, ali sa više fleksibilnosti. U tome leži logika prenosa vlasništva: *Assignment* povezuje određenu vrstu imovine ili prava (`AssignmentType`) sa Seal. Ko god poseduje privatni ključ UTXO povezanog sa ovim Seal (ili ko god može potrošiti ovaj UTXO) smatra se vlasnikom ovog *Owned State*.


Jedna od velikih snaga RGB leži u sposobnosti da po volji otkrije (*reveal*) ili sakrije (*conceal*) polja *Seal Definition* i *Owned State*. Ovo nudi moćnu kombinaciju poverljivosti i selektivnosti. Na primer, možete dokazati da je tranzicija validna bez otkrivanja svih podataka, tako što ćete osobama koje treba da je validiraju pružiti otkrivenu verziju, dok treće strane vide samo skrivenu verziju (Hash). U praksi, `OpId` tranzicije se uvek izračunava iz *skrivenih* podataka.


![RGB-Bitcoin](assets/fr/067.webp)


#### Seal Definition


*Seal Definition*, u svom otkrivenom obliku, ima četiri osnovna polja: `txptr`, `vout`, `blinding` i `method` :




- txptr**: ovo je referenca na UTXO na Bitcoin :
    - U slučaju **Genesis Seal**, direktno ukazuje na postojeći UTXO (onaj povezan sa Genesis);
    - U slučaju **Graf Seal**, možemo imati :
        - Jednostavan `txid`, ako ukazuje na određeni UTXO,
        - Ili `WitnessTx`, koji označava samoreferencu: Seal upućuje na samu transakciju. Ovo je posebno korisno kada nije dostupan spoljašnji UTXO, na primer u transakcijama otvaranja Lightning kanala, ili ako primalac nema UTXO.
- vout** : izlazni broj transakcije označen `txptr`. Prisutan samo za standardni Graph Seal (ne za `WitnessTx`);
- zaslepljivanje**: nasumičan broj od 8 bajtova, za jačanje poverljivosti i sprečavanje pokušaja brutalne sile na identitet UTXO;
- method** : označava korišćeni metod ankerisanja (`Tapret` ili `Opret`).


Skrivena forma Seal Definition je SHA256 Hash (označena) od konkatenacije ova 4 polja, sa oznakom specifičnom za RGB.


![RGB-Bitcoin](assets/fr/068.webp)


#### Vlasničke Države


Druga komponenta *Assignment* je Owned State. Za razliku od Global State, može postojati u javnom ili privatnom obliku:




- Javni Owned State**: svi znaju podatke povezane sa Seal. Na primer, javna slika;
- Privatno Owned State**: podaci su skriveni, poznati samo vlasniku (i potencijalno validatoru ako je potrebno). Na primer, broj tokena koji se drže.


RGB definiše četiri moguća tipa stanja (*StateTypes*) za Owned State:




- Deklarativno**: ne sadrži numeričke podatke, samo deklarativno pravo (npr. pravo glasa). Skriveni i otkriveni oblici su identični;
- Fungible**: predstavlja fungibilnu količinu (kao tokeni). U otkrivenom obliku, imamo `amount` i `blinding`. U skrivenom obliku, imamo jedan *Pedersen commitment* koji skriva količinu i zaslepljivanje;
- Struktuirano**: čuva strukturirane podatke (do 64 kB). U otkrivenom obliku, to je podatkovni blok. U skrivenom obliku, to je označeni Hash ovog bloka:


```txt
SHA-256(SHA-256(tag_data) || SHA-256(tag_data) || blob)
```


Na primer:


```txt
tag_data = urn:lnp-bp:rgb:state-data#2024-02-12
```




- Prilozi**: povezuje datoteku (audio, slika, binarno, itd.) sa Owned State, čuvajući datoteku Hash `file_hash`, MIME tip `media type` i kriptografski salt `salt`. Sama datoteka je hostovana na drugom mestu. U skrivenom obliku, to je Hash označen sa tri prethodna podatka:


```txt
SHA-256(SHA-256(tag_attachment) || SHA-256(tag_attachment) || file_hash || media_type || salt)
```


Na primer:


```txt
tag_attachment = urn:rgb:state-attach#2024-02-12
```


Da rezimiramo, evo 4 moguće vrste stanja u javnom i skrivenom obliku:


```txt
State                      Concealed form                              Revealed form
+---------------------------------------------------------------------------------------------------------
+--------------------------------------------------------------------------------+
|                                                                                |
Declarative        |                              < void >                                          |
|                                                                                |
+--------------------------------------------------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------+ +----------+       |
Fungible           | | Pedersen Commitement | | <========== |         | Amount | | Blinding |       |
| +----------------------+ |             |         +--------+ +----------+       |
+--------------------------+             +---------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------------------+        |
Structured         | |     Tagged Hash      | | <========== |         |     Data Blob      |        |
| +----------------------+ |             |         +--------------------+        |
+--------------------------+             +---------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             | +-----------+ +------------+ +------+ |
Attachments        | |     Tagged Hash      | | <========== | | File Hash | | Media Type | | Salt | |
| +----------------------+ |             | +-----------+ +------------+ +------+ |

+--------------------------+             +---------------------------------------+
```


| **Element**         | **Declarative**  | **Fungible**                         | **Structured**                 | **Attachments**                |
| ------------------- | -------------- | ------------------------------------ | ----------------------------- | ----------------------------- |
| **Data**           | None           | Signed or unsigned 64-bit integer    | Any strict data type          | Any file                      |
| **Info Type**      | None           | Signed or unsigned                   | Strict types                   | MIME Type                      |
| **Privacy**       | Not required    | Pedersen commitment                  | Hash with blinding            | Hashed file identifier         |
| **Size Limits**    | N/A            | 256 bytes                             | Up to 64 KB                    | Up to ~500 GB                  |


### Ulazi


Ulazi *Contract Operation* odnose se na *Zadatke* koji se troše u ovoj novoj operaciji. Ulaz označava :




- prevOpId` : identifikator (`OpId`) prethodne operacije gde se *Assignment* nalazio;
- assignmentType` : tip *Assignment* (na primer, `assetOwner` za token) ;
- `Index`: indeks *Assignment* na listi povezanoj sa prethodnim `OpId`, određen nakon leksikografskog sortiranja skrivenih pečata.


Ulazi se nikada ne pojavljuju u Genesis, pošto nema prethodnih dodela. Takođe se ne pojavljuju u državnim ekstenzijama (jer državne ekstenzije ne zatvaraju pečate; već redefinišu nove pečate na osnovu valentnosti).


Kada imamo Owned States tipa `Fungible`, logika validacije (putem AluVM skripte navedene u Schema) proverava konzistentnost suma: suma ulaznih tokena (*Inputs*) mora biti jednaka sumi izlaznih tokena (u novim *Assignments*).


### Metapodaci


Polje **Metadata** može biti do 64 KiB i koristi se za uključivanje privremenih podataka korisnih za validaciju, ali nije integrisano u trajno stanje Contract. Na primer, ovde se mogu čuvati promenljive za međukalkulacije složenih skripti. Ovaj prostor nije namenjen za čuvanje u globalnoj istoriji, zbog čega je van opsega Owned States ili Global State.


### Valencije


Valencies** su originalni RGB protokolski mehanizam. Mogu se pronaći u Genesis, Prelazima Stanja ili Proširenjima Stanja. Predstavljaju numerička prava koja mogu biti aktivirana od strane State Extension (putem *Redeems*), a zatim finalizovana naknadnim Prelazom. Svaki Valency je identifikovan `ValencyType` (16 bita). Njegova semantika (pravo ponovnog izdavanja, zamena tokena, pravo spaljivanja, itd.) je definisana u Schema.


U konkretnim terminima, mogli bismo zamisliti Genesis koji definiše "pravo na ponovno izdavanje" Valency. State Extension će ga konzumirati (*Redeem*) ako su ispunjeni određeni uslovi, kako bi se uvela nova količina tokena. Zatim, State Transition koji potiče od nosioca tako kreiranog Seal može preneti ove nove tokene.


### Otkupljuje


Iskupljenja su ekvivalent Valency za Unose za Zadate. Pojavljuju se samo u Proširenjima Države, jer se tu aktivira prethodno definisani Valency. Redeem se sastoji od dva polja:




- `PrevOpId` : `OpId` operacije gde je Valency bio naveden;
- `ValencyType`: tip Valency koji želite aktivirati (svaki `ValencyType` može se koristiti samo jednom od strane State Extension).


Primer: Redeem može odgovarati izvršenju CoinSwap-a, u zavisnosti od toga šta je kodirano u Valency.


### RGB status karakteristike


Sada ćemo pogledati nekoliko osnovnih karakteristika države u RGB. Konkretno, pogledaćemo:




- **Strogi tipizirani sistem**, koji nameće preciznu i tipiziranu organizaciju podataka;
- Važnost razdvajanja **validacije** od **Ownership** ;
- Sistem **evolucije konsenzusa** u RGB, koji uključuje pojmove *ubrzanja* i *odlaganja*.


Kao i uvek, imajte na umu da je sve što se tiče statusa Contract validirano na strani klijenta prema pravilima konsenzusa navedenim u protokolu, a čija je krajnja kriptografska referenca usidrena u Bitcoin transakcijama.


#### Strog sistem tipova


RGB koristi *Strogi Tip Sistemi* i deterministički način serijalizacije (*Strogo Kodiranje*). Ova organizacija je dizajnirana da garantuje savršenu reproduktivnost i preciznost u definisanju, rukovanju i validaciji Contract podataka.


U mnogim programskim okruženjima (JSON, YAML...), struktura podataka može biti fleksibilna, čak i previše permisivna. S druge strane, u RGB, Struktura i Tipovi svakog polja su definisani sa eksplicitnim ograničenjima. Na primer :




- Svaka promenljiva ima specifičan tip (na primer, 8-bitni bez predznaka ceo broj `u8`, ili 16-bitni ceo broj sa predznakom, itd.);
- Tipovi mogu biti sastavljeni (ugnežđeni tipovi). Ovo znači da možete definisati tip na osnovu drugih tipova (npr. agregatni tip koji sadrži polje `u8`, polje `bool`, itd.);
- Kolekcije se takođe mogu specificirati: liste (*list*), skupovi (*set*) ili rečnici (*map*), sa determinističkim redosledom napredovanja;
- Svako polje je ograničeno (*donja granica* / *gornja granica*). Takođe postavljamo ograničenja na broj Elements u kolekcijama (sadržaj);
- Podaci su poravnati po bajtovima i serijalizacija je strogo definisana i nedvosmislena.


Zahvaljujući ovom strogom protokolu kodiranja :




- Redosled polja je uvek isti, bez obzira na implementaciju ili korišćeni programski jezik;
- Heševi izračunati na istom skupu podataka su stoga reproduktivni i identični (strogo determinističke *obaveze*);
- Granice sprečavaju nekontrolisani rast veličine podataka (npr. previše polja);
- Ovaj oblik kodiranja olakšava kriptografsku verifikaciju, jer svaki učesnik tačno zna kako da serijalizuje i Hash podatke.


U praksi, struktura (*Schema*) i rezultujući kod (*Interface* i pridružena logika) se kompajliraju. Deskriptivni jezik se koristi za definisanje Contract (tipovi, polja, pravila) i generate strogi binarni format. Kada se kompajlira, rezultat je :




- *Raspored Memorije* za svako polje;
- Semantički identifikatori (koji ukazuju na to da li promena imena promenljive ima uticaj na logiku, čak i ako memorijska struktura ostaje ista).


Strogi sistem tipova takođe omogućava precizno praćenje promena: svaka modifikacija strukture (čak i promena imena polja) je detektabilna i može dovesti do promene u ukupnom otisku.


Konačno, svaka kompilacija proizvodi otisak prsta, kriptografski identifikator koji potvrđuje tačnu verziju koda (podataka, pravila, validacije). Na primer, identifikator u obliku:


```txt
BEiLYE-am9WhTW1-oK8cpvw4-FEMtzMrf-mKocuGZn-qWK6YF#ginger-parking-nirvana
```


Ovo omogućava upravljanje konsenzusom ili ažuriranjima implementacije, uz osiguravanje detaljne sledljivosti verzija korišćenih u mreži.


Da bi se sprečilo da stanje RGB Contract postane previše glomazno za validaciju na strani klijenta, pravilo konsenzusa nameće maksimalnu veličinu od `2^16` bajtova (64 Kio) za bilo koje podatke uključene u kalkulacije validacije. Ovo se odnosi na svaku promenljivu ili strukturu: ne više od 65536 bajtova, ili ekvivalent u brojevima (32768 16-bitnih celih brojeva, itd.). Ovo se takođe odnosi na kolekcije (liste, skupove, mape), koje ne smeju premašiti `2^16` Elements.


Ovo ograničenje garantuje :




- Kontroliše maksimalnu veličinu podataka koji se obrađuju tokom State Transition;
- Kompatibilnost sa virtuelnom mašinom (*AluVM*) koja se koristi za pokretanje skripti za validaciju.


#### Validacija != Ownership paradigma


Jedna od glavnih inovacija RGB je stroga razdvojenost između dva pojma:




- Validacija**: proveravanje da li State Transition poštuje pravila Contract (Business Logic, istorija, itd.);
- **Ownership** (Ownership, ili kontrola): činjenica posedovanja Bitcoin UTXO koja omogućava da se Single-Use Seal potroši (ili zatvori), i tako State Transition da se dogodi.


Validacija** se odvija na nivou RGB softverskog steka (biblioteke, *commitments* protokol, itd.). Njena uloga je da osigura poštovanje internih pravila Contract (iznosi, dozvole, itd.). Posmatrači ili drugi učesnici takođe mogu validirati istoriju podataka.


Ownership**, s druge strane, u potpunosti se oslanja na sigurnost Bitcoin. Posedovanje privatnog ključa UTXO znači kontrolisanje sposobnosti za pokretanje nove tranzicije (zatvaranje Single-Use Seal). Dakle, čak i ako neko može videti ili validirati podatke, ne može promeniti stanje ako ne poseduje dotični UTXO.


![RGB-Bitcoin](assets/fr/069.webp)


Ovaj pristup ograničava klasične ranjivosti koje se susreću u složenijim blokčejnovima (gde je sav kod Smart contract javan i može ga menjati bilo ko, što je ponekad dovodilo do hakova). Na RGB, napadač ne može jednostavno da interaguje sa stanjem On-Chain, jer je pravo na delovanje na stanju (*Ownership*) zaštićeno Bitcoin Layer.


Štaviše, ovo razdvajanje omogućava da se RGB prirodno integriše sa Lightning Network. Lightning kanali se mogu koristiti za angažovanje i pomeranje RGB sredstava bez angažovanja On-Chain *obaveza* svaki put. Detaljnije ćemo razmotriti ovu integraciju RGB na Lightning-u u kasnijim poglavljima kursa.


#### Razvoj konsenzusa u RGB


Pored semantičkog verzionisanja koda, RGB uključuje sistem za evoluciju ili ažuriranje konsenzus pravila Contract tokom vremena. Postoje dva glavna oblika evolucije:




- Premotaj unapred**
- Push-back** (na francuskom)


Brzo premotavanje unapred se dešava kada prethodno nevažeće pravilo postane važeće. Na primer, ako se Contract razvije da dozvoli novi tip `AssignmentType` ili novo polje :




- Ovo se ne može uporediti sa klasičnim Blockchain hardforkom, jer RGB radi u Client-side Validation i ne utiče na ukupnu kompatibilnost Blockchain ;
- U praktičnim terminima, ova vrsta promene je označena poljem `Ffv` (*fast-forward version*) u Contract Operation;
- Trenutni nosioci nisu oštećeni: njihov status ostaje važeći;
- Novi korisnici (ili novi korisnici), s druge strane, treba da ažuriraju svoj softver (svoj Wallet) kako bi prepoznali nova pravila.


Push-back znači da prethodno važeće pravilo postaje nevažeće. To je stoga "pooštravanje" pravila, ali striktno govoreći nije softfork:




- Postojeći vlasnici mogu biti pogođeni (mogli bi se naći sa sredstvima koja su postala zastarela ili nevažeća u novoj verziji);
- Možemo smatrati da zapravo stvaramo novi protokol: ko god usvoji novo pravilo, napušta staro;
- Izdavalac može odlučiti da ponovo izda sredstva u ovom novom protokolu, prisiljavajući korisnike da održavaju dva odvojena novčanika (jedan za stari protokol, drugi za novi), ako žele da upravljaju obe verzije.


U ovom poglavlju o operacijama RGB Contract, istražili smo osnovne principe koji leže u osnovi ovog protokola. Kao što ste primetili, inherentna složenost RGB protokola zahteva upotrebu mnogih tehničkih termina. Dakle, u sledećem poglavlju, pružiću vam rečnik koji će rezimirati sve koncepte pokrivene u ovom prvom teorijskom delu, sa definicijama svih tehničkih termina koji se odnose na RGB. Zatim ćemo u sledećem odeljku praktično razmotriti definiciju i implementaciju RGB ugovora.


## RGB Rečnik


<chapterId>545e16a4-3cca-44a3-9fd5-dbc5868abf97</chapterId>


Ako treba da se vratite na ovaj kratki rečnik važnih tehničkih termina korišćenih u svetu RGB (navedenih abecednim redom), biće vam koristan. Ovo poglavlje nije neophodno ako ste već razumeli sve što smo pokrili u prvom delu.


#### AluVM


Skraćenica AluVM označava "_Algoritamska logička jedinica Virtuelna Mašina_", virtuelnu mašinu zasnovanu na registrima dizajniranu za validaciju Smart contract i distribuirano računanje. Koristi se (ali nije isključivo rezervisana) za validaciju RGB ugovora. Skripte ili operacije uključene u RGB Contract mogu se stoga izvršavati u okruženju AluVM.


Za dodatne informacije: [zvanična veb stranica AluVM](https://www.AluVM.org/)


#### Anchor


Anchor predstavlja skup podataka na strani klijenta koji se koriste za dokazivanje uključivanja jedinstvenog _commitment_-a u transakciju. U RGB protokolu, Anchor se sastoji od sledećih Elements:




- Identifikator transakcije Bitcoin (txid) od **Witness Transaction** ;
- **Multi Protocol Commitment (MPC)** ;
- **Deterministic Bitcoin Commitment (DBC)**;
- **Dodatni dokaz transakcije (ETP)** ako se koristi mehanizam **Tapret** Commitment (pogledajte odeljak posvećen ovom modelu).


Anchor stoga služi za uspostavljanje proverljive veze između određene Bitcoin transakcije i privatnih podataka potvrđenih od strane RGB protokola. To garantuje da su ovi podaci zaista uključeni u Blockchain, bez da njihov tačan sadržaj bude javno izložen.


#### Assignment


U logici RGB, Assignment je ekvivalent izlazu transakcije koji modifikuje, ažurira ili kreira određena svojstva unutar stanja Contract. Assignment se sastoji od dva Elements:




- A **Seal Definition** (referenca na specifični UTXO) ;
- An **Owned State** (podaci koji opisuju stanje povezano sa ovim novim vlasnikom).


Assignment stoga označava da je deo države (na primer, sredstvo) sada dodeljen određenom nosiocu, identifikovanom putem Single-Use Seal povezanog sa UTXO.


#### Business Logic


Business Logic grupiše sva pravila i interne operacije Contract, opisane njegovim **Schema** (tj. strukturom samog Contract). Ono diktira kako stanje Contract može evoluirati i pod kojim uslovima.


#### Client-side Validation


Client-side Validation se odnosi na proces putem kojeg svaka strana (klijent) verifikuje skup podataka razmenjenih privatno, u skladu sa pravilima protokola. U slučaju RGB, ovi razmenjeni podaci su grupisani u ono što je poznato kao **pošiljke**. Za razliku od protokola Bitcoin, koji zahteva da sve transakcije budu objavljene On-Chain, RGB dozvoljava da samo _obaveze_ (usidrene u Bitcoin) budu sačuvane javno, dok osnovne Contract informacije (tranzicije, potvrde, dokazi) ostaju off-chain, deljene samo između korisnika na koje se odnose.


#### Commitment


Commitment (u kriptografskom smislu) je matematički objekat, označen kao `C`, koji se deterministički izvodi iz operacije na strukturiranim podacima `m` (poruka) i nasumične vrednosti `r`. Pišemo:


$$
C = \text{commit}(m, r)
$$


Ovaj mehanizam obuhvata dve glavne operacije:




- Commit**: kriptografska funkcija se primenjuje na poruku `m` i nasumičan broj `r` kako bi se proizvelo `C` ;
- Verifikuj**: koristimo `C`, poruku `m` i vrednost `r` da proverimo da li je ovaj Commitment tačan. Funkcija vraća `True` ili `False`.


Commitment mora poštovati dva svojstva:




- Vezivanje**: mora biti nemoguće pronaći dve različite poruke koje proizvode isti `C` :


$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$


Kao što su :


$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$




- Skrivanje**: znanje o `C` ne sme otkriti sadržaj `m`.


U RGB protokolu, Commitment je uključen u Bitcoin transakciju kako bi se dokazalo postojanje određene informacije u datom trenutku, bez otkrivanja same informacije.


#### Consignment


**Consignment** grupiše podatke razmenjene između strana, podložne Client-side Validation u RGB. Postoje dve glavne kategorije Consignment:




- Contract Consignment**: isporučeno od strane *izdavaoca* (Contract izdavalac), uključuje informacije o inicijalizaciji kao što su Schema, Genesis, Interface i Interface Implementation.
- Transfer Consignment**: isporučeno od strane platioca (*payer*). Sadrži celu istoriju prelaza stanja koja vodi do Terminal Consignment (tj. konačno stanje primljeno od strane platioca).


Ove pošiljke nisu javno zabeležene na Blockchain; razmenjuju se direktno između zainteresovanih strana putem komunikacionog kanala po njihovom izboru.


#### Contract


Contract je skup prava koji se digitalno izvršava između nekoliko aktera putem RGB protokola. Ima aktivno stanje i Business Logic, definisan Schema, koji specificira koje operacije su autorizovane (transferi, produženja, itd.). Stanje Contract, kao i pravila njegove validnosti, izraženi su u Schema. U bilo kom trenutku, Contract se razvija samo u skladu sa onim što je dozvoljeno ovim Schema i validacionim skriptama (koje se, na primer, pokreću u AluVM).


#### Contract Operation


A Contract Operation je ažuriranje statusa Contract izvedeno prema pravilima Schema. Sledeće operacije postoje u RGB:




- State Transition** ;
- Genesis** ;
- State Extension**.


Svaka operacija menja stanje dodavanjem ili zamenom određenih podataka (Global State, Owned State...).


#### Contract Participant


Contract Participant je akter koji učestvuje u operacijama koje se odnose na Contract. U RGB, pravi se razlika između :




- Izdavalac Contract, koji stvara Genesis (poreklo Contract);
- Stranke Contract, tj. nosioci prava na stanje Contract;
- Javne stranke, koje mogu izgraditi Državne Ekstenzije ako Contract nudi Valencije dostupne javnosti.


#### Contract Rights


Contract Rights odnosi se na različita prava koja mogu biti ostvarena od strane onih koji su uključeni u RGB Contract. Ona spadaju u nekoliko kategorija:




- Ownership prava**, povezana sa Ownership određenog UTXO (putem _Definicije Pečata_);
- Izvršna prava**, tj. sposobnost izgradnje jedne ili više tranzicija (State Transitions) u skladu sa Schema ;
- Javna prava**, kada Schema ovlašćuje određene javne upotrebe, na primer stvaranje State Extension putem otkupa Valency.


#### Contract State


Contract State odgovara trenutnom stanju Contract u datom trenutku. Može se sastojati od javnih i privatnih podataka, odražavajući stanje Contract. RGB razlikuje između :




- **Global State**, koji uključuje javne osobine Contract (postavljene u Genesis ili dodate putem autorizovanih ažuriranja);
- Owned States**, koje pripadaju specifičnim vlasnicima, identifikovanim po njihovim UTXO-ima.


#### Deterministic Bitcoin Commitment - DBC


Deterministic Bitcoin Commitment (DBC) je skup pravila korišćenih za dokazivo i jedinstveno registrovanje _obaveze_ u Bitcoin transakciji. U RGB protokolu, postoje dva glavna oblika DBC:




- Opret**
- Tapret**


Ovi mehanizmi precizno definišu kako je _commitment_ kodiran u izlazu ili strukturi Bitcoin transakcije, kako bi se osiguralo da je ovaj Commitment deterministički sledljiv i proverljiv.


#### Directed Acyclic Graph - DAG


DAG (ili *Acyclic Guided Graph*) je graf bez ciklusa, koji omogućava topološko raspoređivanje. Blokčejnovi, poput _shards_ RGB ugovora, mogu biti predstavljeni DAG-ovima.


Za dodatne informacije: [Directed Acyclic Graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph)


#### Graviranje


Gravura je opcioni niz podataka koji uzastopni vlasnici Contract mogu uneti u istoriju Contract. Ova funkcija postoji, na primer, u **RGB21** Interface i omogućava dodavanje komemorativnih ili opisnih informacija u istoriju Contract.


#### Dodatni dokaz transakcije - ETP


ETP (*Extra Transaction Proof*) je deo Anchor koji sadrži dodatne podatke potrebne za validaciju **Tapret** *Commitment* (u kontekstu _taproot_). Uključuje, između ostalog, internu javnu ključu (_internal PubKey_) skripte Taproot i informacije specifične za _Script Path Spend_.


#### Genesis


Genesis se odnosi na skup podataka, kojim upravlja Schema, koji čini početno stanje bilo kog Contract u RGB. Može se uporediti sa Bitcoin konceptom _Genesis Block_, ili sa Coinbase Transaction konceptom, ali ovde na _klijent-strani_ i na nivou RGB tokena.


#### Global State


Global State je skup javnih svojstava sadržanih u Contract State. Definisan je u Genesis i, u zavisnosti od pravila Contract, može biti ažuriran od strane ovlašćenih tranzicija. Za razliku od Owned States, Global State ne pripada određenom entitetu; bliži je javnom registru unutar Contract.


#### Interface


Interface je skup instrukcija korišćenih za dekodiranje binarnih podataka sastavljenih u Schema ili u Contract operacijama i njihovim stanjima, kako bi ih učinili čitljivim za korisnika ili njegov Wallet. Djeluje kao interpretacija Layer.


#### Interface Implementation


Interface Implementation je skup deklaracija koje povezuju **Interface** sa **Schema**. Omogućava semantički prevod koji obavlja sam Interface, tako da sirovi podaci Contract mogu biti razumljivi korisniku ili uključenom softveru (novčanici).


#### Invoice


Invoice ima oblik URL-a kodiranog u [base58](https://en.wikipedia.org/wiki/Binary-to-text_encoding#Base58), koji ugrađuje podatke potrebne za konstrukciju **State Transition** (od strane platioca). Drugim rečima, to je Invoice koji omogućava drugoj strani (*platiocu*) da kreira odgovarajući prelaz za prenos sredstva ili ažuriranje stanja Contract.


#### Lightning Network


Lightning Network je decentralizovana mreža platnih kanala (ili _state channels_) na Bitcoin, sastavljena od 2/2 multi-potpisnih novčanika. Omogućava brze, niskotarifne _off-chain_ transakcije, dok se oslanja na Bitcoin's Layer 1 za arbitražu (ili zatvaranje) kada je to potrebno.


Za više informacija o tome kako Lightning funkcioniše, preporučujem da pohađate ovaj drugi kurs:


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

#### Multi Protocol Commitment - MPC


Multi Protocol Commitment (MPC) se odnosi na strukturu Merkle Tree korišćenu u RGB kako bi se u jednoj Bitcoin transakciji uključilo nekoliko **Transition Bundles** iz različitih ugovora. Ideja je da se objedine nekoliko obaveza (koje potencijalno odgovaraju različitim ugovorima ili različitim sredstvima) u jednoj Anchor tački kako bi se optimizovala zauzetost prostora bloka.


#### Owned State


Owned State je deo Contract State koji je zatvoren u Assignment i povezan sa određenim nosiocem (putem Single-Use Seal koji ukazuje na UTXO). Ovo predstavlja, na primer, digitalnu imovinu ili određeno ugovorno pravo dodeljeno toj osobi.


#### Ownership


Ownership se odnosi na sposobnost kontrole i trošenja UTXO referenciranog od strane Seal Definition. Kada je Owned State povezan sa UTXO, vlasnik ovog UTXO ima pravo, potencijalno, da prenese ili razvije povezano stanje, u skladu sa pravilima Contract.


#### Partially Signed Bitcoin Transaction - PSBT


PSBT (_Delimično Potpisana Bitcoin Transakcija_) je Bitcoin transakcija koja još nije u potpunosti potpisana. Može se deliti između nekoliko entiteta, od kojih svaki može dodati ili verifikovati određene Elements (potpise, skripte...), sve dok se transakcija ne smatra spremnom za On-Chain distribuciju.


Za dodatne informacije: [BIP-0174](https://github.com/Bitcoin/bips/blob/master/bip-0174.mediawiki)


#### Pedersen commitment


Pedersen commitment je tip kriptografskog Commitment sa svojstvom da je **homomorfan** u odnosu na operaciju sabiranja. To znači da je moguće validirati zbir dve obaveze bez otkrivanja pojedinačnih vrednosti.


Formalno, ako :


$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$


onda :


$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$


Ovo svojstvo je korisno, na primer, za prikrivanje količina razmenjenih tokena, dok je i dalje moguće verifikovati ukupne iznose.


Dalje informacije: [Pedersen commitment](https://link.springer.com/chapter/10.1007/3-540-46766-1_9)


#### Redeem


U State Extension, Redeem se odnosi na akciju povraćaja (ili eksploatacije) prethodno deklarisanog **Valency**. Kako je Valency javno pravo, Redeem omogućava ovlašćenom učesniku da zahteva specifičan Contract State Extension.


#### Schema


Schema u RGB je deklarativni deo koda koji opisuje skup promenljivih, pravila i Business Logic (*Business Logic*) koji upravljaju radom Contract. Schema definiše strukturu stanja, tipove dozvoljenih tranzicija i uslove validacije.


#### Seal Definition


Seal Definition je deo Assignment koji povezuje _obavezu_ sa UTXO u vlasništvu novog nosioca. Drugim rečima, ukazuje gde se uslov nalazi (u kojem UTXO), i uspostavlja Ownership imovine ili prava.


#### Shard


Shard predstavlja granu u DAG istoriji prelaza stanja RGB Contract. Drugim rečima, to je koherentan podskup celokupne istorije Contract, koji odgovara, na primer, nizu prelaza potrebnih za dokazivanje validnosti datog sredstva od _Genesis_.


#### Single-Use Seal


Single-Use Seal je kriptografsko obećanje Commitment za još nepoznatu poruku, koja će biti otkrivena tek u budućnosti i mora biti poznata svim članovima određene publike. Cilj je sprečiti stvaranje više konkurentskih obaveza za isti Seal.


#### Stash


Stash je skup podataka na strani klijenta koje korisnik čuva za jedan ili više RGB ugovora, u svrhu validacije (*Client-side Validation*). Ovo uključuje istoriju tranzicija, pošiljke, dokaze o validnosti, itd. Svaki vlasnik zadržava samo delove istorije koji su im potrebni (*shards*).


#### State Extension


State Extension je Contract Operation korišćen za ponovo pokretanje ažuriranja stanja otkupljivanjem prethodno deklarisanih **Valencija**. Da bi bio efikasan, State Extension mora biti zatvoren od strane State Transition (koji ažurira konačno stanje Contract).


#### State Transition


State Transition je operacija koja menja stanje RGB Contract u novo stanje. Može modifikovati Global State i/ili Owned State podatke. U praksi, svaka tranzicija se verifikuje pomoću Schema pravila i usidrena je u Bitcoin Blockchain putem _commitment_-a.


#### Taproot


Odnosi se na format transakcije Bitcoin's SegWit v1, uveden od strane [BIP341](https://github.com/Bitcoin/bips/blob/master/bip-0341.mediawiki) i [BIP342](https://github.com/Bitcoin/bips/blob/master/bip-0342.mediawiki). Taproot poboljšava poverljivost i fleksibilnost skripti, posebno čineći transakcije kompaktnijim i težim za razlikovanje jedne od druge.


#### Terminal Consignment - Consignment Endpoint


Terminal Consignment (ili _Krajnja tačka pošiljke_) je *transfer Consignment* koji sadrži konačno stanje Contract, uključujući State Transition kreiran od primaočevog Invoice (*korisnik plaćanja*). Stoga je to krajnja tačka transfera, sa neophodnim podacima koji dokazuju da je Ownership ili stanje preneto.


#### Transition Bundle


Transition Bundle je skup RGB državnih tranzicija (koje pripadaju istom Contract) koje su sve uključene u isti ***Witness Transaction*** Bitcoin. Ovo omogućava grupisanje nekoliko ažuriranja ili prenosa u jedan On-Chain Anchor.


#### UTXO


Bitcoin UTXO (*Unspent Transaction Output*) je definisan Hash transakcije i izlaznim indeksom (*vout*). Takođe se ponekad naziva _outpoint_. U RGB protokolu, referenca na UTXO (putem **Seal Definition**) omogućava lociranje **Owned State**, tj. svojine koja se drži na Blockchain.


#### Valency


Valency je javno pravo koje ne zahteva državno skladištenje kao takvo, ali koje se može iskoristiti putem **State Extension**. Stoga je to oblik mogućnosti otvoren za sve (ili određene igrače), deklarisan u logici Contract, kako bi se izvršilo određeno proširenje u kasnijem datumu.


#### Witness Transaction


Witness Transaction je Bitcoin transakcija koja zatvara Single-Use Seal oko poruke koja sadrži Multi Protocol Commitment (MPC). Ova transakcija troši UTXO ili kreira jedan, kako bi Seal Commitment povezan sa RGB protokolom. Djeluje kao On-Chain dokaz da je stanje postavljeno u određenom trenutku.


# Programiranje na RGB


<partId>148a7436-d079-56d9-be08-aaa4c14c6b3a</partId>


## Implementacija RGB ugovora


<chapterId>8333ea5f-51c7-5dd5-b1d7-47d491e58e51</chapterId>


:::video id=97d81b85-5a82-40a5-b111-7d96be5afd0f:::


U ovom poglavlju, detaljnije ćemo pogledati kako je RGB Contract definisan i implementiran. Videćemo koji su delovi RGB Contract, koje su njihove uloge i kako su konstruisani.


### Komponente od RGB Contract


Do sada smo već razgovarali o **Genesis**, koji predstavlja početnu tačku Contract, i videli smo kako se uklapa u logiku *Contract Operation* i stanje protokola. Međutim, kompletna definicija RGB Contract nije ograničena samo na Genesis: uključuje tri komplementarne komponente koje zajedno čine srž implementacije.


Prva komponenta se zove **Schema**. Ovo je fajl koji opisuje fundamentalnu strukturu i Business Logic (*Business Logic*) od Contract. On specificira korišćene tipove podataka, pravila validacije, dozvoljene operacije (npr. inicijalno izdavanje tokena, transferi, posebni uslovi, itd.) - ukratko, opšti okvir koji diktira kako Contract funkcioniše.


Druga komponenta je **Interface**. Fokusira se na to kako će korisnici (i posredno, softver za portfelj) komunicirati sa ovim Contract. Opisuje semantiku, tj. čitljivu reprezentaciju različitih polja i akcija. Dakle, dok Schema definiše kako Contract tehnički funkcioniše, Interface definiše kako predstaviti i izložiti te funkcionalnosti: nazivi metoda, prikaz podataka, itd.


Treća komponenta je **Interface Implementation**, koja dopunjuje prethodne dve delujući kao neka vrsta mosta između Schema i Interface. Drugim rečima, ona povezuje semantiku izraženu od strane Interface sa osnovnim pravilima definisanim u Schema. Upravo ova implementacija će upravljati, na primer, konverzijom između parametra unetog u Wallet i binarne strukture nametnute protokolom, ili kompilacijom pravila validacije u mašinski jezik.


Ova modularnost je zanimljiva karakteristika RGB, jer omogućava različitim grupama programera da rade odvojeno na ovim aspektima (*Schema*, *Interface*, *Implementacija*), sve dok prate pravila konsenzusa protokola.


Da sumiramo, svaki Contract se sastoji od :




- Genesis**, što je početno stanje Contract (i može se uporediti sa posebnom transakcijom koja definiše prvi Ownership nekog sredstva, prava ili bilo kojih drugih parametarskih podataka);
- Schema**, koji opisuje Contract-ov Business Logic (tipovi podataka, pravila validacije, itd.);
- Interface**, koji pruža semantički Layer za oba novčanika i ljudske korisnike, pojašnjavajući čitanje i izvršavanje transakcija;
- Implementacija** Interface, koja premošćuje jaz između Business Logic i prezentacije, kako bi se osiguralo da je definicija Contract u skladu sa korisničkim iskustvom.


![RGB-Bitcoin](assets/fr/070.webp)


Važno je napomenuti da da bi Wallet upravljao RGB sredstvom (bilo da je to fungibilni token ili pravo bilo koje vrste), mora imati sve ove Elements kompajlirane: *Schema*, *Interface*, *Interface Implementation* i *Genesis*. Ovo se prenosi putem ***Contract Consignment***, tj. paketom podataka koji sadrži sve što je potrebno za validaciju klijentske strane Contract.


Da bi se razjasnile ove ideje, ovde je tabela sažetka koja upoređuje komponente RGB Contract sa konceptima koji su već poznati bilo u objektno-orijentisanom programiranju (OOP) ili u Ethereum ekosistemu:


| RGB Contract Component       | Meaning                               | OOP Equivalent                             | Ethereum Equivalent               |
| ---------------------------- | ------------------------------------- | ------------------------------------------ | --------------------------------- |
| **Genesis**                  | Initial state of the contract        | Class constructor                         | Contract constructor              |
| **Schema**                   | Business logic of the contract       | Class                                     | Contract                          |
| **Interface**                | Semantics of the contract            | Interface (Java) / Trait (Rust) / Protocol (Swift) | ERC Standard                      |
| **Interface Implementation** | Mapping semantics and logic          | Impl (Rust) / Implements (Java)           | Application Binary Interface (ABI) |


Leva kolona prikazuje Elements specifičan za RGB protokol. Srednja kolona prikazuje konkretnu funkciju svake komponente. Zatim, u koloni "OOP ekvivalent", nalazimo ekvivalentni termin u objektno-orijentisanom programiranju:




- **Genesis** igra ulogu sličnu onoj *konstruktora klase*: ovde se inicijalizuje stanje Contract;
- **Schema** je opis klase, tj. definicija njenih svojstava, metoda i osnovne logike;
- **Interface** odgovara *interfejsima* (Java), *osobinama* (Rust) ili *protokolima* (Swift): ovo su javne definicije funkcija, događaja, polja... ;
- **Interface Implementation** odgovara *Impl* u Rust ili *Implements* u Javi, gde specificiramo kako će kod zapravo izvršavati metode najavljene u Interface.


U kontekstu Ethereuma, Genesis je bliži *Contract konstruktoru*, Schema definiciji Contract, Interface standardu kao što su ERC-20 ili ERC-721, a Interface Implementation ABI-ju (*Application Binary Interface*), koji specificira format interakcija sa Contract.


Prednost modularnosti RGB takođe leži u činjenici da različiti zainteresovani mogu napisati, na primer, svoj sopstveni Interface Implementation, sve dok poštuju logiku *Schema* i semantiku *Interface*. Tako bi izdavač mogao razviti novi, korisnički pristupačniji front-end (Interface), bez modifikovanja logike Contract, ili obrnuto, mogao bi proširiti Schema kako bi dodao funkcionalnost i obezbedio novu verziju prilagođenog Interface Implementation, dok bi stare implementacije ostale važeće za osnovnu funkcionalnost.


Kada kompajliramo novi Contract, mi generate Genesis (prvi korak u izdavanju ili distribuciji sredstva), kao i njegove komponente (Schema, Interface, Interface Implementation). Nakon toga, Contract je potpuno operativan i može se propagirati na novčanike i korisnike. Ova metoda, gde se Genesis kombinuje sa ova tri elementa, garantuje visok stepen prilagodljivosti (svaki Contract može imati svoju logiku), decentralizacije (svako može doprineti datoj komponenti), i sigurnosti (validacija ostaje strogo definisana protokolom, bez oslanjanja na proizvoljan On-Chain kod kao što je često slučaj na drugim blokčejnovima).


Sada bih želeo da detaljnije pogledam svaki od ovih komponenti: **Schema**, **Interface** i **Interface Implementation**.


### Schema


U prethodnom odeljku smo videli da je u ekosistemu RGB, Contract sastavljen od nekoliko Elements: Genesis, koji uspostavlja početno stanje, i nekoliko drugih komplementarnih komponenti. Svrha Schema je da deklarativno opiše sve Business Logic od Contract, tj. strukturu podataka, korišćene tipove, dozvoljene operacije i njihove uslove. Stoga je to veoma važan element u omogućavanju da Contract bude operativan na strani klijenta, jer svaki učesnik (na primer, Wallet) mora proveriti da li prelazi stanja koje prima odgovaraju logici definisanoj u Schema.


Schema se može uporediti sa "klasom" u objektno-orijentisanom programiranju (OOP). Generalno govoreći, služi kao model koji definiše komponente Contract, kao što su :




- Različite vrste Vlasničkih Stanja i Dodela ;
- Valencije, tj. posebna prava koja se mogu aktivirati (*iskoristiti*) za određene operacije;
- Global State polja, koja opisuju globalna, javna i zajednička svojstva Contract;
- Struktura Genesis (prva operacija koja aktivira Contract) ;
- Dozvoljeni oblici državnih prelaza i državnih proširenja, i kako ove operacije mogu modifikovati ;
- Metapodaci povezani sa svakom operacijom, za čuvanje privremenih ili dodatnih informacija;
- Pravila koja određuju kako interni Contract podaci mogu evoluirati (na primer, da li je polje promenljivo ili kumulativno);
- Sekvence operacija koje se smatraju validnim: na primer, redosled tranzicija koji treba poštovati ili skup logičkih uslova koji treba da budu zadovoljeni.


![RGB-Bitcoin](assets/fr/071.webp)


Kada *izdavalac* sredstva na RGB objavi Contract, on obezbeđuje Genesis i Schema povezane s tim. Korisnici ili novčanici koji žele da interaguju sa sredstvom preuzimaju ovaj Schema kako bi razumeli logiku iza Contract, i kako bi kasnije mogli da verifikuju da su tranzicije u kojima će učestvovati legitimne.


Prvi korak, za svakoga ko prima informacije o RGB sredstvu (npr. prenos tokena), jeste da validira ove informacije u odnosu na Schema. Ovo uključuje korišćenje Schema kompilacije za:




- Proverite da su Owned States, Assignments i ostali Elements ispravno definisani i da poštuju nametnute tipove (tzv. *strogi sistem tipova*);
- Proverite da su pravila prelaza (validacioni skripti) zadovoljena. Ovi skripti se mogu pokrenuti putem AluVM, koji je prisutan na strani klijenta i odgovoran je za validaciju konzistentnosti Business Logic (iznos transfera, posebni uslovi, itd.).


U praksi, Schema nije izvršni kod, kao što se može videti u blokčejnovima koji čuvaju On-Chain kod (EVM na Ethereumu). Suprotno tome, RGB odvaja Business Logic (deklarativni) od izvršnog koda na Blockchain (koji je ograničen na kriptografske ankeri). Tako, Schema određuje pravila, ali primena ovih pravila odvija se van Blockchain, na lokaciji svakog učesnika, prema Client-side Validation principu.


Schema mora biti kompajliran pre nego što ga mogu koristiti RGB aplikacije. Ova kompilacija proizvodi binarnu datoteku (npr. `.RGB`) ili enkriptovanu binarnu datoteku (`.rgba`). Kada Wallet uveze ovu datoteku, zna :




- Kako izgleda svaki tip podataka (cijeli brojevi, strukture, nizovi...) zahvaljujući strogom sistemu tipova ;
- Kako Genesis treba da bude strukturiran (da bi se razumela inicijalizacija sredstava);
- Različite vrste operacija (Tranzicije stanja, Proširenja stanja) i kako mogu modifikovati stanje ;
- Pravila skriptovanja (uvedena u Schema) koja će AluVM motor primeniti za proveru validnosti operacija.


Kao što je objašnjeno u prethodnim poglavljima, *strogi sistem tipova* nam pruža stabilan, deterministički format kodiranja: sve promenljive, bilo da su u pitanju Vlasnička Stanja, Globalna Stanja ili Valencije, su precizno opisane (veličina, donje i gornje granice ako je potrebno, potpisani ili nepotpisani tip, itd.). Takođe je moguće definisati ugnježdene strukture, na primer, da bi se podržali složeni slučajevi upotrebe.


Opcionalno, Schema može referencirati korenski `SchemaId`, što olakšava ponovno korišćenje postojeće osnovne strukture (šablona). Na ovaj način, možete razvijati Contract ili kreirati varijacije (npr. novi tip tokena) iz već dokazanog šablona. Ova modularnost izbegava potrebu za ponovnim kreiranjem celih ugovora i podstiče standardizaciju najboljih praksi.


Još jedna važna tačka je da je logika evolucije stanja (transferi, ažuriranja, itd.) opisana u Schema u obliku skripti, pravila i uslova. Dakle, ako dizajner Contract želi da odobri ponovno izdavanje ili nametne mehanizam spaljivanja (uništavanje tokena), može specificirati odgovarajuće skripte za AluVM u delu za validaciju Schema.


#### Razlika od programabilnih On-Chain blokčeina


Za razliku od sistema kao što je Ethereum, gde je Smart contract kod (izvršni) upisan u sam Blockchain, RGB skladišti Contract (svoju logiku) off-chain, u obliku kompajliranog deklarativnog dokumenta. Ovo implicira da :




- Ne postoji Turing-kompletna VM koja radi na svakom čvoru mreže Bitcoin. Pravila RGB Contract se ne izvršavaju na Blockchain, već u svakom korisniku koji želi da validira stanje;
- Contract podaci ne zagađuju Blockchain: samo kriptografski dokazi (*commitments*) su ugrađeni u Bitcoin transakcije (putem `Tapret` ili `Opret`);
- Schema se može ažurirati ili odbiti (*fast-forward*, *push-back*, itd.), bez potrebe za Fork na Bitcoin Blockchain. Novčanici jednostavno treba da uvezu novi Schema i prilagode se promenama konsenzusa.


#### Korišćenje od strane izdavaoca i korisnika


Kada *izdavalac* kreira sredstvo (na primer, neinflatorni fungibilni token), priprema :




- Schema koji opisuje pravila emisije, prenosa, itd.;
- Genesis prilagođen ovom Schema (sa ukupnim brojem izdatih tokena, identitetom početnog vlasnika, bilo kojim posebnim Valencijama za ponovno izdavanje, itd.).


Zatim čini kompajlirani Schema (datoteku `.RGB`) dostupnom korisnicima, tako da svako ko primi transfer ovog tokena može lokalno proveriti doslednost operacije. Bez ovog Schema, korisnik ne bi mogao da interpretira podatke o statusu ili proveri da li su u skladu sa pravilima Contract.


Dakle, kada novi Wallet želi da podrži neki resurs, jednostavno treba da integriše odgovarajući Schema. Ovaj mehanizam omogućava dodavanje kompatibilnosti za nove tipove resursa RGB, bez invazivnih promena u softverskoj bazi Wallet: sve što je potrebno je da se uveze Schema binarni fajl i razume njegova struktura.


Schema definiše Business Logic u RGB. Navodi pravila evolucije Contract, strukturu njegovih podataka (Vlasnička Stanja, Global State, Valencije) i pridružene validacione skripte (izvršive putem AluVM). Zahvaljujući ovom deklarativnom dokumentu, definicija Contract (kompajlirana datoteka) je jasno odvojena od stvarnog izvršenja pravila (na strani klijenta). Ovo razdvajanje daje RGB veliku fleksibilnost, omogućavajući širok spektar slučajeva upotrebe (zamjenjivi tokeni, NFT, sofisticiraniji ugovori) dok se izbegava složenost i mane tipične za programabilne On-Chain blokčejnove.


#### Schema primer


Hajde da pogledamo konkretan primer Schema za RGB Contract. Ovo je izvod u Rust iz fajla `nia.rs` (inicijali za "*Non-Inflatable Assets*"), koji definiše model za fungibilne tokene koji ne mogu biti ponovo izdati izvan njihove početne Supply (neinflaciona imovina). Ova vrsta tokena može se posmatrati kao ekvivalent, u RGB univerzumu, ERC20 na Ethereumu, tj. fungibilni tokeni koji poštuju određena osnovna pravila (npr. o transferima, Supply inicijalizaciji, itd.).


Pre nego što zaronimo u kod, vredi se prisetiti opšte strukture RGB Schema. Postoji niz deklaracija koje uokviruju :




- Mogući `SchemaId` koji ukazuje na korišćenje drugog osnovnog Schema kao šablona;
- **Global States** i **Owned States** (sa njihovim strogim tipovima) ;
- Valencije** (ako ih ima);
- **Operacije** (Genesis, State Transitions, State Extensions) koje mogu referencirati ova stanja i valencije;
- **Strogi tip sistema** korišćen za opisivanje i validaciju podataka;
- Skripte za validaciju** (pokrenuti putem AluVM).


![RGB-Bitcoin](assets/fr/072.webp)


Kod ispod prikazuje kompletnu definiciju Rust Schema. Komentarisaćemo ga deo po deo, prateći anotacije (1) do (9) ispod:


```rust
// ===== PART 1: Function Header and SubSchema =====
fn nia_schema() -> SubSchema {
// definitions of libraries and variables
// ===== PART 2: General Properties (ffv, subset_of, type_system) =====
Schema {
ffv: zero!(),
subset_of: None,
type_system: types.type_system(),
// ===== PART 3: Global States =====
global_types: tiny_bmap! {
GS_NOMINAL => GlobalStateSchema::once(types.get("RGBContract.DivisibleAssetSpec")),
GS_DATA => GlobalStateSchema::once(types.get("RGBContract.ContractData")),
GS_TIMESTAMP => GlobalStateSchema::once(types.get("RGBContract.Timestamp")),
GS_ISSUED_SUPPLY => GlobalStateSchema::once(types.get("RGBContract.Amount")),
},
// ===== PART 4: Owned Types =====
owned_types: tiny_bmap! {
OS_ASSET => StateSchema::Fungible(FungibleType::Unsigned64Bit),
},
// ===== PART 5: Valencies =====
valency_types: none!(),
// ===== PART 6: Genesis: Initial Operations =====
genesis: GenesisSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: tiny_bmap! {
GS_NOMINAL => Occurrences::Once,
GS_DATA => Occurrences::Once,
GS_TIMESTAMP => Occurrences::Once,
GS_ISSUED_SUPPLY => Occurrences::Once,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
},
// ===== PART 7: Extensions =====
extensions: none!(),
// ===== PART 8: Transitions: TS_TRANSFER =====
transitions: tiny_bmap! {
TS_TRANSFER => TransitionSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: none!(),
inputs: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
}
},
// ===== PART 9: Script AluVM and Entry Points =====
script: Script::AluVM(AluScript {
libs: confined_bmap! { alu_id => alu_lib },
entry_points: confined_bmap! {
EntryPoint::ValidateGenesis => LibSite::with(FN_GENESIS_OFFSET, alu_id),
EntryPoint::ValidateTransition(TS_TRANSFER) => LibSite::with(FN_TRANSFER_OFFSET, alu_id),
},
}),
}
}
```




- (1) - Zaglavlje funkcije i PodŠema**


Funkcija `nia_schema()` vraća `SubSchema`, što ukazuje na to da ovaj Schema može delimično naslediti od generičkijeg Schema. U ekosistemu RGB, ova fleksibilnost omogućava ponovno korišćenje određenih standardnih Elements glavnog Schema, a zatim definisanje pravila specifičnih za dotični Contract. Ovde odlučujemo da ne omogućimo nasleđivanje, pošto će `subset_of` biti `None`.




- (2) - Opšte osobine: ffv, subset_of, type_system**


Svojstvo `ffv` odgovara *fast-forward* verziji Contract. Vrednost `zero!()` ovde označava da smo na verziji 0 ili početnoj verziji ovog Schema. Ako kasnije želite da dodate nove funkcionalnosti (novi tip operacije, itd.), možete povećati ovu verziju kako biste označili promenu konsenzusa.


Svojstvo `subset_of: None` potvrđuje odsustvo nasleđivanja. Polje `type_system` odnosi se na strogi sistem tipova već definisan u biblioteci `types`. Ova linija ukazuje da svi podaci koje koristi Contract koriste strogu implementaciju serijalizacije koju pruža pomenuta biblioteka.




- (3) - Global States


U bloku `global_types`, deklarisemo četiri Elements. Koristimo ključ, kao što su `GS_NOMINAL` ili `GS_ISSUED_SUPPLY`, da ih kasnije referenciramo:




- `GS_NOMINAL` se odnosi na tip `DivisibleAssetSpec`, koji opisuje različita polja kreiranog tokena (puno ime, oznaka, preciznost...);
- `GS_DATA` predstavlja opšte podatke, kao što su odricanje od odgovornosti, metapodaci ili drugi tekst;
- `GS_TIMESTAMP` se odnosi na datum izdavanja;
- `GS_ISSUED_SUPPLY` postavlja ukupni Supply, tj. maksimalni broj tokena koji se može kreirati.


Ključna reč `once(...)` znači da se svako od ovih polja može pojaviti samo jednom.




- (4) - Vlasnički Tipovi


U `owned_types`, deklarišemo `OS_ASSET`, koji opisuje fungibilno stanje. Koristimo `StateSchema::Fungible(FungibleType::Unsigned64Bit)`, što označava da je količina sredstava (tokena) pohranjena kao 64-bitni bezznamenkasti cijeli broj. Dakle, svaka transakcija će poslati određenu količinu jedinica ovog tokena, koja će biti validirana prema ovoj strogo tipiziranoj numeričkoj strukturi.




- (5) - Valencije**


Navodimo `valency_types: none!()`, što znači da nema Valencija u ovom Schema, drugim rečima, nema posebnih ili dodatnih prava (kao što su ponovo izdavanje, uslovno spaljivanje, itd.). Ako bi Schema uključivao neka, bila bi navedena u ovom odeljku.




- (6) - Genesis: prve operacije


Ovde ulazimo u deo koji proglašava Contract operacije. Genesis je opisan sa:




- Odsustvo `metadata` (polje `metadata: Ty::<SemId>::UNIT.id(None)`) ;
- Global States koje moraju biti prisutne jednom svaka (`Once`);
- Lista zadataka gde se `OS_ASSET` mora pojaviti `JednomIliVišePuta`. To znači da Genesis zahteva najmanje jedan `OS_ASSET` Assignment (početni nosilac);
- No Valency : `valencies: none!()`.


Ovo je način na koji ograničavamo definiciju inicijalnog izdavanja tokena: moramo deklarisati izdato Supply (`GS_ISSUED_SUPPLY`), plus najmanje jednog imaoca (Owned State tipa `OS_ASSET`).




- (7) - Ekstenzije


Polje `extensions: none!()` označava da se State Extension ne predviđa u ovom Contract. To znači da nema operacije za Redeem digitalno pravo (Valency) ili za izvođenje State Extension pre Transicije. Sve se obavlja putem Genesis ili Državnih Transicija.




- (8) - Tranzicije: TS_TRANSFER


U `transitions`, definišemo tip operacije `TS_TRANSFER`. Objašnjavamo da :




- Nema metapodataka;
- Ne menja Global State (koji je već definisan u Genesis);
- Potrebno je jedno ili više `OS_ASSETa` kao ulazi. To znači da mora potrošiti postojeća Owned States;
- Kreira (`assignments`) najmanje jedan novi `OS_ASSET` (drugim rečima, primalac ili primaoci dobijaju tokene) ;
- Ne generiše novi Valency.


Ovo modelira ponašanje osnovnog transfera, koji troši tokene na UTXO, zatim kreira nova Owned States u korist primalaca, i na taj način očuva jednakost ukupnog iznosa između ulaza i izlaza.




- (9) - AluVM skripta i Ulazne Tačke** (na francuskom)


Konačno, deklarisali smo skript AluVM (`Script::AluVM(AluScript { ... })`). Ovaj skript sadrži :




- Jedna ili više eksternih biblioteka (`libs`) koje će se koristiti tokom validacije;
- Ulazne tačke koje ukazuju na pomake funkcija u kodu AluVM, odgovaraju validaciji Genesis (`ValidateGenesis`) i svake deklarisane Transicije (`ValidateTransition(TS_TRANSFER)`).


Ovaj validacioni kod je odgovoran za primenu Business Logic. Na primer, proveriće:




- Da `GS_ISSUED_SUPPLY` nije prekoračen tokom Genesis ;
- Da zbir `inputs` (potrošenih tokena) bude jednak zbiru `assignments` (primljenih tokena) za `TS_TRANSFER`.


Ako se ova pravila ne poštuju, tranzicija će se smatrati nevažećom.


Ovaj primer "*Non Inflatable Fungible Asset*" Schema nam pruža bolje razumevanje strukture jednostavnog RGB fungibilnog tokena Contract. Jasno možemo videti razdvajanje između opisa podataka (Globalna i Vlasnička Stanja), deklaracije operacija (Genesis, Tranzicije, Ekstenzije) i implementacije validacije (AluVM skripte). Zahvaljujući ovom modelu, token se ponaša kao klasičan fungibilni token, ali ostaje validiran na strani klijenta i ne zavisi od On-Chain infrastrukture za izvršavanje svog koda. Samo kriptografske obaveze su usidrene u Bitcoin Blockchain.


### Interface


Interface je Layer dizajniran da učini Contract čitljivim i manipulativnim, kako za korisnike (ljudsko čitanje) tako i za portfelje (softversko čitanje). Stoga Interface igra ulogu uporedivu sa Interface u objektno-orijentisanom programskom jeziku (Java, Rust osobina, itd.), jer izlaže i pojašnjava funkcionalnu strukturu Contract, bez nužnog otkrivanja unutrašnjih detalja Business Logic.


Za razliku od Schema, koji je isključivo deklarativan i kompajliran u binarnu datoteku koja je teška za korišćenje u izvornom obliku, Interface obezbeđuje ključeve za čitanje potrebne za :




- Navedite i opišite Global States i Owned States uključene u Contract;
- Pristupite imenima i vrednostima svakog polja, tako da mogu biti prikazana (npr. za token, saznajte njegov simbol, maksimalnu količinu, itd.);
- Tumačenje i konstrukcija operacija Contract (Genesis, State Transition, ili State Extension) povezivanjem podataka sa razumljivim nazivima (npr. izvršiti transfer jasno navodeći "iznos" umesto binarnog identifikatora).


![RGB-Bitcoin](assets/fr/073.webp)


Zahvaljujući Interface, možete, na primer, pisati kod u Wallet koji, umesto da manipuliše poljima, direktno manipuliše oznakama kao što su "broj tokena", "ime sredstva", itd. Na ovaj način, upravljanje Contract postaje intuitivnije. Na ovaj način, upravljanje Contract postaje intuitivnije.


#### Opšta operacija


Ova metoda ima mnogo prednosti:




- Standardizacija:**


Isti tip Contract može biti podržan standardnim Interface, deljenim između nekoliko Wallet implementacija. Ovo olakšava kompatibilnost i ponovnu upotrebu koda.




- Jasna razlika između Schema i Interface:**


U dizajnu RGB, Schema (Business Logic) i Interface (prezentacija i manipulacija) su dva nezavisna entiteta. Programeri koji pišu logiku Contract mogu se koncentrisati na Schema, bez brige o ergonomiji ili reprezentaciji podataka, dok drugi tim (ili isti tim, ali u drugom vremenskom okviru) može razvijati Interface.




- Fleksibilna evolucija:**


Interface se može modifikovati ili dodati nakon što je sredstvo izdato, bez potrebe za promenom samog Contract. Ovo je velika razlika u odnosu na neke On-Chain Smart contract sisteme, gde je Interface (često pomešan sa izvršnim kodom) zamrznut u Blockchain.




- Multi-Interface sposobnost


Isti Contract može biti izložen kroz različite Interfejse prilagođene različitim potrebama: jednostavan Interface za krajnjeg korisnika, drugi napredniji za izdavača koji treba da upravlja složenim operacijama konfiguracije. Wallet zatim može izabrati koji Interface da uveze, u zavisnosti od njegove upotrebe.


![RGB-Bitcoin](assets/fr/074.webp)


U praksi, kada Wallet preuzima RGB Contract (putem `.RGB` ili `.rgba` fajla), takođe uvozi povezani Interface, koji je takođe kompajliran. Tokom izvršavanja, Wallet može, na primer :




- Pregledajte listu država i pročitajte njihova imena, kako biste prikazali Ticker, Početni Iznos, Datum Izdavanja, itd. za korisnika Interface, umesto nečitljivog numeričkog identifikatora;
- Izgradite operaciju (kao što je transfer) koristeći eksplicitna imena parametara: umesto da pišete `assignments { OS_ASSET => 1 }`, može ponuditi korisniku polje "Amount" u formi, i prevesti ovu informaciju u striktno tipizirana polja koja očekuje Contract.


#### Razlika između Ethereuma i drugih sistema


Na Ethereumu, Interface (opisan putem ABI, *Application Binary Interface*) je generalno izveden iz On-Chain uskladištenog koda (Smart contract). Može biti skupo ili komplikovano modifikovati specifičan deo Interface bez dodirivanja samog Contract. Međutim, RGB je zasnovan na potpuno off-chain logici, sa podacima usidrenim u *commitments* na Bitcoin. Ovaj dizajn omogućava modifikaciju Interface (ili njegove implementacije) bez uticaja na fundamentalnu sigurnost Contract, jer validacija poslovnih pravila ostaje u Schema i referenciranom AluVM kodu.


#### Interface kompilacija


Kao i kod Schema, Interface je definisan u izvornom kodu (često u Rust) i kompajliran u `.RGB` ili `.rgba` fajl. Ovaj binarni fajl sadrži sve informacije potrebne Wallet da :




- Identifikuj polja po imenu ;
- Povežite svako polje (i njegovu vrednost) sa strogim sistemskim tipom definisanim u Contract;
- Znajte različite dozvoljene operacije i kako ih izgraditi.


Jednom kada je Interface uvezen, Wallet može ispravno prikazati Contract i predložiti interakcije korisniku.


### Interfejsi standardizovani od strane LNP/BP asocijacije


U ekosistemu RGB, Interface se koristi za davanje čitljivog i manipulativnog značenja podacima i operacijama Contract. Interface tako dopunjuje Schema, koji opisuje Business Logic interno (strogi tipovi, validacioni skripti, itd.). U ovom odeljku, pogledaćemo standardne Interfejse razvijene od strane LNP/BP asocijacije za uobičajene tipove Contract (zamjenjivi tokeni, NFT, itd.).


Kao podsetnik, ideja je da svaki Interface opisuje kako prikazati i manipulisati Contract na strani Wallet, jasno imenujući polja (kao što su `spec`, `ticker`, `issuedSupply`...) i definišući moguće operacije (kao što su `Transfer`, `Burn`, `Rename`...). Nekoliko interfejsa je već operativno, ali će ih biti sve više u budućnosti.


#### Neki gotovi interfejsi za upotrebu


**RGB20** je Interface za fungibilne asete, koji se može uporediti sa Ethereumovim ERC20 standardom. Međutim, ide korak dalje, nudeći širu funkcionalnost:




- Na primer, mogućnost preimenovanja sredstva (promena *tikera* ili punog imena) nakon što je izdano, ili prilagođavanje njegove preciznosti (*deobe akcija*);
- Takođe može opisati mehanizme za sekundarno ponovno izdavanje (ograničeno ili neograničeno) i za spaljivanje, a zatim zamenu, kako bi se izdavaocu omogućilo da uništi, a zatim ponovo stvori sredstva pod određenim uslovima;


Na primer, RGB20 Interface može biti povezan sa **šemom Neinflabilne Imovine (NIA)**, koja nameće neinflabilni početni Supply, ili sa drugim naprednijim šemama po potrebi.


**RGB21** se odnosi na ugovore tipa NFT, ili šire, na bilo koji jedinstveni digitalni sadržaj, kao što je predstavljanje digitalnih medija (slike, muzika, itd.). Pored opisivanja izdavanja i prenosa jednog sredstva, uključuje funkcije kao što su:




- Integrisana podrška za direktno uključivanje fajla (do 16 MB) u Contract (za preuzimanje na strani klijenta);
- Mogućnost za vlasnika da unese "*gravuru*" u istoriju kako bi dokazao prošli Ownership NFT-a.


**RGB25** je hibridni standard koji kombinuje fungibilne i ne-fungibilne aspekte. Dizajniran je za delimično fungibilne asete, kao što je tokenizacija nekretnina, gde želite da podelite imovinu dok zadržavate vezu sa jednim osnovnim asetom (drugim rečima, imate fungibilne delove kuće, povezane sa ne-fungibilnom kućom). Tehnički, ovaj Interface može biti povezan sa **Collectible Fungible Asset* (CFA)** Schema, koji uzima u obzir koncept deljenja dok prati originalni aset.


#### Interfejsi u razvoju


Druge interfejse planirane su za specijalizovanije upotrebe, ali još uvek nisu dostupne:




- RGB22**, posvećen digitalnim identitetima, za upravljanje identifikatorima i On-Chain profilima u RGB ekosistemu;
- RGB23**, za napredno vremensko označavanje, koristeći neke od ideja *Opentimestamps*, ali sa funkcijama za praćenje;
- RGB24**, koji ima za cilj ekvivalent decentralizovanog sistema domena (DNS) sličnog *Ethereum Name Service* ;
- RGB26**, dizajniran za upravljanje DAO-ovima (*Decentralized Autonomous Organization*) u složenijem formatu (upravljanje, glasanje, itd.);
- RGB30**, vrlo sličan RGB20, ali sa posebnom karakteristikom uzimanja u obzir decentralizovanog početnog izdavanja i korišćenja državnih ekstenzija. Ovo bi se koristilo za sredstva čije ponovno izdavanje upravlja nekoliko entiteta, ili su podložna finijim uslovima.


Naravno, u zavisnosti od datuma na koji konsultujete ovaj kurs, ove interfejse možda već budu operativne i dostupne.


#### Interface primer


Ovaj Rust isječak koda prikazuje [RGB20](https://github.com/RGB-WG/RGB-std/blob/master/src/Interface/rgb20.rs) Interface (fungibilna imovina). Ovaj kod je preuzet iz `rgb20.rs` datoteke u standardnoj RGB biblioteci. Pogledajmo ga kako bismo razumeli strukturu Interface i kako pruža most između, s jedne strane, Business Logic (definisanog u Schema) i, s druge strane, funkcionalnosti dostupnih novčanicima i korisnicima.


```rust
// ...
fn rgb20() -> Iface {
let types = StandardTypes::with(rgb20_stl());
Iface {
version: VerNo::V1,
name: tn!("RGB20"),
global_state: tiny_bmap! {
fname!("spec") => GlobalIface::required(types.get("RGBContract.DivisibleAssetSpec")),
fname!("data") => GlobalIface::required(types.get("RGBContract.ContractData")),
fname!("created") => GlobalIface::required(types.get("RGBContract.Timestamp")),
fname!("issuedSupply") => GlobalIface::one_or_many(types.get("RGBContract.Amount")),
fname!("burnedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
fname!("replacedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
},
assignments: tiny_bmap! {
fname!("inflationAllowance") => AssignIface::public(OwnedIface::Amount, Req::NoneOrMore),
fname!("updateRight") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnEpoch") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnRight") => AssignIface::public(OwnedIface::Rights, Req::NoneOrMore),
fname!("assetOwner") => AssignIface::private(OwnedIface::Amount, Req::NoneOrMore),
},
valencies: none!(),
genesis: GenesisIface {
metadata: Some(types.get("RGBContract.IssueMeta")),
global: tiny_bmap! {
fname!("spec") => ArgSpec::required(),
fname!("data") => ArgSpec::required(),
fname!("created") => ArgSpec::required(),
fname!("issuedSupply") => ArgSpec::required(),
},
assignments: tiny_bmap! {
fname!("assetOwner") => ArgSpec::many(),
fname!("inflationAllowance") => ArgSpec::many(),
fname!("updateRight") => ArgSpec::optional(),
fname!("burnEpoch") => ArgSpec::optional(),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_RESERVES
},
},
transitions: tiny_bmap! {
tn!("Transfer") => TransitionIface {
optional: false,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("previous") => ArgSpec::from_non_empty("assetOwner"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_non_empty("assetOwner"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Issue") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.IssueMeta")),
globals: tiny_bmap! {
fname!("issuedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_non_empty("inflationAllowance"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_many("inflationAllowance"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
ISSUE_EXCEEDS_ALLOWANCE,
INSUFFICIENT_RESERVES
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("OpenEpoch") => TransitionIface {
optional: true,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnEpoch"),
},
assignments: tiny_bmap! {
fname!("next") => ArgSpec::from_optional("burnEpoch"),
fname!("burnRight") => ArgSpec::required()
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("burnRight")),
},
tn!("Burn") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("burnedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: None,
},
tn!("Replace") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("replacedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS,
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Rename") => TransitionIface {
optional: true,
metadata: None,
globals: tiny_bmap! {
fname!("new") => ArgSpec::from_required("spec"),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("updateRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("updateRight"),
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("future")),
},
},
extensions: none!(),
error_type: types.get("RGB20.Error"),
default_operation: Some(tn!("Transfer")),
type_system: types.type_system(),
}
}
```


U ovom Interface, primećujemo sličnosti sa strukturom Schema: pronalazimo deklaraciju Global State, Owned States, Contract Operations (Genesis i Transitions), kao i rukovanje greškama. Ali Interface se fokusira na prezentaciju i manipulaciju ovih Elements za Wallet ili bilo koju drugu aplikaciju.


Razlika sa Schema leži u prirodi tipova. Schema koristi striktne tipove (kao što je `FungibleType::Unsigned64Bit`) i tehničke identifikatore. Interface koristi nazive polja, makroe (`fname!()`, `tn!()`), i reference na klase argumenata (`ArgSpec`, `OwnedIface::Rights`...). Cilj ovde je da se olakša funkcionalno razumevanje i organizacija Elements za Wallet.


Pored toga, Interface može uvesti dodatnu funkcionalnost osnovnom Schema (npr. upravljanje pravom `burnEpoch`), sve dok to ostaje u skladu sa konačnom validiranom logikom na strani klijenta. Sekcija "script" u AluVM u okviru Schema će osigurati kriptografsku validnost, dok Interface opisuje kako korisnik (ili Wallet) interaguje sa ovim stanjima i tranzicijama.


#### Global State i Zadaci


U odeljku `global_state` nalazimo polja kao što su `spec` (opis sredstva), `data`, `created`, `issuedSupply`, `burnedSupply`, `replacedSupply`. Ovo su polja koja Wallet može da pročita i prikaže. Na primer:




- `spec` će prikazati konfiguraciju tokena;
- `issuedSupply` ili `burnedSupply` daju nam ukupan broj izdatih ili spaljenih tokena, itd.


U odeljku `assignments` definišemo različite uloge ili prava. Na primer:




- `assetOwner` odgovara držanju tokena (to je fungibilni *Owned State*) ;
- `burnRight` odgovara sposobnosti spaljivanja tokena ;
- updateRight` odgovara pravu na preimenovanje sredstva.


Ključna reč `public` ili `private` (npr. `AssignIface::public(...)`) označava da li su ova stanja vidljiva (`public`) ili poverljiva (`private`). Što se tiče `Req::NoneOrMore`, `Req::Optional`, oni označavaju očekivanu pojavu.


#### Genesis i tranzicije


Deo `Genesis` deo opisuje kako se sredstvo inicijalizuje:




- Polja `spec`, `data`, `created`, `issuedSupply` su obavezna (`ArgSpec::required()`) ;
- Zadaci kao što je `assetOwner` mogu biti prisutni u više primeraka (`ArgSpec::many()`), omogućavajući da se tokeni distribuiraju više početnih vlasnika;
- Polja kao što su `inflationAllowance` ili `burnEpoch` mogu (ili ne moraju) biti uključena u Genesis.


Zatim, za svaku Transiciju (`Transfer`, `Issue`, `Burn`...), Interface definiše koja polja operacija očekuje kao ulaz, koja polja će operacija proizvesti kao izlaz, i sve greške koje se mogu pojaviti. Na primer:


**Tranzicija :**




- Ulazi : `previous` → mora biti `assetOwner` ;
- Zadaci : `beneficiary` → će biti novi `assetOwner` ;
- Greška: `NON_EQUAL_AMOUNTS` (Wallet će stoga moći da obradi slučajeve gde ulazna suma ne odgovara izlaznoj sumi).


**Transition `Issue` :**




- Opcionalno (`optional: true`), jer dodatna emisija nije nužno aktivirana;
- Ulazi: `used` → `inflationAllowance`, tj. dozvola za dodavanje više tokena ;
- Zadaci: `korisnik` (novi tokeni primljeni) i `budućnost` (preostali `inflationAllowance`) ;
- Moguće greške: `SUPPLY_MISMATCH`, `ISSUE_EXCEEDS_ALLOWANCE`, itd.


**Prelaz sagorevanja :**




- Ulazi : `used` → a `burnRight` ;
- Globals : `burnedSupply` required ;
- Zadaci: `future` → moguće nastavljanje `burnRight` ako nismo sve spalili ;
- Greške: `SUPPLY_MISMATCH`, `INVALID_PROOF`, `INSUFFICIENT_COVERAGE`.


Svaka operacija je stoga opisana na način koji je čitljiv za Wallet. Ovo omogućava prikaz grafičkog Interface gde korisnik može jasno videti: "Imate pravo da spaljujete. Da li želite da spaljujete određenu količinu? Kod zna da popuni polje `burnedSupply` i proveri da li je `burnRight` važeće.


Ukratko, važno je imati na umu da Interface, ma koliko bio potpun, sam po sebi ne definiše unutrašnju logiku Contract. Srž rada obavlja **Schema**, koji uključuje striktne tipove, strukturu Genesis, tranzicije i tako dalje. Interface jednostavno izlaže ove Elements na intuitivniji i imenovan način, za upotrebu u aplikaciji.


Zahvaljujući modularnosti RGB, Interface se može unaprediti (na primer, dodavanjem `Rename` tranzicije, ispravljanjem prikaza polja, itd.) bez potrebe za ponovnim pisanjem celog Contract. Korisnici ovog Interface mogu odmah iskoristiti ove poboljšice čim ažuriraju `.RGB` ili `.rgba` fajl.


Ali jednom kada proglasite Interface, potrebno je da ga povežete sa odgovarajućim Schema. Ovo se radi putem ***Interface Implementation***, koji specificira kako da mapirate svako imenovano polje (kao što je `fname!("assetOwner")`) na striktni ID (kao što je `OS_ASSET`) definisan u Schema. Ovo osigurava, na primer, da kada Wallet manipuliše poljem `burnRight`, to je stanje koje, u Schema, opisuje sposobnost spaljivanja tokena.


### Interface Implementation


U arhitekturi RGB, videli smo da se svaki komponent (Schema, Interface, itd.) može razvijati i kompajlirati nezavisno. Međutim, postoji jedan neophodan element koji povezuje ove različite građevinske blokove: ***Interface Implementation***. Ovo je ono što eksplicitno mapira identifikatore ili polja definisana u Schema (na strani Business Logic) sa imenima deklarisanim u Interface (na strani prezentacije i interakcije sa korisnikom). Tako kada Wallet učita Contract, može tačno razumeti koje polje odgovara čemu i kako operacija imenovana u Interface se odnosi na logiku Schema.


Važna tačka je da Interface Implementation nije nužno namenjen da izloži sve funkcionalnosti Schema, niti sva polja Interface: može biti ograničen na podskup. U praksi, ovo omogućava ograničavanje ili filtriranje određenih aspekata Schema. Na primer, možete imati Schema sa četiri tipa operacija, ali Implementacija Interface koja mapira samo dva od njih u datom kontekstu. Suprotno tome, ako Interface predlaže dodatne krajnje tačke, možemo odlučiti da ih ovde ne implementiramo.


Evo klasičnog primera Interface Implementation, gde povezujemo *Neinflabilnu Imovinu* (NIA) Schema sa RGB20 Interface:


```rust
fn nia_rgb20() -> IfaceImpl {
let schema = nia_schema();
let iface = Rgb20::iface();
IfaceImpl {
version: VerNo::V1,
schema_id: schema.schema_id(),
iface_id: iface.iface_id(),
script: none!(),
global_state: tiny_bset! {
NamedField::with(GS_NOMINAL, fname!("spec")),
NamedField::with(GS_DATA, fname!("data")),
NamedField::with(GS_TIMESTAMP, fname!("created")),
NamedField::with(GS_ISSUED_SUPPLY, fname!("issuedSupply")),
},
assignments: tiny_bset! {
NamedField::with(OS_ASSET, fname!("assetOwner")),
},
valencies: none!(),
transitions: tiny_bset! {
NamedType::with(TS_TRANSFER, tn!("Transfer")),
},
extensions: none!(),
}
}
```


U ovoj Implementaciji Interface :




- Izričito referenciramo Schema, putem `nia_schema()`, i Interface, putem `Rgb20::iface()`. Pozivi `Schema.schema_id()` i `iface.iface_id()` koriste se za Anchor Interface Implementation na strani kompajliranja (ovo povezuje kriptografske identifikatore ovih dvaju komponenti);
- Uspostavlja se mapiranje između Schema Elements i Interface Elements. Na primer, polje `GS_NOMINAL` u Schema je povezano sa stringom `"spec"` na strani Interface (`NamedField::with(GS_NOMINAL, fname!("spec"))`). Isto radimo za operacije, kao što je `TS_TRANSFER`, koje povezujemo sa `"Transfer"` u Interface... ;
- Možemo videti da nema valencija (`valencies: none!()`) ili ekstenzija (`extensions: none!()`), što odražava činjenicu da ovaj NIA Contract ne koristi ove funkcije.


Rezultat nakon kompilacije je zasebna datoteka `.RGB` ili `.rgba`, koja se uvozi u Wallet pored Schema i Interface. Tako softver zna kako konkretno povezati ovaj NIA Contract (čija je logika opisana njegovim Schema) sa "RGB20" Interface (koji pruža ljudska imena i način interakcije za fungibilne tokene), primenjujući ovaj Interface Implementation kao prolaz između njih.


#### Zašto odvojiti Interface Implementation?


Razdvajanje poboljšava fleksibilnost. Jedan Schema može imati nekoliko različitih implementacija Interface, pri čemu svaka mapira različit skup funkcionalnosti. Štaviše, sam Interface Implementation može evoluirati ili biti prepisan bez potrebe za promenom bilo Schema ili Interface. Ovo zadržava princip modularnosti RGB: svaka komponenta (Schema, Interface, Interface Implementation) može biti verzionisana i ažurirana nezavisno, sve dok se poštuju pravila kompatibilnosti koja nameće protokol (isti identifikatori, doslednost tipova, itd.).


U konkretnoj upotrebi, kada Wallet učitava Contract, mora:




- Učitaj kompajlirani **Schema** (da bi znao strukturu Business Logic) ;
- Učitaj kompajlirani **Interface** (da razumeš imena i operacije sa korisničke strane) ;
- Učitaj kompajlirani **Interface Implementation** (da povežeš logiku Schema sa imenima Interface, operacija po operacija, polje po polje).


Ova modularna arhitektura omogućava scenarije upotrebe kao što su :




- Ograniči određene operacije za određene korisnike: ponudi delimičnu Implementaciju Interface koja omogućava pristup samo osnovnim transferima, bez omogućavanja funkcija spaljivanja ili ažuriranja, na primer;
- Promeni prezentaciju: dizajniraj Interface Implementation koji preimenuje polje u Interface ili ga drugačije mapira, bez menjanja osnove Contract;
- Podržava više šema: Wallet može učitati više Interface implementacija za isti tip Interface, kako bi se obradile različite šeme (različite logike tokena), pod uslovom da je njihova struktura kompatibilna.


U sledećem poglavlju, pogledaćemo kako funkcioniše transfer Contract, i kako se generišu fakture RGB.


## Contract transferi


<chapterId>f043a307-d420-5752-b0d7-ebfd845802c0</chapterId>


:::video id=75eb5a8d-1910-4155-b5e3-81204c9a8901:::


U ovom poglavlju ćemo analizirati proces prenosa Contract u ekosistemu RGB. Da bismo to ilustrovali, pogledaćemo Alisu i Boba, naše uobičajene protagoniste, koji žele da Exchange RGB imovinu. Takođe ćemo prikazati neke isečke komandi iz `RGB` alatke komandne linije, da bismo videli kako to funkcioniše u praksi.


### Razumevanje RGB Contract transfera


Hajde da uzmemo primer transfera između Alice i Boba. U ovom primeru, pretpostavljamo da Bob tek počinje da koristi RGB, dok Alice već drži RGB sredstva u svom Wallet. Videćemo kako Bob postavlja svoje okruženje, uvozi relevantni Contract, zatim zahteva transfer od Alice, i na kraju kako Alice izvršava stvarnu transakciju na Bitcoin Blockchain.


#### 1) Instaliranje RGB Wallet


Prvo, Bob treba da instalira RGB Wallet, tj. softver kompatibilan sa protokolom. Ovo u početku ne sadrži nikakve ugovore. Bob će takođe trebati:




- A Bitcoin Wallet da upravljate svojim UTXO-ima;
- Veza sa Bitcoin čvorom (ili sa Electrum serverom), kako biste mogli identifikovati svoje UTXO-e i propagirati svoje transakcije na mreži.


Kao podsetnik, **Owned States** u RGB odnose se na Bitcoin UTXO-e. Stoga uvek moramo biti u mogućnosti da upravljamo i trošimo UTXO-e u Bitcoin transakciji koja uključuje kriptografske obaveze (`Tapret` ili `Opret`) koje ukazuju na RGB podatke.


#### 2) Contract prikupljanje informacija


Bob zatim treba da preuzme podatke Contract koji ga zanimaju. Ovi podaci mogu cirkulisati putem bilo kog kanala: vebsajt, e-mail, aplikacija za razmenu poruka... U praksi, oni su grupisani zajedno u ***Consignment***, tj. mali paket podataka koji sadrži:




- **Genesis**, koji definiše početno stanje Contract;
- **Schema**, koji opisuje Business Logic (strogi tipovi, skripte za validaciju, itd.);
- **Interface**, koji definiše prezentaciju Layer (nazivi polja, dostupne operacije);
- **Interface Implementation**, koji konkretno povezuje Schema sa Interface.


![RGB-Bitcoin](assets/fr/075.webp)


Ukupna veličina je često reda veličine nekoliko kilobajta, jer svaka komponenta obično teži manje od 200 bajtova. Takođe je moguće emitovati ovaj Consignment u Base58, putem kanala otpornih na cenzuru (kao što su Nostr ili putem Lightning Network, na primer), ili kao QR kod.


#### 3) Contract uvoz i validacija


Jednom kada Bob primi Consignment, on ga uvozi u svoj RGB Wallet. Ovo će zatim :




- Proveri da li su Genesis i Schema validni;
- Učitaj Interface i Interface Implementation ;
- Ažurirajte podatke na strani klijenta Stash.


Bob sada može videti sredstvo u svom Wallet (čak i ako ga još ne poseduje) i razumeti koja su polja dostupna, koje operacije su moguće... Zatim treba da kontaktira osobu koja zapravo poseduje sredstvo koje treba preneti. U našem primeru, to je Alice.


Proces otkrivanja ko drži određenu RGB imovinu sličan je pronalaženju Bitcoin platioca. Detalji ove veze zavise od upotrebe (tržišta, privatni kanali za ćaskanje, fakturisanje, prodaja robe i usluga, plata...).


#### 4) Izdavanje Invoice


Da bi pokrenuo prenos RGB sredstva, Bob prvo mora izdati Invoice. Ovaj Invoice se koristi za :




- Recite Alice vrstu operacije koja treba da se izvrši (na primer, `Transfer` sa RGB20 Interface);
- Obezbedi Alisi Bobov *Seal Definition* (tj. UTXO gde želi da primi sredstvo);
- Navedite količinu aktivnog sastojka (npr. 100 jedinica).


Bob koristi alatku `RGB` na komandnoj liniji. Pretpostavimo da želi 100 jedinica tokena čiji je `ContractId` poznat, želi da se osloni na `Tapret`, i specificira njegov UTXO (`456e3..dfe1:0`) :


```bash
bob$ rgb invoice RGB20 100 <ContractId> tapret1st:456e3..dfe1:0
```


Na kraju ovog poglavlja detaljnije ćemo pogledati strukturu faktura RGB.


#### 5) Invoice prenos


Generisani Invoice (npr. kao URL: `RGB:2WBcas9.../RGB20/100+utxob:...`) sadrži sve informacije koje su Alisi potrebne za pripremu transfera. Kao i kod Consignment, može biti kompaktno kodiran (Base58 ili neki drugi format) i poslat putem aplikacije za razmenu poruka, e-maila, Nostr...


![RGB-Bitcoin](assets/fr/076.webp)


#### 6) Priprema transakcije na strani Alice


Alisa prima Bobov Invoice. U njenom RGB Wallet, ona ima Stash koji sadrži imovinu za prenos. Da bi potrošila UTXO koji sadrži imovinu, ona prvo mora generate PSBT (*Partially Signed Bitcoin Transaction*), tj. nepotpunu Bitcoin transakciju, koristeći UTXO koji ima:


```bash
alice$ wallet construct tx.psbt
```


Ova osnovna transakcija (trenutno nepotpisana) će se koristiti za Anchor kriptografski Commitment povezan sa transferom Bobu. Alisin UTXO će tako biti potrošen, a u izlazu ćemo postaviti `Tapret` ili `Opret` Commitment za Boba.


#### 7) Generisanje transfera Consignment


Zatim, Alice gradi ***Terminal Consignment*** (ponekad nazivan "transfer Consignment") putem komande :


```bash
alice$ rgb transfer tx.psbt <invoice> consignment.rgb
```


Ova nova datoteka `Consignment.RGB` sadrži :




- Kompletna istorija državnih tranzicija potrebnih za validaciju sredstva do sadašnjeg vremena (od Genesis);
- Novi State Transition koji prenosi imovinu sa Alice na Boba, prema Invoice koji je Bob izdao;
- Nepotpuna transakcija Bitcoin (*Witness Transaction*) (`tx.PSBT`), koja troši Alisin Single-Use Seal, modifikovana da uključi kriptografski Commitment Bobu.


U ovoj fazi, transakcija još nije emitovana na Bitcoin mreži. Consignment je veći od osnovnog Consignment, jer uključuje celu istoriju (*proof chain*) da bi se dokazala legitimnost sredstva.


#### 8) Bob proverava i prihvata Consignment


Alisa prenosi ovaj **Terminal Consignment** Bobu. Bob će zatim:




- Proverite validnost State Transition (osigurajte da je istorija dosledna, da su poštovana pravila Contract, itd.);
- Dodajte to svom lokalnom Stash;
- Moguće da je generate potpis (`sig:...`) na Consignment, kako bi se dokazalo da je pregledan i odobren (ponekad se naziva "*platna lista*").


```bash
bob$ rgb accept consignment.rgb
sig:DbwzvSu4BZU81jEpE9FVZ3xjcyuTKWWy2gmdnaxtACrS
```


![RGB-Bitcoin](assets/fr/077.webp)


#### 9) Opcija: Bob šalje potvrdu nazad Alisi (*platni listić*)


Ako Bob želi, može poslati ovaj potpis nazad Alisi. Ovo označava:




- Da prepoznaje tranziciju kao važeću;
- Da se slaže da se transakcija Bitcoin emituje.


Ovo nije obavezno, ali može pružiti Alisi uverenje da neće biti naknadnih sporova oko prenosa.


#### 10) Alis potpisuje i objavljuje transakciju


Alice tada može:




- Proveri Bobov potpis (`RGB check <sig>`) ;
- Potpiši *Witness Transaction* koji je još uvek PSBT (`Wallet potpis`) ;
- Objavi Witness Transaction na Bitcoin mreži (`-publish`).


```bash
alice$ rgb check <sig>
alice$ wallet sign —publish tx.psbt
```


![RGB-Bitcoin](assets/fr/078.webp)


Jednom potvrđeno, ova transakcija označava zaključak prenosa. Bob postaje novi vlasnik sredstva: sada ima Owned State koji pokazuje na UTXO koji on kontroliše, što je dokazano prisustvom Commitment u transakciji.


Da rezimiramo, ovde je kompletan proces prenosa:


![RGB-Bitcoin](assets/fr/079.webp)


### Prednosti RGB transfera




- Poverljivost** :


Samo Alice i Bob imaju pristup svim State Transition podacima. Oni Exchange ove informacije izvan Blockchain, putem pošiljki. Kriptografske obaveze u Bitcoin transakciji ne otkrivaju tip imovine ili iznos, što garantuje daleko veću poverljivost od drugih On-Chain token sistema.




- Validacija na strani klijenta** :


Bob može proveriti doslednost prenosa poređenjem *Consignment* sa *sidrima* u Bitcoin Blockchain. Njemu nije potrebna validacija od strane trećih lica. Alisa ne mora objaviti celu istoriju na Blockchain, što smanjuje opterećenje osnovnog protokola i poboljšava poverljivost.




- Pojednostavljena atomskost** :


Složene razmene (atomski svopovi između BTC i RGB imovine, na primer) mogu se izvršiti unutar jedne transakcije, izbegavajući potrebu za HTLC ili PTLC skriptama. Ako dogovor nije emitovan, svi mogu ponovo koristiti svoje UTXO na druge načine.


### Dijagram sažetka transfera


Pre nego što detaljnije pogledamo fakture, evo dijagrama sažetka celokupnog toka prenosa RGB:




- Bob instalira RGB Wallet i dobija početni Contract Consignment;
- Bob izdaje Invoice pominjući UTXO gde da primi imovinu;
- Alisa prima Invoice, gradi PSBT i generiše Terminal Consignment;
- Bob to prihvata, proverava, dodaje podatke u svoj Stash i potpisuje (*platni listić*) ako je potrebno;
- Alice objavljuje transakciju na Bitcoin mreži;
- Potvrda transakcije čini prenos zvaničnim.


![RGB-Bitcoin](assets/fr/080.webp)


Transfer pokazuje svu moć i fleksibilnost RGB protokola: privatni Exchange, validiran na strani klijenta, minimalno i diskretno usidren na Bitcoin Blockchain, zadržavajući najbolje od sigurnosti protokola (bez rizika od Double-spending). Ovo čini RGB obećavajućim ekosistemom za prenose vrednosti koji su poverljiviji i skalabilniji od On-Chain programabilnih blokčejnova.


### Fakture RGB


U ovom odeljku ćemo detaljno objasniti kako **fakture** funkcionišu u ekosistemu RGB i kako omogućavaju obavljanje operacija (posebno transfera) sa Contract. Prvo ćemo pogledati korišćene identifikatore, zatim kako su kodirani, i na kraju strukturu Invoice izraženu kao URL (format koji je dovoljno praktičan za korišćenje u novčanicima).


#### Identifikatori i kodiranje


Jedinstveni identifikator je definisan za svaki od sledećih Elements:




- An RGB Contract;
- Njegov Schema (Business Logic) ;
- Njegov Interface i Interface Implementation ;
- Njegova sredstva (tokeni, NFT, itd.),


Ova jedinstvenost je veoma važna, jer svaki komponent sistema mora biti prepoznatljiv. Na primer, Contract X ne sme biti pomešan sa drugim Contract Y, i dva različita interfejsa (na primer, RGB20 naspram RGB21) moraju imati različite identifikatore.


Da bismo učinili ove identifikatore i efikasnim (male veličine) i čitljivim, koristimo :




- Base58 kodiranje, koje izbegava upotrebu zbunjujućih karaktera (npr. `0` i slovo `O`) i pruža relativno kratke stringove;
- Prefiks koji označava prirodu identifikatora, obično u obliku `RGB:` ili sličan URN.


Na primer, `ContractId` bi mogao biti predstavljen nečim poput:


```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```


Prefiks `RGB:` potvrđuje da je ovo identifikator RGB, a ne HTTP link ili neki drugi protokol. Zahvaljujući ovom prefiksu, novčanici mogu pravilno protumačiti string.


#### Segmentacija identifikatora


Identifikatori RGB su često prilično dugi, jer osnovna (kriptografska) sigurnost može zahtevati polja od 256 bita ili više. Da bismo olakšali čitanje i verifikaciju od strane ljudi, *delimo* ove stringove u nekoliko blokova odvojenih crticom (`-`). Dakle, umesto da imamo dugačak, neprekinut niz karaktera, delimo ga na kraće blokove. Ova praksa je uobičajena za brojeve kreditnih kartica ili telefona, i takođe se primenjuje ovde radi lakše verifikacije. Na primer, korisniku ili partneru se može reći: "*Molimo vas da proverite da li je treći blok `9GEgnyMj7`*", umesto da moraju da upoređuju ceo niz odjednom. Poslednji blok se često koristi kao **kontrolna suma**, kako bi se imao sistem za detekciju grešaka ili tipografskih grešaka.


Na primer, `ContractId` kodiran u base58 i segmentiran može biti :


```txt
2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```


Svaka crtica deli niz na sekcije. Ovo ne utiče na semantiku koda, već samo na njegovu prezentaciju.


#### Korišćenje URL-ova za fakture


An RGB Invoice je predstavljen kao URL. To znači da se može kliknuti ili skenirati (kao QR kod), a Wallet ga može direktno interpretirati za obavljanje transakcije. Ova jednostavnost interakcije se razlikuje od nekih drugih sistema gde morate kopirati i zalepiti različite delove podataka u različita polja u softveru.


Invoice za fungibilni token (npr. RGB20 token) može izgledati ovako:


```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```


Hajde da analiziramo ovaj URL:




- `RGB:`** (prefiks): označava vezu koja poziva RGB protokol (analogno `http:` ili `Bitcoin:` u drugim kontekstima);
- `2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX`**: predstavlja `ContractId` tokena kojim želite da manipulišete;
- `/RGB20/100`**: označava da se koristi `RGB20` Interface i da je zatraženo 100 jedinica sredstva. Sintaksa je: `/Interface/amount` ;
- `+utxob:`**: specificira da su dodate informacije o primaocu UTXO (ili, preciznije, definicija Single-Use Seal);
- `egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb`**: ovo je *blinded* UTXO (ili Seal Definition). Drugim rečima, Bob je prikrio svoj tačan UTXO, tako da pošiljalac (Alice) ne zna koji je tačan Address. Ona samo zna da postoji važeći Seal koji se odnosi na UTXO kojim upravlja Bob.


Činjenica da se sve uklapa u jedan URL olakšava život korisniku: jednostavan klik ili skeniranje u Wallet, i operacija je spremna za izvršenje.


Čovek bi mogao zamisliti sisteme gde se jednostavan ticker (npr. `USDT`) koristi umesto `ContractId`. Međutim, to bi izazvalo velike probleme poverenja i sigurnosti: ticker nije jedinstvena referenca (nekoliko ugovora bi moglo tvrditi da se zovu `USDT`). Sa RGB, želimo jedinstveni, nedvosmisleni kriptografski identifikator. Stoga je usvojen 256-bitni string, kodiran u base58 i segmentiran. Korisnik zna da manipuliše upravo sa Contract čiji ID je `2WBcas9-yjz...` a ne bilo kojim drugim.


#### Dodatni URL parametri


Takođe možete dodati dodatne parametre u URL, na isti način kao kod HTTP, kao što su:


```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb?sig=6kzbKKffP6xftkxn9UP8gWqiC41W16wYKE5CYaVhmEve
```




- `?sig=...`: predstavlja, na primer, potpis povezan sa Invoice, koji neki novčanici mogu verifikovati;
- Ako Wallet ne upravlja ovim potpisom, jednostavno ignoriše ovaj parametar.


Hajde da razmotrimo slučaj NFT-a putem RGB21 Interface. Na primer, mogli bismo imati:


```txt
rgb:7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK/RGB21/DbwzvSu-4BZU81jEp-E9FVZ3xj-cyuTKWWy-2gmdnaxt-ACrS+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```


Ovde vidimo :




- `RGB:`**: URL prefiks ;
- `7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK`**: Contract ID (NFT) ;
- rGB21**: Interface za nezamenljive asete (NFT) ;
- `DbwzvSu-4BZU81jEp-...`**: eksplicitna referenca na jedinstveni deo NFT-a, na primer Hash podatkovnog bloba (mediji, metapodaci...);
- `+utxob:egXsFnw-...`**: the Seal Definition.


Ideja je ista: preneti jedinstveni link koji Wallet može interpretirati, jasno identifikujući jedinstvenu imovinu koja se prenosi.


#### Druge operacije putem URL-a


RGB URL-ovi se ne koriste samo za zahtev za transfer. Oni takođe mogu kodirati naprednije operacije, kao što je izdavanje novih tokena (*issuance*). Na primer:


```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/issue/100000+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```


Ovde nalazimo :




- `RGB:` : protokol ;
- `2WBcas9-...`: Contract ID ;
- `/RGB20/issue/100000`: označava da želite da pokrenete tranziciju "*Issue*" kako biste kreirali dodatnih 100.000 tokena;
- `+utxob:`: the Seal Definition.


Na primer, Wallet bi mogao glasiti: "Zamoljen sam da izvršim operaciju `issue` sa `RGB20` Interface, na takvom i takvom Contract, za 100.000 jedinica, u korist takvog i takvog Single-Use Seal.*"


Sada kada smo pogledali glavni Elements programiranja RGB, provesti ću vas kroz sledeće poglavlje o tome kako izraditi RGB Contract.


## Izrada pametnih ugovora


<chapterId>0e0a645c-0049-588d-8965-b8c536590cc9</chapterId>


:::video id=a3ad6dcd-90b8-4272-9dfc-76c85c859167:::


U ovom poglavlju, pristupićemo pisanju Contract korak po korak, koristeći alatku komandne linije `RGB`. Cilj je pokazati kako instalirati i manipulisati CLI, kompajlirati **Schema**, uvesti **Interface** i **Interface Implementation**, a zatim izdati (*issue*) sredstvo. Takođe ćemo pogledati osnovnu logiku, uključujući kompajliranje i validaciju stanja. Na kraju ovog poglavlja, trebali biste biti u mogućnosti da reprodukujete proces i kreirate sopstvene RGB ugovore.


Kao podsetnik, interna logika RGB zasnovana je na Rust bibliotekama koje vi, kao programeri, možete uvesti u svoje projekte kako biste upravljali delom Client-side Validation. Pored toga, tim LNP/BP Association radi na povezivanju za druge jezike, ali to još nije finalizovano. Pored toga, druge entitete kao što je Bitfinex razvijaju svoje sopstvene integracione stekove (o njima ćemo govoriti u poslednja 2 poglavlja kursa). Za sada, dakle, `RGB` CLI je zvanična referenca, čak i ako ostaje relativno neizbrušena.


### Instalacija i prezentacija alata RGB


Glavna komanda se jednostavno zove `RGB`. Dizajnirana je da podseća na `git`, sa skupom podkomandi za manipulaciju ugovorima, njihovo pokretanje, izdavanje sredstava i slično. Bitcoin Wallet trenutno nije integrisan, ali će biti u skoroj verziji (0.11). Ova sledeća verzija će omogućiti korisnicima da kreiraju i upravljaju svojim novčanicima (putem deskriptora) direktno iz `RGB`, uključujući generisanje PSBT, kompatibilnost sa eksternim hardverom (npr. Hardware Wallet) za potpisivanje, i interoperabilnost sa softverom kao što je Sparrow. Ovo će pojednostaviti ceo scenario izdavanja i prenosa sredstava.


#### Instalacija putem Cargo-a


Instaliramo alat u Rust sa :


```bash
cargo install rgb-contracts --all-features
```


(Napomena: paket se zove `RGB-contracts`, a instalirana komanda će biti nazvana `RGB`. Ako je paket pod imenom `RGB` već postojao, moglo je doći do konflikta, stoga je naziv ovakav)


Instalacija kompajlira veliki broj zavisnosti (npr. parsiranje komandi, integracija sa Electrum-om, upravljanje dokazima bez saznanja, itd.).


Kada je instalacija završena, :


```bash
rgb
```


Pokretanje `RGB` (bez argumenata) prikazuje listu dostupnih pod-komandi, kao što su `interfaces`, `Schema`, `import`, `export`, `issue`, `Invoice`, `transfer`, itd. Možete promeniti lokalni direktorijum za skladištenje (Stash koji sadrži sve logove, šeme i implementacije), izabrati mrežu (Testnet, Mainnet) ili konfigurisati vaš Electrum server.


![RGB-Bitcoin](assets/fr/081.webp)


#### Prvi pregled kontrola


Kada pokrenete sledeću komandu, videćete da je `RGB20` Interface već integrisan po defaultu:


```bash
rgb interfaces
```


Ako ovaj Interface nije integrisan, kloniraj :


```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```


Sastavi ga:


```bash
cargo run
```


Zatim uvezite Interface po vašem izboru:


```bash
rgb import interfaces/RGB20.rgb
```


![RGB-Bitcoin](assets/fr/082.webp)


S druge strane, rečeno nam je da nijedan Schema još nije uvezen u softver. Takođe, nema Contract u Stash. Da biste to videli, pokrenite komandu :


```bash
rgb schemata
```


Zatim možete klonirati spremište da biste preuzeli određene sheme:


```bash
git clone https://github.com/RGB-WG/rgb-schemata
```


![RGB-Bitcoin](assets/fr/083.webp)


Ovo spremište sadrži, u svom direktorijumu `src/`, nekoliko Rust datoteka (na primer `nia.rs`) koje definišu šeme (NIA za "*Non Inflatable Asset*", UDA za "*Unique Digital Asset*", itd.). Da biste kompajlirali, možete zatim pokrenuti :


```bash
cd rgb-schemata
cargo run
```


Ovo generiše nekoliko `.RGB` i `.rgba` fajlova koji odgovaraju kompajliranim šemama. Na primer, naći ćete `NonInflatableAsset.RGB`.


#### Uvoz Schema i Interface Implementation


Sada možete uvesti šemu u `RGB` :


```bash
rgb import schemata/NonInflatableAssets.rgb
```


![RGB-Bitcoin](assets/fr/084.webp)


Ovo ga dodaje lokalnom Stash. Ako pokrenemo sledeću komandu, vidimo da se sada pojavljuje Schema:


```bash
rgb schemata
```


### Contract kreiranje (izdavanje)


Postoje dva pristupa kreiranju nove imovine:




- Ili koristimo skriptu ili kod u Rust koji gradi Contract popunjavanjem Schema polja (Global State, Owned States, itd.) i proizvodi `.RGB` ili `.rgba` fajl;
- Ili direktno koristite podkomandu `issue`, sa YAML (ili TOML) fajlom koji opisuje svojstva tokena.


You can find examples in Rust in the `examples` folder, which illustrate how you build a `ContractBuilder`, fill in the `Global State` (asset name, ticker, Supply, date, etc.), define the Owned State (to which UTXO it is assigned), then compile all this into a *Contract Consignment* that you can export, validate and import into a Stash.


Drugi način je ručno uređivanje YAML datoteke za prilagođavanje `ticker`, `name`, `Supply`, i tako dalje. Pretpostavimo da se datoteka zove `RGB20-demo.yaml`. Možete navesti :




- `spec`: oznaka, ime, preciznost ;
- `terms`: polje za pravne napomene ;
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


![RGB-Bitcoin](assets/fr/085.webp)


Zatim jednostavno pokrenite komandu :


```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```


![RGB-Bitcoin](assets/fr/086.webp)


U mom slučaju, jedinstveni Schema identifikator (koji treba staviti u jednostruke navodnike) je `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` i nisam naveo izdavaoca. Dakle, moja narudžba je :


```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```


Ako ne znate Schema ID, pokrenite komandu :


```bash
rgb schemata
```


CLI odgovara da je novi Contract izdat i dodat u Stash. Ako unesemo sledeću komandu, vidimo da sada postoji dodatni Contract, koji odgovara upravo izdatom:


```bash
rgb contracts
```


![RGB-Bitcoin](assets/fr/087.webp)


Zatim, sledeća komanda prikazuje globalna stanja (ime, oznaka, Supply...) i listu Posedovanih Stanja, tj. alokacije (na primer, 1 milion `PBN` tokena definisanih u UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`).


```bash
rgb state '<ContractId>'
```


![RGB-Bitcoin](assets/fr/088.webp)


### Izvoz, uvoz i validacija


Da biste podelili ovaj Contract sa drugim korisnicima, može se izvesti iz Stash u:


```bash
rgb export '<ContractId>' myContractPBN.rgb
```


![RGB-Bitcoin](assets/fr/089.webp)


Datoteku `myContractPBN.RGB` može proslediti drugom korisniku, koji je može dodati svom Stash pomoću komande :


```bash
rgb import myContractPBN.rgb
```


Na uvozu, ako je to jednostavan *Contract Consignment*, dobićemo poruku "`Importing Consignment RGB`". Ako je veći *State Transition Consignment*, komanda će biti drugačija (`RGB accept`).


Da biste osigurali validnost, možete koristiti i lokalnu funkciju validacije. Na primer, možete pokrenuti :


```bash
rgb validate myContract.rgb
```


#### Stash upotreba, verifikacija i prikaz


Kao podsetnik, Stash je lokalni inventar šema, interfejsa, implementacija i ugovora (Genesis + tranzicije). Svaki put kada pokrenete "import", dodajete element u Stash. Ovaj Stash se može detaljno pregledati komandom :


```bash
rgb dump
```


![RGB-Bitcoin](assets/fr/090.webp)


Ovo će generate fasciklu sa detaljima celog Stash.


### Transfer i PSBT


Da biste izvršili transfer, potrebno je da manipulišete lokalnim Bitcoin Wallet kako biste upravljali obavezama `Tapret` ili `Opret`.


#### generate an Invoice


U većini slučajeva, interakcija između učesnika u Contract (npr. Alice i Bob) odvija se putem generisanja Invoice. Ako Alice želi da Bob izvrši nešto (prenos tokena, ponovno izdavanje, akciju u DAO, itd.), Alice kreira Invoice sa detaljnim instrukcijama za Boba. Tako imamo :




- Alice** (izdavalac Invoice) ;
- Bob** (koji prima i izvršava Invoice).


Za razliku od drugih ekosistema, RGB Invoice nije ograničen na pojam plaćanja. Može ugraditi bilo koji zahtev povezan sa Contract: opozvati ključ, glasati, kreirati gravuru (*gravura*) na NFT-u, itd. Odgovarajuća operacija može biti opisana u Contract Interface. Odgovarajuća operacija može biti opisana u Contract Interface.


Sledeća komanda generiše RGB Invoice:


```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```


Sa :




- `$Contract`: Contract identifikator (*ContractId*) ;
- `$Interface`: Interface da se koristi (npr. `RGB20`) ;
- `$ACTION`: naziv operacije naveden u Interface (za jednostavan prenos fungibilnog tokena, to može biti "Transfer"). Ako Interface već pruža podrazumevanu akciju, ne morate je ponovo unositi ovde;
- `$STATE`: status podataka koji treba preneti (na primer, količina tokena ako se prenosi fungibilni token);
- `$Seal`: korisnikova (Aliceina) Single-Use Seal, tj. eksplicitna referenca na UTXO. Bob će koristiti ove informacije za izgradnju Witness Transaction, a odgovarajući izlaz će tada pripadati Alice (u *blinded UTXO* ili nešifrovanom obliku).


Na primer, sa sledećim komandama


```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```


CLI će generate an Invoice like :


```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```


Može se preneti Bobu putem bilo kog kanala (tekst, QR kod, itd.).


#### Pravljenje prenosa


Da prenesete sa ovog Invoice :




- Bob (koji drži tokene u svom Stash) ima Bitcoin Wallet. On treba da pripremi Bitcoin transakciju (u obliku PSBT, npr. `tx.PSBT`) koja troši UTXO-e gde se nalaze potrebni RGB tokeni, plus jedan UTXO za valutu (Exchange) ;
- Bob izvršava sledeću komandu:


```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```




- Ovo generiše datoteku `Consignment.RGB` koja sadrži :
 - Istorija prelaza koja dokazuje Alisi da su tokeni autentični;
 - Novi prelaz koji prenosi tokene na Alisin Single-Use Seal ;
 - Witness Transaction (nepotpisano).
- Bob šalje ovu datoteku `Consignment.RGB` Alisi (putem e-maila, servera za deljenje ili RGB-RPC protokola, Storm, itd.);
- Alice prima `Consignment.RGB` i prihvata ga u svom Stash :


```bash
alice$ rgb accept consignment.rgb
```




- CLI proverava validnost tranzicije i dodaje je na Alisin Stash. Ako je nevažeća, komanda ne uspeva sa detaljnim porukama o grešci. U suprotnom, uspeva i izveštava da uzorak transakcije još nije emitovan na Bitcoin mreži (Bob čeka na Alisin Green svetlo);
- Kao potvrdu, komanda `accept` vraća potpis (*platni listić*) koji Alisa može poslati Bobu da mu pokaže da je potvrdila *Consignment* ;
- Bob zatim može potpisati i objaviti (`--publish`) svoju Bitcoin transakciju:


```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```




- Čim se ova transakcija potvrdi On-Chain, Ownership sredstva se smatra prenetim na Alisu. Alisin Wallet, prateći Mining transakcije, vidi novi Owned State kako se pojavljuje u njenom Stash.


U sledećem poglavlju, detaljnije ćemo razmotriti integraciju RGB u Lightning Network.


## RGB na Lightning Network


<chapterId>0962980a-8f94-5d0f-9cd0-43d7f884a01d</chapterId>


:::video id=be25a165-6e23-488c-91d8-3dcfccc6eca1:::


U ovom poglavlju predlažem da ispitamo kako se RGB može koristiti unutar Lightning Network, za integraciju i prenos RGB sredstava (tokena, NFT-ova, itd.) putem off-chain platnih kanala.


Osnovna ideja je da se RGB State Transition (*State Transition*) može obavezati na Bitcoin transakciju koja, zauzvrat, može ostati off-chain sve dok se Lightning kanal ne zatvori. Dakle, svaki put kada se kanal ažurira, novi RGB State Transition može biti uključen u novu obavezujuću transakciju, koja zatim poništava staru tranziciju. Na ovaj način, Lightning kanali se mogu koristiti za prenos RGB sredstava, i mogu se rutirati na isti način kao konvencionalna Lightning plaćanja.


### Kreiranje i finansiranje kanala


Da bismo kreirali Lightning kanal koji nosi RGB sredstva, potrebna su nam dva Elements:




- Bitcoin finansiranje za kreiranje kanala 2/2 Multisig (osnovni UTXO za kanal);
- RGB finansiranje, koje šalje sredstva istom Multisig.


U terminima Bitcoin, transakcija finansiranja mora postojati da bi se definisala referenca UTXO, čak i ako sadrži samo malu količinu Sats (svejedno je da li svaki izlaz u budućim Commitment transakcijama ostaje iznad Dust limita). Na primer, Alisa može odlučiti da obezbedi 10k Sats i 500 USDT (izdatih kao RGB sredstvo). Na transakciji finansiranja, dodajemo Commitment (`Opret` ili `Tapret`) koji sidri RGB State Transition.


![RGB-Bitcoin](assets/fr/091.webp)


Jednom kada je transakcija finansiranja pripremljena (ali još nije emitovana), kreiraju se Commitment transakcije tako da bilo koja strana može jednostrano zatvoriti kanal u bilo kom trenutku. Ove transakcije podsećaju na klasične Lightning Commitment transakcije, osim što dodajemo dodatni izlaz koji sadrži RGB Anchor (OP_RETURN ili Taproot) povezan sa novim State Transition.


RGB State Transition zatim premešta sredstva sa 2/2 Multisig finansiranja na izlaze Commitment Transaction. Prednost ovog procesa je što bezbednost RGB stanja tačno odgovara Lightning-ovim kaznenim mehanikama: ako Bob emituje staro stanje kanala, Alisa može da ga kazni i potroši izlaz, kako bi povratila i Sats i RGB tokene. Podsticaj je stoga još jači nego u Lightning kanalu bez RGB sredstava, jer napadač može izgubiti ne samo Sats, već i RGB sredstva kanala.


Commitment Transaction potpisan od strane Alice i poslat Bobu bi stoga izgledao ovako:


![RGB-Bitcoin](assets/fr/092.webp)


A prateći Commitment Transaction, potpisan od strane Boba i poslat Alisi, izgledaće ovako:


![RGB-Bitcoin](assets/fr/093.webp)


### Ažuriranje kanala


Kada dođe do plaćanja između dva učesnika kanala (ili žele da promene raspodelu sredstava), oni kreiraju novi par Commitment transakcija. Iznos u Sats na svakom izlazu može, ali i ne mora ostati nepromenjen, u zavisnosti od implementacije, jer je njegova glavna uloga omogućavanje konstrukcije validnih UTXO-a. S druge strane, OP_RETURN (ili Taproot) izlaz mora biti modifikovan da sadrži novi RGB Anchor, koji predstavlja novu raspodelu sredstava u kanalu.


Na primer, ako Alisa prenese 30 USDT Bobu u kanalu, novi State Transition će odražavati saldo od 400 USDT za Alisu i 100 USDT za Boba. Transakcija potvrde se dodaje (ili modifikuje) od strane OP_RETURN/Taproot Anchor kako bi uključila ovu tranziciju. Imajte na umu da, iz perspektive RGB, ulaz u tranziciju ostaje početni Multisig (gde su On-Chain sredstva zapravo alocirana dok se kanal ne zatvori). Samo se RGB izlazi (alokacije) menjaju, u zavisnosti od odlučene preraspodele.


Commitment Transaction potpisan od strane Alice, spreman za distribuciju od strane Boba :


![RGB-Bitcoin](assets/fr/094.webp)


Commitment Transaction potpisan od strane Boba, spreman za distribuciju od strane Alise :


![RGB-Bitcoin](assets/fr/095.webp)


### HTLC upravljanje


U stvarnosti, Lightning Network omogućava da se plaćanja usmeravaju putem više kanala, koristeći HTLCs (*Hashed Time-Locked Contracts*). Isto je i sa RGB: za svako plaćanje u tranzitu kroz kanal, HTLC izlaz se dodaje transakciji koja se izvršava, i RGB alokacija povezana sa ovim HTLC. Dakle, ko god potroši HTLC izlaz (zahvaljujući tajni ili nakon isteka vremenskog zaključavanja) povratiće i Sats i povezane RGB resurse. S druge strane, očigledno je da morate imati dovoljno gotovine na putu u smislu i Sats i RGB resursa.


![RGB-Bitcoin](assets/fr/096.webp)


Rad RGB na Lightning-u mora se stoga razmatrati paralelno sa radom samog Lightning Network. Ako želite dublje istražiti ovu temu, toplo preporučujem da pogledate ovaj drugi sveobuhvatni kurs obuke:


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### RGB kodna mapa


Konačno, pre nego što pređemo na sledeći deo, želeo bih da vam dam pregled koda korišćenog u RGB. Protokol se zasniva na skupu Rust biblioteka i specifikacija otvorenog koda. Evo pregleda glavnih repozitorijuma i sanduka:


![RGB-Bitcoin](assets/fr/097.webp)


#### Client-side Validation




- Repozitorijum**: [client_side_validation](https://github.com/LNP-BP/client_side_validation)
- Crates** : [client_side_validation](https://crates.io/crates/client_side_validation), [single_use_seals](https://crates.io/crates/single_use_seals)


Upravljanje validacijom off-chain i logikom jednokratnih zaptivki.


#### Determinističke Bitcoin Obaveze (DBC)




- Repozitorijum**: [bp-core](https://github.com/BP-WG/bp-core)
- Crate**: [bp-dbc](https://crates.io/crates/bp-dbc)


Upravljanje determinističkim sidrenjem u Bitcoin transakcijama (Tapret, OP_RETURN, itd.).


#### Multi Protocol Commitment (MPC)




- Repozitorijum**: [client_side_validation](https://github.com/LNP-BP/client_side_validation)
- Crate** : [commit_verify](https://crates.io/crates/commit_verify)


Višestruke kombinacije angažmana i integracija sa različitim protokolima.


#### Strogi tipovi & Strogo kodiranje




- Specifikacije**: [website strict-types.org](https://www.strict-types.org/)
- Repozitorijumi**: [strict-types](https://github.com/strict-types/strict-types), [strict-encoding](https://github.com/strict-types/strict-encoding)
- Crates** : [strict_types](https://crates.io/crates/strict_types), [strict_encoding](https://crates.io/crates/strict_encoding)


Strogi sistem tipizacije i deterministička serijalizacija korišćeni za Client-side Validation.


#### RGB Core




- Repozitorijum**: [RGB-core](https://github.com/RGB-WG/RGB-core)
- Crate**: [RGB-core](https://crates.io/crates/RGB-core)


Jezgro protokola, koje obuhvata glavnu logiku validacije RGB.


#### RGB Standard Library & Wallet




- Repozitorijum**: [RGB-std](https://github.com/RGB-WG/RGB-std)
- Crate** : [RGB-std](https://crates.io/crates/RGB-std)


Standardne implementacije, Stash i Wallet upravljanje.


#### RGB CLI




- Repozitorijum**: [RGB](https://github.com/RGB-WG/RGB)
- Crates**: [RGB-CLI](https://crates.io/crates/RGB-CLI), [RGB-Wallet](https://crates.io/crates/RGB-Wallet)


`RGB` CLI i sanduk Wallet, za manipulaciju ugovorima putem komandne linije.


#### RGB Schema




- Repozitorijum**: [RGB-schemata](https://github.com/RGB-WG/RGB-schemata/)


Sadrži primere šema (NIA, UDA, itd.) i njihove implementacije.


#### AluVM




- Info** : [AluVM.org](https://www.AluVM.org/)
- Repozitorijumi**: [AluVM-spec](https://github.com/AluVM/AluVM-spec), [alure](https://github.com/AluVM/alure)
- Crates**: [AluVM](https://crates.io/crates/AluVM), [aluasm](https://crates.io/crates/aluasm)


Virtuelna mašina zasnovana na registru koja se koristi za pokretanje skripti za validaciju.


#### Bitcoin Protocol - BP




- Repozitorijumi** : [bp-core](https://github.com/BP-WG/bp-core), [bp-std](https://github.com/BP-WG/bp-std), [bp-Wallet](https://github.com/BP-WG/bp-Wallet)


Dodaci za podršku Bitcoin protokolu (transakcije, zaobilaženja, itd.).


#### Ubiquitous Deterministic Computing - UBIDECO




- Repozitorijum**: [UBIDECO](https://github.com/UBIDECO)


Ekosistem povezan sa razvojem otvorenog koda determinističkog tipa.


# Izgradnja na RGB


<partId>3b4b0d66-0c1b-505a-b5ca-4b2e57dd73c2</partId>


## DIBA i projekat Bitmask


<chapterId>dc92a5e8-ed93-5a3f-bcd0-d433932842f4</chapterId>


:::video id=2ec9a181-a8b0-4da2-b7b5-9dfaaaeb10ba:::


Ovaj završni deo kursa zasnovan je na prezentacijama koje su održali različiti govornici na RGB bootcampu. Uključuje svedočenja i refleksije o RGB i njegovom ekosistemu, kao i prezentacije alata i projekata zasnovanih na protokolu. Ovo prvo poglavlje moderira Hunter Beast, a naredna dva Frederico Tenga.


### Od JavaScripta do Rust, i u ekosistem Bitcoin


U početku, Hunter Beast je uglavnom radio u JavaScript-u. Zatim je otkrio **Rust**, čija sintaksa mu se isprva činila neprivlačnom i frustrirajućom. Međutim, počeo je da ceni moć jezika, kontrolu nad memorijom (*heap* i *stack*), kao i sigurnost i performanse koje dolaze s njim. On naglašava da je Rust odlična osnova za dubinsko razumevanje kako računar funkcioniše.


Hunter Beast opisuje svoje iskustvo u raznim projektima u okviru *Altcoin* ekosistema, kao što su Ethereum (sa Solidity, TypeScript, itd.), a kasnije i Filecoin. Objašnjava da je u početku bio impresioniran nekim protokolima, ali je na kraju osećao razočaranje u većinu njih, ne najmanje zbog njihove tokenomike. On osuđuje sumnjive finansijske podsticaje, inflatorno stvaranje tokena koje razvodnjava investitore, i potencijalno eksploatatorski aspekt ovih projekata. Tako je na kraju usvojio stav **Bitcoin Maximalist**, ne najmanje zato što su mu neki ljudi otvorili oči za zdravije ekonomske mehanizme Bitcoin, i za robusnost ovog sistema.


### Privlačnost RGB i izgradnja na slojevima


Ono što ga je definitivno uverilo u relevantnost Bitcoin, prema njegovim rečima, bilo je otkriće RGB i koncept slojeva. Veruje da bi postojeće funkcionalnosti na drugim blokčejnovima mogle biti reprodukovane na višim slojevima, iznad Bitcoin, bez menjanja osnovnog protokola.


U februaru 2022. pridružio se **DIBA** kako bi radio specifično na RGB, a posebno na **Bitmask** Wallet. U to vreme, Bitmask je bio još uvek na verziji 0.01 i pokretao je RGB na verziji 0.4, samo za upravljanje pojedinačnim tokenima. On primećuje da je to bilo manje orijentisano na samostalno čuvanje nego danas, jer je logika delimično bila zasnovana na serveru. Od tada, arhitektura se razvila ka ovom modelu, koji je veoma cenjen među bitkoinerima.


### Osnove RGB protokola


Protokol **RGB** je najnovija i najnaprednija inkarnacija koncepta _colored coins_, koji je već istraživan oko 2012-2013. U to vreme, nekoliko timova je pokušavalo da poveže različite Bitcoin vrednosti na UTXO-ima, što je dovelo do više raspršenih implementacija. Ovaj nedostatak standardizacije i niska potražnja u to vreme sprečili su ove solucije da steknu trajno uporište.


Danas se RGB ističe svojom konceptualnom robusnošću i ujedinjenim specifikacijama putem LNP/BP asocijacije. Princip se zasniva na Client-side Validation. Bitcoin Blockchain samo skladišti kriptografske obaveze (_commitments_, putem Taproot ili OP_RETURN), dok većinu podataka (Contract definicije, istorije transfera, itd.) skladište korisnici na koje se to odnosi. Na ovaj način, opterećenje skladištenja je raspodeljeno i poverljivost razmena je pojačana, bez opterećivanja Blockchain. Ovaj pristup omogućava kreiranje fungibilnih sredstava (**RGB20** standard) ili jedinstvenih sredstava (**RGB21** standard), unutar modularnog i skalabilnog okvira.


### Funkcija tokena (RGB20) i jedinstvena sredstva (RGB21)


Sa **RGB20**, definišemo fungibilni token na Bitcoin. Izdavač bira _ponudu_, _preciznost_ i kreira _ugovor_ u kojem zatim može vršiti transfere. Svaki transfer se referencira na Bitcoin UTXO, koji deluje kao *Single-Use Seal*. Ova logika osigurava da korisnik neće moći da potroši isti aset dva puta, jer samo osoba koja je sposobna da potroši UTXO zapravo drži ključ za ažuriranje stanja klijentske strane Contract.


**RGB21** cilja na jedinstvene resurse (ili "NFT"). Resurs ima Supply od 1, i može biti povezan sa metapodacima (slikovna datoteka, audio, itd.) opisanim putem specifičnog polja. Za razliku od NFT-ova na javnim blokčejnovima, podaci i njihovi MIME identifikatori mogu ostati privatni, distribuirani peer-to-peer po vlasnikovom nahođenju.


### Rešenje sa bitmaskom: Wallet za RGB


Da bi se u praksi iskoristile mogućnosti RGB, projekat **DIBA** je dizajnirao Wallet pod nazivom [Bitmask](https://bitmask.app/). Ideja je da se obezbedi nekustodijalni alat zasnovan na Taproot, dostupan kao veb aplikacija ili ekstenzija za pregledač. Bitmask upravlja i RGB20 i RGB21 aktivama, i integriše različite sigurnosne mehanizme:




- Osnovni kod je napisan u Rust, zatim kompajliran u WebAssembly da bi se izvršavao u JavaScript okruženju (React);
- Ključevi se generišu lokalno, a zatim se šifrovani čuvaju lokalno ;
- Podaci države (Stash) se čuvaju u memoriji, serijalizovani i enkriptovani putem biblioteke **Carbonado**, koja vrši kompresiju, korekciju grešaka, enkripciju i verifikaciju toka koristeći Blake3.


Zahvaljujući ovoj arhitekturi, sve transakcije imovine odvijaju se na strani klijenta. Sa spoljašnje strane, transakcija Bitcoin nije ništa drugo do klasična Taproot transakcija potrošnje, za koju niko ne bi posumnjao da takođe nosi transfer fungibilnih tokena ili NFT-ova. Odsustvo On-Chain preopterećenja (nema javno pohranjenih metapodataka) garantuje određeni stepen diskrecije i olakšava otpor mogućim pokušajima cenzure.


### Bezbednost i distribuirana arhitektura


U meri u kojoj protokol RGB zahteva da svaki učesnik zadrži svoju istoriju transakcija (kako bi dokazao validnost transfera koje prima), postavlja se pitanje skladištenja. Bitmask predlaže da se ovaj Stash serijalizuje lokalno, a zatim pošalje na nekoliko servera ili oblaka (opciono). Podaci ostaju šifrovani od strane korisnika putem **Carbonado**, tako da server ne može da ih pročita. U slučaju delimične korupcije, korekcija grešaka Layer može rekonstituisati sadržaj.


Korišćenje CRDT (_Conflict-free replicated data type_) omogućava da se različite verzije Stash spoje, ukoliko dođe do njihovog razilaženja. Svi su slobodni da hostuju ove podatke gde god žele, jer nijedan pojedinačni Full node ne nosi sve informacije povezane sa sredstvom. Ovo tačno odražava *Client-side Validation* filozofiju, gde je svaki vlasnik odgovoran za čuvanje dokaza o validnosti njihovog RGB sredstva.


### Ka širem ekosistemu: tržište, interoperabilnost i nove funkcije


Kompanija iza Bitmask-a ne ograničava se na jednostavan razvoj Wallet. DIBA namerava da razvije :




- Tržište za razmenu tokena, posebno u obliku **RGB21**;
- Kompatibilnost sa drugim novčanicima (kao što je *Iris Wallet*);
- Tehnike grupisanja transfera**, tj. mogućnost uključivanja nekoliko uzastopnih RGB transfera u jednu transakciju.


U isto vreme, radimo na **WebBTC** ili **WebLN** (standardi koji omogućavaju vebsajtovima da traže od Wallet da potpiše Bitcoin ili Lightning transakcije), kao i na mogućnosti da "teleburn" Ordinals unose (ako želimo da repatriramo Ordinals u diskretniji i fleksibilniji RGB format).


### Zaključak


Ceo proces pokazuje kako se ekosistem RGB može implementirati i učiniti dostupnim krajnjim korisnicima putem robusnih tehničkih rešenja. Prelaz sa perspektive Altcoin na viziju više usmerenu ka Bitcoin, u kombinaciji sa otkrićem *Client-side Validation*, ilustruje prilično logičan put: razumemo da je moguće implementirati razne funkcionalnosti (zamjenjivi tokeni, NFT, pametni ugovori...) bez forkovanja Blockchain, jednostavno iskorišćavanjem kriptografskih obaveza na Taproot transakcijama ili OP_RETURN-ima.


**Bitmask** Wallet je deo ovog pristupa: na strani Blockchain, sve što vidite je obična Bitcoin transakcija; na strani korisnika, manipulišete web Interface gde kreirate, Exchange i skladištite sve vrste off-chain sredstava. Ovaj model jasno razdvaja monetarnu infrastrukturu (Bitcoin) od logike izdavanja i prenosa (RGB), dok obezbeđuje visok nivo poverljivosti i bolju skalabilnost.


## Rad Bitfinex na RGB


<chapterId>d4d80e07-5eac-5b29-a93a-123180e97047</chapterId>


:::video id=04555813-516f-4eea-9767-7082c2ea6f01:::


U ovom poglavlju, na osnovu prezentacije Frederica Tenge, razmatramo skup alata i projekata koje je kreirao tim Bitfinex posvećen RGB, sa ciljem podsticanja razvoja bogatog i raznovrsnog ekosistema oko ovog protokola. Početni cilj tima nije da objavi specifičan komercijalni proizvod, već da obezbedi softverske građevinske blokove, doprinese samom RGB protokolu i predloži konkretne implementacione reference kao što su mobilni Wallet (*Iris Wallet*) ili RGB-kompatibilan Lightning čvor.


### Pozadina i ciljevi


Od oko 2022. godine, tim Bitfinex RGB se fokusira na razvoj tehnološkog stoga koji omogućava da se RGB efikasno eksploatiše i testira. Napravljeno je nekoliko doprinosa:




- Učešće u izvornom kodu i specifikacijama protokola, uključujući pisanje predloga za poboljšanja, ispravljanje grešaka, itd;
- Alati za programere za pojednostavljenje integracije RGB u njihove aplikacije;
- Dizajn mobilnog Wallet nazvanog [Iris](https://iriswallet.com/) za eksperimentisanje i ilustrovanje najboljih praksi za korišćenje RGB ;
- Kreiranje prilagođenog Lightning čvora, sposobnog za upravljanje kanalima sa RGB sredstvima;
- Podrška drugim timovima u izgradnji rešenja na RGB, kako bi se podstakla raznolikost i snažan ekosistem.


Ovaj pristup ima za cilj da pokrije ceo lanac potreba: od biblioteke niskog nivoa (*[RGBlib](https://github.com/RGB-Tools/RGB-lib)*), koja omogućava implementaciju Wallet, do aspekta proizvodnje (Lightning čvor, Wallet za Android, itd.).


### Biblioteka RGBlib: pojednostavljenje razvoja aplikacija za RGB


Važna tačka u demokratizaciji kreiranja RGB novčanika i aplikacija je omogućavanje dovoljno jednostavne apstrakcije kako programeri ne bi morali da uče sve o unutrašnjoj logici protokola. Upravo je to cilj **RGBlib**, napisanog u Rust.


RGBlib deluje kao most između veoma fleksibilnih (ali ponekad složenih) zahteva RGB koje smo mogli proučiti u prethodnim poglavljima, i konkretnih potreba programera aplikacija. Drugim rečima, Wallet (ili servis) koji želi da upravlja transferima tokena, izdavanjem sredstava, verifikacijom, itd., može se osloniti na RGBlib bez poznavanja svakog kriptografskog detalja ili svakog prilagodljivog RGB parametra.


Knjižara nudi :




- Funkcije po principu "ključ u ruke" za izdavanje (_issuance_) sredstava (fungibilnih ili ne);
- Sposobnost prenosa (slanje/primanje) sredstava manipulacijom jednostavnim objektima (adrese, iznosi, UTXO-i, itd.);
- Mehanizam za skladištenje i učitavanje informacija o statusu (*pošiljke*) potrebnih za Client-side Validation.


RGBlib se stoga oslanja na složene pojmove specifične za RGB (Client-side Validation, Tapret/Opret sidra), ali ih enkapsulira tako da konačna aplikacija ne mora sve ponovo programirati ili donositi rizične odluke. Štaviše, RGBlib je već povezan na nekoliko jezika (Kotlin i Python), otvarajući vrata za upotrebu izvan jednostavnog Rust univerzuma.


### Iris Wallet: primer RGB Wallet primer na Androidu


Da bi dokazao efikasnost RGBlib-a, tim Bitfinex-a je razvio **Iris Wallet**, ekskluzivno na Android-u u ovoj fazi. To je mobilni Wallet koji ilustruje korisničko iskustvo slično onom običnog Bitcoin Wallet: možete izdati sredstvo, poslati ga, primiti ga i pregledati njegovu istoriju, dok ostajete na modelu samostalnog čuvanja.


Iris ima niz zanimljivih karakteristika:


**Korišćenje Electrum servera:**


Kao i svaki Wallet, Iris treba da zna o potvrđivanju transakcija na Blockchain. Umesto da ugrađuje kompletan čvor, Iris podrazumevano koristi Electrum server koji održava tim Bitfinex-a. Korisnici, međutim, mogu konfigurisati svoj server ili neku drugu uslugu treće strane. Na ovaj način, transakcije Bitcoin mogu biti validirane i informacije preuzete (indeksiranje) na modularan način.


**RGB proxy server:**


Za razliku od Bitcoin, RGB zahteva Exchange od off-chain metapodataka (*pošiljke*) između pošiljaoca i primaoca. Da bi se ovaj proces pojednostavio, Iris nudi rešenje gde komunikacija ide preko proxy servera. Prijemni Wallet generiše *Invoice* koji navodi gde pošiljalac treba da pošalje *klijentske* podatke. Podrazumevano, URL pokazuje na proxy koji hostuje Bitfinex tim, ali možete promeniti ovaj proxy (ili hostovati svoj). Ideja je da se vrati na poznato korisničko iskustvo gde primalac prikazuje QR kod, a pošiljalac skenira ovaj kod za transakciju, bez ikakvih složenih dodatnih manipulacija.


**Kontinuirano bekapovanje:**


U strogo Bitcoin kontekstu, pravljenje rezervne kopije vašeg seed je generalno dovoljno (iako ovih dana preporučujemo pravljenje rezervne kopije seed i deskriptora). Sa RGB, to nije dovoljno: takođe morate čuvati lokalnu istoriju (*pošiljke*) koja dokazuje da zaista posedujete RGB imovinu. Svaki put kada primite račun, uređaj skladišti nove podatke, što je ključno za kasniju potrošnju. Iris automatski upravlja šifrovanom rezervnom kopijom na korisnikovom Google Drive-u. Ovo ne zahteva posebno poverenje u Google, jer je rezervna kopija šifrovana, a planirane su i robusnije opcije (kao što je lični server) kako bi se izbegao bilo kakav rizik od cenzure ili brisanja od strane treće strane.


**Ostale funkcije:**




- Kreirajte Faucet za brzo testiranje ili distribuciju tokena za eksperimentisanje ili promociju;
- Sistem sertifikacije (trenutno centralizovan) za razlikovanje legitimnog tokena od lažnog koji kopira poznati ticker. U budućnosti, ova sertifikacija može postati više decentralizovana (putem DNS-a ili drugih mehanizama).


Sve u svemu, Iris nudi korisničko iskustvo slično onom klasičnog Bitcoin Wallet, prikrivajući dodatnu složenost (upravljanje Stash, *istorija Consignment*, itd.) zahvaljujući RGBlib i korišćenju proxy servera.


### Proxy server i korisničko iskustvo


Proxy server opisan iznad zaslužuje detaljno objašnjenje, jer je ključ za glatko korisničko iskustvo. Umesto da pošiljalac mora ručno da prenosi *pošiljke* primaocu, RGB transakcija se odvija u pozadini putem :




- Primalac generiše *Invoice* (koji sadrži, između ostalog, proxy Address);
- Pošiljalac šalje (putem HTTP zahteva) tranzicioni projekat (*Consignment*) ka proxy-ju;
- Primalac preuzima ovaj projekat, izvršava *klijentsku* validaciju lokalno;
- Primalac zatim objavljuje, putem proxy-a, prihvatanje (ili moguće odbijanje) State Transition ;
- Pošiljalac može videti status validacije i, ako je prihvaćeno, emitovati Bitcoin transakciju završavajući transfer.


Na ovaj način, Wallet se ponaša gotovo kao normalan Wallet. Korisnik nije svestan svih međukoraka. Doduše, trenutni proxy nije ni šifrovan ni autentifikovan (što ostavlja zabrinutost za poverljivost i integritet), ali ova poboljšanja su moguća u kasnijim verzijama. Koncept proxy-ja ostaje izuzetno koristan za ponovno kreiranje iskustva "Šaljem QR kod, ti skeniraš da platiš".


### Integracija RGB na Lightning Network


Još jedan ključni fokus rada tima Bitfinex je da Lightning Network učini kompatibilnim sa RGB asetima. Cilj je omogućiti Lightning kanale u USDT (ili bilo kojem drugom tokenu), i iskoristiti iste prednosti kao Bitcoin na Lightning-u (gotovo trenutne transakcije, rutiranje, itd.). U konkretnim terminima, ovo podrazumeva kreiranje modifikovanog Lightning čvora da:




- Otvorite kanal postavljanjem ne samo satoshija, već i jednog ili više RGB sredstava u finansiranje UTXO Multisig ;
- generate Lightning Commitment transakcije (Bitcoin strana) praćene odgovarajućim RGB prelazima stanja. Svaki put kada se kanal ažurira, RGB prelaz redefiniše raspodelu sredstava u Lightning izlazima;
- Omogući jednostrano zatvaranje, gde se sredstvo preuzima u ekskluzivnom UTXO, u skladu sa pravilima Lightning Network (HTLC, vremensko zaključavanje, kazna, itd.).


Ovo rešenje, nazvano "**RGB Lightning Node**", koristi LDK (*Lightning Dev Kit*) kao osnovu, i dodaje mehanizme potrebne za ubacivanje RGB tokena u kanale. Lightning obaveze zadržavaju klasičnu strukturu (puncturable outputs, timelock...), a dodatno Anchor i RGB State Transition (putem `Opret` ili `Tapret`). Za korisnika, ovo otvara put ka Lightning kanalima u stabilnim kovanicama ili u bilo kojoj drugoj imovini emitovanoj putem RGB.


### Potencijal DEX-a i uticaj na Bitcoin


Jednom kada se nekoliko sredstava upravlja putem Lightning-a, postaje moguće zamisliti **atomski Exchange** na jednoj Lightning ruting putanji, koristeći istu logiku tajni i vremenskih zaključavanja. Na primer, korisnik A drži Bitcoin na jednom Lightning kanalu, a korisnik B drži USDT RGB na drugom Lightning kanalu. Oni mogu izgraditi putanju koja povezuje njihove dve kanale i istovremeno Exchange BTC za USDT, bez potrebe za poverenjem. Ovo nije ništa drugo do **atomska zamena** koja se odvija u nekoliko koraka, čineći spoljne učesnike gotovo nesvesnim činjenice da obavljaju trgovinu, a ne samo rutiranje. Ovaj pristup nudi :




- Veoma niska latencija, jer sve ostaje off-chain na Lightning.
- Superiorna **privatnost**: niko ne zna da je to trgovina, a ne normalno usmeravanje ;
- Izbegavanje frontrunning-a, ponavljajući problem za On-Chain DEX ;
- Smanjeni troškovi (ne plaćate prostor u bloku, samo naknade za rutiranje preko Lightning mreže).


Možemo zamisliti ekosistem u kojem Lightning čvorovi nude cene zamene (pružanjem likvidnosti). Svaki čvor, ako to želi, može igrati ulogu _market makera_, kupujući i prodajući razne asete na Lightning-u. Ova perspektiva _layer-2_ DEX-a pojačava ideju da nije neophodno Fork ili koristiti treće strane blokčejnove za dobijanje decentralizovanih razmena aseta.


Uticaj na Bitcoin mogao bi biti pozitivan: Lightning-ova infrastruktura (čvorovi, kanali i usluge) bila bi u potpunosti iskorišćena zahvaljujući obimima generisanim od strane ovih *stablecoins*, derivata i drugih tokena. Trgovci zainteresovani za USDT plaćanja na Lightning-u bi mehanički otkrili BTC plaćanja na Lightning-u (upravljano od strane istog steka). Održavanje i finansiranje Lightning Network infrastrukture takođe bi moglo imati koristi od umnožavanja ovih ne-BTC tokova, što bi indirektno koristilo korisnicima Bitcoin.


### Zaključak i resursi


Tim Bitfinex posvećen RGB ilustruje, kroz svoj rad, raznolikost onoga što se može uraditi na vrhu protokola. S jedne strane, tu je RGBlib, biblioteka koja olakšava dizajn novčanika i aplikacija. S druge strane, imamo Iris Wallet, praktičnu demonstraciju na Androidu urednog krajnjeg korisnika Interface. Na kraju, integracija RGB sa Lightning-om pokazuje da su kanali sa stabilnim kovanicama mogući, i otvara put ka potencijalnom decentralizovanom DEX-u na Lightning-u.


Ovaj pristup ostaje uglavnom eksperimentalan i nastavlja da se razvija: RGBlib biblioteka se usavršava kako idemo dalje, Iris Wallet redovno dobija unapređenja, a posvećeni Lightning čvor još uvek nije mainstream Lightning klijent.


Za one koji žele da saznaju više ili doprinesu, dostupno je nekoliko resursa, uključujući :




- [GitHub RGB Tools repositories](https://github.com/RGB-Tools);
- [Sajt sa informacijama posvećen Iris Wallet](https://iriswallet.com/) za testiranje Wallet na Androidu.


U sledećem poglavlju, detaljnije ćemo pogledati kako pokrenuti RGB Lightning čvor.


## RLN - RGB Lightning Node


<chapterId>ecaabe32-20ba-5f8c-8ca1-a3f095792958</chapterId>


:::video id=d1e9753e-6093-4a47-bcdc-da1aebaefffc:::


U ovom završnom poglavlju, Frederico Tenga vas vodi korak-po-korak kroz postavljanje Lightning RGB čvora u Regtest okruženju, i pokazuje vam kako kreirati RGB tokene na njemu. Pokretanjem dva odvojena čvora, takođe ćete otkriti kako otvoriti Lightning kanal između njih i Exchange RGB sredstava.


Ovaj video služi kao vodič, slično onome što smo pokrili u prethodnom poglavlju, ali ovaj put je posebno fokusiran na Lightning!


Glavni resurs za ovaj video je Github repozitorijum [RGB Lightning Node](https://github.com/RGB-Tools/RGB-lightning-node), koji vam olakšava pokretanje ove konfiguracije u Regtest-u.


### Implementacija Lightning čvora kompatibilnog sa RGB


Proces preuzima i primenjuje sve koncepte obrađene u prethodnim poglavljima:




- Ideja da **UTXO** blokiran na 2/2 Multisig Lightning kanala može primati ne samo bitkoine, već može biti i Single-Use Seal od RGB sredstava (fungibilnih ili ne);
- Dodavanje, u svakoj Lightning transakciji angažovanja, izlaza (`Tapret` ili `Opret`) posvećenog sidrenju RGB State Transition;
- Povezana infrastruktura (bitcoind/indexer/proxy) za validaciju Bitcoin transakcija i Exchange *klijent-strana* podataka.


### Predstavljamo RGB-lightning-node


Projekat **`RGB-lightning-node`** je Rust daemon zasnovan na `Rust-lightning` (LDK) Fork modifikovan da uzme u obzir postojanje RGB sredstava u kanalu. Kada se kanal otvori, prisustvo sredstava može biti specificirano, i svaki put kada se stanje kanala ažurira, kreira se RGB tranzicija, koja odražava distribuciju sredstava u Lightning izlazima. Ovo omogućava :




- Otvorite Lightning kanale u USDT, na primer;
- Usmerite ove tokene kroz mrežu, pod uslovom da rute imaju dovoljnu likvidnost;
- Iskoristi Lightningovu kaznenu i vremensku logiku bez modifikacije: jednostavno Anchor tranziciju RGB u dodatnom izlazu Commitment Transaction.


Kod je još uvek u alfa fazi: preporučujemo da ga koristite samo u **regtest** ili na **Testnet**.


### Instalacija čvora


Da bismo kompajlirali i instalirali binarni fajl `RGB-lightning-node`, počinjemo kloniranjem repozitorijuma i njegovih podmodula, zatim pokrećemo:


```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```


![RGB-Bitcoin](assets/fr/098.webp)




- Opcija `--recurse-submodules` takođe klonira neophodne pod-uređaje (uključujući modifikovanu verziju `Rust-lightning`);
- Opcija `--shallow-submodules` ograničava dubinu kloniranja kako bi se ubrzalo preuzimanje, dok i dalje omogućava pristup ključnim commit-ovima.


Iz korena projekta, pokrenite sledeću komandu da biste kompajlirali i instalirali binarni fajl:


```bash
cargo install --locked --debug --path .
```


![RGB-Bitcoin](assets/fr/099.webp)




- `--locked` osigurava da se verzija zavisnosti striktno poštuje;
- `--debug` nije obavezan, ali može vam pomoći da se fokusirate (možete koristiti `--release` ako više volite) ;
- `--path .` govori `cargo install` da instalira iz trenutnog direktorijuma.


Na kraju ove komande, izvršni fajl `RGB-lightning-node` će biti dostupan u vašem `$CARGO_HOME/bin/`. Uverite se da je ova putanja u vašem `$PATH` kako biste mogli da pozovete komandu iz bilo kog direktorijuma.


### Zahtevi za performanse


Da bi funkcionisao, `RGB-lightning-node` daemon zahteva prisustvo i konfiguraciju:




- Čvor `bitcoind`**


Svaka RLN instanca će morati komunicirati sa `bitcoind` kako bi emitovala i pratila svoje On-Chain transakcije. Autentifikacija (login/lozinka) i URL (host/port) će morati biti obezbeđeni za daemon.




- Indekser** (Electrum ili Esplora)


daemon mora biti u mogućnosti da navede i istraži On-Chain transakcije, posebno da pronađe UTXO na kojem je sredstvo usidreno. Moraćete da navedete URL vašeg Electrum servera ili Esplora.




- An RGB** proxy


Kao što je viđeno u prethodnim poglavljima, **proxy server** je komponenta (opcionalna, ali visoko preporučena) za pojednostavljenje Exchange *pošiljki* između Lightning vršnjaka. Još jednom, URL mora biti specificiran.


ID-ovi i URL-ovi se unose kada je daemon _otključan_ putem API-ja. Više o tome kasnije.


### Pokretanje regtesta


Za jednostavnu upotrebu, postoji skripta `regtest.sh` koja automatski pokreće, putem Dockera, skup servisa: `bitcoind`, `electrs` (indekser), `RGB-proxy-server`.


![RGB-Bitcoin](assets/fr/100.webp)


Ovo vam omogućava pokretanje lokalnog, izolovanog, unapred konfigurisanog okruženja. Kreira i uništava kontejnere i direktorijume podataka pri svakom ponovnom pokretanju. Počećemo pokretanjem :


```bash
./regtest.sh start
```


Ovaj skript će :




- Kreirajte direktorijum `docker/` za čuvanje ;
- Pokreni `bitcoind` u regtest modu, kao i indeksator `electrs` i `RGB-proxy-server` ;
- Sačekajte dok sve ne bude spremno za korišćenje.


![RGB-Bitcoin](assets/fr/101.webp)


Zatim ćemo pokrenuti nekoliko RLN čvorova. U posebnim terminalima pokrenite, na primer (za pokretanje 3 RLN čvora) :


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


![RGB-Bitcoin](assets/fr/102.webp)




- Parametar `--network regtest` označava upotrebu regtest konfiguracije;
- `--daemon-listening-port` označava na kojem REST portu će Lightning čvor slušati za API pozive (JSON);
- `--ldk-peer-listening-port` određuje koji Lightning P2P port će se slušati;
- `dataldk0/`, `dataldk1/` su putanje do direktorijuma za skladištenje (svaki čvor čuva svoje informacije zasebno).


Takođe možete pokretati komande na vašim RLN čvorovima iz vašeg pregledača:


```url
https://rgb-tools.github.io/rgb-lightning-node/
```


Da bi čvor otvorio kanal, prvo mora imati bitkoine na Address generisane sledećom komandom (za čvor br. 1, na primer):


```bash
curl -X POST http://localhost:3001/address
```


Odgovor će vam pružiti Address.


![RGB-Bitcoin](assets/fr/103.webp)


Na `bitcoind` Regtestu, kopaćemo nekoliko bitkoina. Pokreni :


```bash
./regtest.sh mine 101
```


![RGB-Bitcoin](assets/fr/104.webp)


Pošalji sredstva na čvor Address generisan iznad:


```bash
./regtest.sh sendtoaddress <address> <amount>
```


![RGB-Bitcoin](assets/fr/105.webp)


Zatim iskopaj blok da potvrdiš transakciju:


```bash
./regtest.sh mine 1
```


![RGB-Bitcoin](assets/fr/106.webp)


### Testnet lansiranje (bez Dockera)


Ako želite testirati realističniji scenario, možete pokrenuti 3 RLN čvora na Testnet umesto u Regtestu, usmeravajući ka javnim servisima :


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


### Izdavanje RGB tokena


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


![RGB-Bitcoin](assets/fr/107.webp)


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


![RGB-Bitcoin](assets/fr/108.webp)


Odgovor uključuje ID novokreirane imovine. Zapamtite da zabeležite ovaj identifikator. U mom slučaju, to je:


```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```


![RGB-Bitcoin](assets/fr/109.webp)


Zatim ga možete preneti na On-Chain ili ga dodeliti u Lightning kanal. Upravo to ćemo uraditi u sledećem odeljku.


### Otvaranje kanala i prenos RGB sredstva


Prvo morate povezati svoj čvor sa peer-om na Lightning Network koristeći komandu `/connectpeer`. U mom primeru, kontrolišem oba čvora. Tako da ću preuzeti javni ključ mog drugog Lightning čvora pomoću ove komande:


```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```


Komanda vraća javni ključ mog čvora br. 2 :


```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```


![RGB-Bitcoin](assets/fr/110.webp)


Dalje, otvorićemo kanal specificiranjem relevantne imovine (`PBN`). Komanda `/openchannel` vam omogućava da definišete veličinu kanala u satoshijima i odlučite da uključite RGB imovinu. Zavisi od toga šta želite da kreirate, ali u mom slučaju, komanda je :


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
- `push_msat`: Iznos u milisatošima koji se inicijalno prenosi vršnjaku kada se kanal otvori (ovde odmah prenosim 10,000 Sats kako bi on mogao kasnije da izvrši RGB transfer) ;
- `asset_amount`: Iznos RGB sredstava koji će biti posvećen kanalu ;
- `asset_id` : Jedinstveni identifikator RGB sredstva uključenog u kanal;
- `public`: Označava da li kanal treba da bude javan za rutiranje na mreži.


![RGB-Bitcoin](assets/fr/111.webp)


Da bi se transakcija potvrdila, 6 blokova se rudari:


```bash
./regtest.sh mine 6
```


![RGB-Bitcoin](assets/fr/112.webp)


Lightning kanal je sada otvoren i takođe sadrži 500 `PBN` tokena na strani čvora n°1. Ako čvor n°2 želi da primi `PBN` tokene, mora generate i Invoice. Evo kako to uraditi:


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
- `expiry_sec` : Invoice vreme isteka u sekundama ;
- `asset_id` : Identifikator RGB sredstva povezanog sa Invoice ;
- `asset_amount`: Iznos RGB sredstva koje treba preneti sa ovim Invoice.


Kao odgovor, dobićete RGB Invoice (kao što je opisano u prethodnim poglavljima):


```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```


![RGB-Bitcoin](assets/fr/113.webp)


Sada ćemo platiti ovaj Invoice sa prvog čvora, koji drži potreban novac sa `PBN` tokenom:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```


![RGB-Bitcoin](assets/fr/114.webp)


Plaćanje je izvršeno. Ovo se može proveriti izvršavanjem komande :


```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```


![RGB-Bitcoin](assets/fr/115.webp)


Evo kako da implementirate Lightning čvor modifikovan za prenos RGB sredstava. Ova demonstracija se zasniva na :




- A regtest environment (via `./regtest.sh`) or Testnet ;
- Čvor za Lightning mrežu (`RGB-lightning-node`) zasnovan na `bitcoind`, indeksator i `RGB-proxy-server` ;
- Serija JSON REST API-ja za otvaranje/zatvaranje kanala, izdavanje tokena, prenos sredstava putem Lightning-a, itd.


Zahvaljujući ovom procesu :




- Lightning engagement transakcije uključuju dodatni izlaz (OP_RETURN ili Taproot) sa sidrenjem RGB tranzicije;
- Transferi se obavljaju na potpuno isti način kao tradicionalna Lightning plaćanja, ali uz dodatak RGB tokena;
- Više RLN čvorova može biti povezano za usmeravanje i eksperimentisanje sa plaćanjima preko više čvorova, pod uslovom da postoji dovoljna likvidnost u bitkoinima i sredstvu RGB na putu.


Projekat ostaje u alfa fazi. Stoga se snažno preporučuje da se ograničite na test okruženja (regtest, Testnet).


Mogućnosti koje otvara ova kompatibilnost LN-RGB su značajne: stablecoins na Lightning-u, DEX Layer-2, transfer fungibilnih tokena ili NFT-ova po vrlo niskoj ceni... Prethodna poglavlja su opisala konceptualnu arhitekturu i logiku validacije. Sada imate praktičan pregled kako pokrenuti takav čvor, za vaše buduće razvojne projekte ili testove.


# Završni Deo


<partId>b0baebfc-d146-5938-849a-f835fafb386f</partId>


## Recenzije i ocene


<chapterId>0217e8b0-942a-5fee-bd91-9a866551eff3</chapterId>


<isCourseReview>true</isCourseReview>

## Zaključak


<chapterId>0309536d-c336-56a0-869e-a8395ed8d9ae</chapterId>


<isCourseConclusion>true</isCourseConclusion>