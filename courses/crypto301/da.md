---
name: Introduktion til Kryptografi
goal: Forstå oprettelsen af en Bitcoin-pung fra et kryptografisk perspektiv
objectives:
  - Afmystificer terminologien inden for kryptografi relateret til Bitcoin.
  - Mestre oprettelsen af en Bitcoin-pung.
  - Forstå strukturen af en Bitcoin-pung.
  - Forstå adresser og afledningsstier.
---

# En rejse ind i kryptografi

Er du fascineret af Bitcoin? Undrer du dig over, hvordan en Bitcoin-pung fungerer? Gør dig klar til at begive dig ud på en fængslende rejse ind i kryptografi! Vores ekspert, Loïc, vil guide dig gennem de komplekse processer ved oprettelsen af en Bitcoin-pung og afsløre mysterierne bag skræmmende tekniske termer som hashing, nøgleafledning og elliptiske kurver.

Denne træning vil ikke kun ruste dig med viden til at forstå strukturen af en Bitcoin-pung, men også forberede dig på at dykke dybere ned i den spændende verden af kryptografi. Så er du klar til at begive dig ud på denne rejse? Deltag i os og omsæt din nysgerrighed til ekspertise!

+++

# Introduktion

## Introduktion til Kryptografi

### Er denne træning noget for dig? JA!

