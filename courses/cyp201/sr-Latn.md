---
name: Unutrašnje funkcionisanje Bitkojn novčanika
goal: Uronite u kriptografske principe koji pokreću Bitkojn novčanike.
objectives: 

  - Definisanje teorijskih pojmova neophodnih za razumevanje kriptografskih algoritama korišćenih u Bitkojnu
  - Potpuno razumevanje konstrukcije determinističkog i hijerarhijskog novčanika.
  - Znati kako identifikovati i smanjiti rizike povezane sa upravljanjem novčanikom.
  - Razumevanje principa heš funkcija, kriptografskih ključeva i digitalnih potpisa.

---

# Putovanje u središte Bitkojn novčanika


Otkrijte tajne determinističkih i hijerarhijskih Bitkojn novčanika uz naš CYP201 kurs! Bilo da ste redovan korisnik ili entuzijasta koji želi produbiti svoje znanje, ovaj kurs nudi sveobuhvatno upoznavanje sa funkcionisanjem ovih alata koje svakodnevno koristimo.


Saznajte o mehanizmima heš funkcija, digitalnim potpisima (ECDSA i Šnor), mnemonic frazama (bezbednosnim frazama), kriptografskim ključevima i kreiranju adresa za primanje, sve dok istražujete napredne strategije digitalne (informacione) bezbednosti.


Ova obuka će vas ne samo opremiti znanjem za razumevanje osnovnih elemenata Bitkojn novčanika, već će vas i pripremiti da zaronite dublje u uzbudljivi svet kriptografije.


Uz jasnu pedagogiju, preko 60 objašnjavajućih dijagrama i konkretne primere, CYP201 će vam omogućiti da razumete od A do Š kako vaš novčanik funkcioniše, tako da možete sa sigurnošću nastaviti istraživati Bitkojn univerzum. Preuzmite kontrolu nad svojim UTXO-ima danas razumevanjem kako HD(hijarahijski deterministički) novčanici funkcionišu!


+++

# Uvod


<partId>32960669-d13a-592f-a053-37f70b997cbf</partId>


## Uvod u kurs


<chapterId>fb4e8857-ea35-5a8a-ae8a-5300234e0104</chapterId>


Dobrodošli na kurs CYP201, gde ćemo detaljno istražiti funkcionisanje HD Bitkojn novčanika. Ovaj kurs je dizajniran za svakoga ko želi da razume tehničke osnove korišćenja Bitkojna, bilo da su povremeni korisnici, prosvetljeni entuzijasti ili budući stručnjaci.


Cilj ove obuke je da vam pruži ključeve za savladavanje alata koje svakodnevno koristite. HD Bitkojn novčanici, koji su u srcu vašeg korisničkog iskustva, zasnovani su na ponekad složenim konceptima, koje ćemo pokušati učiniti pristupačnim. Zajedno ćemo ih demistifikovati!


Pre nego što se upustimo u detalje strukture i funkcionisana Bitkojn novčanika, počećemo sa nekoliko poglavlja o kriptografskim primitivama koje treba poznavati za ono što sledi.

Počećemo sa kriptografskim heš funkcijama, koje su fundamentalne kako za novčanike, tako i za sam Bitkojn protokol. Otkrićete njihove glavne karakteristike, specifične funkcije korišćene u Bitkojnu, a u tehnički detaljnijem poglavlju, naučićete detalje o funkcionisanju kraljice heš funkcija: SHA256.


![CYP201](assets/fr/010.webp)


Dalje ćemo se pozabaviti funkcionisanjem algoritama za digitalno potpisivanje koje koristite svakodnevno za obezbeđivanje vaših UTXO-a. Bitcoin koristi dva takva algoritma: ECDSA i Šnor protokol. Naučićete koji matematički primitivi leže u osnovi ovih algoritama i kako oni osiguravaju bezbednost transakcija.


![CYP201](assets/fr/021.webp)


Kada dobro razumemo ove kriptografske elemente, konačno ćemo preći na srž obuke: determinističke i hijerarhijske novčanike! Prvo, postoji odeljak posvećen bezbednosnim frazama, ovim sekvencama od 12 ili 24 reči koje vam omogućavaju da kreirate i obnovite svoje novčanike. Otkrićete kako se ove reči generišu iz izvora entropije i kako olakšavaju korišćenje Bitkojna.


![CYP201](assets/fr/040.webp)


Obuka će se nastaviti proučavanjem BIP39 passphrase (sigurnosna fraza, fraza za pristup), seed (ne treba ga mešati sa bezbednosnom frazom), master lanca koda i master ključa. Detaljno ćemo videti šta su ovi elementi, njihove odgovarajuće uloge i kako se izračunavaju.


![CYP201](assets/fr/045.webp)


Konačno, iz glavnog ključa, otkrićemo kako se izvode kriptografski parovi ključeva na deterministički i hijerarhijski način do adresa za primanje.


![CYP201](assets/fr/056.webp)


Ova obuka će vam omogućiti da koristite vaš softverski novčanik sa samopouzdanjem, dok unapređujete svoje veštine za identifikaciju i ublažavanje rizika. Pripremite se da postanete pravi stručnjak za Bitkojn novčanike!


Ova tabela vam nudi prevod glavnih engleskih termina koji se koriste, kako bi vam olakšala razumevanje šema i tehničkih dokumenata korišćenih u okviru kursa CYP 201.

| Engleski        | Prevod / Objašnjenje                                                                               |
| --------------- | -------------------------------------------------------------------------------------------------- |
| *pubkey hash*   | Heš javnog ključa (koristi se za generisanje Bitcoin adrese).                                       |
| *public key*    | Javni ključ (služi za primanje sredstava, izveden iz privatnog ključa).                             |
| *signature*     | Digitalni potpis (kriptografski dokaz da poruka potiče od vlasnika privatnog ključa).               |
| *scriptPubKey*  | Skripta zaključavanja (definiše uslove za trošenje izlaza).                                         |
| *scriptSig*     | Skripta otključavanja (obezbeđuje podatke za ispunjavanje *scriptPubKey*).                          |
| *Stack*         | Stek (struktura podataka koju koristi *Bitcoin Script*).                                            |
| *input*         | Ulaz transakcije (referenca na prethodni izlaz korišćen kao izvor).                                 |
| *output*        | Izlaz transakcije (definiše primaoca i iznos).                                                      |
| *transaction*   | Bitcoin transakcija (skup ulaza i izlaza koji potvrđuju transfer).                                  |
| *XOR*           | Logički operator "isključivo ILI", koristi se u nekim kriptografskim šemama.                       |
| *HMAC*          | Kod za autentifikaciju poruka zasnovan na hešu i tajnom ključu.                                     |
| *ECDSA*         | Algoritam digitalnog potpisa sa eliptičnim krivama.                                                 |
| *hash*          | Heš (jedinstveni i fiksni otisak podataka).                                                         |
| *SigHash*       | Tip heša potpisa (definiše koji delovi transakcije se potpisuju).                                   |
| *HD Wallet*     | Hijerarhijski deterministički novčanik (generiše više ključeva iz jednog semena).                   |
| *Random Number* | Nasumičan broj (koristi se za generisanje sigurnih privatnih ključeva).                             |
| *State*         | Stanje (međuvrednost u kriptografskom procesu).                                                     |
| *Entropy*       | Entropija (mera nasumičnosti, koristi se za generisanje semena za novčanike).                       |
| *Mnemonic*      | Mnemotehnika (niz reči koji olakšava čuvanje i obnavljanje semena).                                 |
| *Wordlist*      | Lista reči (unapred definisan skup korišćen za generisanje BIP39 mnemotehnika).                     |
| *Seed*          | Semе (početna vrednost koja omogućava izvođenje svih ključeva iz HD novčanika).                     |
| *Address*       | Bitcoin adresa (čitljiv identifikator za primanje sredstava, izveden iz javnog ključa).             |
| *Leaf*          | List (krajnji čvor u stablu derivacije).                                                            |

# Heš Funkcije


<partId>3713fee1-2ec2-512e-9e97-b6da9e4d2f17</partId>


## Uvod u heš funkcije


<chapterId>dba011f5-1805-5a48-ac2b-4bd637c93703</chapterId>


Prvi tip kriptografskih algoritama korišćenih u Bitkojnu uključuje heš funkcije. One igraju ključnu ulogu na različitim nivoima protokola, ali i unutar Bitkojn novčanika. Hajde da zajedno otkrijemo šta je heš funkcija i za šta se koristi u Bitkojnu.


### Definicija i princip heširanja


Heširanje je proces koji transformiše informacije proizvoljne dužine u informaciju fiksne dužine putem kriptografske heš funkcije. Drugim rečima, heš funkcija uzima ulaz bilo koje veličine i pretvara ga u otisak fiksne veličine, koji se zove "Heš".

Heš se takođe može ponekad nazivati "digest" (sažetak), "kondenzat", "kondenzovano" (sažeto) ili "hešovano".


Na primer, SHA256 heš funkcija proizvodi heš fiksne dužine od 256 bita. Dakle, ako koristimo ulaz "_PlanB_", poruku proizvoljne dužine, generisani heš će biti sledeći otisak od 256 bita:


```text
24f1b93b68026bfc24f5c8265f287b4c940fb1664b0d75053589d7a4f821b688
```


![CYP201](assets/fr/001.webp)


### Karakteristike heš funkcija


Ove kriptografske heš funkcije imaju nekoliko osnovnih karakteristika koje ih čine posebno korisnim u kontekstu Bitkojna i drugih računarskih sistema:



- Nepovratnost (ili otpornost na pronalaženej ulaza (preimage-a))
- Otpornost na neovlašćeno menjanje (takođe poznat i kao efekat lavine)
- Otpornost na koliziju
- Otpornost na pronalaženje drugog ulaza


#### 1. Nepovratnost (otpornost na preimage (ulazni podaci)):


Nepovratnost znači da je lako izračunati heš iz ulaznih informacija, ali obrnuti proračun, to jest, pronalaženje ulaza iz heša, je praktično nemoguće. Ovo svojstvo čini heš funkcije savršenim za kreiranje jedinstvenih digitalnih otisaka prstiju bez ugrožavanja originalnih informacija. Ova karakteristika se često naziva funkcijom u jednom smeru.


U datom primeru, dobijanje heš vrednosti `24f1b9…` znajući unos "_PlanB_" je jednostavno i brzo. Međutim, pronalaženje poruke "_PlanB_" samo znajući `24f1b9…` je nemoguće.


![CYP201](assets/fr/002.webp)


Stoga je nemoguće pronaći preimage tj.input $m$ znajući vrednost heša $h$ tako da je $h = \text{Hash}(m)$, gde je $\text{Hash}$ kriptografska heš funkcija.


#### 2. Otpornost na neovlašćene izmene (efekat lavine)


Druga karakteristika je otpornost na neovlašćene izmene, takođe poznata kao **efekat lavine**. Ova karakteristika se primećuje u heš funkciji tako što i mala promena u ulaznoj poruci rezultira radikalnom promenom u izlazu heš funkcije.


Ako se vratimo na naš primer sa unosom "_PlanB_" i SHA256 funkcijom, videli smo da generisani heš izgleda ovako:


```text
24f1b93b68026bfc24f5c8265f287b4c940fb1664b0d75053589d7a4f821b688
```


Ako napravimo vrlo malu promenu u unosu koristeći "_Planb_" ovaj put, onda jednostavno menjanje velikog slova "B" u malo slovo "b" u potpunosti menja SHA256 izlaz:


```text
bb038b4503ac5d90e1205788b00f8f314583c5e22f72bec84b8735ba5a36df3f
```


![CYP201](assets/fr/003.webp)


Ovo svojstvo osigurava da se čak i najmanja promena originalne poruke odmah otkrije, jer ne menja samo mali deo heša, već ceo heš. Ovo može biti od interesa u raznim oblastima za verifikaciju integriteta poruka, softvera ili čak Bitkojn transakcija.


#### 3. Otpornost na koliziju


Treća karakteristika je otpornost na koliziju. Heš funkcija je otporna na koliziju ako je računarski nemoguće pronaći 2 različite poruke koje proizvode isti heš izlaz iz heš funkcije. Formalno, teško je pronaći dve različite poruke $m_1$ i $m_2$ tako da imaju istu heš vrednost:


$$
\text{HASH}(m_1) = \text{HASH}(m_2)
$$


![CYP201](assets/fr/004.webp)


U stvarnosti, matematički je neizbežno da kolizije postoje za heš funkcije, jer veličina ulaza može biti veća od veličine izlaza. Ovo je poznato kao Dirihleov princip fioka: ako je $n$ objekata raspoređeno u $m$ fioka, sa $m < n$, onda će najmanje jedna fioka nužno sadržati dva ili više objekata. Za heš funkciju, ovaj princip se primenjuje jer je broj mogućih poruka gotovo beskonačan, dok je broj mogućih heševa konačan ($2^{256}$ u slučaju SHA256 funkcije).


Dakle, ova karakteristika ne znači da ne postoje kolizije za heš funkcije, već da dobra heš funkcija čini verovatnoću pronalaženja kolizije zanemarljivom. Ova karakteristika, na primer, više nije potvrđena za SHA-0 i SHA-1 algoritme, prethodnike SHA-2, za koje su pronađene kolizije. Ove funkcije se stoga sada ne preporučuju i često se smatraju zastarelim.

Za heš funkciju od $n$ bita, otpornost na koliziju je reda $2^{\frac{n}{2}}$, u skladu sa napadom zasnovanom na paradoksu rođendana. Na primer, za SHA256 ($n = 256$), složenost pronalaženja kolizije je reda $2^{128}$ pokušaja. U praktičnim terminima, to znači da ako se kroz funkciju prođe $2^{128}$ različitih poruka, verovatno će se pronaći kolizija.


#### 4. Otpornost na drugi preimage iliti na drugi ulaz


Otpornost na drugi preimage je još jedna važna karakteristika heš funkcija. Ona navodi da je, za datu poruku $m_1$ i njen heš $h$, računarski neizvodljivo pronaći drugu poruku $m_2 \neq m_1$ takvu da:


$$
\text{HASH}(m_1) = \text{HASH}(m_2)
$$


Dakle, otpornost na drugi preimage (ulaz) je donekle slična otpornosti na koliziju, osim što je ovde napad teži jer napadač ne može slobodno izabrati $m_1$.


![CYP201](assets/fr/005.webp)


### Primene heš funkcija u Bitkojnu


Najčešće korišćena heš funkcija u Bitkojnu je **SHA256** ("_Secure Hash Algorithm 256 bits"_). Dizajnirana početkom 2000-ih od strane NSA i standardizovana od strane NIST, proizvodi 256-bitni heš izlaz.


Ova funkcija se koristi u mnogim aspektima Bitkojna. Na nivou protokola, koristi se kod Proof-of-Work mehanizma, gde se primenjuje u dvostrukom heširanju za pretragu delimične kolizije između zaglavlja kandidatskog bloka, kreiranog od strane rudara, i cilja težine (difficulty target). Ako se ova delimična kolizija pronađe, kandidatski blok postaje važeći i može biti dodat u blokčejn.


SHA256 se takođe koristi u konstrukciji Merkle Tree (Merkelovo stablo), koji je specifičan akumulator koji se koristi za beleženje transakcija u blokovima. Ova struktura se takođe nalazi u Utreexo protokolu, koji omogućava smanjenje veličine UTXO skupa. Pored toga, sa uvođenjem Taproot-a u 2021. godini, SHA256 se koristi u MAST-u (_Merkelised Alternative Script Tree_), što omogućava otkrivanje samo zahteva za otključavanje sredstava koji su zapravo korišćeni u skripti, bez otkrivanja drugih mogućih opcija. Takođe se koristi u izračunavanju identifikatora transakcija, u prenosu paketa preko P2P mreže, u elektronskim potpisima... Na kraju, i ovo je od posebnog interesa u ovoj obuci, SHA256 se koristi na nivou aplikacije za kreiranje Bitcoin novčanika i derivaciju adresa.


Većinu vremena, kada naiđete na upotrebu SHA256 u Bitcoin-u, to će zapravo biti dvostruki heš SHA256 funkcije, označen kao "**HASH256**", što jednostavno podrazumeva primenu SHA256 dva puta uzastopno:


$$
\text{HASH256}(m) = \text{SHA256}(\text{SHA256}(m))
$$


Ova praksa dvostrukog heširanja dodaje dodatni nivo sigurnosti protiv određenih potencijalnih napada, iako se jedan SHA256 danas smatra kriptografski sigurnim.


Još jedna funkcija heširanja dostupna u Script jeziku i korišćena za dobijanje adresa za primanje je RIPEMD160 funkcija. Ova funkcija proizvodi 160-bitni heš (dakle kraći od SHA256). Obično se kombinuje sa SHA256 da bi se formirala HASH160 funkcija:


$$
\text{HASH160}(m) = \text{RIPEMD160}(\text{SHA256}(m))
$$


Ova kombinacija se koristi za generisanje kraćih heševa, posebno u kreiranju određenih Bitcoin adresa koje predstavljaju heševe ključeva ili heševe skripti, kao i za kreiranje otisaka ključeva (jedinstveni indentifikator javnog ključa).


Konačno, samo na nivou aplikacije, ponekad se koristi i funkcija SHA512, koja indirektno igra ulogu u derivaciji ključeva za novčanike. Ova funkcija je veoma slična SHA256 u svom radu; obe pripadaju istoj SHA2 porodici, ali SHA512 proizvodi, kao što njen naziv ukazuje, 512-bitni heš, u poređenju sa 256 bita za SHA256. Njenu upotrebu ćemo detaljno opisati u narednim poglavljima.


Sada znate osnove o heš funkcijama za ono što sledi. U sledećem poglavlju predlažem da detaljnije otkrijemo kako funkcioniše funkcija koja je u srcu Bitcoin-a: SHA256. Rastavićemo je kako bismo razumeli kako postiže karakteristike koje smo ovde opisali. Ovo sledeće poglavlje je prilično dugo i tehničko, ali nije neophodno za praćenje ostatka obuke. Dakle, ako imate poteškoća sa razumevanjem, ne brinite i pređite direktno na sledeće poglavlje, koje će biti mnogo pristupačnije.


## Unutrašnji mehanizmi SHA256 funkcije


<chapterId>905eb320-f15b-5fb6-8d2d-5bb447337deb</chapterId>


Prethodno smo videli da heš funkcije poseduju važne karakteristike koje opravdavaju njihovu upotrebu u Bitcoin-u. Hajde sada da ispitamo unutrašnje mehanizme ovih heš funkcija koje im daju ova svojstva, i da bismo to uradili, predlažem da rastavimo operaciju fukcije SHA256.


Funkcije SHA256 i SHA512 pripadaju istoj porodici SHA2. Njihov mehanizam zasniva se na specifičnoj konstrukciji zvanoj **Merkle-Damgård konstrukcija**. RIPEMD160 takođe koristi ovu istu vrstu konstrukcije.


Kao podsetnik, imamo poruku proizvoljne veličine kao ulaz za SHA256, i provući ćemo je kroz funkciju da bismo dobili 256-bitni heš kao izlaz.


### Pre-procesiranje ulaza


Da bismo započeli, potrebno je pripremiti našu ulaznu poruku $m$ tako da ima standardnu dužinu koja je deljiva sa 512 bita. Ovaj korak je ključan za pravilno funkcionisanje algoritma u nastavku.

Da bismo to uradili, počinjemo sa korakom dodavanja bitova za popunjavanje. Prvo dodajemo separator bit `1` poruci, praćen sa određenim brojem `0` bitova. Broj dodatih `0` bitova se računa tako da ukupna dužina poruke nakon ovog dodavanja bude kongruentna sa 448 modulo 512. Dakle, dužina $L$ poruke sa bitovima za popunjavanje je jednaka:


$$
L \equiv 448 \mod 512
$$


$\text{mod}$, za modulo operaciju, je matematička operacija koja, između dva cela broja, vraća ostatak Euklidovskog deljanja prvog broja drugim. Na primer: $16 \mod 5 = 1$. To je operacija koja se široko koristi u kriptografiji.


Ovde, korak popunjavanja osigurava da, nakon dodavanja 64 bita u sledećem koraku, ukupna dužina izjednačene poruke bude deljiva sa 512 bita. Ako početna poruka ima dužinu od $M$ bita, broj ($N$) `0` bita koji treba dodati je:


$$
N = (448 - (M + 1) \mod 512) \mod 512
$$


Na primer, ako je početna poruka 950 bita, proračun bi bio sledeći:


$$
\begin{align*}
M & = 950 \\
M + 1 & = 951 \\
(M + 1) \mod 512 & = 951 \mod 512 \\
& = 951 - 512 \cdot \left\lfloor \frac{951}{512} \right\rfloor \\
& = 951 - 512 \cdot 1 \\
& = 951 - 512 \\
& = 439 \\
\\
448 - (M + 1) \mod 512 & = 448 - 439 \\
& = 9 \\
\\
N & = (448 - (M + 1) \mod 512) \mod 512 \\
N & = 9 \mod 512 \\
& = 9
\end{align*}
$$


Dakle, imali bismo 9 `0` pored separatora `1`. Naši bitovi za popunjavanje koji će biti dodati direktno nakon naše poruke $M$ bi bili:


```text
1000 0000 00
```


Nakon dodavanja bitova popune našoj poruci $M$, takođe dodajemo 64-bitnu reprezentaciju originalne dužine poruke $M$, izraženu u binarnom obliku. Ovo omogućava funkciji heš da bude osetljiva na redosled bitova i dužinu poruke.


Ako se vratimo na naš primer sa početnom porukom od 950 bita, konvertujemo decimalni broj `950` u binarni, što nam daje `1110 1101 10`. Ovaj broj dopunjujemo nulama s leva (na početak) kako bismo dobili ukupno dužinu od 64 bita. U našem primeru, to daje:


```text
0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0011 1011 0110
```


Ovo popunjavanje bitovima za dužinu poruke se dodaje nakon popunjavanja bitovima. Dakle, poruka nakon naše predobrade sastoji se od tri dela:



- Originalna poruka $M$;
- Bit `1` praćen sa nekoliko `0` bitova da formira bitove popunjavenja;
- 64-bitna reprezentacija dužine $M$ za formiranje popunjavanja sa veličinom.


![CYP201](assets/fr/006.webp)


### Inicijalizacija promenljivih


SHA256 koristi osam početnih promenljivih stanja, označenih sa $A$ do $H$, svaka po 32 bita. Ove promenljive su inicijalizovane specifičnim konstantama, koje su decimalni delovi kvadratnih korena prvih osam prostih brojeva. Ove vrednosti ćemo koristiti naknadno tokom procesa heširanja:



- $A = 0x6a09e667$
- $B = 0xbb67ae85$
- $C = 0x3c6ef372$
- $D = 0xa54ff53a$
- $E = 0x510e527f$
- $F = 0x9b05688c$
- $G = 0x1f83d9ab$
- $H = 0x5be0cd19$


SHA256 takođe koristi 64 druge konstante, označene sa $K_0$ do $K_{63}$, koje su decimalni delovi kubnih korenova prvih 64 prostih brojeva:


