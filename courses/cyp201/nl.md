---
name: De innerlijke werking van Bitcoin portemonnees
goal: Duik in de cryptografische principes die Bitcoin wallets aansturen.
objectives: 

  - De theoretische begrippen definiëren die nodig zijn voor het begrijpen van de cryptografische algoritmen die in Bitcoin gebruikt worden.
  - De constructie van een deterministische en hiërarchische Wallet volledig begrijpen.
  - Weten hoe je de risico's die gepaard gaan met het beheren van een Wallet kunt identificeren en verminderen.
  - De principes van Hash functies, cryptografische sleutels en digitale handtekeningen begrijpen.

---

# Een reis naar het hart van Bitcoin portemonnees


Ontdek de geheimen van deterministische en hiërarchische Bitcoin wallets met onze CYP201 cursus! Of je nu een regelmatige gebruiker bent of een enthousiasteling die zijn kennis wil verdiepen, deze cursus biedt een complete onderdompeling in de werking van deze tools die we allemaal dagelijks gebruiken.


Leer meer over de mechanismen van Hash functies, digitale handtekeningen (ECDSA en Schnorr), Mnemonic zinnen, cryptografische sleutels en het aanmaken van ontvangstadressen, terwijl je geavanceerde beveiligingsstrategieën verkent.


Deze training zal je niet alleen uitrusten met de kennis om de structuur van een Bitcoin Wallet te begrijpen, maar zal je ook voorbereiden om dieper in de spannende wereld van cryptografie te duiken.


Met een duidelijke pedagogie, meer dan 60 verklarende diagrammen en concrete voorbeelden, zal CYP201 je in staat stellen om van A tot Z te begrijpen hoe je Wallet werkt, zodat je met vertrouwen door het Bitcoin universum kunt navigeren. Neem vandaag nog de controle over je UTXO's door te begrijpen hoe HD wallets werken!


+++

# Inleiding


<partId>32960669-d13a-592f-a053-37f70b997cbf</partId>


## Cursus Introductie


<chapterId>fb4e8857-ea35-5a8a-ae8a-5300234e0104</chapterId>


Welkom bij de CYP201 cursus, waarin we dieper ingaan op de werking van HD Bitcoin wallets. Deze cursus is bedoeld voor iedereen die de technische basisbeginselen van het gebruik van Bitcoin wil begrijpen, of het nu gaat om gelegenheidsgebruikers, verlichte enthousiastelingen of toekomstige experts.


Het doel van deze training is om je de sleutels te geven om de tools die je dagelijks gebruikt onder de knie te krijgen. HD Bitcoin wallets, die het hart vormen van jouw gebruikerservaring, zijn gebaseerd op soms complexe concepten die we toegankelijk proberen te maken. Samen zullen we ze demystificeren!


Voordat we in de details duiken van de constructie en werking van Bitcoin wallets, beginnen we met een paar hoofdstukken over de cryptografische primitieven die we moeten kennen voor wat volgt.

We zullen beginnen met cryptografische Hash functies, fundamenteel voor zowel wallets als het Bitcoin protocol zelf. Je zult hun belangrijkste kenmerken ontdekken, de specifieke functies die gebruikt worden in Bitcoin, en in een meer technisch hoofdstuk zul je in detail leren over de werking van de koningin van de Hash functies: SHA256.


![CYP201](assets/fr/010.webp)


Vervolgens bespreken we de werking van algoritmen voor digitale handtekeningen die je elke dag gebruikt om je UTXO's te beveiligen. Bitcoin gebruikt er twee: ECDSA en het Schnorr protocol. Je leert welke wiskundige primitieven ten grondslag liggen aan deze algoritmen en hoe ze de veiligheid van transacties garanderen.


![CYP201](assets/fr/021.webp)


Als we eenmaal een goed begrip hebben van deze Elements van cryptografie, gaan we eindelijk verder met het hart van de training: deterministische en hiërarchische wallets! Eerst is er een sectie gewijd aan Mnemonic zinnen, deze reeksen van 12 of 24 woorden waarmee je je wallets kunt maken en herstellen. Je zult ontdekken hoe deze woorden worden gegenereerd uit een bron van entropie en hoe ze het gebruik van Bitcoin vergemakkelijken.


![CYP201](assets/fr/040.webp)


De training gaat verder met de studie van de BIP39 passphrase, de seed (niet te verwarren met de Mnemonic frase), de master chain code en de master key. We zullen in detail zien wat deze Elements zijn, hun respectievelijke rollen en hoe ze berekend worden.


![CYP201](assets/fr/045.webp)


Tenslotte zullen we vanuit de hoofdsleutel ontdekken hoe cryptografische sleutelparen op een deterministische en hiërarchische manier worden afgeleid tot aan de ontvangende adressen.


![CYP201](assets/fr/056.webp)


Deze training stelt je in staat om de Wallet software met vertrouwen te gebruiken, terwijl je vaardigheden om risico's te identificeren en te beperken worden verbeterd. Bereid u voor om een echte expert in Bitcoin wallets te worden!


Deze tabel biedt u een vertaling van de belangrijkste gebruikte Engelse termen, om u te helpen de schema’s en technische documenten die in de cursus CYP 201 worden gebruikt beter te begrijpen.

| Engels          | Vertaling / Uitleg                                                                                 |
| --------------- | -------------------------------------------------------------------------------------------------- |
| *pubkey hash*   | Hash van de publieke sleutel (gebruikt om een Bitcoin-adres te genereren).                         |
| *public key*    | Publieke sleutel (gebruikt om fondsen te ontvangen, afgeleid van de privésleutel).                 |
| *signature*     | Digitale handtekening (cryptografisch bewijs dat een bericht afkomstig is van de houder van een privésleutel). |
| *scriptPubKey*  | Vergrendelingsscript (definieert de voorwaarden om een output te besteden).                         |
| *scriptSig*     | Ontgrendelingsscript (levert de gegevens om het *scriptPubKey* te vervullen).                      |
| *Stack*         | Stack (datastructuur gebruikt door *Bitcoin Script*).                                               |
| *input*         | Transactie-invoer (referentie naar een vorige output die als bron wordt gebruikt).                  |
| *output*        | Transactie-uitvoer (definieert de ontvanger en het bedrag).                                         |
| *transaction*   | Bitcoin-transactie (set van inputs en outputs die een overdracht valideren).                        |
| *XOR*           | Logische operator "exclusief OF", gebruikt in sommige cryptografische schema's.                    |
| *HMAC*          | Berichtauthenticatiecode gebaseerd op een hash en een geheime sleutel.                              |
| *ECDSA*         | Digitale handtekening algoritme met elliptische krommen.                                            |
| *hash*          | Hash (unieke en vaste vingerafdruk van gegevens).                                                   |
| *SigHash*       | Type handtekening-hash (definieert welke delen van een transactie worden ondertekend).              |
| *HD Wallet*     | Hiërarchische deterministische wallet (genereert meerdere sleutels uit één seed).                   |
| *Random Number* | Willekeurig getal (gebruikt om veilige privésleutels te genereren).                                 |
| *State*         | Toestand (tussenliggende waarde in een cryptografisch proces).                                      |
| *Entropy*       | Entropie (maat voor willekeur, gebruikt om wallet-seeds te genereren).                              |
| *Mnemonic*      | Mnemotechnisch hulpmiddel (reeks woorden die het back-uppen en herstellen van een seed vereenvoudigen). |
| *Wordlist*      | Woordenlijst (vooraf gedefinieerde set gebruikt om BIP39-mnemonics te genereren).                   |
| *Seed*          | Seed (initiële waarde waarmee alle sleutels in een HD-wallet kunnen worden afgeleid).               |
| *Address*       | Bitcoin-adres (leesbare identificatie voor het ontvangen van fondsen, afgeleid van de publieke sleutel). |
| *Leaf*          | Blad (eindknooppunt in een afgeleide boom).                                                         |

# Hash Functies


<partId>3713fee1-2ec2-512e-9e97-b6da9e4d2f17</partId>


## Inleiding tot Hash functies


<chapterId>dba011f5-1805-5a48-ac2b-4bd637c93703</chapterId>


Het eerste type cryptografische algoritmen dat gebruikt wordt in Bitcoin omvat Hash functies. Ze spelen een essentiële rol op verschillende niveaus van het protocol, maar ook binnen Bitcoin wallets. Laten we samen ontdekken wat een Hash functie is en waar deze voor wordt gebruikt in Bitcoin.


### Definitie en Principe van Hashing


Hashing is een proces dat informatie van willekeurige lengte omzet in een ander stuk informatie van vaste lengte door middel van een cryptografische Hash functie. Met andere woorden, een Hash functie neemt een invoer van willekeurige grootte en zet deze om in een vingerafdruk van vaste grootte, een "Hash" genaamd.

De Hash wordt soms ook "digest", "condensate", "condensed" of "hashed" genoemd.


De SHA256 Hash functie produceert bijvoorbeeld een Hash met een vaste lengte van 256 bits. Als we dus de invoer "_PlanB_" gebruiken, een bericht van willekeurige lengte, zal de gegenereerde Hash de volgende 256-bit vingerafdruk zijn:


```text
24f1b93b68026bfc24f5c8265f287b4c940fb1664b0d75053589d7a4f821b688
```


![CYP201](assets/fr/001.webp)


### Kenmerken van Hash Functies


Deze cryptografische Hash functies hebben een aantal essentiële kenmerken die ze bijzonder nuttig maken in de context van Bitcoin en andere computersystemen:



- Onomkeerbaarheid (of voorbeeldweerstand)
- Sabotagebestendigheid (lawine-effect)
- Weerstand tegen botsingen
- Tweede preimage weerstand


#### 1. Onomkeerbaarheid (preimage-bestendigheid):


Onomkeerbaarheid betekent dat het eenvoudig is om de Hash uit de invoerinformatie te berekenen, maar de omgekeerde berekening, dat wil zeggen, het vinden van de invoer uit de Hash, is praktisch onmogelijk. Deze eigenschap maakt Hash functies perfect voor het maken van unieke digitale vingerafdrukken zonder de originele informatie aan te tasten. Deze eigenschap wordt vaak een eenrichtingsfunctie genoemd.


In het gegeven voorbeeld is het verkrijgen van de Hash `24f1b9...` door de invoer "_PlanB_" te kennen eenvoudig en snel. Het bericht "_PlanB_" vinden door alleen `24f1b9...` te kennen is echter onmogelijk.


![CYP201](assets/fr/002.webp)


Daarom is het onmogelijk om een preimage $m$ te vinden voor een Hash $h$ zodat $h = \text{Hash}(m)$, waarbij $\text{Hash}$ een cryptografische Hash functie is.


#### 2. Sabotagebestendigheid (lawine-effect)


De tweede eigenschap is de sabotageweerstand, ook bekend als het **avalanche-effect**. Deze eigenschap wordt waargenomen in een Hash functie als een kleine verandering in het ingangsbericht resulteert in een radicale verandering in de Hash uitgang.


Als we teruggaan naar ons voorbeeld met de invoer "_PlanB_" en de SHA256 functie, dan hebben we gezien dat de gegenereerde Hash als volgt is:


```text
24f1b93b68026bfc24f5c8265f287b4c940fb1664b0d75053589d7a4f821b688
```


Als we een heel kleine verandering aanbrengen in de invoer door deze keer "_Planb_" te gebruiken, dan verandert alleen al het veranderen van een hoofdletter "B" naar een kleine letter "b" de SHA256 uitvoer Hash volledig:


```text
bb038b4503ac5d90e1205788b00f8f314583c5e22f72bec84b8735ba5a36df3f
```


![CYP201](assets/fr/003.webp)


Deze eigenschap zorgt ervoor dat zelfs een kleine wijziging van het originele bericht onmiddellijk detecteerbaar is, omdat het niet alleen een klein deel van de Hash verandert, maar de hele Hash. Dit kan op verschillende gebieden van belang zijn om de integriteit van berichten, software of zelfs Bitcoin transacties te verifiëren.


#### 3. Weerstand tegen botsingen


Het derde kenmerk is botsingsbestendigheid. Een Hash functie is botsingsbestendig als het rekenkundig onmogelijk is om 2 verschillende berichten te vinden die dezelfde Hash uitvoer van de functie opleveren. Formeel is het moeilijk om twee verschillende berichten $m_1$ en $m_2$ te vinden zodat:


$$
\text{HASH}(m_1) = \text{HASH}(m_2)
$$


![CYP201](assets/fr/004.webp)


In werkelijkheid is het wiskundig onvermijdelijk dat er botsingen bestaan voor Hash functies, omdat de grootte van de ingangen groter kan zijn dan de grootte van de uitgangen. Dit staat bekend als het Dirichlet-lade principe: als $n$ objecten verdeeld zijn over $m$ laden, met $m < n$, dan zal minstens één lade noodzakelijkerwijs twee of meer objecten bevatten. Voor een Hash functie geldt dit principe omdat het aantal mogelijke berichten (bijna) oneindig is, terwijl het aantal mogelijke hashes eindig is ($2^{256}$ in het geval van SHA256).


Deze eigenschap betekent dus niet dat er geen botsingen zijn voor Hash functies, maar eerder dat een goede Hash functie de kans op het vinden van een botsing verwaarloosbaar klein maakt. Deze eigenschap wordt bijvoorbeeld niet meer gecontroleerd op de SHA-0 en SHA-1 algoritmen, voorgangers van SHA-2, waarvoor botsingen zijn gevonden. Deze functies worden daarom nu afgeraden en vaak als verouderd beschouwd.

Voor een Hash functie van $n$ bits is de botsingsweerstand van de orde van $2^{frac{n}{2}}$, in overeenstemming met de verjaardagsaanval. Bijvoorbeeld, voor SHA256 ($n = 256$) is de complexiteit van het vinden van een botsing van de orde van $2^{128}$ pogingen. In praktische termen betekent dit dat als men $2^{128}$ verschillende berichten door de functie stuurt, men waarschijnlijk een botsing zal vinden.


#### 4. Weerstand tegen Tweede Prebeeld


Weerstand tegen tweede nabeeld is een ander belangrijk kenmerk van Hash functies. Het stelt dat gegeven een bericht $m_1$ en zijn Hash $h$, het computationeel onuitvoerbaar is om een ander bericht $m_2 \neq m_1$ te vinden zodanig dat:


$$
\text{HASH}(m_1) = \text{HASH}(m_2)
$$


Daarom is de weerstand tegen het tweede preimage enigszins vergelijkbaar met botsingsweerstand, behalve dat de aanval hier moeilijker is omdat de aanvaller $m_1$ niet vrij kan kiezen.


![CYP201](assets/fr/005.webp)


### Toepassingen van Hash Functies in Bitcoin


De meest gebruikte Hash functie in Bitcoin is **SHA256** ("_Secure Hash Algorithm 256 bits"_). Ontworpen in de vroege jaren 2000 door de NSA en gestandaardiseerd door het NIST, produceert het een 256-bit Hash uitvoer.


Deze functie wordt in veel aspecten van Bitcoin gebruikt. Op protocolniveau is het betrokken bij het Proof-of-Work mechanisme, waar het wordt toegepast in dubbele hashing om te zoeken naar een gedeeltelijke botsing tussen de header van een kandidaatblok, aangemaakt door een Miner, en het moeilijkheidsdoel. Als deze gedeeltelijke botsing wordt gevonden, wordt het kandidaat-blok geldig en kan het worden toegevoegd aan Blockchain.


SHA256 wordt ook gebruikt bij de opbouw van een Merkle Tree, wat met name de accumulator is die gebruikt wordt om transacties in blokken op te slaan. Deze structuur wordt ook gevonden in het Utreexo protocol, dat het mogelijk maakt om de grootte van de UTXO set te verkleinen. Daarnaast, met de introductie van Taproot in 2021, wordt SHA256 gebruikt in MAST (_Merkelised Alternative Script Tree_), wat het mogelijk maakt om alleen de bestedingsvoorwaarden te onthullen die daadwerkelijk gebruikt worden in een script, zonder de andere mogelijke opties te onthullen. Het wordt ook gebruikt bij het berekenen van transactie identifiers, bij het verzenden van pakketten over het P2P netwerk, bij elektronische handtekeningen... Tot slot, en dit is van bijzonder belang in deze training, wordt SHA256 gebruikt op applicatieniveau voor de constructie van Bitcoin wallets en de afleiding van adressen.


Meestal, wanneer je het gebruik van SHA256 in Bitcoin tegenkomt, zal het eigenlijk een dubbele Hash SHA256 zijn, genoteerd "**HASH256**", die simpelweg bestaat uit het twee keer achter elkaar toepassen van SHA256:


$$
\text{HASH256}(m) = \text{SHA256}(\text{SHA256}(m))
$$


Deze praktijk van dubbel hashen voegt een extra Layer aan beveiliging toe tegen bepaalde potentiële aanvallen, ook al wordt een enkele SHA256 tegenwoordig als cryptografisch veilig beschouwd.


Een andere hashingfunctie die beschikbaar is in de Scripttaal en gebruikt wordt voor het afleiden van ontvangstadressen is de functie RIPEMD160. Deze functie produceert een Hash van 160 bits (dus korter dan SHA256). Deze wordt meestal gecombineerd met SHA256 om de functie HASH160 te vormen:


$$
\text{HASH160}(m) = \text{RIPEMD160}(\text{SHA256}(m))
$$


Deze combinatie wordt gebruikt om generate kortere hashes te maken, met name bij het maken van bepaalde Bitcoin adressen die hashes van sleutels of script-hashes voorstellen, en om fingerprints van sleutels te maken.


Tot slot wordt, alleen op applicatieniveau, soms ook de SHA512 functie gebruikt, die indirect een rol speelt bij het afleiden van sleutels voor wallets. Deze functie lijkt erg op SHA256 in zijn werking; beide behoren tot dezelfde SHA2 familie, maar SHA512 produceert, zoals zijn naam aangeeft, een 512-bit Hash, vergeleken met 256 bits voor SHA256. We zullen het gebruik ervan in de volgende hoofdstukken gedetailleerd beschrijven.


Je kent nu de essentiële basis over hashing functies voor wat volgt. In het volgende hoofdstuk stel ik voor om in meer detail de werking van de functie te ontdekken die het hart vormt van Bitcoin: SHA256. We zullen het ontleden om te begrijpen hoe het de karakteristieken bereikt die we hier beschreven hebben. Dit volgende hoofdstuk is vrij lang en technisch, maar het is niet essentieel om de rest van de training te volgen. Dus, als je moeite hebt om het te begrijpen, maak je dan geen zorgen en ga direct door naar het volgende hoofdstuk, dat veel toegankelijker zal zijn.


## De interne werking van SHA256


<chapterId>905eb320-f15b-5fb6-8d2d-5bb447337deb</chapterId>


We hebben eerder gezien dat hashingfuncties belangrijke eigenschappen bezitten die hun gebruik in Bitcoin rechtvaardigen. Laten we nu de interne mechanismen van deze hashingfuncties onderzoeken die hen deze eigenschappen geven, en om dit te doen, stel ik voor om de werking van SHA256 te ontleden.


De SHA256- en SHA512-functies behoren tot dezelfde SHA2-familie. Hun mechanisme is gebaseerd op een specifieke constructie genaamd **Merkle-Damgård constructie**. RIPEMD160 gebruikt ook ditzelfde type constructie.


Ter herinnering, we hebben een bericht van willekeurige grootte als invoer voor SHA256, en we zullen het door de functie sturen om een 256-bits Hash als uitvoer te verkrijgen.


### Voorbewerking van de invoer


Om te beginnen moeten we ons invoerbericht $m$ voorbereiden zodat het een standaardlengte heeft die een veelvoud is van 512 bits. Deze stap is cruciaal voor de goede werking van het algoritme.

Om dit te doen, beginnen we met de padding bits stap. We voegen eerst een scheidingsbit `1` toe aan het bericht, gevolgd door een bepaald aantal `0` bits. Het aantal toegevoegde `0` bits wordt zo berekend dat de totale lengte van het bericht na deze toevoeging congruent is met 448 modulo 512. De lengte $L$ van het bericht met de opvulbits is dus gelijk aan:


$$
L \equiv 448 \mod 512
$$


$text{mod}$, voor modulo, is een wiskundige bewerking die, tussen twee gehele getallen, de rest geeft van de Euclidische deling van de eerste door de tweede. Bijvoorbeeld: $16 \mod 5 = 1$. Het is een bewerking die veel gebruikt wordt in cryptografie.


Hier zorgt de opvulstap ervoor dat, na het toevoegen van de 64 bits in de volgende stap, de totale lengte van het geëgaliseerde bericht een veelvoud van 512 bits zal zijn. Als het initiële bericht een lengte van $M$ bits heeft, is het aantal ($N$) `0` bits dat toegevoegd moet worden dus:


$$
N = (448 - (M + 1) \mod 512) \mod 512
$$


Als het initiële bericht bijvoorbeeld 950 bits is, zou de berekening als volgt zijn:


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


We zouden dus 9 `0`s hebben naast het scheidingsteken `1`. Onze opvulbits die direct na ons bericht $M$ moeten worden toegevoegd zouden dus zijn:


```text
1000 0000 00
```


Na het toevoegen van de opvulbits aan ons bericht $M$, voegen we ook een 64-bits representatie van de oorspronkelijke lengte van het bericht $M$ toe, uitgedrukt in binair. Hierdoor is de Hash functie gevoelig voor de volgorde van bits en de lengte van het bericht.


Als we teruggaan naar ons voorbeeld met een initiële boodschap van 950 bits, converteren we het decimale getal `950` naar binair, wat ons `1110 1101 10` oplevert. We vullen dit getal aan met nullen aan de basis om een totaal van 64 bits te maken. In ons voorbeeld geeft dit:


```text
0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0011 1011 0110
```


Deze opvulgrootte wordt toegevoegd na de bitopvulling. Daarom bestaat het bericht na onze voorbewerking uit drie delen:



- Het oorspronkelijke bericht $M$;
- Een bit `1` gevolgd door meerdere bits `0` om de bit padding te vormen;
- Een 64-bits weergave van de lengte van $M$ om de padding met de grootte te vormen.


![CYP201](assets/fr/006.webp)


### Initialisatie van variabelen


SHA256 gebruikt acht initiële toestandsvariabelen, aangeduid met $A$ tot $H$, elk van 32 bits. Deze variabelen worden geïnitialiseerd met specifieke constanten, die de fractionele delen zijn van de vierkantswortels van de eerste acht priemgetallen. We zullen deze waarden later gebruiken tijdens het hashingproces:



- $A = 0x6a09e667$
- $B = 0xbb67ae85$
- $C = 0x3c6ef372$
- $D = 0xa54ff53a$
- $E = 0x510e527f$
- $F = 0x9b05688c$
- $G = 0x1f83d9ab$
- $H = 0x5be0cd19$


SHA256 gebruikt ook 64 andere constanten, aangeduid met $K_0$ tot $K_{63}$, die de fractionele delen zijn van de derdemachtswortels van de eerste 64 priemgetallen:


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


### Verdeling van de invoer


