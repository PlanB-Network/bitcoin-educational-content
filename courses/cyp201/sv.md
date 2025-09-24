---
name: Det inre arbetet med Bitcoin-plånböcker
goal: Dyk ner i de kryptografiska principer som driver Bitcoin-plånböcker.
objectives: 

  - Definiera de teoretiska begrepp som är nödvändiga för att förstå de kryptografiska algoritmer som används i Bitcoin.
  - Fullständig förståelse för konstruktionen av en deterministisk och hierarkisk Wallet.
  - Kunna identifiera och minska de risker som är förknippade med att hantera en Wallet.
  - Förstå principerna för Hash-funktioner, kryptografiska nycklar och digitala signaturer.

---

# En resa in i hjärtat av Bitcoin-plånböckerna


Upptäck hemligheterna bakom deterministiska och hierarkiska Bitcoin-plånböcker med vår CYP201-kurs! Oavsett om du är en vanlig användare eller en entusiast som vill fördjupa din kunskap, erbjuder den här kursen en fullständig fördjupning i hur dessa verktyg fungerar som vi alla använder dagligen.


Lär dig mer om mekanismerna bakom Hash-funktioner, digitala signaturer (ECDSA och Schnorr), Mnemonic-fraser, kryptografiska nycklar och skapandet av mottagaradresser, samtidigt som du utforskar avancerade säkerhetsstrategier.


Den här utbildningen ger dig inte bara kunskapen att förstå strukturen hos en Bitcoin Wallet utan förbereder dig också för att dyka djupare in i kryptografins spännande värld.


Med tydlig pedagogik, över 60 förklarande diagram och konkreta exempel kommer CYP201 att göra det möjligt för dig att förstå från A till Ö hur din Wallet fungerar, så att du kan navigera i Bitcoin-universumet med tillförsikt. Ta kontroll över dina UTXO:er idag genom att förstå hur HD wallets fungerar!


+++

# Inledning


<partId>32960669-d13a-592f-a053-37f70b997cbf</partId>


## Kursintroduktion


<chapterId>fb4e8857-ea35-5a8a-ae8a-5300234e0104</chapterId>


Välkommen till kursen CYP201, där vi kommer att utforska på djupet hur HD Bitcoin plånböcker fungerar. Den här kursen är utformad för alla som vill förstå de tekniska grunderna för att använda Bitcoin, oavsett om de är tillfälliga användare, upplysta entusiaster eller framtida experter.


Målet med den här utbildningen är att ge dig nycklarna till att bemästra de verktyg du använder dagligen. HD Bitcoin plånböcker, som är kärnan i din användarupplevelse, baseras på ibland komplexa koncept, som vi kommer att försöka göra tillgängliga. Tillsammans kommer vi att avmystifiera dem!


Innan vi dyker in i detaljerna kring konstruktion och drift av Bitcoin-plånböcker börjar vi med några kapitel om de kryptografiska primitiver som är viktiga att känna till för det som följer.

Vi börjar med kryptografiska Hash-funktioner, som är grundläggande för både plånböcker och själva Bitcoin-protokollet. Du kommer att upptäcka deras huvudsakliga egenskaper, de specifika funktionerna som används i Bitcoin, och i ett mer tekniskt kapitel kommer du att lära dig i detalj om hur drottningen av Hash-funktioner fungerar: SHA256.


![CYP201](assets/fr/010.webp)


Därefter kommer vi att diskutera hur digitala signaturalgoritmer fungerar som du använder varje dag för att säkra dina UTXO:er. Bitcoin använder två: ECDSA och Schnorr-protokollet. Du kommer att lära dig vilka matematiska primitiver som ligger till grund för dessa algoritmer och hur de garanterar säkerheten för transaktioner.


![CYP201](assets/fr/021.webp)


När vi väl har en god förståelse för dessa Elements av kryptografi, kommer vi äntligen att gå vidare till hjärtat av utbildningen: deterministiska och hierarkiska plånböcker! Först finns det ett avsnitt tillägnad Mnemonic-fraser, dessa sekvenser på 12 eller 24 ord som gör att du kan skapa och återställa dina plånböcker. Du kommer att upptäcka hur dessa ord genereras från en källa till entropi och hur de underlättar användningen av Bitcoin.


![CYP201](assets/fr/040.webp)


Utbildningen kommer att fortsätta med studier av BIP39 passphrase, seed (inte att förväxla med Mnemonic frasen), master chain code och huvudnyckeln. Vi kommer att se i detalj vad dessa Elements är, deras respektive roller och hur de beräknas.


![CYP201](assets/fr/045.webp)


Slutligen kommer vi från huvudnyckeln att upptäcka hur kryptografiska nyckelpar härleds på ett deterministiskt och hierarkiskt sätt upp till mottagaradresserna.


![CYP201](assets/fr/056.webp)


Denna utbildning gör det möjligt för dig att använda din Wallet-programvara med förtroende, samtidigt som du förbättrar dina färdigheter för att identifiera och mildra risker. Förbered dig på att bli en sann expert på Bitcoin-plånböcker!


Denna tabell erbjuder dig en översättning av de viktigaste engelska termerna som används, för att underlätta din förståelse av de scheman och tekniska dokument som används inom ramen för kursen CYP 201.

| Engelska        | Översättning / Förklaring                                                                          |
| --------------- | -------------------------------------------------------------------------------------------------- |
| *pubkey hash*   | Publik nyckel-hash (används för att generera en Bitcoin-adress).                                   |
| *public key*    | Publik nyckel (används för att ta emot medel, härledd från den privata nyckeln).                   |
| *signature*     | Digital signatur (kryptografiskt bevis på att ett meddelande kommer från innehavaren av en privat nyckel). |
| *scriptPubKey*  | Låsskript (definierar villkoren för att spendera en utgång).                                        |
| *scriptSig*     | Upplåsningsskript (tillhandahåller data för att uppfylla *scriptPubKey*).                           |
| *Stack*         | Stack (datastruktur som används av *Bitcoin Script*).                                               |
| *input*         | Transaktionsingång (referens till en tidigare utgång som används som källa).                        |
| *output*        | Transaktionsutgång (definierar mottagare och belopp).                                               |
| *transaction*   | Bitcoin-transaktion (uppsättning ingångar och utgångar som validerar en överföring).                |
| *XOR*           | Logisk operator "exklusivt ELLER", används i vissa kryptografiska scheman.                         |
| *HMAC*          | Meddelandeautentiseringskod baserad på en hash och en hemlig nyckel.                               |
| *ECDSA*         | Digital signaturalgoritm med elliptiska kurvor.                                                    |
| *hash*          | Hash (unik och fast fingeravtryck av data).                                                         |
| *SigHash*       | Typ av signatur-hash (definierar vilka delar av en transaktion som signeras).                       |
| *HD Wallet*     | Hierarkisk deterministisk plånbok (genererar flera nycklar från ett enda frö).                      |
| *Random Number* | Slumptal (används för att generera säkra privata nycklar).                                          |
| *State*         | Tillstånd (mellanvärde i en kryptografisk process).                                                 |
| *Entropy*       | Entropi (mått på slumpmässighet, används för att generera plånboksfrön).                            |
| *Mnemonic*      | Mnemoteknik (ordföljd som underlättar säkerhetskopiering och återställning av ett frö).             |
| *Wordlist*      | Ordlista (fördefinierad uppsättning som används för att generera BIP39-mnemoniker).                 |
| *Seed*          | Frö (initialvärde som tillåter härledning av alla nycklar i en HD-plånbok).                         |
| *Address*       | Bitcoin-adress (läsbar identifierare för att ta emot medel, härledd från den publika nyckeln).      |
| *Leaf*          | Löv (slutnod i ett derivationsträd).                                                                |

# Hash Funktioner


<partId>3713fee1-2ec2-512e-9e97-b6da9e4d2f17</partId>


## Introduktion till Hash-funktioner


<chapterId>dba011f5-1805-5a48-ac2b-4bd637c93703</chapterId>


Den första typen av kryptografiska algoritmer som används i Bitcoin omfattar Hash-funktioner. De spelar en viktig roll på olika nivåer i protokollet, men också inom Bitcoin-plånböcker. Låt oss tillsammans upptäcka vad en Hash-funktion är och vad den används till i Bitcoin.


### Definition och princip för Hashing


Hashing är en process som omvandlar information av godtycklig längd till annan information av fast längd genom en kryptografisk Hash-funktion. Med andra ord tar en Hash-funktion en inmatning av valfri storlek och omvandlar den till ett fingeravtryck med fast storlek, kallat "Hash".

Hash kan ibland också kallas "digest", "condensate", "condensed" eller "hashed".


SHA256 Hash-funktionen producerar t.ex. en Hash med en fast längd på 256 bitar. Om vi använder indata "_PlanB_", ett meddelande av godtycklig längd, kommer den genererade Hash att vara följande 256-bitars fingeravtryck:


```text
24f1b93b68026bfc24f5c8265f287b4c940fb1664b0d75053589d7a4f821b688
```


![CYP201](assets/fr/001.webp)


### Kännetecken för Hash-funktioner


Dessa kryptografiska Hash funktioner har flera väsentliga egenskaper som gör dem särskilt användbara i samband med Bitcoin och andra datorsystem:



- Irreversibilitet (eller preimage-resistens)
- Skydd mot sabotage (lavineffekt)
- Motstånd mot kollisioner
- Andra förbildsmotstånd


#### 1. Irreversibilitet (preimage-resistens):


Irreversibilitet innebär att det är lätt att beräkna Hash från den ingående informationen, men den omvända beräkningen, det vill säga att hitta den ingående informationen från Hash, är praktiskt taget omöjlig. Denna egenskap gör Hash-funktioner perfekta för att skapa unika digitala fingeravtryck utan att äventyra den ursprungliga informationen. Den här egenskapen kallas ofta för en envägsfunktion.


I det givna exemplet är det enkelt och snabbt att få Hash `24f1b9...` genom att känna till inmatningen "_PlanB_". Men att hitta meddelandet "_PlanB_" genom att bara känna till `24f1b9...` är omöjligt.


![CYP201](assets/fr/002.webp)


Därför är det omöjligt att hitta en förbild $m$ för en Hash $h$ så att $h = \text{Hash}(m)$, där $\text{Hash}$ är en kryptografisk Hash-funktion.


#### 2. Skydd mot sabotage (lavineffekt)


Den andra egenskapen är manipulationsresistens, även känd som **avalancheffekten**. Denna egenskap observeras i en Hash-funktion om en liten förändring i inmatningsmeddelandet resulterar i en radikal förändring i Hash-utmatningen.


Om vi går tillbaka till vårt exempel med inmatningen "_PlanB_" och SHA256-funktionen, har vi sett att den genererade Hash ser ut enligt följande:


```text
24f1b93b68026bfc24f5c8265f287b4c940fb1664b0d75053589d7a4f821b688
```


Om vi gör en mycket liten ändring av indata genom att använda "_Planb_" den här gången, ändras SHA256-utdata Hash helt och hållet bara genom att ändra från ett versalt "B" till ett gemen "b":


```text
bb038b4503ac5d90e1205788b00f8f314583c5e22f72bec84b8735ba5a36df3f
```


![CYP201](assets/fr/003.webp)


Denna egenskap säkerställer att även en mindre ändring av det ursprungliga meddelandet omedelbart kan upptäckas, eftersom det inte bara ändrar en liten del av Hash, utan hela Hash. Detta kan vara av intresse inom olika områden för att verifiera integriteten hos meddelanden, programvara eller till och med Bitcoin-transaktioner.


#### 3. Motstånd mot kollisioner


Den tredje egenskapen är kollisionsresistens. En Hash-funktion är kollisionsresistent om det är beräkningsmässigt omöjligt att hitta 2 olika meddelanden som ger samma Hash-utdata från funktionen. Formellt är det svårt att hitta två distinkta meddelanden $m_1$ och $m_2$ så att:


$$
\text{HASH}(m_1) = \text{HASH}(m_2)
$$


![CYP201](assets/fr/004.webp)


I verkligheten är det matematiskt oundvikligt att det uppstår kollisioner för Hash-funktioner, eftersom storleken på inmatningarna kan vara större än storleken på utmatningarna. Detta är känt som Dirichlets lådprincip: om $n$ objekt fördelas i $m$ lådor, med $m < n$, kommer minst en låda med nödvändighet att innehålla två eller flera objekt. För en Hash-funktion gäller denna princip eftersom antalet möjliga meddelanden är (nästan) oändligt, medan antalet möjliga hashar är begränsat ($2^{256}$ i fallet med SHA256).


Denna egenskap innebär således inte att det inte finns några kollisioner för Hash-funktioner, utan snarare att en bra Hash-funktion gör sannolikheten för att hitta en kollision försumbar. Denna egenskap är till exempel inte längre verifierad på SHA-0- och SHA-1-algoritmerna, föregångare till SHA-2, för vilka kollisioner har hittats. Dessa funktioner avråds därför nu och betraktas ofta som föråldrade.

För en Hash-funktion på $n$ bitar är kollisionsmotståndet i storleksordningen $2^{\frac{n}{2}}$, i enlighet med birthday-attacken. För SHA256 ($n = 256$) är t.ex. komplexiteten i att hitta en kollision i storleksordningen $2^{128}$ försök. I praktiken innebär detta att om man skickar $2^{128}$ olika meddelanden genom funktionen är det troligt att man hittar en kollision.


#### 4. Motstånd mot den andra förbilden


Motstånd mot andra preimage är en annan viktig egenskap hos Hash-funktioner. Den säger att med tanke på ett meddelande $m_1$ och dess Hash $h$ är det beräkningsmässigt omöjligt att hitta ett annat meddelande $m_2 \neq m_1$ så att:


$$
\text{HASH}(m_1) = \text{HASH}(m_2)
$$


Därför liknar motstånd mot andra preimage något kollisionsmotstånd, förutom här är attacken svårare eftersom angriparen inte fritt kan välja $ m_1 $.


![CYP201](assets/fr/005.webp)


### Tillämpningar av Hash Funktioner i Bitcoin


Den mest använda Hash-funktionen i Bitcoin är **SHA256** ("_Secure Hash Algorithm 256 bits"_). Den utformades i början av 2000-talet av NSA och standardiserades av NIST och producerar en 256-bitars Hash-utdata.


Denna funktion används i många aspekter av Bitcoin. På protokollnivå är den involverad i Proof-of-Work-mekanismen, där den används i dubbel hashing för att söka efter en partiell kollision mellan huvudet på ett kandidatblock, skapat av en Miner, och svårighetsmålet. Om denna partiella kollision hittas blir kandidatblocket giltigt och kan läggas till i Blockchain.


SHA256 används också i konstruktionen av en Merkle Tree, som framför allt är den ackumulator som används för att registrera transaktioner i block. Denna struktur finns också i Utreexo-protokollet, vilket gör det möjligt att minska storleken på UTXO-uppsättningen. I och med införandet av Taproot år 2021 utnyttjas SHA256 dessutom i MAST (_Merkelised Alternative Script Tree_), vilket gör det möjligt att endast avslöja de utgiftsvillkor som faktiskt används i ett skript, utan att avslöja de andra möjliga alternativen. Det används också vid beräkning av transaktionsidentifierare, vid överföring av paket via P2P-nätverket, i elektroniska signaturer... Slutligen, och detta är av särskilt intresse i den här utbildningen, används SHA256 på applikationsnivå för att skapa Bitcoin-plånböcker och härleda adresser.


För det mesta, när du stöter på användningen av SHA256 i Bitcoin, kommer det faktiskt att vara en dubbel Hash SHA256, noterad "**HASH256**", som helt enkelt består av att tillämpa SHA256 två gånger i följd:


$$
\text{HASH256}(m) = \text{SHA256}(\text{SHA256}(m))
$$


Denna metod med dubbel hashing ger en extra Layer i säkerhet mot vissa potentiella attacker, även om en enda SHA256 idag anses vara kryptografiskt säker.


En annan hashingfunktion som finns tillgänglig i Script-språket och som används för att härleda mottagaradresser är funktionen RIPEMD160. Denna funktion ger en 160-bitars Hash (alltså kortare än SHA256). Den kombineras i allmänhet med SHA256 för att bilda funktionen HASH160:


$$
\text{HASH160}(m) = \text{RIPEMD160}(\text{SHA256}(m))
$$


Denna kombination används för generate kortare hashar, särskilt vid skapandet av vissa Bitcoin-adresser som representerar hashar av nycklar eller skripthashar, samt för att producera nyckelfingeravtryck.


Slutligen, endast på applikationsnivå, används ibland även SHA512-funktionen, som indirekt spelar en roll i nyckelderivationen för plånböcker. Denna funktion är mycket lik SHA256 i sin funktion; båda tillhör samma SHA2-familj, men SHA512 producerar, som namnet antyder, en 512-bitars Hash, jämfört med 256 bitar för SHA256. Vi kommer att beskriva dess användning i detalj i följande kapitel.


Du känner nu till de viktigaste grunderna om hashfunktioner för vad som följer. I nästa kapitel föreslår jag att vi mer i detalj går igenom hur den funktion som är kärnan i Bitcoin fungerar: SHA256. Vi kommer att dissekera den för att förstå hur den uppnår de egenskaper som vi har beskrivit här. Nästa kapitel är ganska långt och tekniskt, men det är inte nödvändigt för att följa resten av utbildningen. Så om du har svårt att förstå det, oroa dig inte och gå direkt till följande kapitel, som kommer att vara mycket mer lättillgängligt.


## Det inre arbetet med SHA256


<chapterId>905eb320-f15b-5fb6-8d2d-5bb447337deb</chapterId>


Vi har tidigare sett att hashfunktioner har viktiga egenskaper som motiverar att de används i Bitcoin. Låt oss nu undersöka de interna mekanismerna i dessa hashfunktioner som ger dem dessa egenskaper, och för att göra detta föreslår jag att dissekera driften av SHA256.


Funktionerna SHA256 och SHA512 tillhör samma SHA2-familj. Deras mekanism bygger på en specifik konstruktion som kallas **Merkle-Damgård-konstruktion**. RIPEMD160 använder också samma typ av konstruktion.


Som en påminnelse har vi ett meddelande av godtycklig storlek som indata till SHA256, och vi kommer att skicka det genom funktionen för att få en 256-bitars Hash som utdata.


### Förbehandling av indata


Till att börja med måste vi förbereda vårt inmatade meddelande $m$ så att det har en standardlängd som är en multipel av 512 bitar. Detta steg är avgörande för att algoritmen ska fungera korrekt i fortsättningen.

För att göra detta börjar vi med steget med utfyllnadsbitar. Vi lägger först till en separatorbit `1` till meddelandet, följt av ett visst antal `0`-bitar. Antalet `0`-bitar som läggs till beräknas så att den totala längden på meddelandet efter detta tillägg är kongruent med 448 modulo 512. Således är längden $L$ på meddelandet med utfyllnadsbitarna lika med:


$$
L \equiv 448 \mod 512
$$


$\text{mod}$, för modulo, är en matematisk operation som, mellan två heltal, returnerar resten av den euklidiska divisionen av det första genom det andra. Till exempel: $16 \mod 5 = 1$. Det är en operation som ofta används inom kryptografi.


Här säkerställer utfyllnadssteget att den totala längden på det utjämnade meddelandet blir en multipel av 512 bitar efter att de 64 bitarna har lagts till i nästa steg. Om det ursprungliga meddelandet har en längd av $M$ bitar, är antalet ($N$) `0` bitar som ska läggas till följande:


$$
N = (448 - (M + 1) \mod 512) \mod 512
$$


Om t.ex. det ursprungliga meddelandet är 950 bitar blir beräkningen som följer:


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


Således skulle vi ha 9 `0` utöver separatorn `1`. Våra utfyllnadsbitar som ska läggas till direkt efter vårt meddelande $M$ skulle således vara:


```text
1000 0000 00
```


När vi har lagt till utfyllnadsbitarna i vårt meddelande $M$ lägger vi också till en 64-bitars representation av den ursprungliga längden på meddelandet $M$, uttryckt i binär form. Detta gör att Hash-funktionen kan vara känslig för ordningen på bitarna och meddelandets längd.


Om vi återgår till vårt exempel med ett första meddelande på 950 bitar, konverterar vi det decimala talet 950 till binärt, vilket ger oss 1110 1101 10. Vi kompletterar detta tal med nollor vid basen för att få totalt 64 bitar. I vårt exempel ger detta:


```text
0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0011 1011 0110
```


Denna utfyllnadsstorlek läggs till efter bitutfyllnaden. Därför består meddelandet efter vår förbehandling av tre delar:



- Det ursprungliga meddelandet $M$;
- En bit `1` följd av flera bitar `0` för att bilda bitutfyllnaden;
- En 64-bitars representation av längden på $M$ för att bilda utfyllnaden med storleken.


![CYP201](assets/fr/006.webp)


### Initialisering av variabler


SHA256 använder åtta initiala tillståndsvariabler, betecknade $A$ till $H$, var och en på 32 bitar. Dessa variabler initialiseras med specifika konstanter, som är bråkdelarna av kvadratrötterna till de första åtta primtalen. Vi kommer att använda dessa värden senare under hashingprocessen:



- $A = 0x6a09e667$$
- $B = 0xbb67ae85$$
- $C = 0x3c6ef372$$
- $D = 0xa54ff53a$$
- $E = 0x510e527f$$
- $F = 0x9b05688c$$
- $G = 0x1f83d9ab$$
- $H = 0x5be0cd19$$


