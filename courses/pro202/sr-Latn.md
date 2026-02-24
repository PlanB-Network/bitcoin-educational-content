---
name: Programiranje Bitcoin
goal: Izgradite kompletnu Bitcoin biblioteku od nule i razumite kriptografske osnove Bitcoin
objectives: 

 - Implementirajte aritmetiku konačnih polja i operacije eliptičkih krivih u Pythonu
 - Kreirajte i parsirajte Bitcoin transakcije programatski
 - Kreirajte testnet adrese i emitujte transakcije preko mreže.
 - Savladajte matematičke osnove koje leže u osnovi Bitcoin sigurnosnog modela

---
# Putovanje u skripte i programe Bitcoin


Ovaj intenzivni dvodnevni kurs, koji vodi Jimmy Song, vodi vas duboko u tehničke osnove Bitcoin izgradnjom kompletne Bitcoin biblioteke od nule. Počevši od osnovne matematike konačnih polja i eliptičkih krivih, napredovaćete kroz parsiranje transakcija, izvršavanje skripti i mrežnu komunikaciju. Kroz praktične vežbe kodiranja u Jupyter beležnicama, kreiraćete svoju testnet adresu, ručno konstruisati transakcije i emitovati ih direktno na mrežu—sve to dok stičete duboko razumevanje kriptografskih principa koji čine Bitcoin sigurnim i bez poverenja.


Uživaj u putovanju!


+++

# Uvod


<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>


## Pregled kursa


<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>


Dobrodošli na kurs PRO 202 _**Programming Bitcoin**_, intenzivno putovanje koje vas vodi od aritmetike konačnih polja sve do izgradnje i emitovanja pravih transakcija na Bitcoin-ovom Testnet.


Na ovom kursu, postepeno ćete izgraditi Bitcoin biblioteku u Python-u dok stičete kriptografske, protokolarne i softverske osnove neophodne za precizno razumevanje sigurnosti i unutrašnjeg funkcionisanja Bitcoin. PRO 202 pristup je potpuno praktičan: svaki koncept se odmah implementira u Jupyter beležnicama, osiguravajući da teorija i kod međusobno jačaju.


### Osnovni Matematički Koncepti za Bitcoin


Ovaj prvi deo postavlja neophodne matematičke osnove. Implementiraćete aritmetiku konačnih polja i operacije na eliptičkim krivama (zakon grupe, sabiranje, udvostručavanje, skalarno množenje...) — preduslove za ECDSA. Cilj je dvostruk: razumeti algebarsku strukturu koja omogućava kriptografske potpise i izgraditi pouzdane Python alate za njihovu manipulaciju.


Zatim ćete formalizovati komponente ECDSA: generisanje ključeva, formatiranje tačaka, heširanje, kreiranje potpisa i verifikaciju. Ovaj deo direktno povezuje teoriju sa praksom, naglašavajući detalje implementacije i robusnost osnovnog bezbednosnog modela.


### Bitcoin Transakcija Unutrašnji Radovi


U drugom delu, analiziraćete strukturu Bitcoin transakcije: UTXO-e, ulaze/izlaze, sekvence, skripte, kodiranja i više. Napisaćete kod za konstruisanje, potpisivanje i verifikaciju transakcija, stičući precizno razumevanje onoga što je potvrđeno hešom i zašto.


Dalje, implementiraćete minimalni izvršilac _Script_-a, pregledati ključne opkodove i validirati puteve trošenja. Cilj je da budete sposobni da proveravate ponašanje transakcija, dijagnostikujete neuspehe validacije i razmišljate o bezbednosti politika trošenja.


### Bitcoin Mreža Unutrašnji Rad


U trećem delu, postavićete transakcije unutar šireg sistema: struktura blokova, zaglavlja, težina i Proof-of-Work mehanizam. Rukovaćete porukama protokola, zaglavljima blokova i Merkle stablima.


Konačno, proučavaćete komunikaciju između peer-to-peer čvorova, optimizaciju poruka i uvođenje SegWit.


Kao i kod svakog kursa na Plan ₿ Academy, završni deo uključuje evaluaciju osmišljenu da konsoliduje vaše razumevanje. Spremni da otkrijete unutrašnje funkcionisanje Bitcoin i napišete kod koji ga pokreće? Hajde da počnemo!










# Osnovni matematički koncepti za Bitcoin

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Matematika za Bitcoin Implementaciju

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>