Nu we een geëgaliseerde invoer hebben, gaan we verder met de belangrijkste verwerkingsfase van het SHA256 algoritme: de compressiefunctie. Deze stap is erg belangrijk, omdat het voornamelijk de Hash functie zijn cryptografische eigenschappen geeft die we in het vorige hoofdstuk bestudeerden.


Eerst verdelen we ons geëgaliseerde bericht (resultaat van de voorbewerkingsstappen) in verschillende blokken $P$ van elk 512 bits. Als ons geëgaliseerde bericht een totale grootte heeft van $n maal 512$ bits, dan hebben we dus $n$ blokken van elk 512 bits. Elk blok van 512 bits wordt afzonderlijk verwerkt door de compressiefunctie, die bestaat uit 64 ronden van opeenvolgende bewerkingen. Laten we deze blokken $P_1$, $P_2$, $P_3$ ... noemen.


### Logische bewerkingen


Voordat we de compressiefunctie in detail bekijken, is het belangrijk om de logische basisbewerkingen te begrijpen die erin worden gebruikt. Deze bewerkingen, gebaseerd op Booleaanse algebra, werken op bitniveau. De gebruikte logische basisbewerkingen zijn:



- **Samenvoeging (AND)**: komt overeen met een logische "AND".
- **Ontknoping (OR)**: komt overeen met een logische "OR".
- **Negatie (NOT)**: komt overeen met een logische "NOT".


Vanuit deze basisbewerkingen kunnen we complexere bewerkingen definiëren, zoals de "exclusieve OR" (XOR), aangeduid met $oplus$, die veel gebruikt wordt in de cryptografie.

Elke logische bewerking kan worden weergegeven door een waarheidstabel, die het resultaat aangeeft voor alle mogelijke combinaties van binaire invoerwaarden (twee operanden $p$ en $q$).

Voor XOR ($oplus$):


| $p$ | $q$ | $p \oplus q$ |
| --- | --- | ------------ |
| 0   | 0   | 0            |
| 0   | 1   | 1            |
| 1   | 0   | 1            |
| 1   | 1   | 0            |

Voor AND ($land$):


| $p$ | $q$ | $p \land q$ |
| --- | --- | ----------- |
| 0   | 0   | 0           |
| 0   | 1   | 0           |
| 1   | 0   | 0           |
| 1   | 1   | 1           |

Voor NOT ($niet p$):


| $p$ | $\lnot p$ |
| --- | --------- |
| 0   | 1         |
| 1   | 0         |

Laten we een voorbeeld nemen om de werking van XOR op bitniveau te begrijpen. Als we twee binaire getallen op 6 bits hebben:



- $a = 101100$
- $b = 001000$


Dan:


$$

a \oplus b = 101100 \oplus 001000 = 100100


$$


Door bit voor bit XOR toe te passen:


| Bit Position | $a$ | $b$ | $a \oplus b$ |
| ------------ | --- | --- | ------------ |
| 1            | 1   | 0   | 1            |
| 2            | 0   | 0   | 0            |
| 3            | 1   | 1   | 0            |
| 4            | 1   | 0   | 1            |
| 5            | 0   | 0   | 0            |
| 6            | 0   | 0   | 0            |

Het resultaat is dus $100100$.


Naast logische bewerkingen gebruikt de compressiefunctie bitverschuivingsbewerkingen, die een essentiële rol spelen bij de verspreiding van bits in het algoritme.


Ten eerste is er de logische rechtse verschuiving, aangeduid als $ShR_n(x)$, die alle bits van $x$ naar rechts verschuift met posities van $n$ en de lege bits aan de linkerkant opvult met nullen.


Bijvoorbeeld voor $x = 101100001$ (op 9 bits) en $n = 4$:


$$

ShR_4(101100001) = 000010110


$$


Schematisch kan de rechterschakeling als volgt worden weergegeven:


![CYP201](assets/fr/007.webp)


Een andere bewerking die in SHA256 wordt gebruikt voor bitmanipulatie is de rechtsomwenteling, aangeduid met $RotR_n(x)$, die de bits van $x$ met $n$ posities naar rechts verschuift en de verschoven bits weer aan het begin van de string plaatst.

Bijvoorbeeld voor $x = 101100001$ (meer dan 9 bits) en $n = 4$:


$$

RotR_4(101100001) = 000110110


$$


Schematisch zou de rechter circulaire shift operatie als volgt gezien kunnen worden:


![CYP201](assets/fr/008.webp)


### Compressiefunctie


Nu we de basisbewerkingen hebben begrepen, laten we de SHA256 compressiefunctie in detail bekijken.


In de vorige stap hebben we onze invoer verdeeld in verschillende 512-bits stukken $P$. Voor elk 512-bits blok $P$ hebben we:



- De berichtwoorden **$W_i$**: voor $i$ van 0 tot 63.
- De constanten $K_i$ voor $i$ van 0 tot 63, gedefinieerd in de vorige stap.
- De toestandsvariabelen **$A, B, C, D, E, F, G, H$**: geïnitialiseerd met de waarden uit de vorige stap.


De eerste 16 woorden, $W_0$ tot $W_{15}$, worden rechtstreeks uit het verwerkte 512-bits blok $P$ gehaald. Elk woord $W_i$ bestaat uit 32 opeenvolgende bits uit het blok. We nemen dus bijvoorbeeld ons eerste stukje invoer $P_1$ en verdelen dit verder in kleinere stukjes van 32 bits die we woorden noemen.


De volgende 48 woorden ($W_{16}$ tot $W_{63}$) worden gegenereerd met de volgende formule:


$$
W_i = W_{i-16} + \sigma_0(W_{i-15}) + W_{i-7} + \sigma_1(W_{i-2}) \mod 2^{32}
$$


Met:



- $\sigma_0(x) = RotR_7(x) \oplus RotR_{18}(x) \oplus ShR_3(x)$
- $\sigma_1(x) = RotR_{17}(x) \oplus RotR_{19}(x) \oplus ShR_{10}(x)$


In dit geval is $x$ gelijk aan $W_{i-15}$ voor $\sigma_0(x)$ en $W_{i-2}$ voor $\sigma_1(x)$.


Als we alle woorden $W_i$ voor ons 512-bits stuk hebben bepaald, kunnen we verder met de compressiefunctie, die bestaat uit het uitvoeren van 64 rondes.


![CYP201](assets/fr/009.webp)

Voor elke ronde $i$ van 0 tot 63 hebben we drie verschillende soorten invoer. Ten eerste de $W_i$ die we net hebben bepaald, deels bestaande uit ons berichtstuk $P_n$. Vervolgens de 64 constanten $K_i$. Ten slotte gebruiken we de toestandsvariabelen $A$, $B$, $C$, $D$, $E$, $F$, $G$ en $H$, die tijdens het hashingproces zullen evolueren en bij elke compressiefunctie worden aangepast. Voor het eerste stuk $P_1$ gebruiken we echter de eerder gegeven beginconstanten.


Vervolgens voeren we de volgende bewerkingen uit op onze invoer:



- Functie $Sigma_0$:


$$
\Sigma_0(A) = RotR_2(A) \oplus RotR_{13}(A) \oplus RotR_{22}(A)
$$



- Functie $Sigma_1$:


$$
\Sigma_1(E) = RotR_6(E) \oplus RotR_{11}(E) \oplus RotR_{25}(E)
$$



- Functie $Ch$ ("_Choose_")**:**


$$
Ch(E, F, G) = (E \land F) \oplus (\lnot E \land G)
$$



- Functie $Maj$ ("_Majority_"):


$$
Maj(A, B, C) = (A \land B) \oplus (A \land C) \oplus (B \land C)
$$


Vervolgens berekenen we 2 tijdelijke variabelen:



- $temp1$:


$$
temp1 = H + \Sigma_1(E) + Ch(E, F, G) + K_i + W_i \mod 2^{32}
$$



- $temp2$:


$$
temp2 = \Sigma_0(A) + Maj(A, B, C) \mod 2^{32}
$$


Vervolgens werken we de toestandsvariabelen als volgt bij:


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


Het volgende diagram stelt een ronde voor van de SHA256 compressiefunctie zoals we zojuist beschreven hebben:


![CYP201](assets/fr/010.webp)



- De pijlen geven de gegevensstroom aan;
- De vakjes geven de uitgevoerde bewerkingen weer;
- De omcirkelde $+$ vertegenwoordigen de optelling modulo $2^{32}$.


We kunnen al zien dat deze ronde nieuwe toestandsvariabelen $A$, $B$, $C$, $D$, $E$, $F$, $G$ en $H$ oplevert. Deze nieuwe variabelen dienen als input voor de volgende ronde, die op zijn beurt weer nieuwe variabelen $A$, $B$, $C$, $D$, $E$, $F$, $G$ en $H$ oplevert, die gebruikt worden voor de volgende ronde. Dit proces gaat door tot de 64e ronde.

Na de 64 ronden werken we de beginwaarden van de toestandsvariabelen bij door ze toe te voegen aan de eindwaarden aan het einde van ronde 64:


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


Deze nieuwe waarden van $A$, $B$, $C$, $D$, $E$, $F$, $G$ en $H$ dienen als beginwaarden voor het volgende blok, $P_2$. Voor dit blok $P_2$ herhalen we hetzelfde compressieproces met 64 rondes, dan updaten we de variabelen voor blok $P_3$, enzovoort tot het laatste blok van onze geëgaliseerde invoer.


Na het verwerken van alle berichtblokken, voegen we de uiteindelijke waarden van de variabelen $A$, $B$, $C$, $D$, $E$, $F$, $G$ en $H$ samen om de uiteindelijke 256-bit Hash van onze hashingfunctie te vormen:


$$

\text{Hash} = A \Vert B \Vert C \Vert D \Vert E \Vert F \Vert G \Vert H


$$


Elke variabele is een geheel getal van 32 bits, dus hun aaneenschakeling levert altijd een resultaat van 256 bits op, ongeacht de grootte van het bericht dat we invoeren in de hashing-functie.


### Rechtvaardiging van cryptografische eigenschappen


Maar hoe is deze functie dan onomkeerbaar, botsingsbestendig en bestand tegen knoeien?


Voor de sabotageweerstand is het vrij eenvoudig te begrijpen. Er worden zoveel berekeningen uitgevoerd in cascade, die zowel afhankelijk zijn van de invoer als van de constanten, dat de kleinste wijziging van de initiële boodschap het afgelegde pad volledig verandert, en dus de uitvoer Hash volledig verandert. Dit wordt het lawine-effect genoemd. Deze eigenschap wordt gedeeltelijk gegarandeerd door de menging van de tussentoestanden met de begintoestanden voor elk stuk.

Wanneer we het hebben over een cryptografische Hash functie, wordt de term "onomkeerbaarheid" over het algemeen niet gebruikt. In plaats daarvan hebben we het over "preimage-resistentie", die specificeert dat het voor elke gegeven $y$ moeilijk is om een $x$ te vinden zodat $h(x) = y$. Deze preimage-resistentie wordt gegarandeerd door de algebraïsche complexiteit en de sterke niet-lineariteit van de bewerkingen die in de compressiefunctie worden uitgevoerd, evenals door het verlies van bepaalde informatie in het proces. Bijvoorbeeld, voor een gegeven resultaat van een optelling modulo, zijn er verschillende mogelijke operanden:


$$

3+2 \mod 10 = 5 \\
7+8 \mod 10 = 5 \\
5+10 \mod 10 = 5


$$


In dit voorbeeld kan men, als men alleen de gebruikte modulo (10) en het resultaat (5) kent, niet met zekerheid bepalen welke de juiste operanden zijn die bij de optelling zijn gebruikt. Er wordt gezegd dat er meerdere congruenties modulo 10 zijn.


Voor de XOR-bewerking hebben we te maken met hetzelfde probleem. Denk aan de waarheidstabel voor deze bewerking: elke uitgang van 1 bit kan worden bepaald door twee verschillende ingangsconfiguraties die precies dezelfde waarschijnlijkheid hebben om de juiste waarden te zijn. Daarom kan men de operanden van een XOR niet met zekerheid bepalen door alleen het resultaat te kennen. Als we de grootte van de XOR-operanden vergroten, neemt het aantal mogelijke invoerconfiguraties waarbij alleen het resultaat bekend is exponentieel toe. Bovendien wordt XOR vaak gebruikt naast andere bewerkingen op bitniveau, zoals de bewerking $text{RotR}$, die nog meer mogelijke interpretaties aan het resultaat toevoegen.


De compressiefunctie gebruikt ook de bewerking $text{ShR}$. Deze bewerking verwijdert een deel van de basisinformatie, die later niet meer terug te halen is. Nogmaals, er is geen algebraïsche manier om deze bewerking terug te draaien. Al deze eenrichtings- en informatieverliesoperaties worden zeer vaak gebruikt in compressiefuncties. Het aantal mogelijke inputs voor een gegeven output is dus bijna oneindig, en elke poging tot omgekeerde berekening zou leiden tot vergelijkingen met een zeer groot aantal onbekenden, die bij elke stap exponentieel zouden toenemen.


Tenslotte spelen voor de eigenschap botsingsbestendigheid verschillende parameters een rol. De voorbewerking van het originele bericht speelt een essentiële rol. Zonder deze voorbewerking zou het gemakkelijker kunnen zijn om botsingen op de functie te vinden. Hoewel botsingen theoretisch bestaan (vanwege het "pigeonhole" principe), maakt de structuur van de Hash functie, gecombineerd met de eerder genoemde eigenschappen, de kans op het vinden van een botsing extreem laag.

Om een Hash functie botsingsbestendig te maken, is het essentieel dat:



- De uitvoer is onvoorspelbaar: Elke voorspelbaarheid kan worden uitgebuit om sneller botsingen te vinden dan met een brute force aanval. De functie zorgt ervoor dat elke bit van de uitvoer op een niet-triviale manier afhangt van de invoer. Met andere woorden, de functie is zo ontworpen dat elke bit van het eindresultaat een onafhankelijke kans heeft om 0 of 1 te zijn, zelfs als deze onafhankelijkheid in de praktijk niet absoluut is.
- De verdeling van hashes is pseudo-willekeurig: Dit zorgt ervoor dat de hashes uniform verdeeld zijn.
- De grootte van de Hash is aanzienlijk: hoe groter de mogelijke ruimte voor resultaten, hoe moeilijker het is om een botsing te vinden.


Cryptografen ontwerpen deze functies door de best mogelijke aanvallen te evalueren om botsingen te vinden en vervolgens de parameters aan te passen om deze aanvallen ineffectief te maken.


### Merkle-Damgård Bouw


De structuur van SHA256 is gebaseerd op de Merkle-Damgård constructie, die het mogelijk maakt om een compressiefunctie om te zetten in een Hash functie die berichten van willekeurige lengte kan verwerken. Dit is precies wat we in dit hoofdstuk hebben gezien.


Sommige oude Hash functies zoals SHA1 of MD5, die deze specifieke constructie gebruiken, zijn echter kwetsbaar voor lengte-uitbreidingsaanvallen. Dit is een techniek waarmee een aanvaller die de Hash van een bericht $M$ en de lengte van $M$ kent (zonder het bericht zelf te kennen), de Hash van een bericht $M'$ kan berekenen dat gevormd is door $M$ aan elkaar te rijgen met extra inhoud.


SHA256, hoewel het hetzelfde type constructie gebruikt, is theoretisch bestand tegen dit type aanval, in tegenstelling tot SHA1 en MD5. Dit verklaart misschien het mysterie van de dubbele hashing die Satoshi Nakamoto in Bitcoin implementeerde. Om dit type aanval te vermijden, gebruikte Satoshi misschien liever een dubbele SHA256:


$$

\text{HASH256}(m) = \text{SHA256}(\text{SHA256}(m))


$$


Dit verhoogt de veiligheid tegen mogelijke aanvallen gerelateerd aan de Merkle-Damgård constructie, maar het verhoogt de veiligheid van het hashingproces niet in termen van botsingsbestendigheid. Bovendien, zelfs als SHA256 kwetsbaar was geweest voor dit type aanval, zou het geen ernstige impact hebben gehad, aangezien alle gebruikssituaties van Hash functies in Bitcoin betrekking hebben op openbare gegevens. De aanval voor lengteverlenging zou echter alleen nuttig kunnen zijn voor een aanvaller als de gehashte gegevens privé zijn en de gebruiker de Hash functie heeft gebruikt als authenticatiemechanisme voor deze gegevens, vergelijkbaar met een MAC. De implementatie van dubbel hashing blijft dus een mysterie in het ontwerp van Bitcoin.

Nu we in detail hebben gekeken naar de werking van Hash functies, in het bijzonder SHA256, dat uitgebreid gebruikt wordt in Bitcoin, zullen we ons meer specifiek richten op de cryptografische afleidingsalgoritmen die gebruikt worden op applicatieniveau, in het bijzonder voor het afleiden van de sleutels voor je Wallet.


## De gebruikte algoritmen voor afleiding


<chapterId>cc668121-7789-5e99-bf5e-1ba085f4f5f2</chapterId>


In Bitcoin op applicatieniveau worden, naast Hash functies, cryptografische afleidingsalgoritmen gebruikt om generate gegevens te beveiligen van initiële invoer. Hoewel deze algoritmen gebaseerd zijn op Hash functies, dienen ze verschillende doelen, vooral in termen van authenticatie en sleutelgeneratie. Deze algoritmen behouden enkele kenmerken van Hash functies, zoals onomkeerbaarheid, sabotagebestendigheid en botsingsbestendigheid.


In Bitcoin wallets worden voornamelijk 2 afleidingsalgoritmes gebruikt:



- HMAC (_Hash-gebaseerde berichtenauthenticatiecode_)
- PBKDF2 (**Password-Based Key Derivation Function 2**)


We zullen samen de werking en de rol van elk van hen onderzoeken.


### HMAC-SHA512


HMAC is een cryptografisch algoritme dat een authenticatiecode berekent op basis van een combinatie van een Hash functie en een geheime sleutel. Bitcoin gebruikt HMAC-SHA512, de variant van HMAC die de SHA512 Hash functie gebruikt. We hebben in het vorige hoofdstuk al gezien dat SHA512 deel uitmaakt van dezelfde familie van Hash functies als SHA256, maar het produceert een 512-bit uitvoer.


Hier is het algemene werkingsschema met $m$ als invoerbericht en $K$ als geheime sleutel:


![CYP201](assets/fr/011.webp)


Laten we in meer detail bestuderen wat er gebeurt in deze HMAC-SHA512 zwarte doos. De HMAC-SHA512 functie met:



- $m$: het willekeurig grote bericht gekozen door de gebruiker (eerste invoer);
- $K$: de willekeurige geheime sleutel gekozen door de gebruiker (tweede invoer);
- $K'$: de sleutel $K$ aangepast aan de grootte $B$ van de Hash functieblokken (1024 bits voor SHA512, of 128 bytes);
- ${SHA512}$: de SHA512 Hash functie;
- $oplus$: de XOR (exclusive or) bewerking;
- $Vert$: de aaneenschakelingsoperator, die bitreeksen van begin tot eind aan elkaar koppelt;
- $\text{opad}$: constante samengesteld uit de byte $0x5c$ 128 keer herhaald
- $text{ipad}$: constante samengesteld uit de byte $0x36$ 128 keer herhaald.


Voordat de HMAC wordt berekend, moeten de sleutel en de constanten gelijk worden gemaakt aan de blokgrootte $B$. Als de sleutel $K$ bijvoorbeeld korter is dan 128 bytes, wordt deze opgevuld met nullen om de grootte $B$ te bereiken. Als $K$ langer is dan 128 bytes, wordt hij gecomprimeerd met SHA512 en worden er nullen toegevoegd tot hij 128 bytes bereikt. Op deze manier wordt een geëgaliseerde sleutel met de naam $K'$ verkregen. De waarden van $\text{opad}$ en $\text{ipad}$ worden verkregen door hun basisbyte te herhalen ($0x5c$ voor $\text{opad}$, $0x36$ voor $\text{ipad}$) totdat de grootte $B$ is bereikt. Dus, met $B = 128$ bytes, hebben we:


$$

\text{opad} = \underbrace{0x5c5c\ldots5c}\_{128 \  \text{bytes}}


$$


Nadat de voorbewerking is uitgevoerd, wordt het HMAC-SHA512-algoritme gedefinieerd door de volgende vergelijking:


$$

\text{HMAC-SHA512}(K,m) = \text{SHA512} \left( (K' \oplus \text{opad}) \parallel \text{SHA512} \left( (K' \oplus \text{ipad}) \parallel m \right) \right)


$$


Deze vergelijking is onderverdeeld in de volgende stappen:



- XOR de aangepaste sleutel $K'$ met $\text{ipad}$ om $\text{iKpad}$ te verkrijgen;
- XOR de aangepaste sleutel $K'$ met $\text{opad}$ om $\text{oKpad}$ te verkrijgen;
- Voeg $tekst{iKpad}$ samen met het bericht $m$.
- Hash dit resultaat met SHA512 om een tussenproduct Hash $H_1$ te verkrijgen.
- Voeg ${oKpad}$ samen met $H_1$.
- Hash dit resultaat met SHA512 om het uiteindelijke resultaat $H_2$ te verkrijgen.


Deze stappen kunnen schematisch als volgt worden samengevat:


![CYP201](assets/fr/012.webp)


HMAC wordt in Bitcoin met name gebruikt voor het afleiden van sleutels in HD (Hierarchical Deterministic) wallets (we zullen hier in de komende hoofdstukken dieper op ingaan) en als onderdeel van PBKDF2.


### PBKDF2


PBKDF2 (_Password-Based Key Derivation Function 2_) is een sleutelafleidingsalgoritme dat is ontworpen om de veiligheid van wachtwoorden te verbeteren. Het algoritme past een pseudo-willekeurige functie toe (hier HMAC-SHA512) op een wachtwoord en een cryptografische salt en herhaalt deze bewerking een bepaald aantal keren om een outputsleutel te produceren.


In Bitcoin wordt PBKDF2 gebruikt om generate de seed van een HD Wallet te maken uit een Mnemonic zin en een passphrase (maar daar zullen we in de komende hoofdstukken dieper op ingaan).


Het PBKDF2 proces gaat als volgt, met:



- $m$: de Mnemonic-zin van de gebruiker;
- $s$: de optionele passphrase om de beveiliging te verhogen (leeg veld als er geen passphrase is);
- $n$: het aantal iteraties van de functie, in ons geval is dat 2048.


De PBKDF2-functie is iteratief gedefinieerd. Elke iteratie neemt het resultaat van de vorige, haalt het door HMAC-SHA512 en combineert de opeenvolgende resultaten om de uiteindelijke sleutel te produceren:


$$

\text{PBKDF2}(m, s) = \text{HMAC-SHA512}^{2048}(m, s)


$$


Schematisch kan PBKDF2 als volgt worden voorgesteld:


![CYP201](assets/fr/013.webp)


In dit hoofdstuk hebben we de HMAC-SHA512 en PBKDF2 functies onderzocht, die hashingfuncties gebruiken om de integriteit en veiligheid van sleutelafleidingen in het Bitcoin protocol te garanderen. In het volgende deel zullen we kijken naar digitale handtekeningen, een andere cryptografische methode die veel gebruikt wordt in Bitcoin.