SHA256 använder också 64 andra konstanter, betecknade $K_0$ till $K_{63}$, som är bråkdelarna av kubikrötterna till de första 64 primtalen:


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


### Uppdelning av inmatningen


Nu när vi har en utjämnad indata går vi vidare till den viktigaste bearbetningsfasen i SHA256-algoritmen: komprimeringsfunktionen. Det här steget är mycket viktigt eftersom det är det som ger Hash-funktionen dess kryptografiska egenskaper som vi studerade i föregående kapitel.


Först börjar vi med att dela upp vårt utjämnade meddelande (resultatet av förbehandlingsstegen) i flera block $P$ på 512 bitar vardera. Om vårt utjämnade meddelande har en total storlek på $n \ gånger 512$ bitar, kommer vi därför att ha $n$ block, vart och ett på 512 bitar. Varje 512-bitarsblock kommer att behandlas individuellt av komprimeringsfunktionen, som består av 64 omgångar av successiva operationer. Låt oss kalla dessa block $P_1$, $P_2$, $P_3$...


### Logiska operationer


Innan vi går närmare in på komprimeringsfunktionen är det viktigt att förstå de grundläggande logiska operationer som används i den. Dessa operationer, som är baserade på boolesk algebra, fungerar på bitnivå. De grundläggande logiska operationer som används är:



- **Konjunktion (AND)**: betecknas $\land$, motsvarar ett logiskt "AND".
- **Disjunction (OR)**: betecknas $\lor$, motsvarar ett logiskt "OR".
- **Negation (NOT)**: betecknas $\lnot$ och motsvarar ett logiskt "NOT".


Utifrån dessa grundläggande operationer kan vi definiera mer komplexa operationer, till exempel "Exclusive OR" (XOR) som betecknas $\oplus$ och som ofta används inom kryptografi.

Varje logisk operation kan representeras av en sanningstabell, som anger resultatet för alla möjliga kombinationer av binära ingångsvärden (två operander $p$ och $q$).

För XOR ($\oplus$):


| $p$ | $q$ | $p \oplus q$ |
| --- | --- | ------------ |
| 0   | 0   | 0            |
| 0   | 1   | 1            |
| 1   | 0   | 1            |
| 1   | 1   | 0            |

För AND ($\land$):


| $p$ | $q$ | $p \land q$ |
| --- | --- | ----------- |
| 0   | 0   | 0           |
| 0   | 1   | 0           |
| 1   | 0   | 0           |
| 1   | 1   | 1           |

För NOT ($\lnot p$):


| $p$ | $\lnot p$ |
| --- | --------- |
| 0   | 1         |
| 1   | 0         |

Låt oss ta ett exempel för att förstå hur XOR fungerar på bitnivå. Om vi har två binära tal på 6 bitar:



- $a = 101100$
- $b = 001000$


Då så:


$$

a \oplus b = 101100 \oplus 001000 = 100100


$$


Genom att tillämpa XOR bit för bit:


| Bit Position | $a$ | $b$ | $a \oplus b$ |
| ------------ | --- | --- | ------------ |
| 1            | 1   | 0   | 1            |
| 2            | 0   | 0   | 0            |
| 3            | 1   | 1   | 0            |
| 4            | 1   | 0   | 1            |
| 5            | 0   | 0   | 0            |
| 6            | 0   | 0   | 0            |

Resultatet blir därför $100100$.


Förutom logiska operationer använder komprimeringsfunktionen bitskiftningsoperationer, som kommer att spela en viktig roll i spridningen av bitar i algoritmen.


För det första finns den logiska högerskiftoperationen, betecknad $ShR_n(x)$, som flyttar alla bitar i $x$ till höger med $n$ positioner och fyller de lediga bitarna till vänster med nollor.


Till exempel, för $x = 101100001$ (på 9 bitar) och $n = 4$:


$$

ShR_4(101100001) = 000010110


$$


Schematiskt kan högerskiftsoperationen ses så här:


![CYP201](assets/fr/007.webp)


En annan operation som används i SHA256 för bitmanipulation är högercirkulär rotation, betecknad $RotR_n(x)$, som flyttar bitarna i $x$ till höger med $n$ positioner och återinsätter de flyttade bitarna i början av strängen.

Till exempel, för $x = 101100001$ (över 9 bitar) och $n = 4$:


$$

RotR_4(101100001) = 000110110


$$


Schematiskt kan den högra cirkulära skiftoperationen ses så här:


![CYP201](assets/fr/008.webp)


### Kompressionsfunktion


Nu när vi har förstått de grundläggande operationerna ska vi granska SHA256-komprimeringsfunktionen i detalj.


I det föregående steget delade vi upp vår indata i flera 512-bitars bitar $P$. För varje 512-bitarsblock $P$ har vi:



- Meddelandeorden **$W_i$**: för $i$ från 0 till 63.
- Konstanterna **$K_i$**: för $i$ från 0 till 63, definierade i föregående steg.
- Tillståndsvariablerna $A, B, C, D, E, F, G, H$ initialiseras med värdena från föregående steg.


De första 16 orden, $W_0$ till $W_{15}$, extraheras direkt från det bearbetade 512-bitarsblocket $P$. Varje ord $W_i$ består av 32 på varandra följande bitar från blocket. Vi tar till exempel vår första indata $P_1$ och delar upp den i mindre 32-bitars bitar som vi kallar ord.


De följande 48 orden ($W_{16}$ till $W_{63}$) genereras med hjälp av följande formel:


$$
W_i = W_{i-16} + \sigma_0(W_{i-15}) + W_{i-7} + \sigma_1(W_{i-2}) \mod 2^{32}
$$


Med:



- $\sigma_0(x) = RotR_7(x) \oplus RotR_{18}(x) \oplus ShR_3(x) $\sigma_0(x) = RotR_7(x) \oplus RotR_{18}(x) \oplus ShR_3(x)
- $\sigma_1(x) = RotR_{17}(x) \oplus RotR_{19}(x) \oplus ShR_{10}(x) $\sigma_1(x) = RotR_{17}(x) \oplus ShR_{10}(x)


I detta fall är $x$ lika med $W_{i-15}$ för $\sigma_0(x)$ och $W_{i-2}$ för $\sigma_1(x)$.


När vi har bestämt alla ord $W_i$ för vårt 512-bitarsstycke kan vi gå vidare till komprimeringsfunktionen, som består av att utföra 64 rundor.


![CYP201](assets/fr/009.webp)

För varje runda $i$ från 0 till 63 har vi tre olika typer av indata. För det första $W_i$ som vi just har bestämt och som delvis består av vår meddelandebit $P_n$. Därefter de 64 konstanterna $K_i$. Slutligen använder vi tillståndsvariablerna $A$, $B$, $C$, $D$, $E$, $F$, $G$ och $H$, som kommer att utvecklas under hashprocessen och modifieras med varje komprimeringsfunktion. För den första delen $P_1$ använder vi dock de initiala konstanter som angetts tidigare.


Vi utför sedan följande operationer på våra indata:



- Funktion $\Sigma_0$:


$$
\Sigma_0(A) = RotR_2(A) \oplus RotR_{13}(A) \oplus RotR_{22}(A)
$$



- Funktion $\Sigma_1$:


$$
\Sigma_1(E) = RotR_6(E) \oplus RotR_{11}(E) \oplus RotR_{25}(E)
$$



- Funktion $Ch$ ("_Choose_")**:**


$$
Ch(E, F, G) = (E \land F) \oplus (\lnot E \land G)
$$



- Funktion $Maj$ ("_Majoritet_"):


$$
Maj(A, B, C) = (A \land B) \oplus (A \land C) \oplus (B \land C)
$$


Vi beräknar sedan 2 tillfälliga variabler:



- $temp1$:


$$
temp1 = H + \Sigma_1(E) + Ch(E, F, G) + K_i + W_i \mod 2^{32}
$$



- $temp2$:


$$
temp2 = \Sigma_0(A) + Maj(A, B, C) \mod 2^{32}
$$


Därefter uppdaterar vi tillståndsvariablerna på följande sätt:


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


Följande diagram visar en omgång av komprimeringsfunktionen SHA256 som vi just har beskrivit:


![CYP201](assets/fr/010.webp)



- Pilarna anger dataflödet;
- Rutorna representerar de operationer som utförts;
- De omringade $+$ representerar addition modulo $2^{32}$.


Vi kan redan se att denna omgång ger nya tillståndsvariabler $A$, $B$, $C$, $D$, $E$, $F$, $G$ och $H$. Dessa nya variabler kommer att användas som indata för nästa omgång, som i sin tur kommer att producera nya variabler $A$, $B$, $C$, $D$, $E$, $F$, $G$ och $H$, som ska användas för nästa omgång. Denna process fortsätter till och med den 64:e omgången.

Efter de 64 omgångarna uppdaterar vi de ursprungliga värdena för tillståndsvariablerna genom att lägga till dem till de slutliga värdena i slutet av omgång 64:


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


Dessa nya värden för $A$, $B$, $C$, $D$, $E$, $F$, $G$ och $H$ kommer att fungera som startvärden för nästa block, $P_2$. För detta block $P_2$ replikerar vi samma komprimeringsprocess med 64 omgångar, sedan uppdaterar vi variablerna för block $P_3$, och så vidare till det sista blocket i vår utjämnade indata.


När vi har bearbetat alla meddelandeblock sammankopplar vi de slutliga värdena för variablerna $A$, $B$, $C$, $D$, $E$, $F$, $G$ och $H$ för att bilda den slutliga 256-bitars Hash i vår hashfunktion:


$$

\text{Hash} = A \Vert B \Vert C \Vert D \Vert E \Vert F \Vert G \Vert H


$$


Varje variabel är ett 32-bitars heltal, så deras sammankoppling ger alltid ett 256-bitars resultat, oavsett storleken på vårt meddelande som matas in i hashingfunktionen.


### Motivering av kryptografiska egenskaper


Men hur är då denna funktion irreversibel, kollisionssäker och manipuleringssäker?


För manipulationsmotstånd är det ganska enkelt att förstå. Det finns så många beräkningar som utförs i kaskad, som beror både på ingången och konstanterna, att den minsta modifieringen av det ursprungliga meddelandet helt ändrar den väg som tas, och därmed helt ändrar utgången Hash. Detta är vad som kallas lavineffekten. Denna egenskap säkerställs delvis genom att de mellanliggande tillstånden blandas med de initiala tillstånden för varje del.

När man sedan diskuterar en kryptografisk Hash-funktion används vanligtvis inte termen "irreversibilitet". Istället talar vi om "preimage resistance", vilket innebär att för varje given $y$ är det svårt att hitta en $x$ så att $h(x) = y$. Denna preimage-resistens garanteras av den algebraiska komplexiteten och den starka icke-linjäriteten i de operationer som utförs i komprimeringsfunktionen, samt av förlusten av viss information i processen. För ett givet resultat av en addition modulo finns det t.ex. flera möjliga operander:


$$

3+2 \mod 10 = 5 \\
7+8 \mod 10 = 5 \\
5+10 \mod 10 = 5


$$


I det här exemplet kan man inte med säkerhet avgöra vilka som är de korrekta operanderna i additionen, eftersom man bara känner till den använda modulo (10) och resultatet (5). Det sägs att det finns flera kongruenser modulo 10.


För XOR-operationen står vi inför samma problem. Kom ihåg sanningstabellen för denna operation: alla 1-bitars utdata kan bestämmas av två olika ingångskonfigurationer som har exakt samma sannolikhet att vara de korrekta värdena. Därför kan man inte med säkerhet bestämma operanderna i en XOR genom att bara känna till dess resultat. Om vi ökar storleken på XOR-operanderna ökar antalet möjliga ingångar som bara känner till resultatet exponentiellt. Dessutom används XOR ofta tillsammans med andra operationer på bitnivå, t.ex. operationen $\text{RotR}$, som ger ännu fler möjliga tolkningar av resultatet.


Komprimeringsfunktionen använder också operationen $\text{ShR}$. Denna operation tar bort en del av den grundläggande informationen, som sedan är omöjlig att hämta senare. Återigen finns det inget algebraiskt sätt att vända denna operation. Alla dessa envägsoperationer och informationsförluster används mycket ofta i komprimeringsfunktioner. Antalet möjliga ingångar för en given utgång är alltså nästan oändligt, och varje försök till omvänd beräkning skulle leda till ekvationer med ett mycket stort antal obekanta, som skulle öka exponentiellt för varje steg.


När det gäller egenskapen kollisionsmotstånd är det slutligen flera parametrar som spelar in. Förbehandlingen av det ursprungliga meddelandet spelar en viktig roll. Utan denna förbehandling kan det vara lättare att hitta kollisioner i funktionen. Även om det teoretiskt sett finns kollisioner (på grund av duvhålsprincipen), gör Hash-funktionens struktur, i kombination med de ovannämnda egenskaperna, att sannolikheten för att hitta en kollision är extremt låg.

För att en Hash-funktion ska vara kollisionssäker är det viktigt att:



- Utdata är oförutsägbara: All förutsägbarhet kan utnyttjas för att hitta kollisioner snabbare än med en brute force-attack. Funktionen säkerställer att varje bit i utdata beror på ett icke-trivialt sätt på indata. Med andra ord är funktionen utformad så att varje bit i slutresultatet har en oberoende sannolikhet att vara 0 eller 1, även om detta oberoende inte är absolut i praktiken.
- Fördelningen av hashkoder är pseudoslumpmässig: Detta säkerställer att hasharna är jämnt fördelade.
- Storleken på Hash är betydande: ju större det möjliga utrymmet för resultat är, desto svårare är det att hitta en kollision.


Kryptografer utformar dessa funktioner genom att utvärdera de bästa möjliga attackerna för att hitta kollisioner och sedan justera parametrarna för att göra dessa attacker ineffektiva.


### Merkle-Damgård Byggverksamhet


Strukturen i SHA256 bygger på Merkle-Damgård-konstruktionen, som gör det möjligt att omvandla en komprimeringsfunktion till en Hash-funktion som kan behandla meddelanden av godtycklig längd. Detta är precis vad vi har sett i det här kapitlet.


Vissa gamla Hash-funktioner som SHA1 eller MD5, som använder denna specifika konstruktion, är dock sårbara för längdförlängningsattacker. Detta är en teknik som gör det möjligt för en angripare som känner till Hash för ett meddelande $M$ och längden på $M$ (utan att känna till själva meddelandet) att beräkna Hash för ett meddelande $M'$ som bildas genom att sammanfoga $M$ med ytterligare innehåll.


SHA256, även om den använder samma typ av konstruktion, är teoretiskt motståndskraftig mot denna typ av attack, till skillnad från SHA1 och MD5. Detta kan förklara mysteriet med den dubbla hashingen som implementerades i hela Bitcoin av Satoshi Nakamoto. För att undvika den här typen av attacker kan Satoshi ha föredragit att använda en dubbel SHA256:


$$

\text{HASH256}(m) = \text{SHA256}(\text{SHA256}(m))


$$


Detta ökar säkerheten mot potentiella attacker relaterade till Merkle-Damgård-konstruktionen, men det ökar inte hashingprocessens säkerhet när det gäller kollisionsmotstånd. Även om SHA256 hade varit sårbar för denna typ av attack skulle det inte ha haft någon allvarlig inverkan, eftersom alla användningsfall av Hash-funktioner i Bitcoin omfattar offentliga data. Attacken med längdförlängning kan dock bara vara användbar för en angripare om de hashade uppgifterna är privata och användaren har använt Hash-funktionen som en autentiseringsmekanism för dessa uppgifter, liknande en MAC. Implementeringen av dubbel hashing förblir således ett mysterium i utformningen av Bitcoin.

Nu när vi har tittat i detalj på hur Hash-funktioner fungerar, särskilt SHA256, som används i stor utsträckning i Bitcoin, kommer vi att fokusera mer specifikt på de kryptografiska härledningsalgoritmer som används på applikationsnivå, särskilt för att härleda nycklarna för din Wallet.


## De algoritmer som används för härledning


<chapterId>cc668121-7789-5e99-bf5e-1ba085f4f5f2</chapterId>


I Bitcoin på applikationsnivå används, förutom Hash-funktioner, kryptografiska derivationsalgoritmer för att generate säkra data från initiala indata. Även om dessa algoritmer förlitar sig på Hash-funktioner har de olika syften, särskilt när det gäller autentisering och nyckelgenerering. Dessa algoritmer behåller några av egenskaperna hos Hash-funktioner, t.ex. irreversibilitet, manipuleringsresistens och kollisionsresistens.


I Bitcoin-plånböcker används huvudsakligen 2 derivationsalgoritmer:



- HMAC (_Hash-baserad kod för autentisering av meddelanden_)
- PBKDF2 (**Password-Based Key Derivation Function 2**)


Vi kommer tillsammans att undersöka hur var och en av dem fungerar och vilken roll de har.


### HMAC-SHA512


HMAC är en kryptografisk algoritm som beräknar en autentiseringskod baserad på en kombination av en Hash-funktion och en hemlig nyckel. Bitcoin använder HMAC-SHA512, den variant av HMAC som använder Hash-funktionen SHA512. Vi har redan sett i föregående kapitel att SHA512 ingår i samma familj av Hash-funktioner som SHA256, men den ger en 512-bitars utdata.


Här är dess allmänna driftsschema med $m$ som inmatningsmeddelande och $K$ en hemlig nyckel:


![CYP201](assets/fr/011.webp)


Låt oss studera mer i detalj vad som händer i denna HMAC-SHA512 svarta låda. HMAC-SHA512-funktionen med:



- $m$: det godtyckligt stora meddelande som användaren väljer (första inmatningen);
- $K$: den godtyckliga hemliga nyckel som användaren väljer (andra inmatningen);
- $K'$: nyckeln $K$ justerad till storleken $B$ på Hash:s funktionsblock (1024 bitar för SHA512, eller 128 byte);
- $\text{SHA512}$: SHA512 Hash-funktionen;
- $\oplus$: XOR-operationen (exklusivt eller);
- $\Vert$: konkateneringsoperatorn, som länkar samman bitsträngar från början till slut;
- $\text{opad}$: konstant som består av byten $0x5c$ upprepade 128 gånger
- $\text{ipad}$: konstant som består av byten $0x36$ upprepade 128 gånger.


Innan HMAC beräknas är det nödvändigt att utjämna nyckeln och konstanterna enligt blockstorleken $B$. Om nyckeln $K$ till exempel är kortare än 128 byte, fylls den på med nollor för att nå storleken $B$. Om $K$ är längre än 128 byte komprimeras den med SHA512 och sedan läggs nollor till tills den når 128 byte. På detta sätt erhålls en utjämnad nyckel med namnet $K'$. Värdena för $\text{opad}$ och $\text{ipad}$ erhålls genom att basbytena upprepas ($0x5c$ för $\text{opad}$, $0x36$ för $\text{ipad}$) tills storleken $B$ uppnås. Med $B = 128$ byte har vi således:


$$

\text{opad} = \underbrace{0x5c5c\ldots5c}\_{128 \  \text{bytes}}


$$


När förbehandlingen är klar definieras HMAC-SHA512-algoritmen enligt följande ekvation:


$$

\text{HMAC-SHA512}(K,m) = \text{SHA512} \left( (K' \oplus \text{opad}) \parallel \text{SHA512} \left( (K' \oplus \text{ipad}) \parallel m \right) \right)


$$


Denna ekvation är uppdelad i följande steg:



- XOR den justerade nyckeln $K'$ med $\text{ipad}$ för att erhålla $\text{iKpad}$;
- XOR den justerade nyckeln $K'$ med $\text{opad}$ för att erhålla $\text{oKpad}$;
- Sammankoppla $\text{iKpad}$ med meddelandet $m$.
- Hash detta resultat med SHA512 för att erhålla en mellanliggande Hash $H_1$.
- Sammankoppla $\text{oKpad}$ med $H_1$.
- Hash detta resultat med SHA512 för att erhålla slutresultatet $H_2$.


Dessa steg kan sammanfattas schematiskt enligt följande:


![CYP201](assets/fr/012.webp)


HMAC används i Bitcoin bland annat för nyckelderivation i HD-plånböcker (Hierarchical Deterministic) (vi kommer att prata mer om detta i kommande kapitel) och som en komponent i PBKDF2.


### PBKDF2


PBKDF2 (_Password-Based Key Derivation Function 2_) är en nyckelderivationsalgoritm som är utformad för att förbättra säkerheten för lösenord. Algoritmen tillämpar en pseudoslumpfunktion (här HMAC-SHA512) på ett lösenord och ett kryptografiskt salt och upprepar sedan denna operation ett visst antal gånger för att producera en utdatanyckel.


I Bitcoin används PBKDF2 för att generate seed av en HD Wallet från en Mnemonic-fras och en passphrase (men vi kommer att prata om detta mer i detalj i de kommande kapitlen).


PBKDF2-processen är som följer, med:



- $m$: användarens Mnemonic-fras;
- $s$: tillvalet passphrase för att öka säkerheten (tomt fält om ingen passphrase);
- $n$: antalet iterationer av funktionen, i vårt fall är det 2048.


PBKDF2-funktionen definieras iterativt. Varje iteration tar resultatet av den föregående, skickar det genom HMAC-SHA512 och kombinerar de successiva resultaten för att producera den slutliga nyckeln:


$$

\text{PBKDF2}(m, s) = \text{HMAC-SHA512}^{2048}(m, s)