![introduktion af Rogzy](https://youtu.be/ul8zU5QWIXg)

Vi er glade for at byde dig velkommen til det nye træningskursus med titlen "Crypto 301: Introduktion til Kryptografi og HD-pung", orkestreret af eksperten selv, Loïc Morel. Dette kursus vil nedsænke dig i kryptografins fascinerende verden, den grundlæggende disciplin inden for matematik, der sikrer krypteringen og sikkerheden af dine data.

I vores dagligdag, og især inden for Bitcoin-verdenen, spiller kryptografi en afgørende rolle. Koncepter relateret til kryptografi såsom private nøgler, offentlige nøgler, adresser, afledningsstier, seed og entropi er hjertet af brugen og oprettelsen af en Bitcoin-pung. I løbet af dette kursus vil Loïc forklare detaljeret, hvordan private nøgler genereres, og hvordan de er forbundet med adresser. Loïc vil også afsætte en time til at forklare de matematiske detaljer vedrørende elliptiske kurver, denne komplekse matematiske kurve. Derudover vil du forstå, hvorfor brugen af HMAC SHA512 er vigtig for at sikre din pung, og hvad forskellen er mellem seed og mnemonisk frase.

Det ultimative mål med denne træning er at give dig mulighed for at forstå de tekniske processer ved oprettelsen af en HD-pung og de kryptografiske metoder, der anvendes. Gennem årene er Bitcoin-punge udviklet til at blive nemmere at bruge, mere sikre og standardiserede takket være specifikke BIP'er. Loïc vil hjælpe dig med at forstå disse BIP'er for at forstå de valg, der er truffet af Bitcoin-udviklere og kryptografer. Som med alle træningstilbud fra vores universitet er denne helt gratis og åben kilde. Det betyder, at du frit kan tage det og bruge det, som du ønsker. Vi ser frem til at modtage dine tilbagemeldinger ved afslutningen af dette spændende kursus.

### Ordet er dit, professor!

![intro af loïc](https://youtu.be/mwuxXLk4Kws)

Hej alle sammen, jeg er Loïc Morel, jeres guide gennem denne tekniske udforskning af kryptografien, der anvendes i Bitcoin-punge.

Vores rejse begynder med et dyk ned i dybet af kryptografiske hashfunktioner. Sammen vil vi dissekere de indre mekanismer i den essentielle SHA256 og udforske forskellige algoritmer dedikeret til afledning.

Vi vil fortsætte vores eventyr ved at afkode den mystiske verden af digitale signaturer. Du vil opdage, hvordan magien ved elliptiske kurver anvendes på disse signaturer, og vi vil kaste lys over, hvordan man beregner den offentlige nøgle ud fra den private nøgle. Og selvfølgelig vil vi også beskæftige os med handlingen at signere med den private nøgle.
Dernæst vil vi gå tilbage i tiden for at se udviklingen af Bitcoin-wallets, og vi vil dykke ned i begreberne om entropi og tilfældige tal. Vi vil gennemgå den berømte mnemoniske sætning og undersøge emnet om adgangskoder. Du vil endda have mulighed for at opleve noget unikt ved at oprette en seed fra 128 terningekast!

Med disse solide fundament vil vi være klar til den afgørende del: at oprette en Bitcoin-wallet. Fra fødslen af seedet og master-nøglen til studiet af udvidede nøgler og afledning af børnenøglepar vil vi dissekere hvert trin. Vi vil også diskutere walletens struktur og afledningsstier.

For at toppe det hele afslutter vi vores rejse med at undersøge Bitcoin-adresser. Vi vil forklare, hvordan de oprettes, og hvordan de spiller en essentiel rolle i Bitcoin-wallets funktion.

Tag med mig på denne fængslende rejse og gør dig klar til at udforske kryptoverdenen som aldrig før. Lad dine fordomme blive udenfor og åbn dit sind for en ny måde at forstå Bitcoin og dets fundamentale struktur på.

# Hashfunktioner

## Introduktion til kryptografiske hashfunktioner relateret til Bitcoin

![2.1 - Kryptografiske Hashfunktioner](https://youtu.be/dvnGArYvVr8)

Velkommen til dagens session, der er dedikeret til en dybdegående fordybelse i den kryptografiske verden af hashfunktioner, en essentiel hjørnesten i Bitcoin-protokollens sikkerhed. Forestil dig en hashfunktion som en ultrahurtig kryptografisk afkodningsrobot, der omdanner information af alle størrelser til et unikt og fast digitalt fingeraftryk kaldet en "hash". I løbet af vores udforskning vil vi beskrive profil af kryptografiske hashfunktioner, fremhæve deres anvendelse i Bitcoin-protokollen og definere de specifikke mål, som disse kryptografiske funktioner skal opnå.

![billede](assets/image/section1/0.JPG)

For at beskrive profilen af kryptografiske hashfunktioner kræves forståelse af to essentielle egenskaber: deres uigenkaldelighed og deres modstand mod forfalskning. Hver kryptografisk hashfunktion er som en unik kunstner, der producerer en forskellig "hash" for hver indtastning. Selv en let afvigende pensel ændrer markant det endelige maleri, dvs. hashen. Disse funktioner fungerer som digitale vogtere, der verificerer integriteten af downloadet software. En anden afgørende egenskab, de besidder, er deres modstand mod kollisioner. Selvfølgelig er kollisioner uundgåelige i hashverdenen, men en fremragende kryptografisk hashfunktion minimerer dem betydeligt. Det er som om, at hver hash er et hus i en stor by; på trods af det enorme antal huse sikrer en god hashfunktion, at hvert hus har en unik adresse.

![billede](assets/image/section1/1.JPG)

Lad os nu navigere i de turbulente farvande af forældede hashfunktioner. SHA0, SHA1 og MD5 betragtes nu som rustne relikvier i havet af kryptografisk hashning. De frarådes ofte, da de har mistet deres modstand mod kollisioner. Principperne om skuffer forklarer, hvorfor kollisionsundgåelse er umulig på trods af vores bedste bestræbelser på grund af begrænsningen af outputstørrelsen. Det er også vigtigt at bemærke, at modstand mod anden forbillede er afhængig af modstand mod kollisioner. For at blive betragtet som virkelig sikker skal en hashfunktion modstå kollisioner, anden forbillede og forbillede.

En nøglekomponent i Bitcoin-protokollen er SHA-256 hashfunktionen, der er kaptajnen på skibet. Andre funktioner som SHA-512 bruges til afledning med HMAC og PBKDF. Derudover bruges RIPMD160 til at reducere et fingeraftryk til 160 bit. Når vi taler om HASH256 og HASH160, henviser vi til brugen af dobbelt hashning med SHA-256 og RIPMD. Brugen af HASH160 er særlig fordelagtig, da det tillader sikkerheden ved SHA-256 samtidig med at størrelsen af fingeraftrykket reduceres.
For at opsummere er det ultimative mål for en kryptografisk hashfunktion at omdanne vilkårligt stor information til et fast størrelse fingeraftryk. For at blive anerkendt som sikker skal den have flere styrker: irreversibilitet, modstand mod forfalskning, modstand mod kollisioner og modstand mod anden forudbilleder.
![image](assets/image/section1/2.JPG)

Ved afslutningen af denne udforskning har vi afmystificeret kryptografiske hashfunktioner, fremhævet deres anvendelse i Bitcoin-protokollen og dissekeret deres specifikke mål. Vi har lært, at hashfunktioner for at blive betragtet som sikre skal være modstandsdygtige over for forudbilleder, anden forudbilleder, kollisioner og forfalskning. Vi har også dækket det udvalg af forskellige hashfunktioner, der anvendes i Bitcoin-protokollen. I vores næste session vil vi dykke ned i kernen af SHA256 hashfunktionen og opdage den fascinerende matematik, der giver den sine unikke egenskaber.

## SHA256's indre funktioner

![SHA256's indre funktioner](https://youtu.be/74SWg_ZbUj4)

Velkommen til fortsættelsen af vores fascinerende rejse gennem de kryptografiske labyrinter af hashfunktionen. I dag afslører vi mysterierne om SHA256, en kompleks men genial proces, som vi introducerede i vores tidligere diskussion om hashfunktioner. Lad os tage endnu et skridt ind i denne labyrint og begynde med forbehandlingen af SHA256. Forestil dig forbehandling som forberedelsen af en lækker ret, hvor vi tilføjer "padding bits" for at få størrelsen af vores hovedingrediens, inputtet, til at nå et perfekt multiplum af 512 bits. Alt dette med det ultimative mål at generere en saftig 256-bit hash fra en variabel-størrelse ingrediens.

![image](assets/image/section1/3.JPG)
![image](assets/image/section1/4.JPG)

I denne kryptografiske opskrift leger vi med bits, hvor vi har en indledende beskedstørrelse, som vi vil kalde M. Ét bit er reserveret til separator, mens P bits bruges til padding. Derudover sætter vi 64 bits til side til den anden forbehandlingsfase. Det samlede antal bits skal være et multiplum af 512 bits. Det er lidt ligesom at sikre, at alle ingredienserne blander sig perfekt i vores ret.

![image](assets/image/section1/5.JPG)

Nu går vi videre til den anden fase af forbehandlingen, som involverer tilføjelse af den binære repræsentation af den indledende beskedstørrelse, i bits. Til dette bruger vi vores 64 reserverede bits fra det foregående trin. Vi tilføjer nuller for at afrunde vores 64 bits til vores afbalancerede input. Derefter fusionerer vi den indledende besked, padding bits og størrelsespaddingen som ingredienser i en blender for at opnå vores afbalancerede input.

![image](assets/image/section1/6.JPG)

Nu forbereder vi os på de første trin i SHA-256 funktionens behandling. Som i enhver god opskrift har vi brug for nogle grundlæggende ingredienser, som vi kalder konstanter og initialiseringsvektorer. Initialiseringsvektorerne, fra A til H, er de første 32 bits af decimaldelen af kvadratrødderne af de første 8 primtal. Konstanterne K, fra 0 til 63, repræsenterer de første 32 bits af decimaldelen af kubikrødderne af de første 64 primtal.

![image](assets/image/section1/7.JPG)

Inden for komprimeringsfunktionen bruger vi specifikke operatorer som XOR, AND og NOT. Vi behandler bitsene én efter én i henhold til deres rang ved hjælp af XOR-operatoren og en sandhedstabel. AND-operatoren bruges til kun at returnere 1, hvis begge operandere er lig med 1, og NOT-operatoren bruges til at returnere den modsatte værdi af en operand. Vi bruger også SHR-operationen til at skifte bitsene til højre med et valgt antal.

![image](assets/image/section1/8.JPG)
Endelig, efter at have opdelt den afbalancerede indgang i forskellige blokke af 512-bit beskeder, udfører vi 64 runder af beregning i komprimeringsfunktionen. Ligesom i et cykelløb forbedrer hver omgang vores position. Vi tilføjer modulo 2^32 den mellemliggende tilstand til den indledende tilstand for komprimeringsfunktionen. Additionerne i komprimeringsfunktionen er modulo 2^32 additioner for at begrænse størrelsen af summen til 32 bits.

For at konkludere vil vi gerne understrege den afgørende rolle, som beregningerne udført i CH, MAJ, σ0 og σ1-boksene spiller. Disse operationer, blandt andre, er vogterne, der sikrer robustheden af SHA256 hashfunktionen mod angreb og gør den til et foretrukket valg til sikring af talrige digitale systemer, især inden for Bitcoin-protokollen. Det er tydeligt, at selvom SHA256 er kompleks, ligger skønheden i dens robusthed til at finde indgangen fra hashen, mens verificeringen af hashen for en given indgang er en mekanisk simpel handling.

## De anvendte algoritmer til afledning

![De anvendte algoritmer til afledning](https://youtu.be/ZF1_BMsOJXc)

HMAC- og PBKDF2-afledningsalgoritmerne er nøglekomponenter i sikkerhedsmekanismen for Bitcoin-protokollen. De forhindrer forskellige potentielle angreb og sikrer integriteten af Bitcoin-tegnebøger.

HMAC og PBKDF2 er kryptografiske værktøjer, der bruges til forskellige opgaver i Bitcoin. HMAC bruges primært til at modvirke længdeudvidelsesangreb ved afledning af hierarkisk deterministiske (HD) tegnebøger, mens PBKDF2 bruges til at konvertere en mnemonisk sætning til en seed.

HMAC, der tager en besked og en nøgle som input, genererer en output med fast størrelse. For at sikre ensartethed justeres nøglen baseret på blokstørrelsen, der bruges i hashfunktionen. I konteksten af HD-tegnebogsafledning bruges HMAC-SHA-512. Den sidstnævnte arbejder med 1024-bit (128-byte) blokke og justerer nøglen derefter. Den bruger konstanterne OPAD (0x5c) og IPAD (0x36), gentaget efter behov for at forbedre sikkerheden.

HMAC-SHA-512-processen indebærer at sammenkæde resultatet af SHA-512 anvendt på nøglen XOR OPAD og nøglen XOR IPAD med beskeden. Når den bruges med 1024-bit (128-byte) blokke, fyldes den indledende nøgle med nuller om nødvendigt, derefter XORes den med IPAD og OPAD. Den ændrede nøgle sammenkædes derefter med beskeden.

Brugen af en salt, ved at inkorporere en ekstra kilde til entropi, øger sikkerheden af afledte nøgler. Uden det kunne et angreb kompromittere hele tegnebogen og stjæle alle bitcoinsene.
PBKDF2 bruges til at konvertere en mnemonisk sætning til en seed. Denne algoritme udfører 2048 runder ved hjælp af HMAC SHA512. Takket være disse afledningsalgoritmer kan to forskellige input producere en unik og fast output, hvilket mindsker problemet med mulige længdeudvidelsesangreb på SHA-2-familiefunktioner. Et længdeudvidelsesangreb udnytter en specifik egenskab ved visse kryptografiske hashfunktioner. I et sådant angreb kan en angriber, der allerede har hashen af en ukendt besked, bruge den til at beregne hashen af en længere besked, som er en udvidelse af den oprindelige besked. Dette er ofte muligt uden at kende indholdet af den oprindelige besked, hvilket kan føre til betydelige sikkerhedsproblemer, hvis denne type hashfunktion bruges til opgaver som integritetsverifikation.
![billede](assets/image/section1/16.JPG)

Konklusionen er, at HMAC- og PBKDF2-algoritmerne spiller essentielle roller i sikkerheden af HD-wallet-afledning i Bitcoin-protokollen. HMAC-SHA-512 bruges til at beskytte mod længdeudvidelsesangreb, mens PBKDF2 tillader konvertering af den mnemoniske sætning til en seed. Kædekode tilføjer en yderligere kilde til entropi i nøgleafledning og sikrer robustheden af systemet.

# Digitale signaturer

## Digitale signaturer og elliptiske kurver

![Digitale signaturer og elliptiske kurver](https://youtu.be/gOjYiPkx4z8)

I verdenen af kryptovalutaer er transaktionssikkerhed afgørende. I kernen af Bitcoin-protokollen bruges digitale signaturer som matematiske beviser for at demonstrere besiddelsen af en privat nøgle, der er forbundet med en specifik offentlig nøgle. Denne datanbeskyttelsesteknik er i bund og grund baseret på et fascinerende område inden for kryptografi kaldet elliptisk kurvekryptografi (ECC).

![billede](assets/image/section2/0.JPG)

Elliptisk kurvekryptografi er rygraden i sikkerheden for Bitcoin-transaktioner. Disse elliptiske kurver, der minder om de matematiske kurver, vi studerede i skolen, er nyttige i en række kryptografiske anvendelser, lige fra nøgleudveksling til asymmetrisk kryptering til oprettelse af digitale signaturer. En interessant detalje, der adskiller elliptiske kurver, er deres symmetri: enhver ikke-vertikal linje, der skærer to punkter på kurven, vil skære et tredje punkt.

Nu skal vi grave lidt dybere: Bitcoin-protokollen bruger en specifik elliptisk kurve kaldet SecP256K1 til at udføre sine kryptografiske operationer. Denne kurve, defineret på en endelig mængde af positive heltal modulo et primtal på 256 bits, kan visualiseres som en sky af punkter i stedet for en traditionel kurve. Det er denne unikke design, der gør det muligt for Bitcoin effektivt at sikre sine transaktioner.

![billede](assets/image/section2/1.JPG)

Hvad angår valget af secp256k1-kurven til Bitcoin, er det interessant at bemærke, at den blev foretrukket frem for secp256r1-kurven. Denne kurve er defineret ved parametrene a=0 og b=7, og dens ligning er y² = x³ + 7 modulo n, hvor n repræsenterer primtallet, der bestemmer kurvens orden.

Når vi taler om konstanterne, der bruges i Bitcoin-systemet, henviser vi generelt til de specifikke parametre for Elliptic Curve Digital Signature Algorithm (ECDSA) og det elliptiske kurvesystem, der bruges af Bitcoin, nemlig secp256k1-kurven. Her er disse parametre:
- primt felt (p): Bitcoin bruger en kurve over et primt felt, så p er det første tal, der bruges til at definere dette felt. For secp256k1-kurven er p lig med `p = FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE FFFFFC2F` i hexadecimal eller p = 2^256 - 2^32 - 2^9 - 2^8 - 2^7 - 2^6 - 2^4 -1 i decimaltal.
- kurveorden (n): Dette er antallet af punkter på kurven, inklusive punktet ved uendelighed. For secp256k1 er n lig med `n = FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE BAAEDCE6 AF48A03B BFD25E8C D0364141` i hexadecimal eller n = 2^256 - 432420386565659656852420866394968145599 i decimaltal.
- generatorpunkt (G): Basispunktet eller generatoren er punktet på kurven, hvorfra alle andre offentlige nøgler genereres. Det har specifikke x- og y-koordinater, normalt repræsenteret i hexadecimal. For secp256k1 er koordinaterne for G, i hexadecimal:
  - `Gx = 79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798`
  - `Gy = 483ADA77 26A3C465 5DA4FBFC 0E1108A8 FD17B448 A6855419 9C47D08F FB10D4B8`

Bemærk, at alle hexadecimalværdier generelt repræsenteres i base 16, mens decimalværdier er i base 10. Derudover udføres alle operationer på disse konstanter modulo p for punktkoordinater på kurven og modulo n for nøgle- og signaturoperationer.

Så hvor opbevares disse berømte bitcoins? Ikke i en Bitcoin-pung, som man måske tror. I virkeligheden opbevarer en Bitcoin-pung de private nøgler, der er nødvendige for at bevise ejerskab af bitcoins. Selve bitcoins er registreret på blockchain, en decentraliseret database, der arkiverer alle transaktioner.

I Bitcoin-systemet er enheden for kontoen bitcoin (bemærk det lille "b"). Den kan opdeles op til otte decimaler, hvor den mindste enhed er satoshi. UTXO'er eller "Unspent Transaction Outputs" repræsenterer de ubrugte transaktionsoutputs, der tilhører en bruger. For at bruge disse bitcoins skal man bevise ejerskab af den private nøgle, der svarer til den offentlige nøgle, der er knyttet til hver UTXO.

For at sikre transaktionssikkerhed stoler Bitcoin på to digitale signaturprotokoller: ECDSA (Elliptic Curve Digital Signature Algorithm) og Schnorr. ECDSA er en signaturprotokol, der er integreret i Bitcoin siden lanceringen i 2009, mens Schnorr-signaturer blev tilføjet for nylig i november 2021. Selvom begge protokoller er baseret på elliptisk kurvekryptografi og bruger lignende matematiske mekanismer, adskiller de sig primært i forhold til signaturstruktur.

Inden vi dykker dybere ned i disse signaturmekanismer, er det vigtigt at forstå, hvad en elliptisk kurve er. En elliptisk kurve defineres af ligningen y² = x³ + ax + b. Hvert punkt på denne kurve har en karakteristisk symmetri, der er afgørende for dens anvendelighed inden for kryptografi.
I sidste ende anerkendes forskellige elliptiske kurver som sikre til kryptografisk brug. Måske den mest kendte er secp256r1-kurven. Dog valgte Satoshi Nakamoto en anden kurve til Bitcoin: secp256k1.
I næste afsnit af denne kursus vil vi se nærmere på den offentlige nøgle og den private nøgle for at opnå en grundig forståelse af kryptografi på elliptiske kurver og den digitale signatur algoritme. Dette vil være tidspunktet for at konsolidere din viden og forstå, hvordan al denne information kommer sammen for at sikre sikkerheden af Bitcoin-protokollen.

## Beregning af den offentlige nøgle ud fra den private nøgle

![Beregning af den offentlige nøgle ud fra den private nøgle](https://youtu.be/NJENwFU889Y)

I det følgende afsnit af denne kursus vil vi dykke ned i mekanismerne for offentlige og private nøgler, to afgørende elementer i Bitcoin-protokollen. Disse nøgler er intrinsisk forbundet af Elliptic Curve Digital Signature Algorithm (ECDSA). At forstå dem vil give os en dyb indsigt i, hvordan Bitcoin sikrer transaktioner på sin platform.

![billede](assets/image/section2/3.JPG)
![billede](assets/image/section2/4.JPG)

Lad os begynde med at dykke ned i verdenen af ECDSA-algoritmen. Bitcoin anvender denne digitale signatur algoritme til at forbinde private og offentlige nøgler. I dette system er den private nøgle et tilfældigt eller pseudo-tilfældigt 256-bit nummer. Det samlede antal muligheder for en privat nøgle er teoretisk set 2^256, men i virkeligheden er det lidt mindre end det. For at være præcis er nogle 256-bit private nøgler ikke gyldige for Bitcoin.

![billede](assets/image/section2/5.JPG)

For at være kompatibel med Bitcoin skal en privat nøgle være mellem 1 og n-1, hvor n repræsenterer ordenen af den elliptiske kurve. Dette betyder, at det samlede antal muligheder for en Bitcoin privat nøgle er næsten lig med 1.158 x 10^77. For at sætte dette i perspektiv er det omtrent det samme antal atomer, der er til stede i det observerbare univers. Den unikke private nøgle bruges derefter til at udlede en 512-bit offentlig nøgle.

![billede](assets/image/section2/6.JPG)

Den offentlige nøgle, betegnet som K, er et punkt på den elliptiske kurve, der udledes fra den private nøgle ved hjælp af punktoperationer på kurven. Det er vigtigt at bemærke, at ECDSA-funktionen er irreversibel, hvilket betyder, at det er umuligt at gendanne den private nøgle fra den offentlige nøgle. Denne irreversibilitet er hjørnestenen i Bitcoin wallet-sikkerhed.

Den offentlige nøgle består af to 256-bit punkter, i alt 512 bits. Dog kan den komprimeres til et 264-bit nummer. Punktet G er startpunktet for beregning af alle brugernes offentlige nøgler i systemet.

![billede](assets/image/section2/7.JPG)

En bemærkelsesværdig egenskab ved elliptiske kurver er, at en linje, der skærer kurven ved to punkter, også vil skære et tredje punkt, kaldet punkt O. Denne egenskab bruges til at bestemme punkt U, som er modsætningen til punkt O. Tilføjelse af et punkt til sig selv gøres ved at tegne en tangent til kurven ved det punkt, hvilket resulterer i et nyt unikt punkt kaldet j. Skalar multiplikation af et punkt med n svarer til at tilføje det punkt til sig selv n gange.

![billede](assets/image/section2/8.JPG)
Disse operationer på punkter på en elliptisk kurve danner grundlaget for beregning af offentlige nøgler. Ved at kende den private nøgle er det nemt at beregne den offentlige nøgle. Men ved at kende den offentlige nøgle er det ikke muligt at beregne den private nøgle, hvilket sikrer Bitcoin-systemets sikkerhed. Faktisk er sikkerheden af offentlige og private nøgler baseret på det diskrete logaritmeproblem, et komplekst matematisk spørgsmål.
![image](assets/image/section2/9.JPG)

I vores næste lektion vil vi udforske, hvordan en digital signatur opnås ved hjælp af ECDSA-algoritmen med en privat nøgle til at låse op for bitcoins. Bliv klar til denne spændende udforskning af verdenen af kryptokurver og kryptografi.

## Signering med den private nøgle

![Signering med den private nøgle](https://youtu.be/h2hIyGgPqkM)

Processen med digital signatur er en nøglemetode til at bevise, at du er indehaveren af en privat nøgle uden at afsløre den. Dette opnås ved hjælp af ECDSA-algoritmen, som indebærer at bestemme en unik nonce, beregne et specifikt tal V og oprette en digital signatur bestående af to dele, S1 og S2. Det er afgørende altid at bruge en unik nonce for at undgå sikkerhedsangreb. Et berygtet eksempel på, hvad der kan ske, når denne regel ikke følges, er tilfældet med PlayStation 3-hacket, som blev kompromitteret på grund af genbrug af nonce.

Specifikt for at validere en digital signatur ved hjælp af ECDSA (Elliptic Curve Digital Signature Algorithm) algoritmen, er følgende trin typisk involveret:

1. Verificer, at signaturværdierne, S1 og S2, er inden for intervallet [1, n-1]. Hvis ikke, er signaturen ugyldig.
2. Beregn den inverse af S2 modulo n. Vi vil kalde dette for u. Det beregnes ofte som følger: u = (S2)^-1 mod n.
3. Beregn H, som er hashværdien af den underskrevne besked.
4. Beregn u1 = H _ u mod n og u2 = S1 _ u mod n.
5. Beregn punktet P på den elliptiske kurve ved hjælp af u1, u2 og den offentlige nøgle K: P = u1*G + u2*K, hvor G er kurvens generatorpunkt.
6. Hvis P er punktet ved uendelighed, er signaturen ugyldig.
7. Beregn I = x-koordinaten af P modulo n.
8. Signaturen er gyldig, hvis I er lig med S1.

![image](assets/image/section2/10.JPG)
![image](assets/image/section2/11.JPG)

Det er vigtigt at bemærke, at hver software kan bruge forskellige notationer, og nogle trin kan kombineres eller omarrangeres, men den grundlæggende logik forbliver den samme. Bemærk også, at alle aritmetiske operationer udføres i det endelige felt defineret af den elliptiske kurve (mod n, hvor n er kurvens orden). Som en påmindelse har secp256k1-kurven (brugt i Bitcoin) n = 2^256 - 432420386565659656852420866394968145599.
Når det kommer til at generere offentlige og private nøgler, er det vigtigt at sætte sig ind i den elliptiske kurve og generatorpunktet. For at opnå en offentlig nøgle skal der vælges et tilfældigt tal som den private nøgle, ofte kaldet en `nonce`, og bruges i ligningen for den elliptiske kurve.
Elliptiske kurver er et kraftfuldt værktøj til at generere sikre offentlige og private nøgler. For eksempel, for at få den offentlige nøgle 3G, trækker du en tangent til punktet G, beregner det modsatte af -G for at få 2G, og tilføjer derefter G og 2G. For at udføre en transaktion skal du bevise, at du kender tallet 3 ved at låse op for bitcoinsene, der er forbundet med den offentlige nøgle 3G.
For at oprette en digital signatur og bevise, at du kender den private nøgle, der er forbundet med den offentlige nøgle 3G, beregner du først en nonce, derefter punktet V, der er forbundet med denne nonce (i det givne eksempel er det 4G). Derefter beregner du punktet T ved at tilføje den offentlige nøgle 3G og punktet V, hvilket giver 7G.

![image](assets/image/section2/12.JPG)

At verificere en digital signatur er et afgørende trin i brugen af ECDSA-algoritmen, der gør det muligt at bekræfte ægtheden af en underskrevet besked uden at have brug for afsenderens private nøgle. Her er hvordan det fungerer i detaljer:

I vores eksempel har vi to vigtige værdier: T og V. T er en numerisk værdi (7 i dette eksempel), og V er et punkt på den elliptiske kurve (repræsenteret ved 4G her). Disse værdier produceres under oprettelsen af den digitale signatur og sendes derefter sammen med beskeden for at muliggøre verifikation.

Når verificatoren modtager beskeden, vil de også modtage disse to værdier, T og V.

Her er trinnene, som verificatoren vil følge for at validere signaturen:

1. De vil først beregne hashen af beskeden, som vi vil kalde H.
2. Derefter vil de beregne u1 og u2. For at gøre dette vil de bruge følgende formler:
   - u1 = H \* (S2)^-1 mod n
   - u2 = T \* (S2)^-1 mod n'

# Den mnemoniske sætning

## Udvikling af Bitcoin-tegnebøger

![Udvikling af Bitcoin-tegnebøger](https://youtu.be/6tmu1R9cXyk)

Den Hierarkiske Deterministiske Tegnebog, eller mere almindeligt kendt som HD-tegnebogen, spiller en fremtrædende rolle i kryptocurrency-økosystemet. Udtrykket "tegnebog" kan virke misvisende for dem, der er nye på området, da det ikke antyder at holde penge eller valuta. I stedet henviser det til en samling af private kryptografiske nøgler, der er afledt af en enkelt master-nøgle takket være en genial proces med algoritmisk aritmetik. Disse private nøgler, der har en fast længde på 256 bits, udgør selve kernen i ejerskabet af kryptovaluta og omtales sommetider med det lidt grovere navn "Bare en Bunke Nøgler" (JBOC).

![image](assets/image/section3/0.JPG)

Dog opvejes kompleksiteten ved at administrere disse nøgler af en række protokoller, kendt som Bitcoin Improvement Proposals (BIP'er). Disse opgraderingsforslag er hjertet i funktionaliteten og sikkerheden ved HD-tegnebøger. For eksempel revolutionerede [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), der blev lanceret i 2012, måden disse nøgler genereres og opbevares på ved at introducere konceptet om deterministisk og hierarkisk afledte nøgler. Dette forenkler i høj grad processen med at gemme disse nøgler, samtidig med at deres sikkerhedsniveau opretholdes.

![image](assets/image/section3/1.JPG)
Here is the translation:

Here are the guidelines to ensure a high quality translation:

Original language: The content is originally in English.
Nature of the content: You will encounter technical material, potentially including industry-specific terminology.
Links and technical terms: Do not translate URLs or very specific technical terms. If in doubt, keep the original term.
Consistent formatting: Maintain the same markdown layout and formatting as the original text. Consistency in structure is crucial.
YML properties: If a line starts with a YML property (e.g. 'name:', 'goal:', 'objectives:'), keep the property name in English.
Cultural context: For cultural or context-specific references that may not be directly translatable, rephrase to preserve the intended meaning or provide a brief explanation.
The focus should be on preserving the integrity of the technical content while ensuring the translation is understandable and contextually correct in Danish.

Subsequently, [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) introducerede en banebrydende innovation: den 24-ords mnemoniske sætning. Dette system gjorde det muligt at omdanne en kompleks, svær-at-huske sekvens af tal til en række almindelige ord, meget nemmere at huske og gemme. Derudover foreslog [BIP38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki) at tilføje en ekstra adgangskode for at styrke sikkerheden af individuelle nøgler. Disse successive forbedringer førte til BIP43 og BIP44, som standardiserede strukturen og hierarkiet af HD-wallets og gjorde dem mere tilgængelige og nemmere at bruge for den brede offentlighed.

I de følgende afsnit vil vi dykke dybere ned i, hvordan HD-porteføljer fungerer. Vi vil dække principperne for nøgleafledning og undersøge de grundlæggende begreber om entropi og tilfældig talgenerering, som er afgørende for at garantere sikkerheden af din HD-portefølje.

Den Hierarkiske Deterministiske Wallet, eller mere almindeligt kendt som HD-wallet, spiller en fremtrædende rolle i kryptocurrency-økosystemet. Begrebet "wallet" kan virke misvisende for dem, der er nye på området, da det ikke antyder opbevaring af penge eller valuta. I stedet henviser det til en samling af private kryptografiske nøgler, der er afledt fra en enkelt master-nøgle takket være en genial proces med algoritmisk aritmetik. Disse private nøgler, som har en fast længde på 256 bits, udgør selve essensen af kryptovaluta-ejerskab og omtales sommetider med det lidt grovere navn "Just a Bunch Of Keys" (JBOC).

![image](assets/image/section3/0.JPG)

Dog opvejes kompleksiteten ved at administrere disse nøgler af en række protokoller, kendt som Bitcoin Improvement Proposals (BIP'er). Disse opgraderingsforslag er hjertet i funktionaliteten og sikkerheden af HD-wallets. For eksempel revolutionerede [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), der blev lanceret i 2012, måden disse nøgler genereres og gemmes på ved at introducere konceptet med deterministisk og hierarkisk afledte nøgler. Dette forenkler i høj grad processen med at gemme disse nøgler, samtidig med at deres sikkerhedsniveau opretholdes.![image](assets/image/section3/1.JPG)

Sammenfattende er det vigtigt at fremhæve den centrale rolle, som BIP32 og BIP39 spiller i designet og sikkerheden af HD-wallets. Disse protokoller muliggør genereringen af flere nøgler fra en enkelt seed, som antages at være et tilfældigt eller pseudo-tilfældigt tal. I dag er disse standarder vedtaget af flertallet af kryptocurrency-wallets, uanset om de er dedikeret til en enkelt kryptocurrency eller understøtter flere typer af valutaer.

Jeg håber, denne introduktion har hjulpet dig med at få en bedre forståelse af grundlaget for HD-wallets og deres forskellige karakteristika. Vores mål er at hjælpe dig med at mestre disse essentielle begreber og navigere mere effektivt i den komplekse verden af kryptocurrency. Så bliv hos os, mens vi fortsætter med at udforske de intrikate detaljer og nuancer i denne fascinerende verden i de kommende lektioner.

## Entropi og Tilfældige Tal

![Entropi og Tilfældige Tal](https://youtu.be/k18yH18w2TE)
Betydningen af sikkerheden af private nøgler i Bitcoin-økosystemet er uundgåelig. De udgør faktisk hjørnestenen, der sikrer sikkerheden af Bitcoin-transaktioner. For at undgå sårbarheder forbundet med forudsigelighed skal disse nøgler genereres på en virkelig tilfældig måde, hvilket hurtigt kan blive en besværlig opgave for brugeren. En løsning på denne gåde er Hierarkisk Deterministisk Wallet, eller HD-wallet. Denne metode tillader deterministisk og hierarkisk generering af underordnede nøglepar fra en enkelt information i bunden af ​​wallet'en. Her bliver tilfældighed afgørende for at garantere sikkerheden af ​​afledte nøgler.
![image](assets/image/section3/2.JPG)

Genereringen af tilfældige tal er faktisk et afgørende element inden for kryptografi for at sikre integriteten af private nøgler. For at forhindre sårbarheder forbundet med forudsigelighed skal en privat nøgle genereres tilfældigt. Brugen af ​​et nyt nøglepar til hver transaktion øger yderligere sikkerheden, selvom det komplicerer deres backup og kun delvist bevarer fortroligheden. Sammenfattende er sikkerheden af private nøgler en absolut prioritet, der kræver en streng og tilfældig generering. HD-wallets tilbyder en løsning for at lette genereringen og styringen af nøgler samtidig med at opretholde et højt sikkerhedsniveau.

Generering af tilfældige tal på computere udgør imidlertid en betydelig udfordring, da de opnåede resultater ikke er virkelig tilfældige. Derfor er det vigtigt at bruge en tilfældighedsgenerator (RNG). Typerne af RNG varierer og spænder fra pseudotilfældighedsgeneratorer (PRNG) til sande tilfældighedsgeneratorer (TRNG) samt PRNG'er, der inkorporerer en entropikilde.

![image](assets/image/section3/3.JPG)

I tilfældet med Bitcoin genereres private nøgler ud fra en enkelt information i bunden af ​​wallet'en. Denne information tillader deterministisk og hierarkisk afledning af underordnede nøglepar. Entropi er grundlaget for enhver HD-wallet, selvom der ikke er nogen standard for generering af dette tilfældige tal. Derfor er generering af tilfældige tal en stor bekymring for sikring af Bitcoin-transaktioner.

Verifikationsfasen af nøglegenerering er afgørende for at sikre sikkerheden og ægtheden af tilfældig talgenerering, et grundlæggende skridt for at forhindre sårbarheder forbundet med forudsigelighed. Det anbefales stærkt at bruge open-source wallets for at muliggøre denne verifikation.

Det er dog vigtigt at bemærke, at nogle hardware-wallets kan være "lukket kildekode", hvilket gør det umuligt at verificere genereringen af det tilfældige tal. En mulig løsning ville være at generere sin egen mnemoniske sætning ved hjælp af terninger, selvom denne tilgang kan indebære visse risici.

![image](assets/image/section3/4.JPG)

Brug af en tilfældigt genereret adgangskode kan hjælpe med at mindske disse risici.

Et eksempel på anvendelse af denne metode er "dice roll" -muligheden, som CoinKit tilbyder for at generere mnemoniske sætninger. En anden mulighed ville være at bruge en meget stor startinformation og reducere denne information til 256 bits med SHA-256 hashfunktionen, der er i stand til at generere et godt tilfældigt tal. Det er vigtigt at nævne, at SHA-256 hashfunktionen modstår sammenstød, forfalskning og forudbilledangreb.

Til syvende og sidst spiller tilfældighed en central rolle inden for kryptografi og datalogi, og evnen til at generere tilfældighed sikkert er afgørende for at sikre sikkerheden af private nøgler og Bitcoin-transaktioner. Entropi, som er hjertet af Bitcoin HD-wallet'en, er afgørende for dens sikkerhed. I vores næste lektion vil vi fortsætte med at udforske dette emne og dykke ned i, hvordan entropi bidrager til sikkerheden af HD-wallets.

## Den mnemoniske sætning

![Den mnemoniske sætning](https://youtu.be/uJERqH9Xp7I)

Sikkerheden af en Bitcoin-wallet er en stor bekymring for alle dens brugere. En væsentlig måde at sikre backup af wallet'en på er at generere en mnemonisk sætning baseret på entropi og checksum.
Entropi er hjørnestenen i HD wallet-sikkerhed. Der findes flere metoder til at generere denne entropi, herunder gennem pseudo-tilfældige talgeneratorer (PRNG'er), sande tilfældige talgeneratorer (TRNG'er) eller manuelt. Det er afgørende, at denne entropi er tilfældig eller pseudo-tilfældig for at garantere sikkerheden af ​​wallet'en.

På den anden side sikrer checksummen verifikationen af ​​nøjagtigheden af ​​gendannelsesfrasen. Uden denne checksum kan en fejl i frasen resultere i oprettelsen af ​​en anden wallet og dermed tabet af midler. Checksummen opnås ved at sende entropien gennem SHA256-funktionen og hente de første 8 bits af hashen.

Der findes forskellige standarder for den mnemoniske frase afhængigt af størrelsen af ​​entropien. Den mest almindeligt anvendte standard for en 24-ords gendannelsesfrase er en entropi på 256 bits. Størrelsen af ​​checksummen bestemmes ved at dividere størrelsen af ​​entropien med 32.

For eksempel genererer en 256-bit entropi en 8-bit checksum. Konkatenationen af ​​entropien og checksummen fører derefter til respektive størrelser på 128 bits, 160 bits osv. Afhængigt af størrelsen af ​​entropien vil gendannelsesfrasen bestå af 12 ord for 128 bits, 15 ord for 160 bits og 24 ord for 256 bits.

For at omdanne bits til fraser er hver segment forbundet med et ord fra en liste over 2048 ord. Det er vigtigt at bemærke, at ingen ord har samme rækkefølge af de første fire bogstaver.

Det er vigtigt at sikkerhedskopiere den 24-ords gendannelsesfrase for at bevare integriteten af ​​Bitcoin-wallet'en. De to mest almindeligt anvendte standarder er baseret på en entropi på 128 eller 256 bits og en konkatenation af 12 eller 24 ord. Tilføjelse af en adgangskode er en yderligere mulighed for at forbedre sikkerheden af ​​wallet'en.

Konklusionen er, at generering af en mnemonisk frase til at sikre en Bitcoin-wallet er en afgørende proces. Det er vigtigt at overholde standarderne for den mnemoniske frase afhængigt af størrelsen af ​​entropien. Sikkerhedskopiering af den 24-ords gendannelsesfrase er afgørende for at forhindre tab af midler. Tak for din opmærksomhed, og vi ser frem til vores næste kryptokurrency-kursus.

## Adgangskoden

Adgangskoden er en ekstra adgangskode, der kan integreres i en Bitcoin-wallet for at øge sikkerheden. Dens brug er valgfri og er op til brugeren. Ved at tilføje arbitrær information, der sammen med den mnemoniske frase tillader beregningen af ​​wallet'ens seed, forbedrer adgangskoden sikkerheden.

For at aflede nøglerne til en HD wallet er både den mnemoniske frase og adgangskoden nødvendige. Adgangskoden er gratis og kan have en næsten uendelig størrelse. Den er ikke inkluderet i den mnemoniske frase, som er standardiseret og skal følge visse begrænsninger for størrelse, checksum og kodning. En angriber kan ikke få adgang til en brugers bitcoins uden at kende adgangskoden. Adgangskoden spiller en rolle i konstruktionen og beregningen af ​​alle wallet'ens nøgler.

Funktionen pbkdf2 bruges til at generere seed'en fra adgangskoden. Denne seed tillader afledningen af ​​alle wallet'ens underordnede nøglepar. Hvis adgangskoden ændres, bliver Bitcoin-wallet'en helt anderledes.
Passphrase er et essentielt værktøj til at forbedre sikkerheden af Bitcoin-wallets. Det kan muliggøre anvendelsen af forskellige sikkerhedsstrategier. For eksempel kan det bruges til at oprette kopier og lette backup af den mnemoniske sætning. Det kan også forbedre wallet'ens sikkerhed ved at mindske risikoen forbundet med tilfældig generering af den mnemoniske sætning.
En effektiv passphrase bør være lang (20 til 40 tegn) og varieret (ved at bruge store bogstaver, små bogstaver, tal og symboler). Den bør ikke være direkte relateret til brugeren eller deres miljø. Det er sikrere at bruge en tilfældig sekvens af tegn i stedet for et simpelt ord som passphrase.

![image](assets/image/section3/9.JPG)

En passphrase er mere sikker end et simpelt kodeord. Den ideelle passphrase er lang, varieret og tilfældig. Den kan forbedre sikkerheden af en wallet eller hot software. Den kan også bruges til at oprette redundante og sikre backups.

Det er vigtigt at passe på passphrase-backups for at undgå at miste adgangen til wallet'en. En passphrase er en mulighed for en HD-wallet. Den kan genereres tilfældigt med terninger eller en anden pseudo-tilfældig talgenerator. Det anbefales ikke at huske en passphrase eller mnemonisk sætning.

I vores næste lektion vil vi undersøge detaljeret, hvordan seed'en fungerer, og det første par nøgler, der genereres ud fra den. Du er velkommen til at følge denne kursus for at fortsætte din læring. Vi ser frem til at se dig meget snart.

# Oprettelse af Bitcoin Wallets

## Oprettelse af seed'en og master-nøglen

![Oprettelse af seed'en og master-nøglen](https://youtu.be/56yAt_JDWhY)

I denne del af kurset vil vi udforske trinnene til at aflede en Hierarchical Deterministic Wallet (HD Wallet), som tillader oprettelse og styring af private og offentlige nøgler hierarkisk.

![image](assets/image/section4/0.JPG)

Grundlaget for HD Wallet'en er to essentielle elementer: den mnemoniske sætning og passphrase'en (valgfrit ekstra kodeord). Sammen udgør de seed'en, en 512-bit alfanumerisk sekvens, der fungerer som grundlaget for at aflede wallet'ens nøgler. Fra denne seed er det muligt at aflede alle de underordnede nøglepar i Bitcoin-wallet'en. Seed'en er nøglen, der giver adgang til alle bitcoins, der er forbundet med wallet'en, uanset om du bruger en passphrase eller ej.

For at få seed'en bruges pbkdf2-funktionen (Password-Based Key Derivation Function 2) med den mnemoniske sætning og passphrase'en. Outputtet fra pbkdf2 er en 512-bit seed. Master private key og master chain code bestemmes ved hjælp af HMAC SHA-512 (Hash-based Message Authentication Code Secure Hash Algorithm 512) algoritmen. Denne algoritme kræver en besked og en nøgle for at generere et resultat. Master private key beregnes ud fra seed'en og sætningen "Bitcoin SEED". Denne sætning er identisk for alle HD wallet-afledninger og sikrer konsistens på tværs af wallet'er.

![image](assets/image/section4/1.JPG)

I starten var SHA-512 funktionen ikke implementeret i Bitcoin-protokollen, hvilket er grunden til, at HMAC SHA-512 bruges. Brugen af HMAC SHA-512 med sætningen "Bitcoin SEED" begrænser brugeren til at generere en wallet specifik for Bitcoin. Resultatet af HMAC SHA-512 er et 512-bit tal, opdelt i to dele: de venstre 256 bits repræsenterer master private key, mens de højre 256 bits repræsenterer master chain code.
Den primære private nøgle er forældrenøglen til alle fremtidige nøgler i tegnebogen, mens den primære kædekode er involveret i afledningen af underordnede nøgler. Det er vigtigt at bemærke, at det er umuligt at aflede et par underordnede nøgler uden at kende den tilsvarende kædekode for forældreparret. Kædekoden tilføjer en kilde til entropi til afledningsprocessen.
Et nøglepar i tegnebogen består af en privat nøgle, en offentlig nøgle og en kædekode. Kædekoden tillader introduktion af tilfældighed i afledningen af underordnede nøgler og isolerer hvert nøglepar for at forhindre lækage af information.
Det er vigtigt at understrege, at den primære private nøgle er den første private nøgle, der er afledt fra seedet, og den har ingen forbindelse til tegnebogens udvidede nøgler. Derfor er seedet det grundlæggende element til afledning af alle nøgler i tegnebogen. Det adskiller sig fra den mnemoniske frase og adgangskoden, der bruges til seedoprettelse.
I den næste lektion vil vi udforske de udvidede nøgler, såsom xPub, xPRV, zPub, og forstå hvorfor de bruges og hvordan de konstrueres.
Udvidede nøgler adskiller sig fra hovednøgler. En HD-tegnebog genererer en mnemonisk frase og et seed for at opnå hovednøglen og hovedkædekoden. Udvidede nøgler bruges til at aflede underordnede nøgler og kræver både forældrenøglen og den tilsvarende kædekode. En udvidet nøgle kombinerer disse to informationer for at forenkle afledningsprocessen.
Udvidede nøgler identificeres af specifikke præfikser (XPRV, XPUB, YPUB, ZPUB), der angiver, om det er en udvidet privat eller offentlig nøgle, samt dens specifikke formål. Metadataet forbundet med en udvidet nøgle inkluderer versionen (præfiks), dybden, offentlig nøgle fingeraftryk, indeks og nyttelast (kædekode og forældrenøgle).
Nyttelasten består af kædekoden (32 byte) og forældrenøglen (33 byte). Disse elementer er afgørende for afledning af underordnede nøgler. En privat nøgle genereres ud fra et tilfældigt eller pseudotilfældigt tal, mens en offentlig nøgle genereres ved hjælp af ECDSA (Elliptic Curve Digital Signature Algorithm) algoritmen.
Hvert par udvidede nøgler er forbundet med en unik kædekode, der tillader specifikke afledninger. Ved at sammenkæde forældrenøglen med kædekoden opnås en udvidet privat eller offentlig nøgle.
Udvidede offentlige nøgler kan kun afledes fra normale offentlige underordnede nøgler, mens udvidede private nøgler kan afledes fra både offentlige og private underordnede nøgler, enten gennem normal eller hærdet afledning. Ved brug af udvidede nøgler med præfikset XPUB kan der afledes nye adresser uden at gå tilbage til de tilsvarende private nøgler, hvilket giver bedre sikkerhed. Metadataet forbundet med udvidede nøgler giver vigtig information om deres rolle og position i nøglehierarkiet.
Komprimerede offentlige nøgler har en størrelse på 33 byte, mens ukomprimerede offentlige nøgler er 512 bit. Komprimerede offentlige nøgler bevarer den samme information som ukomprimerede nøgler, men med en reduceret størrelse. Udvidede nøgler har en størrelse på 82 byte, og deres præfiks repræsenteres i base 58 gennem hexadecimal konvertering. Checksummen beregnes ved hjælp af HASH256 hashfunktionen.
Hærdede afledninger starter fra indekser, der er potenser af 2 (2^31). Udvidede offentlige nøgler tillader kun afledning af normale offentlige børnenøgler, mens udvidede private nøgler tillader afledning af enhver børnenøgle. Det er værd at bemærke, at de mest almindeligt anvendte præfikser er xpub og zpub, som svarer til henholdsvis legacy og segwit v1 og segwit v0-standarderne.

I vores næste lektion vil vi udforske afledningen af børnenøglepar ved hjælp af den viden, der er opnået om udvidede nøgler og tegnebogens masternøgle.

Konklusionen er, at udvidede nøgler spiller en afgørende rolle inden for kryptografi og drift af HD-tegnebøger. Forståelse af deres anvendelse og beregning er afgørende for at sikre transaktionssikkerhed og beskyttelse af digitale aktiver. Præfikserne og metadataene, der er forbundet med udvidede nøgler, muliggør effektiv brug og nøjagtig afledning af nødvendige børnenøgler.

## Afledning af børnenøglepar

![Afledning af børnenøglepar](https://youtu.be/FXhI-GmE9Aw)

Næste vil vi diskutere beregningen af seedet og masternøglen, som er de første essentielle elementer til den hierarkiske organisering og afledning af HD-tegnebogen (Hierarchical Deterministic Wallet). Seedet, med en længde på 128 til 256 bits, genereres tilfældigt eller fra en hemmelig sætning. Det spiller en deterministisk rolle i afledningen af alle andre nøgler. Masternøglen er den første nøgle, der afledes fra seedet, og den tillader afledning af alle andre børnenøglepar.

Masterkædekode spiller en vigtig rolle i at gendanne porteføljen fra seedet. Det skal bemærkes, at alle nøgler, der er afledt fra samme seed, vil have den samme masterkædekode.

![billede](assets/image/section4/7.JPG)

Den hierarkiske og deterministiske tegnebog (HD-tegnebog) giver mere effektiv styring af nøgler og tegnebogsstrukturer. Udvidede nøgler tillader afledning af et børnenøglepar fra et forældre-nøglepar ved hjælp af matematiske beregninger og specifikke algoritmer.

Der er forskellige typer af børnenøglepar, herunder hærdede nøgler og normale nøgler. Den udvidede offentlige nøgle tillader kun afledning af normale offentlige børnenøgler, mens den udvidede private nøgle tillader afledning af alle børnenøgler, både offentlige og private, uanset om de er i normal eller hærdet tilstand. Hvert nøglepar har et indeks, der adskiller dem fra hinanden.

![billede](assets/image/section4/8.JPG)

Afledningen af børnenøgler bruger HMAC-SHA512-funktionen ved at bruge forældrenøglen sammen med indekset og kædekode, der er forbundet med nøgleparret. Normale børnenøgler har et indeks, der spænder fra 0 til 2 i 31 minus 1, mens hærdede børnenøgler har et indeks, der spænder fra 2 i 31 til 2 i 32 minus 1.

![billede](assets/image/section4/9.JPG)
![billede](assets/image/section4/10.JPG)

Der er to typer af børnenøglepar: hærdede par og normale par. Processen med at aflede børnenøgler bruger de offentlige nøgler til at generere betingelser for brug af midler, mens de private nøgler bruges til at underskrive. Den udvidede offentlige nøgle tillader kun afledning af normale offentlige børnenøgler, mens den udvidede private nøgle tillader afledning af alle børnenøgler, både offentlige og private, i normal eller hærdet tilstand.

![billede](assets/image/section4/11.JPG)
![billede](assets/image/section4/12.JPG)

Hærdet afledning bruger forældreprivatnøglen, mens normal afledning bruger forældreoffentlignøglen. HMAC-SHA512-funktionen bruges til hærdet afledning, mens normal afledning bruger en 512-bit hash. Den offentlige børnenøgle opnås ved at multiplicere den private børnenøgle med generatoren for den elliptiske kurve.

![billede](assets/image/section4/13.JPG)
## Walletstruktur og afledningsstier

![Walletstruktur og afledningsstier](https://youtu.be/etO9UxwyE2I)

I dette kapitel vil vi studere strukturen af afledningstræet i en Hierarkisk Deterministisk Wallet (HD Wallet). Vi har allerede udforsket beregningen af seed, masternøglen og afledningen af barnenøglepar. Nu vil vi fokusere på organiseringen af nøgler inden for wallet'en.

HD Wallet'en bruger dybdeniveauer til at organisere nøglerne. Hver afledning fra et forældrepar til et barnepar svarer til et dybdeniveau. Dybde 0 svarer til masternøglen og masterkædekodeordet.

![image](assets/image/section4/15.JPG)

- Dybde 1 bruges til at aflede barnenøgler til et specifikt formål, som bestemmes af indekset. Formålene er i overensstemmelse med BIP 84 og Segwit v0/v1-standarderne.

- Dybde 2 tillader differentiering af konti til forskellige kryptokurser eller netværk. Dette gør det muligt at organisere wallet'en baseret på forskellige kilder til midler.

- Dybde 3 bruges til at organisere wallet'en i forskellige konti og giver en mere klar og organiseret struktur.

- Dybde 4 svarer til de eksterne og interne kæder, som bruges til adresser, der er beregnet til offentlig kommunikation. Indeks 0 er forbundet med den eksterne kæde, mens indeks 1 er forbundet med den interne kæde. Hver konto har to kæder: den eksterne kæde (0) og den interne kæde (1). Dybde 4 bruges også til at administrere scripttyper i tilfælde af multisignatur-wallets.

- Dybde 5 bruges til at modtage adresser i en standard wallet. I næste afsnit vil vi undersøge afledningen af barnenøglepar mere detaljeret.

![image](assets/image/section4/16.JPG)

For hvert dybdeniveau bruger vi indekser til at differentiere barnenøgleparrene. Hærdede indekser bruges med et apostroftegn for visse afledninger. Den offentlige nøgle pr. år bruges som input til HMAC-funktionen. Indekset i en afledningssti angiver værdien, der bruges i HMAC-funktionen.
Indekset uden et apostroftegn svarer til det faktiske brugte indeks, mens indekset med et apostroftegn svarer til det faktiske indeks + 2^31. Forstærkede afledninger bruger indekser fra 2^31 til 2^32-1. For eksempel svarer indeks 44' til det faktiske indeks 2^31 + 44.
For at generere en specifik modtagelsesadresse afleder vi et par barnenøgler fra masternøglen og masterkædekodeordet. Derefter bruger vi indekset til at differentiere mellem forskellige par barnenøgler på samme dybde.

Udvidede nøgler, såsom XPUB, giver dig mulighed for at dele din wallet med flere personer. Afledningsstien bruges til at differentiere mellem den eksterne kæde (adresser beregnet til kommunikation) og den interne kæde (ændringsadresser).

Det er vigtigt at bemærke, at forskellige dybder bruges i en HD wallet afhængigt af forskellige standarder. Afledning af forældrenøgler til barnenøgler muliggør overgang fra et dybdeniveau til et andet. Brugen af forskellige grene i HD wallet'en indikerer de forskellige standarder, der følges.

I næste kapitel vil vi studere modtagelsesadresser, deres fordele ved brug og de trin, der er involveret i deres konstruktion.

# Hvad er en Bitcoin-adresse?

## Bitcoin-adresser

![Bitcoin-adresser](https://youtu.be/nqGBMjPtFNI)
I dette kapitel vil vi udforske modtagelsesadresser, som spiller en afgørende rolle i Bitcoin-systemet. De gør det muligt at modtage midler på en mønt og genereres ud fra par af private og offentlige nøgler. Selvom der findes en scripttype kaldet Pay2PublicKey, der tillader at låse bitcoins til en offentlig nøgle, foretrækker brugere generelt at bruge modtagelsesadresser i stedet for denne script.

Når en modtager ønsker at modtage bitcoins, giver de en modtagelsesadresse til afsenderen i stedet for deres offentlige nøgle. En adresse er faktisk en hash af en offentlig nøgle med et specifikt format. Den offentlige nøgle udledes fra den tilhørende private nøgle ved hjælp af matematiske operationer som punktaddition og fordobling på elliptiske kurver.

Det er vigtigt at bemærke, at det ikke er muligt at reversere fra en adresse til den offentlige nøgle eller fra den offentlige nøgle til den private nøgle. Brugen af en adresse hjælper med at reducere størrelsen af den offentlige nøgleinformation, som oprindeligt er på 512 bits. Det er muligt at komprimere en offentlig nøgle ved kun at beholde x-værdien og tilføje et præfiks, men denne teknik var ikke kendt på tidspunktet for Bitcoin's oprettelse. Derfor sparer brugen af en adresse ikke plads i blokkene.

## Hvordan oprettes en Bitcoin-adresse?

![Hvordan oprettes en Bitcoin-adresse?](https://youtu.be/ewMGTN8dKjI)

I dette kapitel vil vi diskutere konstruktionen af en modtagelsesadresse til Bitcoin-transaktioner. En modtagelsesadresse er en alfanumerisk repræsentation af en komprimeret offentlig nøgle. Konverteringen af en offentlig nøgle til en modtagelsesadresse gennemgår flere trin.

En fordelagtig funktion ved modtagelsesadresser er tilstedeværelsen af en kontrolsum, der tillader fejldetektion. Til dette bruger vi BCH (Bose-Chaudhuri-Hocquenghem) kontrolsumsteknologi, som sikrer nøjagtig fejldetektion. Denne teknologi bidrager også til at reducere antallet af tegn, der kræves for at repræsentere en adresse, hvilket gør det nemmere at bruge.

For at begynde at opbygge en adresse skal vi komprimere den tilsvarende offentlige nøgle. En rå offentlig nøgle optager 520 bits, men takket være symmetrien i den anvendte elliptiske kurve kan en elliptisk kurve have en x-koordinat forbundet med to mulige værdier for y: positiv eller negativ. På Bitcoin-netværket arbejder vi med en endelig mængde positive heltal i stedet for mængden af reelle tal. For at repræsentere en offentlig nøgle ud fra x tilføjer vi et præfiks, der angiver værdien af y (lige eller ulige). Komprimering af en offentlig nøgle reducerer dens størrelse fra 520 til 264 bits. Pariteten af y i en endelig mængde positive heltal svarer til pariteten af y i mængden af reelle tal.

Lad os tage eksemplet med den offentlige nøgle, der tilhører Satoshi Nakamoto, med et præfiks 0,3, der angiver en ulige værdi af y. Derefter kan vi gå videre til det andet trin i konstruktionen af en adresse ud fra komprimerede offentlige nøgler. Det er muligt at beregne to adresser for hver offentlig nøgle. Til dette bruger vi SHA256-funktionen til at få hashen af den offentlige nøgle. Derefter anvender vi ripemd160-funktionen på resultatet af SHA256 for at få en streng af tegn. Denne streng kodes derefter i binær format i grupper af 5 bits, hvortil metadata tilføjes til kontrolsumsberegning ved hjælp af BCH-programmet.
I tilfælde af legacy-adresser bruger vi dobbelt SHA256-hashfunktionen til at generere adressens kontrolsum. Dog er vi for Segwit V0- og V1-adresser afhængige af BCH-kontrolsumsteknologien for at sikre fejldetektion. BCH-programmet er i stand til at foreslå og rette fejl med en ekstremt lav fejlrate. I øjeblikket bruges BCH-programmet til at detektere og foreslå ændringer, men det foretager ikke automatisk ændringerne på brugerens vegne. Beregningen af kontrolsummen med BCH-koden er baseret på polynomisk Chien-Chauffage-aritmetik.
![image](assets/image/section5/7.JPG)

BCH-programmet kræver flere inputoplysninger, herunder HRP (Human Readable Part), der skal udvides. Udvidelsen af HRP indebærer kodning af hver bogstav i base 2, hvor de første tre bits af hvert tegn indsættes med en separator 0, og derefter sammenkobles de sidste fem bits af hvert tegn. De blå tegn konverteret til base 10 svarer til 3 og 3 i decimaltal, mens de andre fem orange tegn svarer til 2 og 3 i base 10. Udvidelsen af HRP i base 10 gør det muligt at isolere de sidste fem bits af hvert tegn og dermed forstærke kontrolsummen.

![image](assets/image/section5/8.JPG)

Segwit V0-versionen repræsenteres af koden 00, og "payload" er i sort, i base 10. Derefter følger seks tegn reserveret til kontrolsummen. Inputtet, der indeholder metadataen, sendes derefter til BCH-programmet for at få kontrolsummen i base 10. Sammenkoblingen af versionen, payloaden og kontrolsummen gør det muligt at opbygge adressen. De base 10-tegn konverteres derefter til bech32-tegn ved hjælp af en oversættelsestabel. Bech32-alfabetet inkluderer alle alfanumeriske tegn undtagen 1, b, i og o for at undgå forvirring.

![image](assets/image/section5/9.JPG)
![image](assets/image/section5/10.JPG)

For at opbygge en adresse, der starter med bc1q, skal vi anvende en hashfunktion (H160) på en komprimeret offentlig nøgle, derefter tilføje kontrolsummen, versionen (q), HRP'en (bc) og separator (1). Taproot-adresser derimod starter med bc1p, fordi deres version (Segwit V1) svarer til 0+1=1, derfor bruges karakteren p. Alle disse elementer konverteres derefter til BCH32, en Bitcoin-specifik variant af base 32.

Således har vi gennemgået trinnene til konstruktion af en modtageradresse, brugen af BCH-kontrolsumsteknologi samt konstruktionen af en adresse, der starter med bc1q eller bc1p ved hjælp af BCH32-varianten af Bitcoin-specifik base 32.

## Resumé af kryptografi for Bitcoin Wallets

![træningsoversigt](https://youtu.be/NkAYoVUMvOs)

I løbet af denne træning har vi studeret Hierarchical Deterministic (HD) wallet med BIP32 i dybden. Entropi spiller en central rolle i denne type wallet, da den bruges til at generere en mnemonisk sætning fra et tilfældigt tal. Med listen over 2048 ord, der er angivet i BIP39, kan denne mnemoniske sætning kodes til en række let huskelige ord. Den mnemoniske sætning, sammen med en valgfri passphrase, er nødvendig for at generere walletets seed. Passphrasen fungerer som en kryptografisk salt, der tilføjer et ekstra lag beskyttelse til walletet.

![image](assets/image/section5/11.JPG)
Funktionen pbkdf2 bruges til at generere seed fra den mnemoniske sætning og adgangskoden ved hjælp af hmacha512 og 2048 iterationer. Masternøglen og masterkædekode afledes derefter fra denne seed ved hjælp af hmacha512-funktionen igen med sætningen "bitcoin seed". Masterprivatnøglen og masterkædekode er de øverste elementer i HD-wallet-hierarkiet.
![image](assets/image/section5/12.JPG)

Afhængigt af flere faktorer, herunder forældrenøglen og den tilsvarende kædekode, afhænger afledningen af en underordnet nøgle. En udvidet nøgle opnås ved at sammenkæde en forældrenøgle med dens kædekode, mens en masternøgle er en separat nøgle. For at aflede en adresse hashes den komprimerede offentlige nøgle først ved hjælp af SHA256 og RIPMD160, og derefter beregnes en kontrolsum. Dobbelt SHA256-hashing bruges til at beregne kontrolsummen i tilfælde af en legacy-standard, mens BCH (Bose-Chaudhuri-Hocquenghem)-programmet bruges til at beregne kontrolsummen i tilfælde af en segwit-standard. Derefter bruges en repræsentation i base 58-format til en legacy-standard, mens bech32-formatet bruges til en segwit-standard for at opnå HD-wallet-adressen.

![image](assets/image/section5/13.JPG)

I sammenfatning har vi udforsket hashfunktionerne og deres karakteristika samt digitale signaturer og elliptiske kurver i detaljer. Derefter dykkede vi ned i verdenen af Hierarchical Deterministic (HD) wallets med BIP32, hvor vi brugte entropi og adgangskode til at generere wallet-seedet. Vi lærte også, hvordan man afleder underordnede nøgler og opnår HD-wallet-adressen. Jeg håber, at denne information har været nyttig for dig, og jeg opfordrer dig nu til at gå videre til vurderingen for at teste den viden, du har opnået under Crypto 301-kurset. Tak for din opmærksomhed.

# Gå videre

## Oprettelse af et seed fra 128 terningekast!

![Oprettelse af et seed fra 128 terningekast!](https://youtu.be/lUw-1kk75Ok)

Oprettelsen af en mnemonisk sætning er et afgørende skridt i sikringen af din kryptocurrency-portefølje. Der er flere metoder til at generere en mnemonisk sætning, men vi vil fokusere på den manuelle genereringsmetode ved hjælp af terninger. Det er vigtigt at bemærke, at denne metode ikke er egnet til en wallet med høj værdi. Det anbefales at bruge open-source-software eller en hardware-wallet til at generere den mnemoniske sætning. For at oprette en mnemonisk sætning vil vi bruge terninger til at generere binær information. Målet er at forstå processen med at oprette den mnemoniske sætning.

**Trin 1 - Forberedelse:**
Sørg for, at du har en amnesisk Linux-distribution, såsom Tails OS, installeret på en USB-drev for øget sikkerhed. Bemærk, at denne vejledning ikke bør bruges til at oprette en primær wallet.

**Trin 2 - Generering af et tilfældigt binært tal:**
Vi vil bruge terninger til at generere binær information. Kast en terning 128 gange og noter hvert resultat (1 for ulige, 0 for lige).

**Trin 3 - Organisering af de binære tal:**
Organisér de opnåede binære tal i rækker med 11 cifre for at lette yderligere beregninger. Den tolvte række skal kun have 7 cifre.

**Trin 4 - Beregning af kontrolsummen:**
De sidste 4 cifre for den tolvte række svarer til checksummen. For at beregne denne checksum skal vi bruge en terminal fra en Linux-distribution. Det anbefales at bruge [TailOs](https://tails.boum.org/index.fr.html), som er en hukommelsesløs distribution, der kan startes fra en USB-drev. Når du er i din terminal, skal du indtaste kommandoen `echo <binært tal> | shasum -a 254 -0`. Erstat `<binært tal>` med din liste over 128 nuller og ettere. Outputtet er en hexadecimal hash. Tag notits af det første tegn i denne hash og konverter det til binært. Du kan bruge denne [tabel](https://www.educative.io/answers/decimal-binary-and-hex-conversion-table) til hjælp. Tilføj checksummen i binært format (4 cifre) til den tolvte række på dit ark.

**Trin 5 - Konvertering til decimaltal:**
For at finde ordene, der er forbundet med hver af dine linjer, skal du først konvertere hver serie af 11 bits til decimaltal. Her kan du ikke bruge en online konverter, fordi disse bits repræsenterer din mnemoniske sætning. Så du skal konvertere ved hjælp af en lommeregner og en trick som følger: Hver bit er forbundet med en potens af 2, så fra venstre mod højre har vi 11 rangordninger, der svarer til 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1. For at konvertere din serie af 11 bits til decimaltal skal du blot lægge rangordningerne sammen, der indeholder en 1. For eksempel for serien 00110111011 svarer dette til følgende addition: 256 + 128 + 32 + 16 + 8 + 2 + 1 = 443. Du kan nu konvertere hver linje til decimaltal. Og inden du går videre til kodning til ord, skal du tilføje +1 til alle linjerne, fordi indekset for BIP39-ordlisten starter fra 1 og ikke 0.

**Trin 8 - Generering af den mnemoniske sætning:**
Start med at udskrive [listen over 2048 ord](https://seedxor.com/files/wordlist.pdf) for at konvertere mellem dine decimaltal og BIP39-ordene. Særligheden ved denne liste er, at ingen ord har de samme første 4 bogstaver til fælles med alle de andre ord i denne ordbog. Derefter skal du for hver af dine linjer finde det ord, der er forbundet med decimaltallet.

**Trin 9 - Test af den mnemoniske sætning:**
Test straks din mnemoniske sætning på Sparrow Wallet ved at oprette en tegnebog ud fra den. Hvis du får en fejl med ugyldig checksum, er det sandsynligt, at du har lavet en beregningsfejl. Ret denne fejl ved at gå tilbage til trin 4 og test igen på Sparrow Wallet. Sådan! Du har lige oprettet en ny Bitcoin-tegnebog ud fra 128 terningekast.

Generering af en mnemonisk sætning er en vigtig proces til sikring af din kryptocurrency-tegnebog. Det anbefales at bruge mere sikre metoder, såsom brug af open source-software eller hardware-tegnebøger, til at generere den mnemoniske sætning. Dog hjælper fuldførelsen af denne workshop med at forstå bedre, hvordan vi kan oprette en Bitcoin-tegnebog ud fra et tilfældigt tal.

## Konklusion og afslutning

### Anerkendelser og fortsæt med at grave i kaninhullet

Vi vil gerne takke dig oprigtigt for at have deltaget i Crypto 301-træningen. Vi håber, at denne oplevelse har været berigende og lærerig for dig. Vi har dækket mange spændende emner, lige fra matematik til kryptografi til Bitcoin-protokollens funktion.
Hvis du ønsker at dykke dybere ned i emnet, har vi en ekstra ressource at tilbyde dig. Vi har gennemført et eksklusivt interview med Théo Pantamis og Loïc Morel, to anerkendte eksperter inden for kryptografi. Dette interview dykker dybt ned i forskellige aspekter af emnet og tilbyder interessante perspektiver.

Du er velkommen til at se dette interview for at fortsætte udforskningen af det fascinerende felt inden for kryptografi. Vi håber, at det vil være nyttigt og inspirerende i din rejse. Endnu engang tak for din deltagelse og engagement i løbet af denne træning.

### Støt os

Denne kursus, sammen med alt indholdet tilgængeligt på dette universitet, er blevet stillet til rådighed for dig gratis af vores fællesskab. For at støtte os kan du dele det med andre, blive medlem af universitetet og endda bidrage til dets udvikling via GitHub. På vegne af hele teamet, tak!

### Bedøm træningen

Et bedømmelsessystem for træningen vil snart blive integreret i denne nye E-learning platform! I mellemtiden takker vi dig meget for at have taget kurset, og hvis du nød det, bedes du overveje at dele det med andre.