$$
K[0 \ldots 63] = \begin{pmatrix}
0x428a2f98, & 0x71374491, & 0xb5c0fbcf, & 0xe9b5dba5, \\
0x3956c25b, & 0x59f111f1, & 0x923f82a4, & 0xab1c5ed5, \\
0xd807aa98, & 0x12835b01, & 0x243185be, & 0x550c7dc3, \\
0x72be5d74, & 0x80deb1fe, & 0x9bdc06a7, & 0xc19bf174, \\
0xe49b69c1, & 0xefbe4786, & 0x0fc19dc6, & 0x240ca1cc, \\
0x2de92c6f, & 0x4a7484aa, & 0x5cb0a9dc, & 0x76f988da, \\
0x983e5152, & 0xa831c66d, & 0xb00327c8, & 0xbf597fc7, \\
0xc6e00bf3, & 0xd5a79147, & 0x06ca6351, & 0x14292967, \\
0x27b70a85, & 0x2e1b2138, & 0x4d2c6dfc, & 0x53380d13, \\
0x650a7354, & 0x766a0abb, & 0x81c2c92e, & 0x92722c85, \\
0xa2bfe8a1, & 0xa81a664b, & 0xc24b8b70, & 0xc76c51a3, \\
0xd192e819, & 0xd6990624, & 0xf40e3585, & 0x106aa070, \\
0x19a4c116, & 0x1e376c08, & 0x2748774c, & 0x34b0bcb5, \\
0x391c0cb3, & 0x4ed8aa4a, & 0x5b9cca4f, & 0x682e6ff3, \\
0x748f82ee, & 0x78a5636f, & 0x84c87814, & 0x8cc70208, \\
0x90befffa, & 0xa4506ceb, & 0xbef9a3f7, & 0xc67178f2
\end{pmatrix}
$$


### Deljenje ulaza


Sada kada imamo izjednačen ulaz, preći ćemo na glavnu fazu obrade SHA256 algoritma: funkciju kompresije. Ovaj korak je veoma važan, jer je to prvenstveno ono što daje heš funkciji njene kriptografske osobine koje smo proučavali u prethodnom poglavlju.


Prvo, počinjemo tako što našu izjednačenu poruku (rezultat koraka predobrade) delimo na nekoliko blokova $P$ od po 512 bita. Ako naša izjednačena poruka ima ukupnu veličinu od $n \times 512$ bita, imaćemo $n$ blokova, svaki od po 512 bita. Svaki blok od 512 bita biće obrađen pojedinačno pomoću funkcije kompresije, koja se sastoji od 64 runde uzastopnih operacija. Nazovimo ove blokove $P_1$, $P_2$, $P_3$...


### Logičke Operacije


Pre nego što detaljno istražimo funkciju kompresije, važno je razumeti osnovne logičke operacije koje se koriste u njoj. Ove operacije, zasnovane na Bulovoj algebri, funkcionišu na nivou bita. Osnovne logičke operacije koje se koriste su:



- **Konjunkcija (I)**: označena sa $\land$, odgovara logičkom "I".
- **Disjunkcija (ILI)**: označena sa $\lor$, odgovara logičkom "ILI".
- **Negacija (NE)**: označena sa $\lnot$, odgovara logičkom "NE".


Iz ovih osnovnih operacija možemo definisati složenije operacije, kao što je "Ekskluzivno ILI" (XOR) označeno sa $\oplus$, koje se široko koristi u kriptografiji.

Svaka logička operacija može biti predstavljena tabelom istinitosti, koja pokazuje rezultat za sve moguće kombinacije binarnih ulaznih vrednosti (dva operanda $p$ i $q$).

Za XOR ($\oplus$):


| $p$ | $q$ | $p \oplus q$ |
| --- | --- | ------------ |
| 0   | 0   | 0            |
| 0   | 1   | 1            |
| 1   | 0   | 1            |
| 1   | 1   | 0            |

Za I ($\land$):


| $p$ | $q$ | $p \land q$ |
| --- | --- | ----------- |
| 0   | 0   | 0           |
| 0   | 1   | 0           |
| 1   | 0   | 0           |
| 1   | 1   | 1           |

Za NE ($\lnot p$):


| $p$ | $\lnot p$ |
| --- | --------- |
| 0   | 1         |
| 1   | 0         |

Hajde da uzmemo primer da bismo razumeli operaciju XOR na nivou bita. Ako imamo dva binarna broja sa 6 bita:



- $a = 101100$
- $b = 001000$


Onda:


$$

a \oplus b = 101100 \oplus 001000 = 100100


$$


Primenom XOR-a bit po bit:


| Bit Position | $a$ | $b$ | $a \oplus b$ |
| ------------ | --- | --- | ------------ |
| 1            | 1   | 0   | 1            |
| 2            | 0   | 0   | 0            |
| 3            | 1   | 1   | 0            |
| 4            | 1   | 0   | 1            |
| 5            | 0   | 0   | 0            |
| 6            | 0   | 0   | 0            |

Rezultat je $100100$.


Pored logičkih operacija, funkcija kompresije koristi operacije pomeranja bitova, koje će igrati ključnu ulogu u difuziji bitova u algoritmu.


Prvo, tu je logička operacija pomeranja udesno, označena sa $ShR_n(x)$, koja pomera sve bitove $x$ udesno za $n$ pozicija, popunjavajući prazne bitove s leve strane nulama.


Na primer, za $x = 101100001$ (na 9 bita) i $n = 4$:


$$

ShR_4(101100001) = 000010110


$$


Šema pomeranja u desno može se videti ovako:


![CYP201](assets/fr/007.webp)


Još jedna operacija koja se koristi u SHA256 za manipulaciju bitovima je desna kružna rotacija, označena sa $RotR_n(x)$, koja pomera $x$ bitove udesno za $n$ pozicija, umećući pomerene bitove na početak niza.

Na primer, za $x = 101100001$ (sa 9 bitova) i $n = 4$:


$$

RotR_4(101100001) = 000110110


$$


Šema za kružno pomeranje u desno može izgledati ovako:


![CYP201](assets/fr/008.webp)


### Funkcija kompresije


Sada kada smo razumeli osnovne operacije, hajde da detaljno ispitamo SHA256 kompresionu funkciju.


U prethodnom koraku, podelili smo naš ulaz na nekoliko delova od 512 bita $P$. Za svaki blok od 512 bita $P$, imamo:



- **Reči poruke $W_i$**: za $i$ od 0 do 63.
- **Konstante $K_i$**: za $i$ od 0 do 63, definisane u prethodnom koraku.
- **Varijable stanja $A, B, C, D, E, F, G, H$**: inicijalizovane vrednostima iz prethodnog koraka.


Prvih 16 reči, $W_0$ do $W_{15}$, direktno su izvučene iz obrađenog 512-bitnog bloka $P$. Svaka reč $W_i$ se sastoji od 32 uzastopna bita iz bloka. Tako, na primer, uzimamo naš prvi deo ulaza $P_1$, i dalje ga delimo na manje 32-bitne delove koje nazivamo rečima.


Sledećih 48 reči ($W_{16}$ do $W_{63}$) generišu se koristeći sledeću formulu:


$$
W_i = W_{i-16} + \sigma_0(W_{i-15}) + W_{i-7} + \sigma_1(W_{i-2}) \mod 2^{32}
$$


Sa:



- $\sigma_0(x) = RotR_7(x) \oplus RotR_{18}(x) \oplus ShR_3(x)$
- $\sigma_1(x) = RotR_{17}(x) \oplus RotR_{19}(x) \oplus ShR_{10}(x)$


U ovom slučaju, $x$ je jednako $W_{i-15}$ za $\sigma_0(x)$ i $W_{i-2}$ za $\sigma_1(x)$.


Kada odredimo sve reči $W_i$ za naš 512-bitni deo, možemo preći na funkciju kompresije, koja se sastoji od izvođenja 64 runde.


![CYP201](assets/fr/009.webp)

Za svaku rundu $i$ od 0 do 63, imamo tri različite vrste ulaza. Prvo, $W_i$ koji smo upravo odredili, delimično sastavljenu od naše poruke $P_n$. Zatim, 64 konstante $K_i$. Na kraju, koristimo variable stanja $A$, $B$, $C$, $D$, $E$, $F$, $G$ i $H$, koje će se menjati tokom procesa heširanja i biti modifikovane svakom funkcijom kompresije. Međutim, za prvi deo $P_1$, koristimo prethodno date početne konstante.


Zatim izvodimo sledeće operacije na našim ulazima:



- Funkcija $\Sigma_0$:


$$
\Sigma_0(A) = RotR_2(A) \oplus RotR_{13}(A) \oplus RotR_{22}(A)
$$



- Funkcija $\Sigma_1$:


$$
\Sigma_1(E) = RotR_6(E) \oplus RotR_{11}(E) \oplus RotR_{25}(E)
$$



- Funkcija $Ch$ ("_Choose_"):


$$
Ch(E, F, G) = (E \land F) \oplus (\lnot E \land G)
$$



- Funkcija $Maj$ ("_Majority_"):


$$
Maj(A, B, C) = (A \land B) \oplus (A \land C) \oplus (B \land C)
$$


Zatim izračunavamo 2 privremene promenljive:



- $temp1$:


$$
temp1 = H + \Sigma_1(E) + Ch(E, F, G) + K_i + W_i \mod 2^{32}
$$



- $temp2$:


$$
temp2 = \Sigma_0(A) + Maj(A, B, C) \mod 2^{32}
$$


Zatim ažuriramo varijable stanja na sledeći način:


$$
\begin{cases}
H = G \\
G = F \\
F = E \\
E = D + temp1 \mod 2^{32} \\
D = C \\
C = B \\
B = A \\
A = temp1 + temp2 \mod 2^{32}
\end{cases}
$$


Sledeći dijagram predstavlja rundu SHA256 kompresione funkcije kako smo upravo opisali:


![CYP201](assets/fr/010.webp)



- Strelice označavaju tok podataka;
- Kutije predstavljaju izvršene operacije;
- Okruženi $+$ predstavljaju sabiranje modulo $2^{32}$.


Već možemo primetiti da ova runda daje nove varijable stanja $A$, $B$, $C$, $D$, $E$, $F$, $G$, i $H$. Ove nove promenljive će služiti kao ulaz za sledeću rundu, koja će zauzvrat proizvesti nove promenljive $A$, $B$, $C$, $D$, $E$, $F$, $G$, i $H$, koje će se koristiti za narednu rundu. Ovaj proces se nastavlja do 64. runde.

Nakon 64 runde, ažuriramo početne vrednosti variajabli stanja dodavanjem konačnih vrednosti na kraju 64. runde:


$$
\begin{cases}
A = A_{\text{initial}} + A \mod 2^{32} \\
B = B_{\text{initial}} + B \mod 2^{32} \\
C = C_{\text{initial}} + C \mod 2^{32} \\
D = D_{\text{initial}} + D \mod 2^{32} \\
E = E_{\text{initial}} + E \mod 2^{32} \\
F = F_{\text{initial}} + F \mod 2^{32} \\
G = G_{\text{initial}} + G \mod 2^{32} \\
H = H_{\text{initial}} + H \mod 2^{32}
\end{cases}
$$


Ove nove vrednosti $A$, $B$, $C$, $D$, $E$, $F$, $G$ i $H$ će služiti kao početne vrednosti za sledeći blok, $P_2$. Za ovaj blok $P_2$, ponavljamo isti proces kompresije sa 64 runde, zatim ažuriramo promenljive za blok $P_3$, i tako dalje sve do poslednjeg bloka našeg izjednačenog ulaza.


Nakon obrade svih blokova poruka, spajamo konačne vrednosti promenljivih $A$, $B$, $C$, $D$, $E$, $F$, $G$ i $H$ da bismo formirali konačni 256-bitni heš naše heš funkcije:


$$

\text{Hash} = A \Vert B \Vert C \Vert D \Vert E \Vert F \Vert G \Vert H


$$


Svaka promenljiva je 32-bitni ceo broj, tako da njihova spajanje (konkatinacija) uvek daje 256-bitni rezultat, bez obzira na veličinu naše ulazne poruke za heš funkciju.


### Dokaz kriptografskih svojstava


Ali, kako je onda ova funkcija ireverzibilna, otporna na kolizije i otporna na neovlašćene izmene?


Za otpornost na neovlašćene izmene, prilično je jednostavno razumeti. Postoji toliko mnogo proračuna koji se izvode u kaskadi, a koji zavise i od ulaza i od konstanti, da i najmanja modifikacija početne poruke potpuno menja putanju, a time i potpuno menja izlazni heš. Ovo se naziva efektom lavine. Ovo svojstvo je delimično osigurano mešanjem međustanja sa početnim stanjima za svaki naredni deo.

Zatim, kada se diskutuje o heš kriptografskoj funkciji, termin "nepovratnost" se generalno ne koristi. Umesto toga, govorimo o "otpornosti na preimage," što znači da je za bilo koje dato $y$ teško pronaći $x$ takvo da je $h(x) = y$. Ova otpornost na preimage je zagarantovana algebarskom složenošću i jakom nelinearnošću operacija koje se izvode u funkciji kompresije, kao i gubitkom određenih informacija u procesu. Na primer, za dati rezultat sabiranja po modulu, postoji nekoliko mogućih operanada:


$$

3+2 \mod 10 = 5 \\
7+8 \mod 10 = 5 \\
5+10 \mod 10 = 5


$$


U ovom primeru, znajući samo korišćeni modulo (10) i rezultat (5), ne može se sa sigurnošću odrediti koji su tačni operandi korišćeni u sabiranju. Kaže se da postoji više kongruencija modulo 10.


Za operaciju XOR suočavamo se sa istim problemom. Setite se tabele istinitosti za ovu operaciju: bilo koji 1-bitni izlaz može biti određen sa dve različite ulazne konfiguracije koje imaju potpuno istu verovatnoću da budu tačne vrednosti. Stoga, ne može se sa sigurnošću odrediti operandi XOR-a znajući samo njegov rezultat. Ako povećamo veličinu operanada XOR-a, znajući samo rezultat broj mogućih ulaza eksponencijalno raste. Štaviše, XOR se često koristi zajedno sa drugim operacijama na nivou bita, kao što je operacija $\text{RotR}$, koje dodaju još više mogućih interpretacija rezultatu.


Funkcija kompresije takođe koristi operaciju $\text{ShR}$. Ova operacija uklanja deo osnovnih informacija, koje je kasnije nemoguće povratiti. Još jednom, ne postoji algebarski način da se ova operacija obrne. Sve ove operacije jednosmernog gubitka informacija koriste se vrlo često u funkcijama kompresije. Broj mogućih ulaza za dati izlaz je stoga gotovo beskonačan, a svaki pokušaj obrnutog izračunavanja doveo bi do jednačina sa veoma velikim brojem nepoznatih, koje bi eksponencijalno rasle na svakom koraku.


Konačno, za karakteristiku otpornosti na kolizije, nekoliko parametara dolazi u igru. Predobrada originalne poruke igra ključnu ulogu. Bez ove predobrade, moglo bi biti lakše pronaći kolizije. Iako, teoretski, kolizije postoje (zbog principa fioka), sama struktura heš funkcije, u kombinaciji sa prethodno navedenim svojstvima, čini verovatnoću pronalaženja kolizije izuzetno niskom.

Da bi funkcija heš bila otporna na sudare, neophodno je da:



- je izlaz nepredvidiv: Svaka predvidljivost može biti iskorišćena za pronalaženje kolizija brže nego sa napadom silovite pretrage. Funkcija osigurava da svaki bit izlaza zavisi na složen način od ulaza. Drugim rečima, funkcija je dizajnirana tako da svaki bit konačnog rezultata ima nezavisnu verovatnoću da bude 0 ili 1, čak i ako ta nezavisnost nije apsolutna u praksi.
- Distribucija heševa je pseudo-slučajna: Ovo osigurava da su heševi ravnomerno raspoređeni.
- Veličina heša je značajna: što je veći mogući prostor za rezultate, to je teže pronaći koliziju.


Kriptografi dizajniraju ove funkcije procenjujući najbolje moguće napade za pronalaženje kolizija, a zatim prilagođavaju parametre kako bi ovi napadi postali neefikasni.


### Merkle-Damgård Konstrukcija


Struktura SHA256 zasnovana je na Merkle-Damgård konstrukciji, koja omogućava transformisanje kompresione funkcije u heš funkciju koja može obrađivati poruke proizvoljne dužine. Ovo je upravo ono što smo videli u ovom poglavlju.


Međutim, neke stare heš funkcije kao što su SHA1 ili MD5, koje koriste ovu specifičnu konstrukciju, su ranjive na napade produženja dužine. Ovo je tehnika koja omogućava napadaču koji zna heš poruke $M$ i dužinu $M$ (bez poznavanja same poruke) da izračuna heš vrednost poruke $M'$ formirane spajanjem $M$ sa dodatnim sadržajem.


SHA256, čak iako koristi isti tip konstrukcije, teoretski je otporan na ovu vrstu napada, za razliku od SHA1 i MD5. Ovo bi moglo objasniti misteriju dvostrukog heširanja implementiranog kroz Bitcoin od strane Satoshi Nakamota. Da bi izbegao ovu vrstu napada, Satoshi je možda preferirao da koristi dvostruki SHA256:


$$

\text{HASH256}(m) = \text{SHA256}(\text{SHA256}(m))


$$


Ovo poboljšava sigurnost protiv potencijalnih napada povezanih sa Merkle-Damgård konstrukcijom, ali ne povećava sigurnost procesa heširanja u smislu otpornosti na kolizije. Štaviše, čak i da je SHA256 bio ranjiv na ovu vrstu napada, to ne bi imalo ozbiljan uticaj, jer svi slučajevi upotrebe heš funkcija u Bitcoin-u uključuju javne podatke. Međutim, napad produženja dužine mogao bi biti koristan za napadača samo ako su heširani podaci privatni i korisnik je koristio heš funkciju kao mehanizam autentifikacije za te podatke, slično kao MAC (kod za autentikaciju poruke - Message Authentication Code). Stoga, implementacija dvostrukog heširanja ostaje misterija u dizajnu Bitcoin-a.

Sada kada smo detaljno pogledali kako funkcionišu heš funkcije, posebno SHA256, koja se intenzivno koristi u Bitcoin-u, fokusiraćemo se konkretnije na algoritme kriptografske derivacije koje se koriste na nivou aplikacije, posebno na derivaciju ključeva za vaš novčanik.


## Algoritmi korišćeni za izvođenje


<chapterId>cc668121-7789-5e99-bf5e-1ba085f4f5f2</chapterId>


Na aplikacionom nivou Bitcoin-a, pored heš funkcija, koriste se kriptografski algoritmi derivacije koji služe da se iz početnih podataka naprave nove, kriptografski bezbedne vrednosti. Iako se ovi algoritmi oslanjaju na heš funkcije, služe različitim svrhama, posebno u smislu autentifikacije i generisanja ključeva. Ovi algoritmi zadržavaju neke od karakteristika heš funkcija, kao što su ireverzibilnost, otpornost na manipulacije i otpornost na kolizije.


U Bitcoin novčanicima, uglavnom se koriste 2 algoritma derivacije:



- **HMAC (_Hash-based Message Authentication Code_)**
- **PBKDF2 (_Password-Based Key Derivation Function 2_)**


Zajedno ćemo istražiti funkcionisanje i ulogu svakog od njih.


### HMAC-SHA512


HMAC je kriptografski algoritam koji izračunava autentifikacioni kod na osnovu kombinacije heš funkcije i tajnog ključa. Bitcoin koristi HMAC-SHA512, varijantu HMAC-a koja koristi SHA512 heš funkciju. Već smo videli u prethodnom poglavlju da je SHA512 deo iste porodice heš funkcija kao i SHA256, ali proizvodi 512-bitni izlaz.


Evo njegove opšte operativne šeme sa $m$ kao ulaznom porukom i $K$ kao tajnim ključem:


![CYP201](assets/fr/011.webp)


Hajde da detaljnije proučimo šta se dešava u ovoj HMAC-SHA512 crnoj kutiji. Funkcija HMAC-SHA512 sa:



- $m$: proizvoljno velika poruka koju bira korisnik (prvi unos);
- $K$: proizvoljni tajni ključ koji bira korisnik (drugi unos);
- $K'$: ključ $K$ prilagođen veličini $B$ blokova heš funkcije (1024 bita za SHA512, ili 128 bajtova);
- $\text{SHA512}$: SHA512 heš funkcija;
- $\oplus$: XOR (isključivo ILI) operacija;
- $\Vert$: operator za konkatenaciju, povezuje nizove bitova od kraja do kraja;
- $\text{opad}$: konstanta sastavljena od bajta $0x5c$ ponovljenog 128 puta
- $\text{ipad}$: konstanta sastavljena od bajta $0x36$ ponovljenog 128 puta.


Pre nego što se izračuna HMAC, neophodno je izjednačiti ključ i konstante prema dužini bloka $B$. Na primer, ako je ključ $K$ kraći od 128 bajtova, dopunjava se nulama da dostigne dužinu $B$. Ako je $K$ duži od 128 bajtova, kompresuje se koristeći SHA512, a zatim se dodaju nule dok ne dostigne 128 bajtova. Na ovaj način se dobija izjednačen ključ nazvan $K'$. Vrednosti $\text{opad}$ i $\text{ipad}$ se dobijaju ponavljanjem njihovog osnovnog bajta ($0x5c$ za $\text{opad}$, $0x36$ za $\text{ipad}$) dok se ne dostigne veličina $B$. Tako, sa $B = 128$ bajtova, imamo:


$$

\text{opad} = \underbrace{0x5c5c\ldots5c}\_{128 \  \text{bytes}}


$$


Kada je predobrada završena, HMAC-SHA512 algoritam je definisan sledećom jednačinom:


$$

\text{HMAC-SHA512}(K,m) = \text{SHA512} \left( (K' \oplus \text{opad}) \parallel \text{SHA512} \left( (K' \oplus \text{ipad}) \parallel m \right) \right)


$$


Ova jednačina je razložena na sledeće korake:



- prilagođeni ključ $K'$ XOR sa $\text{ipad}$ da bi se dobio $\text{iKpad}$;
- prilagođeni ključ $K'$ XOR sa $\text{opad}$ da bi se dobio $\text{oKpad}$;
- Konkatenirajte $\text{iKpad}$ sa porukom $m$.
- Heširaj ovaj rezultat sa SHA512 da bi se dobio privremeni heš $H_1$.
- Konkateniraj $\text{oKpad}$ sa $H_1$.
- Heširaj ovaj rezultat sa SHA512 da bi se dobio konačni rezultat $H_2$.


Ovi koraci se mogu šematski rezimirati na sledeći način:


![CYP201](assets/fr/012.webp)


HMAC se koristi u Bitcoin-u posebno za derivaciju ključeva u HD (Hijerarhijski Deterministički) novčanicima (o tome ćemo detaljnije govoriti u narednim poglavljima) i kao komponenta PBKDF2.


### PBKDF2