# Digitale handtekeningen


<partId>76b58a00-0c18-54b9-870d-6b7e34029db8</partId>


## Digitale handtekeningen en elliptische krommen


<chapterId>c9dd9672-6da1-57f8-9871-8b28994d4c1a</chapterId>


De tweede cryptografische methode die gebruikt wordt in Bitcoin zijn digitale handtekening algoritmen. Laten we eens onderzoeken wat dit inhoudt en hoe het werkt.


### Bitcoins, UTXO's en bestedingsvoorwaarden


De term "_wallet_" in Bitcoin kan nogal verwarrend zijn voor beginners. Een Bitcoin Wallet is namelijk software die niet direct je bitcoins bevat, in tegenstelling tot een fysieke Wallet die munten of biljetten kan bevatten. Bitcoins zijn gewoon rekeneenheden. Deze rekeneenheid wordt vertegenwoordigd door **UTXO** (_Unspent Transaction Outputs_), dat zijn niet-uitgegeven transactie-uitgangen. Als deze outputs niet uitgegeven zijn, betekent dit dat ze toebehoren aan een gebruiker. UTXO's zijn in zekere zin stukjes bitcoins, van variabele grootte, die toebehoren aan een gebruiker.


Het Bitcoin protocol is gedistribueerd en werkt zonder centrale autoriteit. Daarom is het niet zoals traditionele bankgegevens, waar de euro's die van jou zijn simpelweg geassocieerd zijn met je persoonlijke identiteit. In Bitcoin zijn je UTXO's van jou, omdat ze beschermd zijn door bestedingsvoorwaarden die in de Scripttaal zijn gespecificeerd. Simpel gezegd zijn er twee soorten scripts: het vergrendelingsscript (_scriptPubKey_), dat een UTXO beschermt, en het ontgrendelingsscript (_scriptSig_), dat het mogelijk maakt een UTXO te ontgrendelen en dus de Bitcoin eenheden die het vertegenwoordigt uit te geven.

De initiële werking van Bitcoin met P2PK scripts houdt in dat er een publieke sleutel gebruikt wordt om geld te blokkeren, waarbij in een _scriptPubKey_ gespecificeerd wordt dat de persoon die deze UTXO wil uitgeven een geldige handtekening moet leveren met de private sleutel die overeenkomt met deze publieke sleutel. Om deze UTXO te ontgrendelen, is het dus nodig om een geldige handtekening te leveren in het _scriptSig_. Zoals de namen al suggereren, is de publieke sleutel bij iedereen bekend, omdat deze wordt uitgezonden op de Blockchain, terwijl de privésleutel alleen bekend is bij de rechtmatige eigenaar van het geld.

Dit is de basiswerking van Bitcoin, maar in de loop der tijd is deze werking complexer geworden. Eerst introduceerde Satoshi ook P2PKH scripts, die een ontvangende Address gebruiken in de _scriptPubKey_, die de Hash van de publieke sleutel voorstelt. Daarna werd het systeem nog complexer met de komst van SegWit en daarna Taproot. Het algemene principe blijft echter fundamenteel hetzelfde: een publieke sleutel of een representatie van deze sleutel wordt gebruikt om UTXO's te vergrendelen, en een corresponderende private sleutel is nodig om ze te ontgrendelen en dus uit te geven.


Een gebruiker die een Bitcoin transactie wil doen, moet daarom een digitale handtekening zetten met zijn privé-sleutel op de transactie. De handtekening kan worden geverifieerd door andere netwerkdeelnemers. Als deze geldig is, betekent dit dat de gebruiker die de transactie initieert inderdaad de eigenaar is van de private sleutel, en dus de eigenaar van de bitcoins die hij/zij wil uitgeven. Andere gebruikers kunnen de transactie dan accepteren en verspreiden.


Daarom moet een gebruiker die bitcoins bezit die vergrendeld zijn met een publieke sleutel, een manier vinden om veilig op te bergen wat het mogelijk maakt om zijn fondsen te ontgrendelen: de privésleutel. Een Bitcoin Wallet is precies een apparaat waarmee je gemakkelijk al je sleutels kunt bewaren zonder dat andere mensen er toegang toe hebben. Het is daarom meer een sleutelhanger dan een Wallet.


Het wiskundige verband tussen een openbare sleutel en een privésleutel, evenals de mogelijkheid om een handtekening uit te voeren om het bezit van een privésleutel te bewijzen zonder deze te onthullen, worden mogelijk gemaakt door een algoritme voor digitale handtekeningen. In het Bitcoin protocol worden twee handtekeningalgoritmen gebruikt: **ECDSA** (_Elliptic Curve Digital Signature Algorithm_) en het **Schnorr handtekeningenschema**. ECDSA is het digitale handtekeningprotocol dat vanaf het begin in Bitcoin gebruikt werd. Schnorr is recenter in Bitcoin, omdat het in november 2021 werd geïntroduceerd met de Taproot update.

Deze twee algoritmen lijken erg op elkaar in hun mechanisme. Ze zijn beide gebaseerd op elliptische curve cryptografie. Het grote verschil tussen deze twee protocollen zit in de structuur van de handtekening en enkele specifieke wiskundige eigenschappen. We zullen daarom de werking van deze algoritmen bestuderen, te beginnen met de oudste: ECDSA.


### Elliptische kromme cryptografie


Elliptische Curve Cryptografie (ECC) is een reeks algoritmen die een elliptische curve gebruiken voor zijn verschillende wiskundige en geometrische eigenschappen voor cryptografische doeleinden. De veiligheid van deze algoritmen berust op de moeilijkheid van het discrete logaritmeprobleem op elliptische krommen. Elliptische krommen worden met name gebruikt voor sleuteluitwisselingen, asymmetrische encryptie of voor het maken van digitale handtekeningen.


Een belangrijke eigenschap van deze krommen is dat ze symmetrisch zijn ten opzichte van de x-as. Zo zal elke niet-verticale lijn die de kromme in twee verschillende punten snijdt, de kromme altijd snijden in een derde punt. Bovendien zal elke raaklijn aan de kromme in een niet-singulier punt de kromme in een ander punt snijden. Deze eigenschappen zijn nuttig voor het definiëren van bewerkingen op de kromme.


Hier is een voorstelling van een elliptische kromme over het veld van reële getallen:


![CYP201](assets/fr/014.webp)


Elke elliptische curve wordt gedefinieerd door een vergelijking van de vorm:


$$

y^2 = x^3 + ax + b


$$


### secp256k1


Om ECDSA of Schnorr te gebruiken, moet men de parameters van de elliptische curve kiezen, dat wil zeggen de waarden van $a$ en $b$ in de vergelijking van de curve. Er zijn verschillende standaarden van elliptische krommen die cryptografisch veilig zijn. De meest bekende is de _secp256r1_ curve, gedefinieerd en aanbevolen door het NIST (_National Institute of Standards and Technology_).


Desondanks koos Satoshi Nakamoto, de uitvinder van Bitcoin, ervoor om deze curve niet te gebruiken. De reden voor deze keuze is onbekend, maar sommigen geloven dat hij liever een alternatief zocht omdat de parameters van deze curve mogelijk een achterdeur zouden kunnen bevatten. In plaats daarvan gebruikt het Bitcoin protocol de standaard **_secp256k1_** curve. Deze curve wordt gedefinieerd door de parameters $a = 0$ en $b = 7$. De vergelijking is dus:


$$

y^2 = x^3 + 7


$$


De grafische voorstelling over het veld van reële getallen ziet er als volgt uit:


![CYP201](assets/fr/015.webp)


In cryptografie werken we echter met eindige verzamelingen getallen. Meer specifiek werken we met het eindige veld $\mathbb{F}_p$, dat het veld is van gehele getallen modulo een priemgetal $p$.

**Definitie**: Een priemgetal is een natuurlijk geheel getal groter dan of gelijk aan 2 dat slechts twee verschillende positieve gehele delers heeft: 1 en zichzelf. Bijvoorbeeld, het getal 7 is een priemgetal omdat het alleen door 1 en 7 gedeeld kan worden. Aan de andere kant is het getal 8 geen priemgetal omdat het kan worden gedeeld door 1, 2, 4 en 8.

In Bitcoin is het priemgetal $p$ dat gebruikt wordt om het eindige veld te definiëren erg groot. Het is zo gekozen dat de orde van het veld (d.w.z. het aantal Elements in $\mathbb{F}_p$) groot genoeg is om cryptografische veiligheid te garanderen.


Het gebruikte priemgetal $p$ is:


```text
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
```


In decimale notatie komt dit overeen met:


$$

p = 2^{256} - 2^{32} - 977


$$


De vergelijking van onze elliptische curve is dus eigenlijk:


$$

y^2 \equiv x^3 + 7 \mod p


$$


Aangezien deze kromme gedefinieerd is over het eindige veld $mathbb{F}_p$, lijkt hij niet langer op een continue kromme maar eerder op een discrete verzameling punten. Hier is bijvoorbeeld hoe de kromme gebruikt in Bitcoin eruit ziet voor een zeer kleine $p = 17$:


![CYP201](assets/fr/016.webp)


In dit voorbeeld heb ik het eindige veld opzettelijk beperkt tot $p = 17$ om educatieve redenen, maar je moet je voorstellen dat het veld dat in Bitcoin wordt gebruikt immens veel groter is, bijna $2^{256}$.


We gebruiken een eindig veld van gehele getallen modulo $p$ om de nauwkeurigheid van bewerkingen op de kromme te garanderen. Elliptische krommen over het veld van reële getallen zijn namelijk onderhevig aan onnauwkeurigheden door afrondingsfouten tijdens berekeningen. Als er veel bewerkingen op de kromme worden uitgevoerd, stapelen deze fouten zich op en kan het eindresultaat onjuist of moeilijk reproduceerbaar zijn. Het exclusieve gebruik van positieve gehele getallen zorgt voor een perfecte nauwkeurigheid van de berekeningen en dus reproduceerbaarheid van het resultaat.


De wiskunde van elliptische krommen over eindige velden is analoog aan die over het veld van reële getallen, met de aanpassing dat alle bewerkingen modulo $p$ worden uitgevoerd. Om de uitleg te vereenvoudigen zullen we in de volgende hoofdstukken de concepten illustreren aan de hand van een kromme gedefinieerd over reële getallen, terwijl we in gedachten houden dat de kromme in de praktijk gedefinieerd wordt over een eindig veld.


Als je meer wilt leren over de wiskundige grondslagen van moderne cryptografie, raad ik je ook aan deze andere cursus op Plan ₿ Network te raadplegen:


https://planb.network/courses/d2fd9fc0-d9ed-4a87-9fa3-0fdbb3937e28

## De openbare sleutel uit de privésleutel berekenen


<chapterId>fcb2bd58-5dda-5ecf-bb8f-ad1a0561ab4a</chapterId>

Zoals eerder gezien, zijn de digitale handtekening algoritmen in Bitcoin gebaseerd op een paar private en publieke sleutels die wiskundig aan elkaar gekoppeld zijn. Laten we samen onderzoeken wat deze wiskundige link is en hoe ze gegenereerd worden.


### De privésleutel


De privésleutel is eenvoudigweg een willekeurig of pseudo-willekeurig getal. In het geval van Bitcoin is dit getal 256 bits groot. Het aantal mogelijkheden voor een Bitcoin private sleutel is dus theoretisch $2^{256}$.


**Noot**: Een "pseudo-willekeurig getal" is een getal dat eigenschappen heeft die lijken op die van een echt willekeurig getal, maar gegenereerd wordt door een deterministisch algoritme.


In de praktijk zijn er echter maar $n$ verschillende punten op onze elliptische kromme secp256k1, waarbij $n$ de orde is van het generator punt $G$ van de kromme. We zullen later zien waar dit getal mee overeenkomt, maar onthoud gewoon dat een geldige privésleutel een geheel getal is tussen $1$ en $n-1$, wetende dat $n$ een getal is dat dicht bij maar iets minder dan $2^{256}$ ligt. Daarom zijn er enkele 256-bit getallen die niet geldig zijn om een private sleutel te worden in Bitcoin, meer bepaald alle getallen tussen $n$ en $2^{256}$. Als het genereren van het willekeurige getal (de privésleutel) een waarde $k$ oplevert zodanig dat $k \geq n$, dan wordt het als ongeldig beschouwd en moet er een nieuwe willekeurige waarde gegenereerd worden.


Het aantal mogelijkheden voor een Bitcoin privésleutel is dus ongeveer $n$, een getal dat in de buurt komt van $1,158 maal 10^{77}$. Dit aantal is zo groot dat als je willekeurig een privésleutel kiest, het statistisch gezien bijna onmogelijk is om op de privésleutel van een andere gebruiker terecht te komen. Om je een idee te geven van de schaal, het aantal mogelijke privésleutels in Bitcoin is van een orde van grootte die in de buurt komt van het geschatte aantal atomen in het waarneembare universum.


Zoals we in de komende hoofdstukken zullen zien, worden vandaag de dag de meeste private sleutels die gebruikt worden in Bitcoin niet willekeurig gegenereerd, maar zijn ze het resultaat van deterministische afleiding van een Mnemonic frase, zelf pseudo-willekeurig (dit is de beroemde frase van 12 of 24 woorden). Deze informatie verandert niets aan het gebruik van handtekeningalgoritmen zoals ECDSA, maar het helpt om onze popularisatie in Bitcoin te heroriënteren.


Voor de rest van de uitleg wordt de privésleutel aangeduid met de kleine letter $k$.


### De openbare sleutel


De openbare sleutel is een punt op de elliptische kromme, aangeduid met de hoofdletter $K$, en wordt berekend uit de privésleutel $k$. Dit punt $K$ wordt voorgesteld door een paar coördinaten $(x, y)$ op de elliptische kromme, waarbij elke coördinaat een geheel getal is modulo $p$, het priemgetal dat het eindige veld $mathbb{F}_p$ definieert.

In de praktijk wordt een ongecomprimeerde openbare sleutel weergegeven door 520 bits (of 65 bytes), wat overeenkomt met twee 256-bits getallen ($x$ en $y$) die achter elkaar zijn geplaatst, voorafgegaan door het 8-bits voorvoegsel $0x04$.


Het is echter ook mogelijk om de openbare sleutel in een gecomprimeerde vorm weer te geven met slechts 33 bytes (264 bits) door alleen de abscis $x$ van ons punt op de curve en een byte die de pariteit van $y$ aangeeft, te behouden. Dit staat bekend als een gecomprimeerde publieke sleutel. Ik zal hier meer over vertellen in de laatste hoofdstukken van deze training. Maar wat je moet onthouden is dat een publieke sleutel $K$ een punt is dat wordt beschreven door $x$ en $y$.


Om het punt $K$ te berekenen dat overeenkomt met onze publieke sleutel, gebruiken we de operatie van scalaire vermenigvuldiging op elliptische krommen, gedefinieerd als een herhaalde optelling ($k$ keer) van het generatorpunt $G$:


$$

K = k \cdot G


$$


waar:



- $k$ is de privésleutel (een willekeurig geheel getal tussen $1$ en $n-1$);
- $G$ is het generatorpunt van de elliptische curve die gebruikt wordt door alle deelnemers van het Bitcoin netwerk;
- $\cdot$ staat voor de scalaire vermenigvuldiging op de elliptische kromme, die gelijk is aan het optellen van het punt $G$ bij zichzelf $k$ keer.


Het feit dat dit punt $G$ gemeenschappelijk is voor alle publieke sleutels in Bitcoin laat ons toe er zeker van te zijn dat dezelfde private sleutel $k$ ons altijd dezelfde publieke sleutel $K$ zal geven:


![CYP201](assets/fr/017.webp)


Het belangrijkste kenmerk van deze operatie is dat het een eenrichtingsfunctie is. Het is gemakkelijk om de publieke sleutel $K$ te berekenen als je de private sleutel $k$ en het generator punt $G$ kent, maar het is praktisch onmogelijk om de private sleutel $k$ te berekenen als je alleen de publieke sleutel $K$ en het generator punt $G$ kent. Het vinden van $k$ uit $K$ en $G$ komt neer op het oplossen van het discrete logaritmeprobleem op elliptische krommen, een wiskundig moeilijk probleem waarvoor geen efficiënt algoritme bekend is. Zelfs de krachtigste huidige rekenmachines zijn niet in staat om dit probleem in een redelijke tijd op te lossen.


![CYP201](assets/fr/018.webp)


### Optellen en verdubbelen van punten op elliptische krommen


Het concept van optelling op elliptische krommen is meetkundig gedefinieerd. Als we twee punten $P$ en $Q$ op de kromme hebben, wordt de operatie $P + Q$ berekend door een lijn door $P$ en $Q$ te trekken. Deze lijn snijdt de kromme noodzakelijkerwijs in een derde punt $R'$. Vervolgens nemen we het spiegelbeeld van dit punt ten opzichte van de x-as om het punt $R$ te verkrijgen, dat het resultaat is van de optelling:


$$

P + Q = R


$$


Grafisch kan dit als volgt worden voorgesteld:


![CYP201](assets/fr/019.webp)


Voor de verdubbeling van een punt, dat is de bewerking $P + P$, tekenen we de raaklijn aan de kromme in het punt $P$. Deze raaklijn snijdt de kromme in een ander punt $S'$. We nemen dan het spiegelbeeld van dit punt ten opzichte van de x-as om het punt $S$ te verkrijgen, dat het resultaat is van de verdubbeling:


$$

2P = S


$$


Grafisch wordt dit weergegeven als:


![CYP201](assets/fr/020.webp)


Door deze optel- en verdubbelingsbewerkingen te gebruiken, kunnen we de scalaire vermenigvuldiging van een punt met een geheel getal $k$, aangeduid als $kP$, uitvoeren door herhaalde verdubbelingen en optellingen uit te voeren.


Stel bijvoorbeeld dat we een privésleutel $k = 4$ hebben gekozen. Om de bijbehorende openbare sleutel te berekenen, voeren we het volgende uit:


$$

K = k \cdot G = 4G


$$


Grafisch komt dit overeen met het uitvoeren van een reeks optellingen en verdubbelingen:



- Bereken $2G$ door $G$ te verdubbelen.
- Bereken $4G$ door $2G$ te verdubbelen.


![CYP201](assets/fr/021.webp)


Als we bijvoorbeeld het punt $3G$ willen berekenen, moeten we eerst het punt $2G$ berekenen door het punt $G$ te verdubbelen, en dan $G$ en $2G$ optellen. Om $G$ en $2G$ op te tellen, trek je gewoon de lijn die deze twee punten verbindt, zoek je het unieke punt $-3G$ op het snijpunt van deze lijn en de elliptische kromme, en bepaal je vervolgens $3G$ als het tegenovergestelde van $-3G$.


We hebben:


$$

G + G = 2G


$$


$$

2G + G = 3G


$$


Grafisch zou dit als volgt worden weergegeven:


![CYP201](assets/fr/022.webp)


### Eenrichtingsfunctie


Dankzij deze bewerkingen kunnen we begrijpen waarom het eenvoudig is om een openbare sleutel af te leiden uit een privésleutel, maar waarom het omgekeerde praktisch onmogelijk is.


Laten we teruggaan naar ons vereenvoudigde voorbeeld. Met een privésleutel $k = 4$. Om de bijbehorende openbare sleutel te berekenen, voeren we uit:


$$
K = k \cdot G = 4G
$$


We hebben dus gemakkelijk de openbare sleutel $K$ kunnen berekenen door $k$ en $G$ te kennen.


Als iemand alleen de openbare sleutel $K$ kent, wordt hij geconfronteerd met het discrete logaritmeprobleem: $k$ vinden zodat $K = k ≤ G$. Dit probleem wordt als moeilijk beschouwd omdat er geen efficiënt algoritme is om het op elliptische krommen op te lossen. Dit zorgt voor de veiligheid van de ECDSA- en Schnorr-algoritmen.


Natuurlijk zou het in dit vereenvoudigde voorbeeld met $k = 4$ mogelijk zijn om $k$ met vallen en opstaan te vinden, omdat het aantal mogelijkheden laag is. In de praktijk is $k$ echter een geheel getal van 256 bits, waardoor het aantal mogelijkheden astronomisch groot is (ongeveer $1,158 maal 10^{77}$). Daarom is het ondoenlijk om $k$ met brute kracht te vinden.


## Ondertekenen met de privésleutel


<chapterId>bb07826f-826e-5905-b307-3d82001fb778</chapterId>


Nu je weet hoe je een publieke sleutel kunt afleiden uit een privésleutel, kun je al bitcoins ontvangen door dit sleutelpaar te gebruiken als bestedingsvoorwaarde. Maar hoe kunt u ze uitgeven? Om bitcoins uit te geven, moet je de _scriptPubKey_ die aan je UTXO hangt ontgrendelen om te bewijzen dat je inderdaad de rechtmatige eigenaar ervan bent. Om dit te doen, moet je een handtekening $s$ produceren die overeenstemt met de publieke sleutel $K$ die aanwezig is in de _scriptPubKey_ door gebruik te maken van de private sleutel $k$ die initieel gebruikt werd om $K$ te berekenen. De digitale handtekening is dus een onweerlegbaar bewijs dat u in het bezit bent van de privésleutel die hoort bij de openbare sleutel die u claimt.


### Elliptische kromme parameters


Om een digitale handtekening uit te voeren, moeten alle deelnemers het eerst eens zijn over de parameters van de gebruikte elliptische curve. In het geval van Bitcoin zijn de parameters van **secp256k1** als volgt:


Het eindige veld $\mathbb{Z}_p$ gedefinieerd door:


$$
p = 2^{256} - 2^{32} - 977
$$


```text
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
```


$p$ is een heel groot priemgetal iets minder dan $2^{256}$.


De elliptische kromme $y^2 = x^3 + ax + b$ over $\mathbb{Z}_p$ gedefinieerd door:


$$
a = 0, \quad b = 7
$$


Het generatorpunt of oorsprongspunt $G$:


```text
G = 0x0279BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
```


Dit getal is de gecomprimeerde vorm die alleen de abscis van het punt $G$ geeft. Het voorvoegsel `02` aan het begin bepaalt welke van de twee waarden met deze abscis $x$ gebruikt moet worden als voortbrengend punt.

De orde $n$ van $G$ (het aantal bestaande punten) en de cofactor $h$:


```text
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
```


$n$ is een heel groot getal dat iets kleiner is dan $p$.


$$
h=1
$$


$h$ is de cofactor of het aantal subgroepen. Ik zal hier niet uitweiden over wat dit voorstelt, omdat het vrij complex is, en in het geval van Bitcoin hoeven we er geen rekening mee te houden omdat het gelijk is aan $1$.


Al deze informatie is openbaar en bekend bij alle deelnemers. Dankzij hen kunnen gebruikers een digitale handtekening maken en deze verifiëren.


### Handtekening met ECDSA