$$


Schematiskt kan PBKDF2 beskrivas enligt följande:


![CYP201](assets/fr/013.webp)


I det här kapitlet har vi undersökt funktionerna HMAC-SHA512 och PBKDF2, som använder hashfunktioner för att säkerställa integriteten och säkerheten för nyckelderivationer i Bitcoin-protokollet. I nästa del tittar vi närmare på digitala signaturer, en annan kryptografisk metod som ofta används i Bitcoin.


# Digitala signaturer


<partId>76b58a00-0c18-54b9-870d-6b7e34029db8</partId>


## Digitala signaturer och elliptiska kurvor


<chapterId>c9dd9672-6da1-57f8-9871-8b28994d4c1a</chapterId>


Den andra kryptografiska metoden som används i Bitcoin involverar digitala signaturalgoritmer. Låt oss utforska vad detta innebär och hur det fungerar.


### Bitcoins, UTXO:er och utgiftsförhållanden


Termen "_plånbok_" i Bitcoin kan vara ganska förvirrande för nybörjare. Det som kallas en Bitcoin Wallet är faktiskt programvara som inte direkt håller dina bitcoins, till skillnad från en fysisk Wallet som kan hålla mynt eller sedlar. Bitcoins är helt enkelt kontoenheter. Denna kontoenhet representeras av **UTXO** (_Unspent Transaction Outputs_), som är outnyttjade transaktionsutgångar. Om dessa utgångar är outnyttjade betyder det att de tillhör en användare. UTXO är på sätt och vis bitar av bitcoins, av varierande storlek, som tillhör en användare.


Bitcoin-protokollet är distribuerat och fungerar utan en central myndighet. Därför är det inte som traditionella bankuppgifter, där de euro som tillhör dig helt enkelt är associerade med din personliga identitet. I Bitcoin tillhör dina UTXO:er dig eftersom de skyddas av utgiftsvillkor som anges i Script-språket. För att förenkla finns det två typer av skript: låsningsskriptet (_scriptPubKey_), som skyddar en UTXO, och upplåsningsskriptet (_scriptSig_), som gör det möjligt att låsa upp en UTXO och därmed spendera de Bitcoin-enheter som den representerar.

Den initiala driften av Bitcoin med P2PK-skript innebär att en publik nyckel används för att låsa medel, och i en _scriptPubKey_ anges att den person som vill använda denna UTXO måste tillhandahålla en giltig signatur med den privata nyckel som motsvarar denna publika nyckel. För att låsa upp denna UTXO är det därför nödvändigt att tillhandahålla en giltig signatur i _scriptSig_. Som namnen antyder är den publika nyckeln känd av alla eftersom den sänds ut på Blockchain, medan den privata nyckeln endast är känd av den rättmätiga ägaren till pengarna.

Detta är den grundläggande operationen för Bitcoin, men med tiden har denna operation blivit mer komplex. Först introducerade Satoshi också P2PKH-skript, som använder en mottagande Address i _scriptPubKey_, som representerar Hash för den offentliga nyckeln. Sedan blev systemet ännu mer komplext med ankomsten av SegWit och sedan Taproot. Den allmänna principen förblir dock i grunden densamma: en offentlig nyckel eller en representation av denna nyckel används för att låsa UTXO:er, och en motsvarande privat nyckel krävs för att låsa upp dem och därmed spendera dem.


En användare som vill göra en Bitcoin-transaktion måste därför skapa en digital signatur med hjälp av sin privata nyckel på transaktionen. Signaturen kan verifieras av andra nätverksdeltagare. Om den är giltig innebär det att den användare som initierar transaktionen verkligen är ägare till den privata nyckeln och därmed ägare till de bitcoins som användaren vill spendera. Andra användare kan sedan acceptera och sprida transaktionen.


Som ett resultat måste en användare som äger bitcoins låsta med en offentlig nyckel hitta ett sätt att säkert lagra det som gör det möjligt att låsa upp sina medel: den privata nyckeln. En Bitcoin Wallet är just en enhet som gör att du enkelt kan förvara alla dina nycklar utan att andra människor har tillgång till dem. Den är därför mer lik en nyckelring än en Wallet.


Den matematiska kopplingen mellan en publik nyckel och en privat nyckel, samt möjligheten att utföra en signatur för att bevisa innehav av en privat nyckel utan att avslöja den, möjliggörs av en digital signaturalgoritm. I Bitcoin-protokollet används två signaturalgoritmer: **ECDSA** (_Elliptic Curve Digital Signature Algorithm_) och **Schnorr-signaturschemat**. ECDSA är det digitala signaturprotokoll som använts i Bitcoin från början. Schnorr är nyare i Bitcoin, eftersom det introducerades i november 2021 med Taproot-uppdateringen.

Dessa två algoritmer är ganska lika i sina mekanismer. De bygger båda på kryptografi med elliptisk kurva. Den stora skillnaden mellan dessa två protokoll ligger i signaturens struktur och vissa specifika matematiska egenskaper. Vi kommer därför att studera hur dessa algoritmer fungerar och börjar med den äldsta: ECDSA.


### Kryptografi med elliptisk kurva


Elliptisk kurva-kryptografi (ECC) är en uppsättning algoritmer som använder en elliptisk kurva för dess olika matematiska och geometriska egenskaper för kryptografiska ändamål. Säkerheten i dessa algoritmer bygger på svårigheten i det diskreta logaritmproblemet på elliptiska kurvor. Elliptiska kurvor används framför allt för nyckelutbyten, asymmetrisk kryptering eller för att skapa digitala signaturer.


En viktig egenskap hos dessa kurvor är att de är symmetriska i förhållande till x-axeln. Således kommer varje icke-vertikal linje som skär kurvan i två olika punkter alltid att skära kurvan i en tredje punkt. Dessutom kommer varje tangent till kurvan i en icke-singulär punkt att skära kurvan i en annan punkt. Dessa egenskaper kommer att vara användbara för att definiera operationer på kurvan.


Här är en representation av en elliptisk kurva över fältet av reella tal:


![CYP201](assets/fr/014.webp)


Varje elliptisk kurva definieras av en ekvation av formen:


$$

y^2 = x^3 + ax + b


$$


### secp256k1


För att använda ECDSA eller Schnorr måste man välja parametrarna för den elliptiska kurvan, det vill säga värdena för $a$ och $b$ i kurvekvationen. Det finns olika standarder för elliptiska kurvor som har rykte om sig att vara kryptografiskt säkra. Den mest välkända är kurvan _secp256r1_, som definieras och rekommenderas av NIST (_National Institute of Standards and Technology_).


Trots detta valde Satoshi Nakamoto, uppfinnaren av Bitcoin, att inte använda den här kurvan. Orsaken till detta val är okänd, men vissa tror att han föredrog att hitta ett alternativ eftersom parametrarna för denna kurva potentiellt skulle kunna innehålla en bakdörr. Istället använder Bitcoin-protokollet standardkurvan **_secp256k1_**. Denna kurva definieras av parametrarna $a = 0$ och $b = 7$. Dess ekvation är därför:


$$

y^2 = x^3 + 7


$$


Dess grafiska representation över fältet av reella tal ser ut så här:


![CYP201](assets/fr/015.webp)


Inom kryptografi arbetar vi dock med ändliga uppsättningar av tal. Mer specifikt arbetar vi med det finita fältet $\mathbb{F}_p$, som är fältet av heltal modulo ett primtal $p$.

**Definition**: Ett primtal är ett naturligt heltal större än eller lika med 2 som bara har två distinkta positiva heltalsdivisorer: 1 och sig självt. Till exempel är talet 7 ett primtal eftersom det bara kan delas med 1 och 7. Å andra sidan är talet 8 inte ett primtal eftersom det kan delas med 1, 2, 4 och 8.

I Bitcoin är primtalet $p$ som används för att definiera det finita fältet mycket stort. Det är valt på ett sådant sätt att fältets ordning (dvs. antalet Elements i $\mathbb{F}_p$) är tillräckligt stort för att garantera kryptografisk säkerhet.


Primtalet $p$ som används är:


```text
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
```


I decimalnotation motsvarar detta:


$$

p = 2^{256} - 2^{32} - 977


$$


Ekvationen för vår elliptiska kurva är alltså faktiskt:


$$

y^2 \equiv x^3 + 7 \mod p


$$


Eftersom denna kurva definieras över det ändliga fältet $\mathbb{F}_p$ liknar den inte längre en kontinuerlig kurva utan snarare en diskret uppsättning punkter. Så här ser till exempel kurvan som användes i Bitcoin ut för ett mycket litet $p = 17$:


![CYP201](assets/fr/016.webp)


I det här exemplet har jag av pedagogiska skäl avsiktligt begränsat det finita fältet till $p = 17$, men man måste föreställa sig att det som används i Bitcoin är oerhört mycket större, nästan $2^{256}$.


Vi använder ett ändligt fält av heltal modulo $p$ för att säkerställa noggrannheten i operationerna på kurvan. Elliptiska kurvor över fältet av reella tal är föremål för felaktigheter på grund av avrundningsfel under beräkningsberäkningar. Om många operationer utförs på kurvan ackumuleras dessa fel och slutresultatet kan bli felaktigt eller svårt att återskapa. Genom att uteslutande använda positiva heltal säkerställs perfekt noggrannhet i beräkningarna och därmed reproducerbarhet i resultatet.


Matematiken för elliptiska kurvor över ändliga fält är analog med den över fältet av reella tal, med den anpassningen att alla operationer utförs modulo $p$. För att förenkla förklaringarna fortsätter vi i följande kapitel att illustrera begreppen med hjälp av en kurva definierad över reella tal, samtidigt som vi kommer ihåg att kurvan i praktiken är definierad över ett ändligt fält.


Om du vill lära dig mer om de matematiska grunderna för modern kryptografi rekommenderar jag också att du läser den här andra kursen på Plan ₿ Network:


https://planb.network/courses/d2fd9fc0-d9ed-4a87-9fa3-0fdbb3937e28

## Beräkning av den publika nyckeln från den privata nyckeln


<chapterId>fcb2bd58-5dda-5ecf-bb8f-ad1a0561ab4a</chapterId>

Som tidigare nämnts baseras de digitala signaturalgoritmerna i Bitcoin på ett par privata och offentliga nycklar som är matematiskt sammankopplade. Låt oss tillsammans utforska vad denna matematiska länk är och hur de genereras.


### Den privata nyckeln


Den privata nyckeln är helt enkelt ett slumpmässigt eller pseudoslumpmässigt tal. När det gäller Bitcoin är detta tal 256 bitar stort. Antalet möjligheter för en privat nyckel för Bitcoin är därför teoretiskt $2^{256}$.


**Notering**: Ett "pseudoslumptal" är ett tal som har egenskaper som ligger nära egenskaperna hos ett verkligt slumptal men som genereras av en deterministisk algoritm.


I praktiken finns det dock bara $n$ distinkta punkter på vår elliptiska kurva secp256k1, där $n$ är ordningen på kurvans generatorpunkt $G$. Vi kommer senare att se vad detta tal motsvarar, men kom helt enkelt ihåg att en giltig privat nyckel är ett heltal mellan $1$ och $n-1$, med vetskapen om att $n$ är ett tal nära men något mindre än $2^{256}$. Därför finns det vissa 256-bitars tal som inte är giltiga för att bli en privat nyckel i Bitcoin, nämligen alla tal mellan $n$ och $2^{256}$. Om genereringen av slumptalet (den privata nyckeln) ger ett värde $k$ som är så stort att $k \geq n$, anses det vara ogiltigt och ett nytt slumpvärde måste genereras.


Antalet möjligheter för en privat nyckel till Bitcoin är därför ca $n$, vilket är ett tal nära $1,158 \times 10^{77}$. Detta antal är så stort att om du väljer en privat nyckel slumpmässigt är det statistiskt sett nästan omöjligt att landa på en annan användares privata nyckel. För att ge dig en uppfattning om skalan är antalet möjliga privata nycklar i Bitcoin av en storleksordning som ligger nära antalet uppskattade atomer i det observerbara universum.


Som vi kommer att se i de kommande kapitlen genereras idag majoriteten av de privata nycklar som används i Bitcoin inte slumpmässigt utan är resultatet av deterministisk härledning från en Mnemonic-fras, i sig pseudoslumpmässig (detta är den berömda frasen med 12 eller 24 ord). Denna information förändrar ingenting för användningen av signaturalgoritmer som ECDSA, men den hjälper till att fokusera vår popularisering i Bitcoin.


I resten av förklaringen kommer den privata nyckeln att betecknas med den gemena bokstaven $k$.


### Den publika nyckeln


Den publika nyckeln är en punkt på den elliptiska kurvan, betecknad med den stora bokstaven $K$, och beräknas från den privata nyckeln $k$. Denna punkt $K$ representeras av ett koordinatpar $(x, y)$ på elliptisk kurva, där varje koordinat är ett heltal modulo $p$, det primtal som definierar det finita fältet $\mathbb{F}_p$.

I praktiken representeras en okomprimerad publik nyckel av 520 bitar (eller 65 byte), vilket motsvarar två 256-bitars tal ($x$ och $y$) placerade bout till bout, föregångna av 8-bitars prefixet $0x04$.


Det är emellertid också möjligt att representera den publika nyckeln i en komprimerad form med endast 33 byte (264 bitar) genom att endast behålla abscissen $x$ för vår punkt på kurvan och en byte som anger pariteten för $y$. Detta är vad som kallas en komprimerad offentlig nyckel. Jag kommer att prata mer om detta i de sista kapitlen i den här utbildningen. Men vad du behöver komma ihåg är att en offentlig nyckel $K$ är en punkt som beskrivs av $x$ och $y$.


För att beräkna den punkt $K$ som motsvarar vår publika nyckel använder vi operationen skalär multiplikation på elliptiska kurvor, definierad som en upprepad addition ($k$ gånger) av generatorpunkten $G$:


$$

K = k \cdot G


$$


var:



- $k$ är den privata nyckeln (ett slumpmässigt heltal mellan $1$ och $n-1$);
- $G$ är generatorpunkten för den elliptiska kurva som används av alla deltagare i Bitcoin-nätverket;
- $\cdot$ representerar den skalära multiplikationen på den elliptiska kurvan, vilket är likvärdigt med att addera punkten $G$ till sig själv $k$ gånger.


Det faktum att denna punkt $G$ är gemensam för alla publika nycklar i Bitcoin gör att vi kan vara säkra på att samma privata nyckel $k$ alltid kommer att ge oss samma publika nyckel $K$:


![CYP201](assets/fr/017.webp)


Den viktigaste egenskapen hos denna operation är att den är en envägsfunktion. Det är lätt att beräkna den publika nyckeln $K$ om man känner till den privata nyckeln $k$ och generatorpunkten $G$, men det är praktiskt taget omöjligt att beräkna den privata nyckeln $k$ om man bara känner till den publika nyckeln $K$ och generatorpunkten $G$. Att hitta $k$ från $K$ och $G$ innebär att lösa det diskreta logaritmproblemet på elliptiska kurvor, ett matematiskt svårt problem för vilket ingen effektiv algoritm är känd. Inte ens de mest kraftfulla nuvarande räknarna kan lösa detta problem på rimlig tid.


![CYP201](assets/fr/018.webp)


### Addition och fördubbling av punkter på elliptiska kurvor


Begreppet addition på elliptiska kurvor definieras geometriskt. Om vi har två punkter $P$ och $Q$ på kurvan, beräknas operationen $P + Q$ genom att dra en linje som går genom $P$ och $Q$. Denna linje kommer med nödvändighet att skära kurvan i en tredje punkt $R'$. Vi tar sedan spegelbilden av denna punkt i förhållande till x-axeln för att få punkten $R$, som är resultatet av additionen:


$$

P + Q = R


$$


Grafiskt kan detta beskrivas på följande sätt:


![CYP201](assets/fr/019.webp)


För fördubbling av en punkt, det vill säga operationen $P + P$, drar vi tangenten till kurvan i punkten $P$. Denna tangent skär kurvan i en annan punkt $S'$. Vi tar sedan spegelbilden av denna punkt med avseende på x-axeln för att få punkten $S$, som är resultatet av fördubblingen:


$$

2P = S


$$


Grafiskt visas detta som:


![CYP201](assets/fr/020.webp)


Genom att använda dessa additions- och dubbleringsoperationer kan vi utföra den skalära multiplikationen av en punkt med ett heltal $k$, betecknat $kP$, genom att utföra upprepade dubbleringar och additioner.


Anta till exempel att vi har valt en privat nyckel $k = 4$. För att beräkna den tillhörande offentliga nyckeln utför vi:


$$

K = k \cdot G = 4G


$$


Grafiskt motsvarar detta att utföra en serie additioner och dubbleringar:



- Beräkna $2G$ genom att dubbla $G$.
- Beräkna $4G$ genom att dubbla $2G$.


![CYP201](assets/fr/021.webp)


Om vi till exempel vill beräkna punkten $3G$, måste vi först beräkna punkten $2G$ genom att dubbla punkten $G$, och sedan addera $G$ och $2G$. För att addera $G$ och $2G$ är det bara att dra linjen som förbinder dessa två punkter, ta fram den unika punkten $-3G$ i skärningspunkten mellan denna linje och den elliptiska kurvan och sedan bestämma $3G$ som motsatsen till $-3G$.


Vi kommer att ha:


$$

G + G = 2G


$$


$$

2G + G = 3G


$$


Grafiskt kan detta beskrivas på följande sätt:


![CYP201](assets/fr/022.webp)


### Envägsfunktion


Tack vare dessa operationer kan vi förstå varför det är lätt att härleda en publik nyckel från en privat nyckel, men det omvända är praktiskt taget omöjligt.


Låt oss gå tillbaka till vårt förenklade exempel. Med en privat nyckel $k = 4$. För att beräkna den tillhörande offentliga nyckeln utför vi:


$$
K = k \cdot G = 4G
$$


Vi har alltså enkelt kunnat beräkna den publika nyckeln $K$ genom att känna till $k$ och $G$.


Om någon nu bara känner till den publika nyckeln $K$, står de inför det diskreta logaritmproblemet: att hitta $k$ så att $K = k \cdot G$. Detta problem anses vara svårt eftersom det inte finns någon effektiv algoritm för att lösa det på elliptiska kurvor. Detta garanterar säkerheten för ECDSA- och Schnorr-algoritmerna.


I det här förenklade exemplet med $k = 4$ skulle det naturligtvis vara möjligt att hitta $k$ genom att pröva sig fram, eftersom antalet möjligheter är lågt. I praktiken är dock $k$ ett 256-bitars heltal, vilket gör att antalet möjligheter är astronomiskt stort (cirka 1,158 gånger 10^{77}$). Därför är det inte möjligt att hitta $k$ med brute force.


## Signera med den privata nyckeln


<chapterId>bb07826f-826e-5905-b307-3d82001fb778</chapterId>


Nu när du vet hur man härleder en offentlig nyckel från en privat nyckel kan du redan ta emot bitcoins genom att använda detta nyckelpar som ett utgiftsvillkor. Men hur spenderar man dem? För att spendera bitcoins måste du låsa upp _scriptPubKey_ som är kopplad till din UTXO för att bevisa att du verkligen är dess legitima ägare. För att göra detta måste du producera en signatur $s$ som matchar den offentliga nyckeln $K$ som finns i _scriptPubKey_ med hjälp av den privata nyckeln $k$ som ursprungligen användes för att beräkna $K$. Den digitala signaturen är således ett ovedersägligt bevis på att du har den privata nyckel som är kopplad till den publika nyckel som du hävdar.


### Parametrar för elliptiska kurvor


För att utföra en digital signatur måste alla deltagare först komma överens om parametrarna för den elliptiska kurva som används. När det gäller Bitcoin är parametrarna för **secp256k1** följande:


Det ändliga fältet $\mathbb{Z}_p$ definieras av:


$$
p = 2^{256} - 2^{32} - 977
$$


```text
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
```


$p$ är ett mycket stort primtal som är något mindre än $2^{256}$.


Den elliptiska kurvan $y^2 = x^3 + ax + b$ över $\mathbb{Z}_p$ definieras av:


$$
a = 0, \quad b = 7
$$


Generatorpunkten eller ursprungspunkten $G$:


```text
G = 0x0279BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
```


Detta tal är den komprimerade formen som endast ger abscissen för punkten $G$. Prefixet `02` i början bestämmer vilket av de två värdena som har denna abscissa $x$ som ska användas som genereringspunkt.

Ordningen $n$ av $G$ (antalet existerande punkter) och cofaktorn $h$:


```text
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
```


$n$ är ett mycket stort tal som är något mindre än $p$.


$$
h=1
$$


$h$ är kofaktorn eller antalet undergrupper. Jag kommer inte att utveckla vad detta representerar här, eftersom det är ganska komplext, och i fallet med Bitcoin behöver vi inte ta hänsyn till det eftersom det är lika med $1$.


All denna information är offentlig och känd av alla deltagare. Tack vare dem kan användarna skapa en digital signatur och verifiera den.


### Signatur med ECDSA


ECDSA-algoritmen gör det möjligt för en användare att signera ett meddelande med sin privata nyckel på ett sådant sätt att alla som känner till motsvarande offentliga nyckel kan verifiera signaturens giltighet utan att den privata nyckeln någonsin avslöjas. I samband med Bitcoin beror det meddelande som ska signeras på den _sighash_ som användaren väljer. Det är denna _sighash_ som avgör vilka delar av transaktionen som täcks av signaturen. Jag kommer att prata mer om detta i nästa kapitel.