PBKDF2 (_Password-Based Key Derivation Function 2_) je algoritam za derivaciju ključeva dizajniran da poboljša sigurnost lozinki. Algoritam primenjuje pseudo-slučajnu funkciju (ovde HMAC-SHA512) na lozinku i kriptografski salt (nasumični niz koji se koristi kako bi heširane vrednosti bile jedinstvene čak i kada su ulazni podaci isti), a zatim ponavlja ovu operaciju određeni broj puta kako bi proizveo izlazni ključ.


U Bitcoin-u, PBKDF2 se koristi za generisanje seed-a HD novčanika iz bezbednosne fraze i sigurnosne fraze (passphrase-a) (ali o tome ćemo detaljnije govoriti u narednim poglavljima).


PBKDF2 proces je sledeći, sa:



- $m$: korisnikova bezbednosna fraza;
- $s$: opciona sigurnosna lozinka za povećanje sigurnosti (prazno polje ako je nema);
- $n$: broj iteracija funkcije, u našem slučaju, to je 2048.


Funkcija PBKDF2 je definisana iterativno. Svaka iteracija uzima rezultat prethodne, primenjuje HMAC-SHA512 na njega, i kombinuje uzastopne rezultate kako bi proizvela konačni ključ:


$$

\text{PBKDF2}(m, s) = \text{HMAC-SHA512}^{2048}(m, s)


$$


Šema PBKDF2 može biti predstavljen na sledeći način:


![CYP201](assets/fr/013.webp)


U ovom poglavlju smo istražili funkcije HMAC-SHA512 i PBKDF2, koje koriste heš funkcije kako bi osigurale integritet i sigurnost derivacija ključeva u Bitcoin protokolu. U sledećem delu ćemo se baviti digitalnim potpisima, još jednom kriptografskom metodom koja se široko koristi u Bitcoin-u.


# Digitalni potpisi


<partId>76b58a00-0c18-54b9-870d-6b7e34029db8</partId>


## Digitalni potpisi i eliptičke krive


<chapterId>c9dd9672-6da1-57f8-9871-8b28994d4c1a</chapterId>


Druga kriptografska metoda korišćena u Bitcoin-u uključuje algoritme digitalnog potpisa. Hajde da istražimo šta to podrazumeva i kako funkcioniše.


### Bitcoini, UTXO-i i uslovi trošenja


Termin "_novčanik_" u Bitcoin-u može biti prilično zbunjujući za početnike. Zaista, ono što se naziva Bitcoin novčanikom je softver koji ne drži direktno vaše bitkojne, za razliku od fizičkog novčanika koji može držati kovanice ili novčanice. Bitkoini su jednostavno jedinice obračuna. Ova jedinica obračuna je predstavljena **UTXO-om** (_Unspent Transaction Outputs_), što su neiskorišćeni izlazi transakcija. Ako ovi izlazi nisu iskorišćeni, to znači da pripadaju korisniku. UTXO-ovi su, na neki način, delovi bitkojna, promenljive veličine, koji pripadaju korisniku.


Bitcoin protokol je distribuiran i funkcioniše bez centralnog autoriteta. Stoga, nije kao tradicionalni bankarski zapisi, gde su evri koji pripadaju vama jednostavno povezani sa vašim ličnim identitetom. U Bitcoin-u, vaši UTXO-ovi pripadaju vama jer su zaštićeni uslovima trošenja specificiranim u Script jeziku. Da pojednostavimo, postoje dve vrste skripti: skripta zaključavanja (_scriptPubKey_), koja štiti UTXO, i skripta otključavanja (_scriptSig_), koja omogućava otključavanje UTXO-a i time trošenje bitcoin jedinica koje predstavlja.

U početku Bitcoin je funkcionisao sa P2PK skriptama koja uključuje korišćenje javnog ključa za zaključavanje sredstava, navodeći u _scriptPubKey_ da osoba koja želi da potroši ovaj UTXO mora obezbediti važeći potpis sa privatnim ključem koji odgovara ovom javnom ključu. Da bi se otključao ovaj UTXO, potrebno je obezbediti važeći potpis u _scriptSig_. Kao što njihova imena sugerišu, javni ključ je poznat svima jer se emituje na blokčejnu, dok je privatni ključ poznat samo legitimnom vlasniku sredstava.

Ovo je osnovni princip funkcionisanja Bitcoin-a, ali s vremenom je ova operacija postala složenija. Prvo, Satoshi je takođe uveo P2PKH skripte, koje koriste prijemnu adresu u _scriptPubKey_, što predstavlja heš javnog ključa. Zatim je sistem postao još složeniji dolaskom SegWit-a, a potom i Taproot-a. Međutim, opšti princip ostaje u osnovi isti: javni ključ ili njegova reprezentacija se koristi za zaključavanje UTXO-a, a odgovarajući privatni ključ je potreban da bi se oni otključali i time potrošili.


Korisnik koji želi da izvrši Bitcoin transakciju mora stoga kreirati digitalni potpis koristeći svoj privatni ključ nad tom transakcijom. Potpis može biti verifikovan od strane drugih učesnika mreže. Ako je validan, to znači da je korisnik koji inicira transakciju zaista vlasnik privatnog ključa, a samim tim i vlasnik bitkoina koje želi da potroši. Drugi korisnici tada mogu prihvatiti i propagirati transakciju.


Kao rezultat toga, korisnik koji poseduje bitkoine zaključane javnim ključem mora pronaći način da bezbedno čuva ono što omogućava otključavanje njihovih sredstava: privatni ključ. Bitcoin novčanik je upravo uređaj koji će vam omogućiti da lako čuvate sve svoje ključeve bez da im drugi ljudi imaju pristup. Stoga je više nalik na privezak za ključeve nego na novčanik.


Matematička veza između javnog ključa i privatnog ključa, kao i mogućnost izvršavanja potpisa kako bi se dokazalo posedovanje privatnog ključa bez njegovog otkrivanja, omogućeni su algoritmom digitalnog potpisa. U Bitcoin protokolu koriste se dva algoritma digitalnog potpisa: **ECDSA** (_Elliptic Curve Digital Signature Algorithm_) i **Schnorr signature scheme**. ECDSA je protokol digitalnog potpisa korišćen u Bitcoin-u od samog početka. Schnorr je noviji u Bitcoin-u, jer je uveden u novembru 2021. sa ažuriranjem Taproot-a.

Ova dva algoritma su prilično slična u svojim mehanizmima. Obe su zasnovane na kriptografiji eliptičkih krivih. Glavna razlika između ovih protokola leži u strukturi potpisa i nekim specifičnim matematičkim svojstvima. Stoga ćemo proučiti funkcionisanje ovih algoritama, počevši od najstarijeg: ECDSA.


### Kriptografija eliptičkih krivih


Kriptografija eliptičkih krivih (ECC) je skup algoritama koji koriste eliptičku krivu zbog njenih različitih matematičkih i geometrijskih svojstava u kriptografske svrhe. Sigurnost ovih algoritama oslanja se na težinu problema diskretnog logaritma na eliptičkim krivama. Eliptičke krive se posebno koriste za razmenu ključeva, asimetričnu enkripciju ili za kreiranje digitalnih potpisa.


Važna osobina ovih krivih je da su simetrične u odnosu na x-osu. Dakle, svaka nevertikalna linija koja seče krivu u dve različite tačke će uvek preseći krivu u trećoj tački. Štaviše, svaka tangenta na krivu u nesingularnoj tački će preseći krivu u drugoj tački. Ove osobine će biti korisne za definisanje operacija na krivoj.


Evo prikaza eliptičke krive nad poljem realnih brojeva:


![CYP201](assets/fr/014.webp)


Svaka eliptička kriva definisana je jednačinom oblika:


$$

y^2 = x^3 + ax + b


$$


### secp256k1


Da bi se koristio ECDSA ili Schnorr, potrebno je izabrati parametre eliptičke krive, odnosno vrednosti $a$ i $b$ u jednačini krive. Postoje različiti standardi eliptičkih krivih za koje se smatra da su kriptografski sigurni. Najpoznatija je _secp256r1_ kriva, definisana i preporučena od strane NIST-a (_National Institute of Standards and Technology_).


Uprkos tome, Satoshi Nakamoto, pronalazač Bitcoin-a, odlučio je da ne koristi ovu krivu. Razlog za ovu odluku je nepoznat, ali neki veruju da je želeo da pronađe alternativu jer parametri ove krive potencijalno mogu sadržati namerno ubačenu slabost, skrivenu ranjivost, koja omogućava zaobilaženje standardnih bezbednosnih mehanizama — često bez znanja korisnika. Umesto toga, Bitcoin protokol koristi standardnu **_secp256k1_** krivu. Ova kriva je definisana parametrima $a = 0$ i $b = 7$. Njena jednačina je stoga:


$$

y^2 = x^3 + 7


$$


Njegova grafička reprezentacija u skupu realnih brojeva izgleda ovako:


![CYP201](assets/fr/015.webp)


Međutim, u kriptografiji radimo sa konačnim skupovima brojeva. Tačnije, radimo na konačnom polju $\mathbb{F}_p$, koje je polje celih brojeva modulo prosti broj $p$.

**Definicija**: Prosti broj je prirodan ceo broj veći ili jednak od 2 koji ima samo dva različita pozitivna cela delitelja: 1 i samog sebe. Na primer, broj 7 je prost broj jer se može deliti samo sa 1 i 7. S druge strane, broj 8 nije prost jer se može deliti sa 1, 2, 4 i 8.

U Bitcoin-u, prost broj $p$ korišćen za definisanje konačnog polja je veoma veliki. Izabran je na takav način da je red polja (tj. broj elemenata u $\mathbb{F}_p$) dovoljno veliki da obezbedi kriptografsku sigurnost.


Prosti broj $p$ koji se koristi je:


```text
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
```


U decimalnoj notaciji, ovo odgovara:


$$

p = 2^{256} - 2^{32} - 977


$$


Dakle, jednačina naše eliptičke krive je zapravo:


$$

y^2 \equiv x^3 + 7 \mod p


$$


S obzirom na to da je ova kriva definisana nad konačnim poljem $\mathbb{F}_p$, ona više ne liči na kontinuiranu krivu već na diskretan skup tačaka. Na primer, evo kako izgleda kriva korišćena u Bitcoin-u za veoma malo $p = 17$:


![CYP201](assets/fr/016.webp)


U ovom primeru, namerno sam ograničio konačno polje na $p = 17$ iz obrazovnih razloga, ali treba zamisliti da je ono korišćeno u Bitcoin-u neizmerno veće, skoro $2^{256}$.


Koristimo konačno polje celih brojeva modulo $p$ kako bismo osigurali tačnost operacija na krivi. Naime, eliptičke krive nad poljem realnih brojeva podložne su netačnostima zbog grešaka zaokruživanja tokom računskih proračuna. Ako se na krivi izvrši veliki broj operacija, te greške se akumuliraju i konačni rezultat može biti netačan ili teško ponovljiv. Isključiva upotreba pozitivnih celih brojeva osigurava savršenu tačnost proračuna i time ponovljivost rezultata.


Matematika eliptičkih krivih nad konačnim poljima je analogna onoj nad poljem realnih brojeva, s prilagodbom da se sve operacije izvode modulo $p$. Da bismo pojednostavili objašnjenja, u narednim poglavljima ćemo nastaviti ilustrovati pojmove koristeći krivu definisanu nad realnim brojevima, imajući na umu da je u praksi kriva definisana nad konačnim poljem.


Ako želite da saznate više o matematičkim osnovama moderne kriptografije, preporučujem da pogledate i ovaj drugi kurs na Plan ₿ Network:


https://planb.network/courses/d2fd9fc0-d9ed-4a87-9fa3-0fdbb3937e28

## Izračunavanje javnog ključa iz privatnog ključa


<chapterId>fcb2bd58-5dda-5ecf-bb8f-ad1a0561ab4a</chapterId>

Kao što je ranije viđeno, algoritmi digitalnog potpisa u Bitcoin-u zasnivaju se na paru privatnih i javnih ključeva koji su matematički povezani. Hajde da zajedno istražimo šta je ta matematička veza i kako se oni generišu.


### Privatni ključ


Privatni ključ je jednostavno nasumičan ili pseudo-nasumičan broj. U slučaju Bitcoin-a, ovaj broj je veličine 256 bita. Broj mogućnosti za Bitcoin privatni ključ je stoga teoretski $2^{256}$.


**Napomena**: "Pseudo-slučajan broj" je broj koji ima osobine bliske onima pravog slučajnog broja, ali se generiše determinističkim algoritmom.


Međutim, u praksi, postoji samo $n$ različitih tačaka na našoj eliptičnoj krivoj secp256k1, gde je $n$ red generatora tačke $G$ krive. Videćemo kasnije čemu odgovara ovaj broj, ali jednostavno zapamtite da je važeći privatni ključ ceo broj između $1$ i $n-1$, znajući da je $n$ broj blizak, ali malo manji od $2^{256}$. Dakle, postoje neki 256-bitni brojevi koji nisu važeći da budu privatni ključevi u Bitcoin-u, konkretno, svi brojevi između $n$ i $2^{256}$. Ako generisanje slučajnog broja (privatnog ključa) proizvede vrednost $k$ takvu da je $k \geq n$, ta vrednost se smatra nevažećom i mora se generisati nova slučajna vrednost.


Broj mogućnosti za privatni ključ Bitcoin-a je stoga oko $n$, što je broj blizak $1.158 \times 10^{77}$. Ovaj broj je toliko veliki da, ako nasumično izaberete privatni ključ, statistički je gotovo nemoguće da bude isti kao privatni ključ drugog korisnika. Da biste dobili predstavu o razmeri, broj mogućih privatnih ključeva u Bitcoin-u je reda veličine procenjenom broju atoma u posmatranom univerzumu.


Kao što ćemo videti u narednim poglavljima, danas većina privatnih ključeva korišćenih u Bitcoin-u nije generisana nasumično, već je rezultat determinističke derivacije iz bezbednosne fraze, koja je sama po sebi pseudo-nasumična (ovo je čuvena fraza od 12 ili 24 reči). Ova informacija ne menja ništa za upotrebu algoritama za potpisivanje kao što je ECDSA, ali pomaže da se preusmeri naš fokus na popularizaciju Bitcoina.


U ostatku objašnjenja, privatni ključ će biti označen malim slovom $k$.


### Javni ključ


Javni ključ je tačka na eliptičkoj krivi, označena velikim slovom $K$, i izračunava se iz privatnog ključa $k$. Ova tačka $K$ je predstavljena parom koordinata $(x, y)$ na eliptičkoj krivi, pri čemu je svaka koordinata ceo broj modulo $p$, prost broj koji definiše konačno polje $\mathbb{F}_p$.

U praksi, nekompresovani javni ključ je predstavljen sa 520 bita (ili 65 bajtova), što odgovara dvema 256-bitnim brojevima ($x$ i $y$) postavljenim jedan za drugim, sa prefiksom od 8 bita $0x04$.


Međutim, moguće je predstaviti javni ključ i u kompresovanom obliku koristeći samo 33 bajta (264 bita) tako što će da sadrži samo apscisa $x$ naše tačke na krivi i bajt koji označava paritet $y$. Ovo je poznato kao kompresovani javni ključ. Više ću o tome govoriti u poslednjim poglavljima ove obuke. Ali ono što treba da zapamtite je da je javni ključ $K$ tačka opisana sa $x$ i $y$.


Da bismo izračunali tačku $K$ koja odgovara našem javnom ključu, koristimo operaciju skalarnog množenja na eliptičkim krivama, definisanu kao ponovljeno sabiranje ($k$ puta) generatora tačke $G$:


$$

K = k \cdot G


$$


gde:



- $k$ je privatni ključ (slučajan ceo broj između $1$ i $n-1$);
- $G$ je generišuća tačka eliptičke krive koju koriste svi učesnici Bitcoin mreže;
- $\cdot$ predstavlja skalarno množenje na eliptičnoj krivi, što je ekvivalentno dodavanju tačke $G$ samoj sebi $k$ puta.


Činjenica da je tačka $G$ zajednička za sve javne ključeve u Bitcoin-u omogućava nam da budemo sigurni da će isti privatni ključ $k$ uvek dati isti javni ključ $K$:


![CYP201](assets/fr/017.webp)


Glavna karakteristika ove operacije je da je to jednosmerna funkcija. Lako je izračunati javni ključ $K$ znajući privatni ključ $k$ i generator tačku $G$, ali je praktično nemoguće izračunati privatni ključ $k$ znajući samo javni ključ $K$ i generator tačku $G$. Pronalaženje $k$ iz $K$ i $G$ svodi se na rešavanje problema diskretnog logaritma na eliptičkim krivama, matematički teškog problema za koji nije poznat efikasan algoritam. Čak ni najmoćniji trenutni kalkulatori nisu u stanju da reše ovaj problem u razumnom vremenu.


![CYP201](assets/fr/018.webp)


### Dodavanje i udvostručavanje tačaka na eliptičkim krivama


Koncept sabiranja na eliptičkim krivama je definisan geometrijski. Ako imamo dve tačke $P$ i $Q$ na krivi, operacija $P + Q$ se izračunava povlačenjem prave koja prolazi kroz $P$ i $Q$. Ova prava će nužno preseći krivu u trećoj tački $R'$. Zatim uzimamo refleksiju ove tačke u odnosu na x-osu da bismo dobili tačku $R$, koja je rezultat sabiranja:


$$

P + Q = R


$$


Grafički, ovo se može predstaviti na sledeći način:


![CYP201](assets/fr/019.webp)


Za udvostručavanje tačke, što je operacija $P + P$, povlačimo tangentu na krivu u tački $P$. Ova tangenta seče krivu u drugoj tački $S'$. Zatim uzimamo refleksiju ove tačke u odnosu na x-osu da bismo dobili tačku $S$, koja je rezultat udvostručavanja:


$$

2P = S


$$


Grafički, ovo je prikazano kao:


![CYP201](assets/fr/020.webp)


Korišćenjem ovih operacija sabiranja i udvostručavanja, možemo izvršiti skalarno množenje tačke celim brojem $k$, označeno sa $kP$, izvođenjem ponovljenih udvostručavanja i sabiranja.


Na primer, pretpostavimo da smo izabrali privatni ključ $k = 4$. Da bismo izračunali odgovarajući javni ključ, izvršavamo:


$$

K = k \cdot G = 4G


$$


Grafički, ovo odgovara izvođenju niza sabiranja i udvostručavanja:



- Izračunajte $2G$ udvostručavanjem $G$.
- Izračunajte $4G$ udvostručavanjem $2G$.


![CYP201](assets/fr/021.webp)


Ako želimo, na primer, da izračunamo tačku $3G$, prvo moramo izračunati tačku $2G$ udvostručavanjem tačke $G$, zatim dodati $G$ i $2G$. Da bismo dodali $G$ i $2G$, jednostavno nacrtamo pravu koja povezuje ove dve tačke, pronađemo jedinstvenu tačku $-3G$ na preseku između ove prave i eliptičke krive, a zatim odredimo $3G$ kao suprotnost od $-3G$.


Imaćemo:


$$

G + G = 2G


$$


$$

2G + G = 3G


$$


Grafički, ovo bi bilo predstavljeno na sledeći način:


![CYP201](assets/fr/022.webp)


### Jednosmerna funkcija


Zahvaljujući ovim operacijama, možemo razumeti zašto je lako izvesti javni ključ iz privatnog ključa, ali je obrnuto praktično nemoguće.


Hajde da se vratimo na naš pojednostavljeni primer. Sa privatnim ključem $k = 4$. Da bismo izračunali pripadajući javni ključ, izvršavamo:


$$
K = k \cdot G = 4G
$$


Tako smo mogli lako izračunati javni ključ $K$ znajući $k$ i $G$.


Sada, ako neko zna samo javni ključ $K$, suočen je sa problemom diskretnog logaritma: pronalaženje $k$ takvog da je $K = k \cdot G$. Ovaj problem se smatra teškim jer ne postoji efikasan algoritam za njegovo rešavanje na eliptičkim krivama. Ovo osigurava sigurnost ECDSA i Schnorr algoritama.


Naravno, u ovom pojednostavljenom primeru sa $k = 4$, bilo bi moguće pronaći $k$ metodom pokušaja i greške, jer je broj mogućnosti mali. Međutim, u praksi, $k$ je 256-bitni ceo broj, što čini broj mogućnosti astronomski velikim (oko $1.158 \times 10^{77}$). Stoga je neizvodljivo pronaći $k$ metodom silovite pretrage (bruteforce).


## Potpisivanje privatnim ključem


<chapterId>bb07826f-826e-5905-b307-3d82001fb778</chapterId>


Sada kada znate kako da izvedete javni ključ iz privatnog ključa, već možete primati bitkojne koristeći ovaj par ključeva kao uslov za trošenje. Ali kako ih potrošiti? Da biste potrošili bitkoine, potrebno je da otključate _scriptPubKey_ priložen uz vaš UTXO kako biste dokazali da ste zaista njegov legitimni vlasnik. Da biste to uradili, morate proizvesti potpis $s$ koji odgovara javnom ključu $K$ prisutnom u _scriptPubKey_ koristeći privatni ključ $k$ koji je prvobitno korišćen za izračunavanje $K$. Digitalni potpis je tako neoboriv dokaz da posedujete privatni ključ povezan sa javnim ključem koji tvrdite da imate.


### Parametri eliptičke krive


Da bi se izvršio digitalni potpis, svi učesnici moraju prvo da se dogovore o parametrima korišćene eliptičke krive. U slučaju Bitcoin-a, parametri **secp256k1** su sledeći:


Konačno polje $\mathbb{Z}_p$ definisano sa:


$$
p = 2^{256} - 2^{32} - 977
$$


```text
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
```


$p$ je veoma veliki prost broj malo manji od $2^{256}$.


Eliptička kriva $y^2 = x^3 + ax + b$ nad $\mathbb{Z}_p$ definisana sa:


$$
a = 0, \quad b = 7
$$


Tačka generatora ili početna tačka $G$:


```text
G = 0x0279BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
```


Ovaj broj je kompresovani oblik koji daje samo apscisu tačke $G$. Prefiks `02` na početku određuje koja od dve vrednosti koje imaju ovu apscisu $x$ treba da se koristi kao generišuća tačka.

Red grupe $n$ (broj postojećih tačaka) generišuće tačke $G$  i kofaktor $h$:


```text
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
```


$n$ je veoma veliki broj malo manji od $p$.


$$
h=1
$$


$h$ je kofaktor ili broj podgrupa. Neću ovde elaborirati šta to predstavlja, jer je prilično složeno, a u slučaju Bitcoin-a, ne moramo ga uzimati u obzir pošto je jednak $1$.


Sve ove informacije su javne i poznate svim učesnicima. Zahvaljujući njima, korisnici mogu napraviti digitalni potpis i verifikovati ga.


### Potpis sa ECDSA


ECDSA algoritam omogućava korisniku da potpiše poruku koristeći svoj privatni ključ, na takav način svako ko zna odgovarajući javni ključ može da proveri validnost potpisa, a da privatni ključ nikada ne bude otkriven. U kontekstu Bitcoin-a, poruka koja se potpisuje zavisi od _sighash_-a koji korisnik izabere. Upravo taj _sighash_ će odrediti koji delovi transakcije su pokriveni potpisom. O tome ću više govoriti u sledećem poglavlju.