![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


### Bitcoin Osnove programiranja: Osnovne matematičke strukture


Ovaj kurs kondenzuje suštinsku matematiku iza kriptografskih sistema Bitcoin u visoko praktičan tok rada. Koncepti su objašnjeni, demonstrirani primerima, a zatim implementirani u Jupyter Notebook. Vodeća ideja je jednostavna: zaista razumete kriptografski primitiv tek kada ga kodirate. Tokom dvodnevne strukture, studenti koriste generate testnet adrese, kreiraju i emituju [transakcije](https://planb.academy/resources/glossary/transaction-tx), i na kraju komuniciraju sa mrežom bez blok eksplorera. Sve ovo zahteva čvrstu osnovu u konačnim poljima i eliptičkim krivama.


### Konačna Polja: Aritmetički Pogon Kriptografije


Konačno polje F(p) je aritmetički sistem definisan prostim brojem p, koji sadrži elemente od 0 do p–1. Prosta polja osiguravaju da svaki nenulti element ima inverz i da sve operacije ostaju unutar polja. Aritmetika se obavlja koristeći modulo p za sabiranje, oduzimanje i množenje. Pythonova funkcija `pow(base, exp, mod)` omogućava efikasno modularno potenciranje, što je ključno za velike eksponente korišćene u stvarnim kriptografskim operacijama.


#### Multiplikativno Ponašanje

Množenje bilo kog nenultog elementa k sa svim elementima prostog polja proizvodi permutaciju polja. Ovo svojstvo garantuje uniformnost i sprečava strukturne slabosti, čineći prosta polja idealnim za sigurno generisanje ključeva i [digitalne potpise](https://planb.academy/resources/glossary/digital-signature).


#### Deljenje i Fermatova mala teorema

Deljenje se sprovodi putem multiplikativnih inverza. Mali Fermatov teorem kaže da

n^(p–1) ≡ 1 (mod p),

tako da je inverz n^(p–2). Python to direktno podržava sa `pow(n, -1, p)`. Ove operacije se stalno pojavljuju u [ECDSA](https://planb.academy/resources/glossary/ecdsa) i osnovnim kriptografskim rutinama Bitcoin.


### Eliptičke Krive: Nelinearne Strukture za Javni-Ključ Sigurnost


Eliptičke krive prate jednačinu y² = x³ + ax + b. Bitcoin koristi secp256k1, definisanu kao y² = x³ + 7 nad konačnim poljem. Tačke na eliptičkoj krivoj formiraju matematičku grupu pod sabiranjem tačaka. Prava povučena kroz dve tačke P i Q seče krivu u trećoj tački R; refleksija R preko x-ose daje P + Q. Ovaj sistem je asocijativan i uključuje identitetni element: tačku u beskonačnosti.


Udvostručavanje tačke koristi tangentnu liniju umesto sekantne linije, sa nagibom izvedenim iz izvoda krive. Iako ove formule uključuju računanje preko realnih brojeva, one postaju potpuno diskretne i tačne kada je kriva definisana nad konačnim poljem—kontekst korišćen u Bitcoin.


### Od matematike do Bitcoin kriptografije


Konačna polja pružaju determinističku, invertibilnu aritmetiku; eliptičke krive pružaju nelinearnu strukturu gde je lako izračunati k·P, ali je obrnuti proces računski neizvodljiv. Kombinovanjem oba dobija se osnova za javne/privatne ključeve Bitcoin, ECDSA potpise i sigurnost transakcija. Razumevanje ovih osnova priprema studente da direktno implementiraju ključeve, transakcije i potpise—bez apstrakcija ili eksternih alata.


## Kriptografija eliptičkih krivih

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>


![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


Ovo poglavlje uvodi eliptičke krive definisane nad konačnim poljima i objašnjava zašto one čine matematičku osnovu [kriptografije](https://planb.academy/resources/glossary/cryptography) Bitcoin. Dok eliptičke krive nad realnim brojevima izgledaju glatko i kontinuirano, primena istih jednačina nad konačnim poljem stvara diskretnu, rasutu skupinu tačaka. Uprkos vizuelnoj razlici, sve formule za sabiranje tačaka, nagibi i algebarska pravila ponašaju se potpuno isto—samo se aritmetika menja u modularnu aritmetiku. Bitcoin koristi krivu y² = x³ + 7 (secp256k1), koja čuva simetriju i nelinearno ponašanje neophodno za kriptografsku sigurnost.


### Verifying Points and Finite Field Implementation


Tačka leži na eliptičnoj krivoj nad konačnim poljem ako njene koordinate zadovoljavaju jednačinu krive pod mod p. Provera tačke kao što je (73,128) na F₁₃₇ zahteva proveru da y² mod p jednako je x³ + 7 mod p. Implementacija ovoga u kodu uključuje kreiranje klasa za elemente konačnog polja i tačke krive. Preopterećenje operatora osigurava da se sva aritmetika—sabiranje, množenje, eksponenciranje, deljenje—automatski izvodi mod p. Kada ove apstrakcije postoje, naprednije kriptografske operacije postaju jednostavne za pisanje i razumevanje.


#### Svojstva grupe i sabiranje tačaka

Tačke eliptičke krive formiraju matematičku grupu pod operacijom sabiranja. Grupa zadovoljava zatvorenost, asocijativnost, identitet (tačka u beskonačnosti) i inverze (refleksija preko x-ose). Geometrijske konstrukcije potvrđuju ova svojstva, čineći skalarno množenje (P dodato samom sebi više puta) dobro definisanim. Ova grupna pravila omogućavaju eliptičku krivuljnu kriptografiju i osiguravaju konzistentno, predvidljivo ponašanje pod ponovljenim operacijama tačaka.


### Ciklične Grupe i Problem Diskretnog Logaritma


Odabir generatora tačke G na krivoj omogućava nam da generate cikličku grupu: G, 2G, 3G, …, nG = 0. Tačke se pojavljuju nelinearno i nepredvidivo, čak i kada se generišu sekvencijalno. Ova nepredvidivost stvara osnovu za problem diskretnog logaritma: izračunavanje P = sG je lako, ali određivanje s iz P je računarski neizvodljivo za velike grupe. Ova jednosmerna funkcija je ono što čini javni ključ kriptografije sigurnim. Skalari ([privatni ključevi](https://planb.academy/resources/glossary/private-key)) se pišu malim slovima; tačke ([javni ključevi](https://planb.academy/resources/glossary/public-key)) velikim slovima.


#### Efikasna Skalarna Množenja

Da bi se sG efikasno izračunao, implementacije koriste algoritam dupliranja i dodavanja: skeniranje binarne reprezentacije skalara, dupliranje tačke pri svakom koraku i dodavanje G samo kada je bit 1. Ovo smanjuje računanje sa O(n) sabiranja na O(log n), omogućavajući praktične kriptografske operacije čak i sa skalarima od 256 bita.


#### Kriva secp256k1 u Bitcoin


Bitcoin koristi krivu secp256k1, definisanu kao y² = x³ + 7 nad prostim poljem gde je p = 2²⁵⁶ − 2³² − 977. Generator tačka G ima fiksirane koordinate izabrane korišćenjem determinističke NUMS (“nothing up my sleeve”) procedure. Red grupe n je veliki prost broj blizu 2²⁵⁶, što osigurava da svaka nenulta tačka generiše istu grupu. Veličina 2²⁵⁶ (~10⁷⁷) je astronomski velika, što čini brute‑force napade na privatne ključeve fizički nemogućim. Čak ni trilion superkompjutera koji rade trilion godina ne bi značajno smanjili prostor ključeva.


### Javni ključevi, privatni ključevi i SEC serijalizacija


Privatni ključ je nasumičan skalar s; javni ključ je P = sG. Pošto je rešavanje problema diskretnog logaritma neizvodljivo, P se može deliti bez otkrivanja s. Javni ključevi moraju biti serijalizovani za prenos koristeći SEC format. Nekomprimovani SEC format koristi 65 bajtova: prefiks 0x04 + x‑koordinata + y‑koordinata. Komprimovani format koristi samo 33 bajta: prefiks 0x02 ili 0x03 (u zavisnosti od pariteta y) + x‑koordinata. Bitcoin je prvobitno koristio nekomprimovane ključeve, ali sada preferira komprimovane zbog efikasnosti.


#### Bitcoin Address Kreacija


Bitcoin adrese su heševi javnih ključeva, a ne sami sirovi ključevi. Da biste generate adresu, serijalizujte javni ključ u SEC formatu, izračunajte hash160 (SHA‑256 zatim RIPEMD‑160), dodajte prefiks mreže (0x00 za mainnet, 0x6F za testnet), izračunajte kontrolni zbir koristeći dvostruki SHA‑256, dodajte prva četiri bajta kontrolnog zbira i kodirajte rezultat koristeći Base58. Ovo kodiranje uklanja dvosmislene karaktere i uključuje kontrolni zbir kako bi se sprečile greške pri prepisivanju. Višestepeni proces skriva javni ključ dok se ne izvrši trošenje, dodaje identifikaciju mreže i osigurava adrese koje su čitljive za ljude i otporne na greške.


# Bitcoin Transakcija Unutrašnji Mehanizmi

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin Parsiranje Transakcija i ECDSA Potpisi

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>


![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


### Razumevanje ECDSA: Osnova digitalnog potpisa Bitcoin


Bitcoin se oslanja na ECDSA, šemu potpisa zasnovanu na eliptičnim krivama koja nudi snažnu sigurnost uz znatno manje veličine ključeva nego RSA. Njena sigurnost dolazi iz problema diskretnog logaritma eliptične krive: dato P = eG, računanje P je lako, ali izvođenje e iz P je računski neizvodljivo. Ova asimetrija omogućava kriptografiju javnog ključa dok privatni ključevi ostaju sigurni.


#### DER Kodiranje ECDSA Potpisa


Bitcoin kodira ECDSA potpise koristeći DER format:


- 0x30 (sekvencijalni marker)
- dužina bajta
- 0x02 + length + R bajtova
- 0x02 + length + S bajtova


Ovo dodaje dodatni teret, proširujući potpis od 64 bajta na ~71–72 bajta. [Taproot](https://planb.academy/resources/glossary/taproot) eliminiše ovu neefikasnost usvajanjem [Schnorr](https://planb.academy/resources/glossary/schnorr-protocol) potpisa fiksne veličine.


### Potpisivanje obaveza i proces potpisivanja


ECDSA potpisi se oslanjaju na jednačinu posvećenja: UG + VP = KG. Potpisnik bira nenulte vrednosti U i V, i nasumični [nonce](https://planb.academy/resources/glossary/nonce) K, dokazujeći poznavanje privatnog ključa bez njegovog otkrivanja. Poruka se hešira u Z, generiše se nasumični K, R je x‑koordinata KG, i S = (Z + RE)/K. Potpis je par (R, S). Bezbednost kritično zavisi od korišćenja jedinstvenog, nepredvidivog K—ako se K ponovo koristi ili procuri, privatni ključ je ugrožen. Moderne implementacije koriste determinističko generisanje K (RFC 6979) kako bi izbegle neuspehe RNG-a.


#### Verifikacija potpisa

Dat Z, (R, S), i javni ključ P, verifikator izračunava U = Z/S i V = R/S, zatim proverava da li x‑koordinata UG + VP odgovara R. Ovo funkcioniše jer verifikaciona algebra rekonstruiše KG bez potrebe za privatnim ključem. Falsifikovanje potpisa bi zahtevalo rešavanje problema diskretnog logaritma ili razbijanje heš funkcije.


#### Schnorr potpisi i istorijski kontekst


Schnorr potpisi su matematički čistiji i podržavaju funkcije agregacije, ali su bili patentirani kada je Bitcoin lansiran. ECDSA je ponudio besplatnu alternativu, iako sa više složenosti i većim potpisima. Sa isteklim patentima, Bitcoin je dodao Schnorr potpise putem Taproot, pružajući fiksne potpise od 64 bajta i poboljšanu privatnost. ECDSA ostaje podržan radi kompatibilnosti sa starijim verzijama.



### Struktura transakcije i Ulazi/Izlazi


Transakcija Bitcoin se sastoji od:


- verzija (4 bajta, malo‑endian)
- lista ulaza
- lista izlaza
- locktime (4 bajta)


Ulazi referenciraju prethodne [UTXO](https://planb.academy/resources/glossary/utxo)-e po njihovom hešu transakcije i indeksu izlaza, i uključuju skriptu za otključavanje (scriptSig) i redni broj koji se koristi za vremenske brave ili RBF. Izlazi specificiraju iznos (8 bajtova) i skriptu za zaključavanje (scriptPubKey), definišući uslove trošenja. Bitcoin adrese su reprezentacije ovih skripti.


#### Model UTXO

Bitcoin prati neiskorišćene izlaze umesto stanja na računima. UTXO-i moraju biti potpuno potrošeni—delimično trošenje je nemoguće. Da bi se potrošio 1 BTC od 100 BTC UTXO, transakcija mora uključivati izlaz za kusur. Zaboravljanje izlaza za kusur pretvara ostatak u naknadu za rudare.


#### Serijalizacija i Parsiranje Transakcija


Transakcije koriste kompaktni binarni format. Nakon polja verzije, varint kodira broj ulaza. Ulazi uključuju:


- prethodni tx hash (32 bajta)
- izlazni indeks (4 bajta)
- scriptSig (varstr)
- sekvenca (4 bajta)


Izlazi uključuju iznos od 8 bajtova i scriptPubKey (varstr). Locktime kontroliše kada transakcija postaje važeća. Serijalizacija koristi little‑endian redosled za većinu celih brojeva. Parseri troše bajtove sekvencijalno i delegiraju specijalizovanim klasama za ulaze, izlaze i [skripte](https://planb.academy/resources/glossary/script).


### Naknade, Promene i Savitljivost


Naknade su implicitne:

naknada = zbir(ulazne vrednosti) – zbir(izlazne vrednosti).

Bilo koja nedodeljena vrednost postaje naknada, što čini pravilnu konstrukciju izlaza kusura ključnom. Pre [SegWit](https://planb.academy/resources/glossary/segwit), potpisi su dozvoljavali promenljivost—modifikovanje S u N-S proizvodilo je novu važeću transakciju sa drugačijim ID-jem. Bitcoin sada sprovodi pravilo niskog‑S, a SegWit izoluje potpise iz txid proračuna, čineći ID-jeve stabilnim i omogućavajući protokole drugog sloja poput [Lightning](https://planb.academy/resources/glossary/lightning-network)-a.


## Bitcoin Skripta i Validacija Transakcija

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>


![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


Bitcoin Script je mali, stek-bazirani jezik za pametne ugovore koji definiše kako se novčići mogu trošiti. Svaki izlaz nosi scriptPubKey (zaključavajući skript) i svaki ulaz nosi scriptSig (otključavajući skript). Zajedno formiraju program koji mora evaluirati kao „tačno“ da bi trošak bio važeći. Skript je namerno ne-Tjuring-potpun kako bi svi putevi izvršenja bili predvidljivi i laki za validaciju preko mreže.


### Operacije skripti i model izvršavanja


Skripta je sekvenca podataka i opkoda. Podaci (potpisi, javni ključevi, heševi) se postavljaju na stek, dok opkodi koji počinju sa `OP_` transformišu stek. Nakon izvršenja, gornji element steka mora biti različit od nule za uspeh. Primeri: `OP_DUP` duplira gornji element, `OP_HASH160` primenjuje SHA256 pa RIPEMD160, a `OP_CHECKSIG` verifikuje potpis u odnosu na heš transakcije i javni ključ, postavljajući 1 za validan, 0 za nevalidan. Pravila parsiranja razlikuju sirove podatke (sa prefiksom dužine) i opkode (koji se traže po vrednosti bajta), a mala virtuelna mašina ih deterministički izvršava na svakom [čvoru](https://planb.academy/resources/glossary/node).


### P2PK i P2PKH: Osnovni obrasci plaćanja


Najraniji obrazac, Pay-to-Public-Key (P2PK), zaključavao je novčiće direktno na puni javni ključ: scriptPubKey je `<pubkey> OP_CHECKSIG`, a scriptSig je samo potpis. Jednostavan je, ali neefikasan u pogledu prostora i izlaže javni ključ pre nego što su novčići potrošeni.


#### P2PKH i Adrese

Pay-to-Public-Key-Hash (P2PKH) poboljšava ovo zaključavanjem na 20‑bajtni heš javnog ključa. scriptPubKey je `OP_DUP OP_HASH160 <pubkey_hash> OP_EQUALVERIFY OP_CHECKSIG`, a scriptSig obezbeđuje `<signature> <pubkey>`. Izvršenje proverava da li dati javni ključ hešira na posvećenu vrednost i zatim verifikuje potpis. Ovo skriva javni ključ do trenutka trošenja, smanjuje veličinu i odgovara poznatom formatu adrese “1…” mainnet.


### Validacija transakcije i heširanje potpisa


Čvor koji validira transakciju mora osigurati:

1) Svaki ulaz se odnosi na postojeći, neutrošeni izlaz.

2) Ukupna ulazna vrednost ≥ ukupna izlazna vrednost (razlika je naknada).

3) Svaki scriptSig ispravno otključava svoj referencirani scriptPubKey.


Verifikacija potpisa zahteva konstruisanje tačne poruke koja je potpisana, nazvane sighash. Za nasleđeni ECDSA, validacija prazni sve scriptSig-ove, zamenjuje scriptSig trenutnog ulaza odgovarajućim scriptPubKey-em, dodaje 4‑bajtni tip heša (obično `SIGHASH_ALL`), i dvostruko hešira rezultat. Ta 256‑bitna vrednost je ono što koristi `OP_CHECKSIG`. Alternativni tipovi heša (npr. `SINGLE`, `NONE`, sa ili bez `ANYONECANPAY`) menjaju koje delove transakcije se obavezuju, omogućavajući specifične slučajeve upotrebe kao što su kolaborativno finansiranje ili delimično specificirane transakcije, ali se retko koriste u praksi.


#### Kvadratno heširanje i SegWit

Zato što svaki unos u nasleđenoj transakciji zahteva sopstvenu sighash računicu preko strukture koja uključuje sve unose, vreme validacije može rasti kvadratno sa brojem unosa. Velike transakcije sa više unosa su nekada izazivale primetne kašnjenja u validaciji. SegWit je redizajnirao sighash računanje da kešira delove koji se dele i smanji složenost na linearno vreme, poboljšavajući skalabilnost i otežavajući napade uskraćivanjem usluge.


### Skripte Zagonetke i Lekcije o Bezbednosti


Skripta može izraziti mnogo više od jednostavnog „jedan potpis otključava ove novčiće.” Skriptni zagonetke to pokazuju enkodiranjem proizvoljnih uslova—matematičkih problema, izazova preimage heša, ili čak nagrada za koliziju—gde svako ko pruži tačne podatke može potrošiti novčiće. Međutim, izlazi koji se oslanjaju samo na javne podatke (bez potpisa) su ranjivi na pretrčavanje [rudara](https://planb.academy/resources/glossary/miner): kada se validno rešenje pojavi u [mempool-u](https://planb.academy/resources/glossary/mempool), bilo koji rudar može ga kopirati i preusmeriti isplatu sebi.


Praktična lekcija je da ugovori u stvarnom svetu gotovo uvek uključuju provere potpisa, čak i kada sadrže složeniju logiku kao što su multisig, vremenske brave ili hashlocks. Potpisi vezuju rešenje za određenu stranu, čuvajući podsticaje i sprečavajući druge da ukradu isplatu. Razumevanje Script-ovog modela steka, standardnih obrazaca i suptilnih zamki je ključno za dizajniranje sigurnih Bitcoin pametnih ugovora i za razumevanje kako se transakcije zapravo validiraju na mreži.


## Izgradnja Transakcije i Plaćanje na Skriptu Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>


![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


### Izgradnja Bitcoin Transakcije i P2SH


Konstrukcija transakcije Bitcoin povezuje teoretsko znanje o protokolu sa praktičnom primenom. Transakcija bira UTXO-ove za trošenje, kreira izlaze sa skriptama za zaključavanje, stvara potpise za svaki ulaz i serijalizuje sve u tačnom formatu koji čvorovi očekuju. Proces zahteva razumevanje generisanja sighash-a, ponašanja Skripta i pravilno rukovanje naknadama i kusurom.


### Osnovna konstrukcija transakcije


Svaka ulazna transakcija referencira prethodni izlaz putem txid i indeksa. Izlazi specificiraju iznose u satoshijima i skripte za zaključavanje. Razlika između ukupnih ulaza i ukupnih izlaza je naknada. Da bi se potpisao ulaz, modifikovana verzija transakcije se serijalizuje, izračunava se njen sighash, a privatni ključ je potpisuje. Rezultujući potpis i javni ključ formiraju ScriptSig. Kada su svi ulazi potpisani, sirova transakcija može biti emitovana na mrežu.


### Transakcije sa višestrukim potpisom


Bare multisig koristi `OP_CHECKMULTISIG` da zahteva m-of-n potpisa. Zbog ranog baga sa pomeranjem za jedan, OP_CHECKMULTISIG troši dodatni element steka, zahtevajući početni `OP_0` u ScriptSig. Bare multisig je funkcionalan, ali neefikasan: svi javni ključevi se pojavljuju on-chain, čineći scriptPubKeys velikim, skupim i teškim za kodiranje kao adrese. Ova ograničenja su motivisala uvođenje plaćanja na heš skripte (pay-to-script-hash).


#### P2SH Arhitektura

P2SH skriva složene skripte iza 20-bajtne HASH160. scriptPubKey je fiksiran: `OP_HASH160 <20-byte hash> OP_EQUAL`. Osnovna redeem skripta—koja sadrži multisig, vremenske brave ili druge uslove—otkriva se i izvršava samo prilikom trošenja. Pošiljalac vidi samo hash, dok primalac privatno upravlja redeem skriptom. Ovaj dizajn smanjuje veličinu on-chain, poboljšava privatnost i omogućava složene ugovore bez opterećenja pošiljalaca.


### P2SH Trošenje i Implementacija


Da biste potrošili P2SH izlaz, ScriptSig mora uključivati neophodne podatke za otključavanje *plus* sam otkupni skript. Validacija se odvija u dva koraka:

1) HASH160(redeem_script) mora odgovarati hash-u scriptPubKey.

2) Nakon verifikacije, skripta za otkup se izvršava sa dostavljenim podacima.


Kada generišete potpise za P2SH unos, sighash proces koristi redeem skriptu umesto scriptPubKey. Svaki potpisnik mora posedovati kompletnu redeem skriptu za generate validne potpise. P2SH adrese koriste verzioni bajt 0x05 na mainnet (“3…” adrese) i 0xC4 na testnetu (“2…” adrese).


#### Praktična razmatranja bezbednosti


Gubitak otkupnog skripta znači gubitak sredstava: trošenje zahteva i privatne ključeve i sam otkupni skript. Učesnici Multisig moraju proveriti da li su njihovi javni ključevi ispravno uključeni pre nego što prihvate depozite. P2SH podržava napredne konstrukcije kao što su multisig, vremenska zaključavanja i hash zaključavanja, ali greške u logici skripta mogu trajno zaključati sredstva, pa je testiranje na testnet-u neophodno.


P2SH poboljšava privatnost skrivanjem uslova potrošnje do prve potrošnje, ali kada se pojavi otkupni skript on-chain, postaje trajno vidljiv. Uprkos tome, prednosti smanjenja veličine, unazadne kompatibilnosti i podrške za fleksibilne ugovore učinile su P2SH značajnom prekretnicom, utičući na kasnije nadogradnje kao što su SegWit i Taproot.


# Bitcoin Mreža Unutrašnji Radovi

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Bitcoin Blokovi i Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>


![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


Bitcoin blokira grupne transakcije i osigurava ih koristeći [proof of work](https://planb.academy/resources/glossary/proof-of-work). Svaki blok uključuje [zaglavlje](https://planb.academy/resources/glossary/block-header) od 80 bajtova plus listu transakcija. Uprkos velikoj energetskoj ceni proizvodnje važećeg bloka, verifikacija jednog je jeftina: skladištenje svih ~900k zaglavlja zahteva samo ~72 MB, omogućavajući čak i malim uređajima da efikasno verifikuju lanac proof of work.


### Transakcije na Coinbase-u i Nagrade za Blok


Svaki blok počinje sa tačno jednom [Coinbase transakcijom](https://planb.academy/resources/glossary/coinbase-transaction)—jedini način na koji novi bitkoin ulazi u cirkulaciju. Ima nulirani prev-tx hash i indeks od 0xffffffff, što ga jedinstveno identifikuje. Subvencija je počela sa 50 BTC i prepolovljava se na svakih 210,000 [blokova](https://planb.academy/resources/glossary/block) (50, 25, 12.5, 6.25, 3.125, …). Rudari takođe uključuju naknade za transakcije. Pošto je 4-bajtni nonce premali za moderne ASIC-ove, rudari menjaju podatke u Coinbase transakciji kako bi promenili [Merkle](https://planb.academy/resources/glossary/merkle-tree) root i stvorili dodatni prostor za pretragu. [BIP34](https://planb.academy/resources/glossary/bip) zahteva ugrađivanje visine bloka u Coinbase scriptSig kako bi se osiguralo da svaki Coinbase txid bude jedinstven.


### Polja zaglavlja bloka i Soft Fork signalizacija


Zaglavlje od 80 bajtova sadrži:


- verzija (4 bajta)
- prethodni heš bloka (32 bajta)
- Merkle root (32 bajta)
- vremenska oznaka (4 bajta)
- bits (ciljni nivo težine, 4 bajta)
- nonce (4 bajta)


Brojevi verzija su evoluirali u sistem signalizacije sa bit‑poljem putem BIP9, omogućavajući rudarima da koordiniraju spremnost za [soft-fork](https://planb.academy/resources/glossary/soft-fork). Vremenska oznaka je 32‑bitna Unix vremenska vrednost i biće potrebno ažuriranje oko godine 2106.


#### Bits Field and Targets

Polje bitova kodira cilj u kompaktnom obliku: cilj = koeficijent × 256^(eksponent−3). Važeći heševi blokova moraju biti numerički ispod ovog cilja. Pošto se heševi tumače kao celobrojne vrednosti u formatu malog endian-a, važeći heševi često izgledaju sa mnogo pratećih nula kada se prikazuju u heksadecimalnom formatu.


### Teškoća, Validacija i Prilagođavanja


[Težina](https://planb.academy/resources/glossary/difficulty) je definisana kao lowest_target / current_target, izražavajući koliko je teže mining danas u poređenju sa najlakšom mogućom težinom. Validacija zahteva samo poređenje heša zaglavlja sa ciljem—izuzetno jeftino u odnosu na mining.


Svakih 2016 blokova, Bitcoin podešava težinu kako bi ciljao intervale blokova od ~10 minuta. Podešavanje upoređuje stvarno vreme za prethodnih 2016 blokova sa očekivane dve nedelje. Ograničenja ograničavaju podešavanja unutar faktora četiri. Veliki događaji u stvarnom svetu—kao što je kineska zabrana mining—pokazali su otpornost ovog mehanizma kada je stopa heširanja naglo opala i težina se prilagodila naniže kako bi kompenzovala.


### Subvencija za blok i ukupno Supply


Subvencija na visini h se izračunava kao: subvencija = 5_000_000_000 >> (h // 210_000). Ovo daje raspored prepolovljavanja koji konvergira ka ukupnoj ponudi od ~21 milion BTC. Zbir geometrijskog niza (50 + 25 + 12.5 + …) × 210,000 objašnjava ograničenje. Rudari mogu zahtevati manje od dozvoljene subvencije, ali nikada više, inače blok postaje nevažeći. Kako se subvencije smanjuju kroz uzastopna prepolovljavanja, transakcione naknade postaju sve važnija komponenta prihoda rudara i dugoročne sigurnosti mreže.


## Mrežna komunikacija i Merkleova stabla

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>


![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


### Bitcoin Mrežna Arhitektura


Bitcoin-ova [peer-to-peer](https://planb.academy/resources/glossary/peertopeer-p2p) mreža funkcioniše kao decentralizovani gossip sistem gde čvorovi prenose transakcije i blokove bez međusobnog poverenja. Novi čvorovi se pokreću kontaktiranjem hardkodiranih DNS semena koje održavaju glavni programeri. Ova DNS semena vraćaju IP adrese aktivnih vršnjaka, omogućavajući čvorovima da otkriju mrežu i zatim zatraže dodatne vršnjake putem getaddr. Mrežna komunikacija namerno nije kritična za konsenzus, tako da implementacije mogu da se razlikuju sve dok pravila [konsenzusa](https://planb.academy/resources/glossary/consensus) ostaju nepromenjena.


### Struktura Poruke i Rukovanje


Sve Bitcoin P2P poruke koriste fiksni omotač: 4‑bajtna magična vrednost (F9BEB4D9 za mainnet), 12‑bajtna ASCII komanda, 4‑bajtna dužina sadržaja u little‑endian formatu, 4‑bajtni kontrolni zbir (prva 4 bajta hash256), i sadržaj. Uobičajene komande uključuju version, verack, inv, getdata, tx, block, getheaders, headers, ping, i pong.


Rukovanje počinje kada povezivani čvor pošalje poruku verzije. Primalac odgovara sa verack i svojom verzijom. Kada obe strane razmene ove dve poruke, veza je aktivna i čvorovi mogu početi sa prenosom inventara i podataka.


### Merkle stabla i Merkle koreni


Bitcoin skladišti jedan 32‑bajtni Merkle root u svakom zaglavlju bloka kao posvećenost svim transakcijama u bloku. Transakcije se [heširaju](https://planb.academy/resources/glossary/hash-function) (hash256), uparuju, konkateniraju i heširaju ponavljano dok ne ostane jedan heš. Kada nivo ima neparan broj, poslednji heš se duplira. Interno, heševi su big‑endian, dok serijalizovani podaci bloka koriste little‑endian, što zahteva obrtanje pre i posle konstrukcije stabla.


#### Merkle dokazi i SPV

Merkle dokazi omogućavaju verifikaciju da je transakcija uključena u blok bez preuzimanja celog bloka. Dokaz se sastoji od heševa braće i sestara duž puta do korena. Laki SPV klijenti čuvaju samo zaglavlja blokova i zahtevaju ove dokaze od [punih čvorova](https://planb.academy/resources/glossary/full-node). Pošto Merkle stablo raste logaritamski, dokazivanje uključenja u blok sa hiljadama transakcija zahteva samo nekoliko stotina bajtova.


Taproot proširuje ovaj koncept tako što uslove potrošnje vezuje za Merklizovano stablo skripti (MAST), otkrivajući samo izvršenu granu zajedno sa Merkle dokazom. Ovo poboljšava i efikasnost i privatnost.


### Operacije mreže i sinhronizacija blokova


Čvorovi koriste getdata za zahtev transakcija ili blokova, navodeći ID tipa (1=tx, 2=blok, 3=filtrirani blok, 4=kompaktni blok) plus 32‑bajtni identifikator. Za sinhronizaciju lanca, čvorovi šalju getheaders sa hešom početnog bloka, primajući do 2000 zaglavlja kao odgovor. Svako vraćeno zaglavlje ima 80 bajtova praćeno lažnim brojem transakcija od nula.


Potpuna verifikacija primljenih blokova zahteva dve provere:

1. Heš bloka mora biti ispod cilja kodiranog u polju bitova.

2. Merkle root izračunat iz svih transakcija (sa pravilnim rukovanjem endianness-om) mora se poklapati sa root-om zaglavlja.


Samo ako oba uslova uspeju, čvor prihvata blok, odražavajući Bitcoin princip „ne veruj, proveri“.


## Napredna komunikacija čvorova i odvojeni svedok

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>


![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)


Ova sesija objedinjuje napredno umrežavanje P2P sa Segregated Witness, pokazujući kako moderni Bitcoin softver direktno komunicira sa čvorovima dok koristi SegWit-svesne strukture transakcija. Programeri uče kako da preuzmu blokove, skeniraju relevantne transakcije i konstruiraju transakcije koristeći samo sirovu mrežnu komunikaciju—bez potrebe za blok istraživačima.


### Preuzimanje transakcija zasnovano na blokovima i privatnost


[Novčanici](https://planb.academy/resources/glossary/wallet) moraju detektovati dolazne uplate skeniranjem blokova za izlaze koji odgovaraju njihovom scriptPubKey. Preuzimanje celih blokova bolje štiti privatnost nego zahtev za pojedinačnim transakcijama, što odaje jake signale o aktivnosti korisnika. Čak i zahtevi za blokove mogu odati informacije na lancima sa malim obimom, što čini kompaktne blok filtere (BIP158) ključnim za klijente koji čuvaju privatnost. Filteri mogu proizvesti lažno pozitivne, ali nikada lažno negativne rezultate, omogućavajući klijentima da preuzmu samo potencijalno relevantne blokove bez otkrivanja specifičnih adresa.


### Trustless Mrežna Interakcija


Radni tok `get_block` demonstrira pravilnu upotrebu mreže: pošalji getdata, primi blok, zatim nezavisno verifikuj njegov Merkle root i proof of work. Blok se prihvata samo ako se primljeni hash zaglavlja poklapa sa traženim hashom i njegov izračunati Merkle root poklapa sa zaglavljem. Ovo utelovljuje „ne veruj, proveri“, osiguravajući da čak ni zlonamerni čvorovi ne mogu prevariti čvorove da prihvate izmenjene podatke.


#### Preuzimanje transakcija iz blokova

Transakcije bloka mogu se skenirati za odgovarajuće scriptPubKeys koristeći jednostavnu iteraciju. Proizvodni novčanici to kontinuirano izvode kako novi blokovi stižu, dokazujući vlasništvo nad izlazima isključivo putem kriptografske validacije umesto oslanjanja na API-je trećih strana.


### SegWit Ciljevi i dizajn


Segregated Witness (SegWit) je rešio problem promenljivosti transakcija uklanjanjem podataka o potpisu iz txid proračuna. Ovo je omogućilo pouzdane unapred potpisane lance transakcija i učinilo Lightning Network praktičnim. SegWit je takođe povećao kapacitet bloka koristeći "težinu bloka": stari čvorovi i dalje vide ≤1 MB blokove, dok nadograđeni čvorovi validiraju do 4 MB uključujući podatke svedoka. Verzijski programi svedoka (v0–v1 do sada) stvaraju strukturirani put za nadogradnju budućih tipova skripti.


#### P2WPKH (Native SegWit)


P2WPKH zamenjuje zastarelu P2PKH strukturu sa 22‑bajt skriptom: OP_0 + push20 + hash160(pubkey). Trošenje premešta potpis i javni ključ u zasebno polje svedoka.


- Pre‑SegWit čvorovi: pogledajte “anyone‑can‑spend,” tretirajte to kao važeće.
- Post‑SegWit čvorovi: prepoznaju OP_0 + 20‑bajtni heš i validiraju koristeći podatke svedoka.


Ovo razdvajanje popravlja savitljivost i smanjuje naknade. Svedok koristi varint brojanje praćeno potpisom i javnim ključem.


#### P2SH-P2WPKH (Backward-Compatible SegWit)


Da bi se omogućilo starim novčanicima da šalju na SegWit adrese, P2WPKH skripte mogu biti obuhvaćene u P2SH.


- scriptPubKey: standard P2SH hash160(redeemScript)
- scriptSig: the redeemScript (the P2WPKH program)
- svedok: potpis + javni ključ


Slojevi validacije:

1. Pre‑BIP16 čvorovi prihvataju redeemScript kao važeći.

2. Čvorovi nakon BIP16 ga procenjuju, ostavljajući OP_0 + hash na steku.

3. SegWit čvorovi obavljaju punu validaciju svedoka.


#### P2WSH za složene skripte


P2WSH generalizuje SegWit za multisig i napredne skripte tako što se obavezuje na SHA256(script) umesto na hash160. Tipičan 2‑od‑3 multisig svedok stek:


- prazan element (CHECKMULTISIG greška)
- sig1
- sig2
- script svedoka (multisig skripta)


SegWit čvorovi proveravaju da li se SHA256(witnessScript) poklapa sa hash-om scriptPubKey i zatim ga izvršavaju. Korišćenje SHA256 i 32‑bajtni hash omogućava razlikovanje P2WSH od P2WPKH i jača sigurnost.


#### P2SH-P2WSH (Maksimalna Kompatibilnost)


Složeni SegWit skripti mogu biti i P2SH‑omotani:


- scriptSig: redeemScript (OP_0 + 32‑byte hash)
- svedok: potpisi + svedokSkript


Validacija prolazi kroz tri generacije pravila tačno kao sa P2SH‑P2WPKH. Ovaj omotač je bio ključan za rane Lightning implementacije koje su zahtevale multisig bez malleabilnosti. Iako je danas preferiran native P2WSH, omotani oblik osigurava kompatibilnost sa starijim wallet sistemima.


### Uticaj SegWit


SegWit obezbeđen:


- stabilni ID-ovi transakcija
- niže naknade putem sniženih podataka svedoka
- veći protok blokova putem težine bloka
- kompatibilnost za stare čvorove
- čist put nadogradnje za Taproot i buduća proširenja


Zajedno sa interakcijom sa mrežom bez poverenja, ovi alati čine okosnicu modernog razvoja Bitcoin.



# Završni Deo


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Recenzije i ocene


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>

## Završni ispit


<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>



<isCourseExam>true</isCourseExam>

## Zaključak



<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>


<isCourseConclusion>true</isCourseConclusion>