Met het ECDSA-algoritme kan een gebruiker een bericht ondertekenen met zijn privé-sleutel, op zo'n manier dat iedereen die de corresponderende publieke sleutel kent de geldigheid van de handtekening kan verifiëren, zonder dat de privé-sleutel ooit onthuld wordt. In de context van Bitcoin hangt het te ondertekenen bericht af van de _sighash_ gekozen door de gebruiker. Het is deze _sighash_ die bepaalt welke delen van de transactie gedekt worden door de handtekening. Ik zal hier meer over vertellen in het volgende hoofdstuk.


Hier zijn de stappen om generate een ECDSA handtekening te geven:


Eerst berekenen we de Hash ($e$) van het bericht dat ondertekend moet worden. Het bericht $m$ wordt dus door een cryptografische Hash functie gehaald, meestal SHA256 of dubbel SHA256 in het geval van Bitcoin:


$$
e = \text{HASH}(m)
$$


Vervolgens berekenen we een Nonce. In cryptografie is een Nonce gewoon een getal dat willekeurig of pseudo-willekeurig gegenereerd wordt en slechts één keer gebruikt wordt. Dat wil zeggen, elke keer dat er een nieuwe digitale handtekening wordt gemaakt met dit sleutelpaar, is het erg belangrijk om een andere Nonce te gebruiken, anders zal dit de veiligheid van de private sleutel in gevaar brengen. Het is daarom voldoende om een willekeurig en uniek geheel getal $r$ te bepalen zodat $1 \leq r \leq n-1$, waarbij $n$ de orde is van het voortbrengende punt $G$ van de elliptische curve.


Dan berekenen we het punt $R$ op de elliptische kromme met de coördinaten $(x_R, y_R)$ zo dat:


$$
R = r \cdot G
$$


We extraheren de waarde van de abscis van het punt $R$ ($x_R$). Deze waarde vertegenwoordigt het eerste deel van de handtekening. Tot slot berekenen we het tweede deel van de handtekening $s$ op deze manier:


$$
s = r^{-1} \left( e + k \cdot x_R \right) \mod n
$$


waar:



- $r^{-1}$ is de modulaire inverse van $r$ modulo $n$, dat wil zeggen, een geheel getal zo dat $r \dot r^{-1} \equiv 1 mod n$;
- $k$ is de privésleutel van de gebruiker;
- $e$ is de Hash van het bericht;
- $n$ is de orde van het generator punt $G$ van de elliptische kromme.


De handtekening is dan gewoon de aaneenschakeling van $x_R$ en $s$:


$$
\text{SIG} = x_R \Vert s
$$


### Verificatie van de ECDSA-handtekening


Om een handtekening $(x_R, s)$ te verifiëren, kan iedereen die de openbare sleutel $K$ en de parameters van de elliptische curve kent, op deze manier te werk gaan:


Controleer eerst of $x_R$ en $s$ binnen het interval $[1, n-1]$ liggen. Dit zorgt ervoor dat de handtekening de wiskundige beperkingen van de elliptische groep respecteert. Als dit niet het geval is, verwerpt de verificateur de handtekening onmiddellijk als ongeldig.


Bereken dan de Hash van het bericht:


$$
e = \text{HASH}(m)
$$


Bereken de modulaire inverse van $s$ modulo $n$:


$$
s^{-1} \mod n
$$


Bereken op deze manier twee scalaire waarden $u_1$ en $u_2$:


$$
\begin{align*}
u_1 &= e \cdot s^{-1} \mod n \\
u_2 &= x_R \cdot s^{-1} \mod n
\end{align*}
$$


En bereken tenslotte het punt $V$ op de elliptische kromme zodat:


$$
V = u_1 \cdot G + u_2 \cdot K
$$


De signatuur is alleen geldig als $x_V \equiv x_R \mod n$, waarbij $x_V$ de $x$ coördinaat van het punt $V$ is. Door het combineren van $u_1 \cdot G$ en $u_2 \cdot K$ verkrijgt men immers een punt $V$ dat, indien de signatuur geldig is, moet corresponderen met het punt $R$ gebruikt tijdens de signatuur (modulo $n$).


### Handtekening met het Schnorr-protocol


Het Schnorr handtekeningschema is een alternatief voor ECDSA dat veel voordelen biedt. Het is sinds 2021 en de introductie van Taproot mogelijk om het te gebruiken in Bitcoin, met de P2TR scriptpatronen. Net als ECDSA maakt het Schnorr-schema het mogelijk om een bericht te ondertekenen met een privésleutel, op zo'n manier dat de handtekening geverifieerd kan worden door iedereen die de corresponderende publieke sleutel kent.

In het geval van Schnorr wordt exact dezelfde curve als ECDSA gebruikt met dezelfde parameters. De publieke sleutels worden echter iets anders voorgesteld dan bij ECDSA. Ze worden namelijk alleen aangeduid door de $x$ coördinaat van het punt op de elliptische curve. In tegenstelling tot ECDSA, waar gecomprimeerde publieke sleutels worden voorgesteld door 33 bytes (met de prefixbyte die de pariteit van $y$ aangeeft), gebruikt Schnorr publieke sleutels van 32 bytes, die enkel overeenkomen met de $x$ coördinaat van het punt $K$, en er wordt aangenomen dat $y$ standaard even is. Deze vereenvoudigde weergave vermindert de grootte van de handtekeningen en vergemakkelijkt bepaalde optimalisaties in de verificatiealgoritmen.

De publieke sleutel is dan de $x$ coördinaat van het punt $K$:


$$
\text{pk} = K_x
$$


De eerste stap naar generate een handtekening is Hash het bericht. Maar in tegenstelling tot ECDSA wordt dit gedaan met andere waarden en wordt een gelabelde Hash functie gebruikt om botsingen in verschillende contexten te voorkomen. Bij een gelabelde Hash functie wordt eenvoudigweg een willekeurig label toegevoegd aan de Hash functieingangen naast de berichtgegevens.


![CYP201](assets/fr/023.webp)


Naast het bericht worden ook de $x$ coördinaat van de publieke sleutel $K_x$, en het punt $R = r \cdot G$, berekend uit de Nonce $r$ (die zelf een uniek geheel getal is voor elke handtekening, deterministisch berekend uit de private sleutel en het bericht om kwetsbaarheden gerelateerd aan hergebruik van Nonce te voorkomen), doorgegeven aan de gelabelde functie. Net als voor de publieke sleutel wordt alleen de $x$ coördinaat van het Nonce punt $R_x$ behouden om het punt te beschrijven.


Het resultaat van deze hashing genoteerd $e$ wordt de "uitdaging" genoemd:


$$
e = \text{HASH}(\text{``BIP0340/challenge''}, R_x \Vert K_x \Vert m) \mod n
$$