Evo koraka za generisanje ECDSA potpisa:


Prvo, izračunavamo heš ($e$) poruke koja treba da bude potpisana. Poruka $m$ se stoga propušta kroz kriptografsku heš funkciju, obično SHA256 ili dvostruki SHA256 u slučaju Bitcoin-a:


$$
e = \text{HASH}(m)
$$


Zatim, izračunavamo nonce (broj koji se koristi samo jednom). U kriptografiji, nonce je jednostavno broj generisan na slučajan ili pseudo-slučajan način koji se koristi samo jednom. To jest, svaki put kada se napravi novi digitalni potpis sa ovim parom ključeva, biće veoma važno koristiti drugačiji nonce, inače će to ugroziti sigurnost privatnog ključa. Stoga je dovoljno odrediti slučajan i jedinstven ceo broj $r$ takav da $1 \leq r \leq n-1$, gde je $n$ red generišuće tačke $G$ eliptičke krive.


Zatim ćemo izračunati tačku $R$ na eliptičnoj krivoj sa koordinatama $(x_R, y_R)$ tako da:


$$
R = r \cdot G
$$


Izvlačimo vrednost apscise tačke $R$ ($x_R$). Ova vrednost predstavlja prvi deo potpisa. I na kraju, izračunavamo drugi deo potpisa $s$ na sledeći način:


$$
s = r^{-1} \left( e + k \cdot x_R \right) \mod n
$$


gde:



- $r^{-1}$ je modularni inverz od $r$ po modulu $n$, to jest, ceo broj takav da $r \cdot r^{-1} \equiv 1 \mod n$;
- $k$ je korisnikov privatni ključ;
- $e$ je heš poruke;
- $n$ je red generatora tačke $G$ eliptičke krive.


Potpis je tada jednostavno konkatenacija $x_R$ i $s$:


$$
\text{SIG} = x_R \Vert s
$$


### Verifikacija ECDSA potpisa


Da bi verifikovao potpis $(x_R, s)$, svako ko zna javni ključ $K$ i parametre eliptičke krive može postupiti na sledeći način:


Prvo, proverite da li su $x_R$ i $s$ unutar intervala $[1, n-1]$. Ovo osigurava da potpis poštuje matematička ograničenja eliptičke grupe. Ako to nije slučaj, verifikator odmah odbacuje potpis kao nevažeći.


Zatim, izračunaj heš poruke:


$$
e = \text{HASH}(m)
$$


Izračunajte modularni inverz od $s$ modulo $n$:


$$
s^{-1} \mod n
$$


Izračunaj dve skalarne vrednosti $u_1$ i $u_2$ na sledeći način:


$$
\begin{align*}
u_1 &= e \cdot s^{-1} \mod n \\
u_2 &= x_R \cdot s^{-1} \mod n
\end{align*}
$$


I na kraju, izračunajte tačku $V$ na eliptičnoj krivoj takvu da:


$$
V = u_1 \cdot G + u_2 \cdot K
$$


Potpis je važeći samo ako je $x_V \equiv x_R \mod n$, gde je $x_V$ $x$ koordinata tačke $V$. Zaista, kombinovanjem $u_1 \cdot G$ i $u_2 \cdot K$, dobija se tačka $V$ koja, ako je potpis važeći, mora odgovarati tački $R$ korišćenoj tokom potpisa (modulo $n$).


### Potpisivanje sa Schnorr protokolom


Šema Schnorr potpisa je alternativa ECDSA koja nudi mnoge prednosti. Moguće ju je koristiti u Bitcoin-u od 2021. godine i uvođenja Taproot-a, sa šablonima skripti P2TR. Kao i ECDSA, šema Schnorr omogućava potpisivanje poruke korišćenjem privatnog ključa, na takav način da potpis može biti verifikovan od strane bilo koga ko zna odgovarajući javni ključ.

U slučaju Schnorra, koristi se potpuno ista kriva kao kod ECDSA sa istim parametrima. Međutim, javni ključevi su predstavljeni malo drugačije u poređenju sa ECDSA. Naime, oni su određeni samo $x$ koordinatom tačke na eliptičnoj krivi. Za razliku od ECDSA, gde su kompresovani javni ključevi predstavljeni sa 33 bajta (sa prefiksnim bajtom koji označava paritet $y$), Schnorr koristi 32-bajtne javne ključeve, koji odgovaraju samo $x$ koordinati tačke $K$, i pretpostavlja se da je $y$ paran po defaultu. Ova pojednostavljena reprezentacija smanjuje veličinu potpisa i olakšava određene optimizacije u algoritmima za verifikaciju.

Javni ključ je tada $x$ koordinata tačke $K$:


$$
\text{pk} = K_x
$$


Prvi korak do generisanja potpisa je heš poruka. Ali za razliku od ECDSA, to se radi sa drugim vrednostima i koristi se heš funkcija kojoj je dodata oznaka (label) kako bi se izbegle kolizije u različitim kontekstima. Ova heš funkcija jednostavno podrazumeva dodavanje proizvoljne oznake ulazima heš funkcije zajedno sa podacima poruke.


![CYP201](assets/fr/023.webp)


Pored poruke, $x$ koordinata javnog ključa $K_x$, kao i tačka $R = r \cdot G$, izračunata iz nonce-a $r$ (koji je sam po sebi jedinstven ceo broj za svaki potpis, deterministički izračunat iz privatnog ključa i poruke kako bi se izbegle ranjivosti povezane sa ponovnom upotrebom nonce-a), takođe se prosleđuju u heš funkciju sa oznakom. Kao i za javni ključ, samo $x$ koordinata nonce tačke $R_x$ se zadržava da opiše tačku.


Rezultat ovog heširanja označen $e$ naziva se "izazov":


$$
e = \text{HASH}(\text{``BIP0340/challenge''}, R_x \Vert K_x \Vert m) \mod n
$$


Ovde, $\text{Hash}$ je SHA256 heš funkcija, a $\text{``BIP0340/challenge''}$ je specifična oznaka za heširanje.


Konačno, parametar $s$ se izračunava iz privatnog ključa $k$, nonce-a $r$, i izazova $e$ na sledeći način:


$$
s = (r + e \cdot k) \mod n
$$


Potpis je tada jednostavno par $R_x$ i $s$.


$$
\text{SIG} = R_x \Vert s
$$


### Verifikacija Schnorr potpisa


Verifikacija Schnorr potpisa je jednostavnija od verifikacije ECDSA potpisa. Ovo su koraci za verifikaciju potpisa $(R_x, s)$ sa javnim ključem $K_x$ i porukom $m$.

Prvo, proveravamo da li je $K_x$ validan ceo broj manji od $p$. Ako je to slučaj, pronalazimo odgovarajuću tačku na krivi sa parnim $K_y$. Takođe izdvajamo $R_x$ i $s$ razdvajanjem potpisa $\text{SIG}$. Zatim proveravamo da li je $R_x < p$ i $s < n$ (red krive).

Zatim, izračunavamo izazov $e$ na isti način kao izdavalac potpisa:


$$
e = \text{HASH}(\text{``BIP0340/challenge''}, R_x \Vert K_x \Vert m) \mod n
$$


Zatim, referentnu tačku na krivoj izračunavamo na sledeći način:


$$
R' = s \cdot G - e \cdot K
$$


Konačno, proveravamo da li je $R'_x = R_x$. Ako se dve x-koordinate poklapaju, tada je potpis $(R_x, s)$ zaista važeći sa javnim ključem $K_x$.


### Zašto ovo radi?


Potpisnik je izračunao $s = r + e \cdot k \mod n$, tako da bi $R' = s \cdot G - e \cdot K$ trebalo da bude jednako originalnoj tački $R$, zato što:


$$
s \cdot G = (r + e \cdot k) \cdot G = r \cdot G + e \cdot k \cdot G
$$


Pošto je $K = k \cdot G$, imamo $e \cdot k \cdot G = e \cdot K$. Dakle:


$$
R' = r \cdot G = R
$$


Dakle, imamo:


$$
R'_x = R_x
$$


### Prednosti Schnorr potpisa


Šema Schnorr potpisa nudi nekoliko prednosti za Bitcoin u odnosu na originalni ECDSA algoritam. Prvo, Schnorr omogućava agregaciju ključeva i potpisa. To znači da se više javnih ključeva može kombinovati u jedan ključ.


![CYP201](assets/fr/024.webp)


Isto tako, više potpisa može biti agregirano u jedan važeći potpis. Dakle, u slučaju transakcije sa više potpisa, skup učesnika može potpisati sa jednim potpisom i jednim agregiranim javnim ključem. Ovo značajno smanjuje troškove skladištenja i računanja za mrežu, jer svaki čvor treba da verifikuje samo jedan potpis.


![CYP201](assets/fr/025.webp)


Štaviše, agregacija potpisa poboljšava privatnost. Sa Schnorr-om, postaje nemoguće razlikovati transakciju sa višestrukim potpisom od standardne transakcije sa jednim potpisom. Ova homogenost otežava analizu blokčejna, jer ograničava mogućnost identifikacije novčanika.


Konačno, Schnorr takođe nudi mogućnost grupne verifikacije. Verifikovanjem više potpisa istovremeno, čvorovi mogu postići veću efikasnost, posebno za blokove koji sadrže mnogo transakcija. Ova optimizacija smanjuje vreme i resurse potrebne za validaciju bloka.

Takođe, Schnorr potpisi nisu podložni promenama, za razliku od potpisa proizvedenih sa ECDSA. To znači da napadač ne može da izmeni važeći potpis kako bi stvorio drugi važeći potpis za istu poruku i isti javni ključ. Ova ranjivost je prethodno bila prisutna u Bitcoin i značajno je sprečila sigurnu implementaciju Lightning Network-a. Ovaj propust za ECDSA je rešen sa SegWit softforkom 2017. godine, koji uključuje premeštanje potpisa u zasebnu bazu podataka od transakcija kako bi se sprečila njihova promenljivost.


### Zašto je Satoshi izabrao ECDSA?


Kao što smo videli, Satoshi je u početku odlučio da implementira ECDSA za digitalne potpise u Bitcoin-u. Ipak, takođe smo videli da je Schnorr superiorniji od ECDSA u mnogim aspektima, a ovaj protokol je kreirao Claus-Peter Schnorr 1989. godine, 20 godina pre izuma Bitcoin.


Pa, mi stvarno ne znamo zašto Satoshi nije izabrao to, ali verovatna hipoteza je da je ovaj protokol bio pod patentom do 2008. Iako je Bitcoin kreiran godinu dana kasnije, u januaru 2009, u to vreme nije postojala otvorena standardizacija za Schnorr potpise. Možda je Satoshi smatrao da je sigurnije koristiti ECDSA, koji je već bio široko korišćen i testiran u open-source softveru i imao nekoliko priznatih implementacija (posebno OpenSSL biblioteka korišćena do 2015. u Bitcoin Core-u, zatim zamenjena libsecp256k1 u verziji 0.10.0). Ili možda jednostavno nije bio svestan da će ovaj patent isteći 2008. U svakom slučaju, najverovatnija hipoteza izgleda da je povezana sa ovim patentom i činjenicom da je ECDSA imao dokazanu istoriju i bio lakši za implementaciju.


## Sighash indikatori


<chapterId>231c41a2-aff2-4655-9048-47b6d2d83d64</chapterId>


Kao što smo videli u prethodnim poglavljima, digitalni potpisi se često koriste za otključavanje skripte ulaza (input skripta). U procesu potpisivanja, neophodno je uključiti potpisane podatke u izračunavanje, označene u našim primerima kao poruka $m$. Ovi podaci, kada su jednom potpisani, ne mogu biti izmenjeni bez poništavanja potpisa. Zaista, bilo da se radi o ECDSA ili Schnorr, verifikator potpisa mora uključiti u svoje izračunavanje istu poruku $m$. Ako se razlikuje od poruke $m$ koju je inicijalno koristio potpisnik, rezultat će biti netačan i potpis će biti proglašen nevažećim. Tada se kaže da potpis pokriva određene podatke i na neki način ih štiti od neovlašćenih izmena.


### Šta je sighash indikator?


U specifičnom Bitcoin slučaju, videli smo da poruka $m$ odgovara transakciji. Međutim, u stvarnosti je to malo složenije. Zaista, zahvaljujući sighash indikatorima, moguće je odabrati specifične podatke unutar transakcije koji će biti pokriveni ili ne potpisom.

"Sighash indikator" je stoga parametar dodat svakom ulazu, omogućavajući određivanje komponenti transakcije koje su pokrivene pridruženim potpisom. Te komponente su ulazi i izlazi. Izbor sighash indikatora stoga određuje koji ulazi i koji izlazi transakcije su fiksirani potpisom i koji se još uvek mogu menjati bez poništavanja potpisa. Ovaj mehanizam omogućava da potpisi obuhvate podatke o transakciji u skladu sa namerama potpisnika.

Očigledno, kada je transakcija potvrđena na blokčejnu, postaje nepromenljiva, bez obzira na korišćene sighash indikatore. Mogućnost izmene putem sighash indikatora ograničena je na period između potpisivanja i potvrde.


Generalno, softverski novčanik vam ne nudi opciju da ručno modifikujete sighash indikator vaših ulaza kada kreirate transakciju. Podrazumevano, `SIGHASH_ALL` je postavljen. Lično, znam samo za Sparrow Wallet koji omogućava ovu modifikaciju uz pomoć korisničkog interfejsa.


### Koji su postojeći sighash indikatori u Bitcoin-u?


U Bitcoin-u, postoje pre svega 3 osnovna sighash indikatora:



- `SIGHASH_ALL` (`0x01`): Potpis se odnosi na sve ulaze i sve izlaze transakcije. Transakcija je tako u potpunosti pokrivena potpisom i više se ne može menjati. `SIGHASH_ALL` je najčešće korišćen sighash u svakodnevnim transakcijama kada neko jednostavno želi da izvrši transakciju bez mogućnosti njenog menjanja.


![CYP201](assets/fr/026.webp)


U svim dijagramima ovog poglavlja, narandžasta boja predstavlja elemente pokrivene potpisom, dok crna boja označava one koji nisu.



- `SIGHASH_NONE` (`0x02`): Potpis pokriva sve ulaze, ali nijedan izlaz, što omogućava modifikaciju izlaza nakon potpisivanja. U konkretnim terminima, ovo je slično blanko čeku. Potpisnik otključava UTXO-e u ulazima, ali ostavlja polje izlaza potpuno promenljivim. Svako ko zna za ovu transakciju može dodati izlaz po svom izboru, na primer, specificiranjem adrese za primanje kako bi prikupio sredstava potrošenih inputa, a zatim emitovati transakciju da prihvati bitkojne. Potpis vlasnika ulaza neće biti poništen, jer pokriva samo ulaze.


![CYP201](assets/fr/027.webp)



- `SIGHASH_SINGLE` (`0x03`): Potpis pokriva sve ulaze kao i jedan izlaz, koji odgovara indeksu potpisanog ulaza. Na primer, ako potpis otključava _scriptPubKey_ ulaza #0, onda pokriva i izlaz #0. Potpis takođe štiti sve ostale ulaze, koji se više ne mogu menjati. Međutim, svako može dodati dodatni izlaz bez poništavanja potpisa, pod uslovom da izlaz #0, koji je jedini pokriven njime, nije izmenjen.


![CYP201](assets/fr/028.webp)


Pored ova tri sighash indikatora, postoji i modifikator `SIGHASH_ANYONECANPAY` (`0x80`). Ovaj modifikator se može kombinovati sa osnovnim sighash indikatorom kako bi se kreirala tri nova sighash indikatora:



- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): Potpis pokriva jedan ulaz dok uključuje sve izlaze transakcije. Ovaj kombinovani sighash indikator omogućava, na primer, kreiranje transakcije za crowdfunding. Organizator priprema izlaz sa svojom adresom i ciljnim iznosom, a svaki investitor može dodati ulaze kako bi finansirao ovaj izlaz. Kada se skupi dovoljno sredstava u ulazima da zadovolje izlaz, transakcija se može emitovati.


![CYP201](assets/fr/029.webp)



- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): Potpis pokriva jedan ulaz, bez obavezivanja na bilo koji izlaz;


![CYP201](assets/fr/030.webp)



- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): Potpis pokriva jedan ulaz kao i izlaz koji ima isti indeks kao ovaj ulaz. Na primer, ako potpis otključava _scriptPubKey_ ulaza #3, pokriće i izlaz #3. Ostatak transakcije ostaje promenljiv, kako u smislu drugih ulaza, tako i drugih izlaza.


![CYP201](assets/fr/031.webp)


### Projekti za dodavanje novih Sighash indikatora


Trenutno (2024), samo sighash indikatori predstavljeni u prethodnom odeljku su upotrebljivi u Bitcoin-u. Međutim, neki projekti razmatraju dodavanje novih sighash indikatora. Na primer, BIP118, koji su predložili Christian Decker i Anthony Towns, uvodi dva nova sighash indikatora: `SIGHASH_ANYPREVOUT` i `SIGHASH_ANYPREVOUTANYSCRIPT` (_AnyPrevOut = "Bilo koji prethodni izlaz"_).


Ova dva sighash indikatora bi ponudile dodatnu mogućnost u Bitcoin-u: kreiranje potpisa koji ne pokrivaju nijedan specifičan ulaz transakcije.


![CYP201](assets/fr/032.webp)


Ovu ideju su prvobitno formulisali Joseph Poon i Thaddeus Dryja u Lightning White Paper-u. Pre nego što je preimenovan, ovaj sighash indikator se zvao `SIGHASH_NOINPUT`.

Ako se ovaj sighash indikator integriše u Bitcoin, to će omogućiti upotrebu tzv. kovenanata — pravila koja ograničavaju kako se sredstva mogu trošiti u budućnosti, ali je takođe i obavezan preduslov za implementaciju Eltoo-a, opšteg protokola za druge slojeve koji definiše kako zajednički upravljati vlasništvom nad UTXO-om. Eltoo je specifično dizajniran da reši probleme povezane sa mehanizmima za pregovaranje o stanju Lightning kanala, to jest, između otvaranja i zatvaranja.


Da biste produbili svoje znanje o Lightning Network, nakon kursa CYP201, toplo preporučujem kurs LNP201 od Fanisa Michalakisa, koji detaljno pokriva ovu temu:


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

U narednom delu predlažem da otkrijemo kako funkcioniše bezbednosna fraza koja je osnova vašeg Bitcoin novčanika.


# Bezbednosna fraza


<partId>4070af16-c8a2-58b5-9871-a22c86c07458</partId>


## Evolucija Bitcoin novčanika


<chapterId>9d9acd5d-a0e5-5dfd-b544-f043fae8840f</chapterId>


Sada kada smo istražili funkcionisanje heš funkcija i digitalnih potpisa, možemo proučiti kako funkcionišu Bitcoin novčanici. Cilj će biti da opišemo kako je novčanik u Bitcoin-u konstruisan, kako se dekomponuje i za šta se koriste različiti delovi informacija koji ga čine. Ovo razumevanje mehanizama novčanika omogućiće vam da poboljšate korišćenje Bitcoin-a u smislu sigurnosti i privatnosti.


Pre nego što se upustimo u tehničke detalje, neophodno je razjasniti šta se podrazumeva pod "Bitcoin novčanik" i razumeti njegovu korisnost.


### Šta je Bitcoin novčanik?


Za razliku od tradicionalnih novčanika, koji vam omogućavaju da čuvate fizičke novčanice i kovanice, Bitcoin novčanik ne "sadrži" bitkoine per se. Naime, bitkoini ne postoje u fizičkom ili digitalnom obliku koji se može čuvati, već su predstavljeni jedinicama obračuna prikazanim u Bitcoin sistemu u obliku **UTXO-a** (_Unspent Transaction Outputs_).


UTXO-i tako predstavljaju fragmente bitkoina, različitih veličina, koji se mogu potrošiti pod uslovom da je njihov _scriptPubKey_ zadovoljen. Da bi potrošio svoje bitkoine, korisnik mora obezbediti _scriptSig_ koji otključava _scriptPubKey_ povezan sa njegovim UTXO. Ovaj dokaz se obično vrši putem digitalnog potpisa, generisanog iz privatnog ključa koji odgovara javnom ključu prisutnom u _scriptPubKey_. Dakle, ključni element koji korisnik mora obezbediti je privatni ključ.

Uloga Bitcoin novčanika je upravo da bezbedno upravlja ovim privatnim ključevima. U stvarnosti, njegova uloga je više slična ulozi priveska za ključeve nego novčanika u tradicionalnom smislu.


### JBOK Novčanici


Prvi novčanici korišćeni u Bitcoin-u bili su JBOK (_Just a Bunch Of Keys_) novčanici, koji su grupisali privatne ključeve generisane nezavisno i bez ikakve veze među njima. Ovi novčanici su radili na jednostavnom modelu gde je svaki privatni ključ mogao da otključa jedinstvenu Bitcoin primajuću adresu.


![CYP201](assets/fr/033.webp)


Ako neko želi da koristi više privatnih ključeva, bilo je potrebno napraviti onoliko rezervnih kopija koliko je potrebno da se obezbedi pristup sredstvima u slučaju problema sa uređajem koji hostuje novčanik. Ako se koristi jedan privatni ključ, ova struktura novčanika može biti dovoljna, jer je jedna rezervna kopija dovoljna. Međutim, ovo predstavlja problem: u Bitcoin-u se snažno savetuje protiv korišćenja uvek istog privatnog ključa. Naime, privatni ključ je povezan sa jedinstvenom adresom, a Bitcoin adrese za primanje su obično dizajnirane za jednokratnu upotrebu. Svaki put kada primite sredstva, trebalo bi da generišete novu praznu adresu.


Ovo ograničenje proizlazi iz Bitcoin modela privatnosti. Ponovnim korišćenjem iste adrese, spoljnim posmatračima se olakšava praćenje Bitcoin transakcija. Zato se ponovna upotreba prijemne adrese snažno obeshrabruje. Međutim, da bismo imali više adresa i javno odvojili naše transakcije, neophodno je upravljati sa više privatnih ključeva. U slučaju JBOK novčanika, to podrazumeva kreiranje onoliko rezervnih kopija koliko ima novih parova ključeva, zadatak koji može brzo postati složen i težak za održavanje korisnicima.


Da biste saznali više o modelu privatnosti Bitcoin-a i otkrili metode za zaštitu vaše privatnosti, takođe preporučujem da pratite moj BTC204 kurs na Plan ₿ Network:


https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### HD Novčanici


Kako bi se rešilo ograničenje JBOK novčanika, naknadno je korišćena nova struktura novčanika. Godine 2012, Pieter Wuille je predložio poboljšanje sa BIP32, koje uvodi HD (Hijerarhijski Determinističke) novčanike. Princip HD novčanika je da se svi privatni ključevi izvedu iz jednog izvora informacija, nazvanog seed, na deterministički i hijerarhijski način. Ovaj seed se nasumično generiše kada se novčanik kreira i predstavlja jedinstvenu rezervnu kopiju koja omogućava rekreaciju svih privatnih ključeva novčanika. Tako korisnik može generisati veoma veliki broj privatnih ključeva kako bi izbegao ponovnu upotrebu adresa i očuvao svoju privatnost, dok mu je potrebno samo da napravi jednu rezervnu kopiju svog novčanika putem seed-a.