Här följer stegen för att generate en ECDSA-signatur:


Först beräknar vi Hash ($e$) för det meddelande som ska signeras. Meddelandet $m$ skickas alltså genom en kryptografisk Hash-funktion, vanligtvis SHA256 eller dubbel SHA256 när det gäller Bitcoin:


$$
e = \text{HASH}(m)
$$


Därefter beräknar vi ett Nonce. Inom kryptografi är en Nonce helt enkelt ett tal som genereras på ett slumpmässigt eller pseudoslumpmässigt sätt och som bara används en gång. Det vill säga att varje gång en ny digital signatur görs med det här nyckelparet är det mycket viktigt att använda en annan Nonce, annars kommer det att äventyra säkerheten för den privata nyckeln. Det är därför tillräckligt att bestämma ett slumpmässigt och unikt heltal $r$ så att $1 \leq r \leq n-1$, där $n$ är ordningen på den elliptiska kurvans genereringspunkt $G$.


Sedan beräknar vi punkten $R$ på den elliptiska kurvan med koordinaterna $(x_R, y_R)$ så att:


$$
R = r \cdot G
$$


Vi extraherar värdet på abscissen för punkten $R$ ($x_R$). Detta värde representerar den första delen av signaturen. Och slutligen beräknar vi den andra delen av signaturen $s$ på detta sätt:


$$
s = r^{-1} \left( e + k \cdot x_R \right) \mod n
$$


var:



- $r^{-1}$ är den modulära inversen av $r$ modulo $n$, det vill säga ett heltal som är sådant att $r \cdot r^{-1} \equiv 1 \mod n$;
- $k$ är användarens privata nyckel;
- $e$ är Hash för meddelandet;
- $n$ är ordningen på den elliptiska kurvans generatorpunkt $G$.


Signaturen är då helt enkelt sammankopplingen av $x_R$ och $s$:


$$
\text{SIG} = x_R \Vert s
$$


### Verifiering av ECDSA-signaturen


För att verifiera en signatur $(x_R, s)$ kan alla som känner till den publika nyckeln $K$ och parametrarna för den elliptiska kurvan gå tillväga på detta sätt:


Kontrollera först att $x_R$ och $s$ ligger inom intervallet $[1, n-1]$. Detta säkerställer att signaturen respekterar de matematiska begränsningarna för den elliptiska gruppen. Om så inte är fallet avvisar verifieraren omedelbart signaturen som ogiltig.


Beräkna sedan Hash för meddelandet:


$$
e = \text{HASH}(m)
$$


Beräkna den modulära inversen av $s$ modulo $n$:


$$
s^{-1} \mod n
$$


Beräkna två skalära värden $u_1$ och $u_2$ på detta sätt:


$$
\begin{align*}
u_1 &= e \cdot s^{-1} \mod n \\
u_2 &= x_R \cdot s^{-1} \mod n
\end{align*}
$$


Och slutligen, beräkna den punkt $V$ på den elliptiska kurvan som är sådan att:


$$
V = u_1 \cdot G + u_2 \cdot K
$$


Signaturen är giltig endast om $x_V \equiv x_R \mod n$, där $x_V$ är $x$-koordinaten för punkten $V$. Genom att kombinera $u_1 \cdot G$ och $u_2 \cdot K$ erhåller man en punkt $V$ som, om signaturen är giltig, måste motsvara den punkt $R$ som används vid signeringen (modulo $n$).


### Underskrift med Schnorr-protokollet


Schnorr-signaturschemat är ett alternativ till ECDSA som erbjuder många fördelar. Det har varit möjligt att använda det i Bitcoin sedan 2021 och introduktionen av Taproot, med P2TR-skriptmönstren. Liksom ECDSA tillåter Schnorr-schemat att ett meddelande signeras med en privat nyckel på ett sådant sätt att signaturen kan verifieras av alla som känner till motsvarande offentliga nyckel.

När det gäller Schnorr används exakt samma kurva som ECDSA med samma parametrar. De offentliga nycklarna representeras dock på ett något annorlunda sätt jämfört med ECDSA. De betecknas nämligen endast med $x$-koordinaten för punkten på den elliptiska kurvan. Till skillnad från ECDSA, där komprimerade offentliga nycklar representeras av 33 byte (med prefixbyte som anger pariteten för $y$), använder Schnorr offentliga nycklar på 32 byte, som endast motsvarar $x$-koordinaten för punkten $K$, och det antas att $y$ är jämn som standard. Denna förenklade representation minskar storleken på signaturerna och underlättar vissa optimeringar i verifieringsalgoritmerna.

Den publika nyckeln är då $x$-koordinaten för punkten $K$:


$$
\text{pk} = K_x
$$


Det första steget för att generate en signatur är att Hash meddelandet. Men till skillnad från ECDSA görs det med andra värden och en märkt Hash-funktion används för att undvika kollisioner i olika sammanhang. En märkt Hash-funktion innebär helt enkelt att en godtycklig etikett läggs till Hash-funktionens ingångar tillsammans med meddelandedata.


![CYP201](assets/fr/023.webp)


Förutom meddelandet skickas även $x$-koordinaten för den publika nyckeln $K_x$ samt punkten $R = r \cdot G$, beräknad från Nonce $r$ (som i sig är ett unikt heltal för varje signatur, beräknat deterministiskt från den privata nyckeln och meddelandet för att undvika sårbarheter relaterade till återanvändning av Nonce), till den märkta funktionen. Precis som för den publika nyckeln behålls endast $x$-koordinaten för Nonce-punkten $R_x$ för att beskriva punkten.


Resultatet av denna hashing noterade $e$ kallas "utmaningen":


$$
e = \text{HASH}(\text{``BIP0340/challenge''}, R_x \Vert K_x \Vert m) \mod n
$$


Här är $\text{Hash}$ funktionen SHA256 Hash och $\text{``BIP0340/challenge''}$ är den specifika taggen för hashingen.


Slutligen beräknas parametern $s$ från den privata nyckeln $k$, Nonce $r$ och utmaningen $e$ enligt följande:


$$
s = (r + e \cdot k) \mod n
$$


Signaturen är då helt enkelt paret $R_x$ och $s$.


$$
\text{SIG} = R_x \Vert s
$$


### Verifiering av Schnorr-signaturen


Verifieringen av en Schnorr-signatur är enklare än verifieringen av en ECDSA-signatur. Här följer stegen för att verifiera signaturen $(R_x, s)$ med den offentliga nyckeln $K_x$ och meddelandet $m$.

Först kontrollerar vi att $K_x$ är ett giltigt heltal som är mindre än $p$. Om så är fallet hämtar vi motsvarande punkt på kurvan där $K_y$ är jämnt. Vi extraherar också $R_x$ och $s$ genom att dela upp signaturen $\text{SIG}$. Sedan kontrollerar vi att $R_x < p$ och $s < n$ (kurvans ordning).

Därefter beräknar vi utmaningen $e$ på samma sätt som utfärdaren av signaturen:


$$
e = \text{HASH}(\text{``BIP0340/challenge''}, R_x \Vert K_x \Vert m) \mod n
$$


Sedan beräknar vi en referenspunkt på kurvan på det här sättet:


$$
R' = s \cdot G - e \cdot K
$$


Slutligen verifierar vi att $R'_x = R_x$. Om de två x-koordinaterna matchar är signaturen $(R_x, s)$ verkligen giltig med den publika nyckeln $K_x$.


### Varför fungerar det här?


Signaturen har beräknat $s = r + e \cdot k \mod n$, så $R' = s \cdot G - e \cdot K$ bör vara lika med den ursprungliga punkten $R$, eftersom:


$$
s \cdot G = (r + e \cdot k) \cdot G = r \cdot G + e \cdot k \cdot G
$$


Eftersom $K = k \cdot G$, har vi $e \cdot k \cdot G = e \cdot K$. På så sätt..:


$$
R' = r \cdot G = R
$$


Därför har vi det:


$$
R'_x = R_x
$$


### Fördelarna med Schnorr-signaturer


Schnorr-signaturschemat erbjuder flera fördelar för Bitcoin jämfört med den ursprungliga ECDSA-algoritmen. För det första möjliggör Schnorr aggregering av nycklar och signaturer. Detta innebär att flera publika nycklar kan kombineras till en enda nyckel.


![CYP201](assets/fr/024.webp)


På samma sätt kan flera signaturer sammanföras till en enda giltig signatur. Vid en transaktion med flera signaturer kan alltså en uppsättning deltagare signera med en enda signatur och en enda aggregerad publik nyckel. Detta minskar avsevärt lagrings- och beräkningskostnaderna för nätverket, eftersom varje nod bara behöver verifiera en enda signatur.


![CYP201](assets/fr/025.webp)


Aggregering av signaturer förbättrar dessutom integriteten. Med Schnorr blir det omöjligt att skilja en transaktion med flera signaturer från en standardtransaktion med en enda signatur. Denna homogenitet gör kedjeanalysen svårare, eftersom den begränsar möjligheten att identifiera Wallet-fingeravtryck.


Slutligen erbjuder Schnorr också möjligheten till batchverifiering. Genom att verifiera flera signaturer samtidigt kan noderna bli mer effektiva, särskilt för block som innehåller många transaktioner. Denna optimering minskar den tid och de resurser som krävs för att validera ett block.

Schnorr-signaturer är inte heller formbara, till skillnad från signaturer som produceras med ECDSA. Detta innebär att en angripare inte kan modifiera en giltig signatur för att skapa en annan giltig signatur för samma meddelande och samma publika nyckel. Denna sårbarhet fanns tidigare i Bitcoin och förhindrade framför allt en säker implementering av Lightning Network. Den löstes för ECDSA med SegWit softfork 2017, vilket innebär att signaturerna flyttas till en separat databas från transaktionerna för att förhindra att de kan manipuleras.


### Varför valde Satoshi ECDSA?


Som vi har sett valde Satoshi ursprungligen att implementera ECDSA för digitala signaturer i Bitcoin. Men vi har också sett att Schnorr är överlägset ECDSA i många avseenden, och detta protokoll skapades av Claus-Peter Schnorr 1989, 20 år innan Bitcoin uppfanns.


Tja, vi vet inte riktigt varför Satoshi inte valde det, men en trolig hypotes är att detta protokoll var under patent fram till 2008. Även om Bitcoin skapades ett år senare, i januari 2009, fanns ingen standardisering med öppen källkod för Schnorr-signaturer tillgänglig vid den tidpunkten. Kanske ansåg Satoshi att det var säkrare att använda ECDSA, som redan användes och testades i stor utsträckning i programvara med öppen källkod och hade flera erkända implementeringar (särskilt OpenSSL-biblioteket som användes fram till 2015 i Bitcoin Core och sedan ersattes av libsecp256k1 i version 0.10.0). Eller så kanske han helt enkelt inte var medveten om att patentet skulle löpa ut 2008. I vilket fall som helst verkar den mest sannolika hypotesen vara relaterad till detta patent och det faktum att ECDSA hade en beprövad historia och var lättare att implementera.


## Sighash-flaggorna


<chapterId>231c41a2-aff2-4655-9048-47b6d2d83d64</chapterId>


Som vi har sett i tidigare kapitel används digitala signaturer ofta för att låsa upp skriptet för en inmatning. I signeringsprocessen är det nödvändigt att inkludera de signerade uppgifterna i beräkningen, i våra exempel betecknade med meddelandet $m$. När dessa data väl har signerats kan de inte ändras utan att signaturen blir ogiltig. Oavsett om det gäller ECDSA eller Schnorr måste signaturverifieraren inkludera samma meddelande $m$ i sin beräkning. Om det skiljer sig från det meddelande $m$ som undertecknaren ursprungligen använde, blir resultatet felaktigt och signaturen anses ogiltig. Man kan då säga att en signatur täcker vissa data och på sätt och vis skyddar dem mot obehöriga ändringar.


### Vad är en sighash-flagga?


I det specifika fallet med Bitcoin har vi sett att meddelandet $m$ motsvarar transaktionen. I verkligheten är det dock lite mer komplicerat. Tack vare sighash-flaggor är det faktiskt möjligt att välja specifika data inom transaktionen som ska täckas eller inte täckas av signaturen.

"Sighash-flaggan" är således en parameter som läggs till varje ingång och som gör det möjligt att fastställa vilka delar av en transaktion som omfattas av den tillhörande signaturen. Dessa komponenter är ingångar och utgångar. Valet av sighash-flagga avgör således vilka inmatningar och utmatningar i transaktionen som fixeras av signaturen och vilka som fortfarande kan modifieras utan att den ogiltigförklaras. Denna mekanism gör det möjligt för signaturer att binda transaktionsdata i enlighet med undertecknarens avsikter.


När transaktionen har bekräftats på Blockchain blir den naturligtvis oföränderlig, oavsett vilka sighash-flaggor som används. Möjligheten att ändra via sighash-flaggorna är begränsad till perioden mellan signeringen och bekräftelsen.


Generellt erbjuder inte Wallet-programvaran dig möjligheten att manuellt ändra sighash-flaggan för dina inmatningar när du konstruerar en transaktion. Som standard är `SIGHASH_ALL` inställd. Personligen känner jag bara till Sparrow wallet som tillåter denna modifiering från användaren Interface.


### Vilka är de befintliga sighash-flaggorna i Bitcoin?


I Bitcoin finns det först och främst 3 grundläggande sighash-flaggor:



- `SIGHASH_ALL` (`0x01`): Signaturen gäller för alla inmatningar och alla utmatningar i transaktionen. Transaktionen är därmed helt täckt av signaturen och kan inte längre modifieras. `SIGHASH_ALL` är den vanligaste sighashen i vardagliga transaktioner när man helt enkelt vill göra en transaktion utan att den kan modifieras.


![CYP201](assets/fr/026.webp)


I alla diagram i det här kapitlet representerar den orange färgen de Elements som omfattas av signaturen, medan den svarta färgen anger de som inte omfattas.



- `SIGHASH_NONE` (`0x02`): Signaturen täcker alla ingångar men ingen av utgångarna, vilket gör det möjligt att ändra utgångarna efter signaturen. I konkreta termer är detta att likna vid en blankocheck. Undertecknaren låser upp UTXO:erna i ingångarna men lämnar fältet med utgångar helt modifierbart. Vem som helst som känner till denna transaktion kan således lägga till valfri output, t.ex. genom att ange en mottagande Address för att samla in de medel som förbrukats av inputs och sedan sända transaktionen för att återfå bitcoins. Signaturen från ägaren av inputs kommer inte att ogiltigförklaras, eftersom den endast täcker inputs.


![CYP201](assets/fr/027.webp)



- `SIGHASH_SINGLE` (`0x03`): Signaturen täcker alla inmatningar samt en enda utmatning, motsvarande indexet för den signerade inmatningen. Om signaturen t.ex. låser upp _scriptPubKey_ för indata #0, täcker den även utdata #0. Signaturen skyddar även alla andra inmatningar, som inte längre kan ändras. Vem som helst kan dock lägga till ytterligare en utgång utan att signaturen ogiltigförklaras, förutsatt att utgång #0, som är den enda som omfattas av den, inte ändras.


![CYP201](assets/fr/028.webp)


Förutom dessa tre sighashflaggor finns också modifieraren `SIGHASH_ANYONECANPAY` (`0x80`). Denna modifierare kan kombineras med en grundläggande sighashflagga för att skapa tre nya sighashflaggor:



- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): Signaturen täcker en enda inmatning samtidigt som den inkluderar alla utmatningar från transaktionen. Denna kombinerade sighash-flagga tillåter till exempel skapandet av en crowdfunding-transaktion. Organisatören förbereder outputen med sin Address och målbeloppet, och varje investerare kan sedan lägga till inputs för att finansiera denna output. När tillräckligt med medel har samlats in för att tillgodose outputen kan transaktionen sändas.


![CYP201](assets/fr/029.webp)



- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): Signaturen täcker en enda input, utan att förbinda sig till någon output;


![CYP201](assets/fr/030.webp)



- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): Signaturen täcker en enda inmatning samt den utmatning som har samma index som denna inmatning. Om signaturen t.ex. låser upp _scriptPubKey_ för input #3, täcker den även output #3. Resten av transaktionen är fortfarande modifierbar, både när det gäller andra inmatningar och andra utmatningar.


![CYP201](assets/fr/031.webp)


### Projekt för att lägga till nya Sighash-flaggor


För närvarande (2024) är endast de sighash-flaggor som presenteras i föregående avsnitt användbara i Bitcoin. Vissa projekt överväger dock att lägga till nya sighash-flaggor. Till exempel introducerar BIP118, som föreslagits av Christian Decker och Anthony Towns, två nya sighash-flaggor: `SIGHASH_ANYPREVOUT` och `SIGHASH_ANYPREVOUTANYSCRIPT` (_AnyPrevOut = "Alla tidigare utdata"_).


Dessa två sighash-flaggor skulle ge ytterligare en möjlighet i Bitcoin: att skapa signaturer som inte täcker någon specifik del av transaktionen.


![CYP201](assets/fr/032.webp)


Den här idén formulerades ursprungligen av Joseph Poon och Thaddeus Dryja i Lightning White Paper. Innan den döptes om hette den här sighash-flaggan `SIGHASH_NOINPUT`.

Om denna sighash-flagga integreras i Bitcoin kommer det att möjliggöra användning av covenants, men det är också en obligatorisk förutsättning för att implementera Eltoo, ett allmänt protokoll för andra lager som definierar hur man gemensamt hanterar Ownership i en UTXO. Eltoo är särskilt utformat för att lösa de problem som är förknippade med mekanismerna för att förhandla om tillståndet för Lightning-kanaler, det vill säga mellan öppning och stängning.


För att fördjupa dina kunskaper om Lightning Network efter CYP201-kursen rekommenderar jag starkt LNP201-kursen av Fanis Michalakis, som behandlar ämnet i detalj:


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

I nästa del föreslår jag att du upptäcker hur Mnemonic-frasen vid basen av din Bitcoin Wallet fungerar.


# Mnemonic-frasen


<partId>4070af16-c8a2-58b5-9871-a22c86c07458</partId>


## Utvecklingen av Bitcoin-plånböcker


<chapterId>9d9acd5d-a0e5-5dfd-b544-f043fae8840f</chapterId>


Nu när vi har utforskat hur Hash-funktioner och digitala signaturer fungerar kan vi studera hur Bitcoin-plånböcker fungerar. Målet är att beskriva hur en Wallet i Bitcoin är uppbyggd, hur den bryts ned och vad de olika informationsbitarna som utgör den används till. Denna förståelse för Wallet-mekanismerna gör att du kan förbättra din användning av Bitcoin när det gäller säkerhet och integritet.


Innan vi går in på de tekniska detaljerna är det viktigt att klargöra vad som menas med "Bitcoin Wallet" och att förstå dess användningsområde.


### Vad är en Bitcoin Wallet?


Till skillnad från traditionella plånböcker, som låter dig lagra fysiska sedlar och mynt, "innehåller" en Bitcoin Wallet inte bitcoins i sig. Bitcoins existerar faktiskt inte i en fysisk eller digital form som kan lagras, utan representeras av kontoenheter som avbildas i Bitcoin-systemet i form av **UTXOs** (_Unspent Transaction Outputs_).


UTXO:er representerar således fragment av bitcoins, av varierande storlek, som kan spenderas förutsatt att deras _scriptPubKey_ är uppfylld. För att spendera sina bitcoins måste en användare tillhandahålla en _scriptSig_ som låser upp den _scriptPubKey_ som är kopplad till hans UTXO. Detta bevis görs i allmänhet genom en digital signatur som genereras från den privata nyckel som motsvarar den publika nyckel som finns i _scriptPubKey_. Det avgörande elementet som användaren måste säkra är alltså den privata nyckeln.

Rollen för en Bitcoin Wallet är just att hantera dessa privata nycklar på ett säkert sätt. I själva verket är dess roll mer besläktad med en nyckelring än en Wallet i traditionell mening.


### JBOK Plånböcker


De första plånböckerna som användes i Bitcoin var JBOK-plånböcker (_Just a Bunch Of Keys_), som grupperade privata nycklar som genererats oberoende av varandra och utan någon länk mellan dem. Dessa plånböcker fungerade enligt en enkel modell där varje privat nyckel kunde låsa upp en unik Bitcoin som tog emot Address.


![CYP201](assets/fr/033.webp)


Om man ville använda flera privata nycklar var det då nödvändigt att göra så många säkerhetskopior för att säkerställa tillgång till medel i händelse av problem med den enhet som var värd för Wallet. Om man använder en enda privat nyckel kan denna Wallet-struktur vara tillräcklig, eftersom det räcker med en enda säkerhetskopia. Detta utgör dock ett problem: i Bitcoin avråds starkt från att alltid använda samma privata nyckel. En privat nyckel är faktiskt associerad med en unik Address, och Bitcoin-mottagningsadresser är normalt utformade för engångsbruk. Varje gång du tar emot pengar bör du generate en ny tom Address.


Denna begränsning härrör från Bitcoin:s sekretessmodell. Genom att återanvända samma Address blir det lättare för externa observatörer att spåra Bitcoin-transaktioner. Det är därför som återanvändning av en mottagande Address starkt avråds. För att ha flera adresser och offentligt separera våra transaktioner är det dock nödvändigt att hantera flera privata nycklar. När det gäller JBOK-plånböcker innebär detta att man skapar lika många säkerhetskopior som det finns nya nyckelpar, en uppgift som snabbt kan bli komplex och svår att underhålla för användarna.