Hier is $\text{Hash}$ de SHA256 Hash functie en $\text{`BIP0340/challenge''}$ de specifieke tag voor het hashen.


Tenslotte wordt de parameter $s$ als volgt berekend uit de privésleutel $k$, de Nonce $r$ en de uitdaging $e$:


$$
s = (r + e \cdot k) \mod n
$$


De handtekening is dan gewoon het paar $R_x$ en $s$.


$$
\text{SIG} = R_x \Vert s
$$


### Verificatie van de Schnorr-handtekening


De verificatie van een Schnorr handtekening is eenvoudiger dan die van een ECDSA handtekening. Hier zijn de stappen om de handtekening $(R_x, s)$ met de openbare sleutel $K_x$ en het bericht $m$ te verifiëren.

Eerst controleren we of $K_x$ een geldig geheel getal is kleiner dan $p$. Als dit het geval is, vinden we het overeenkomstige punt op de kromme waarbij $K_y$ even is. We extraheren ook $R_x$ en $s$ door de handtekening $\text{SIG}$ te splitsen. Daarna controleren we of $R_x < p$ en $s < n$ (de volgorde van de kromme).

Vervolgens berekenen we de uitdaging $e$ op dezelfde manier als de uitgever van de handtekening:


$$
e = \text{HASH}(\text{``BIP0340/challenge''}, R_x \Vert K_x \Vert m) \mod n
$$


Vervolgens berekenen we op deze manier een referentiepunt op de curve:


$$
R' = s \cdot G - e \cdot K
$$


Tot slot controleren we of $R'_x = R_x$. Als de twee x-coördinaten overeenkomen, dan is de handtekening $(R_x, s)$ inderdaad geldig met de openbare sleutel $K_x$.


### Waarom werkt dit?


De ondertekenaar heeft berekend $s = r + e ‛ k ‛mod n$, dus $R' = s ‛ G - e ↪Pi_201 K$ moet gelijk zijn aan het oorspronkelijke punt $R$, want:


$$
s \cdot G = (r + e \cdot k) \cdot G = r \cdot G + e \cdot k \cdot G
$$


Omdat $K = k \dot G$ hebben we $e \dot k \dot G = e \dot K$. Dus:


$$
R' = r \cdot G = R
$$


Daarom hebben we:


$$
R'_x = R_x
$$


### De voordelen van Schnorr-handtekeningen


Het Schnorr handtekeningschema biedt verschillende voordelen voor Bitcoin ten opzichte van het originele ECDSA algoritme. Ten eerste staat Schnorr de aggregatie van sleutels en handtekeningen toe. Dit betekent dat meerdere publieke sleutels gecombineerd kunnen worden tot één enkele sleutel.


![CYP201](assets/fr/024.webp)


Op dezelfde manier kunnen meerdere handtekeningen worden samengevoegd tot één geldige handtekening. Dus, in het geval van een transactie met meerdere handtekeningen, kan een groep deelnemers ondertekenen met een enkele handtekening en een enkele geaggregeerde openbare sleutel. Dit vermindert de opslag- en rekenkosten voor het netwerk aanzienlijk, omdat elk knooppunt slechts één handtekening hoeft te verifiëren.


![CYP201](assets/fr/025.webp)


Bovendien verbetert handtekeningaggregatie de privacy. Met Schnorr wordt het onmogelijk om een transactie met meerdere handtekeningen te onderscheiden van een standaard transactie met één handtekening. Deze homogeniteit maakt ketenanalyse moeilijker, omdat het de mogelijkheid om Wallet vingerafdrukken te identificeren beperkt.


Tot slot biedt Schnorr ook de mogelijkheid van batchverificatie. Door meerdere handtekeningen tegelijkertijd te verifiëren, kunnen nodes efficiënter werken, vooral voor blokken die veel transacties bevatten. Deze optimalisatie vermindert de tijd en middelen die nodig zijn om een blok te valideren.

Schnorr-handtekeningen zijn ook niet vervormbaar, in tegenstelling tot handtekeningen die geproduceerd worden met ECDSA. Dit betekent dat een aanvaller een geldige handtekening niet kan wijzigen om een andere geldige handtekening te maken voor hetzelfde bericht en dezelfde openbare sleutel. Deze kwetsbaarheid was eerder aanwezig in Bitcoin en verhinderde met name de veilige implementatie van Lightning Network. Het werd opgelost voor ECDSA met de SegWit softfork in 2017, waarbij de handtekeningen worden verplaatst naar een aparte database van de transacties om hun vervalsbaarheid te voorkomen.


### Waarom koos Satoshi voor ECDSA?


Zoals we gezien hebben, koos Satoshi er in eerste instantie voor om ECDSA te implementeren voor digitale handtekeningen in Bitcoin. We hebben echter ook gezien dat Schnorr in veel opzichten superieur is aan ECDSA, en dit protocol werd gecreëerd door Claus-Peter Schnorr in 1989, 20 jaar voor de uitvinding van Bitcoin.


Nou, we weten niet echt waarom Satoshi er niet voor koos, maar een waarschijnlijke hypothese is dat dit protocol tot 2008 gepatenteerd was. Hoewel Bitcoin een jaar later werd gemaakt, in januari 2009, was er op dat moment nog geen open-source standaardisatie voor Schnorr handtekeningen beschikbaar. Misschien vond Satoshi het veiliger om ECDSA te gebruiken, dat al veel gebruikt en getest werd in open-source software en verschillende erkende implementaties had (met name de OpenSSL library die tot 2015 gebruikt werd in Bitcoin Core, daarna vervangen door libsecp256k1 in versie 0.10.0). Of misschien was hij zich er gewoon niet van bewust dat dit patent in 2008 zou verlopen. In ieder geval lijkt de meest waarschijnlijke hypothese gerelateerd aan dit patent en het feit dat ECDSA een bewezen geschiedenis had en gemakkelijker te implementeren was.


## De sighashvlaggen


<chapterId>231c41a2-aff2-4655-9048-47b6d2d83d64</chapterId>


Zoals we in vorige hoofdstukken hebben gezien, worden digitale handtekeningen vaak gebruikt om het script van een invoer te ontsluiten. In het ondertekeningsproces is het noodzakelijk om de ondertekende gegevens in de berekening op te nemen, in onze voorbeelden aangeduid met het bericht $m$. Deze gegevens kunnen, eenmaal ondertekend, niet worden gewijzigd zonder de handtekening ongeldig te maken. Inderdaad, of het nu voor ECDSA of Schnorr is, de verificateur van de handtekening moet hetzelfde bericht $m$ in zijn berekening opnemen. Als het verschilt van het bericht $m$ dat aanvankelijk door de ondertekenaar werd gebruikt, zal het resultaat onjuist zijn en wordt de handtekening ongeldig geacht. Er wordt dan gezegd dat een handtekening bepaalde gegevens afdekt en op een bepaalde manier beschermt tegen ongeoorloofde wijzigingen.


### Wat is een sighashvlag?


In het specifieke geval van Bitcoin hebben we gezien dat het bericht $m$ overeenkomt met de transactie. In werkelijkheid is het echter een beetje complexer. Dankzij sighash-flags is het namelijk mogelijk om specifieke gegevens binnen de transactie te selecteren die wel of niet gedekt worden door de handtekening.

De "sighash flag" is dus een parameter die aan elke ingang wordt toegevoegd, zodat kan worden bepaald welke onderdelen van een transactie onder de bijbehorende handtekening vallen. Deze componenten zijn de ingangen en de uitgangen. De keuze van de sighash flag bepaalt dus welke inputs en welke outputs van de transactie vastliggen in de handtekening en welke nog gewijzigd kunnen worden zonder deze ongeldig te maken. Met dit mechanisme kunnen handtekeningen transactiegegevens vastleggen volgens de bedoelingen van de ondertekenaar.


Het is duidelijk dat zodra de transactie bevestigd is op de Blockchain, deze onveranderbaar wordt, ongeacht de gebruikte sighash vlaggen. De mogelijkheid van wijziging via de sighash vlaggen is beperkt tot de periode tussen het ondertekenen en de bevestiging.


Over het algemeen biedt de Wallet software u niet de mogelijkheid om handmatig de sighash flag van uw invoer te wijzigen wanneer u een transactie aanmaakt. Standaard is `SIGHASH_ALL` ingesteld. Persoonlijk ken ik alleen Sparrow wallet die deze wijziging toestaat van de gebruiker Interface.


### Wat zijn de bestaande sighash-vlaggen in Bitcoin?


In Bitcoin zijn er eerst en vooral 3 basis sighash-vlaggen:



- `SIGHASH_ALL` (`0x01`): De handtekening geldt voor alle ingangen en alle uitgangen van de transactie. De transactie wordt dus volledig gedekt door de handtekening en kan niet meer gewijzigd worden. `SIGHASH_ALL` is de meest gebruikte sighash in alledaagse transacties als men gewoon een transactie wil maken zonder dat deze gewijzigd kan worden.


![CYP201](assets/fr/026.webp)


In alle diagrammen van dit hoofdstuk staat de oranje kleur voor de Elements die onder de signatuur valt, terwijl de zwarte kleur aangeeft welke dat niet zijn.



- `SIGHASH_NONE` (`0x02`): De handtekening dekt alle ingangen maar geen van de uitgangen, waardoor de uitgangen na de handtekening gewijzigd kunnen worden. Concreet lijkt dit op een blanco cheque. De ondertekenaar ontgrendelt de UTXO's in de ingangen, maar laat het veld van de uitgangen volledig wijzigbaar. Iedereen die op de hoogte is van deze transactie kan dus de output van zijn keuze toevoegen, bijvoorbeeld door een ontvangende Address op te geven om het geld te innen dat verbruikt is door de inputs, en vervolgens de transactie uit te zenden om de bitcoins terug te krijgen. De handtekening van de eigenaar van de inputs wordt niet ongeldig gemaakt, omdat deze alleen betrekking heeft op de inputs.


![CYP201](assets/fr/027.webp)



- `SIGHASH_SINGLE` (`0x03`): De handtekening dekt alle ingangen en een enkele uitvoer, die overeenkomt met de index van de ondertekende invoer. Als de handtekening bijvoorbeeld de _scriptPubKey_ van ingang #0 ontgrendelt, dan dekt het ook uitvoer #0. De handtekening beschermt ook alle andere ingangen, die niet meer gewijzigd kunnen worden. Iedereen kan echter een extra uitvoer toevoegen zonder de handtekening ongeldig te maken, op voorwaarde dat uitvoer #0, de enige die door de handtekening wordt gedekt, niet wordt gewijzigd.


![CYP201](assets/fr/028.webp)


Naast deze drie sighash vlaggen is er ook de modifier `SIGHASH_ANYONECANPAY` (`0x80`). Deze modifier kan gecombineerd worden met een basis sighash vlag om drie nieuwe sighash vlaggen te maken:



- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): De handtekening heeft betrekking op een enkele invoer en omvat alle uitgangen van de transactie. Deze gecombineerde sighash flag maakt het bijvoorbeeld mogelijk om een crowdfundingtransactie aan te maken. De organisator bereidt de output voor met zijn Address en het doelbedrag, en elke investeerder kan dan inputs toevoegen om deze output te financieren. Zodra er voldoende inputs zijn verzameld om de output te financieren, kan de transactie worden uitgezonden.


![CYP201](assets/fr/029.webp)



- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): De handtekening heeft betrekking op een enkele invoer, zonder zich vast te leggen op een uitvoer;


![CYP201](assets/fr/030.webp)



- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): De handtekening dekt een enkele invoer evenals de uitvoer die dezelfde index heeft als deze invoer. Als de handtekening bijvoorbeeld de _scriptPubKey_ van invoer #3 ontgrendelt, zal deze ook uitvoer #3 dekken. De rest van de transactie blijft wijzigbaar, zowel wat betreft andere ingangen als andere uitgangen.


![CYP201](assets/fr/031.webp)


### Projecten om nieuwe Sighash-vlaggen toe te voegen


Op dit moment (2024) zijn alleen de sighash vlaggen uit de vorige sectie bruikbaar in Bitcoin. Sommige projecten overwegen echter de toevoeging van nieuwe sighash vlaggen. Bijvoorbeeld, BIP118, voorgesteld door Christian Decker en Anthony Towns, introduceert twee nieuwe sighash vlaggen: `SIGHASH_ANYPREVOUT` en `SIGHASH_ANYPREVOUTANYSCRIPT` (_AnyPrevOut = "Any Previous Output"_).


Deze twee sighash vlaggen zouden een extra mogelijkheid bieden in Bitcoin: het maken van handtekeningen die geen enkele specifieke invoer van de transactie dekken.


![CYP201](assets/fr/032.webp)


Dit idee werd oorspronkelijk geformuleerd door Joseph Poon en Thaddeus Dryja in het Lightning White Paper. Voordat deze vlag werd hernoemd, heette hij `SIGHASH_NOINPUT`.

Als deze sighash flag wordt geïntegreerd in Bitcoin, zal het het gebruik van convenanten mogelijk maken, maar het is ook een verplichte voorwaarde voor het implementeren van Eltoo, een algemeen protocol voor tweede lagen dat definieert hoe de Ownership van een UTXO gezamenlijk beheerd moet worden. Eltoo is specifiek ontworpen om de problemen op te lossen die samenhangen met de mechanismen voor het onderhandelen over de toestand van Lightning-kanalen, dat wil zeggen tussen openen en sluiten.


Om je kennis van de Lightning Network te verdiepen, raad ik je na de CYP201 cursus van harte de LNP201 cursus van Fanis Michalakis aan, die het onderwerp in detail behandelt:


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

In het volgende deel stel ik voor om te ontdekken hoe de Mnemonic frase aan de basis van je Bitcoin Wallet werkt.


# De Mnemonic zin


<partId>4070af16-c8a2-58b5-9871-a22c86c07458</partId>


## Evolutie van Bitcoin-portefeuilles


<chapterId>9d9acd5d-a0e5-5dfd-b544-f043fae8840f</chapterId>


Nu we de werking van Hash functies en digitale handtekeningen hebben onderzocht, kunnen we bestuderen hoe Bitcoin wallets functioneren. Het doel is te beschrijven hoe een Wallet in Bitcoin opgebouwd is, hoe het gedecomponeerd is en waar de verschillende stukjes informatie waaruit het bestaat voor gebruikt worden. Dit begrip van de Wallet mechanismen zal je in staat stellen om je gebruik van Bitcoin te verbeteren op het gebied van veiligheid en privacy.


Voordat we in de technische details duiken, is het essentieel om te verduidelijken wat bedoeld wordt met "Bitcoin Wallet" en om het nut ervan te begrijpen.


### Wat is een Bitcoin Wallet?


In tegenstelling tot traditionele portemonnees, die het mogelijk maken om fysieke biljetten en munten op te slaan, "bevat" een Bitcoin Wallet niet per se bitcoins. Bitcoins bestaan namelijk niet in een fysieke of digitale vorm die kan worden opgeslagen, maar worden vertegenwoordigd door rekeneenheden die in het Bitcoin systeem worden weergegeven in de vorm van **UTXO's** (_Unspent Transaction Outputs_).


UTXO's vertegenwoordigen dus fragmenten van bitcoins, van verschillende groottes, die kunnen worden uitgegeven op voorwaarde dat aan hun _scriptPubKey_ is voldaan. Om zijn bitcoins uit te geven, moet een gebruiker een _scriptSig_ leveren die de _scriptPubKey_ ontsluit die geassocieerd is met zijn UTXO. Dit bewijs wordt meestal geleverd door middel van een digitale handtekening. Dit bewijs wordt meestal geleverd door middel van een digitale handtekening, gegenereerd uit de private sleutel die overeenkomt met de publieke sleutel in de _scriptPubKey_. Het cruciale element dat de gebruiker moet beveiligen is dus de private sleutel.

De rol van een Bitcoin Wallet is juist om deze private sleutels veilig te beheren. In werkelijkheid lijkt zijn rol meer op die van een sleutelhanger dan op die van een Wallet in de traditionele zin.


### JBOK Portemonnees


De eerste wallets die gebruikt werden in Bitcoin waren JBOK (_Just a Bunch Of Keys_) wallets, die privé-sleutels groepeerden die onafhankelijk van elkaar gegenereerd waren, zonder enig verband ertussen. Deze wallets werkten volgens een eenvoudig model waarbij elke private sleutel een unieke Bitcoin kon ontgrendelen die Address ontving.


![CYP201](assets/fr/033.webp)


Als men meerdere privésleutels wilde gebruiken, was het nodig om evenzoveel back-ups te maken om toegang tot fondsen te garanderen in geval van problemen met het apparaat waarop de Wallet staat. Als men één enkele private sleutel gebruikt, kan deze Wallet structuur volstaan, aangezien één back-up voldoende is. Dit levert echter een probleem op: in Bitcoin wordt het sterk afgeraden om steeds dezelfde private sleutel te gebruiken. Een private sleutel is namelijk geassocieerd met een unieke Address, en Bitcoin ontvangstadressen zijn normaal ontworpen voor eenmalig gebruik. Elke keer dat je geld ontvangt, moet je generate een nieuwe lege Address aanmaken.


Deze beperking komt voort uit het privacymodel van Bitcoin. Door dezelfde Address te hergebruiken, wordt het voor externe waarnemers gemakkelijker om Bitcoin transacties te traceren. Daarom wordt het hergebruiken van een ontvangende Address sterk afgeraden. Echter, om meerdere adressen te hebben en onze transacties publiekelijk te scheiden, is het noodzakelijk om meerdere privésleutels te beheren. In het geval van JBOK wallets betekent dit dat er evenveel back-ups moeten worden gemaakt als er nieuwe sleutelparen zijn, een taak die snel complex en moeilijk te onderhouden kan worden voor gebruikers.


Om meer te leren over het privacymodel van Bitcoin en methodes te ontdekken om je privacy te beschermen, raad ik je ook aan om mijn BTC204-cursus over Plan ₿ Network te volgen:


https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### HD Portemonnees


Om Address de beperking van JBOK wallets op te heffen, werd vervolgens een nieuwe Wallet structuur gebruikt. In 2012 stelde Pieter Wuille een verbetering voor met BIP32, die HD (Hierarchical Deterministic) wallets introduceerde. Het principe van een HD Wallet is om alle private sleutels af te leiden uit één enkele informatiebron, een seed genaamd, op een deterministische en hiërarchische manier. Deze seed wordt willekeurig gegenereerd wanneer de Wallet wordt aangemaakt en vormt een unieke back-up waarmee alle privésleutels van de Wallet opnieuw kunnen worden aangemaakt. De gebruiker kan dus generate een zeer groot aantal privésleutels aanmaken om Address hergebruik te voorkomen en zijn privacy te bewaren, terwijl hij slechts één back-up van zijn Wallet hoeft te maken via de seed.


![CYP201](assets/fr/034.webp)


In HD wallets wordt de sleutelafleiding uitgevoerd volgens een hiërarchische structuur die het mogelijk maakt om sleutels te organiseren in afleidingsdeelruimten, waarbij elke deelruimte verder onderverdeeld kan worden, om het beheer van fondsen en de interoperabiliteit tussen verschillende Wallet software te vergemakkelijken. Tegenwoordig wordt deze standaard aangenomen door de overgrote meerderheid van de Bitcoin gebruikers. Daarom zullen we het in detail onderzoeken in de volgende hoofdstukken.


### De BIP39-standaard: De Mnemonic zin


In aanvulling op BIP32, standaardiseert BIP39 het seed formaat als een Mnemonic zin, om back-up en leesbaarheid voor gebruikers te vergemakkelijken. De Mnemonic frase, ook wel herstelfrase of 24-woord frase genoemd, is een reeks woorden uit een voorgedefinieerde lijst die de Wallet's seed veilig codeert.


De Mnemonic-zin vereenvoudigt het maken van back-ups voor de gebruiker enorm. In geval van verlies, beschadiging of diefstal van het apparaat waarop de Wallet staat, kan de Wallet eenvoudigweg worden hersteld met behulp van deze Mnemonic-zin en kan de toegang tot alle fondsen die erdoor zijn beveiligd, worden hersteld.


In de komende hoofdstukken zullen we de interne werking van HD wallets onderzoeken, inclusief sleutelafleidingsmechanismen en de verschillende mogelijke hiërarchische structuren. Dit zal je toelaten om de cryptografische fundamenten waarop de veiligheid van fondsen in Bitcoin gebaseerd is, beter te begrijpen. En om te beginnen stel ik voor om in het volgende hoofdstuk de rol van entropie aan de basis van je Wallet te ontdekken.


## Entropie en willekeurige getallen


<chapterId>b43c715d-affb-56d8-a697-ad5bc2fffd63</chapterId>

Moderne HD wallets vertrouwen op een enkel initieel stukje informatie genaamd "entropie" om deterministisch generate de hele set Wallet sleutels te maken. Deze entropie is een pseudo-willekeurig getal dat deels de veiligheid van de Wallet bepaalt.


### Definitie van Entropie


Entropie, in de context van cryptografie en informatie, is een kwantitatieve maat voor de onzekerheid of onvoorspelbaarheid geassocieerd met een gegevensbron of een willekeurig proces. Entropie speelt een belangrijke rol in de veiligheid van cryptografische systemen, vooral bij het genereren van sleutels en willekeurige getallen. Een hoge entropie zorgt ervoor dat de gegenereerde sleutels voldoende onvoorspelbaar zijn en bestand tegen brute kracht aanvallen, waarbij een aanvaller alle mogelijke combinaties probeert om de sleutel te raden.


In de context van Bitcoin wordt entropie gebruikt om generate de seed te maken. Bij het creëren van een HD Wallet, wordt de Mnemonic zin geconstrueerd uit een willekeurig getal, zelf afgeleid van een entropiebron. De zin wordt dan gebruikt om meerdere private sleutels generate te maken, op een deterministische en hiërarchische manier, om bestedingsvoorwaarden voor UTXO's te creëren.


### Methoden voor het genereren van entropie


De initiële entropie die gebruikt wordt voor een HD Wallet is over het algemeen 128 bits of 256 bits, waarbij:



- 128 bits entropie komen overeen met een Mnemonic zin van **12 woorden**;
- 256 bits entropie komen overeen met een Mnemonic zin van **24 woorden**.


In de meeste gevallen wordt dit willekeurige getal automatisch gegenereerd door de Wallet software met behulp van een PRNG (_Pseudo-Random Number Generator_). PRNGs zijn een categorie algoritmes die gebruikt worden om generate getallenreeksen te genereren vanuit een initiële toestand, die kenmerken hebben die lijken op die van een willekeurig getal, zonder er daadwerkelijk één te zijn. Een goede PRNG moet eigenschappen hebben zoals eenvormige uitvoer, onvoorspelbaarheid en weerstand tegen voorspellende aanvallen. In tegenstelling tot True Random Number Generators (TRNGs), zijn PRNGs deterministisch en reproduceerbaar.


![CYP201](assets/fr/035.webp)


Een alternatief is om handmatig generate de entropie te genereren, wat een betere controle biedt, maar ook veel riskanter is. Ik raad ten zeerste af om zelf de entropie voor je HD Wallet te genereren.


In het volgende hoofdstuk zullen we zien hoe we van een willekeurig getal naar een Mnemonic zin van 12 of 24 woorden gaan.


## De Mnemonic zin


<chapterId>8f9340c1-e6dc-5557-a2f2-26c9669987d5</chapterId>

De Mnemonic frase, ook wel "seed frase", "herstelfrase", "geheime frase", of "24-woord frase" genoemd, is een reeks die meestal bestaat uit 12 of 24 woorden, die gegenereerd wordt uit entropie. Deze wordt gebruikt om deterministisch alle sleutels van een HD Wallet af te leiden. Dit betekent dat het mogelijk is om uit deze zin op deterministische wijze generate alle private en publieke sleutels van de Bitcoin Wallet te recreëren en dus toegang te krijgen tot de fondsen die ermee beschermd zijn. Het doel van de Mnemonic-zin is om een veilige en gebruiksvriendelijke manier te bieden voor back-up en herstel van bitcoins. Het werd in 2013 geïntroduceerd met de BIP39 standaard.


Laten we samen ontdekken hoe we van entropie naar een Mnemonic zin kunnen gaan.


### De controlesom


Om entropie om te zetten in een Mnemonic zin, moet men eerst een controlesom (of "controlesom") toevoegen aan het einde van de entropie. Deze controlesom is een korte reeks bits die de integriteit van de gegevens garandeert door te verifiëren dat er geen toevallige wijzigingen zijn aangebracht.


Om de controlesom te berekenen wordt de SHA256 Hash functie toegepast op de entropie (slechts één keer; dit is één van de zeldzame gevallen in Bitcoin waar een enkele SHA256 Hash wordt gebruikt in plaats van een dubbele Hash). Deze bewerking produceert een 256-bit Hash. De controlesom bestaat uit de eerste bits van deze Hash, en de lengte hangt af van die van de entropie, volgens de volgende formule:


$$
\text{CS} = \frac{\text{ENT}}{32}
$$


waarbij ${ENT}$ staat voor de lengte van de entropie in bits en ${CS}$ voor de lengte van de controlesom in bits.


Bijvoorbeeld, voor een entropie van 256 bits, worden de eerste 8 bits van de Hash genomen om de controlesom te vormen:


$$
\text{CS} = \frac{256}{32} = 8 \text{ bits}
$$


Nadat de controlesom is berekend, wordt deze samengevoegd met de entropie om een uitgebreide bitreeks te verkrijgen die wordt aangeduid met ${ENT} \Vert \text{CS}$ ("aaneenschakelen" betekent aaneenschakelen).


![CYP201](assets/fr/036.webp)


### Correspondentie tussen de Entropie en de Mnemonic zin


Het aantal woorden in de Mnemonic zin hangt af van de grootte van de initiële entropie, zoals geïllustreerd in de volgende tabel met:



- $text{ENT}$: de grootte in bits van de entropie;
- $text{CS}$: de grootte in bits van de controlesom;
- $w$: het aantal woorden in de uiteindelijke Mnemonic zin.


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


Bijvoorbeeld, voor een entropie van 256 bits is het resultaat ${ENT} \264 bits en levert een Mnemonic zin van 24 woorden op.


### Conversie van de binaire sequentie in een Mnemonic zin


De bitreeks ${ENT} \wordt dan verdeeld in segmenten van 11 bits. Elk 11-bits segment komt, na omzetting naar decimaal, overeen met een getal tussen 0 en 2047, dat de positie van een woord aangeeft [in een lijst van 2048 woorden gestandaardiseerd door BIP39] (https://github.com/Planb-Network/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf).


![CYP201](assets/fr/037.webp)


Bijvoorbeeld, voor een 128-bits entropie is de controlesom 4 bits, en dus meet de totale reeks 132 bits. Het is verdeeld in 12 segmenten van 11 bits (de oranje bits geven de controlesom aan):


![CYP201](assets/fr/038.webp)


Elk segment wordt dan omgezet in een decimaal getal dat een woord in de lijst voorstelt. Bijvoorbeeld, het binaire segment `01011010001` is in decimaal gelijk aan `721`. Door 1 toe te voegen om op één lijn te komen met de indexering van de lijst (die begint bij 1 en niet bij 0), geeft dit de woordrang `722`, wat "_focus_" in de lijst is.


![CYP201](assets/fr/039.webp)


Deze correspondentie wordt herhaald voor elk van de 12 segmenten om een woordgroep van 12 woorden te verkrijgen.


![CYP201](assets/fr/040.webp)


### Kenmerken van de BIP39-woordenlijst


Een bijzonderheid van de BIP39-woordenlijst is dat geen enkel woord dezelfde eerste vier letters in dezelfde volgorde deelt met een ander woord. Dit betekent dat het opschrijven van alleen de eerste vier letters van elk woord voldoende is om de Mnemonic zin op te slaan. Dit kan interessant zijn om ruimte te besparen, vooral voor wie het op een metalen drager wil graveren.


Deze lijst van 2048 woorden bestaat in verschillende talen. Dit zijn geen eenvoudige vertalingen, maar aparte woorden voor elke taal. Het wordt echter sterk aangeraden om de Engelse versie te gebruiken, omdat versies in andere talen over het algemeen niet worden ondersteund door de Wallet software.


### Welke lengte moet je kiezen voor je Mnemonic zin?


Om de optimale lengte van uw Mnemonic zin te bepalen, moet u rekening houden met de werkelijke beveiliging die deze biedt. Een woordgroep van 12 woorden biedt 128 bits beveiliging, terwijl een woordgroep van 24 256 bits biedt.


Dit verschil in beveiliging op zinsniveau verbetert echter niet de algemene veiligheid van een Bitcoin Wallet, aangezien de private sleutels die van deze zin zijn afgeleid slechts 128 bits veiligheid genieten. Inderdaad, zoals we eerder gezien hebben, worden Bitcoin private sleutels gegenereerd uit willekeurige getallen (of afgeleid van een willekeurige bron) variërend tussen $1$ en $n-1$, waarbij $n$ de orde van het generator punt $G$ van de secp256k1 curve voorstelt, een getal iets minder dan $2^{256}$. Men zou dus kunnen denken dat deze private sleutels 256 bits veiligheid bieden. Hun veiligheid ligt echter in de moeilijkheid om een privésleutel te vinden uit de bijbehorende publieke sleutel, een moeilijkheid die is vastgesteld door het wiskundige probleem van de discrete logaritme op elliptische krommen (_ECDLP_). Tot nu toe is het bekendste algoritme om dit probleem op te lossen het rho-algoritme van Pollard, dat het aantal bewerkingen dat nodig is om een sleutel te kraken terugbrengt tot de vierkantswortel van de grootte.


Voor 256-bits sleutels, zoals die gebruikt worden in Bitcoin, reduceert Pollard's rho algoritme de complexiteit dus tot $2^{128}$ operaties:


$$

O(\sqrt{2^{256}}) = O(2^{128})


$$


Daarom wordt aangenomen dat een privésleutel gebruikt in Bitcoin 128 bits veiligheid biedt.


Het kiezen van een woordgroep van 24 woorden biedt dus geen extra bescherming voor de Wallet, omdat 256 bits beveiliging van de woordgroep zinloos is als de afgeleide sleutels slechts 128 bits beveiliging bieden. Om dit principe te illustreren, is het alsof je een huis hebt met twee deuren: een oude houten deur en een versterkte deur. Bij een inbraak zou de versterkte deur geen nut hebben, omdat de indringer door de houten deur zou gaan. Dit is een analoge situatie.


Een zin van 12 woorden, die ook 128 bits veiligheid biedt, is daarom momenteel voldoende om je bitcoins te beschermen tegen elke poging tot diefstal. Zolang het algoritme voor digitale handtekeningen niet verandert om grotere sleutels te gebruiken of om te vertrouwen op een ander wiskundig probleem dan de ECDLP, blijft een zin van 24 woorden overbodig. Bovendien verhoogt een langere zin het risico op verlies tijdens de back-up: een back-up die twee keer zo kort is, is altijd gemakkelijker te beheren.


Om verder te gaan en concreet te leren hoe je handmatig generate een test Mnemonic zin kunt maken, raad ik je aan deze tutorial te ontdekken:


https://planb.network/tutorials/wallet/backup/generate-mnemonic-phrase-47507d90-e6af-4cac-b01b-01a14d7a8228

Voordat we verder gaan met de afleiding van de Wallet uit deze Mnemonic frase, zal ik je in het volgende hoofdstuk kennis laten maken met de BIP39 passphrase, omdat deze een rol speelt in het afleidingsproces en zich op hetzelfde niveau bevindt als de Mnemonic frase.


## De passphrase


<chapterId>6a51b397-f3b5-5084-b151-cef94bc9b93f</chapterId>


Zoals we net gezien hebben, worden HD wallets gegenereerd uit een Mnemonic zin die meestal uit 12 of 24 woorden bestaat. Deze zin is erg belangrijk, omdat het de mogelijkheid biedt om alle sleutels van een Wallet te herstellen in het geval dat het fysieke apparaat (zoals een Hardware Wallet, bijvoorbeeld) verloren gaat. Het is echter een enkelvoudig faalpunt, want als het gecompromitteerd wordt, kan een aanvaller alle bitcoins stelen. Dit is waar de BIP39 passphrase om de hoek komt kijken.


### Wat is een BIP39 passphrase?


De passphrase is een optioneel wachtwoord, dat u vrij kunt kiezen, dat wordt toegevoegd aan de Mnemonic zin in het sleutelafleidingsproces om de veiligheid van de Wallet te verbeteren.


Let op, de passphrase mag niet verward worden met de PIN-code van je Hardware Wallet of het wachtwoord dat gebruikt wordt om de toegang tot je Wallet op je computer te ontgrendelen. In tegenstelling tot al deze Elements, speelt de passphrase een rol bij het afleiden van de sleutels van je Wallet. **Dit betekent dat je zonder de passphrase nooit in staat zult zijn om je bitcoins terug te krijgen.**


De passphrase werkt samen met de Mnemonic-zin en wijzigt de seed waaruit de sleutels worden gegenereerd. Dus zelfs als iemand uw 12- of 24-woordzin bemachtigt, heeft hij zonder de passphrase geen toegang tot uw fondsen. Het gebruik van een passphrase creëert in wezen een nieuwe Wallet met verschillende sleutels. Als je de passphrase (zelfs maar een beetje) wijzigt, ontstaat er een andere Wallet.


![CYP201](assets/fr/041.webp)


### Waarom zou je een passphrase gebruiken?


De passphrase is willekeurig en kan elke combinatie van tekens zijn die de gebruiker kiest. Het gebruik van een passphrase biedt dus verschillende voordelen. Ten eerste vermindert het alle risico's die gepaard gaan met het compromitteren van de Mnemonic-zin door een tweede factor nodig te hebben om toegang te krijgen tot de fondsen (inbraak, toegang tot je huis, enz.).


Vervolgens kan het strategisch gebruikt worden om een lok Wallet te maken, om fysieke beperkingen het hoofd te bieden om je fondsen te stelen, zoals de beruchte "_$5 wrench attack_". In dit scenario is het idee om een Wallet zonder passphrase te hebben, die slechts een kleine hoeveelheid bitcoins bevat, genoeg om een potentiële aanvaller tevreden te stellen, terwijl je een verborgen Wallet hebt. Deze laatste gebruikt dezelfde Mnemonic zin, maar is beveiligd met een extra passphrase.

Tenslotte is het gebruik van een passphrase interessant wanneer men de willekeurigheid van het genereren van de seed van de HD Wallet wil controleren.


### Hoe kies je een goede passphrase?


Om de passphrase effectief te laten zijn, moet deze lang en willekeurig genoeg zijn. Net als bij een sterk wachtwoord, raad ik aan een passphrase te kiezen die zo lang en willekeurig mogelijk is, met een verscheidenheid aan letters, cijfers en symbolen om een brute force aanval onmogelijk te maken.


Het is ook belangrijk om deze passphrase goed op te slaan, op dezelfde manier als de Mnemonic zin. **Verlies betekent verlies van toegang tot je bitcoins**. Ik raad sterk af om het alleen uit het hoofd te onthouden, omdat dit het risico op verlies onredelijk vergroot. Het ideale is om het op te schrijven op een fysieke drager (papier of metaal), los van de Mnemonic-zin. Deze back-up moet uiteraard op een andere plaats bewaard worden dan waar uw Mnemonic zin is opgeslagen om te voorkomen dat beide tegelijkertijd gecompromitteerd worden.


![CYP201](assets/fr/042.webp)


In de volgende paragraaf zullen we ontdekken hoe deze twee Elements aan de basis van je Wallet - de Mnemonic frase en de passphrase - gebruikt worden om de sleutelparen af te leiden die gebruikt worden in de _scriptPubKey_ die je UTXO's vergrendelen.


# Creatie van Bitcoin portemonnees


<partId>9c25e767-7eae-50b8-8c5f-679d8fc83bab</partId>


## Aanmaken van de seed en hoofdsleutel


<chapterId>63093760-2010-5691-8d0e-9a04732ae557</chapterId>


Zodra de Mnemonic zin en de optionele passphrase zijn gegenereerd, kan het proces van het afleiden van een Bitcoin HD Wallet beginnen. De Mnemonic zin wordt eerst omgezet in een seed, die de basis vormt voor alle sleutels van de Wallet.


![CYP201](assets/fr/043.webp)


### De seed van een HD Wallet


De BIP39 standaard definieert de seed als een 512-bit reeks, die dient als startpunt voor de afleiding van alle sleutels van een HD Wallet. De seed wordt afgeleid van de Mnemonic zin en de mogelijke passphrase met behulp van het **PBKDF2** algoritme (_Password-Based Key Derivation Function 2_), dat we al besproken hebben in hoofdstuk 3.3. In deze afleidingsfunctie gebruiken we de volgende parameters:



- $m$ : de Mnemonic zin;
- $p$ : een optionele passphrase gekozen door de gebruiker om de veiligheid van de seed te verhogen. Als er geen passphrase is, wordt dit veld leeg gelaten;
- $BBKDF2}$ : de afleidingsfunctie met $HMAC-SHA512}$ en $2048$ iteraties;
- $s$: de 512-bits Wallet seed.

Ongeacht de gekozen zinslengte van de Mnemonic (132 bits of 264 bits), zal de PBKDF2-functie altijd een 512-bits uitvoer produceren en de seed zal daarom altijd deze grootte hebben.


### seed Afleidingsschema met PBKDF2


De volgende vergelijking illustreert de afleiding van de seed uit de Mnemonic zin en de passphrase:


$$
s = \text{PBKDF2}_{\text{HMAC-SHA512}}(m, p, 2048)
$$


![CYP201](assets/fr/044.webp)


De waarde van de seed wordt dus beïnvloed door de waarde van de Mnemonic zin en de passphrase. Door de passphrase te veranderen, wordt een andere seed verkregen. Echter, met dezelfde Mnemonic zin en passphrase, wordt altijd dezelfde seed gegenereerd, omdat PBKDF2 een deterministische functie is. Dit zorgt ervoor dat dezelfde sleutelparen teruggehaald kunnen worden via onze back-ups.


**Noot:** In het gewone taalgebruik verwijst de term "seed" vaak, door verkeerd taalgebruik, naar de Mnemonic frase. Bij afwezigheid van een passphrase is de ene gewoon de codering van de andere. Zoals we echter gezien hebben, zijn in de technische realiteit van portemonnees, de seed en de Mnemonic zin inderdaad twee verschillende Elements.


Nu we onze seed hebben, kunnen we verder gaan met de afleiding van onze Bitcoin Wallet.


### De hoofdsleutel en de chain code hoofdsleutel


Zodra de seed verkregen is, bestaat de volgende stap in het afleiden van een HD Wallet uit het berekenen van de master private key en de master chain code, die diepte 0 van onze Wallet zal vertegenwoordigen.


Om de master private sleutel en de master chain code te verkrijgen, wordt de HMAC-SHA512 functie toegepast op de seed, met een vaste sleutel "_Bitcoin Seed_" die identiek is voor alle Bitcoin gebruikers. Deze constante is gekozen om ervoor te zorgen dat de sleutelafleidingen specifiek zijn voor Bitcoin. Hier zijn de Elements:



- ${HMAC-SHA512}$: de afleidingsfunctie;
- $s$: de 512-bits Wallet seed;
- $"Bitcoin seed"}$: de gemeenschappelijke afleidingsconstante voor alle Bitcoin portemonnees.


$$

\text{output} = \text{HMAC-SHA512}(\text{"Bitcoin Seed"}, s)


$$


De uitgang van deze functie is dus 512 bits. Deze wordt vervolgens opgedeeld in 2 delen:



- De resterende 256 bits vormen de **privésleutel**;
- De rechter 256 bits vormen de **master chain code**.


Wiskundig kunnen deze twee waarden als volgt geschreven worden met $k_M$ als de master private key en $C_M$ als de master chain code:


$$
k_M = \text{HMAC-SHA512}(\text{"Bitcoin Seed"}, s)_{[:256]}
$$


$$
C_M = \text{HMAC-SHA512}(\text{"Bitcoin Seed"}, s)_{[256:]}
$$


![CYP201](assets/fr/045.webp)


### Rol van de hoofdsleutel en de chain code


De master private sleutel wordt beschouwd als de oudersleutel, waarvan alle afgeleide private sleutels - kinderen, kleinkinderen, achterkleinkinderen, enz. Het vertegenwoordigt het nulniveau in de afleidingshiërarchie.


De master chain code, aan de andere kant, introduceert een extra bron van entropie in het sleutelafleidingsproces voor kinderen, om bepaalde potentiële aanvallen tegen te gaan. Bovendien is in de HD Wallet aan elk sleutelpaar een unieke chain code gekoppeld, die ook gebruikt wordt om kindsleutels van dit paar af te leiden, maar dit zullen we in de komende hoofdstukken in meer detail bespreken.


Voordat we verder gaan met de afleiding van de HD Wallet met de volgende Elements, wil ik in het volgende hoofdstuk de uitgebreide sleutels introduceren, die vaak verward worden met de hoofdsleutel. We zullen zien hoe ze zijn opgebouwd en welke rol ze spelen in de Bitcoin Wallet.


## Uitgebreide toetsen

<chapterId>8dcffce1-31bd-5e0b-965b-735f5f9e4602</chapterId>


Een uitgebreide sleutel is eenvoudigweg de aaneenschakeling van een sleutel (privaat of publiek) en zijn geassocieerde chain code. Deze chain code is essentieel voor het afleiden van kindsleutels, omdat het zonder deze sleutel onmogelijk is om kindsleutels af te leiden van een oudersleutel. Deze uitgebreide sleutels maken het dus mogelijk om alle benodigde informatie te verzamelen om kindsleutels af te leiden, waardoor accountbeheer binnen een HD Wallet vereenvoudigd wordt.


![CYP201](assets/fr/046.webp)


De uitgebreide sleutel bestaat uit twee delen:


- De payload, die de private of publieke sleutel en de bijbehorende chain code bevat;
- De metadata zijn verschillende stukjes informatie om de interoperabiliteit tussen software te vergemakkelijken en het begrip voor de gebruiker te verbeteren.


### Hoe uitgebreide toetsen werken

Als de uitgebreide sleutel een privésleutel bevat, wordt het een uitgebreide privésleutel genoemd. Deze is te herkennen aan de prefix die de identificatie `prv` bevat. Naast de privésleutel bevat de uitgebreide privésleutel ook de bijbehorende chain code. Met dit type uitgebreide sleutel is het mogelijk om alle soorten kind-privésleutels af te leiden. Door het optellen en verdubbelen van punten op elliptische krommen is het dus ook mogelijk om child public keys af te leiden.


Als de uitgebreide sleutel geen privésleutel bevat, maar een openbare sleutel, wordt het een uitgebreide openbare sleutel genoemd. Deze wordt herkend aan de prefix die de identificatie `pub` bevat. Naast de sleutel bevat het uiteraard ook de bijbehorende chain code. In tegenstelling tot de uitgebreide private sleutel, kunnen met de uitgebreide publieke sleutel alleen "normale" child public keys worden afgeleid (wat betekent dat er geen "hardened" child keys kunnen worden afgeleid). We zullen in het volgende hoofdstuk zien wat deze "normale" en "geharde" kwalificaties betekenen.


In ieder geval is het met de uitgebreide openbare sleutel niet mogelijk om privésleutels van kinderen af te leiden. Dus zelfs als iemand toegang heeft tot een `xpub`, kan hij de bijbehorende gelden niet uitgeven, omdat hij geen toegang heeft tot de bijbehorende privésleutels. Ze kunnen alleen publieke kindsleutels afleiden om de bijbehorende transacties te observeren.


In het volgende gebruiken we de volgende notatie:


- $K_{\text{PAR}}$: een openbare sleutel van een ouder;
- $k_{\text{PAR}}$: een privésleutel van de ouder;
- $C_{\text{PAR}}$: een ouder chain code;
- $C_{CHD}}$: een kind chain code;
- $K_{\text{CHD}}^n$: een normale openbare kindersleutel;
- $k_{CHD}}^n$: een normale kind-privésleutel;
- $K_{\text{CHD}}^h$: een geharde openbare kindersleutel;
- $k_{CHD}}^h$: een geharde kind-privésleutel.


![CYP201](assets/fr/047.webp)


### Constructie van een uitgebreide sleutel


Een uitgebreide sleutel is als volgt opgebouwd:


- **Versie**: Versiecode om de aard van de sleutel te identificeren (`xprv`, `xpub`, `yprv`, `ypub`...). We zullen aan het eind van dit hoofdstuk zien waar de letters `x`, `y` en `z` mee corresponderen.
- **Depth**: Hiërarchisch niveau in de HD Wallet ten opzichte van de hoofdsleutel (0 voor de hoofdsleutel).
- **Parent Fingerprint**: De eerste 4 bytes van de HASH160 Hash van de openbare sleutel die gebruikt is om de sleutel in de payload af te leiden.
- **Indexnummer**: Identificatiecode van het kind onder sibling-sleutels, dat wil zeggen, onder alle sleutels op hetzelfde afleidingsniveau die dezelfde oudersleutel hebben.
- **chain code**: Een unieke code van 32 bytes voor het afleiden van kindsleutels.
- **Sleutel**: De privésleutel (voorafgegaan door 1 byte voor de grootte) of de openbare sleutel.
- **Controlesom**: Een controlesom berekend met de functie HASH256 (dubbele SHA256) is ook toegevoegd, waarmee de integriteit van de uitgebreide sleutel kan worden geverifieerd tijdens de overdracht of opslag.


Het volledige formaat van een uitgebreide sleutel is daarom 78 bytes zonder de controlesom en 82 bytes met de controlesom. Vervolgens wordt het omgezet naar Base58 om een representatie te krijgen die gemakkelijk leesbaar is voor gebruikers. Het Base58 formaat is hetzelfde als dat gebruikt wordt voor *Legacy* ontvangstadressen (vóór *SegWit*).


| Element           | Description                                                                                                        | Size      |
| ----------------- | ------------------------------------------------------------------------------------------------------------------ | --------- |
| Version           | Indicates whether the key is public (`xpub`, `ypub`) or private (`xprv`, `zprv`), as well as the version of the extended key | 4 bytes   |
| Depth             | Level in the hierarchy relative to the master key                                                                  | 1 byte    |
| Parent Fingerprint| The first 4 bytes of HASH160 of the parent public key                                                              | 4 bytes   |
| Index Number      | Position of the key in the order of children                                                                       | 4 bytes   |
| Chain Code        | Used to derive child keys                                                                                          | 32 bytes  |
| Key               | The private key (with a 1-byte prefix) or the public key                                                          | 33 bytes  |
| Checksum          | Checksum to verify integrity                                                                                       | 4 bytes   |

Als er één byte wordt toegevoegd aan alleen de privésleutel, dan is dat omdat de gecomprimeerde openbare sleutel één byte langer is dan de privésleutel. Deze extra byte, toegevoegd aan het begin van de privésleutel als `0x00`, maakt hun grootte gelijk en zorgt ervoor dat de payload van de uitgebreide sleutel even lang is, of het nu een publieke of een privésleutel is.


### Uitgebreide sleutelvoorvoegsels

Zoals we zojuist hebben gezien, bevatten uitgebreide sleutels een voorvoegsel dat zowel de versie van de uitgebreide sleutel als de aard ervan aangeeft. De notatie `pub` geeft aan dat het om een uitgebreide openbare sleutel gaat en de notatie `prv` geeft een uitgebreide privésleutel aan. De extra letter aan de basis van de uitgebreide sleutel helpt om aan te geven of de gevolgde standaard Legacy, SegWit v0, SegWit v1, enz. is.

Hier volgt een overzicht van de gebruikte voorvoegsels en hun betekenis:


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


### Details van een Extended Key's Elements


Om de interne structuur van een uitgebreide sleutel beter te begrijpen, nemen we er een als voorbeeld en breken we hem af. Hier is een uitgebreide sleutel:



- In **Base58**:


```text
xpub6CTNzMUkzpurBWaT4HQoYzLP4uBbGJuWY358Rj7rauiw4rMHCyq3Rfy9w4kyJXJzeFfyrKLUar2rUCukSiDQFa7roTwzjiAhyQAdPLEjqHT
```



- In hexadecimaal:


```text
0488B21E036D5601AD80000000C605DF9FBD77FD6965BD02B77831EC5C78646AD3ACA14DC3984186F72633A89303772CCB99F4EF346078D167065404EED8A58787DED31BFA479244824DF50658051F067C3A
```


Deze uitgebreide sleutel valt uiteen in verschillende Elements:


1.**Versie**: `0488B21E`


De eerste 4 bytes zijn de versie. Hier komt het overeen met een uitgebreide publieke sleutel op de Mainnet met een afleidingsdoel van ofwel *Legacy* of *SegWit v1*.


2.**Diepte**: `03`


Dit veld geeft het hiërarchische niveau van de sleutel binnen de HD Wallet aan. In dit geval betekent een diepte van `03` dat deze sleutel drie afleidingsniveaus lager is dan de hoofdsleutel.


3.**Vaderlijke vingerafdruk**: `6D5601AD`


Dit zijn de eerste 4 bytes van de HASH160 Hash van de openbare sleutel die gebruikt is om deze `xpub` af te leiden.


4.**Indexnummer**: `80000000`


Deze index geeft de positie van de sleutel aan tussen de kinderen van zijn ouder. Het `0x80` voorvoegsel geeft aan dat de sleutel is afgeleid op een verharde manier en aangezien de rest is gevuld met nullen, geeft het aan dat deze sleutel de eerste is onder zijn mogelijke broers en zussen.


5.**chain code**: `C605DF9FBD77FD6965BD02B77831EC5C78646AD3ACA14DC3984186F72633A893`


6.**Publieke sleutel**: `03772CCB99F4EF346078D167065404EED8A58787DED31BFA479244824DF5065805`


7.**Checksum**: `1F067C3A`


De controlesom komt overeen met de eerste 4 bytes van de Hash (dubbele SHA256) van al het andere.


In dit hoofdstuk ontdekten we dat er twee verschillende soorten kind sleutels zijn. We hebben ook geleerd dat voor het afleiden van deze kindsleutels een sleutel (privé of publiek) en zijn chain code nodig zijn. In het volgende hoofdstuk zullen we in detail ingaan op de aard van deze verschillende typen sleutels en hoe we ze kunnen afleiden van hun oudersleutel en chain code.



## Afleiding van kindersleutelparen

<chapterId>61c0807c-845b-5076-ad06-7f395b36adfd</chapterId>


De afleiding van kind-sleutelparen in Bitcoin HD wallets is gebaseerd op een hiërarchische structuur die het mogelijk maakt een groot aantal sleutels te genereren, terwijl deze paren in verschillende groepen worden georganiseerd via takken. Elk kindpaar dat is afgeleid van een ouderpaar kan direct worden gebruikt in een *scriptPubKey* om bitcoins te vergrendelen, of als een startpunt voor generate meer kind sleutels, enzovoort, om een boom van sleutels te creëren.


Al deze afleidingen beginnen met de hoofdsleutel en de hoofd chain code, die de eerste ouders zijn op diepteniveau 0. Zij zijn, in zekere zin, de Adam en Eva van jouw Wallet sleutels, gemeenschappelijke voorouders van alle afgeleide sleutels. Zij zijn in zekere zin de Adam en Eva van jouw Wallet sleutels, gemeenschappelijke voorouders van alle afgeleide sleutels.


![CYP201](assets/fr/048.webp)


Laten we eens kijken hoe deze deterministische afleiding werkt.


### De verschillende soorten afleidingen van kindersleutels


Zoals we in het vorige hoofdstuk al kort aanstipten, zijn kindersleutels onderverdeeld in twee hoofdtypen.


- **Normale kindsleutels** ($k_{\text{CHD}}^n, K_{\text{CHD}}^n$): Deze worden afgeleid van de uitgebreide openbare sleutel ($K_{\text{PAR}}$), of de uitgebreide privésleutel ($k_{\text{PAR}}$), door eerst de openbare sleutel af te leiden.
- **Geharde kindsleutels** ($k_{CHD}^h, K_{\text{CHD}}^h$): Deze kunnen alleen worden afgeleid van de uitgebreide privésleutel ($k_{\text{PAR}}$) en zijn daarom onzichtbaar voor waarnemers die alleen de uitgebreide publieke sleutel hebben.


Elk sleutelpaar wordt geïdentificeerd door een 32-bits **index** ($i$ genoemd in onze berekeningen). De indexen voor normale sleutels variëren van $0$ tot $2^{31}-1$, terwijl die voor verharde sleutels variëren van $2^{31}$ tot $2^{32}-1$. Deze getallen worden gebruikt om broer-zus sleutelparen te onderscheiden tijdens het afleiden. Elk ouder-sleutelpaar moet namelijk meerdere kind-sleutelparen kunnen afleiden. Als we systematisch dezelfde berekening zouden uitvoeren vanaf de oudersleutels, zouden alle verkregen verwante sleutels identiek zijn, wat niet wenselijk is. De index introduceert dus een variabele die de afleidingsberekening wijzigt, waardoor elk broer-zus paar gedifferentieerd kan worden. Behalve voor specifiek gebruik in bepaalde protocollen en afleidingsstandaarden, beginnen we over het algemeen met het afleiden van de eerste kindsleutel met de index `0`, de tweede met de index `1`, enzovoort.


### Afleidingsproces met HMAC-SHA512


De afleiding van elke kindsleutel is gebaseerd op de HMAC-SHA512 functie, die we bespraken in Sectie 2 over Hash functies. Deze heeft twee ingangen: de ouder chain code $C_{\text{PAR}}$ en de aaneenschakeling van de oudersleutel (de publieke sleutel $K_{\text{PAR}}$ of de privésleutel $k_{\text{PAR}}$, afhankelijk van het gewenste type kindsleutel) met de index. De uitvoer van HMAC-SHA512 is een reeks van 512 bits, verdeeld in twee delen:


- De eerste **32 bytes** (of $h_1$) worden gebruikt om het nieuwe kindpaar te berekenen.
- De laatste 32 bytes (of $h_2$) dienen als de nieuwe chain code $C_{{CHD}}$ voor het kindpaar.


In al onze berekeningen zal ik de uitvoer van de HMAC-SHA512-functie aanduiden als ${Hash}$.


![CYP201](assets/fr/049.webp)


#### Afleiden van een Kind-Privésleutel van een Ouder-Privésleutel


Om een kind-privésleutel $k_{\text{CHD}}$ af te leiden uit een ouder-privésleutel $k_{\text{PAR}}$ zijn twee scenario's mogelijk, afhankelijk van of een geharde of normale sleutel gewenst is.


Voor een **normale kindersleutel** ($i < 2^{31}$) is de berekening van $text{Hash}$ als volgt:


$$
\text{hash} = \text{HMAC-SHA512}(C_{\text{PAR}},  k_{\text{PAR}} \cdot G \Vert i)
$$


In deze berekening zien we dat onze HMAC-functie twee ingangen nodig heeft: eerst de chain code van de ouder en dan de aaneenschakeling van de index met de openbare sleutel die hoort bij de privésleutel van de ouder. De openbare sleutel van de ouder wordt hier gebruikt omdat we een normale kindsleutel willen afleiden, geen geharde sleutel.

We hebben nu een 64-byte $tekst{Hash}$ die we opsplitsen in 2 delen van elk 32 bytes, $h_1$ en $h_2$:



$$

\text{hash} = h_1 \Vert h_2

$$



$$
h_1 = \text{hash}_{[:32]} \quad, \quad h_2 = \text{hash}_{[32:]}
$$


De privésleutel van het kind $k_{CHD}}^n$ wordt dan als volgt berekend:


$$
k_{\text{CHD}}^n = \text{parse256}(h_1) + k_{\text{PAR}} \mod n
$$


In deze berekening bestaat de bewerking ${parse256}(h_1)$ uit het interpreteren van de eerste 32 bytes van de ${Hash}$ als een geheel getal van 256 bits. Dit getal wordt dan toegevoegd aan de ouderprivésleutel, allemaal modulo $n$ om binnen de orde van de elliptische curve te blijven, zoals we zagen in hoofdstuk 3 over digitale handtekeningen. Om een normale kind-privésleutel af te leiden, wordt de openbare sleutel van de ouder weliswaar gebruikt als basis voor de berekening in de ingangen van de HMAC-SHA512-functie, maar het is altijd nodig om de privésleutel van de ouder te hebben om de berekening af te ronden.


Van deze kind-privésleutel is het mogelijk om de corresponderende publieke sleutel af te leiden door ECDSA of Schnorr toe te passen. Op deze manier verkrijgen we een compleet sleutelpaar.


Dan wordt het tweede deel van de $\text{Hash}$ eenvoudig geïnterpreteerd als de chain code voor het kind sleutelpaar dat we zojuist hebben afgeleid:


$$
C_{\text{CHD}} = h_2
$$


Hier volgt een schematische voorstelling van de algemene afleiding:


![CYP201](assets/fr/050.webp)


Voor een **geharde kindersleutel** ($i \geq 2^{31}$) is de berekening van de $tekst{Hash}$ als volgt:



$$
\text{hash} = \text{HMAC-SHA512}(C_{\text{PAR}}, 0x00 \Vert k_{\text{PAR}} \Vert i)
$$


In deze berekening zien we dat onze HMAC-functie twee ingangen nodig heeft: eerst de chain code van de ouder en dan de aaneenschakeling van de index met de privésleutel van de ouder. De privésleutel van de ouder wordt hier gebruikt omdat we een geharde kindersleutel willen afleiden. Bovendien wordt een byte gelijk aan `0x00` toegevoegd aan het begin van de sleutel. Deze bewerking maakt de lengte gelijk aan die van een gecomprimeerde openbare sleutel.

We hebben nu dus een $tekst{Hash}$ van 64 bytes die we opsplitsen in 2 delen van elk 32 bytes, $h_1$ en $h_2$:

$$

\text{hash} = h_1 \Vert h_2

$$



$$
h_1 = \text{hash}[:32] \quad, \quad h_2 = \text{hash}[32:]
$$


De privésleutel van het kind $k_{CHD}}^h$ wordt dan als volgt berekend:


$$
k_{\text{CHD}}^h = \text{parse256}(h_1) + k_{\text{PAR}} \mod n
$$


Vervolgens interpreteren we simpelweg het tweede deel van de $W-407}$ als zijnde de chain code voor het paar kindersleutels dat we zojuist hebben afgeleid:


$$
C_{\text{CHD}} = h_2
$$


Hier volgt een schematische voorstelling van de algemene afleiding:


![CYP201](assets/fr/051.webp)


We kunnen zien dat normale afleiding en verharde afleiding op dezelfde manier werken, met dit verschil: normale afleiding gebruikt de openbare sleutel van de ouder als invoer voor de HMAC-functie, terwijl verharde afleiding de privésleutel van de ouder gebruikt.


#### Een openbare sleutel van een kind afleiden van een openbare sleutel van een ouder


Als we alleen de openbare oudersleutel $K_{\text{PAR}}$ en de bijbehorende chain code $C_{\text{PAR}}$ kennen, dus een uitgebreide openbare sleutel, is het mogelijk om openbare kindsleutels $K_{\text{CHD}}^n$ af te leiden, maar alleen voor normale (niet-geharde) kindsleutels. Dit principe maakt het met name mogelijk om de bewegingen van een account in een Bitcoin Wallet te monitoren vanaf de `xpub` (*watch-only*).


Om deze berekening uit te voeren, berekenen we de $\text{Hash}$ met een index $i < 2^{31}$ (normale afleiding):


$$
\text{hash} = \text{HMAC-SHA512}(C_{\text{PAR}}, K_{\text{PAR}} \Vert i)
$$


In deze berekening zien we dat onze HMAC-functie twee ingangen nodig heeft: eerst de chain code van de ouder, dan de aaneenschakeling van de index met de openbare sleutel van de ouder.


We hebben nu dus een $\text{Hash}$ van 64 bytes die we opsplitsen in 2 delen van elk 32 bytes, $h_1$ en $h_2$:



$$

\text{hash} = h_1 \Vert h_2

$$



$$

h_1 = \text{hash}[:32] \quad, \quad h_2 = \text{hash}[32:]

$$


De openbare kindersleutel $K_{{CHD}}^n$ wordt dan als volgt berekend:


$$
K_{\text{CHD}}^n = \text{parse256}(h_1) \cdot G + K_{\text{PAR}}
$$


Als $K_{parse256}(h_1) \geq n$ (orde van de elliptische kromme) of als $K_{parse256}}^n$ het punt op oneindig is, is de afleiding ongeldig en moet een andere index gekozen worden.


In deze berekening interpreteert de bewerking ${parse256}(h_1)$ de eerste 32 bytes van de ${Hash}$ als een geheel getal van 256 bits. Dit getal wordt gebruikt om een punt op de elliptische curve te berekenen door optelling en verdubbeling vanaf het generatorpunt $G$. Dit punt wordt vervolgens toegevoegd aan de openbare sleutel van de ouder om de normale openbare sleutel van het kind te verkrijgen. Om een normale kind-openbare sleutel af te leiden, zijn dus alleen de ouder-openbare sleutel en de ouder-chain code nodig; de ouder-privésleutel komt nooit in dit proces voor, in tegenstelling tot de berekening van de kind-privésleutel die we eerder zagen.


Vervolgens wordt het kind chain code gewoon:


$$
C_{\text{CHD}} = h_2
$$


Hier volgt een schematische voorstelling van de algemene afleiding:


![CYP201](assets/fr/052.webp)


### Correspondentie tussen openbare en privésleutels van kinderen


Een vraag die kan opkomen is hoe een normale kind-privésleutel die is afgeleid van een ouder-privésleutel kan corresponderen met een normale kind-privésleutel die is afgeleid van de corresponderende ouder-privésleutel. Dit verband wordt precies gegarandeerd door de eigenschappen van elliptische krommen. Om een normale kind-publieke sleutel af te leiden, wordt HMAC-SHA512 op dezelfde manier toegepast, maar de uitvoer wordt anders gebruikt:


- Normale kind-privésleutel: $k_{CHD}^n = \text{parse256}(h_1) + k_{\text{PAR}} \mod n$
- Normale openbare sleutel kind: $K_{CHD}^n = \text{parse256}(h_1) \cdot G + K_{\text{PAR}}$


Dankzij de optel- en verdubbelingsbewerkingen op de elliptische curve produceren beide methoden consistente resultaten: de openbare sleutel die is afgeleid van de privésleutel van het kind is identiek aan de openbare sleutel van het kind die rechtstreeks is afgeleid van de openbare sleutel van de ouder.


### Overzicht van afleidingstypen


Samengevat zijn hier de verschillende mogelijke soorten afleidingen:


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


Tot nu toe heb je geleerd om de basis Elements van een HD Wallet te maken: de Mnemonic frase, de seed, en dan de master key en master chain code. Je hebt ook ontdekt hoe je kind sleutelparen kunt afleiden in dit hoofdstuk. In het volgende hoofdstuk zullen we onderzoeken hoe deze afleidingen georganiseerd zijn in Bitcoin wallets en welke structuur gevolgd moet worden om concreet de ontvangende adressen en de sleutelparen te verkrijgen die gebruikt worden in het *scriptPubKey* en *scriptSig*.


## Wallet Structuur en afleidingstrajecten

<chapterId>34e1bbda-67de-5493-b268-1fded8d67689</chapterId>


De hiërarchische structuur van HD wallets in Bitcoin maakt het mogelijk om sleutelparen op verschillende manieren te organiseren. Het idee is om uit de master private key en master chain code verschillende niveaus van diepte af te leiden. Elk toegevoegd niveau komt overeen met de afleiding van een kind sleutelpaar van een ouder sleutelpaar.


In de loop der tijd hebben verschillende BIP's standaarden geïntroduceerd voor deze afleidingspaden, met als doel het gebruik ervan te standaardiseren in verschillende software. In dit hoofdstuk zullen we de betekenis van elk afleidingsniveau in HD wallets ontdekken, volgens deze standaarden.


### De afleidingsdiepte van een HD Wallet


Afleidingspaden zijn georganiseerd in lagen van diepte, variërend van diepte 0, die de hoofdsleutel en chain code vertegenwoordigt, tot lagen van subniveaus voor het afleiden van adressen die gebruikt worden om UTXO's te vergrendelen. De BIP's (*Bitcoin Improvement Proposals*) definiëren de standaarden voor elke Layer, wat helpt bij het harmoniseren van praktijken tussen verschillende Wallet beheersoftware.


Een afleidingspad verwijst daarom naar de reeks indexen die worden gebruikt om kindsleutels van een hoofdsleutel af te leiden.


**Diepte 0: Hoofdsleutel (BIP32)**


Deze diepte komt overeen met de master private key en master chain code van de Wallet. Het wordt weergegeven door de notatie $m/$.


**Diepgang 1: Doel (BIP43)**


Het doel bepaalt de logische structuur van de afleiding. Bijvoorbeeld, een P2WPKH Address zal $/84'/$ hebben op diepte 1 (volgens BIP84), terwijl een P2TR Address $/86'/$ zal hebben (volgens BIP86). Deze Layer vergemakkelijkt de compatibiliteit tussen portemonnees door indexnummers aan te geven die overeenkomen met de BIP-nummers.


Met andere woorden, zodra je de hoofdsleutel en de chain code hoofdsleutel hebt, dienen deze als ouder sleutelpaar om een kind sleutelpaar af te leiden. De index die gebruikt wordt in deze afleiding kan bijvoorbeeld $/84'/$ zijn als de Wallet bedoeld is om SegWit v0 type scripts te gebruiken. Dit sleutelpaar bevindt zich dan op diepte 1. Zijn rol is niet om bitcoins te vergrendelen, maar gewoon om te dienen als een tussenpunt in de afleidingshiërarchie.


**Diepte 2: Valutasoort (BIP44)**


Van het sleutelpaar op diepte 1 wordt een nieuwe afleiding uitgevoerd om het sleutelpaar op diepte 2 te verkrijgen. Deze diepte maakt het mogelijk om Bitcoin-accounts te onderscheiden van andere cryptocurrencies binnen dezelfde Wallet.


Elke valuta heeft een unieke index om compatibiliteit tussen meerdere valuta wallets te garanderen. Voor Bitcoin is de index bijvoorbeeld $/0'/$ (of `0x80000000` in hexadecimale notatie). Valuta-indexen worden gekozen in het bereik van $2^{31}$ tot $2^{32}-1$ om een geharde afleiding te garanderen.


Om je andere voorbeelden te geven, zijn hier de indexen van enkele valuta:


- $1'$ (`0x80000001`) voor Testnet bitcoins;
- $2'$ (`0x80000002`) voor Litecoin;
- $60'$ (`0x8000003c`) voor Ethereum...


**Diepte 3: Rekening (BIP32)**


Elke Wallet kan worden onderverdeeld in verschillende accounts, genummerd vanaf $2^{31}$, en op diepte 3 weergegeven door $/0'/$ voor de eerste account, $/1'/$ voor de tweede, enzovoort. Over het algemeen wordt bij het verwijzen naar een uitgebreide sleutel `xpub` verwezen naar sleutels op deze afleidingsdiepte.


Deze scheiding in verschillende accounts is optioneel. Het is bedoeld om de organisatie van de Wallet voor gebruikers te vereenvoudigen. In de praktijk wordt vaak maar één account gebruikt, meestal standaard het eerste. Echter, in sommige gevallen, als men duidelijk onderscheid wil maken tussen sleutelparen voor verschillend gebruik, kan dit nuttig zijn. Het is bijvoorbeeld mogelijk om een persoonlijk account en een professioneel account te maken van dezelfde seed, met volledig verschillende groepen sleutels van deze afleidingsdiepte.


**Diepte 4: Ketting (BIP32)**


Elke rekening die op diepte 3 wordt gedefinieerd, wordt vervolgens gestructureerd in twee ketens:


- De **externe keten**: In deze keten worden zogenaamde "openbare" adressen afgeleid. Deze ontvangstadressen zijn bedoeld om UTXO's te blokkeren die afkomstig zijn van externe transacties (dat wil zeggen, die afkomstig zijn van de consumptie van UTXO's die niet van jou zijn). Simpel gezegd wordt deze externe keten gebruikt wanneer iemand bitcoins wil ontvangen. Wanneer je op "*ontvangen*" klikt in je Wallet software, is het altijd een Address van de externe keten die je wordt aangeboden. Deze keten wordt vertegenwoordigd door een paar sleutels met de index $/0/$.
- De interne keten (wissel): Deze keten is gereserveerd voor het ontvangen van adressen die bitcoins vergrendelen die afkomstig zijn van de consumptie van UTXO's die aan jou toebehoren, met andere woorden, wisseladressen. Het wordt geïdentificeerd door de index $/1/$.


**Diepte 5: Address Index (BIP32)**


Diepte 5 tenslotte vertegenwoordigt de laatste afleidingsstap in de Wallet. Hoewel het technisch mogelijk is om oneindig door te gaan, stoppen de huidige standaarden hier. Op deze laatste diepte worden de sleutelparen afgeleid die daadwerkelijk zullen worden gebruikt om de UTXO's te vergrendelen en te ontgrendelen. Elke index maakt het mogelijk een onderscheid te maken tussen broer-zus sleutelparen: de eerste ontvangende Address zal dus de index $/0/$ gebruiken, de tweede de index $/1/$, enzovoort.


![CYP201](assets/fr/053.webp)


### Notatie van afleidingspaden


Het afleidingspad wordt geschreven door elk niveau te scheiden met een schuine streep ($/$). Elke schuine streep geeft dus een afleiding aan van een ouder sleutelpaar ($k_{\text{PAR}}$, $K_{\text{PAR}}$, $C_{\text{PAR}}$) naar een kindersleutelpaar ($k_{\text{CHD}}$, $K_{\text{CHD}}$, $C_{\text{CHD}}$). Het nummer op elke diepte komt overeen met de index die is gebruikt om deze sleutel van de ouders af te leiden. De apostrof ($'$) die soms rechts van de index staat, geeft een verharde afleiding aan ($k_{\text{CHD}}^h$, $K_{\text{CHD}}^h$). Soms wordt deze apostrof vervangen door een $h$. Zonder apostrof of $h$ is het dus een normale afleiding ($k_{text{CHD}}^n$, $K_{\text{CHD}}^n$).

Zoals we in de vorige hoofdstukken hebben gezien, beginnen geharde sleutelindexen vanaf $2^{31}$, of `0x80000000` in hexadecimaal. Daarom moet, wanneer een index wordt gevolgd door een apostrof in een afleidingspad, $2^{31}$ worden opgeteld bij het aangegeven getal om de werkelijke waarde te verkrijgen die wordt gebruikt in de HMAC-SHA512-functie. Als het afleidingspad bijvoorbeeld $/44'/$ specificeert, is de werkelijke index:

$$

i = 44 + 2^{31} = 2\,147\,483\,692

$$


In hexadecimaal is dit `0x8000002C`.


Nu we de belangrijkste principes van afleidingspaden hebben begrepen, laten we een voorbeeld nemen! Hier is het afleidingspad voor een Bitcoin die Address ontvangt:



$$

m / 84' / 0' / 1' / 0 / 7

$$


In dit voorbeeld:


- $84'$ geeft de P2WPKH (SegWit v0) standaard aan;
- $0'$ geeft de Bitcoin valuta aan op de Mainnet;
- $1'$ komt overeen met de tweede rekening in de Wallet;
- $0$ geeft aan dat de Address zich op de externe keten bevindt;
- $7$ geeft de 8e externe Address van dit account aan.


### Samenvatting van de afleidingsstructuur


| Depth | Description        | Standard Example                  |
| ----- | ------------------ | --------------------------------- |
| 0     | Master Key         | $m/$                              |
| 1     | Purpose            | $/86'/$ (P2TR)                    |
| 2     | Currency           | $/0'/$ (Bitcoin)                  |
| 3     | Account            | $/0'/$ (First account)            |
| 4     | Chain              | $/0/$ (external) or $/1/$ (change)|
| 5     | Address Index      | $/0/$ (first address)             |

In het volgende hoofdstuk zullen we ontdekken wat "*output script descriptors*" zijn, een recent geïntroduceerde innovatie in Bitcoin Core die de back-up van een Bitcoin Wallet vereenvoudigt.


## Uitvoer script descriptors

<chapterId>e4f1c2d3-9b8a-4d3e-8f2a-7b6c5d4e3f2a</chapterId>

Er wordt vaak gezegd dat de Mnemonic zin alleen voldoende is om toegang te krijgen tot een Wallet. In werkelijkheid liggen de zaken iets ingewikkelder. In het vorige hoofdstuk hebben we gekeken naar de afleidingsstructuur van de HD Wallet, en het is je misschien opgevallen dat dit proces behoorlijk complex is. Afleidingspaden vertellen software welke richting ze moet volgen om de sleutels van de gebruiker af te leiden. Echter, bij het herstellen van een Bitcoin Wallet, als men deze paden niet kent, is de Mnemonic zin alleen niet genoeg. Het maakt het mogelijk om de hoofdsleutel en de hoofd chain code te verkrijgen, maar dan is het nodig om de indexen te kennen die gebruikt zijn om de kind sleutels te bereiken.


Theoretisch zou het nodig zijn om niet alleen de Mnemonic zinsnede van onze Wallet op te slaan, maar ook de paden naar de accounts die we gebruiken. In de praktijk is het vaak mogelijk om zonder deze informatie weer toegang te krijgen tot de kind sleutels, mits de standaarden zijn gevolgd. Door elke standaard één voor één te testen, is het over het algemeen mogelijk om weer toegang te krijgen tot de bitcoins. Dit is echter niet gegarandeerd en het is vooral ingewikkeld voor beginners. Met de diversificatie van scripttypen en de opkomst van complexere configuraties kan deze informatie bovendien moeilijk te extrapoleren zijn, waardoor deze gegevens privé-informatie worden en moeilijk te achterhalen zijn met brute kracht. Daarom is er onlangs een innovatie geïntroduceerd die nu in uw favoriete Wallet software geïntegreerd begint te worden: de *output script descriptors*.


### Wat is een "descriptor"?


De "*output script descriptors*", of eenvoudigweg "*descriptors*", zijn gestructureerde uitdrukkingen die een output script (*scriptPubKey*) volledig beschrijven en alle nodige informatie verschaffen om de transacties te volgen die met een bepaald script geassocieerd zijn. Ze vergemakkelijken het beheer van sleutels in HD wallets door een gestandaardiseerde en volledige beschrijving te geven van de Wallet structuur en de gebruikte adrestypes.


Het belangrijkste voordeel van descriptoren ligt in hun vermogen om alle essentiële informatie om een Wallet te herstellen in een enkele string in te kapselen (naast de herstelzin). Door een descriptor op te slaan met de bijbehorende Mnemonic zinnen, wordt het mogelijk om de private sleutels te herstellen door precies hun positie in de hiërarchie te kennen. Voor Multisig wallets, waarvan de back-up in eerste instantie complexer was, bevat de descriptor de `xpub` van elke factor, waardoor het mogelijk wordt om de adressen te regenereren in geval van een probleem.


### Constructie van een descriptor


Een descriptor bestaat uit verschillende Elements:


- Script functies zoals `pk` (*Pay-to-PubKey*), `pkh` (*Pay-to-PubKey-Hash*), `wpkh` (*Pay-to-Witness-PubKey-Hash*), `sh` (*Pay-to-Script-Hash*), `wsh` (*Pay-to-Witness-Script-Hash*), `tr` (*Pay-to-Taproot*), `multi` (*Multisignature*) en `sortedmulti` (*Multisignature met gesorteerde sleutels*);
- Afgeleide paden, bijvoorbeeld `[d34db33f/44h/0h/0h]` die een afgeleid accountpad en een specifieke vingersleutelafdruk aangeeft;
- Sleutels in verschillende formaten zoals hexadecimale openbare sleutels of uitgebreide openbare sleutels (`xpub`);
- Een controlesom, voorafgegaan door een Hash teken, om de integriteit van het descriptor te verifiëren.


Een descriptor voor een P2WPKH (SegWit v0) Wallet zou er bijvoorbeeld zo uit kunnen zien:


```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7nr4
```


In deze descriptor geeft de afleidingsfunctie `wpkh` een scripttype *Pay-to-Witness-Public-Key-Hash* aan. Het wordt gevolgd door het afleidingspad dat bevat:


- `cdeab12f`: de hoofdsleutel vingerafdruk;
- `84h`: wat het gebruik van een BIP84 doel aangeeft, bedoeld voor SegWit v0 adressen;
- `0h`: wat aangeeft dat het een BTC valuta is op de Mainnet;
- `0h`: dat verwijst naar het specifieke rekeningnummer dat in de Wallet wordt gebruikt.


De descriptor bevat ook de uitgebreide openbare sleutel die in deze Wallet wordt gebruikt:


```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```


De notatie `/<0;1>/*` geeft aan dat de descriptor adressen kan genereren uit zowel de externe keten (`0`) als de interne keten (`1`). Het jokerteken (`*`) aan het einde van het pad betekent dat vanaf deze positie alle niet-versterkte (“*unhardened*”) subkeys sequentieel kunnen worden afgeleid, of het nu gaat om externe of interne adressen. Deze syntaxis impliceert niet direct het concept van *gap limit*, dat onderdeel is van een wallets-specifiek mechanisme voor adresdetectie, maar dient hier alleen om aan te geven dat alle mogelijke afleidingen op deze locatie in aanmerking worden genomen.


Tenslotte vertegenwoordigt `#jy0l7nr4` de controlesom om de integriteit van de descriptor te verifiëren.


U weet nu alles over de werking van HD wallets in Bitcoin en het proces van het afleiden van sleutelparen. In de laatste hoofdstukken hebben we ons echter beperkt tot het genereren van private en publieke sleutels, zonder in te gaan op de constructie van ontvangstadressen. Dit is precies het onderwerp van het volgende hoofdstuk!


## Adressen ontvangen

<chapterId>ca80a89d-f8da-4e09-8c35-43179b65bced</chapterId>


Ontvangstadressen zijn stukjes informatie die in *scriptPubKey* zijn ingesloten om nieuw aangemaakte UTXO's te vergrendelen. Simpel gezegd dient een Address om bitcoins te ontvangen. Laten we eens kijken hoe ze werken in samenhang met wat we in de vorige hoofdstukken hebben bestudeerd.


### De rol van Bitcoin-adressen in scripts


Zoals eerder uitgelegd, is de rol van een transactie het Ownership van bitcoins overbrengen van inputs naar outputs. Dit proces omvat het consumeren van UTXO's als inputs en het creëren van nieuwe UTXO's als outputs. Deze UTXO's worden beveiligd door scripts, die de noodzakelijke voorwaarden definiëren om de fondsen te ontgrendelen.


Wanneer een gebruiker bitcoins ontvangt, maakt de verzender een UTXO aan en vergrendelt deze met een *scriptPubKey*. Dit script bevat de regels om de UTXO te ontgrendelen, meestal met vermelding van de vereiste handtekeningen en publieke sleutels. Om deze UTXO uit te geven in een nieuwe transactie, moet de gebruiker de gevraagde informatie verstrekken via een *scriptSig*. De uitvoering van *scriptSig* in combinatie met *scriptPubKey* moet "true" of `1` opleveren. Als aan deze voorwaarde is voldaan, kan de UTXO worden gebruikt om een nieuwe UTXO aan te maken, die zelf wordt vergrendeld door een nieuwe *scriptPubKey*, enzovoort.


![CYP201](assets/fr/054.webp)


Het is precies in de *scriptPubKey* dat de ontvangende adressen te vinden zijn. Het gebruik ervan varieert echter afhankelijk van de gebruikte scriptstandaard. Hier is een samenvattende tabel van de informatie in de *scriptPubKey* volgens de gebruikte standaard, evenals de informatie die verwacht wordt in de *scriptSig* om de *scriptPubKey* te ontgrendelen.


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

*Bron: Bitcoin Core PR review club, 7 juli 2021 - Gloria Zhao*


De opcodes die in een script worden gebruikt, zijn ontworpen om informatie te manipuleren en, indien nodig, te vergelijken of te testen. Laten we het voorbeeld nemen van een P2PKH script, dat er als volgt uitziet:


```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG
```


Zoals we in dit hoofdstuk zullen zien, vertegenwoordigt `<pubKeyHash>` eigenlijk de payload van de ontvangende Address die gebruikt wordt om de UTXO te locken. Om deze *scriptPubKey* te ontgrendelen, is het nodig om een *scriptSig* mee te geven:


```text
<signature> <public key>
```


In scripttaal is de stack een *LIFO* ("*Last In, First Out*") datastructuur die wordt gebruikt om Elements tijdelijk op te slaan tijdens de uitvoering van het script. Elke scriptbewerking manipuleert deze stack, waar Elements kan worden toegevoegd (*push*) of verwijderd (*pop*). Scripts gebruiken de stack om expressies te evalueren, tijdelijke variabelen op te slaan en voorwaarden te beheren.


De uitvoering van het script dat ik net als voorbeeld gaf, volgt dit proces:



- We hebben de *scriptSig*, de *scriptPubKey* en de stack:


![CYP201](assets/fr/055.webp)



- Het *scriptSig* wordt op de stack geduwd:


![CYP201](assets/fr/056.webp)



- `OP_DUP` dupliceert de openbare sleutel in *scriptSig* op de stack:


![CYP201](assets/fr/057.webp)



- `OP_HASH160` geeft de Hash van de openbare sleutel terug die zojuist gedupliceerd is:


![CYP201](assets/fr/058.webp)



- `OP_PUSHBYTES_20 <pubKeyHash>` duwt de Bitcoin Address die in de *scriptPubKey* staat op de stack:


![CYP201](assets/fr/059.webp)



- `OP_EQUALVERIFY` controleert of de gehashte openbare sleutel overeenkomt met de verstrekte ontvangende Address:


![CYP201](assets/fr/060.webp)


`OP_CHECKSIG` controleert de handtekening in het *scriptSig* met behulp van de publieke sleutel. Deze opcode voert in wezen een handtekeningverificatie uit zoals we beschreven in deel 3 van deze training:



![CYP201](assets/fr/061.webp)



- Als `1` op de stack blijft staan, dan is het script geldig:


![CYP201](assets/fr/062.webp)


Samengevat maakt dit script het dus mogelijk om met behulp van de digitale handtekening te verifiëren dat de gebruiker die Ownership van deze UTXO claimt en het wil uitgeven, inderdaad de private sleutel bezit die geassocieerd is met de ontvangende Address die gebruikt is tijdens het aanmaken van deze UTXO.


### De verschillende soorten Bitcoin adressen


In de loop van de evolutie van de Bitcoin zijn er verschillende standaard scriptmodellen toegevoegd. Elk daarvan maakt gebruik van een ander type ontvangende Address. Hier volgt een overzicht van de belangrijkste scriptmodellen die tot op heden beschikbaar zijn:


**P2PK (*Pay-to-PubKey*)**:


Dit scriptmodel werd geïntroduceerd in de eerste versie van Bitcoin door Satoshi Nakamoto. Het P2PK-script vergrendelt bitcoins rechtstreeks met behulp van een onbewerkte openbare sleutel (er wordt dus geen ontvangende Address gebruikt bij dit model). De structuur is eenvoudig: het bevat een openbare sleutel en vereist een overeenkomstige digitale handtekening om de fondsen te ontgrendelen. Dit script maakt deel uit van de "*Legacy*" standaard.


**P2PKH (*Pay-to-PubKey-Hash*)**:


Net als P2PK werd het P2PKH-script geïntroduceerd bij de lancering van Bitcoin. In tegenstelling tot zijn voorganger, vergrendelt het de bitcoins door gebruik te maken van de Hash van de publieke sleutel, in plaats van direct gebruik te maken van de ruwe publieke sleutel. Het *scriptSig* moet dan de publieke sleutel leveren die geassocieerd is met de ontvangende Address, evenals een geldige handtekening. De adressen die overeenkomen met dit model beginnen met `1` en zijn gecodeerd in *base58check*. Dit script behoort ook tot de "*Legacy*" standaard.


**P2SH (*Pay-to-Script-Hash*)**:


Het P2SH model, geïntroduceerd in 2012 met BIP16, maakt het mogelijk om de Hash van een willekeurig script te gebruiken in de *scriptPubKey*. Dit gehashte script, genaamd "*redeemscript*", bevat de voorwaarden voor het ontgrendelen van het geld. Om een UTXO uit te geven die vergrendeld is met P2SH, is het nodig om een *scriptSig* aan te leveren die de originele *redeemscript* bevat, evenals de benodigde gegevens om het te valideren. Dit model wordt met name gebruikt voor oude multisigs. De adressen geassocieerd met P2SH beginnen met `3` en zijn gecodeerd in *base58check*. Dit script behoort ook tot de "*Legacy*" standaard.


**P2WPKH (*Pay-to-Witness-PubKey-Hash*)**:


Dit script lijkt op P2PKH, omdat het ook bitcoins vergrendelt met behulp van de Hash van een publieke sleutel. Echter, in tegenstelling tot P2PKH, is het *scriptSig* verplaatst naar een aparte sectie genaamd "*Witness*". Dit wordt soms "*scriptWitness*" genoemd om de set aan te duiden die bestaat uit de handtekening en de publieke sleutel. Elke SegWit invoer heeft zijn eigen *scriptWitness* en de verzameling *scriptWitnesses* vormt het *Witness* veld van de transactie. Deze verplaatsing van handtekeninggegevens is een innovatie die is geïntroduceerd door de SegWit update, met name gericht op het voorkomen van de vervormbaarheid van transacties door ECDSA handtekeningen.

P2WPKH adressen gebruiken *bech32* codering en beginnen altijd met `bc1q`. Dit type script komt overeen met versie 0 SegWit uitgangen.


**P2WSH (*Pay-to-Witness-Script-Hash*)**:


Het P2WSH-model werd ook geïntroduceerd met de SegWit update in augustus 2017. Vergelijkbaar met het P2SH model, vergrendelt het bitcoins met behulp van de Hash van een script. Het belangrijkste verschil zit in de manier waarop handtekeningen en scripts in de transactie worden opgenomen. Om bitcoins te vergrendelen met dit type script, moet de ontvanger het originele script leveren, genaamd *witnessScript* (gelijk aan *redeemscript* in P2SH), samen met de benodigde gegevens om dit *witnessScript* te valideren. Dit mechanisme maakt de implementatie van complexere bestedingsvoorwaarden mogelijk, zoals multisigs.


P2WSH adressen gebruiken *bech32* codering en beginnen altijd met `bc1q`. Dit script komt ook overeen met versie 0 SegWit uitvoer.


**P2TR (*Pay-to-Taproot*)**:


Het P2TR model werd geïntroduceerd met de implementatie van Taproot in november 2021. Het is gebaseerd op het Schnorr-protocol voor cryptografische sleutelaggregatie, en op een Merkle Tree voor alternatieve scripts, genaamd MAST (*Merkelized Alternative Script Tree*). In tegenstelling tot andere typen scripts, waarbij de bestedingsvoorwaarden openbaar worden gemaakt (bij ontvangst of besteding), maakt P2TR het mogelijk om complexe scripts te verbergen achter een enkele, schijnbare openbare sleutel.


Technisch gezien vergrendelt een P2TR script bitcoins op een unieke Schnorr publieke sleutel, aangeduid als $Q$. Deze sleutel $Q$ is eigenlijk een aggregaat van een publieke sleutel $P$ en een publieke sleutel $M$, de laatste wordt berekend uit de Merkle Root van een lijst met *scriptPubKey*. Bitcoins die met dit type script zijn vergrendeld, kunnen op twee manieren worden uitgegeven:


- Door een handtekening te publiceren voor de openbare sleutel $P$ (*sleutelpad*).
- Door te voldoen aan een van de scripts in de Merkle Tree (*scriptpad*).


P2TR biedt dus een grote flexibiliteit, omdat bitcoins kunnen worden vergrendeld met een unieke publieke sleutel, met meerdere scripts naar keuze, of met beide tegelijk. Het voordeel van deze Merkle Tree structuur is dat alleen het gebruikte uitgavenscript wordt onthuld tijdens de transactie, maar dat alle andere alternatieve scripts geheim blijven.


![CYP201](assets/fr/063.webp)


P2TR komt overeen met versie 1 SegWit uitgangen, wat betekent dat de handtekeningen voor P2TR ingangen worden opgeslagen in de *Witness* sectie van de transactie, en niet in de *scriptSig*. P2TR adressen gebruiken de *bech32m* codering en beginnen met `bc1p`, maar ze zijn vrij uniek omdat ze geen Hash functie gebruiken voor hun constructie. Ze vertegenwoordigen namelijk direct de publieke sleutel $Q$ die eenvoudigweg geformatteerd is met metadata. Het is daarom een scriptmodel dat dicht in de buurt komt van P2PK.


Nu we de theorie behandeld hebben, gaan we over naar de praktijk! In het volgende hoofdstuk stel ik voor om zowel een SegWit v0 Address als een SegWit v1 Address af te leiden uit een paar sleutels.


## Address Afleiding

<chapterId>3ebdc750-4135-4881-b07e-08965941b93e</chapterId>


Laten we samen onderzoeken hoe we generate een ontvangende Address kunnen maken van een paar sleutels die zich bijvoorbeeld op diepte 5 van een HD Wallet bevinden. Deze Address kan dan gebruikt worden in een Wallet software om een UTXO te vergrendelen.


Aangezien het genereren van een Address afhankelijk is van het gebruikte scriptmodel, concentreren we ons op twee specifieke gevallen: het genereren van een SegWit v0 Address in P2WPKH en een SegWit v1 Address in P2TR. Deze twee soorten adressen dekken de overgrote meerderheid van het huidige gebruik.


### Openbare sleutel compressie


Na het uitvoeren van alle afleidingsstappen van de hoofdsleutel tot diepte 5 met behulp van de juiste indexen, verkrijgen we een sleutelpaar ($k$, $K$) met $K = k cdot G$. Hoewel het mogelijk is om deze publieke sleutel te gebruiken om fondsen te vergrendelen met de P2PK standaard, is dat hier niet ons doel. In plaats daarvan willen we in eerste instantie een Address maken in P2WPKH, en daarna in P2TR voor een ander voorbeeld.


De eerste stap is het comprimeren van de openbare sleutel $K$. Om dit proces goed te begrijpen, herinneren we ons eerst enkele basisprincipes uit deel 3.

Een publieke sleutel in Bitcoin is een punt $K$ gelegen op een elliptische curve. Het wordt weergegeven in de vorm $(x, y)$, waarbij $x$ en $y$ de coördinaten van het punt zijn. In ongecomprimeerde vorm is deze openbare sleutel 520 bits groot: 8 bits voor een prefix (initiële waarde van `0x04`), 256 bits voor de coördinaat $x$ en 256 bits voor de coördinaat $y$.

Elliptische krommen hebben echter een symmetrie-eigenschap ten opzichte van de x-as: voor een gegeven coördinaat van $x$ zijn er slechts twee mogelijke waarden voor $y$: $y$ en $-y$. Deze twee punten liggen aan weerszijden van de x-as. Met andere woorden, als we $x$ kennen, is het voldoende om aan te geven of $y$ even of oneven is om het exacte punt op de kromme te bepalen.


![CYP201](assets/fr/064.webp)


Om een openbare sleutel te comprimeren, wordt alleen $x$ gecodeerd, die 256 bits in beslag neemt, en wordt een prefix toegevoegd om de pariteit van $y$ te specificeren. Deze methode verkleint de grootte van de openbare sleutel tot 264 bits in plaats van de oorspronkelijke 520. Het voorvoegsel `0x02` geeft aan dat $y$ even is en het voorvoegsel `0x03` geeft aan dat $y$ oneven is.


Laten we een voorbeeld nemen om het goed te begrijpen, met een onbewerkte openbare sleutel in ongecomprimeerde weergave:


```text
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```


Als we deze sleutel ontleden, hebben we:


   - Het voorvoegsel: `04`;
   - $x$: `678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6`;
   - $y$: `49f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f`


Het laatste hexadecimale teken van $y$ is `f`. In basis 10 is `f = 15`, wat overeenkomt met een oneven getal. Daarom is $y$ oneven en wordt het voorvoegsel `0x03` om dit aan te geven.


De gecomprimeerde openbare sleutel wordt:


```text
K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6
```

Deze bewerking geldt voor alle scriptmodellen die gebaseerd zijn op ECDSA, dat wil zeggen, alle behalve P2TR die Schnorr gebruikt. In het geval van Schnorr, zoals uitgelegd in deel 3, behouden we alleen de waarde van $x$, zonder een prefix toe te voegen om de pariteit van $y$ aan te geven, in tegenstelling tot ECDSA. Dit wordt mogelijk gemaakt door het feit dat een unieke pariteit willekeurig wordt gekozen voor alle sleutels. Hierdoor is er iets minder opslagruimte nodig voor openbare sleutels.

### Afleiding van een SegWit v0 (bech32) Address


Nu we onze gecomprimeerde publieke sleutel hebben, kunnen we hieruit een SegWit v0 afleiden die Address ontvangt.


De eerste stap is het toepassen van de HASH160 Hash functie op de gecomprimeerde openbare sleutel. HASH160 is een samenstelling van twee opeenvolgende Hash functies: SHA256, gevolgd door RIPEMD160:



$$

\text{HASH160}(K) = \text{RIPEMD160}(\text{SHA256}(K))

$$


Eerst halen we de sleutel door SHA256:


```text
SHA256(K) = C489EBD66E4103B3C4B5EAFF462B92F5847CA2DCE0825F4997C7CF57DF35BF3A
```


Vervolgens geven we het resultaat door aan RIPEMD160:


```text
RIPEMD160(SHA256(K)) = 9F81322CC88622CA4CCB2A52A21E2888727AA535
```


We hebben een 160-bit Hash van de publieke sleutel verkregen, die de zogenaamde payload van de Address vormt. Deze payload vertegenwoordigt het centrale en belangrijkste deel van de Address. Het wordt ook gebruikt in het *scriptPubKey* om de UTXO's te vergrendelen.


Om deze payload echter gemakkelijker bruikbaar te maken voor mensen, wordt er metadata aan toegevoegd. De volgende stap is het coderen van deze Hash in groepen van 5 bits in decimaal. Deze decimale transformatie zal nuttig zijn voor de conversie naar *bech32*, gebruikt door post-SegWit adressen. De 160-bits binaire Hash wordt dus verdeeld in 32 groepen van 5 bits:



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

Dus we hebben:


```text
HASH = 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21
```


Nadat de Hash in groepen van 5 bits is gecodeerd, wordt een controlesom aan de Address toegevoegd. Deze controlesom wordt gebruikt om te controleren of de payload van de Address niet is gewijzigd tijdens opslag of verzending. Zo kan een Wallet-software bijvoorbeeld controleren of je geen typefout hebt gemaakt bij het invoeren van een ontvangen Address. Zonder deze verificatie zou je per ongeluk bitcoins naar een verkeerde Address kunnen sturen, wat resulteert in een permanent verlies van fondsen, omdat je niet de eigenaar bent van de bijbehorende publieke of private sleutel. Daarom is de controlesom een bescherming tegen menselijke fouten.


Voor de oude Bitcoin *Legacy* adressen werd de controlesom eenvoudig berekend vanaf het begin van de Address Hash met de HASH256 functie. Met de introductie van SegWit en het *bech32* formaat, worden nu BCH codes (*Bose, Ray-Chaudhuri en Hocquenghem*) gebruikt. Deze foutcorrigerende codes worden gebruikt om fouten in gegevensreeksen op te sporen en te corrigeren. Ze zorgen ervoor dat de verzonden informatie intact aankomt op de bestemming, zelfs in het geval van kleine wijzigingen. BCH-codes worden op veel gebieden gebruikt, zoals SSD's, dvd's en QR-codes. Dankzij deze BCH-codes kan bijvoorbeeld een gedeeltelijk verborgen QR-code nog steeds worden gelezen en gedecodeerd.


In de context van Bitcoin bieden BCH-codes een beter compromis tussen grootte en foutdetectiecapaciteit vergeleken met de eenvoudige Hash functies die gebruikt worden voor *Legacy* adressen. In Bitcoin worden BCH-codes echter alleen gebruikt voor foutdetectie, niet voor correctie. Dus, Wallet software zal een onjuist ontvangen Address signaleren, maar niet automatisch corrigeren. Deze beperking is opzettelijk: het toestaan van automatische correctie zou de foutdetectiecapaciteit verminderen.


Om de checksum met BCH-codes te berekenen, moeten we verschillende Elements voorbereiden.


- De HRP (**Human Readable Part**): Voor de Bitcoin Mainnet is de HRP `bc`;


De HRP moet worden uitgebreid door elk teken in twee delen te scheiden:


- De karakters van de HRP in ASCII nemen:
 - `b`: `01100010`
 - `c`: `01100011`
- De 3 meest significante bits en de 5 minst significante bits extraheren:
  - 3 meest significante bits: `011` (3 in decimaal)
  - 3 meest significante bits: `011` (3 in decimaal)
  - 5 minst significante bits: `00010` (2 in decimaal)
  - 5 minst significante bits: `00011` (3 in decimaal)


Met het scheidingsteken `0` tussen de twee tekens is de HRP-extensie dus:


```text
03 03 00 02 03
```



- **De getuigeversie**: Voor SegWit versie 0 is dit `00`;



- **De payload**: De decimale waarden van de openbare sleutel Hash;



- De reservering voor de controlesom: We voegen 6 nullen `[0, 0, 0, 0, 0, 0]` toe aan het einde van de reeks.


Alle gecombineerde gegevens om in te voeren in het programma om de controlesom te berekenen zijn als volgt:


```text
HRP = 03 03 00 02 03
SEGWIT v0 = 00
HASH = 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21
CHECKSUM = 00 00 00 00 00 00

INPUT = 03 03 00 02 03 00 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21 00 00 00 00 00 00
```


De berekening van de checksum is behoorlijk complex. Er komt polynomiale eindige veldrekening bij kijken. We zullen deze berekening hier niet in detail bespreken en direct naar het resultaat gaan. In ons voorbeeld is de verkregen checksum in decimalen:


```text
10 16 11 04 13 18
```


We kunnen nu de ontvangende Address construeren door de volgende Elements in volgorde aan elkaar te rijgen:


- De SegWit versie: `00`
- **De payload**: De publieke sleutel Hash
- De controlesom: De waarden verkregen in de vorige stap (`10 16 11 04 13 18`)


Dit geeft ons in decimalen:


```text
00 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21 10 16 11 04 13 18
```


Vervolgens moet elke decimale waarde worden omgezet naar het *bech32* teken met behulp van de volgende conversietabel:



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


Om een waarde om te zetten in een _bech32_ teken met behulp van deze tabel, zoek je gewoon de waarden in de eerste kolom en de eerste rij die, wanneer ze bij elkaar opgeteld worden, het gewenste resultaat opleveren. Haal dan het corresponderende teken op. Bijvoorbeeld, het decimale getal `19` wordt omgezet in de letter `n`, omdat $19 = 16 + 3$.


Door al onze waarden in kaart te brengen, krijgen we de volgende Address:


```
qn7qnytxgsc3v5nxt9ff2y83g3pe84ff42stydj
```


Alles wat overblijft is het toevoegen van de HRP `bc`, die aangeeft dat het een Address is voor de Bitcoin Mainnet, en het scheidingsteken `1`, om de volledige ontvangende Address te krijgen:


```
bc1qn7qnytxgsc3v5nxt9ff2y83g3pe84ff42stydj
```


Het bijzondere aan dit _bech32_ alfabet is dat het alle alfanumerieke tekens bevat behalve `1`, `b`, `i` en `o` om visuele verwarring tussen gelijksoortige tekens te voorkomen, vooral tijdens het invoeren of lezen door mensen.


Samengevat is dit het afleidingsproces:


![CYP201](assets/fr/065.webp)


Dit is hoe je een P2WPKH (SegWit v0) die Address ontvangt, kunt afleiden uit een paar sleutels. Laten we nu verder gaan met P2TR (SegWit v1 / Taproot) adressen en hun generatieproces ontdekken.


### Afleiding van een SegWit v1 (bech32m) Address


Voor Taproot adressen verschilt het generatieproces enigszins. Laten we hier samen naar kijken!


Vanaf de stap van de compressie van de openbare sleutel verschijnt er een eerste verschil met ECDSA: de openbare sleutels die voor Schnorr in Bitcoin worden gebruikt, worden alleen weergegeven door hun abscis ($x$). Daarom is er geen prefix en is de gecomprimeerde sleutel precies 256 bits groot.

Zoals we in het vorige hoofdstuk zagen, vergrendelt een P2TR script bitcoins op een unieke Schnorr publieke sleutel, aangeduid met $Q$. Deze sleutel $Q$ is een aggregaat van twee publieke sleutels: $P$, een hoofd interne publieke sleutel, en $M$, een publieke sleutel afgeleid van de Merkle Root van een lijst van _scriptPubKey_. De bitcoins die met dit type script zijn vergrendeld, kunnen op twee manieren worden uitgegeven:



- Door een handtekening te publiceren voor de openbare sleutel $P$ (_key path_);
- Door te voldoen aan een van de scripts die zijn opgenomen in de Merkle Tree (_scriptpad_).


In werkelijkheid zijn deze twee sleutels niet echt "samengevoegd" De sleutel $P$ wordt in plaats daarvan getweakt door de sleutel $M$. In cryptografie betekent het "tweaken" van een openbare sleutel het wijzigen van deze sleutel door een additieve waarde toe te passen die een "tweak" wordt genoemd Deze operatie zorgt ervoor dat de gewijzigde sleutel compatibel blijft met de originele privésleutel en de tweak. Technisch gezien is een tweak een scalaire waarde $t$ die wordt toegevoegd aan de oorspronkelijke openbare sleutel. Als $P$ de originele openbare sleutel is, wordt de aangepaste sleutel:



$$

P' = P + t \cdot G

$$


Waarbij $G$ de generator van de gebruikte elliptische curve is. Deze bewerking produceert een nieuwe openbare sleutel die is afgeleid van de originele sleutel, met behoud van de cryptografische eigenschappen die het gebruik ervan toestaan.


Als u geen alternatieve scripts hoeft toe te voegen (uitsluitend uitgeven via het _sleutelpad_), kunt u generate een Taproot Address opzetten, die uitsluitend gebaseerd is op de publieke sleutel die op diepte 5 van uw Wallet aanwezig is. In dit geval is het nodig om een niet-uitgeefbaar script te maken voor het _scriptpad_, om aan de eisen van de structuur te voldoen. De tweak $t$ wordt dan berekend door een Hash functie, **`TapTweak`**, toe te passen op de interne publieke sleutel $P$:



$$

t = \text{H}_{\text{TapTweak}}(P)

$$


waar:



- **${H}_{TapTweak}$** is een SHA256 Hash functie getagd met de tag `TapTweak`. Als je niet bekend bent met wat een getagde Hash functie is, raadpleeg dan hoofdstuk 3.3;
- $P$ is de interne openbare sleutel, weergegeven in het gecomprimeerde 256-bits formaat, waarbij alleen de coördinaat $x$ wordt gebruikt.


De Taproot publieke sleutel $Q$ wordt dan berekend door de tweak $t$, vermenigvuldigd met de elliptische curvegenerator $G$, toe te voegen aan de interne publieke sleutel $P$:



$$

Q = P + t \cdot G

$$


Zodra de Taproot publieke sleutel $Q$ verkregen is, kunnen we generate de overeenkomstige ontvangende Address. In tegenstelling tot andere formaten, worden Taproot-adressen niet vastgelegd op een Hash van de openbare sleutel. Daarom wordt de sleutel $Q$ direct in de Address geplaatst, op een onbewerkte manier.


Om te beginnen extraheren we de $x$ coördinaat van het punt $Q$ om een gecomprimeerde publieke sleutel te verkrijgen. Op deze payload wordt een checksum berekend met BCH codes, net als bij SegWit v0 adressen. Het programma dat gebruikt wordt voor Taproot adressen verschilt echter enigszins. Na de introductie van het _bech32_ formaat met SegWit werd namelijk een bug ontdekt: wanneer het laatste teken van een Address een `p` is, maakt het invoegen of verwijderen van `q`s vlak voor deze `p` de controlesom niet ongeldig. Hoewel deze bug geen gevolgen heeft voor SegWit v0 (dankzij een beperking in grootte), zou het in de toekomst een probleem kunnen vormen. Deze bug is daarom gecorrigeerd voor Taproot adressen, en het nieuwe gecorrigeerde formaat heet "_bech32m_".


De Taproot Address wordt gegenereerd door de $x$ coördinaat van $Q$ te coderen in het _bech32m_ formaat, met de volgende Elements:



- Het HRP (_Human Readable Part_): `bc`, om het hoofdnetwerk van Bitcoin aan te geven;
- De **versie**: `1` om Taproot / SegWit v1 aan te geven;
- De controlesom.


De uiteindelijke Address zal daarom het formaat hebben:


```
bc1p[Qx][checksum]
```


Aan de andere kant, als je alternatieve scripts wilt toevoegen naast de uitgaven met de interne openbare sleutel (_scriptpad_), zal de berekening van de ontvangende Address iets anders zijn. Je moet de Hash van de alternatieve scripts opnemen in de berekening van de tweak. In Taproot wordt elk alternatief script, dat zich aan het einde van de Merkle Tree bevindt, een "blad" genoemd.


Als de verschillende alternatieve scripts geschreven zijn, moet je ze afzonderlijk door een Hash functie `TapLeaf` laten lopen, samen met wat metadata:



$$

\text{h}_{\text{leaf}} = \text{H}_{\text{TapLeaf}} (v \Vert sz \Vert S)

$$


Met:



- $v$: het versienummer van het script (standaard `0xC0` voor Taproot);
- $sz$: de grootte van het script gecodeerd in _CompactSize_ formaat;
- $S$: het script.


De verschillende scripthashes (${h}_{{leaf}}) worden eerst in lexicografische volgorde gesorteerd. Daarna worden ze paarsgewijs samengevoegd en door een Hash functie `TapBranch` gehaald. Dit proces wordt iteratief herhaald om stap voor stap de Merkle Tree op te bouwen:

$$

\text{h}_{\text{branch}} = \text{H}_{\text{TapBranch}}(\text{h}_{\text{leaf1}} \Vert \text{h}_{\text{leaf2}})

$$


We gaan dan verder door de resultaten twee aan twee aan elkaar te rijgen en ze bij elke stap door de Hash functie `TapBranch` te halen, totdat we de Merkle Tree wortel verkrijgen:


![CYP201](assets/fr/066.webp)


Zodra de Merkle Root $h_{{root}}$ berekend is, kunnen we de tweak berekenen. Hiervoor concateneren we de interne publieke sleutel van de Wallet $P$ met de root $h_{{\text{root}}$, en sturen het geheel door de getagde Hash functie `TapTweak`:



$$

t = \text{H}_{\text{TapTweak}}(P \Vert h_{\text{root}})

$$


Tenslotte wordt, zoals eerder, de Taproot publieke sleutel $Q$ verkregen door de interne publieke sleutel $P$ op te tellen bij het product van de tweak $t$ door het generatorpunt $G$:



$$

Q = P + t \cdot G

$$

Daarna volgt het genereren van de Address hetzelfde proces, met de ruwe publieke sleutel $Q$ als payload, vergezeld van wat extra metadata.


En daar heb je het! We zijn aan het einde gekomen van deze CYP201 cursus. Als je deze cursus nuttig vond, zou ik je erg dankbaar zijn als je even de tijd neemt om de cursus een goede beoordeling te geven in het volgende evaluatiehoofdstuk. Voel je vrij om het ook te delen met je dierbaren of op je sociale netwerken. Tot slot, als je je diploma voor deze cursus wilt behalen, kun je direct na het evaluatiehoofdstuk het eindexamen doen.

# Laatste Sectie

<partId>58111408-b734-54db-9ea7-0d5b67f99f99</partId>


## Beoordelingen

<chapterId>0cd71541-a7fd-53db-b66a-8611b6a28b04</chapterId>

<isCourseReview>true</isCourseReview>

## Eindexamen

<chapterId>a53ea27d-0f84-56cd-b37c-a66210a4b31d</chapterId>

<isCourseExam>true</isCourseExam>

## Conclusie

<chapterId>d291428b-3cfa-5394-930e-4b514be82d5a</chapterId>

<isCourseConclusion>true</isCourseConclusion>