![CYP201](assets/fr/034.webp)


U HD novčanicima, derivacija ključeva se vrši prema hijerarhijskoj strukturi koja omogućava da ključevi budu organizovani u derivacione podprostore, pri čemu se svaki podprostor može dalje deliti, kako bi se olakšalo upravljanje sredstvima i interoperabilnost između različitih softverskih novčanika. Danas, ovaj standard usvaja velika većina korisnika Bitcoin-a. Iz tog razloga, detaljno ćemo ga ispitati u narednim poglavljima.


### BIP39 Standard: Bezbednosna fraza


Pored BIP32, BIP39 standardizuje seed format kao bezbednosnu frazu, kako bi olakšalo pravljenje sigurnosne kopije i čitljivosti korisnicima. Bezbednosna fraza, takođe nazvana fraza za oporavak ili fraza od 24 reči, je sekvenca reči izvučena iz unapred definisane liste koja sigurno kodira seed novčanika.


Bezbednosna fraza u velikoj meri pojednostavljuje pravljenje sigurnosne kopije za korisnika. U slučaju gubitka, oštećenja ili krađe uređaja koji hostuje novčanik, jednostavno poznavanje ove bezbednosne fraze omogućava rekreaciju novčanika i povratak pristupa svim sredstvima koja su njome osigurana.


U narednim poglavljima istražićemo unutrašnje funkcionisanje HD novčanika, uključujući mehanizme derivacije ključeva i različite moguće hijerarhijske strukture. Ovo će vam omogućiti bolje razumevanje kriptografskih osnova na kojima se zasniva sigurnost sredstava u Bitcoin-u. I za početak, u sledećem poglavlju, predlažem da otkrijemo ulogu entropije koja je u osnovi vašeg novčanika.


## Entropija i slučajni brojevi


<chapterId>b43c715d-affb-56d8-a697-ad5bc2fffd63</chapterId>

Moderni HD novčanici oslanjaju se na jedan početni deo informacija nazvan "entropija" kako bi deterministički generisali čitav skup ključeva u novčaniku. Ova entropija je pseudo-slučajni broj koji delimično određuje sigurnost novčanika.


### Definicija entropije


Entropija, u kontekstu kriptografije i informacija, je kvantitativna mera nesigurnosti ili nepredvidljivosti povezane sa izvorom podataka ili slučajnim procesom. Ona igra važnu ulogu u bezbednosti kriptografskih sistema, posebno u generisanju ključeva i slučajnih brojeva. Visoka entropija osigurava da su generisani ključevi dovoljno nepredvidljivi i otporni na napade silovite pretrage, gde napadač pokušava da otkrije ključ isprobavanjem svih mogućih kombinacija.


U kontekstu Bitcoin-a, entropija se koristi za generisanje seed-a. Kada se kreira HD novčanik, konstrukcija bezbednosne fraze se vrši iz slučajnog broja, koji je sam izveden iz izvora entropije. Fraza se zatim koristi za genirsanje više privatnih ključeva, na deterministički i hijerarhijski način, kako bi se kreirali uslovi trošenja na UTXO-vima.


### Metode generisanja entropije


Početna entropija korišćena za HD Wallet je generalno 128 bita ili 256 bita, gde:



- **128 bita entropije** odgovara bezbednosnoj frazi od **12 reči**;
- **256 bita entropije** odgovara bezbednosnoj frazi od **24 reči**.


U većini slučajeva, ovaj nasumični broj automatski generiše softver novčanika koristeći PRNG (_Pseudo-Random Number Generator_). PRNG-ovi su kategorija algoritama koji se koriste za generisanje sekvence brojeva iz početnog stanja, koje imaju karakteristike približne onima nasumičnog broja, bez da su zaista nasumični. Dobar PRNG mora imati osobine kao što su uniformnost izlaza, nepredvidivost i otpornost na napade putem predviđanja vrednosti. Za razliku od pravih generatora nasumičnih brojeva (TRNG-ova), PRNG-ovi su deterministički i reproduktivni.


![CYP201](assets/fr/035.webp)


Alternativa je ručno generisanje entropije, što nudi bolju kontrolu, ali je takođe mnogo rizičnije. Snažno preporučujem da ne pokušavate sami da generišete entropiju za svoj HD novčanik.


U sledećem poglavlju, videćemo kako prelazimo sa nasumičnog broja na bezbednosnu frazu od 12 ili 24 reči.


## Bezbednosna fraza


<chapterId>8f9340c1-e6dc-5557-a2f2-26c9669987d5</chapterId>

Bezbednosna fraza, takođe nazvana "seed fraza", "fraza za oporavak", "tajna fraza" ili "fraza od 24 reči", je sekvenca koja se obično sastoji od 12 ili 24 reči, a generiše se iz entropije. Koristi se za determinističko izvođenje svih ključeva HD novčanika. To znači da je iz ove fraze moguće deterministički generisati i ponovo kreirati sve privatne i javne ključeve Bitcoin novčanika, i samim tim pristupiti sredstvima koja su njome zaštićena. Svrha bezbednosne fraze je da omogući siguran i jednostavan način za pravljenje rezervne kopije i povraćaj pristupa bitkoinima. Uvedena je 2013. godine sa standardom BIP39.


Hajde da zajedno otkrijemo kako preći od entropije do bezbednosne fraze.


### Kontrolna suma (checksum)


Da bi se entropija transformisala u bezbednosnu frazu, prvo se mora dodati kontrolna suma (ili "checksum") na kraj entropije. Ova kontrolna suma je kratka sekvenca bitova koja osigurava integritet podataka proverom da nije došlo do slučajnih izmena.


Da bi se izračunala kontrolna suma, SHA256 heš funkcija se primenjuje na entropiju (samo jednom; ovo je jedan od retkih slučajeva u Bitcoin-u gde se koristi jedan SHA256 heš umesto duplog heša). Ova operacija proizvodi 256-bitni heš. Kontrolni zbir se sastoji od prvih bitova ovog heša, a njegova dužina zavisi od dužine entropije, prema sledećoj formuli:


$$
\text{CS} = \frac{\text{ENT}}{32}
$$


gde $\text{ENT}$ predstavlja dužinu entropije u bitovima, a $\text{CS}$ dužinu kontrolne sume u bitovima.


Na primer, za entropiju od 256 bita, prvih 8 bita heša se uzima da predstavlja kontrolni zbir:


$$
\text{CS} = \frac{256}{32} = 8 \text{ bits}
$$


Jednom kada je kontrolni zbir izračunat, on se konkatenira sa entropijom da bi se dobila proširena sekvenca bitova označena sa $\text{ENT} \Vert \text{CS}$ ("konkatenirati" znači spojiti stvari jednu za drugom).


![CYP201](assets/fr/036.webp)


### Korespondencija između entropije i bezbednosne fraze


Broj reči u bezbednosnoj frazi zavisi od veličine početne entropije, kao što je prikazano u sledećoj tabeli sa:



- $\text{ENT}$: veličina entropije u bitovima;
- $\text{CS}$: veličina u bitovima kontrolnog zbira;
- $w$: broj reči u konačnoj bezbednosnoj frazi.


$$
\begin{array}{|c|c|c|c|}
\hline
\text{ENT} & \text{CS} & \text{ENT} \Vert \text{CS} & w \\
\hline
128 & 4 & 132 & 12 \\
160 & 5 & 165 & 15 \\
192 & 6 & 198 & 18 \\
224 & 7 & 231 & 21 \\
256 & 8 & 264 & 24 \\
\hline
\end{array}
$$


Na primer, za entropiju od 256 bita, rezultat $\text{ENT} \Vert \text{CS}$ je 264 bita i daje bezbednosnu frazu od 24 reči.


### Pretvaranje binarnog niza u bezbednosnu frazu