För att lära dig mer om Bitcoin:s integritetsmodell och upptäcka metoder för att skydda din integritet rekommenderar jag också att du följer min BTC204-kurs om Plan ₿ Network:


https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### HD plånböcker


För att Address komma till rätta med begränsningarna i JBOK-plånböckerna användes därefter en ny Wallet-struktur. År 2012 föreslog Pieter Wuille en förbättring med BIP32, som introducerar HD-plånböcker (Hierarchical Deterministic). Principen för en HD Wallet är att härleda alla privata nycklar från en enda informationskälla, en så kallad seed, på ett deterministiskt och hierarkiskt sätt. Denna seed genereras slumpmässigt när Wallet skapas och utgör en unik säkerhetskopia som gör det möjligt att återskapa alla Wallet:s privata nycklar. Användaren kan alltså generate ett mycket stort antal privata nycklar för att undvika Address återanvändning och bevara sin integritet, samtidigt som han eller hon bara behöver göra en enda säkerhetskopia av sin Wallet via seed.


![CYP201](assets/fr/034.webp)


I HD-plånböcker utförs nyckelderivation enligt en hierarkisk struktur som gör det möjligt att organisera nycklar i derivationsunderutrymmen, där varje underutrymme kan delas upp ytterligare, för att underlätta fondhantering och interoperabilitet mellan olika Wallet-programvaror. Numera används denna standard av de allra flesta Bitcoin-användare. Av denna anledning kommer vi att undersöka den i detalj i följande kapitel.


### BIP39-standarden: Mnemonic-frasen


Utöver BIP32 standardiserar BIP39 seed-formatet som en Mnemonic-fras för att underlätta säkerhetskopiering och läsbarhet för användare. Mnemonic-frasen, även kallad återställningsfras eller 24-ordsfras, är en sekvens av ord som hämtas från en fördefinierad lista och som på ett säkert sätt kodar Wallet:s seed.


Mnemonic-frasen förenklar i hög grad säkerhetskopiering för användaren. I händelse av förlust, skada eller stöld av den enhet som är värd för Wallet, kan Wallet återskapas och återfå åtkomst till alla medel som är säkrade av den genom att helt enkelt känna till denna Mnemonic-fras.


I de kommande kapitlen kommer vi att utforska det interna arbetet i HD-plånböcker, inklusive mekanismer för nyckelavledning och olika möjliga hierarkiska strukturer. Detta kommer att göra det möjligt för dig att bättre förstå de kryptografiska grunder som säkerheten för medel i Bitcoin bygger på. Och för att börja, i nästa kapitel, föreslår jag att vi upptäcker entropins roll i basen av din Wallet.


## Entropi och slumpmässiga tal


<chapterId>b43c715d-affb-56d8-a697-ad5bc2fffd63</chapterId>

Moderna HD-plånböcker förlitar sig på en enda initial information som kallas "entropi" för att deterministiskt generate hela uppsättningen Wallet-nycklar. Denna entropi är ett pseudoslumpmässigt tal som delvis avgör säkerheten för Wallet.


### Definition av entropi


Entropi är i samband med kryptografi och information ett kvantitativt mått på den osäkerhet eller oförutsägbarhet som är förknippad med en datakälla eller en slumpmässig process. Entropin spelar en viktig roll för säkerheten i kryptografiska system, särskilt när det gäller generering av nycklar och slumptal. Hög entropi säkerställer att de genererade nycklarna är tillräckligt oförutsägbara och motståndskraftiga mot brute force-attacker, där en angripare försöker gissa sig till nyckeln med alla möjliga kombinationer.


I samband med Bitcoin används entropi för att generate seed. När man skapar en HD Wallet görs konstruktionen av Mnemonic-frasen från ett slumpmässigt tal, som i sin tur härrör från en källa till entropi. Frasen används sedan för att generate flera privata nycklar, på ett deterministiskt och hierarkiskt sätt, för att skapa utgiftsvillkor för UTXO:er.


### Metoder för att generera entropi


Den initiala entropi som används för en HD Wallet är i allmänhet 128 bitar eller 256 bitar, där:



- 128 bitars entropi motsvarar en Mnemonic-fras på **12 ord**;
- 256 bitars entropi motsvarar en Mnemonic-fras på **24 ord**.


I de flesta fall genereras detta slumptal automatiskt av programvaran Wallet med hjälp av en PRNG (_Pseudo-Random Number Generator_). PRNG är en kategori av algoritmer som används för att generate generera talsekvenser från ett initialt tillstånd, som har egenskaper som närmar sig ett slumpmässigt tal, utan att egentligen vara ett sådant. En bra PRNG måste ha egenskaper som enhetlighet i utdata, oförutsägbarhet och motståndskraft mot prediktiva attacker. Till skillnad från äkta slumptalsgeneratorer (TRNG) är PRNG deterministiska och reproducerbara.


![CYP201](assets/fr/035.webp)


Ett alternativ är att manuellt generate entropin, vilket ger bättre kontroll men också är mycket mer riskabelt. Jag avråder starkt från att generera entropin för din HD Wallet själv.


I nästa kapitel ska vi se hur vi går från ett slumpmässigt tal till en Mnemonic-fras med 12 eller 24 ord.


## Mnemonic-frasen


<chapterId>8f9340c1-e6dc-5557-a2f2-26c9669987d5</chapterId>

Mnemonic-frasen, även kallad "seed-fras", "återhämtningsfras", "hemlig fras" eller "24-ordsfras", är en sekvens som vanligtvis består av 12 eller 24 ord, som genereras från entropi. Den används för att på ett deterministiskt sätt härleda alla nycklar till en HD Wallet. Detta innebär att det från denna fras är möjligt att deterministiskt generate och återskapa alla privata och offentliga nycklar till Bitcoin Wallet, och följaktligen få tillgång till de medel som skyddas med den. Syftet med Mnemonic-frasen är att tillhandahålla ett sätt att säkerhetskopiera och återskapa bitcoins som är både säkert och enkelt att använda. Den introducerades 2013 med BIP39-standarden.


Låt oss tillsammans upptäcka hur vi kan gå från entropi till en Mnemonic-fras.


### Kontrollsumman


För att omvandla entropi till en Mnemonic-fras måste man först lägga till en kontrollsumma (eller "kontrollsumma") i slutet av entropin. Denna kontrollsumma är en kort sekvens av bitar som säkerställer dataintegriteten genom att verifiera att ingen oavsiktlig modifiering har införts.


För att beräkna kontrollsumman tillämpas funktionen SHA256 Hash på entropin (bara en gång; detta är ett av de sällsynta fall i Bitcoin där en enda SHA256 Hash används i stället för en dubbel Hash). Denna operation producerar en 256-bitars Hash. Kontrollsumman består av de första bitarna i denna Hash, och dess längd beror på entropins längd, enligt följande formel:


$$
\text{CS} = \frac{\text{ENT}}{32}
$$


där $\text{ENT}$ representerar entropins längd i bitar och $\text{CS}$ kontrollsummans längd i bitar.


För en entropi på 256 bitar används t.ex. de första 8 bitarna av Hash för att bilda kontrollsumman:


$$
\text{CS} = \frac{256}{32} = 8 \text{ bits}
$$


När kontrollsumman har beräknats sammanlänkas den med entropin för att få en utökad bitsekvens som noteras $\text{ENT} \Vert \text{CS}$ ("concatenate" betyder att sätta ihop ända till ända).


![CYP201](assets/fr/036.webp)


### Korrespondens mellan entropi och Mnemonic-frasen


Antalet ord i Mnemonic-frasen beror på storleken på den ursprungliga entropin, vilket illustreras i följande tabell:



- $\text{ENT}$: storleken i bitar på entropin;
- $\text{CS}$: storleken i bitar på kontrollsumman;
- $w$: antalet ord i den slutliga Mnemonic-frasen.


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


Till exempel, för en 256-bitars entropi är resultatet $\text{ENT} \Vert \text{CS}$ är 264 bitar och ger en Mnemonic-fras på 24 ord.


### Omvandling av den binära sekvensen till en Mnemonic-fras