Bit sekvenca $\text{ENT} \Vert \text{CS}$ se zatim deli na segmente od 11 bita. Svaki segment od 11 bita, kada se konvertuje u decimalni oblik, odgovara broju između 0 i 2047, koji označava poziciju reči [u listi od 2048 reči standardizovanih od strane BIP39](https://github.com/Planb-Network/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf).


![CYP201](assets/fr/037.webp)


Na primer, za entropiju od 128 bita, kontrolni zbir je 4 bita, i tako ukupna sekvenca iznosi 132 bita. Ona je podeljena na 12 segmenata od po 11 bita (narandžasti bitovi označavaju kontrolni zbir):


![CYP201](assets/fr/038.webp)


Svaki segment se zatim konvertuje u decimalni broj koji predstavlja reč u listi. Na primer, binarni segment `01011010001` je ekvivalentan decimalnom broju `721`. Dodavanjem 1 da bi se uskladilo sa indeksiranjem liste (koje počinje od 1, a ne od 0), ovo daje rang reči `722`, što je "_focus_" u listi.


![CYP201](assets/fr/039.webp)


Ova prepiska se ponavlja za svaki od 12 segmenata, kako bi se dobila fraza od 12 reči.


![CYP201](assets/fr/040.webp)


### Karakteristike BIP39 liste reči


Jedinstvena karakteristika BIP39 liste reči je da nijedna reč ne deli ista prva četiri slova u istom redosledu sa drugom rečju. To znači da je zapisivanje samo prva četiri slova svake reči dovoljno za čuvanje bezbednosne fraze. Ovo može biti zanimljivo za uštedu prostora, posebno za one koji žele da je ugraviraju na metalnu podlogu.


Ova lista od 2048 reči postoji na nekoliko jezika. Ovo nisu jednostavni prevodi, već različite reči za svaki jezik. Međutim, snažno se preporučuje pridržavanje engleske verzije, jer verzije na drugim jezicima generalno nisu podržane od strane svih softverskih novčanika.


### Koju dužinu odabrati za svoju bezbednosnu frazu?


Da biste odredili optimalnu dužinu vaše bezbednosne fraze, potrebno je razmotriti stvarnu sigurnost koju pruža. Fraza od 12 reči obezbeđuje 128 bita sigurnosti, dok fraza od 24 reči nudi 256 bita.


Međutim, ova razlika u sigurnosti na nivou fraza ne poboljšava ukupnu sigurnost Bitcoin novčanika, jer privatni ključevi izvedeni iz ove fraze imaju korist samo od 128 bita sigurnosti. Zaista, kao što smo ranije videli, Bitcoin privatni ključevi se generišu iz slučajnih brojeva (ili izvedeni iz slučajnog izvora) u rasponu između $1$ i $n-1$, gde $n$ predstavlja red generator tačke $G$ krive secp256k1, broj nešto manji od $2^{256}$. Moglo bi se stoga pomisliti da ovi privatni ključevi nude 256 bita sigurnosti. Međutim, njihova sigurnost leži u težini pronalaženja privatnog ključa iz njegovog pridruženog javnog ključa, težini koju postavlja matematički problem diskretnog logaritma na eliptičkim krivama (_ECDLP_). Do danas, najpoznatiji algoritam za rešavanje ovog problema je Pollardov rho algoritam, koji smanjuje broj operacija potrebnih za razbijanje ključa na kvadratni koren njegove veličine.


Za ključeve od 256 bita, kao što su oni korišćeni u Bitcoin-u, Pollardov rho algoritam tako smanjuje složenost na $2^{128}$ operacija:


$$

O(\sqrt{2^{256}}) = O(2^{128})


$$


Stoga se smatra da privatni ključ korišćen u Bitcoin-u nudi 128 bita sigurnosti.


Kao rezultat toga, odabir fraze od 24 reči ne pruža dodatnu zaštitu za novčanik, jer 256 bita sigurnosti na frazi je besmisleno ako izvedeni ključevi nude samo 128 bita sigurnosti. Da ilustrujemo ovaj princip, to je kao da imate kuću sa dvoja vrata: stara drvena vrata i ojačana vrata. U slučaju provale, ojačana vrata ne bi bila od koristi, jer bi provalnik prošao kroz drvena vrata. Ovo je analogna situacija ovde.


Fraza od 12 reči, koja takođe nudi 128 bita sigurnosti, trenutno je dovoljna da zaštiti vaše bitkojne od bilo kakvog pokušaja krađe. Sve dok se algoritam digitalnog potpisa ne promeni da koristi veće ključeve ili da se oslanja na matematički problem drugačiji od ECDLP, fraza od 24 reči ostaje suvišna. Štaviše, duža fraza povećava rizik od gubitka tokom pravljenja sigurnosne kopije: sigurnosna kopija koja je duplo kraća uvek je lakše za upravljanje.


Da biste išli dalje i konkretno naučili kako ručno generisati testnu bezbednosnu frazu, savetujem vam da otkrijete ovaj vodič:


https://planb.network/tutorials/wallet/backup/generate-mnemonic-phrase-47507d90-e6af-4cac-b01b-01a14d7a8228

Pre nego što nastavim sa izvođenjem novčanika iz ove bezbednosne fraze, u sledećem poglavlju ću vas upoznati sa BIP39 passphrase, jer igra ulogu u procesu izvođenja i nalazi se na istom nivou kao i bezbednosna fraza.


## passphrase (lozinka bezbednosne fraze)


<chapterId>6a51b397-f3b5-5084-b151-cef94bc9b93f</chapterId>


Kao što smo upravo videli, HD novčanici se generišu iz bezbednosne fraze koja obično sadrži 12 ili 24 reči. Ova fraza je veoma važna jer omogućava obnavljanje svih ključeva novčanika u slučaju da se fizički uređaj (kao što je hardverski novčanik, na primer) izgubi. Međutim, ona predstavlja jedinstvenu tačku otkaza, jer ako je kompromitovana, napadač bi mogao da ukrade sve bitkoine. Tu na scenu stupa BIP39 passphrase.


### Šta je BIP39 passphrase?


Passphrase je opcionalna lozinka, koju možete slobodno izabrati, koja se dodaje bezbednosnoj frazi u procesu derivacije ključa kako bi se poboljšala sigurnost novčanika.


Budite pažljivi, passphrase ne treba mešati sa PIN kodom vašeg hardverskog novčanika ili lozinkom koja se koristi za otključavanje pristupa vašem novčaniku na vašem računaru. Za razliku od svih ovih elemenata, passphrase igra ulogu u derivaciji ključeva vašeg novčanika. **To znači da bez njega nikada nećete moći da povratite svoje bitkoine.**


Passphrase radi u tandemu sa bezbednosnom frazom, modifikujući seed iz koje se generišu ključevi. Dakle, čak i ako neko dobije vašu frazu od 12 ili 24 reči, bez passphrase, ne može pristupiti vašim sredstvima. Korišćenje passphrase u suštini stvara novi novčanik sa različitim ključevima. Modifikovanje passphrase-a (čak i minimalno) će generisati drugačiji novčanik.


![CYP201](assets/fr/041.webp)


### Zašto bi trebalo da koristite passphrase?


Passphrase je proizvoljan i može biti bilo koja kombinacija karaktera koju izabere korisnik. Korišćenje passphrase-a stoga nudi nekoliko prednosti. Pre svega, smanjuje sve rizike povezane sa kompromitovanjem bezbednosne fraze zahtevajući još jedan sigurnosni korak za pristup sredstvima (provala, pristup vašem domu, itd.).


Dalje, može se strateški koristiti za kreiranje "mamca" novčanika, kako bi se suočili sa fizičkim ograničenjima za krađu vaših sredstava kao što je ozloglašeni "_napad uz fizičku pretnju_". U ovom scenariju, ideja je imati novčanik bez passphrase koji sadrži samo malu količinu bitkoina, dovoljno da zadovolji potencijalnog napadača, dok je pravi novčanik skriven. Ovaj poslednji koristi istu bezbednosnu frazu, ali je osiguran dodatnim passphrase-om.

Konačno, upotreba passphrase-a je zanimljiva kada se želi kontrolisati nasumičnost generisanja seed-a od HD novčanika.


### Kako odabrati dobar passphrase?


Da bi passphrase bio efikasan, mora biti dovoljno dug i nasumičan. Kao i kod jakih lozinki, preporučujem odabir passphrase koji je što duži i nasumičniji, sa raznovrsnošću slova, brojeva i simbola kako bi bilo koji napad silovitom pretragom bio nemoguć.


Takođe je važno pravilno sačuvati ovaj passphrase, na isti način kao i bezbednosnu frazu. **Gubitak znači gubitak pristupa vašim bitcoinima**. Snažno savetujem protiv oslanjanja samo na pamćenje, jer to nerazumno povećava rizik od gubitka. Idealno je zapisati ga na fizički medijum (papir ili metal) odvojen od bezbednosne fraze. Ova rezervna kopija mora očigledno biti uskladištena na drugom mestu od mesta gde je vaša bezbednosna fraza uskladištena kako bi se sprečilo da obe budu istovremeno ugrožene.


![CYP201](assets/fr/042.webp)


U sledećem odeljku, otkrićemo kako se ova dva osnovna elementa vašeg novčanika — bezbednosna fraza i passphrase — koriste za izvođenje parova ključeva korišćenih u _scriptPubKey_ koji zaključavaju vaše UTXO-ve.


# Kreiranje Bitcoin novčanika


<partId>9c25e767-7eae-50b8-8c5f-679d8fc83bab</partId>


## Kreiranje seed-a i glavnog ključa


<chapterId>63093760-2010-5691-8d0e-9a04732ae557</chapterId>


Kada se generišu bezbednosna fraza i opcioni passphrase, može početi proces derivacije Bitcoin HD novčanika. Bezbednsona fraza se prvo konvertuje u seed koji čini osnovu svih ključeva novčanika.


![CYP201](assets/fr/043.webp)


### Seed HD novčanika


BIP39 standard definiše seed kao 512-bitni niz, koji služi kao početna tačka za izvođenje svih ključeva HD novčanika. Seed se izvodi iz bezbednosne fraze i mogućeg passphrase-a koristeći **PBKDF2** algoritam (_Password-Based Key Derivation Function 2_) koji smo već diskutovali u poglavlju 3.3. U ovoj funkciji izvođenja, koristićemo sledeće parametre:



- $m$ : bezbednosna fraza;
- $p$ : opcioni passphrase koji korisnik bira da poboljša sigurnost seed-a. Ako nema passphrase, ovo polje ostaje prazno;
- $\text{PBKDF2}$ : the derivation function with $\text{HMAC-SHA512}$ and $2048$ iterations;
- $s$: the 512-bit seed novčanika.

Bez obzira na izabranu dužinu bezbednosne fraze (132 bita ili 264 bita), funkcija PBKDF2 će uvek proizvesti izlaz od 512 bita, i seed će stoga uvek biti ove veličine.


### Šema izveđenja seed-a sa PBKDF2


Sledeća jednačina ilustruje izvođenje seed-a iz bezbednonse fraze i passphrase-a:


$$
s = \text{PBKDF2}_{\text{HMAC-SHA512}}(m, p, 2048)
$$


![CYP201](assets/fr/044.webp)


Vrednost seed-a je stoga pod uticajem vrednosti bezbednosne fraze i passphrase-a. Promenom passphrase-a dobija se drugačiji seed. Međutim, sa istom bezbednosnom frazom i passphrase-om, uvek se generiše isti seed, jer je PBKDF2 deterministička funkcija. Ovo osigurava da se isti parovi ključeva mogu povratiti putem naših rezervnih kopija.


**Napomena:** U svakodnevnom jeziku, termin "seed" često se pogrešno koristi za bezbednosnu frazu. Naime, u odsustvu passphrase-a, jedno je jednostavno kodiranje drugog. Međutim, kao što smo videli, u tehničkoj stvarnosti novčanika, seed i bezbednosna fraza su zaista dva različita elementa.


Sada kada imamo naš seed, možemo nastaviti sa izvođenjem našeg Bitcoin novčanika.


### Glavni ključ i glavni kod lanca (eng. chain code)


Kada se seed dobije, sledeći korak u izvođenju HD novčanika uključuje izračunavanje glavnog privatnog ključa i glavnog koda lance, koji će predstavljati dubinu 0 našeg novčanika.


Da bi se dobio glavni privatni ključ i glavni kod lanca, HMAC-SHA512 funkcija se primenjuje na seed, koristeći fiksni termin "_Bitcoin Seed_" identičan za sve Bitcoin korisnike. Ova konstanta je izabrana kako bi se osiguralo da su izvedeni ključevi specifični za Bitcoin. Ovde su elementi:



- $\text{HMAC-SHA512}$: funkcija derivacije;
- $s$: 512-bit seed novčanika;
- "$\text{"Bitcoin seed"}$": zajednička konstanta derivacije za sve Bitcoin novčanike.


$$

\text{output} = \text{HMAC-SHA512}(\text{"Bitcoin Seed"}, s)


$$


Izlaz ove funkcije je stoga 512 bita. Zatim se deli na 2 dela:



- Levih 256 bita čine **glavni privatni ključ**;
- Desnih 256 bita čine **glavni kod lanca**.


Matematički, ove dve vrednosti mogu se zapisati na sledeći način, gde je $k_M$ glavni privatni ključ, a $C_M$ glavni kod lanca:


$$
k_M = \text{HMAC-SHA512}(\text{"Bitcoin Seed"}, s)_{[:256]}
$$


$$
C_M = \text{HMAC-SHA512}(\text{"Bitcoin Seed"}, s)_{[256:]}
$$


![CYP201](assets/fr/045.webp)


### Uloga glavnog ključa i lanca koda


Glavni privatni ključ se smatra roditeljskim ključem, iz kojeg će biti generisani svi izvedeni privatni ključevi — deca, unuci, praunuci, itd. On predstavlja nulti nivo u hijerarhiji derivacije.


S druge strane, glavni lančani kod uvodi dodatni izvor entropije u proces izvođenja ključeva, kako bi se suprotstavio određenim potencijalnim napadima. Štaviše, u HD novčaniku, svaki par ključeva ima jedinstveni lančani kod povezan s njim, koji se takođe koristi za izvođenje ključeva iz ovog para, ali o tome ćemo detaljnije raspravljati u narednim poglavljima.


Pre nego što nastavimo sa izvođenjem HD novčanika sa sledećim elementima, želim da vas u sledećem poglavlju upoznam sa proširenim ključevima, koji se često mešaju sa glavnim ključem. Videćemo kako su konstruisani i koju ulogu igraju u Bitcoin novčaniku.


## Prošireni ključevi

<chapterId>8dcffce1-31bd-5e0b-965b-735f5f9e4602</chapterId>


Prošireni ključ je jednostavno konkatenacija ključa (bilo privatnog ili javnog) i njegovog pridruženog lanca koda. Ovaj lanac koda je ključan za izvođenje podključeva jer, bez njega, nije moguće izvesti podključeve iz roditeljskog ključa, ali ćemo ovaj proces preciznije istražiti u sledećem poglavlju. Ovi prošireni ključevi tako omogućavaju agregaciju svih potrebnih informacija za izvođenje podključeva, čime se pojednostavljuje upravljanje računima unutar HD novčanika.


![CYP201](assets/fr/046.webp)


Prošireni ključ se sastoji iz dva dela:


- payload ili glavni sadržaj, koji sadrži privatni ili javni ključ kao i povezani lančani kod;
- Metapodaci, koji su različiti delovi informacija za olakšavanje interoperabilnosti između softvera i poboljšanje razumevanja za korisnika.


### Kako funkcionišu prošireni ključevi

Kada prošireni ključ sadrži privatni ključ, naziva se prošireni privatni ključ. Prepoznaje se po prefiksu koji sadrži identifikator `prv`. Pored privatnog ključa, prošireni privatni ključ takođe sadrži pridruženi kod lanca. Sa ovom vrstom proširenog ključa, moguće je izvesti sve vrste podređenih privatnih ključeva. Stoga, dodavanjem i udvostručavanjem tačaka na eliptičkim krivama, omogućava i izvođenje podređenih javnih ključeva.


Kada prošireni ključ ne sadrži privatni ključ, već umesto toga javni ključ, naziva se prošireni javni ključ. Prepoznaje se po prefiksu koji sadrži identifikator `pub`. Očigledno, pored ključa, sadrži i pridruženi kod lanca. Za razliku od proširenog privatnog ključa, prošireni javni ključ omogućava izvođenje samo "normalnih" podređenih javnih ključeva (što znači da ne može izvesti "ojačane" podređene ključeve). U sledećem poglavlju ćemo videti šta znače ovi kvalifikatori "normalni" i "ojačani".


U svakom slučaju, prošireni javni ključ ne omogućava izvođenje privatnih podključeva. Dakle, čak i ako neko ima pristup `xpub`, neće moći da troši povezana sredstva, jer neće imati pristup odgovarajućim privatnim ključevima. Oni mogu samo izvesti javne podključeve kako bi posmatrali povezane transakcije.


Za nastavak, usvojićemo sledeću notaciju:


- $K_{\text{PAR}}$: javni nadključ;
- $k_{\text{PAR}}$: privatni nadključ;
- $C_{\text{PAR}}$: kod nad lanca;
- $C_{\text{CHD}}$: kod pod lanca;
- $K_{\text{CHD}}^n$: normalan javni podključ;
- $k_{\text{CHD}}^n$: normalan privatni podključ;
- $K_{\text{CHD}}^h$: ojačani javni podključ;
- $k_{\text{CHD}}^h$: ojačani privatni podključ.


![CYP201](assets/fr/047.webp)


### Izgradnja proširenog ključa


Prošireni ključ je strukturisan na sledeći način:


- **Verzija**: Kod verzije za identifikaciju prirode ključa (`xprv`, `xpub`, `yprv`, `ypub`...). Videćemo na kraju ovog poglavlja čemu odgovaraju slova `x`, `y` i `z`.
- **Dubina**: Hijerarhijski nivo u HD novčaniku u odnosu na glavni ključ (0 za glavni ključ).
- **Roditeljski otisak**: Prva 4 bajta HASH160 heša roditeljskog javnog (nad)ključa korišćenog za izvođenje ključa prisutnog u payload-u.
- **Broj indeksa**: Identifikator deteta među ključevima braće i sestara, to jest, među svim ključevima na istom nivou derivacije koji imaju iste roditeljske ključeve.
- **Kod lanca**: Jedinstveni 32-bajtni kod za izvođenje podređenih ključeva.
- **Ključ**: Privatni ključ (prefiksiran sa 1 bajtom za veličinu) ili javni ključ.
- **Kontrolni zbir**: Kontrolni zbir izračunat pomoću funkcije HASH256 (dvostruki SHA256) se takođe dodaje, što omogućava verifikaciju integriteta proširenog ključa tokom njegovog prenosa ili skladištenja.


Potpuni format proširenog ključa je stoga 78 bajtova bez kontrolnog zbira, i 82 bajta sa kontrolnim zbirom. Zatim se konvertuje u Base58 kako bi se dobila reprezentacija koja je lako čitljiva korisnicima. Base58 format je isti kao onaj koji se koristi za *Legacy* adrese (stariji format adrese) za primanje (pre *SegWit*).


| Element           | Opis                                                                                                               | Veličina  |
| ----------------- | ------------------------------------------------------------------------------------------------------------------ | --------- |
| Verzija           | Označava je li je ključ javni (`xpub`, `ypub`) ili privatni (`xprv`, `zprv`), kao i verziju proširenog ključa      | 4 bajta   |
| Dubina            | Nivo u hiararhiji u odnosu na glavni ključ                                                                         | 1 bajt    |
| Roditeljski otisak| Prva 4 bajta HASH160 roditeljskog javnog ključa                                                                    | 4 bajta   |
| Indeksni broj     | Redni broj ključa u hijerarhiji potomaka                                                                           | 4 bajta   |
| Lanac koda        | Koristi se za izvođenje potključeva                                                                                | 32 bajta  |
| Ključ             | Privatni ključ (koji sadrži prefiks od jednog bajta) ili javni ključ                                               | 33 bajta  |
| Kontrolni zbir    | Kontrolni zbir za verifikaciju integriteta                                                                         | 4 bajta   |

Ako se jedan bajt doda samo privatnom ključu, to je zato što je kompresovani javni ključ duži od privatnog ključa za jedan bajt. Ovaj dodatni bajt, dodat na početak privatnog ključa kao `0x00`, izjednačava njihovu veličinu, osiguravajući da je sadržaj proširenog ključa iste dužine, bilo da je u pitanju javni ili privatni ključ.


### Prefiksi proširenih ključeva

Kao što smo upravo videli, prošireni ključevi uključuju prefiks koji označava i verziju proširenog ključa i njegovu prirodu. Oznaka `pub` ukazuje da se odnosi na prošireni javni ključ, a oznaka `prv` označava prošireni privatni ključ. Dodatno slovo na bazi proširenog ključa pomaže da se naznači da li je standard koji se prati Legacy, SegWit v0 ili SegWit v1, itd.

Evo sažetka prefiksa koji se koriste i njihovih značenja:


| Base 58 Prefix  | Base 16 Prefix  | Mreža   | Svrha               | Pridružene skripte  | Derivacija            | Tip ključa   |
| --------------- | --------------- | ------- | ------------------- | ------------------- | --------------------- | ------------ |
| `xpub`          | `0488b21e`      | Mainnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/0'`, `m/86'/0'` | javni       |
| `xprv`          | `0488ade4`      | Mainnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/0'`, `m/86'/0'` | privatni    |
| `tpub`          | `043587cf`      | Testnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/1'`, `m/86'/1'` | javni       |
| `tprv`          | `04358394`      | Testnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/1'`, `m/86'/1'` | privatni    |
| `ypub`          | `049d7cb2`      | Mainnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/0'`             | javni        |
| `yprv`          | `049d7878`      | Mainnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/0'`             | privatni     |
| `upub`          | `049d7cb2`      | Testnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/1'`             | javni        |
| `uprv`          | `044a4e28`      | Testnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/1'`             | privatni     |
| `zpub`          | `04b24746`      | Mainnet | SegWit V0           | P2WPKH              | `m/84'/0'`             | javni        |
| `zprv`          | `04b2430c`      | Mainnet | SegWit V0           | P2WPKH              | `m/84'/0'`             | privatni     |
| `vpub`          | `045f1cf6`      | Testnet | SegWit V0           | P2WPKH              | `m/84'/1'`             | javni        |
| `vprv`          | `045f18bc`      | Testnet | SegWit V0           | P2WPKH              | `m/84'/1'`             | privatni     |


### Detalji o elementima proširenog ključa


Da bismo bolje razumeli unutrašnju strukturu proširenog ključa, uzmimo jedan kao primer i razložimo ga. Evo jednog proširenog ključa:



- **U formatu Base58**:


```text
xpub6CTNzMUkzpurBWaT4HQoYzLP4uBbGJuWY358Rj7rauiw4rMHCyq3Rfy9w4kyJXJzeFfyrKLUar2rUCukSiDQFa7roTwzjiAhyQAdPLEjqHT
```



- **U heksadecimalnom formatu**:


```text
0488B21E036D5601AD80000000C605DF9FBD77FD6965BD02B77831EC5C78646AD3ACA14DC3984186F72633A89303772CCB99F4EF346078D167065404EED8A58787DED31BFA479244824DF50658051F067C3A
```


Ovaj prošireni ključ se razlaže na nekoliko različitih elemenata:


1.**Verzija**: `0488B21E`


Prva 4 bajta su verzija. Ovde, ona odgovara proširenom javnom ključu na Mainnet-u sa svrhom derivacije ili *Legacy* ili *SegWit v1*.


2.**Dubina**: `03`


Ovo polje označava hijerarhijski nivo ključa unutar HD novčanika. U ovom slučaju, dubina od `03` znači da je ovaj ključ tri nivoa derivacije ispod glavnog ključa.


3.**Roditeljski otisak**: `6D5601AD`


Ovo su prva 4 bajta HASH160 heša nadređenog javnog ključa koji je korišćen za izvođenje ovog `xpub`.


4.**Indeks broj**: `80000000`


Ovaj indeks označava poziciju ključa među decom njegovog roditelja. Prefiks `0x80` označava da je ključ izveden na ojačan način, a pošto je ostatak ispunjen nulama, to označava da je ovaj ključ prvi među svojim mogućim srodnicima.


5.**Kod lanca**: `C605DF9FBD77FD6965BD02B77831EC5C78646AD3ACA14DC3984186F72633A893`


6.**Javni ključ**: `03772CCB99F4EF346078D167065404EED8A58787DED31BFA479244824DF5065805`


7.**Kontrolni zbir**: `1F067C3A`


Kontrolni zbir odgovara prva 4 bajta heša (dupli SHA256) svega ostalog.


U ovom poglavlju smo otkrili da postoje dve različite vrste dečijih (pod) ključeva. Takođe smo naučili da za izvođenje ovih dečijih ključeva je potreban ključ (bilo privatni ili javni) i njegov lančani kod. U sledećem poglavlju ćemo detaljno ispitati prirodu ovih različitih vrsta ključeva i kako ih izvesti iz njihovog roditeljskog ključa i lančanog koda.



## Izvođenje podparova ključeva

<chapterId>61c0807c-845b-5076-ad06-7f395b36adfd</chapterId>


Izvođenje parova ključeva za decu u Bitcoin HD novčanicima oslanja se na hijerarhijsku strukturu koja omogućava generisanje velikog broja ključeva, dok organizuje ove parove u različite grupe kroz grane. Svaki podpar izveden iz roditeljskog (nad)para može se koristiti ili direktno u *scriptPubKey* za zaključavanje bitkoina, ili kao početna tačka za generisanje više podključeva, i tako dalje, kako bi se stvorilo stablo ključeva.


Sva ova izvođenja počinju sa glavnim ključem i glavnim kodom lanca, koji su prvi roditelji na dubinskom nivou 0. Oni su, na neki način, Adam i Eva ključeva vašeg novčanika, zajednički preci svih izvedenih ključeva.


![CYP201](assets/fr/048.webp)


Hajde da istražimo kako ova deterministička derivacija funkcioniše.


### Različite vrste derivacija podključeva


Kao što smo ukratko pomenuli u prethodnom poglavlju, podključevi su podeljeni u dve glavne vrste.


- **Normalni podključevi** ($k_{\text{CHD}}^n, K_{\text{CHD}}^n$): Ovi se izvode iz proširenog javnog ključa ($K_{\text{PAR}}$), ili proširenog privatnog ključa ($k_{\text{PAR}}$), prvo izvodeći javni ključ.
- **Ojačani podključevi** ($k_{\text{CHD}}^h, K_{\text{CHD}}^h$): Ovi ključevi mogu biti izvedeni samo iz proširenog privatnog ključa ($k_{\text{PAR}}$) i stoga su nevidljivi posmatračima koji imaju samo prošireni javni ključ.


Svaki par podključeva identifikovan je 32-bitnim **indeksom** (nazvanim $i$ u našim proračunima). Indeksi za normalne ključeve kreću se od $0$ do $2^{31}-1$, dok se oni za ojačane ključeve kreću od $2^{31}$ do $2^{32}-1$. Ovi brojevi se koriste za razlikovanje parova ključeva braće i sestara tokom derivacije. Naime, svaki roditeljski par ključeva mora biti sposoban da izvede više parova ključeva deteta. Ako bismo sistematski primenili isti proračun sa roditeljskih ključeva, svi dobijeni ključevi braće i sestara bi bili identični, što nije poželjno. Indeks tako uvodi promenljivu koja modifikuje proračun derivacije, omogućavajući da se svaki par braće i sestara razlikuje. Osim za specifičnu upotrebu u određenim protokolima i standardima derivacije, generalno počinjemo derivaciju prvog ključa deteta sa indeksom `0`, drugog sa indeksom `1`, i tako dalje.


### Proces derivacije sa HMAC-SHA512


Izvođenje svakog ključa deteta zasniva se na HMAC-SHA512 funkciji, koju smo diskutovali u Odeljku 2 o heš funkcijama. Ona uzima dva ulaza: roditeljski kod lanca$C_{\text{PAR}}$, i konkatenaciju roditeljskog ključa (bilo javnog ključa $K_{\text{PAR}}$ ili privatnog ključa $k_{\text{PAR}}$, u zavisnosti od tipa željenog ključa deteta) sa indeksom. Izlaz HMAC-SHA512 je 512-bitni niz, podeljen na dva dela:


- **Prvih 32 bajta** (ili $h_1$) koriste se za izračunavanje novog para potomaka.
- **Poslednjih 32 bajta** (ili $h_2$) služe kao novi kod lanca $C_{\text{CHD}}$ za par deteta.


U svim našim proračunima, označiću $\text{Hash}$ kao izlaz funkcije HMAC-SHA512.


![CYP201](assets/fr/049.webp)


#### Izvođenje privatnog ključa deteta iz privatnog ključa roditelja


Da bi se izveo privatni ključ deteta $k_{\text{CHD}}$ iz roditeljskog privatnog ključa $k_{\text{PAR}}$, moguća su dva scenarija u zavisnosti od toga da li se želi ojačani ili normalni ključ.


Za **normalan ključ deteta** ($i < 2^{31}$), proračun $\text{Hash}$ je sledeći:


$$
\text{hash} = \text{HMAC-SHA512}(C_{\text{PAR}},  k_{\text{PAR}} \cdot G \Vert i)
$$


U ovom proračunu, primećujemo da naša HMAC funkcija uzima dva ulaza: prvo, roditeljski lančani kod, a zatim konkatenaciju indeksa sa javnim ključem povezanim sa roditeljskim privatnim ključem. Roditeljski javni ključ se ovde koristi jer želimo da izvedemo normalan dečiji ključ, a ne ojačani.

Sada imamo 64-bajtni $\text{Hash}$ koji ćemo podeliti na 2 dela od po 32 bajta, $h_1$ i $h_2$:



$$

\text{hash} = h_1 \Vert h_2

$$



$$
h_1 = \text{hash}_{[:32]} \quad, \quad h_2 = \text{hash}_{[32:]}
$$


Privatni ključ deteta $k_{\text{CHD}}^n$ se zatim izračunava na sledeći način:


$$
k_{\text{CHD}}^n = \text{parse256}(h_1) + k_{\text{PAR}} \mod n
$$


U ovom proračunu, operacija $\text{parse256}(h_1)$ sastoji se od interpretacije prvih 32 bajta $\text{Hash}$ kao 256-bitnog celog broja. Ovaj broj se zatim dodaje roditeljskom privatnom ključu, sve uzeto modulo $n$ da bi se ostalo unutar reda eliptičke krive, kao što smo videli u odeljku 3 o digitalnim potpisima. Dakle, da bi se izveo normalan dečiji privatni ključ, iako se roditeljski javni ključ koristi kao osnova za proračun u ulazima HMAC-SHA512 funkcije, uvek je neophodno imati roditeljski privatni ključ da bi se proračun završio.


Iz ovog privatnog ključa deteta, moguće je izvesti odgovarajući javni ključ primenom ECDSA ili Schnorr. Na ovaj način, dobijamo kompletan par ključeva.


Zatim, drugi deo $\text{Hash}$ se jednostavno tumači kao lančani kod za par ključeva deteta koji smo upravo izveli:


$$
C_{\text{CHD}} = h_2
$$


Evo šematski prikaz celokupne izvedbe:


![CYP201](assets/fr/050.webp)


Za **ojačani ključ deteta** ($i \geq 2^{31}$), proračun $\text{Hash}$ je sledeći:



$$
\text{hash} = \text{HMAC-SHA512}(C_{\text{PAR}}, 0x00 \Vert k_{\text{PAR}} \Vert i)
$$


U ovom proračunu, primećujemo da naša HMAC funkcija uzima dva ulaza: prvo, roditeljski lančani kod, a zatim konkatenaciju indeksa sa roditeljskim privatnim ključem. Roditeljski privatni ključ se koristi ovde jer želimo da izvedemo ojačani dečiji ključ. Štaviše, bajt jednak `0x00` se dodaje na početku ključa. Ova operacija izjednačava njegovu dužinu kako bi odgovarala dužini kompresovanog javnog ključa.

Dakle, sada imamo 64-bajtni $\text{Hash}$ koji ćemo podeliti na 2 dela od po 32 bajta, $h_1$ i $h_2$:

$$

\text{hash} = h_1 \Vert h_2

$$



$$
h_1 = \text{hash}[:32] \quad, \quad h_2 = \text{hash}[32:]
$$


Privatni ključ deteta $k_{\text{CHD}}^h$ se zatim izračunava na sledeći način:


$$
k_{\text{CHD}}^h = \text{parse256}(h_1) + k_{\text{PAR}} \mod n
$$


Zatim jednostavno tumačimo drugi deo $\text{Hash}$ kao lančani kod za par ključeva potomaka koje smo upravo izveli:


$$
C_{\text{CHD}} = h_2
$$


Evo šematskog prikaza celokupne izvedbe:


![CYP201](assets/fr/051.webp)


Možemo videti da normalna derivacija i ojačana derivacija funkcionišu na isti način, sa ovom razlikom: normalna derivacija koristi roditeljski javni ključ kao ulaz za HMAC funkciju, dok ojačana derivacija koristi roditeljski privatni ključ.


#### Izvođenje javnog ključa deteta iz javnog ključa roditelja


Ako znamo samo roditeljski javni ključ $K_{\text{PAR}}$ i pridruženi lančani kod $C_{\text{PAR}}$, tj. prošireni javni ključ, moguće je izvesti dečije javne ključeve $K_{\text{CHD}}^n$, ali samo za normalne (neojačane) dečije ključeve. Ovaj princip posebno omogućava praćenje kretanja računa u Bitcoin novčanicima sa `xpub` (*samo za gledanje*).


Da bismo izvršili ovaj proračun, izračunaćemo $\text{Hash}$ sa indeksom $i < 2^{31}$ (normalna derivacija):


$$
\text{hash} = \text{HMAC-SHA512}(C_{\text{PAR}}, K_{\text{PAR}} \Vert i)
$$


U ovom proračunu, primećujemo da naša HMAC funkcija uzima dva ulaza: prvo roditeljski lančani kod, zatim konkatenaciju indeksa sa roditeljskim javnim ključem.


Dakle, sada imamo $\text{Hash}$ od 64 bajta koji ćemo podeliti na 2 dela od po 32 bajta, $h_1$ i $h_2$:



$$

\text{hash} = h_1 \Vert h_2

$$



$$

h_1 = \text{hash}[:32] \quad, \quad h_2 = \text{hash}[32:]

$$


Javni ključ deteta $K_{\text{CHD}}^n$ se zatim izračunava na sledeći način:


$$
K_{\text{CHD}}^n = \text{parse256}(h_1) \cdot G + K_{\text{PAR}}
$$


Ako je $\text{parse256}(h_1) \geq n$ (red eliptičke krive) ili ako je $K_{\text{CHD}}^n$ tačka u beskonačnosti, derivacija je nevažeća i mora se izabrati drugi indeks.


U ovom proračunu, operacija $\text{parse256}(h_1)$ uključuje interpretaciju prvih 32 bajta $\text{Hash}$ kao 256-bitnog celog broja. Ovaj broj se koristi za izračunavanje tačke na eliptičnoj krivoj kroz sabiranje i udvostručavanje od generatora tačke $G$. Ova tačka se zatim dodaje roditeljskom javnom ključu kako bi se dobio normalni dečiji javni ključ. Dakle, za izvođenje normalnog dečijeg javnog ključa, potrebni su samo roditeljski javni ključ i roditeljski lančani kod; roditeljski privatni ključ nikada ne ulazi u ovaj proces, za razliku od izračunavanja dečijeg privatnog ključa koji smo ranije videli.


Dalje, kod lanca za dete je jednostavno:


$$
C_{\text{CHD}} = h_2
$$


Evo šematskog prikaza celokupne izvedbe:


![CYP201](assets/fr/052.webp)


### Korespondencija između javnih i privatnih ključeva deteta


Pitanje koje se može postaviti je kako normalni javni ključ deteta izveden iz roditeljskog javnog ključa može odgovarati normalnom privatnom ključu deteta izvedenom iz odgovarajućeg roditeljskog privatnog ključa. Ova veza je precizno osigurana svojstvima eliptičkih krivih. Naime, za izvođenje normalnog javnog ključa deteta, HMAC-SHA512 se primenjuje na isti način, ali se njegov izlaz koristi drugačije:


   - **Normalan privatni ključ deteta**: $k_{\text{CHD}}^n = \text{parse256}(h_1) + k_{\text{PAR}} \mod n$
   - **Normalan javni ključ deteta**: $K_{\text{CHD}}^n = \text{parse256}(h_1) \cdot G + K_{\text{PAR}}$


Zahvaljujući operacijama sabiranja i udvostručavanja na eliptičnoj krivi, obe metode proizvode dosledne rezultate: javni ključ izveden iz privatnog ključa deteta je identičan javnom ključu deteta izvedenom direktno iz javnog ključa roditelja.


### Rezime tipova derivacija


Da rezimiramo, evo različitih mogućih tipova derivacija:


$$
\begin{array}{|c|c|c|c|}
\hline
\rightarrow & \text{PAR} & \text{CHD} & \text{n/h} \\
\hline
k_{\text{PAR}} \rightarrow k_{\text{CHD}} & k_{\text{PAR}} & \{ k_{\text{CHD}}^n, k_{\text{CHD}}^h \} & \{ n, h \} \\
k_{\text{PAR}} \rightarrow K_{\text{CHD}} & k_{\text{PAR}} & \{ K_{\text{CHD}}^n, K_{\text{CHD}}^h \} & \{ n, h \} \\
K_{\text{PAR}} \rightarrow k_{\text{CHD}} & K_{\text{PAR}} & \times & \times \\
K_{\text{PAR}} \rightarrow K_{\text{CHD}} & K_{\text{PAR}} & K_{\text{CHD}}^n & n \\
\hline
\end{array}
$$


Do sada ste naučili kako da kreirate osnovne elemente HD novčanika: bezbednosnu frazu, seed, a zatim glavni ključ i glavni kod lanca. Takođe ste otkrili kako da izvedete parove ključeva za decu u ovom poglavlju. U sledećem poglavlju, istražićemo kako su ove izvedbe organizovane u Bitcoin novčanicima i koju strukturu treba pratiti da bi se konkretno dobile adrese za primanje, kao i parovi ključeva korišćeni u *scriptPubKey* i *scriptSig*.


## Struktura novčanika i putanje derivacije

<chapterId>34e1bbda-67de-5493-b268-1fded8d67689</chapterId>


Hijerarhijska struktura HD novčanika u Bitcoin-u omogućava organizaciju parova ključeva na različite načine. Ideja je da se iz glavnog privatnog ključa i glavnog lanca koda izvedu različiti nivoi dubine. Svaki dodati nivo odgovara derivaciji para ključeva deteta iz para ključeva roditelja.


Tokom vremena, različiti BIP-ovi su uveli standarde za ove putanje derivacije, s ciljem standardizacije njihove upotrebe u različitim softverima. Dakle, u ovom poglavlju ćemo otkriti značenje svakog nivoa derivacije u HD novčanicima, prema tim standardima.


### Dubine derivacije HD novčanicima


Putanje derivacije su organizovane u slojeve dubine, počevši od dubine 0, koja predstavlja master ključ i master lančani kod, do slojeva podnivoa za derivaciju adresa koje se koriste za zaključavanje UTXO-a. BIP-ovi (*Bitcoin Improvement Proposals*) definišu standarde za svaki nivo, što pomaže u harmonizaciji praksi među različitim softverima novčanika za upravljanje.


Putanja derivacije, dakle, odnosi se na sekvencu indeksa korišćenih za izvođenje podključeva iz glavnog ključa.


**Dubina 0: Glavni ključ (BIP32)**


Ova dubina odgovara glavnom privatnom ključu i glavnom lancu koda novčanika. Predstavlja se notacijom $m/$.


**Dubina 1: Svrha (BIP43)**


Svrha određuje logičku strukturu izvođenja. Na primer, P2WPKH Address će imati $/84'/$ na dubini 1 (prema BIP84), dok će P2TR Address imati $/86'/$ (prema BIP86). Ovaj nivo olakšava kompatibilnost između novčanika označavanjem brojeva indeksa koji odgovaraju BIP brojevima.


Drugim rečima, kada imate glavni ključ i glavni lančani kod, oni služe kao roditeljski par ključeva za izvođenje para dečijih ključeva. Indeks korišćen u ovoj izvedbi može biti, na primer, $/84'/$ ako je novčanik namenjen za korišćenje SegWit v0 tip skripti. Ovaj par ključeva je tada na dubini 1. Njegova uloga nije da zaključava bitkoine, već jednostavno da služi kao međutačka u hijerarhiji izvođenja.


**Dubina 2: Tip valute (BIP44)**


Iz para ključeva na dubini 1, vrši se nova derivacija kako bi se dobio par ključeva na dubini 2. Ova dubina omogućava razlikovanje Bitcoin naloga od drugih kriptovaluta unutar istog novčanika.


Svaka valuta ima jedinstveni indeks kako bi se osigurala kompatibilnost između novčanika sa više valuta. Na primer, za Bitcoin, indeks je $/0'/$ (ili `0x80000000` u heksadecimalnoj notaciji). Indeksi valuta se biraju u opsegu od $2^{31}$ do $2^{32}-1$ kako bi se osigurala ojačana derivacija.


Da bih vam dao druge primere, evo indeksa nekih valuta:


- $1'$ (`0x80000001`) za Testnet bitkoina;
- $2'$ (`0x80000002`) za Litecoin;
- $60'$ (`0x8000003c`) za Ethereum...


**Dubina 3: Nalog (BIP32)**


Svaki novčanik može biti podeljen na nekoliko naloga, numerisanih od $2^{31}$, i predstavljenih na dubini 3 sa $/0'/$ za prvi nalog, $/1'/$ za drugi, i tako dalje. Generalno, kada se pominje prošireni ključ `xpub`, to se odnosi na ključeve na ovoj dubini derivacije.


Ova podela na različite naloge je opcionalna. Cilj joj je da pojednostavi organizaciju novčanika za korisnike. U praksi se često koristi samo jedan nalog, obično prvi po defaultu. Međutim, u nekim slučajevima, ako neko želi jasno da razlikuje parove ključeva za različite namene, ovo može biti korisno. Na primer, moguće je kreirati lični nalog i profesionalni nalog iz istog seed-a, sa potpuno različitim grupama ključeva od ove dubine derivacije.


**Dubina 4: Lanac (BIP32)**


Svaki nalog definisan na dubini 3 je zatim strukturisan u dva lanca:


- **Eksterni lanac**: U ovom lancu se izvode takozvane "javne" adrese. Ove adrese za primanje su namenjene za zaključavanje UTXO-a koji dolaze iz eksternih transakcija (odnosno, koji potiču iz potrošnje UTXO-a koji ne pripadaju vama). Jednostavno rečeno, ovaj eksterni lanac se koristi kad god želite da primite bitkoine. Kada kliknete na "*primi*" u vašem novčanik softveru, uvek vam se nudi adresa iz eksternog lanca. Ovaj lanac je predstavljen parom ključeva izvedenih sa indeksom $/0/$.
- **Interni lanac (kusur)**: Ovaj lanac je rezervisan za primanje adresa koje zaključavaju bitkoine dolazeći od potrošnje UTXO-a koji pripadaju vama, drugim rečima, adrese za kusur. Identifikovan je indeksom $/1/$.


**Dubina 5: Indeks adrese (BIP32)**


Konačno, dubina 5 predstavlja poslednji korak derivacije u novčaniku. Iako je tehnički moguće nastaviti beskonačno, trenutni standardi se zaustavljaju ovde. Na ovoj konačnoj dubini, parovi ključeva koji će zapravo biti korišćeni za zaključavanje i otključavanje UTXO-a su izvedeni. Svaki indeks omogućava razlikovanje između parova ključeva braće i sestara: tako će prva prijemna adresa koristiti indeks $/0/$, druga indeks $/1/$, i tako dalje.


![CYP201](assets/fr/053.webp)


### Označavanje putanja derivacije


Putanja derivacije se piše razdvajanjem svakog nivoa kosom crtom ($/$). Svaka kosa crta tako označava derivaciju roditeljskog para ključeva ($k_{\text{PAR}}$, $K_{\text{PAR}}$, $C_{\text{PAR}}$) do para ključeva deteta ($k_{\text{CHD}}$, $K_{\text{CHD}}$, $C_{\text{CHD}}$). Broj naveden na svakoj dubini odgovara indeksu koji se koristi za izvođenje ovog ključa iz njegovih roditelja. Apostrof ($'$) ponekad postavljen desno od indeksa označava ojačanu derivaciju ($k_{\text{CHD}}^h$, $K_{\text{CHD}}^h$). Ponekad se ovaj apostrof zamenjuje sa $h$. U odsustvu apostrofa ili $h$, u pitanju je normalna derivacija ($k_{\text{CHD}}^n$, $K_{\text{CHD}}^n$).

Kao što smo videli u prethodnim poglavljima, indeksi ojačanih ključeva počinju od $2^{31}$, ili `0x80000000` u heksadecimalnom obliku. Stoga, kada indeks prati apostrof u putanji derivacije, $2^{31}$ mora biti dodato naznačenom broju da bi se dobila stvarna vrednost koja se koristi u HMAC-SHA512 funkciji. Na primer, ako putanja derivacije specificira $/44'/$, stvarni indeks će biti:

$$

i = 44 + 2^{31} = 2\,147\,483\,692

$$


U heksadecimalnom formatu, ovo je `0x8000002C`.


Sada kada smo razumeli glavne principe putanja derivacije, hajde da uzmemo primer! Evo putanje derivacije za Bitcoin primajuću adresu:



$$

m / 84' / 0' / 1' / 0 / 7

$$


U ovom primeru:


- $84'$ označava standard P2WPKH (SegWit v0);
- $0'$ označava valutu Bitcoin na Mainnet;
- $1'$ odgovara drugom nalogu u novčaniku;
- $0$ označava da je adresa na eksternom lancu;
- $7$ označava 8. eksternu adresu na ovom nalogu.


### Rezime strukture izvođenja


|Dubina | Opis               | Standardni primer                 |
| ----- | ------------------ | --------------------------------- |
| 0     | Glavni ključ       | $m/$                              |
| 1     | Svrha              | $/86'/$ (P2TR)                    |
| 2     | Valuta             | $/0'/$ (Bitcoin)                  |
| 3     | Nalog              | $/0'/$ (Prvi nalog)               |
| 4     | Lanac              | $/0/$ (eksterni) ili $/1/$ (kusur)|
| 5     | Indeks adrese      | $/0/$ (prva adresa)               |

U sledećem poglavlju, otkrićemo šta su "*output script descriptors*", nedavno uvedena inovacija u Bitcoin Core-u koja pojednostavljuje pravljenje rezervne kopije (bekap) Bitcoin novčanika.


## Izlazni opisi skripti (eng. output script descriptors)

<chapterId>e4f1c2d3-9b8a-4d3e-8f2a-7b6c5d4e3f2a</chapterId>

Često vam se govori da je sama bezbednosna fraza dovoljna za povratak pristupa novčaniku. U stvarnosti, stvari su malo složenije. U prethodnom poglavlju smo pogledali strukturu derivacije HD novčanika, i možda ste primetili da je ovaj proces prilično složen. Derivacioni putevi govore softveru koji pravac da prati kako bi izveo korisničke ključeve. Međutim, prilikom oporavka Bitcoin novčanika, ako neko ne zna ove puteve, sama bezbednosna fraza nije dovoljna. Ona omogućava dobijanje glavnog ključa i glavnog lanca koda, ali je onda potrebno znati indekse korišćene za dostizanje podređenih ključeva.


Teoretski, bilo bi neophodno sačuvati ne samo bezbednosnu frazu našeg novčanika već i puteve do naloga koje koristimo. U praksi, često je moguće povratiti pristup dečijim ključevima bez ovih informacija, pod uslovom da su standardi ispoštovani. Testiranjem svakog standarda jedan po jedan, generalno je moguće povratiti pristup bitkoinima. Međutim, ovo nije zagarantovano i posebno je komplikovano za početnike. Takođe, sa diverzifikacijom tipova skripti i pojavom složenijih konfiguracija, ove informacije bi mogle postati teške za ekstrapolaciju, čime se ovi podaci pretvaraju u privatne informacije koje je teško povratiti silovitom pretragom. Zbog toga je nedavno uvedena inovacija koja počinje da se integriše u vaš omiljeni softverski novčanik: *izlazni opisi skripti*.


### Šta je "opis (descriptor)"?


"*output script descriptors*", ili jednostavno "*deskriptori*", su strukturirani izrazi koji u potpunosti opisuju izlazni skript (*scriptPubKey*) i pružaju sve neophodne informacije za praćenje transakcija povezanih sa određenom skriptom. Oni olakšavaju upravljanje ključevima u HD novčanicima nudeći standardizovan i potpun opis strukture novčanika i tipova adresa koje se koriste.


Glavna prednost deskriptora leži u njihovoj sposobnosti da enkapsuliraju sve bitne informacije za oporavak novčanika u jedan niz (pored fraze za oporavak). Čuvanjem deskriptora sa povezanom bezbednosnim frazama, postaje moguće vratiti privatne ključeve preciznim poznavanjem njihove pozicije u hijerarhiji. Za višepotpisne novčanike, čija je rezervna kopija u početku bila složenija, deskriptor uključuje `xpub` svakog faktora, čime se osigurava mogućnost regenerisanja adresa u slučaju problema.


### Izgradnja deskriptora


Opis se sastoji od nekoliko elemenata:


- Skripte funkcije kao što su `pk` (*Pay-to-PubKey*), `pkh` (*Pay-to-PubKey-Hash*), `wpkh` (*Pay-to-Witness-PubKey-Hash*), `sh` (*Pay-to-Script-Hash*), `wsh` (*Pay-to-Witness-Script-Hash*), `tr` (*Pay-to-Taproot*), `multi` (*Multisignature*), i `sortedmulti` (*Multisignature with sorted keys*);
- Putanje derivacije, na primer, `[d34db33f/44h/0h/0h]` označava putanju izvedenog naloga i specifičan otisak prsta glavnog ključa;
- Ključevi u različitim formatima kao što su heksadecimalni javni ključevi ili prošireni javni ključevi (`xpub`);
- Kontrolni zbir, prethodi mu znak Hash, za proveru integriteta deskriptora.


Na primer, opis za P2WPKH (SegWit v0) novčanik mogao bi izgledati ovako:


```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7nr4
```


U ovom opisu, funkcija derivacije `wpkh` označava tip skripte *Pay-to-Witness-Public-Key-Hash*. Sledi putanja derivacije koja sadrži:


- `cdeab12f`: otisak glavnog ključa;
- `84h`: što označava upotrebu BIP84 svrhe, namenjene za SegWit v0 adrese;
- `0h`: što ukazuje da je to BTC valuta na Mainnet;
- `0h`: što se odnosi na specifičan broj naloga korišćen u novčaniku.


Opis takođe uključuje prošireni javni ključ korišćen u ovom novčaniku:


```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```


Notacija `/<0;1>/*` označava da deskriptor može generisati adrese iz spoljnog lanca (`0`) i iz unutrašnjeg lanca (`1`). Džoker znak (`*`) na kraju putanje znači da se sa ove pozicije mogu sekvencijalno izvesti svi neojačani („*unhardened*“) podključevI, bilo da su to spoljne ili unutrašnje adrese. Ova sintaksa ne podrazumeva direktno pojam *gap limit*, koji pripada mehanizmu specifičnom za novčanike za detekciju adresa, već ovde služi samo da pokaže da se sve moguće derivacije na ovoj poziciji uzimaju u obzir.


Konačno, `#jy0l7nr4` predstavlja kontrolni zbir za verifikaciju integriteta deskriptora.


Sada znate sve o radu HD novčanika u Bitcoin-u i procesu derivacije parova ključeva. Međutim, u poslednjim poglavljima smo se ograničili na generisanje privatnih i javnih ključeva, bez bavljenja konstrukcijom adresa za primanje. Upravo će to biti tema sledećeg poglavlja!


## Adrese za primanje

<chapterId>ca80a89d-f8da-4e09-8c35-43179b65bced</chapterId>


Primajuće adrese su delovi informacija ugrađeni u *scriptPubKey* kako bi zaključali novo kreirane UTXO-e. Jednostavno rečeno, adresa služi za primanje bitkoina. Hajde da istražimo njihovo funkcionisanje u vezi sa onim što smo proučavali u prethodnim poglavljima.


### Uloga Bitcoin adresa u skriptama


Kao što je ranije objašnjeno, uloga transakcije je da prenese vlasništvo nad bitkoinima sa ulaza na izlaze. Ovaj proces uključuje korišćenje UTXO-a kao ulaza dok se kreiraju novi UTXO-vi kao izlazi. Ovi UTXO-i su osigurani skriptama, koje definišu neophodne uslove za otključavanje sredstava.


Kada korisnik primi bitkoine, pošiljalac kreira UTXO i zaključava ga pomoću *scriptPubKey*. Ovaj skript sadrži pravila za otključavanje UTXO, obično navodeći potpise i javne ključeve koji su potrebni. Da bi potrošio ovaj UTXO u novoj transakciji, korisnik mora obezbediti tražene informacije putem *scriptSig*. Izvršenje *scriptSig* u kombinaciji sa *scriptPubKey* mora vratiti "true" ili `1`. Ako je ovaj uslov ispunjen, UTXO se može potrošiti za kreiranje novog UTXO, koji je sam zaključan novim *scriptPubKey*, i tako dalje.


![CYP201](assets/fr/054.webp)


Upravo u *scriptPubKey* se nalaze adrese primaoca. Međutim, njihova upotreba varira u zavisnosti od usvojenog standarda skripte. Ovde je tabela sažetka informacija sadržanih u *scriptPubKey* prema korišćenom standardu, kao i informacija koje se očekuju u *scriptSig* da bi se otključao *scriptPubKey*.


| Standard           | *scriptPubKey*                                              | *scriptSig*                     | *redeem script*     | *witness*                                |
| ------------------ | ----------------------------------------------------------- | ------------------------------- | ------------------- | ---------------------------------------- |
| P2PK               | `<pubkey> OP_CHECKSIG`                                      | `<signature>`                   |                     |                                          |
| P2PKH              | `OP_DUP OP_HASH160 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG` | `<signature> <public key>`      |                     |                                          |
| P2SH               | `OP_HASH160 <scriptHash> OP_EQUAL`                          | `<data pushes> <redeem script>` | Arbitrary data     |                                          |
| P2WPKH             | `0 <pubKeyHash>`                                            |                                 |                     | `<signature> <public key>`               |
| P2WSH              | `0 <witnessScriptHash>`                                     |                                 |                     | `<data pushes> <witness script>`         |
| P2SH-P2WPKH        | `OP_HASH160 <redeemScriptHash> OP_EQUAL`                    | `<redeem script>`               | `0 <pubKeyHash>`    | `<signature> <public key>`               |
| P2SH-P2WSH         | `OP_HASH160 <redeemScriptHash> OP_EQUAL`                    | `<redeem script>`               | `0 <scriptHash>`    | `<data pushes> <witness script>`         |
| P2TR (key path)    | `1 <public key>`                                            |                                 |                     | `<signature>`                            |
| P2TR (script path) | `1 <public key>`                                            |                                 |                     | `<data pushes> <script> <control block>` |

*Izvor: Bitcoin Core PR review club, 7. jul 2021 - Gloria Zhao*


Opkodovi korišćeni u skripti su dizajnirani da manipulišu informacijama i, ako je potrebno, da ih uporede ili testiraju. Uzmimo primer P2PKH skripte, koja je sledeća:


```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG
```


Kao što ćemo videti u ovom poglavlju, `<pubKeyHash>` zapravo predstavlja sadržaj primajuće adrese korišćene za zaključavanje UTXO. Da bi se otključao ovaj *scriptPubKey*, potrebno je obezbediti *scriptSig* koji sadrži:


```text
<signature> <public key>
```


U skriptnom jeziku, stek je *LIFO* ("*Poslednji unutra, prvi van (eng. Last In, First Out*")) struktura podataka koja se koristi za privremeno skladištenje elemenata tokom izvršavanja skripte. Svaka operacija skripte manipuliše ovim stekom, gde se element može dodati (*push*) ili ukloniti (*pop*). Skripte koriste stek za evaluaciju izraza, skladištenje privremenih varijabli i upravljanje uslovima.


Izvršenje skripte koju sam upravo dao kao primer prati ovaj proces:



- Imamo *scriptSig*, *scriptPubKey* i stek:


![CYP201](assets/fr/055.webp)



- *scriptSig* je gurnut na stek:


![CYP201](assets/fr/056.webp)



- `OP_DUP` duplira javni ključ naveden u *scriptSig* na steku:


![CYP201](assets/fr/057.webp)



- `OP_HASH160` vraća heš javnog ključa koji je upravo dupliran:


![CYP201](assets/fr/058.webp)



- `OP_PUSHBYTES_20 <pubKeyHash>` postavlja Bitcoin adresu sadržanu u *scriptPubKey* na stek:


![CYP201](assets/fr/059.webp)



- `OP_EQUALVERIFY` proverava da li se heširani javni ključ poklapa sa datom primajućom adresom:


![CYP201](assets/fr/060.webp)


`OP_CHECKSIG` proverava potpis sadržan u *scriptSig* koristeći javni ključ. Ovaj opkode u suštini vrši proveru potpisa kao što smo opisali u delu 3 ove obuke:



![CYP201](assets/fr/061.webp)



- Ako `1` ostane na steku, onda je skripta važeća:


![CYP201](assets/fr/062.webp)


Stoga, da rezimiramo, ovaj skript omogućava verifikaciju, uz pomoć digitalnog potpisa, da korisnik koji tvrdi da je vlasnik ovog UTXO-a i želi da ga potroši zaista poseduje privatni ključ povezan sa prijemnom adresom korišćenom tokom kreiranja ovog UTXO.


### Različite vrste Bitcoin adresa


Tokom evolucije Bitcoin-a, dodato je nekoliko standardnih modela skripti. Svaki od njih koristi različitu vrstu prijemne adrese. Ovde je pregled glavnih modela skripti dostupnih do danas:


**P2PK (*Pay-to-PubKey*)**:


Ovaj model skripte je uveden u prvoj verziji Bitcoin-a od strane Satoshi Nakamoto. P2PK skripta zaključava bitkoine direktno koristeći sirovi javni ključ (dakle, nijedna prijemna adresa se ne koristi sa ovim modelom). Njegova struktura je jednostavna: sadrži javni ključ i zahteva odgovarajući digitalni potpis za otključavanje sredstava. Ova skripta je deo "*Legacy*" standarda.


**P2PKH (*Pay-to-PubKey-Hash*)**:


Kao P2PK, P2PKH skripta je uvedena prilikom lansiranja Bitcoin-a. Za razliku od svog prethodnika, ona zaključava bitkoine koristeći heš javnog ključa, umesto da direktno koristi nehešovan javni ključ. *scriptSig* tada mora obezbediti javni ključ povezan sa primajućom adresom, kao i važeći potpis. Adrese koje odgovaraju ovom modelu počinju sa `1` i kodirane su u *base58check*. Ova skripta takođe pripada "*Legacy*" standardu.


**P2SH (*Pay-to-Script-Hash*)**:


Uveden 2012. sa BIP16, model P2SH omogućava korišćenje heša proizvoljne skripte u *scriptPubKey*. Ovaj heširani skript, nazvan "*redeemscript*", sadrži uslove za otključavanje sredstava. Da bi se potrošio UTXO zaključan sa P2SH, potrebno je obezbediti *scriptSig* koji sadrži originalni *redeemscript* kao i potrebne podatke za njegovu validaciju. Ovaj model se posebno koristi za stare multisigove. Adrese povezane sa P2SH počinju sa `3` i kodirane su u *base58check*. Ovaj skript takođe pripada "*Legacy*" standardu.


**P2WPKH (*Pay-to-Witness-PubKey-Hash*)**:


Ovaj skript je sličan P2PKH, jer takođe zaključava bitkoine koristeći heš javnog ključa. Međutim, za razliku od P2PKH, *scriptSig* je premešten u poseban deo nazvan "*Witness*". Ovo se ponekad naziva "*scriptWitness*" da označi skup koji obuhvata potpis i javni ključ. Svaki SegWit ulaz ima svoj *scriptWitness*, a kolekcija *scriptWitnesses* čini *Witness* polje transakcije. Ovo premeštanje podataka o potpisu je inovacija uvedena SegWit ažuriranjem, posebno usmerena na sprečavanje izmenljivosti transakcija kod ECDSA potpisa.

P2WPKH koristi *bech32* kodiranje i uvek počinje sa `bc1q`. Ovaj tip skripte odgovara verziji 0 SegWit izlaza.


**P2WSH (*Pay-to-Witness-Script-Hash*)**:


Model P2WSH je takođe uveden sa ažuriranjem SegWit u avgustu 2017. Slično modelu P2SH, zaključava bitkoine koristeći heš skripte. Glavna razlika leži u načinu na koji se potpisi i skripte uključuju u transakciju. Da bi se potrošili bitkoini zaključani ovim tipom skripte, primalac mora obezbediti originalnu skriptu, zvanu *witnessScript* (ekvivalentno *redeemscript* u P2SH), zajedno sa neophodnim podacima za validaciju ove *witnessScript*. Ovaj mehanizam omogućava implementaciju složenijih uslova trošenja, kao što su multisigs.


P2WSH adrese koriste *bech32* kodiranje i uvek počinju sa `bc1q`. Ovaj skript takođe odgovara verziji 0 SegWit izlaza.


**P2TR (*Pay-to-Taproot*)**:


Model P2TR je uveden sa implementacijom Taproot u novembru 2021. Baziran je na Schnorr protokolu za kriptografsko agregiranje ključeva, kao i na Merkle Tree-u za alternativne skripte, nazvane MAST (*Merkelized Alternative Script Tree*). Za razliku od drugih tipova skripti, gde su uslovi trošenja javno izloženi (bilo pri prijemu ili pri trošenju), P2TR omogućava skrivanje kompleksnih skripti iza jednog, prividnog javnog ključa.


Tehnički, P2TR skripta zaključava bitkoine na jedinstveni Schnorr javni ključ, označen kao $Q$. Ovaj ključ $Q$ je zapravo agregat javnog ključa $P$ i javnog ključa $M$, pri čemu se potonji izračunava kao Merkle Root iz liste *scriptPubKey-jeva*. Bitkoini zaključani ovom vrstom skripte mogu se potrošiti na dva načina:


- Objavljivanjem potpisa za javni ključ $P$ (*putanja ključa*).
- Ispunjavanjem jednog od skripti sadržanih u Merkle Tree-u (*putanja skripte*).


P2TR tako nudi veliku fleksibilnost, jer omogućava zaključavanje bitkoina bilo sa jedinstvenim javnim ključem, sa nekoliko skripti po izboru, ili oba istovremeno. Prednost ove Merkle Tree strukture je da se tokom transakcije otkriva samo skripta koja se koristi za trošenje, dok sve druge alternativne skripte ostaju tajne.


![CYP201](assets/fr/063.webp)


P2TR odgovara verziji 1 SegWit izlaza, što znači da su potpisi za P2TR ulaze pohranjeni u *Witness* sekciju transakcije, a ne u *scriptSig*. P2TR adrese koriste *bech32m* kodiranje i počinju sa `bc1p`, ali su prilično jedinstvene jer ne koriste heš funkciju za svoju konstrukciju. Zapravo, one direktno predstavljaju javni ključ $Q$ koji je jednostavno formatiran sa metapodacima. Dakle, to je skript model blizak P2PK.


Sada kada smo pokrili teoriju, pređimo na praksu! U sledećem poglavlju, predlažem izvođenje i SegWit v0 Address i SegWit v1 Address iz para ključeva.


## Izvođenje adresa

<chapterId>3ebdc750-4135-4881-b07e-08965941b93e</chapterId>


Hajde da zajedno istražimo kako da generišete adresu za primanje iz para ključeva lociranih, na primer, na dubini 5 HD novčanika. Ova adresa se zatim može koristiti u novčanik softveru za zaključavanje UTXO-a.


Pošto proces generisanja adresa zavisi od usvojenog modela skripte, fokusirajmo se na dva specifična slučaja: generisanje SegWit v0 adrese u P2WPKH i SegWit v1 adrese u P2TR. Ove dve vrste adresa pokrivaju veliku većinu današnjih upotreba.


### Kompresija javnog ključa


Nakon izvođenja svih koraka derivacije od glavnog ključa do dubine 5 koristeći odgovarajuće indekse, dobijamo par ključeva ($k$, $K$) sa $K = k \cdot G$. Iako je moguće koristiti ovaj javni ključ kao takav za zaključavanje sredstava sa P2PK standardom, to nije naš cilj ovde. Umesto toga, cilj nam je da kreiramo adresu u P2WPKH u prvom slučaju, a zatim u P2TR za drugi primer.


Prvi korak je kompresija javnog ključa $K$. Da bismo dobro razumeli ovaj proces, prvo se prisetimo nekih osnovnih pojmova obrađenih u delu 3.

Javni ključ u Bitcoin-u je tačka $K$ koja se nalazi na eliptičnoj krivi. Predstavljen je u obliku $(x, y)$, gde su $x$ i $y$ koordinate tačke. U svom nekompresovanom obliku, ovaj javni ključ je dužine 520 bita: 8 bita za prefiks (početna vrednost `0x04`), 256 bita za $x$ koordinatu i 256 bita za $y$ koordinatu.

Međutim, eliptičke krive imaju svojstvo simetrije u odnosu na x-osu: za datu $x$ koordinatu, postoje samo dve moguće vrednosti za $y$: $y$ i $-y$. Ove dve tačke se nalaze sa obe strane x-ose. Drugim rečima, ako znamo $x$, dovoljno je odrediti da li je $y$ paran ili neparan da bismo identifikovali tačnu tačku na krivi.


![CYP201](assets/fr/064.webp)


Da bi se kompresovao javni ključ, kodira se samo $x$, koji zauzima 256 bita, i dodaje se prefiks da bi se specificirala parnost $y$. Ova metoda smanjuje dužinu javnog ključa na 264 bita umesto početnih 520. Prefiks `0x02` označava da je $y$ paran, a prefiks `0x03` označava da je $y$ neparan.


Hajde da uzmemo primer da bismo bolje razumeli, sa nekodiranim javnim ključem u nekompresovanoj reprezentaciji:


```text
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```


Ako razložimo ovaj ključ, imamo:


   - Prefiks: `04`;
   - $x$: `678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6`;
   - $y$: `49f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f`


Poslednji heksadecimalni karakter od $y$ je `f`. U dekadnom (desetnom) sistemu, `f = 15`, što odgovara neparnom broju. Dakle, $y$ je neparan, i prefiks će biti `0x03` da bi to označio.


Kompresovani javni ključ postaje:


```text
K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6
```

Ova operacija se primenjuje na sve modele skripti zasnovane na ECDSA, to jest, sve osim P2TR koji koristi Schnorr. U slučaju Schnorr-a, kao što je objašnjeno u delu 3, zadržavamo samo vrednost $x$, bez dodavanja prefiksa za označavanje pariteta $y$, za razliku od ECDSA. Ovo je omogućeno činjenicom da je jedinstveni paritet proizvoljno izabran za sve ključeve. Ovo omogućava blago smanjenje prostora za skladištenje potrebnog za javne ključeve.

### Izvođenje SegWit v0 (bech32) adrese


Sada kada smo dobili naš kompresovani javni ključ, možemo izvesti SegWit v0 primajuću adresu iz njega.


Prvi korak je primena HASH160 heš funkcije na kompresovani javni ključ. HASH160 je kompozicija dve uzastopne heš funkcije: SHA256, praćena sa RIPEMD160:



$$

\text{HASH160}(K) = \text{RIPEMD160}(\text{SHA256}(K))

$$


Prvo, propuštamo ključ kroz SHA256:


```text
SHA256(K) = C489EBD66E4103B3C4B5EAFF462B92F5847CA2DCE0825F4997C7CF57DF35BF3A
```


Zatim propuštamo rezultat kroz RIPEMD160:


```text
RIPEMD160(SHA256(K)) = 9F81322CC88622CA4CCB2A52A21E2888727AA535
```


Dobili smo 160-bitni heš javnog ključa, koji čini ono što se naziva payload adrese. Ovaj payload predstavlja centralni i najvažniji deo adrese. Takođe se koristi u *scriptPubKey* za zaključavanje UTXO-a.


Međutim, da bi ovaj payload bio lakše upotrebljiv za ljude, dodaje mu se metapodatak. Sledeći korak uključuje kodiranje ovog heša u grupe od 5 bita u decimalnom obliku. Ova decimalna transformacija će biti korisna za konverziju u *bech32*, koji se koristi za adrese posle SegWit. Binarnom hešu od 160 bita se tako deli na 32 grupe od po 5 bita:



$$

\begin{array}{|c|c|}
\hline
\text{5 bits} & \text{Decimal} \\
\hline
10011 & 19 \\
11110 & 30 \\
00000 & 0 \\
10011 & 19 \\
00100 & 4 \\
01011 & 11 \\
00110 & 6 \\
01000 & 8 \\
10000 & 16 \\
11000 & 24 \\
10001 & 17 \\
01100 & 12 \\
10100 & 20 \\
10011 & 19 \\
00110 & 6 \\
01011 & 11 \\
00101 & 5 \\
01001 & 9 \\
01001 & 9 \\
01010 & 10 \\
00100 & 4 \\
00111 & 7 \\
10001 & 17 \\
01000 & 8 \\
10001 & 17 \\
00001 & 1 \\
11001 & 25 \\
00111 & 7 \\
10101 & 21 \\
00101 & 5 \\
00101 & 5 \\
10101 & 21 \\
\hline
\end{array}

$$

Dakle, imamo:


```text
HASH = 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21
```


Kada je heš kodiran u grupe od 5 bita, kontrolni zbir se dodaje na adresu. Ovaj kontrolni zbir se koristi za proveru da payload adrese nije izmenjen tokom skladištenja ili prenosa. Na primer, omogućava softveru novčanika da osigura da niste napravili grešku prilikom unosa primajuće adrese. Bez ove provere, mogli biste slučajno poslati bitkoine na pogrešnu adresu, što bi rezultiralo trajnim gubitkom sredstava, jer ne posedujete povezani javni ili privatni ključ. Stoga, kontrolni zbir je zaštita protiv ljudskih grešaka.


Kod starih Bitcoin Legacy adresa, kontrolna suma se dobijala primenom HASH256 funkcije na početni deo heša adrese. Sa uvođenjem SegWit i *bech32* formata, sada se koriste BCH kodovi (*Bose, Ray-Chaudhuri, i Hocquenghem*). Ovi kodovi za ispravljanje grešaka koriste se za otkrivanje i ispravljanje grešaka u sekvencama podataka. Oni osiguravaju da prenesene informacije stignu netaknute na svoje odredište, čak i u slučaju manjih izmjena. BCH kodovi se koriste u mnogim oblastima, kao što su SSD-ovi, DVD-ovi i QR kodovi. Na primer, zahvaljujući ovim BCH kodovima, delimično zaklonjen QR kod i dalje može biti pročitan i dekodiran.


U kontekstu Bitcoin-a, BCH kodovi nude bolji kompromis između veličine i sposobnosti detekcije grešaka u poređenju sa jednostavnim heš funkcijama korišćenim za *Legacy* adrese. Međutim, u Bitcoin-u, BCH kodovi se koriste samo za detekciju grešaka, ne i za ispravljanje. Dakle, softver novčanik će signalizirati netačnu prijemnu adresu ali ga neće automatski ispraviti. Ovo ograničenje je namerno: omogućavanje automatskog ispravljanja bi smanjilo sposobnost detekcije grešaka.


Da bismo izračunali kontrolni zbir sa BCH kodovima, potrebno je pripremiti nekoliko elemenata.


- **HRP (*Deo adrese čitljiv za čoveka eng.Human Readable Part*)**: Za Bitcoin Mainnet, HRP je `bc`;


HRP mora biti proširen razdvajanjem svakog karaktera na dva dela:


- Uzimajući karaktere HRP u ASCII:
 - `b`: `01100010`
 - `c`: `01100011`
- Izdvajanje 3 najznačajnija bita i 5 najmanje značajnih bitova:
  - 3 najznačajnija bita: `011` (3 u dekadnom sistemu)
  - 3 najznačajnija bita: `011` (3 u dekadnom sistemu)
  - 5 najmanje značajnih bitova: `00010` (2 u dekadnom sistemu)
  - 5 najmanje značajnih bita: `00011` (3 u dekadnom sistemu)


Sa separatorom `0` između dva karaktera, HRP ekstenzija je stoga:


```text
03 03 00 02 03
```



- **Verzija svedoka**: Za SegWit verziju 0, to je `00`;



- **Payload**: Dekadne vrednosti heša javnog ključa;



- **Rezervacija za kontrolni zbir**: Dodajemo 6 nula `[0, 0, 0, 0, 0, 0]` na kraj niza.


Svi podaci kombinovani za unos u program za izračunavanje kontrolnog zbira su sledeći:


```text
HRP = 03 03 00 02 03
SEGWIT v0 = 00
HASH = 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21
CHECKSUM = 00 00 00 00 00 00

INPUT = 03 03 00 02 03 00 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21 00 00 00 00 00 00
```


Izračun kontrolnog zbira je prilično složen. Uključuje aritmetiku polinoma u konačnim poljima. Nećemo detaljisati ovaj izračun ovde i preći ćemo direktno na rezultat. U našem primeru, kontrolni zbir dobijen u decimalnom obliku je:


```text
10 16 11 04 13 18
```


Sada možemo konstruisati prijemnu adresu konkatenacijom redom sledećih elemenata:


- **SegWit verzija**: `00`
- **Payload**: heš javnog ključa 
- **Kontrolni zbir**: Vrednosti dobijene u prethodnom koraku (`10 16 11 04 13 18`)


Ovo nam daje u dekadnom sistemu:


```text
00 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21 10 16 11 04 13 18
```


Zatim, svaka dekadna vrednost mora biti mapirana na svoj *bech32* karakter koristeći sledeću tabelu konverzije:



$$

\begin{array}{|c|c|c|c|c|c|c|c|c|}
\hline
& 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 \\
\hline
+0 & q & p & z & r & y & 9 & x & 8 \\
\hline
+8 & g & f & 2 & t & v & d & w & 0 \\
\hline
+16 & s & 3 & j & n & 5 & 4 & k & h \\
\hline
+24 & c & e & 6 & m & u & a & 7 & l \\
\hline
\end{array}

$$


Da biste konvertovali vrednost u _bech32_ karakter koristeći ovu tabelu, jednostavno pronađite vrednosti u prvoj koloni i prvom redu koje, kada se saberu, daju željeni rezultat. Zatim, preuzmite odgovarajući karakter. Na primer, decimalni broj `19` će biti konvertovan u slovo `n`, jer $19 = 16 + 3$.


Mapiranjem svih naših vrednosti, dobijamo sledeću adresu:


```
qn7qnytxgsc3v5nxt9ff2y83g3pe84ff42stydj
```


Sve što preostaje je da dodate HRP `bc`, što označava da je to adresa za Bitcoin Mainnet, kao i separator `1`, kako biste dobili kompletnu prijemnu adresu:


```
bc1qn7qnytxgsc3v5nxt9ff2y83g3pe84ff42stydj
```


Posebnost ovog _bech32_ alfabeta je da uključuje sve alfanumeričke karaktere osim `1`, `b`, `i` i `o` kako bi se izbegla vizuelna konfuzija između sličnih karaktera, posebno prilikom njihovog unosa ili čitanja od strane ljudi.


Da rezimiramo, evo procesa izvođenja:


![CYP201](assets/fr/065.webp)


Ovo je način kako izvesti P2WPKH (SegWit v0) primajuću adresu iz para ključeva. Sada pređimo na P2TR (SegWit v1 / Taproot) adrese i otkrijmo njihov proces generisanja.


### Derivacija SegWit v1 (bech32m) adresa


Za Taproot adrese, proces generisanja se malo razlikuje. Hajde da pogledamo ovo zajedno!


Od koraka kompresije javnog ključa, pojavljuje se prva razlika u poređenju sa ECDSA: javni ključevi korišćeni za Schnorr u Bitcoin-u su predstavljeni samo njihovom apscisom ($x$). Dakle, nema prefiksa, a kompresovani ključ ima dužinu od tačno 256 bita.

Kao što smo videli u prethodnom poglavlju, skripta P2TR zaključava bitkoine na jedinstvenom Schnorr javnom ključu, označenom sa $Q$. Ovaj ključ $Q$ je agregat dva javna ključa: $P$, glavnog internog javnog ključa, i $M$, javnog ključa izvedenog iz Merkle Root liste _scriptPubKey_. Bitkoini zaključani ovim tipom skripte mogu se potrošiti na dva načina:



- Objavljivanjem potpisa za javni ključ $P$ (_key path_);
- Zadovoljavajući jedan od skripti uključenih u Merkle Tree (_putanja skripte_).


U stvarnosti, ova dva ključa nisu zaista "agregirana." Ključ $P$ je umesto toga izmenjen ključem $M$. U kriptografiji, "prilagoditi (izmeniti)" javni ključ znači modifikovati ovaj ključ primenom aditivne vrednosti koja se zove "prilagodba (tweak)." Ova operacija omogućava da modifikovani ključ ostane kompatibilan sa originalnim privatnim ključem i prilagodbom. Tehnički, prilagodba je skalarna vrednost $t$ koja se dodaje početnom javnom ključu. Ako je $P$ originalni javni ključ, prilagođeni ključ postaje:



$$

P' = P + t \cdot G

$$


Gde je $G$ generator eliptičke krive koja se koristi. Ova operacija proizvodi novi javni ključ izveden iz originalnog ključa, zadržavajući kriptografske osobine koje omogućavaju njegovu upotrebu.


Ako ne treba da dodajete alternativne skripte (trošenje isključivo putem _putanje za ključ_), možete generisati Taproot adresu generisanu isključivo sa javnim ključem prisutnim na dubini 5 vašeg novčanika. U tom slučaju, potrebno je kreirati skriptu koja se ne može potrošiti za _putanju skripte_, kako bi se ispunili zahtevi strukture. Prilagodba $t$ se zatim izračunava primenom označene heš funkcije, **`TapTweak`**, na interni javni ključ $P$:



$$

t = \text{H}_{\text{TapTweak}}(P)

$$


gde:



- $\text{H}_{\text{TapTweak}}$ je SHA256 heš funkcija označena oznakom `TapTweak`. Ako niste upoznati sa time šta je označena heš funkcija, pozivam vas da pogledate poglavlje 3.3;
- $P$ je interni javni ključ, predstavljen u kompresovanom formatu od 256 bita, koristeći samo $x$ koordinatu.


Taproot javni ključ $Q$ se zatim izračunava dodavanjem prilagodbe $t$, pomnožene sa generatorom eliptičke krive $G$, internom javnom ključu $P$:



$$

Q = P + t \cdot G

$$


Jednom kada se dobije Taproot javni ključ $Q$, možemo generisati odgovarajuću prijemnu adresu. Za razliku od drugih formata, Taproot adrese nisu uspostavljene na hešu javnog ključa. Stoga se ključ $Q$ ubacuje direktno u adresu, na sirov način.


Da bismo započeli, izdvajamo $x$ koordinatu tačke $Q$ kako bismo dobili kompresovani javni ključ. Na ovom payload-u se izračunava kontrolna suma koristeći BCH kodove, kao kod SegWit v0 adresa. Međutim, program korišćen za Taproot adrese se malo razlikuje. Naime, nakon uvođenja _bech32_ formata za SegWit, otkriven je bug: kada je poslednji karakter Address `p`, umetanje ili uklanjanje `q` neposredno pre ovog `p` ne čini kontrolnu sumu nevažećom. Iako ovaj bug nema posledice na SegWit v0 (zahvaljujući ograničenju veličine), mogao bi predstavljati problem u budućnosti. Ovaj bug je stoga ispravljen za Taproot adrese, a novi ispravljeni format se zove "_bech32m_".


Taproot adresa se generiše enkodiranjem $x$ koordinate od $Q$ u _bech32m_ formatu, sa sledećim elementima:



- **HRP (_Deo adrese čitljiv za čoveka (eng. Human Readable Part_))**: `bc`, da označi glavnu Bitcoin mrežu;
- **Verzija**: `1` da označi Taproot / SegWit v1;
- **Kontrolni zbir**.


Konačni adresa će stoga imati format:


```
bc1p[Qx][checksum]
```


S druge strane, ako želite dodati alternativne skripte pored trošenja sa internim javnim ključem (_script path_), izračunavanje adrese za primanje će biti malo drugačije. Trebaće da uključite heš alternativnih skripti u izračunavanje prilagođavanja. U Taproot, svaka alternativna skripta, koja se nalazi na kraju Merkle Tree, naziva se "list".


Kada su različite alternativne skripte napisane, morate ih pojedinačno proći kroz označenu heš funkciju `TapLeaf`, praćenu nekim metapodacima:



$$

\text{h}_{\text{leaf}} = \text{H}_{\text{TapLeaf}} (v \Vert sz \Vert S)

$$


Sa:



- $v$: verzija skripte (podrazumevano `0xC0` za Taproot);
- $sz$: veličina skripte kodirane u _CompactSize_ formatu;
- $S$: skripta.


Različiti heševi skripti ($\text{h}_{\text{leaf}}$) prvo se sortiraju u leksikografskom redosledu. Zatim se konkateniraju u parovima i prosleđuju kroz označenu heš funkciju `TapBranch`. Ovaj proces se ponavlja iterativno kako bi se, korak po korak, izgradio Merkle Tree:

$$

\text{h}_{\text{branch}} = \text{H}_{\text{TapBranch}}(\text{h}_{\text{leaf1}} \Vert \text{h}_{\text{leaf2}})

$$


Zatim nastavljamo spajanjem rezultata dva po dva, propuštajući ih kroz označenu heš funkciju `TapBranch` na svakom koraku, sve dok ne dobijemo Merkle Tree Root, koji predstavlja koren:


![CYP201](assets/fr/066.webp)


Jednom kada se izračuna Merkle Root $h_{\text{root}}$, možemo izračunati prilagodbu. Za ovo, konkatenišemo interni javni ključ novčanika $P$ sa korenom $h_{\text{root}}$, a zatim sve to propuštamo kroz označenu heš funkciju `TapTweak`:



$$

t = \text{H}_{\text{TapTweak}}(P \Vert h_{\text{root}})

$$


Konačno, kao i ranije, Taproot javni ključ $Q$ se dobija dodavanjem internog javnog ključa $P$ proizvodu tweak-a $t$ sa generatorom tačke $G$:



$$

Q = P + t \cdot G

$$

Zatim se generisanje adrese odvija po istom postupku, koristeći sirovi javni ključ kao osnovni podatak (payload), uz dodatne metapodatke.

I eto ga! Stigli smo do kraja ovog kursa CYP201. Ako vam je ovaj kurs bio od pomoći, bio bih veoma zahvalan ako biste mogli odvojiti nekoliko trenutaka da mu date dobru ocenu u sledećem poglavlju za evaluaciju. Slobodno ga podelite i sa svojim voljenima ili na svojim društvenim mrežama. Na kraju, ako želite da dobijete diplomu za ovaj kurs, možete polagati završni ispit odmah nakon poglavlja za evaluaciju.

# Završni Deo

<partId>58111408-b734-54db-9ea7-0d5b67f99f99</partId>


## Recenzije i ocene

<chapterId>0cd71541-a7fd-53db-b66a-8611b6a28b04</chapterId>

<isCourseReview>true</isCourseReview>

## Završni ispit

<chapterId>a53ea27d-0f84-56cd-b37c-a66210a4b31d</chapterId>

<isCourseExam>true</isCourseExam>

## Zaključak

<chapterId>d291428b-3cfa-5394-930e-4b514be82d5a</chapterId>

<isCourseConclusion>true</isCourseConclusion>