Bitsekvensen $\text{ENT} \Vert \text{CS}$ är sedan uppdelad i segment om 11 bitar. Varje 11-bitarssegment motsvarar, efter omvandling till decimal, ett tal mellan 0 och 2047, vilket anger positionen för ett ord [i en lista med 2048 ord som standardiserats av BIP39] (https://github.com/Planb-Network/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf).


![CYP201](assets/fr/037.webp)


För en 128-bitars entropi är t.ex. kontrollsumman 4 bitar och den totala sekvensen mäter alltså 132 bitar. Den är indelad i 12 segment om 11 bitar (de orange bitarna anger kontrollsumman):


![CYP201](assets/fr/038.webp)


Varje segment konverteras sedan till ett decimaltal som representerar ett ord i listan. Till exempel motsvarar det binära segmentet `01011010001` i decimalform `721`. Genom att lägga till 1 för att anpassa sig till listans indexering (som börjar på 1 och inte 0) får man ordrankningen `722`, vilket är "_focus_" i listan.


![CYP201](assets/fr/039.webp)


Denna korrespondens upprepas för vart och ett av de 12 segmenten för att erhålla en fras med 12 ord.


![CYP201](assets/fr/040.webp)


### Egenskaper hos BIP39-ordlistan


En särskild egenskap hos BIP39-ordlistan är att inget ord delar samma fyra första bokstäver i samma ordning med ett annat ord. Det innebär att det räcker att skriva ner endast de fyra första bokstäverna i varje ord för att spara Mnemonic-frasen. Detta kan vara intressant för att spara utrymme, särskilt för dem som vill gravera den på ett metallstöd.


Denna lista med 2048 ord finns på flera språk. Det är inte enkla översättningar, utan distinkta ord för varje språk. Det är dock starkt rekommenderat att hålla sig till den engelska versionen, eftersom versioner på andra språk i allmänhet inte stöds av Wallet-programvaran.


### Vilken längd ska du välja för din Mnemonic-fras?


För att bestämma den optimala längden på din Mnemonic-fras måste man ta hänsyn till den faktiska säkerhet som den ger. En fras på 12 ord ger 128 bitars säkerhet, medan en fras på 24 ord ger 256 bitars säkerhet.


Denna skillnad i säkerhet på frasnivå förbättrar dock inte den övergripande säkerheten för en Bitcoin Wallet, eftersom de privata nycklar som härleds från denna fras endast drar nytta av 128 bitars säkerhet. Som vi har sett tidigare genereras privata Bitcoin-nycklar från slumptal (eller härleds från en slumpmässig källa) som sträcker sig mellan $1$ och $n-1$, där $n$ representerar ordningen på generatorpunkten $G$ i secp256k1-kurvan, ett tal som är något mindre än $2^{256}$. Man skulle därför kunna tro att dessa privata nycklar erbjuder 256 bitars säkerhet. Deras säkerhet ligger dock i svårigheten att hitta en privat nyckel från dess tillhörande offentliga nyckel, en svårighet som fastställts av det matematiska problemet med den diskreta logaritmen på elliptiska kurvor (_ECDLP_). Den hittills mest kända algoritmen för att lösa detta problem är Pollards rho-algoritm, som minskar antalet operationer som krävs för att knäcka en nyckel till kvadratroten av dess storlek.


För 256-bitarsnycklar, som de som används i Bitcoin, reducerar Pollards rho-algoritm komplexiteten till $2^{128}$ operationer:


$$

O(\sqrt{2^{256}}) = O(2^{128})


$$


Därför anses det att en privat nyckel som används i Bitcoin erbjuder 128 bitars säkerhet.


Att välja en fras på 24 ord ger därför inte ytterligare skydd för Wallet, eftersom 256 bitars säkerhet för frasen är meningslöst om de härledda nycklarna endast ger 128 bitars säkerhet. För att illustrera den här principen är det som att ha ett hus med två dörrar: en gammal trädörr och en förstärkt dörr. Vid ett inbrott skulle den förstärkta dörren inte vara till någon nytta, eftersom inkräktaren skulle gå igenom trädörren. Det är en analog situation här.


En 12-ordsfras, som också erbjuder 128 bitars säkerhet, är därför för närvarande tillräcklig för att skydda dina bitcoins mot alla stöldförsök. Så länge den digitala signaturalgoritmen inte ändras för att använda större nycklar eller för att förlita sig på ett annat matematiskt problem än ECDLP, är en 24 ords fras fortfarande överflödig. Dessutom ökar en längre fras risken för förlust under säkerhetskopieringen: en säkerhetskopia som är dubbelt så kort är alltid lättare att hantera.


För att gå vidare och lära dig konkret hur du manuellt generate en test Mnemonic fras, rekommenderar jag att du upptäcker den här handledningen:


https://planb.network/tutorials/wallet/backup/generate-mnemonic-phrase-47507d90-e6af-4cac-b01b-01a14d7a8228

Innan vi fortsätter med härledningen av Wallet från denna Mnemonic-fras kommer jag i följande kapitel att presentera BIP39 passphrase för dig, eftersom den spelar en roll i härledningsprocessen och befinner sig på samma nivå som Mnemonic-frasen.


## passphrase


<chapterId>6a51b397-f3b5-5084-b151-cef94bc9b93f</chapterId>


Som vi just har sett genereras HD-plånböcker från en Mnemonic-fras som vanligtvis består av 12 eller 24 ord. Denna fras är mycket viktig eftersom den gör det möjligt att återställa alla nycklar i en Wallet om dess fysiska enhet (som t.ex. en Hardware Wallet) skulle gå förlorad. Den utgör dock en enda felkälla, för om den äventyras kan en angripare stjäla alla bitcoins. Det är här som BIP39 passphrase kommer in i bilden.


### Vad är en BIP39 passphrase?


passphrase är ett valfritt lösenord, som du kan välja fritt, som läggs till Mnemonic-frasen i nyckelhärledningsprocessen för att förbättra Wallet:s säkerhet.


Var försiktig, passphrase ska inte förväxlas med PIN-koden för din Hardware Wallet eller lösenordet som används för att låsa upp åtkomst till din Wallet på din dator. Till skillnad från alla dessa Elements spelar passphrase en roll i härledningen av din Wallet:s nycklar. **Detta innebär att utan den kommer du aldrig att kunna återfå dina bitcoins.**


passphrase fungerar tillsammans med Mnemonic-frasen och modifierar seed från vilken nycklarna genereras. Även om någon får tag på din 12- eller 24-ordsfras kan de alltså inte komma åt dina pengar utan passphrase. Genom att använda en passphrase skapas i princip en ny Wallet med distinkta nycklar. Om passphrase modifieras (även något) blir generate en annan Wallet.


![CYP201](assets/fr/041.webp)


### Varför ska du använda en passphrase?


passphrase är godtycklig och kan vara vilken kombination av tecken som helst som användaren väljer. Att använda en passphrase ger således flera fördelar. För det första minskar alla risker som är förknippade med att Mnemonic-frasen äventyras genom att det krävs en andra faktor för att få tillgång till pengarna (inbrott, tillgång till ditt hem etc.).


Därefter kan den användas strategiskt för att skapa en lockande Wallet, för att möta fysiska begränsningar för att stjäla dina medel som den ökända "_$5 wrench attack_". I det här scenariot är tanken att ha en Wallet utan en passphrase som bara innehåller en liten mängd bitcoins, tillräckligt för att tillfredsställa en potentiell angripare, samtidigt som den har en dold Wallet. Denna senare använder samma Mnemonic-fras men är säkrad med ytterligare en passphrase.

Slutligen är användningen av en passphrase intressant när man vill kontrollera slumpmässigheten i genereringen av seed från HD Wallet.


### Hur väljer man en bra passphrase?


För att passphrase ska vara effektivt måste det vara tillräckligt långt och slumpmässigt. Precis som med ett starkt lösenord rekommenderar jag att du väljer ett passphrase som är så långt och slumpmässigt som möjligt, med en mångfald av bokstäver, siffror och symboler för att omöjliggöra en brute force-attack.


Det är också viktigt att spara denna passphrase på rätt sätt, på samma sätt som Mnemonic frasen. **Att förlora den innebär att du förlorar tillgången till dina bitcoins**. Jag avråder starkt från att bara komma ihåg den utantill, eftersom detta orimligt ökar risken för förlust. Det ideala är att skriva ner det på ett fysiskt medium (papper eller metall) separat från Mnemonic-frasen. Denna säkerhetskopia måste självklart lagras på en annan plats än där din Mnemonic-fras lagras för att förhindra att båda komprometteras samtidigt.


![CYP201](assets/fr/042.webp)


I följande avsnitt kommer vi att upptäcka hur dessa två Elements vid basen av din Wallet - Mnemonic-frasen och passphrase - används för att härleda de nyckelpar som används i _scriptPubKey_ som låser dina UTXO:er.


# Skapande av Bitcoin plånböcker


<partId>9c25e767-7eae-50b8-8c5f-679d8fc83bab</partId>


## Skapande av seed och huvudnyckel


<chapterId>63093760-2010-5691-8d0e-9a04732ae557</chapterId>


När Mnemonic-frasen och den valfria passphrase har genererats kan processen med att härleda en Bitcoin HD Wallet påbörjas. Mnemonic-frasen konverteras först till en seed som utgör basen för alla nycklar i Wallet.


![CYP201](assets/fr/043.webp)


### seed av en HD Wallet


I BIP39-standarden definieras seed som en 512-bitarssekvens, som fungerar som utgångspunkt för härledning av alla nycklar i en HD Wallet. seed härleds från frasen Mnemonic och den möjliga passphrase med hjälp av algoritmen **PBKDF2** (_Password-Based Key Derivation Function 2_) som vi redan har diskuterat i kapitel 3.3. I denna härledningsfunktion kommer vi att använda följande parametrar:



- $m$ : Mnemonic frasen;
- $p$ : en valfri passphrase som väljs av användaren för att förbättra säkerheten för seed. Om det inte finns någon passphrase lämnas detta fält tomt;
- $\text{PBKDF2}$ : härledningsfunktionen med $\text{HMAC-SHA512}$ och $2048$ iterationer;
- $s$: 512-bitars Wallet seed.

Oavsett vilken Mnemonic-fraslängd som väljs (132 bitar eller 264 bitar), kommer PBKDF2-funktionen alltid att producera en 512-bitars utdata, och seed kommer därför alltid att vara av denna storlek.


### seed Derivationsschema med PBKDF2


Följande ekvation illustrerar härledningen av seed från frasen Mnemonic och passphrase:


$$
s = \text{PBKDF2}_{\text{HMAC-SHA512}}(m, p, 2048)
$$


![CYP201](assets/fr/044.webp)


Värdet på seed påverkas således av värdet på frasen Mnemonic och passphrase. Genom att ändra passphrase erhålls en annan seed. Med samma Mnemonic-fras och passphrase genereras dock alltid samma seed, eftersom PBKDF2 är en deterministisk funktion. Detta säkerställer att samma nyckelpar kan hämtas via våra säkerhetskopior.


**Anmärkning:** I vanligt språkbruk hänvisar termen "seed" ofta, genom språkmissbruk, till Mnemonic-frasen. I avsaknad av en passphrase är den ena faktiskt helt enkelt kodningen av den andra. Men som vi har sett, i plånbokens tekniska verklighet, är seed och Mnemonic-frasen faktiskt två distinkta Elements.


Nu när vi har vår seed kan vi fortsätta med härledningen av vår Bitcoin Wallet.


### Huvudnyckeln och huvud chain code


När seed har erhållits innebär nästa steg i att härleda en HD Wallet att beräkna den privata huvudnyckeln och huvud-chain code, som kommer att representera djup 0 i vår Wallet.


För att erhålla den privata huvudnyckeln och huvud-chain code tillämpas HMAC-SHA512-funktionen på seed med hjälp av en fast nyckel "_Bitcoin Seed_" som är identisk för alla Bitcoin-användare. Denna konstant är vald för att säkerställa att nyckelavledningarna är specifika för Bitcoin. Här är Elements:



- $\text{HMAC-SHA512}$: härledningsfunktionen;
- $s$: 512-bitars Wallet seed;
- $\text{"Bitcoin seed"}$: den gemensamma härledningskonstanten för alla Bitcoin plånböcker.


$$

\text{output} = \text{HMAC-SHA512}(\text{"Bitcoin Seed"}, s)


$$


Utdata från denna funktion är därför 512 bitar. Den delas sedan in i 2 delar:



- De återstående 256 bitarna utgör **master private key**;
- De högra 256 bitarna bildar **master chain code**.


Matematiskt kan dessa två värden skrivas på följande sätt, där $k_M$ är den privata huvudnyckeln och $C_M$ är den privata huvudnyckeln chain code:


$$
k_M = \text{HMAC-SHA512}(\text{"Bitcoin Seed"}, s)_{[:256]}
$$


$$
C_M = \text{HMAC-SHA512}(\text{"Bitcoin Seed"}, s)_{[256:]}
$$


![CYP201](assets/fr/045.webp)


### Huvudnyckelns och chain code:s roll


Den privata huvudnyckeln betraktas som den överordnade nyckeln, från vilken alla härledda privata nycklar - barn, barnbarn, barnbarnsbarn etc. - kommer att genereras. Den representerar nollnivån i härledningshierarkin.


Master chain code, å andra sidan, introducerar en ytterligare källa till entropi i processen för att härleda nycklar för barn, för att motverka vissa potentiella attacker. I HD Wallet har dessutom varje nyckelpar en unik chain code associerad med sig, som också används för att härleda barnnycklar från detta par, men vi kommer att diskutera detta mer i detalj i de kommande kapitlen.


Innan jag fortsätter med härledningen av HD Wallet med följande Elements, vill jag i nästa kapitel introducera dig till utökade nycklar, som ofta förväxlas med huvudnyckeln. Vi ska se hur de är uppbyggda och vilken roll de spelar i Bitcoin Wallet.


## Utökade nycklar

<chapterId>8dcffce1-31bd-5e0b-965b-735f5f9e4602</chapterId>


En utökad nyckel är helt enkelt en sammankoppling av en nyckel (privat eller offentlig) och dess tillhörande chain code. Denna chain code är nödvändig för att härleda underordnade nycklar eftersom det utan den är omöjligt att härleda underordnade nycklar från en överordnad nyckel, men vi kommer att beskriva denna process mer ingående i nästa kapitel. Dessa utökade nycklar gör det alltså möjligt att samla all nödvändig information för att härleda underordnade nycklar, vilket förenklar kontohanteringen inom en HD Wallet.


![CYP201](assets/fr/046.webp)


Den utökade nyckeln består av två delar:


- Nyttolasten, som innehåller den privata eller publika nyckeln samt den tillhörande chain code;
- Metadata, som är olika informationsbitar för att underlätta interoperabilitet mellan programvaror och förbättra förståelsen för användaren.


### Så här fungerar utökade nycklar

När den utökade nyckeln innehåller en privat nyckel kallas den för en utökad privat nyckel. Den känns igen på sitt prefix som innehåller identifieraren `prv`. Förutom den privata nyckeln innehåller den utökade privata nyckeln också den associerade chain code. Med denna typ av utökad nyckel är det möjligt att härleda alla typer av underordnade privata nycklar. Genom addition och dubblering av punkter på elliptiska kurvor är det därför också möjligt att härleda underordnade publika nycklar.


När den utökade nyckeln inte innehåller en privat nyckel, utan istället en publik nyckel, kallas den för en utökad publik nyckel. Den känns igen på sitt prefix som innehåller identifieraren "pub". Förutom nyckeln innehåller den naturligtvis också den tillhörande chain code. Till skillnad från den utökade privata nyckeln kan den utökade publika nyckeln endast härleda "normala" publika underordnade nycklar (vilket innebär att den inte kan härleda "härdade" underordnade nycklar). Vi kommer i nästa kapitel att se vad dessa "normala" och "härdade" kvalifikatorer betyder.


I vilket fall som helst tillåter den utökade offentliga nyckeln inte härledning av barns privata nycklar. Även om någon har tillgång till en `xpub` kommer de därför inte att kunna spendera de tillhörande pengarna, eftersom de inte har tillgång till motsvarande privata nycklar. De kan bara härleda underordnade publika nycklar för att observera de tillhörande transaktionerna.


I det följande kommer vi att använda följande notation:


- $K_{\text{PAR}}$: en överordnad publik nyckel;
- $k_{\text{PAR}}$: en överordnad privat nyckel;
- $C_{\text{PAR}}$: en förälder till chain code;
- $C_{\text{CHD}}$: ett barn chain code;
- $K_{\text{CHD}}^n$: en normal publik nyckel för barn;
- $k_{\text{CHD}}^n$: en normal privat nyckel för barn;
- $K_{\text{CHD}}^h$: ett härdat barns publika nyckel;
- $k_{\text{CHD}}^h$: en privat nyckel för ett härdat barn.


![CYP201](assets/fr/047.webp)


### Konstruktion av en utökad nyckel


En utökad nyckel är uppbyggd på följande sätt:


- **Version**: Versionskod för att identifiera nyckelns karaktär (`xprv`, `xpub`, `yprv`, `ypub`...). Vi kommer i slutet av detta kapitel att se vad bokstäverna "x", "y" och "z" motsvarar.
- **Djup**: Hierarkisk nivå i HD Wallet i förhållande till huvudnyckeln (0 för huvudnyckeln).
- **Överordnat fingeravtryck**: De första 4 bytena av HASH160 Hash för den överordnade offentliga nyckel som används för att härleda den nyckel som finns i nyttolasten.
- **Indexnummer**: Identifierar barnet bland syskonnycklar, det vill säga bland alla nycklar på samma härledningsnivå som har samma föräldranycklar.
- **chain code**: En unik 32-byte kod för att härleda barnnycklar.
- **Nyckel**: Den privata nyckeln (med 1 byte som prefix för storlek) eller den offentliga nyckeln.
- **Checksumma**: En kontrollsumma som beräknas med funktionen HASH256 (dubbel SHA256) läggs också till, vilket gör det möjligt att verifiera den utökade nyckelns integritet under överföring eller lagring.


Det fullständiga formatet för en utökad nyckel är därför 78 byte utan kontrollsumma och 82 byte med kontrollsumma. Den konverteras sedan till Base58 för att ge en representation som är lättläst för användarna. Base58-formatet är detsamma som används för *Legacy*-mottagningsadresser (före *SegWit*).


| Element           | Description                                                                                                        | Size      |
| ----------------- | ------------------------------------------------------------------------------------------------------------------ | --------- |
| Version           | Indicates whether the key is public (`xpub`, `ypub`) or private (`xprv`, `zprv`), as well as the version of the extended key | 4 bytes   |
| Depth             | Level in the hierarchy relative to the master key                                                                  | 1 byte    |
| Parent Fingerprint| The first 4 bytes of HASH160 of the parent public key                                                              | 4 bytes   |
| Index Number      | Position of the key in the order of children                                                                       | 4 bytes   |
| Chain Code        | Used to derive child keys                                                                                          | 32 bytes  |
| Key               | The private key (with a 1-byte prefix) or the public key                                                          | 33 bytes  |
| Checksum          | Checksum to verify integrity                                                                                       | 4 bytes   |

Om endast en byte läggs till i den privata nyckeln beror det på att den komprimerade offentliga nyckeln är en byte längre än den privata nyckeln. Denna extra byte, som läggs till i början av den privata nyckeln som `0x00`, utjämnar deras storlek och säkerställer att nyttolasten för den utökade nyckeln har samma längd, oavsett om det är en offentlig eller en privat nyckel.


### Utökade nyckelprefix

Som vi just har sett innehåller utökade nycklar ett prefix som anger både versionen av den utökade nyckeln och dess natur. Notationen "pub" anger att det rör sig om en utökad publik nyckel och notationen "prv" anger en utökad privat nyckel. Den extra bokstaven i början av den utökade nyckeln hjälper till att ange om den standard som följs är Legacy, SegWit v0, SegWit v1, etc.

Här följer en sammanfattning av de prefix som används och deras innebörd:


| Base 58 Prefix  | Base 16 Prefix  | Network | Purpose             | Associated Scripts  | Derivation            | Key Type     |
| --------------- | --------------- | ------- | ------------------- | ------------------- | --------------------- | ------------ |
| `xpub`          | `0488b21e`      | Mainnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/0'`, `m/86'/0'` | public       |
| `xprv`          | `0488ade4`      | Mainnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/0'`, `m/86'/0'` | private      |
| `tpub`          | `043587cf`      | Testnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/1'`, `m/86'/1'` | public       |
| `tprv`          | `04358394`      | Testnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/1'`, `m/86'/1'` | private      |
| `ypub`          | `049d7cb2`      | Mainnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/0'`             | public       |
| `yprv`          | `049d7878`      | Mainnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/0'`             | private      |
| `upub`          | `049d7cb2`      | Testnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/1'`             | public       |
| `uprv`          | `044a4e28`      | Testnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/1'`             | private      |
| `zpub`          | `04b24746`      | Mainnet | SegWit V0           | P2WPKH              | `m/84'/0'`             | public       |
| `zprv`          | `04b2430c`      | Mainnet | SegWit V0           | P2WPKH              | `m/84'/0'`             | private      |
| `vpub`          | `045f1cf6`      | Testnet | SegWit V0           | P2WPKH              | `m/84'/1'`             | public       |
| `vprv`          | `045f18bc`      | Testnet | SegWit V0           | P2WPKH              | `m/84'/1'`             | private      |


### Detaljer om en utökad nyckels Elements


För att bättre förstå den interna strukturen i en utökad nyckel, låt oss ta en som exempel och bryta ner den. Här är en utökad nyckel:



- I Base58:


```text
xpub6CTNzMUkzpurBWaT4HQoYzLP4uBbGJuWY358Rj7rauiw4rMHCyq3Rfy9w4kyJXJzeFfyrKLUar2rUCukSiDQFa7roTwzjiAhyQAdPLEjqHT
```



- I hexadecimal:


```text
0488B21E036D5601AD80000000C605DF9FBD77FD6965BD02B77831EC5C78646AD3ACA14DC3984186F72633A89303772CCB99F4EF346078D167065404EED8A58787DED31BFA479244824DF50658051F067C3A
```


Denna förlängda nyckel bryts ned i flera olika Elements:


1.**Version**: `0488B21E`


De första 4 byte är versionen. Här motsvarar den en utökad publik nyckel på Mainnet med ett härledningssyfte på antingen *Legacy* eller *SegWit v1*.


2.**Djup**: `03`


Detta fält anger den hierarkiska nivån för nyckeln i HD Wallet. I detta fall innebär ett djup på `03` att denna nyckel ligger tre nivåer under huvudnyckeln.


3.**Parent fingeravtryck**: `6D5601AD`


Detta är de första 4 bytena i HASH160 Hash för den överordnade publika nyckel som användes för att härleda denna `xpub`.


4.**Indexnummer**: `80000000`


Detta index anger nyckelns position bland dess förälders barn. Prefixet `0x80` indikerar att nyckeln är härledd på ett härdat sätt, och eftersom resten är fyllt med nollor indikerar det att denna nyckel är den första bland sina möjliga syskon.


5.**chain code**: `C605DF9FBD77FD6965BD02B77831EC5C78646AD3ACA14DC3984186F72633A893`


6.**Öppen nyckel**: `03772CCB99F4EF346078D167065404EED8A58787DED31BFA479244824DF5065805`


7.**Checksumma**: `1F067C3A`


Kontrollsumman motsvarar de första 4 byte av Hash (dubbel SHA256) av allt annat.


I det här kapitlet har vi lärt oss att det finns två olika typer av underordnade nycklar. Vi har också lärt oss att härledningen av dessa underordnade nycklar kräver en nyckel (antingen privat eller offentlig) och dess chain code. I nästa kapitel går vi närmare in på hur dessa olika typer av nycklar ser ut och hur de härleds från sin överordnade nyckel och chain code.



## Härledning av nyckelpar för barn

<chapterId>61c0807c-845b-5076-ad06-7f395b36adfd</chapterId>


Härledningen av barnnyckelpar i Bitcoin HD-plånböcker förlitar sig på en hierarkisk struktur som gör det möjligt att generera ett stort antal nycklar, samtidigt som dessa par organiseras i olika grupper genom grenar. Varje barnpar som härrör från ett föräldrapar kan användas antingen direkt i en *scriptPubKey* för att låsa bitcoins, eller som utgångspunkt för generate fler barnnycklar, och så vidare, för att skapa ett träd av nycklar.


Alla dessa härledningar börjar med huvudnyckeln och huvud-chain code, som är de första föräldrarna på djupnivå 0. De är på sätt och vis Adam och Eva för dina Wallet-nycklar, gemensamma förfäder till alla härledda nycklar.


![CYP201](assets/fr/048.webp)


Låt oss undersöka hur denna deterministiska härledning fungerar.


### De olika typerna av avledningar av barnnycklar


Som vi kort berörde i föregående kapitel är barnnycklar indelade i två huvudtyper.


- **Normala underordnade nycklar** ($k_{\text{CHD}}^n, K_{\text{CHD}}^n$): Dessa härleds från den utökade publika nyckeln ($K_{\text{PAR}}$), eller den utökade privata nyckeln ($k_{\text{PAR}}$), genom att först härleda den publika nyckeln.
- **Härdade underordnade nycklar** ($k_{\text{CHD}}^h, K_{\text{CHD}}^h$): Dessa kan endast härledas från den utökade privata nyckeln ($k_{\text{PAR}}$) och är därför osynliga för observatörer som endast har den utökade publika nyckeln.


Varje underordnat nyckelpar identifieras med ett 32-bitars **index** (som kallas $i$ i våra beräkningar). Indexen för normala nycklar sträcker sig från $0$ till $2^{31}-1$, medan de för härdade nycklar sträcker sig från $2^{31}$ till $2^{32}-1$. Dessa nummer används för att skilja syskonnyckelpar åt under härledningen. Varje föräldranyckelpar måste kunna härleda flera barnnyckelpar. Om vi skulle tillämpa samma beräkning systematiskt från föräldranycklarna skulle alla syskonnycklar som erhålls vara identiska, vilket inte är önskvärt. Indexet introducerar således en variabel som modifierar härledningsberäkningen, vilket gör att varje syskonpar kan differentieras. Med undantag för specifik användning i vissa protokoll och härledningsstandarder börjar vi i allmänhet med att härleda den första underordnade nyckeln med index "0", den andra med index "1" och så vidare.


### Härledningsprocess med HMAC-SHA512


Härledningen av varje underordnad nyckel baseras på HMAC-SHA512-funktionen, som vi diskuterade i avsnitt 2 om Hash-funktioner. Den tar två ingångar: den överordnade chain code $C_{\text{PAR}}$ och sammankopplingen av den överordnade nyckeln (antingen den publika nyckeln $K_{\text{PAR}}$ eller den privata nyckeln $k_{\text{PAR}}$, beroende på vilken typ av underordnad nyckel som önskas) med indexet. Resultatet av HMAC-SHA512 är en 512-bitarssekvens som är uppdelad i två delar:


- De första 32 bytena (eller $h_1$) används för att beräkna det nya barnparet.
- De sista 32 byte (eller $h_2$) fungerar som den nya chain code $C_{\text{CHD}}$ för barnparet.


I alla våra beräkningar kommer jag att beteckna $\text{Hash}$ utdata från HMAC-SHA512-funktionen.


![CYP201](assets/fr/049.webp)


#### Härledning av en underordnad privat nyckel från en överordnad privat nyckel


För att härleda en privat nyckel för barn $k_{\text{CHD}}$ från en privat nyckel för förälder $k_{\text{PAR}}$ är två scenarier möjliga beroende på om en härdad eller normal nyckel önskas.


För en **normal barnnyckel** ($i < 2^{31}$) beräknas $\text{Hash}$ på följande sätt:


$$
\text{hash} = \text{HMAC-SHA512}(C_{\text{PAR}},  k_{\text{PAR}} \cdot G \Vert i)
$$


I den här beräkningen ser vi att vår HMAC-funktion tar två indata: först den överordnade chain code och sedan sammankopplingen av indexet med den offentliga nyckel som är associerad med den överordnade privata nyckeln. Den överordnade offentliga nyckeln används här eftersom vi är ute efter att härleda en normal underordnad nyckel, inte en härdad.

Vi har nu en $\text{Hash}$ på 64 byte som vi ska dela upp i två delar på 32 byte vardera, $h_1$ och $h_2$:



$$

\text{hash} = h_1 \Vert h_2

$$



$$
h_1 = \text{hash}_{[:32]} \quad, \quad h_2 = \text{hash}_{[32:]}
$$


Den privata nyckeln för barnet $k_{\text{CHD}}^n$ beräknas sedan enligt följande:


$$
k_{\text{CHD}}^n = \text{parse256}(h_1) + k_{\text{PAR}} \mod n
$$


I den här beräkningen består operationen $\text{parse256}(h_1)$ av att tolka de första 32 bytena i $\text{Hash}$ som ett 256-bitars heltal. Detta tal läggs sedan till den överordnade privata nyckeln, allt taget modulo $n$ för att hålla sig inom den elliptiska kurvans ordning, som vi såg i avsnitt 3 om digitala signaturer. För att härleda en normal privat nyckel för ett barn, även om den publika nyckeln för föräldern används som beräkningsgrund i ingångarna till HMAC-SHA512-funktionen, är det alltså alltid nödvändigt att ha den privata nyckeln för föräldern för att slutföra beräkningen.


Från barnets privata nyckel kan man härleda motsvarande offentliga nyckel genom att tillämpa ECDSA eller Schnorr. På så sätt får vi ett komplett nyckelpar.


Sedan tolkas den andra delen av $\text{Hash}$ helt enkelt som chain code för det nyckelpar för barn som vi just har härlett:


$$
C_{\text{CHD}} = h_2
$$


Här är en schematisk bild av den övergripande härledningen:


![CYP201](assets/fr/050.webp)


För en **härdad barnnyckel** ($i \geq 2^{31}$) är beräkningen av $\text{Hash}$ följande:



$$
\text{hash} = \text{HMAC-SHA512}(C_{\text{PAR}}, 0x00 \Vert k_{\text{PAR}} \Vert i)
$$


I den här beräkningen ser vi att vår HMAC-funktion tar två ingångar: först den överordnade chain code och sedan sammankopplingen av indexet med den överordnade privata nyckeln. Den överordnade privata nyckeln används här eftersom vi vill härleda en härdad underordnad nyckel. Dessutom läggs en byte som är lika med `0x00` till i början av nyckeln. Denna operation utjämnar dess längd så att den matchar en komprimerad offentlig nyckel.

Så vi har nu en 64-byte $\text{Hash}$ som vi kommer att dela upp i 2 delar på 32 byte vardera, $h_1$ och $h_2$:

$$

\text{hash} = h_1 \Vert h_2

$$



$$
h_1 = \text{hash}[:32] \quad, \quad h_2 = \text{hash}[32:]
$$


Den privata nyckeln för barnet $k_{\text{CHD}}^h$ beräknas sedan enligt följande:


$$
k_{\text{CHD}}^h = \text{parse256}(h_1) + k_{\text{PAR}} \mod n
$$


Därefter tolkar vi helt enkelt den andra delen av $\text{Hash}$ som chain code för det par av underordnade nycklar som vi just har härlett:


$$
C_{\text{CHD}} = h_2
$$


Här är en schematisk bild av den övergripande härledningen:


![CYP201](assets/fr/051.webp)


Vi kan se att normal härledning och härdad härledning fungerar på samma sätt, med denna skillnad: normal härledning använder den överordnade offentliga nyckeln som indata till HMAC-funktionen, medan härdad härledning använder den överordnade privata nyckeln.


#### Härleda en underordnad publik nyckel från en överordnad publik nyckel


Om vi bara känner till den överordnade publika nyckeln $K_{\text{PAR}}$ och den tillhörande chain code $C_{\text{PAR}}$, det vill säga en utökad publik nyckel, är det möjligt att härleda publika barnnycklar $K_{\text{CHD}}^n$, men bara för normala (icke-härdade) barnnycklar. Denna princip gör det särskilt möjligt att övervaka rörelserna för ett konto i en Bitcoin Wallet från `xpub` (*watch-only*).


För att utföra denna beräkning kommer vi att beräkna $\text{Hash}$ med index $i < 2^{31}$ (normal härledning):


$$
\text{hash} = \text{HMAC-SHA512}(C_{\text{PAR}}, K_{\text{PAR}} \Vert i)
$$


I den här beräkningen ser vi att vår HMAC-funktion kräver två ingångar: först den överordnade chain code, sedan sammankopplingen av indexet med den överordnade publika nyckeln.


Så vi har nu en $\text{Hash}$ på 64 byte som vi kommer att dela upp i 2 delar på 32 byte vardera, $h_1$ och $h_2$:



$$

\text{hash} = h_1 \Vert h_2

$$



$$

h_1 = \text{hash}[:32] \quad, \quad h_2 = \text{hash}[32:]

$$


Den publika nyckeln för barnet $K_{\text{CHD}}^n$ beräknas sedan enligt följande:


$$
K_{\text{CHD}}^n = \text{parse256}(h_1) \cdot G + K_{\text{PAR}}
$$


Om $\text{parse256}(h_1) \geq n$ (ordningen på den elliptiska kurvan) eller om $K_{\text{CHD}}^n$ är punkten i oändligheten, är härledningen ogiltig och ett annat index måste väljas.


I den här beräkningen innebär operationen $\text{parse256}(h_1)$ att de första 32 bytena i $\text{Hash}$ tolkas som ett 256-bitars heltal. Detta tal används för att beräkna en punkt på den elliptiska kurvan genom addition och dubblering från generatorpunkten $G$. Denna punkt läggs sedan till den överordnade offentliga nyckeln för att erhålla den normala offentliga barnnyckeln. För att härleda en normal publik nyckel för barn behövs alltså bara den publika nyckeln för förälder och chain code för förälder; den privata nyckeln för förälder kommer aldrig in i denna process, till skillnad från beräkningen av den privata nyckeln för barn som vi såg tidigare.


Därefter är barnet chain code helt enkelt:


$$
C_{\text{CHD}} = h_2
$$


Här är en schematisk bild av den övergripande härledningen:


![CYP201](assets/fr/052.webp)


### Korrespondens mellan barnets offentliga och privata nycklar


En fråga som kan uppstå är hur en normal publik nyckel för barn som härrör från en publik nyckel för förälder kan motsvara en normal privat nyckel för barn som härrör från motsvarande privat nyckel för förälder. Denna länk säkerställs exakt av egenskaperna hos elliptiska kurvor. För att härleda en normal underordnad publik nyckel används HMAC-SHA512 på samma sätt, men dess resultat används på ett annat sätt:


- Normal privat nyckel för barn: $k_{\text{CHD}}^n = \text{parse256}(h_1) + k_{\text{PAR}} \mod n$
- **Normal offentlig nyckel för barn**: $K_{\text{CHD}}^n = \text{parse256}(h_1) \cdot G + K_{\text{PAR}}$


Tack vare additions- och dubblingsoperationerna på den elliptiska kurvan ger båda metoderna konsekventa resultat: den publika nyckel som härleds från barnets privata nyckel är identisk med den publika nyckel som härleds direkt från förälderns publika nyckel.


### Sammanfattning av derivattyper


Här följer en sammanfattning av de olika möjliga typerna av avledningar:


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


Hittills har du lärt dig att skapa den grundläggande Elements för en HD Wallet: Mnemonic-frasen, seed och sedan huvudnyckeln och huvud-chain code. I det här kapitlet har du också lärt dig hur man härleder nyckelpar för barn. I nästa kapitel kommer vi att utforska hur dessa härledningar organiseras i Bitcoin-plånböcker och vilken struktur som ska följas för att konkret erhålla mottagaradresserna samt de nyckelpar som används i *scriptPubKey* och *scriptSig*.


## Wallet Struktur och härledningsvägar

<chapterId>34e1bbda-67de-5493-b268-1fded8d67689</chapterId>


Den hierarkiska strukturen för HD-plånböcker i Bitcoin gör det möjligt att organisera nyckelpar på olika sätt. Tanken är att från den privata huvudnyckeln och huvudnyckeln chain code härleda flera nivåer av djup. Varje tillagd nivå motsvarar härledningen av ett underordnat nyckelpar från ett överordnat nyckelpar.


Med tiden har olika BIP:er infört standarder för dessa härledningsvägar, i syfte att standardisera användningen av dem i olika programvaror. I det här kapitlet ska vi därför ta reda på vad varje härledningsnivå i HD-plånböcker betyder enligt dessa standarder.


### Djupet av härledningen av en HD Wallet


Härledningsvägarna är organiserade i djuplager, från djup 0, som representerar huvudnyckeln och huvud-chain code, till lager med undernivåer för härledning av adresser som används för att låsa UTXO:er. BIP:erna (*Bitcoin Improvement Proposals*) definierar standarderna för varje Layer, vilket bidrar till att harmonisera praxis mellan olika Wallet-hanteringsprogram.


En härledningsväg avser därför den sekvens av index som används för att härleda underordnade nycklar från en huvudnyckel.


**Djup 0: Huvudnyckel (BIP32)**


Detta djup motsvarar Wallet:s privata huvudnyckel och chain code:s huvudnyckel. Det representeras av notationen $m/$.


**Djup 1: Syfte (BIP43)**


Syftet bestämmer den logiska strukturen för härledning. Till exempel kommer en P2WPKH Address att ha $/84'/$ på djup 1 (enligt BIP84), medan en P2TR Address kommer att ha $/86'/$ (enligt BIP86). Denna Layer underlättar kompatibilitet mellan plånböcker genom att ange indexnummer som motsvarar BIP-numren.


Med andra ord, när du väl har huvudnyckeln och huvud-chain code fungerar dessa som ett överordnat nyckelpar för att härleda ett underordnat nyckelpar. Indexet som används i denna härledning kan t.ex. vara $/84'/$ om Wallet är avsedd att använda skript av typen SegWit v0. Detta nyckelpar är då på djup 1. Dess roll är inte att låsa bitcoins, utan helt enkelt att fungera som en vägpunkt i härledningshierarkin.


**Fördjupning 2: Valutatyp (BIP44)**


Från nyckelparet på djup 1 utförs en ny härledning för att erhålla nyckelparet på djup 2. Detta djup gör det möjligt att skilja Bitcoin-konton från andra kryptovalutor inom samma Wallet.


Varje valuta har ett unikt index för att säkerställa kompatibilitet mellan plånböcker med flera valutor. Till exempel, för Bitcoin är indexet $/0'/$ (eller `0x80000000` i hexadecimal notation). Valutaindex väljs i intervallet $2^{31}$ till $2^{32}-1$ för att säkerställa härdad härledning.


För att ge dig andra exempel, här är indexen för några valutor:


- $1'$ (`0x80000001`) för Testnet bitcoins;
- $2'$ (`0x80000002`) för Litecoin;
- $60'$ (`0x8000003c`) för Ethereum...


**Djup 3: Konto (BIP32)**


Varje Wallet kan delas in i flera konton, numrerade från $2^{31}$, och representeras på djup 3 av $/0'/$ för det första kontot, $/1'/$ för det andra, och så vidare. När man hänvisar till en utökad nyckel `xpub`, hänvisar den i allmänhet till nycklar på detta härledningsdjup.


Denna uppdelning i olika konton är frivillig. Den syftar till att förenkla organisationen av Wallet för användarna. I praktiken används ofta bara ett konto, vanligtvis det första som standard. I vissa fall kan det dock vara användbart om man vill skilja tydligt på nyckelpar för olika användningsområden. Det är till exempel möjligt att skapa ett personligt konto och ett professionellt konto från samma seed, med helt olika grupper av nycklar från detta djup av härledning.


**Djup 4: Kedja (BIP32)**


Varje konto som definieras på djupet 3 struktureras sedan i två kedjor:


- **Den externa kedjan**: I denna kedja härleds vad som kallas "offentliga" adresser. Dessa mottagaradresser är avsedda att låsa UTXO:er som kommer från externa transaktioner (det vill säga som härrör från konsumtion av UTXO:er som inte tillhör dig). För att uttrycka det enkelt används denna externa kedja när man vill ta emot bitcoins. När du klickar på "*receive*" i din Wallet-programvara är det alltid en Address från den externa kedjan som erbjuds dig. Denna kedja representeras av ett par nycklar som härleds med indexet $/0/$.
- **Den interna kedjan (förändring)**: Denna kedja är reserverad för att ta emot adresser som låser bitcoins som kommer från konsumtionen av UTXO som tillhör dig, med andra ord ändra adresser. Den identifieras med indexet $/1/$.


**Djup 5: Address Index (BIP32)**


Slutligen representerar djup 5 det sista steget i härledningen i Wallet. Även om det är tekniskt möjligt att fortsätta på obestämd tid, slutar nuvarande standarder här. På detta sista djup härleds de nyckelpar som faktiskt kommer att användas för att låsa och låsa upp UTXO:erna. Varje index gör det möjligt att skilja mellan syskonnyckelpar: sålunda kommer den första mottagande Address att använda index $/0/$, den andra index $/1/$, och så vidare.


![CYP201](assets/fr/053.webp)


### Notation av härledningsvägar


Härledningsvägen skrivs genom att varje nivå separeras med ett snedstreck ($/$). Varje snedstreck anger således en härledning från ett överordnat nyckelpar ($k_{\text{PAR}}$, $K_{\text{PAR}}$, $C_{\text{PAR}}$) till ett underordnat nyckelpar ($k_{\text{CHD}}$, $K_{\text{CHD}}$, $C_{\text{CHD}}$). Det nummer som anges vid varje djup motsvarar det index som används för att härleda denna nyckel från dess föräldrar. Apostrofen ($'$) som ibland placeras till höger om indexet indikerar en härdad härledning ($k_{\text{CHD}}^h$, $K_{\text{CHD}}^h$). Ibland ersätts apostrofen med ett $h$. I avsaknad av apostrof eller $h$ är det därför en normal avledning ($k_{\text{CHD}}^n$, $K_{\text{CHD}}^n$).

Som vi har sett i de tidigare kapitlen börjar index för härdade nycklar från $2^{31}$, eller `0x80000000` i hexadecimal. När ett index följs av en apostrof i en härledningssökväg måste därför $2^{31}$ läggas till det angivna numret för att få fram det faktiska värde som används i HMAC-SHA512-funktionen. Om härledningsvägen t.ex. anger $/44'/$ blir det faktiska indexet följande:

$$

i = 44 + 2^{31} = 2\,147\,483\,692

$$


I hexadecimal är detta "0x8000002C".


Nu när vi har förstått de viktigaste principerna för härledningsvägar, låt oss ta ett exempel! Här är härledningsvägen för en Bitcoin som tar emot Address:



$$

m / 84' / 0' / 1' / 0 / 7

$$


I detta exempel:


- $84'$ anger standarden P2WPKH (SegWit v0);
- $0'$ indikerar Bitcoin-valutan på Mainnet;
- $1'$ motsvarar det andra kontot i Wallet;
- $0$ indikerar att Address befinner sig på den externa kedjan;
- $7$ anger den 8:e externa Address för detta konto.


### Sammanfattning av derivatstrukturen


| Depth | Description        | Standard Example                  |
| ----- | ------------------ | --------------------------------- |
| 0     | Master Key         | $m/$                              |
| 1     | Purpose            | $/86'/$ (P2TR)                    |
| 2     | Currency           | $/0'/$ (Bitcoin)                  |
| 3     | Account            | $/0'/$ (First account)            |
| 4     | Chain              | $/0/$ (external) or $/1/$ (change)|
| 5     | Address Index      | $/0/$ (first address)             |

I nästa kapitel kommer vi att upptäcka vad "*output script descriptors*" är, en nyligen introducerad innovation i Bitcoin Core som förenklar säkerhetskopieringen av en Bitcoin Wallet.


## Skriptbeskrivningar för utdata

<chapterId>e4f1c2d3-9b8a-4d3e-8f2a-7b6c5d4e3f2a</chapterId>

Du får ofta höra att Mnemonic-frasen ensam är tillräcklig för att återställa åtkomst till en Wallet. I verkligheten är saker och ting lite mer komplexa. I det föregående kapitlet tittade vi på härledningsstrukturen för HD Wallet, och du kanske har märkt att den här processen är ganska komplex. Härledningsvägar talar om för programvaran vilken riktning den ska följa för att härleda användarens nycklar. Men när man återställer en Bitcoin Wallet, om man inte känner till dessa vägar, är Mnemonic-frasen ensam inte tillräckligt. Det gör det möjligt att få huvudnyckeln och huvud chain code, men det är då nödvändigt att känna till de index som används för att nå barnnycklarna.


Teoretiskt sett skulle det vara nödvändigt att spara inte bara Mnemonic-frasen för vår Wallet utan även sökvägarna till de konton vi använder. I praktiken är det ofta möjligt att återfå åtkomst till barnnycklarna utan denna information, förutsatt att standarderna har följts. Genom att testa varje standard en efter en är det i allmänhet möjligt att återfå åtkomst till bitcoins. Detta är dock inte garanterat och det är särskilt komplicerat för nybörjare. Med diversifieringen av skripttyper och uppkomsten av mer komplexa konfigurationer kan denna information också bli svår att extrapolera, vilket gör att dessa uppgifter blir privat information och svåra att återställa med brute force. Det är därför som en innovation nyligen har introducerats och börjar integreras i din favoritprogramvara Wallet: *output script descriptors*.


### Vad är en "deskriptor"?


"*output script descriptors*", eller helt enkelt "*descriptors*", är strukturerade uttryck som fullständigt beskriver ett output script (*scriptPubKey*) och ger all nödvändig information för att följa de transaktioner som är associerade med ett visst script. De underlättar hanteringen av nycklar i HD-plånböcker genom att erbjuda en standardiserad och fullständig beskrivning av Wallet-strukturen och de typer av adresser som används.


Den största fördelen med deskriptorer är att de kan kapsla in all viktig information för att återställa en Wallet i en enda sträng (förutom återställningsfrasen). Genom att spara en descriptor med de tillhörande Mnemonic-fraserna blir det möjligt att återställa de privata nycklarna genom att exakt känna till deras position i hierarkin. För Multisig-plånböcker, vars säkerhetskopiering ursprungligen var mer komplex, innehåller deskriptorn `xpub` för varje faktor, vilket säkerställer möjligheten att regenerera adresserna i händelse av problem.


### Konstruktion av en deskriptor


En deskriptor består av flera Elements:


- Skriptfunktioner som `pk` (*Pay-to-PubKey*), `pkh` (*Pay-to-PubKey-Hash*), `wpkh` (*Pay-to-Witness-PubKey-Hash*), `sh` (*Pay-to-Script-Hash*), `wsh` (*Pay-to-Witness-Script-Hash*), `tr` (*Pay-to-Taproot*), `multi` (*Multisignatur*), och `sortedmulti` (*Multisignatur med sorterade nycklar*);
- Härledningsvägar, t.ex. `[d34db33f/44h/0h/0h]` som anger en härledd kontosökväg och ett specifikt fingeravtryck för huvudnyckel;
- Nycklar i olika format, t.ex. hexadecimala publika nycklar eller utökade publika nycklar (xpub);
- En kontrollsumma, föregången av ett Hash-tecken, för att verifiera deskriptorns integritet.


Till exempel kan en deskriptor för en P2WPKH (SegWit v0) Wallet se ut på följande sätt:


```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7nr4
```


I denna deskriptor indikerar härledningsfunktionen `wpkh` en skripttyp *Pay-to-Witness-Public-Key-Hash*. Den följs av en härledningsväg som innehåller:


- `cdeab12f`: huvudnyckelns fingeravtryck;
- `84h`: vilket innebär användning av ett BIP84-ändamål, avsett för SegWit v0-adresser;
- `0h`: vilket indikerar att det är en BTC-valuta på Mainnet;
- `0h`: som hänvisar till det specifika kontonummer som används i Wallet.


Deskriptorn innehåller också den utökade publika nyckel som används i denna Wallet:


```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```


Notation `/<0;1>/*` anger att deskriptorn kan generera adresser från både den externa kedjan (`0`) och den interna kedjan (`1`). Jokertecknet (`*`) i slutet av sökvägen betyder att alla ohärdade (“*unhardened*”) undernycklar kan härledas sekventiellt från denna position, oavsett om de är externa eller interna adresser. Denna syntax innebär inte direkt begreppet *gap limit*, som är en del av en plånboksspecifik mekanism för adressidentifiering, utan används här endast för att ange att alla möjliga härledningar på denna plats beaktas.


Slutligen representerar `#jy0l7nr4` kontrollsumman för att verifiera integriteten hos deskriptorn.


Du vet nu allt om hur HD-plånböcker fungerar i Bitcoin och processen för att härleda nyckelpar. I de senaste kapitlen begränsade vi oss dock till genereringen av privata och offentliga nycklar utan att ta itu med konstruktionen av mottagningsadresser. Just detta kommer att vara ämnet för nästa kapitel!


## Mottagande adresser

<chapterId>ca80a89d-f8da-4e09-8c35-43179b65bced</chapterId>


Mottagningsadresser är informationsbitar inbäddade i *scriptPubKey* för att låsa nyskapade UTXO:er. Enkelt uttryckt tjänar en Address till att ta emot bitcoins. Låt oss utforska deras funktion i samband med vad vi har studerat i de tidigare kapitlen.


### Bitcoin-adressernas roll i skript


Som förklarats tidigare är en transaktions roll att överföra Ownership av bitcoins från inputs till outputs. Denna process innebär att UTXO:er konsumeras som inputs samtidigt som nya UTXO:er skapas som outputs. Dessa UTXO:er säkras av skript, som definierar de nödvändiga villkoren för att låsa upp medlen.


När en användare tar emot bitcoins skapar avsändaren en UTXO och låser den med en *scriptPubKey*. Detta skript innehåller reglerna för att låsa upp UTXO, vanligtvis med angivande av de signaturer och publika nycklar som krävs. För att använda denna UTXO i en ny transaktion måste användaren tillhandahålla den begärda informationen via ett *scriptSig*. Exekveringen av *scriptSig* i kombination med *scriptPubKey* måste ge resultatet 'true' eller '1'. Om detta villkor är uppfyllt kan UTXO användas för att skapa en ny UTXO, som i sin tur låses med en ny *scriptPubKey*, och så vidare.


![CYP201](assets/fr/054.webp)


Det är just i *scriptPubKey* som mottagaradresserna finns. Användningen av dessa varierar dock beroende på vilken skriptstandard som används. Här följer en sammanfattande tabell över den information som finns i *scriptPubKey* enligt den standard som används, samt den information som förväntas i *scriptSig* för att låsa upp *scriptPubKey*.


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

*Källa: Bitcoin Core PR review club, 7 juli 2021 - Gloria Zhao*


De opkoder som används i ett skript är utformade för att manipulera information och, vid behov, jämföra eller testa den. Låt oss ta ett exempel på ett P2PKH-skript, som ser ut enligt följande:


```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG
```


Som vi kommer att se i detta kapitel representerar `<pubKeyHash>` faktiskt nyttolasten i den mottagande Address som används för att låsa UTXO. För att låsa upp denna *scriptPubKey* är det nödvändigt att tillhandahålla en *scriptSig* som innehåller:


```text
<signature> <public key>
```


I skriptspråk är stacken en *LIFO* ("*Last In, First Out*") datastruktur som används för att tillfälligt lagra Elements under skriptexekveringen. Varje skriptoperation manipulerar denna stack, där Elements kan läggas till (*push*) eller tas bort (*pop*). Skript använder stacken för att utvärdera uttryck, lagra temporära variabler och hantera villkor.


Exekveringen av det skript som jag just gav som exempel följer denna process:



- Vi har *scriptSig*, *scriptPubKey* och stacken:


![CYP201](assets/fr/055.webp)



- *scriptSig* läggs på stacken:


![CYP201](assets/fr/056.webp)



- `OP_DUP` duplicerar den offentliga nyckel som anges i *scriptSig* på stacken:


![CYP201](assets/fr/057.webp)



- `OP_HASH160` returnerar Hash för den offentliga nyckel som just duplicerades:


![CYP201](assets/fr/058.webp)



- `OP_PUSHBYTES_20 <pubKeyHash>` lägger Bitcoin Address som ingår i *scriptPubKey* på stacken:


![CYP201](assets/fr/059.webp)



- `OP_EQUALVERIFY` verifierar att den hashade offentliga nyckeln matchar den tillhandahållna mottagande Address:


![CYP201](assets/fr/060.webp)


`OP_CHECKSIG` kontrollerar signaturen som finns i *scriptSig* med hjälp av den offentliga nyckeln. Denna opcode utför i huvudsak en signaturverifiering som vi beskrev i del 3 av denna utbildning:



![CYP201](assets/fr/061.webp)



- Om `1` ligger kvar på stacken är skriptet giltigt:


![CYP201](assets/fr/062.webp)


Sammanfattningsvis gör detta skript det därför möjligt att med hjälp av den digitala signaturen verifiera att den användare som gör anspråk på Ownership av denna UTXO och vill spendera den verkligen har den privata nyckel som är associerad med den mottagande Address som användes vid skapandet av denna UTXO.


### De olika typerna av Bitcoin-adresser


Under utvecklingen av Bitcoin har flera standardskriptmodeller lagts till. Var och en av dem använder en distinkt typ av mottagande Address. Här är en översikt över de viktigaste skriptmodellerna som finns tillgängliga hittills:


**P2PK (*Pay-to-PubKey*)**:


Denna skriptmodell introducerades i den första versionen av Bitcoin av Satoshi Nakamoto. P2PK-skriptet låser bitcoins direkt med en rå offentlig nyckel (således används ingen mottagande Address med den här modellen). Dess struktur är enkel: den innehåller en offentlig nyckel och kräver en motsvarande digital signatur för att låsa upp pengarna. Detta skript är en del av "*Legacy*"-standarden.


**P2PKH (*Pay-to-PubKey-Hash*)**:


Precis som P2PK introducerades P2PKH-skriptet vid lanseringen av Bitcoin. Till skillnad från sin föregångare låser det bitcoins med hjälp av Hash för den offentliga nyckeln, snarare än att direkt använda den råa offentliga nyckeln. *scriptSig* måste då tillhandahålla den publika nyckel som är associerad med den mottagande Address, samt en giltig signatur. Adresserna som motsvarar denna modell börjar med `1` och är kodade i *base58check*. Detta skript tillhör också standarden "*Legacy*".


**P2SH (*Pay-to-Script-Hash*)**:


P2SH-modellen, som introducerades 2012 med BIP16, gör det möjligt att använda Hash för ett godtyckligt skript i *scriptPubKey*. Detta hashade skript, kallat "*redeemscript*", innehåller villkoren för att låsa upp medlen. För att använda en UTXO som är låst med P2SH måste man tillhandahålla ett *scriptSig* som innehåller den ursprungliga *redeemscript* samt de uppgifter som krävs för att validera den. Denna modell används framför allt för gamla multisigs. Adresserna associerade med P2SH börjar med `3` och är kodade i *base58check*. Detta skript tillhör också "*Legacy*"-standarden.


**P2WPKH (*Pay-to-Witness-PubKey-Hash*)**:


Det här skriptet liknar P2PKH, eftersom det också låser bitcoins med hjälp av Hash för en offentlig nyckel. Till skillnad från P2PKH flyttas dock *scriptSig* till ett separat avsnitt som heter "*Witness*". Detta kallas ibland för "*scriptWitness*" för att beteckna den uppsättning som består av signaturen och den offentliga nyckeln. Varje SegWit-ingång har sitt eget *scriptWitness*, och samlingen av *scriptWitnesses* utgör transaktionens *Witness*-fält. Denna förflyttning av signaturdata är en innovation som infördes genom SegWit-uppdateringen och som särskilt syftar till att förhindra att transaktioner kan manipuleras på grund av ECDSA-signaturer.

P2WPKH-adresser använder *bech32*-kodning och börjar alltid med `bc1q`. Denna typ av skript motsvarar version 0 SegWit-utgångar.


**P2WSH (*Pay-to-Witness-Script-Hash*)**:


P2WSH-modellen introducerades också med SegWit-uppdateringen i augusti 2017. I likhet med P2SH-modellen låser den bitcoins med hjälp av Hash i ett skript. Huvudskillnaden ligger i hur signaturer och skript införlivas i transaktionen. För att spendera bitcoins som är låsta med den här typen av skript måste mottagaren tillhandahålla det ursprungliga skriptet, kallat *witnessScript* (motsvarande *redeemscript* i P2SH), tillsammans med nödvändiga data för att validera detta *witnessScript*. Denna mekanism gör det möjligt att implementera mer komplexa utgiftsvillkor, t.ex. multisigs.


P2WSH-adresser använder *bech32*-kodning och börjar alltid med `bc1q`. Detta skript motsvarar också version 0 SegWit-utgångar.


**P2TR (*Pay-to-Taproot*)**:


Modellen P2TR introducerades i samband med implementeringen av Taproot i november 2021. Den baseras på Schnorr-protokollet för kryptografisk nyckelaggregering samt på en Merkle Tree för alternativa skript, kallad MAST (*Merkelized Alternative Script Tree*). Till skillnad från andra typer av skript, där utgiftsvillkoren är offentligt exponerade (antingen vid mottagandet eller vid utgifterna), gör P2TR det möjligt att dölja komplexa skript bakom en enda, uppenbar offentlig nyckel.


Tekniskt sett låser ett P2TR-skript bitcoins på en unik Schnorr-offentlig nyckel, betecknad som $Q$. Denna nyckel $Q$ är faktiskt ett aggregat av en offentlig nyckel $P$ och en offentlig nyckel $M$, den senare beräknas från Merkle Root av en lista med *scriptPubKey*. Bitcoins som är låsta med den här typen av skript kan användas på två sätt:


- Genom att publicera en signatur för den publika nyckeln $P$ (*nyckelsökväg*).
- Genom att uppfylla ett av de skript som ingår i Merkle Tree (*skriptväg*).


P2TR erbjuder således stor flexibilitet, eftersom det gör det möjligt att låsa bitcoins antingen med en unik publik nyckel, med flera valfria skript eller båda samtidigt. Fördelen med denna Merkle Tree-struktur är att endast det utgiftsskript som används avslöjas under transaktionen, men alla andra alternativa skript förblir hemliga.


![CYP201](assets/fr/063.webp)


P2TR motsvarar SegWit-utgångar i version 1, vilket innebär att signaturerna för P2TR-ingångar lagras i transaktionens *Witness*-avsnitt och inte i *scriptSig*. P2TR-adresser använder kodningen *bech32m* och börjar med `bc1p`, men de är ganska unika eftersom de inte använder en Hash-funktion för sin konstruktion. I själva verket representerar de direkt den publika nyckeln $Q$ som helt enkelt är formaterad med metadata. Det är därför en skriptmodell som ligger nära P2PK.


Nu när vi har gått igenom teorin kan vi gå vidare till praktiken! I följande kapitel föreslår jag att man härleder både en SegWit v0 Address och en SegWit v1 Address från ett par nycklar.


## Address härledning

<chapterId>3ebdc750-4135-4881-b07e-08965941b93e</chapterId>


Låt oss tillsammans utforska hur man kan generate en mottagande Address från ett nyckelpar som till exempel finns på djup 5 i en HD Wallet. Denna Address kan sedan användas i en Wallet-programvara för att låsa en UTXO.


Eftersom processen för att generera en Address beror på vilken skriptmodell som används ska vi fokusera på två specifika fall: att generera en SegWit v0 Address i P2WPKH och en SegWit v1 Address i P2TR. Dessa två typer av adresser täcker de allra flesta användningsområden idag.


### Komprimering av publik nyckel


Efter att ha utfört alla härledningssteg från huvudnyckeln till djup 5 med hjälp av lämpliga index, får vi ett nyckelpar ($k$, $K$) med $K = k \cdot G$. Även om det är möjligt att använda denna publika nyckel som den är för att låsa medel med P2PK-standarden, är det inte vårt mål här. Istället strävar vi efter att skapa en Address i P2WPKH i första hand, och sedan i P2TR för ett annat exempel.


Det första steget är att komprimera den offentliga nyckeln $K$. För att förstå denna process väl, låt oss först komma ihåg några grundläggande saker som behandlas i del 3.

En publik nyckel i Bitcoin är en punkt $K$ som ligger på en elliptisk kurva. Den representeras i formen $(x, y)$, där $x$ och $y$ är koordinaterna för punkten. I okomprimerad form mäter denna publika nyckel 520 bitar: 8 bitar för ett prefix (initialvärde `0x04`), 256 bitar för $x$-koordinaten och 256 bitar för $y$-koordinaten.

Elliptiska kurvor har dock en symmetriegenskap i förhållande till x-axeln: för en given $x$-koordinat finns det bara två möjliga värden för $y$: $y$ och $-y$. Dessa två punkter ligger på var sin sida om x-axeln. Med andra ord, om vi känner till $x$ räcker det att ange om $y$ är jämn eller udda för att identifiera den exakta punkten på kurvan.


![CYP201](assets/fr/064.webp)


För att komprimera en publik nyckel kodas endast $x$, som upptar 256 bitar, och ett prefix läggs till för att ange pariteten för $y$. Den här metoden minskar storleken på den publika nyckeln till 264 bitar istället för de ursprungliga 520. Prefixet `0x02` anger att $y$ är jämnt och prefixet `0x03` anger att $y$ är udda.


Låt oss ta ett exempel för att förstå väl, med en rå offentlig nyckel i okomprimerad representation:


```text
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```


Om vi bryter ner den här nyckeln har vi..:


   - Prefixet: `04`;
   - $x$: `678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6`;
   - $y$: `49f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f`


Det sista hexadecimala tecknet i $y$ är `f`. I bas 10 är `f = 15`, vilket motsvarar ett udda tal. Därför är $y$ udda och prefixet kommer att vara `0x03` för att ange detta.


Den komprimerade offentliga nyckeln blir:


```text
K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6
```

Denna operation gäller för alla skriptmodeller som baseras på ECDSA, det vill säga alla utom P2TR som använder Schnorr. När det gäller Schnorr, som förklaras i del 3, behåller vi bara värdet på $x$ utan att lägga till ett prefix för att ange pariteten på $y$, till skillnad från ECDSA. Detta möjliggörs genom att en unik paritet väljs godtyckligt för alla nycklar. Detta möjliggör en liten minskning av det lagringsutrymme som krävs för publika nycklar.

### Härledning av en SegWit v0 (bech32) Address


Nu när vi har fått vår komprimerade offentliga nyckel kan vi härleda en SegWit v0 som tar emot Address från den.


Det första steget är att tillämpa Hash-funktionen HASH160 på den komprimerade offentliga nyckeln. HASH160 är en sammansättning av två successiva Hash-funktioner: SHA256, följt av RIPEMD160:



$$

\text{HASH160}(K) = \text{RIPEMD160}(\text{SHA256}(K))

$$


Först skickar vi nyckeln genom SHA256:


```text
SHA256(K) = C489EBD66E4103B3C4B5EAFF462B92F5847CA2DCE0825F4997C7CF57DF35BF3A
```


Sedan skickar vi resultatet genom RIPEMD160:


```text
RIPEMD160(SHA256(K)) = 9F81322CC88622CA4CCB2A52A21E2888727AA535
```


Vi har fått en 160-bitars Hash av den offentliga nyckeln, som utgör det som kallas nyttolasten i Address. Denna nyttolast representerar den centrala och viktigaste delen av Address. Den används också i *scriptPubKey* för att låsa UTXO:erna.


För att göra denna nyttolast mer lättanvänd för människor läggs dock metadata till den. Nästa steg innebär att denna Hash kodas i grupper om 5 bitar i decimal. Denna decimala omvandling kommer att vara användbar för konvertering till *bech32*, som används av post-SegWit-adresser. Den 160-bitars binära Hash delas alltså in i 32 grupper om 5 bitar:



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

Så, det har vi:


```text
HASH = 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21
```


När Hash har kodats i grupper om 5 bitar läggs en kontrollsumma till i Address. Denna kontrollsumma används för att verifiera att nyttolasten i Address inte har ändrats under lagring eller överföring. Det gör det t.ex. möjligt för en Wallet-programvara att säkerställa att du inte har gjort ett skrivfel när du anger en mottagande Address. Utan denna verifiering kan du av misstag skicka bitcoins till en felaktig Address, vilket resulterar i en permanent förlust av medel, eftersom du inte äger den tillhörande offentliga eller privata nyckeln. Därför är kontrollsumman ett skydd mot mänskliga fel.


För de gamla Bitcoin *Legacy*-adresserna beräknades checksumman helt enkelt från början av Address Hash med funktionen HASH256. I och med introduktionen av SegWit och formatet *bech32* används nu BCH-koder (*Bose, Ray-Chaudhuri och Hocquenghem*). Dessa felkorrigerande koder används för att upptäcka och korrigera fel i datasekvenser. De säkerställer att den överförda informationen kommer fram intakt till sin destination, även vid mindre förändringar. BCH-koder används inom många områden, t.ex. SSD-enheter, DVD-skivor och QR-koder. Tack vare dessa BCH-koder kan t.ex. en delvis skymd QR-kod fortfarande läsas och avkodas.


I samband med Bitcoin erbjuder BCH-koder en bättre kompromiss mellan storlek och feldetekteringsförmåga jämfört med de enkla Hash-funktioner som används för *Legacy*-adresser. I Bitcoin används dock BCH-koder endast för feldetektering, inte för korrigering. Således kommer Wallet-programvaran att signalera en felaktigt mottagande Address men kommer inte att korrigera den automatiskt. Denna begränsning är avsiktlig: att tillåta automatisk korrigering skulle minska feldetekteringskapaciteten.


För att beräkna kontrollsumman med BCH-koder måste vi förbereda flera Elements.


- HRP (**Human Readable Part**): För Bitcoin Mainnet är HRP `bc`;


HRP måste utvidgas genom att varje karaktär delas upp i två delar:


- Tar fram HRP:s tecken i ASCII:
 - `b`: `01100010`
 - `c`: `01100011`
- Extrahering av de 3 mest signifikanta bitarna och de 5 minst signifikanta bitarna:
  - 3 mest signifikanta bitar: `011` (3 i decimal)
  - 3 mest signifikanta bitar: `011` (3 i decimal)
  - 5 minst signifikanta bitar: `00010` (2 i decimal)
  - 5 minst signifikanta bitar: `00011` (3 i decimal)


Med separatorn `0` mellan de två tecknen är HRP-tillägget därför:


```text
03 03 00 02 03
```



- **Vittnets version**: För SegWit version 0, är det "00";



- **Nyttolasten**: Decimalvärdena för den publika nyckeln Hash;



- **Reservationen för kontrollsumman**: Vi lägger till 6 nollor `[0, 0, 0, 0, 0, 0, 0]` i slutet av sekvensen.


Alla kombinerade data som ska matas in i programmet för att beräkna kontrollsumman är följande:


```text
HRP = 03 03 00 02 03
SEGWIT v0 = 00
HASH = 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21
CHECKSUM = 00 00 00 00 00 00

INPUT = 03 03 00 02 03 00 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21 00 00 00 00 00 00
```


Beräkningen av kontrollsumman är ganska komplex. Den involverar polynomial finit fältaritmetik. Vi kommer inte att beskriva denna beräkning i detalj här utan går direkt till resultatet. I vårt exempel är kontrollsumman som erhålls i decimal:


```text
10 16 11 04 13 18
```


Vi kan nu konstruera den mottagande Address genom att i tur och ordning sammankoppla följande Elements:


- **SegWit version**: `00`
- **Nyttolasten**: Den publika nyckeln Hash
- **Kontrollsumman**: De värden som erhölls i föregående steg (`10 16 11 04 13 18`)


Detta ger oss i decimal:


```text
00 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21 10 16 11 04 13 18
```


Därefter måste varje decimalvärde mappas till sitt *bech32*-tecken med hjälp av följande konverteringstabell:



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


Om du vill konvertera ett värde till ett _bech32_-tecken med hjälp av den här tabellen letar du bara upp de värden i den första kolumnen och den första raden som tillsammans ger det önskade resultatet. Hämta sedan motsvarande tecken. Till exempel kommer decimaltalet `19` att konverteras till bokstaven `n`, eftersom $19 = 16 + 3$.


Genom att kartlägga alla våra värderingar får vi fram följande Address:


```
qn7qnytxgsc3v5nxt9ff2y83g3pe84ff42stydj
```


Det enda som återstår är att lägga till HRP `bc`, som anger att det är en Address för Bitcoin Mainnet, samt separatorn `1`, för att få den kompletta mottagande Address:


```
bc1qn7qnytxgsc3v5nxt9ff2y83g3pe84ff42stydj
```


Det speciella med detta _bech32_-alfabet är att det innehåller alla alfanumeriska tecken utom `1`, `b`, `i` och `o` för att undvika visuell förväxling mellan liknande tecken, särskilt när de skrivs in eller läses av människor.


För att sammanfatta, här är härledningsprocessen:


![CYP201](assets/fr/065.webp)


Så här härleder man en P2WPKH (SegWit v0) som tar emot Address från ett nyckelpar. Låt oss nu gå vidare till P2TR (SegWit v1 / Taproot) adresser och upptäcka deras generationsprocess.


### Härledning av en SegWit v1 (bech32m) Address


För Taproot-adresser skiljer sig genereringsprocessen något. Låt oss titta på detta tillsammans!


När det gäller komprimering av offentliga nycklar finns det en första skillnad jämfört med ECDSA: de offentliga nycklar som används för Schnorr i Bitcoin representeras endast av sin abscissa ($x$). Därför finns det inget prefix, och den komprimerade nyckeln mäter exakt 256 bitar.

Som vi såg i föregående kapitel låser ett P2TR-skript bitcoins på en unik Schnorr-offentlig nyckel, betecknad med $Q$. Denna nyckel $Q$ är ett aggregat av två offentliga nycklar: $P$, en intern offentlig nyckel, och $M$, en offentlig nyckel som härrör från Merkle Root i en lista över _scriptPubKey_. De bitcoins som är låsta med den här typen av skript kan användas på två sätt:



- Genom att publicera en signatur för den publika nyckeln $P$ (_key path_);
- Genom att följa ett av de skript som ingår i Merkle Tree (_skriptsökväg_).


I verkligheten är dessa två nycklar inte riktigt "aggregerade" Nyckeln $P$ är istället tweakad av nyckeln $M$. Att "tweaka" en publik nyckel innebär inom kryptografi att man modifierar denna nyckel genom att tillämpa ett additivt värde som kallas "tweak" Denna operation gör att den modifierade nyckeln förblir kompatibel med den ursprungliga privata nyckeln och tweaken. Tekniskt sett är en tweak ett skalärt värde $t$ som läggs till den ursprungliga publika nyckeln. Om $P$ är den ursprungliga publika nyckeln blir den tweakade nyckeln:



$$

P' = P + t \cdot G

$$


Där $G$ är generatorn för den elliptiska kurva som används. Denna operation producerar en ny publik nyckel som härrör från den ursprungliga nyckeln, samtidigt som den behåller kryptografiska egenskaper som gör det möjligt att använda den.


Om du inte behöver lägga till alternativa skript (spendera uteslutande via _key path_) kan du generate en Taproot Address som enbart är etablerad på den offentliga nyckel som finns på djup 5 i din Wallet. I detta fall är det nödvändigt att skapa ett script som inte kan spenderas för _script path_, för att uppfylla kraven i strukturen. Tweak $t$ beräknas sedan genom att tillämpa en taggad Hash-funktion, **`TapTweak`**, på den interna publika nyckeln $P$:



$$

t = \text{H}_{\text{TapTweak}}(P)

$$


var:



- $\text{H}_{\text{TapTweak}}$ **är en SHA256 Hash-funktion taggad med taggen `TapTweak`. Om du inte är bekant med vad en taggad Hash-funktion är, uppmanar jag dig att läsa kapitel 3.3;**
- $P$ är den interna offentliga nyckeln, representerad i sitt komprimerade 256-bitarsformat, med endast $x$-koordinaten.


Taproot:s publika nyckel $Q$ beräknas sedan genom att addera tweaken $t$, multiplicerad med den elliptiska kurvgeneratorn $G$, till den interna publika nyckeln $P$:



$$

Q = P + t \cdot G

$$


När den publika nyckeln Taproot $Q$ har erhållits kan vi generate motsvarande mottagande Address. Till skillnad från andra format upprättas inte Taproot-adresser på en Hash av den publika nyckeln. Därför sätts nyckeln $Q$ in direkt i Address, på ett obearbetat sätt.


Till att börja med extraherar vi $x$-koordinaten för punkten $Q$ för att få en komprimerad offentlig nyckel. På denna nyttolast beräknas en kontrollsumma med hjälp av BCH-koder, som med SegWit v0-adresser. Programmet som används för Taproot-adresser skiljer sig dock något. Efter införandet av _bech32_-formatet med SegWit upptäcktes en bugg: när det sista tecknet i en Address är ett "p" blir inte kontrollsumman ogiltig om man infogar eller tar bort "q" precis före detta "p". Även om denna bugg inte har några konsekvenser för SegWit v0 (tack vare en storleksbegränsning), kan den utgöra ett problem i framtiden. Denna bugg har därför korrigerats för Taproot-adresser, och det nya korrigerade formatet kallas "_bech32m_".


Taproot Address genereras genom att $x$-koordinaten för $Q$ kodas i formatet _bech32m_, med följande Elements:



- **HRP (_Human Readable Part_)**: `bc`, för att ange huvudnätverket Bitcoin;
- **Version**: `1` för att indikera Taproot / SegWit v1;
- **Kontrollsumman**.


Den slutliga Address kommer därför att ha formatet:


```
bc1p[Qx][checksum]
```


Om du å andra sidan vill lägga till alternativa skript utöver att spendera med den interna publika nyckeln (_script path_), kommer beräkningen av den mottagande Address att bli något annorlunda. Du måste inkludera Hash för de alternativa skripten i beräkningen av tweaken. I Taproot kallas varje alternativt skript, som ligger i slutet av Merkle Tree, för ett "blad".


När de olika alternativa skripten är skrivna måste du skicka dem individuellt genom en taggad Hash-funktion `TapLeaf`, tillsammans med vissa metadata:



$$

\text{h}_{\text{leaf}} = \text{H}_{\text{TapLeaf}} (v \Vert sz \Vert S)

$$


Med:



- $v$: skriptets versionsnummer (standard `0xC0` för Taproot);
- $sz$: storleken på skriptet kodat i formatet _CompactSize_;
- $S$: skriptet.


De olika skripthasharna ($\text{h}_{\text{leaf}}$) sorteras först i lexikografisk ordning. Sedan sammanfogas de i par och skickas genom en taggad Hash-funktion `TapBranch`. Denna process upprepas iterativt för att steg för steg bygga upp Merkle Tree:

$$

\text{h}_{\text{branch}} = \text{H}_{\text{TapBranch}}(\text{h}_{\text{leaf1}} \Vert \text{h}_{\text{leaf2}})

$$


Vi fortsätter sedan med att sammanfoga resultaten två och två, och skickar dem i varje steg genom den taggade Hash-funktionen `TapBranch`, tills vi får Merkle Tree-roten:


![CYP201](assets/fr/066.webp)


När Merkle Root $h_{\text{root}}$ har beräknats kan vi beräkna tweaken. För detta sammankopplar vi den interna publika nyckeln för Wallet $P$ med roten $h_{\text{root}}$ och skickar sedan hela genom den taggade Hash-funktionen `TapTweak`:



$$

t = \text{H}_{\text{TapTweak}}(P \Vert h_{\text{root}})

$$


Slutligen, som tidigare, erhålls Taproot:s offentliga nyckel $Q$ genom att lägga till den interna offentliga nyckeln $P$ till produkten av tweak $t$ med generatorpunkten $G$:



$$

Q = P + t \cdot G

$$

Sedan följer genereringen av Address samma process, med den råa publika nyckeln $Q$ som nyttolast, tillsammans med ytterligare metadata.


Och där har du det! Vi har nått slutet av denna CYP201-kurs. Om du tyckte att den här kursen var till hjälp skulle jag vara mycket tacksam om du kunde ta en stund och ge den ett gott betyg i följande utvärderingskapitel. Du får också gärna dela den med dina nära och kära eller på dina sociala nätverk. Slutligen, om du vill få ditt diplom för den här kursen kan du göra slutprovet direkt efter utvärderingskapitlet.

# Sista avsnittet

<partId>58111408-b734-54db-9ea7-0d5b67f99f99</partId>


## Recensioner & betyg

<chapterId>0cd71541-a7fd-53db-b66a-8611b6a28b04</chapterId>

<isCourseReview>true</isCourseReview>

## Slutlig tentamen

<chapterId>a53ea27d-0f84-56cd-b37c-a66210a4b31d</chapterId>

<isCourseExam>true</isCourseExam>

## Slutsats

<chapterId>d291428b-3cfa-5394-930e-4b514be82d5a</chapterId>

<isCourseConclusion>true</isCourseConclusion>