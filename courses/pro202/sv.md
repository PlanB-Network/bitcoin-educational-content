---
name: Programmering Bitcoin
goal: Bygga ett komplett Bitcoin-bibliotek från grunden och förstå Bitcoin:s kryptografiska grundprinciper
objectives: 

 - Implementera aritmetik för finita fält och elliptiska kurvor i Python
 - Konstruera och analysera Bitcoin-transaktioner programmatiskt
 - Skapa testnet-adresser och sända transaktioner över nätverket
 - Behärska de matematiska grunderna som ligger till grund för Bitcoin:s säkerhetsmodell

---
# En resa in i Bitcoin:s manus och program


Denna intensiva tvådagarskurs, som leds av Jimmy Song, tar dig djupt in i Bitcoin:s tekniska grunder genom att bygga ett komplett Bitcoin-bibliotek från grunden. Vi börjar med den grundläggande matematiken för finita fält och elliptiska kurvor och går sedan vidare med transaktionsanalys, skriptexekvering och nätverkskommunikation. Genom praktiska kodningsövningar i Jupyter-anteckningsböcker skapar du din egen testnetadress, konstruerar transaktioner manuellt och sänder dem direkt till nätverket - allt medan du får en djup förståelse för de kryptografiska principer som gör Bitcoin säkert och förtroendefritt.


Ha en trevlig resa!


+++

# Inledning


<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>


## Kursöversikt


<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>


Välkommen till kursen PRO 202 _**Programmering Bitcoin**_, en intensiv resa som tar dig från aritmetik med ändliga fält hela vägen till att bygga och sända riktiga transaktioner på Bitcoin:s Testnet.


I den här kursen kommer du successivt att bygga ett Bitcoin-bibliotek i Python samtidigt som du förvärvar de kryptografiska, protokoll- och programvarufundament som krävs för att resonera exakt om Bitcoin: s säkerhet och inre funktion. PRO 202-metoden är genomgående praktisk: varje koncept implementeras omedelbart i Jupyter-anteckningsböcker, vilket säkerställer att teori och kod stärker varandra.


### Grundläggande matematiska begrepp för Bitcoin


I detta första avsnitt läggs den oumbärliga matematiska grunden. Du kommer att implementera aritmetik för finita fält och elliptiska kurvoperationer (grupplag, addition, dubblering, skalär multiplikation ...) - förutsättningarna för ECDSA. Målet är tvåfaldigt: att förstå den algebraiska struktur som gör kryptografiska signaturer möjliga och att bygga tillförlitliga Python-verktyg för att manipulera dem.


Du kommer sedan att formalisera komponenterna i ECDSA: nyckelgenerering, punktformatering, hashning, signaturskapande och verifiering. I det här avsnittet kopplas teori direkt till praktik, med betoning på implementeringsdetaljer och robustheten i den underliggande säkerhetsmodellen.


### Bitcoin Transaktionens inre arbete


I det andra avsnittet kommer du att dissekera strukturen för en Bitcoin-transaktion: UTXO:er, inmatningar/utmatningar, sekvenser, skript, kodningar med mera. Du kommer att skriva kod för att konstruera, signera och verifiera transaktioner, och få en exakt förståelse för vad som görs av hashen och varför.


Därefter kommer du att implementera en minimal _Script_-exekverare, granska viktiga opkoder och validera utgiftsvägar. Målet är att göra dig kapabel att granska transaktionsbeteende, diagnostisera valideringsfel och resonera om säkerheten i utgiftspolicyn.


### Bitcoin-nätverkets inre arbete


I det tredje avsnittet placerar du transaktioner inom det bredare systemet: blockstruktur, headers, svårigheter och Proof-of-Work-mekanismen. Du kommer att hantera protokollmeddelanden, blockheaders och Merkle-träd.


Slutligen kommer du att studera peer-to-peer-nodkommunikation, meddelandeoptimering och introduktionen av SegWit.


Som med alla kurser om Plan ₿ Academy innehåller det sista avsnittet en utvärdering som är utformad för att konsolidera din förståelse. Är du redo att avslöja det inre arbetet i Bitcoin och skriva koden som driver det? Låt oss börja!










# Grundläggande matematiska begrepp för Bitcoin

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Matematik för implementering av Bitcoin

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>


![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


### Bitcoin Programmeringens grunder: Centrala matematiska strukturer


Denna kurs kondenserar den väsentliga matematiken bakom Bitcoin:s kryptografiska system till ett mycket praktiskt arbetsflöde. Begrepp förklaras, demonstreras med exempel och implementeras sedan i Jupyter Notebook. Den vägledande idén är enkel: du förstår bara en kryptografisk primitiv när du kodar den. Under de två dagarna får eleverna generate testnet-adresser, bygga och sända transaktioner och så småningom interagera med nätverket utan block explorers. Allt detta kräver en solid grund i finita fält och elliptiska kurvor.


### Finita fält: Kryptografins aritmetiska motor


Ett finit fält F(p) är ett aritmetiskt system som definieras av ett primtal p och som innehåller elementen 0 till och med p-1. Primtalsfält säkerställer att varje element som inte är noll har en invers och att alla operationer stannar inom fältet. Aritmetik omsluter sig runt att använda modulo p för addition, subtraktion och multiplikation. Pythons `pow(base, exp, mod)` möjliggör effektiv modulär exponentiering, vilket är avgörande för stora exponenter som används i verkliga kryptografiska operationer.


#### Multiplikativt beteende

Om man multiplicerar ett element k som inte är noll med alla element i ett primtalsfält får man en permutation av fältet. Denna egenskap garanterar enhetlighet och förhindrar strukturella svagheter, vilket gör primtalsfält idealiska för säker nyckelgenerering och digitala signaturer.


#### Division och Fermats lilla sats

Division genomförs med hjälp av multiplikativa inverser. Fermats lilla sats säger att

n^(p-1) ≡ 1 (mod p),

så inversen är n^(p-2). Python stöder detta direkt med `pow(n, -1, p)`. Dessa operationer förekommer ständigt i ECDSA:s och Bitcoin:s underliggande kryptografiska rutiner.


### Elliptiska kurvor: Olinjära strukturer för säkerhet med offentlig nyckel


Elliptiska kurvor följer ekvationen y² = x³ + ax + b. Bitcoin använder secp256k1, definierad som y² = x³ + 7 över ett ändligt fält. Punkter på en elliptisk kurva bildar en matematisk grupp under punktaddition. En linje dragen genom två punkter P och Q skär kurvan i en tredje punkt R; genom att spegla R över x-axeln erhålls P + Q. Detta system är associativt och innehåller ett identitetselement: punkten i oändligheten.


Om en punkt fördubblas används en tangentlinje i stället för en sekantlinje, med en lutning som härleds från kurvans derivata. Även om dessa formler involverar kalkyl över reella tal, blir de helt diskreta och exakta när kurvan definieras över ett ändligt fält - det sammanhang som används i Bitcoin.


### Från matematik till Bitcoin-kryptografi


Finita fält ger deterministisk, inverterbar aritmetik; elliptiska kurvor ger en icke-linjär struktur där det är lätt att beräkna k-P men omöjligt att vända på det. Kombinationen av de båda ger grunden för Bitcoin:s offentliga/privata nycklar, ECDSA-signaturer och transaktionssäkerhet. Genom att förstå dessa grundläggande principer förbereds studenterna för att implementera nycklar, transaktioner och signaturer direkt - utan abstraktioner eller externa verktyg.


## Kryptografi med elliptisk kurva

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>


![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


I det här kapitlet introduceras elliptiska kurvor definierade över finita fält och det förklaras varför de utgör den matematiska ryggraden i Bitcoin:s kryptografi. Medan elliptiska kurvor över reella tal verkar jämna och kontinuerliga, skapar tillämpningen av samma ekvationer över ett finit fält en diskret, utspridd uppsättning punkter. Trots den visuella skillnaden beter sig alla formler för punktaddition, lutningar och algebraiska regler exakt likadant - det är bara aritmetiken som ändras till modulär aritmetik. Bitcoin använder kurvan y² = x³ + 7 (secp256k1), som bevarar symmetri och icke-linjärt beteende som är viktigt för kryptografisk säkerhet.


### Verifiering av punkter och implementering av finita fält


En punkt ligger på en elliptisk kurva med finita fält om dess koordinater uppfyller kurvekvationen under modulo p. För att verifiera en punkt som (73,128) på F₁₃₇ krävs att man kontrollerar att y² mod p är lika med x³ + 7 mod p. För att implementera detta i kod måste man skapa klasser för element med finita fält och kurvpunkter. Operatörsöverladdning säkerställer att all aritmetik - addition, multiplikation, exponentiering, division - automatiskt utförs modulo p. När dessa abstraktioner finns blir mer avancerade kryptografiska operationer enkla att skriva och resonera om.


#### Gruppegenskaper och punktaddition

Elliptiska kurvors punkter bildar en matematisk grupp under addition. Gruppen uppfyller kraven på slutenhet, associativitet, identitet (punkten i oändligheten) och invers (reflektion över x-axeln). Geometriska konstruktioner bekräftar dessa egenskaper och gör skalär multiplikation (P adderat till sig självt upprepade gånger) väldefinierad. Dessa gruppregler möjliggör kryptografi med elliptisk kurva och säkerställer ett konsekvent och förutsägbart beteende vid upprepade punktoperationer.


### Cykliska grupper och det diskreta logaritmproblemet


Genom att välja en generatorpunkt G på en kurva kan vi generate en cyklisk grupp: G, 2G, 3G, ..., nG = 0. Punkterna verkar icke-linjära och oförutsägbara, även när de genereras i följd. Denna oförutsägbarhet skapar grunden för det diskreta logaritmproblemet: det är lätt att beräkna P = sG, men att bestämma s från P är beräkningsmässigt omöjligt för stora grupper. Denna envägsfunktion är det som gör kryptografi med publika nycklar säker. Skalärer (privata nycklar) skrivs med små bokstäver, punkter (offentliga nycklar) med stora bokstäver.


#### Effektiv skalarmultiplikation

För att beräkna sG på ett effektivt sätt används dubbel- och additionsalgoritmen: scanna skalarens binära representation, dubbla punkten i varje steg och addera G endast när biten är 1. Detta minskar beräkningen från O(n) additioner till O(log n), vilket möjliggör praktiska kryptografiska operationer även med 256-bitarsskalärer.


#### Kurvan för secp256k1 i Bitcoin


Bitcoin använder kurvan secp256k1, definierad av y² = x³ + 7 över ett primtalsfält där p = 2²⁵⁶ - 2³² - 977. Generatorpunkten G har fasta koordinater som väljs med hjälp av en deterministisk NUMS-procedur ("nothing up my sleeve"). Gruppordningen n är ett stort primtal nära 2²⁵⁶, vilket garanterar att varje punkt som inte är noll genererar samma grupp. Storleken på 2²⁵⁶ (~10⁷⁷) är astronomiskt stor, vilket gör det fysiskt omöjligt att brute-forcen privata nycklar. Inte ens en triljon superdatorer som körs i en triljon år skulle minska nyckelutrymmet på ett meningsfullt sätt.


### Offentliga nycklar, privata nycklar och SEC Serialization


En privat nyckel är en slumpmässig skalär s; den publika nyckeln är P = sG. Eftersom det är omöjligt att lösa det diskreta log-problemet kan P delas utan att s avslöjas. Publika nycklar måste serialiseras för överföring med SEC-format. Det okomprimerade SEC-formatet använder 65 byte: prefix 0x04 + x-koordinat + y-koordinat. Det komprimerade formatet använder endast 33 byte: prefix 0x02 eller 0x03 (beroende på y:s paritet) + x-koordinat. Bitcoin använde ursprungligen okomprimerade nycklar men föredrar nu komprimerade nycklar för effektivitetens skull.


#### Bitcoin Address Skapande


Bitcoin-adresser är hashvärden av offentliga nycklar, inte själva rånycklarna. För att generate en adress, serialisera den publika nyckeln i SEC-format, beräkna hash160 (SHA-256 och sedan RIPEMD-160), lägg till nätverksprefixet (0x00 för mainnet, 0x6F för testnet), beräkna en kontrollsumma med dubbla SHA-256, lägg till de fyra första bytena med kontrollsumman och koda resultatet med Base58. Denna kodning tar bort tvetydiga tecken och inkluderar kontrollsumman för att förhindra transkriptionsfel. Den flerstegade pipelinen döljer den publika nyckeln tills en användning sker, lägger till nätverksidentifiering och säkerställer läsbara, felsäkra adresser.


# Bitcoin Transaktionens inre arbete

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin Transaktionsparsning och ECDSA-signaturer

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>


![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


### Förstå ECDSA: Bitcoin:s stiftelse för digitala signaturer


Bitcoin förlitar sig på ECDSA, ett elliptisk kurva-baserat signaturschema som erbjuder stark säkerhet med mycket mindre nyckelstorlekar än RSA. Dess säkerhet kommer från den elliptiska kurvans diskreta logaritmproblem: givet P = eG är det enkelt att beräkna P, men att härleda e från P är beräkningsmässigt ogenomförbart. Denna asymmetri möjliggör kryptografi med publika nycklar samtidigt som privata nycklar hålls säkra.


#### DER-kodning av ECDSA-signaturer


Bitcoin kodar ECDSA-signaturer med hjälp av DER-formatet:


- 0x30 (sekvensmarkör)
- längd byte
- 0x02 + längd + R byte
- 0x02 + längd + S byte


Detta ökar omkostnaderna och utökar en signatur på 64 byte till ~71-72 byte. Taproot eliminerar denna ineffektivitet genom att anta Schnorr-signaturer med fast storlek.


### Signaturåtaganden och signeringsprocessen


ECDSA-signaturer bygger på en åtagandeekvation: UG + VP = KG. Signatören väljer U- och V-värden som inte är noll och en slumpmässig nonce K, vilket bevisar att han känner till den privata nyckeln utan att avslöja den. Meddelandet hashas till Z, en slumpmässig K genereras, R är x-koordinaten för KG och S = (Z + RE)/K. Signaturen utgörs av paret (R, S). Säkerheten är beroende av att ett unikt och oförutsägbart K används - om K återanvänds eller läcker ut är den privata nyckeln äventyrad. Moderna implementeringar använder deterministisk K-generering (RFC 6979) för att undvika RNG-fel.


#### Verifiering av signatur

Givet Z, (R, S) och den offentliga nyckeln P beräknar verifieraren U = Z/S och V = R/S och kontrollerar sedan om x-koordinaten för UG + VP är lika med R. Detta fungerar eftersom verifieringsalgebran rekonstruerar KG utan att behöva den privata nyckeln. Att förfalska signaturer skulle kräva att man löser det diskreta log-problemet eller bryter hashfunktionen.


#### Schnorr-signaturer och historisk kontext


Schnorr-signaturer är matematiskt renare och har stöd för aggregeringsfunktioner, men var patenterade när Bitcoin lanserades. ECDSA erbjöd ett gratis alternativ, men med mer komplexitet och större signaturer. När patenten löpte ut lade Bitcoin till Schnorr-signaturer via Taproot, vilket gav fasta 64-byte-signaturer och förbättrad integritet. ECDSA stöds fortfarande för äldre kompatibilitet.



### Transaktionsstruktur och inmatningar/utmatningar


En Bitcoin-transaktion består av:


- version (4 byte, little-endian)
- inmatningslista
- utgångslista
- locktime (4 byte)


Ingångar refererar till tidigare UTXO:er genom deras transaktionshash och utgångsindex, och inkluderar ett upplåsningsskript (scriptSig) och ett sekvensnummer som används för tidslås eller RBF. Utdata specificerar beloppet (8 byte) och låsningsskriptet (scriptPubKey), som definierar utgiftsvillkoren. Bitcoin-adresser är representationer av dessa skript.


#### UTXO-modellen

Bitcoin spårar outnyttjade outputs snarare än kontosaldon. UTXO:er måste spenderas helt och hållet - partiella utgifter är omöjliga. För att spendera 1 BTC från en 100 BTC UTXO måste en transaktion inkludera en förändringsutgång. Om du glömmer ändringsutgången blir återstoden en gruvarbetaravgift.


#### Serialisering och parsning av transaktioner


Transaktionerna använder ett kompakt binärt format. Efter versionsfältet kodar en varint antalet inmatningar. Inmatningar inkluderar:


- tidigare tx-hash (32 byte)
- utmatningsindex (4 byte)
- scriptSig (varstr)
- sekvens (4 byte)


Utdata inkluderar ett belopp på 8 byte och scriptPubKey (varstr). Locktime styr när transaktionen blir giltig. Serialisering använder little-endian-ordning för de flesta heltal. Parsers konsumerar bytes sekventiellt och delegerar till specialiserade klasser för inmatningar, utmatningar och skript.


### Avgifter, förändring och formbarhet


Avgifterna är implicita:

avgift = summa(ingångsvärden) - summa(utgångsvärden).

Varje icke tilldelat värde blir avgiften, vilket gör det viktigt med korrekt konstruktion av ändringsutdata. Före SegWit tillät signaturer manipulerbarhet - genom att ändra S till N-S skapades en ny giltig transaktion med ett annat ID. Bitcoin tillämpar nu en regel med lågt S och SegWit isolerar signaturer från txid-beräkningen, vilket gör ID:n stabila och möjliggör protokoll i andra lagret som Lightning.


## Bitcoin Skript- och transaktionsvalidering

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>


![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


Bitcoin Script är ett litet, stackbaserat smart kontraktsspråk som definierar hur mynt kan spenderas. Varje utdata har en scriptPubKey (låsningsskript) och varje indata har en scriptSig (upplåsningsskript). Tillsammans bildar de ett program som måste utvärderas till "sant" för att spenderingen ska vara giltig. Script är avsiktligt inte Turing-komplett så att alla exekveringsvägar är förutsägbara och lätta att validera i hela nätverket.


### Skriptoperationer och exekveringsmodell


Ett skript är en sekvens av dataelement och opkoder. Datapushar (signaturer, offentliga nycklar, hashar) placeras på stacken, medan opkoder som börjar med `OP_` transformerar stacken. Efter exekvering måste det översta stapelelementet vara icke-noll för att lyckas. Exempel: `OP_DUP` duplicerar det översta elementet, `OP_HASH160` använder SHA256 och sedan RIPEMD160, och `OP_CHECKSIG` verifierar en signatur mot transaktionens sighash och en publik nyckel, med 1 för giltig, 0 för ogiltig. Parsingreglerna skiljer mellan rådata (längdprefixerade) och opkoder (söks upp efter bytevärde), och en liten virtuell maskin utför dem deterministiskt på varje nod.


### P2PK och P2PKH: Centrala betalningsmönster


Det tidigaste mönstret, Pay-to-Public-Key (P2PK), låste mynt direkt till en fullständig publik nyckel: scriptPubKey är `<pubkey> OP_CHECKSIG`, och scriptSig är bara en signatur. Det är enkelt men utrymmesineffektivt och exponerar den publika nyckeln innan mynten spenderas.


#### P2PKH och adresser

Pay-to-Public-Key-Hash (P2PKH) förbättrar detta genom att låsa till en 20-byte hash av den offentliga nyckeln. ScriptPubKey är `OP_DUP OP_HASH160 <pubkey_hash> OP_EQUALVERIFY OP_CHECKSIG`, och scriptSig tillhandahåller `<signature> <pubkey>`. Exekveringen kontrollerar att den tillhandahållna publika nyckeln hashar till det bekräftade värdet och verifierar sedan signaturen. Detta döljer den publika nyckeln tills det är dags att använda den, minskar storleken och matchar det välbekanta "1..." mainnet adressformat.


### Transaktionsvalidering och signaturhashing


En nod som validerar en transaktion måste säkerställa detta:

1) Varje input refererar till en befintlig, outnyttjad output.

2) Totalt ingångsvärde ≥ totalt utgångsvärde (skillnaden är avgiften).

3) Varje scriptSig låser korrekt upp sin scriptPubKey som det hänvisas till.


För signaturverifiering krävs att man konstruerar det exakta meddelandet som signerades, kallat sighash. För äldre ECDSA innebär validering att alla scriptSigs töms, att den aktuella inmatningens scriptSig ersätts med motsvarande scriptPubKey, att en 4-bytes hashtyp (vanligtvis `SIGHASH_ALL`) läggs till och att resultatet dubbelhashas. Det 256-bitarsvärdet är det som `OP_CHECKSIG` använder. Alternativa hashtyper (t.ex. `SINGLE`, `NONE`, med eller utan `ANYONECANPAY`) ändrar vilka delar av transaktionen som bekräftas, vilket möjliggör nischade användningsfall som samarbetsfinansiering eller delvis specificerade transaktioner, men de används sällan i praktiken.


#### Kvadratisk hashning och SegWit

Eftersom varje inmatning i en äldre transaktion kräver sin egen sighash-beräkning över en struktur som omfattar alla inmatningar, kan valideringstiden växa kvadratiskt med antalet inmatningar. Stora transaktioner med flera inmatningar orsakade en gång märkbara valideringsfördröjningar. SegWit omformade sighash-beräkningen för att cacha delade delar och minska komplexiteten till linjär tid, vilket förbättrar skalbarheten och gör överbelastningsattacker svårare.


### Skriptpussel och säkerhetslektioner


Skript kan uttrycka mycket mer än bara "en signatur låser upp dessa mynt" Script-pussel visar detta genom att koda godtyckliga villkor - matematikproblem, hashpreimage-utmaningar eller till och med kollisionsbounties - där alla som tillhandahåller rätt data kan spendera mynten. Utgångar som endast förlitar sig på offentliga data (inga signaturer) är dock sårbara för gruvarbetares front-running: när en giltig lösning dyker upp i mempoolen kan vilken gruvarbetare som helst kopiera den och omdirigera utbetalningen till sig själva.


Den praktiska lärdomen är att verkliga kontrakt nästan alltid innehåller signaturkontroller, även när de innehåller mer komplex logik som multisig, timelocks eller hashlocks. Signaturer binder lösningen till en specifik part, bevarar incitament och förhindrar att andra stjäl utbetalningen. Att förstå Scripts stackmodell, standardmönster och subtila fallgropar är viktigt för att utforma säkra Bitcoin smarta kontrakt och för att resonera om hur transaktioner faktiskt valideras i nätverket.


## Transaktionskonstruktion och Pay-to-Script Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>


![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


### Byggnad Bitcoin Transaktioner och P2SH


Bitcoin-transaktionskonstruktion överbryggar teoretisk protokollkunskap med praktisk implementering. En transaktion väljer UTXO:er att spendera, bygger utgångar med låsningsskript, skapar signaturer för varje ingång och serialiserar allt i det exakta format som noderna förväntar sig. Processen kräver förståelse för generering av sighash, skriptbeteende och korrekt hantering av avgifter och ändringar.


### Grundläggande transaktionskonstruktion


Varje transaktionsinmatning refererar till en tidigare utmatning med txid och index. Utdata specificerar belopp i satoshis och låsningsskript. Skillnaden mellan totala inmatningar och totala utmatningar är avgiften. För att signera en inmatning serialiseras en modifierad version av transaktionen, dess sighash beräknas och den privata nyckeln signerar den. Den resulterande signaturen och den publika nyckeln bildar ScriptSig. När alla inmatningar har signerats kan den obearbetade transaktionen sändas till nätverket.


### Transaktioner med flera signaturer


Bare multisig använder `OP_CHECKMULTISIG` för att kräva m-av-n signaturer. På grund av en tidig off-by-one-bugg förbrukar OP_CHECKMULTISIG ett extra stackelement, vilket kräver en initial `OP_0` i ScriptSig. Bare multisig är funktionellt men ineffektivt: alla publika nycklar visas on-chain, vilket gör scriptPubKeys stora, dyra och svåra att koda som adresser. Dessa begränsningar motiverade införandet av pay-to-script-hash.


#### P2SH Arkitektur

P2SH döljer komplexa skript bakom en 20-byte HASH160. ScriptPubKey är fast: `OP_HASH160 <20-byte hash> OP_EQUAL`. Det underliggande redeem-skriptet - som innehåller multisig, tidslås eller andra villkor - avslöjas och exekveras endast när det spenderas. Avsändaren ser bara hashen, medan mottagaren hanterar inlösenskriptet privat. Denna design minskar on-chain-storleken, förbättrar integriteten och möjliggör komplexa kontrakt utan att belasta avsändarna.


### P2SH Utgifter och genomförande


För att använda en P2SH-utgång måste ScriptSig innehålla nödvändiga upplåsningsdata *plus* själva inlösenskriptet. Valideringen sker i två steg:

1) HASH160(redeem_script) måste matcha scriptPubKey-hashvärdet.

2) Efter verifiering körs redeem-skriptet med de angivna uppgifterna.


Vid generering av signaturer för en P2SH-ingång använder sighash-processen redeem-skriptet i stället för scriptPubKey. Varje undertecknare måste ha det fullständiga redeem-skriptet för att generate ska vara giltiga signaturer. P2SH-adresser använder versionsbyte 0x05 på mainnet ("3..."-adresser) och 0xC4 på testnet ("2..."-adresser).


#### Praktiska säkerhetsöverväganden


Att förlora ett redeem-skript innebär att förlora pengar: utgifter kräver både de privata nycklarna och själva redeem-skriptet. Multisig-deltagare måste verifiera att deras offentliga nycklar är korrekt inkluderade innan de accepterar insättningar. P2SH stöder avancerade konstruktioner som multisig, tidslås och hashlocks, men fel i skriptlogiken kan låsa medel permanent, så det är viktigt att testa på testnet.


P2SH förbättrar integriteten genom att dölja utgiftsvillkoren fram till den första utgiften, men när inlösenskriptet visas on-chain blir det permanent synligt. Trots detta gjorde fördelarna med minskad storlek, bakåtkompatibilitet och flexibelt kontraktsstöd P2SH till en viktig milstolpe som påverkade senare uppgraderingar som SegWit och Taproot.


# Bitcoin-nätverkets inre arbete

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Bitcoin Block och Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>


![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


Bitcoin blockerar grupptransaktioner och säkrar dem med hjälp av proof of work. Varje block innehåller en header på 80 byte samt en lista över transaktioner. Trots den höga energikostnaden för att producera ett giltigt block är det billigt att verifiera ett: att lagra alla ~900k headers kräver bara ~72 MB, vilket gör att även små enheter kan verifiera kedjans proof of work på ett effektivt sätt.


### Coinbase-transaktioner och Block Rewards


Varje block börjar med exakt en Coinbase-transaktion - det enda sättet för nya bitcoin att komma i omlopp. Det har en nollställd prev-tx-hash och ett index på 0xffffffffff, vilket identifierar det på ett unikt sätt. Subventionen började på 50 BTC och halveras var 210 000:e block (50, 25, 12,5, 6,25, 3,125, ...). Gruvarbetare inkluderar också transaktionsavgifter. Eftersom noncen på 4 byte är för liten för moderna ASIC:er modifierar miners data i Coinbase-transaktionen för att ändra Merkle-roten och skapa ytterligare sökutrymme. BIP34 kräver att blockhöjden bäddas in i Coinbase scriptSig för att säkerställa att varje Coinbase txid är unik.


### Blockhuvudfält och Soft Fork-signalering


Huvudet på 80 byte innehåller:


- version (4 byte)
- hash för föregående block (32 byte)
- Merkle rot (32 byte)
- tidsstämpel (4 byte)
- bitar (svårighetsmål, 4 byte)
- nonce (4 byte)


Versionsnummer utvecklades till ett bitfältssignaleringssystem via BIP9, vilket gjorde det möjligt för gruvarbetare att samordna soft-fork-beredskap. Tidsstämpeln är ett 32-bitars Unix-tidsvärde och kommer att behöva uppdateras runt år 2106.


#### Bits-fält och mål

Bitfältet kodar målet i kompakt form: mål = koefficient × 256^(exponent-3). Giltiga blockhashar måste ligga numeriskt under detta mål. Eftersom hasher tolkas som little-endian heltal visas giltiga hasher ofta med många nollor efteråt när de visas i hex.


### Svårighetsgrad, validering och justeringar


Svårighetsgrad definieras som lowest_target / current_target, vilket uttrycker hur mycket svårare mining är idag jämfört med den enklast möjliga svårighetsgraden. Validering kräver endast att man jämför rubrikens hash med målet - extremt billigt i förhållande till mining.


Varje 2016-block justerar Bitcoin svårighetsgraden för att rikta in sig på blockintervall på ~ 10 minuter. Justeringen jämför den faktiska tiden för de föregående 2016-blocken med de förväntade två veckorna. Begränsningar begränsar justeringar till inom en faktor fyra. Stora händelser i den verkliga världen - som Kinas mining-förbud - demonstrerade denna mekanisms motståndskraft när hashfrekvensen sjönk kraftigt och svårigheten justerades nedåt för att kompensera.


### Blocksubvention och totalt Supply


Subventionen på höjden h beräknas enligt följande: subvention = 5_000_000_000 >> (h // 210_000). Detta ger halveringsschemat som konvergerar mot en total tillgång på ~21 miljoner BTC. Summeringen av den geometriska serien (50 + 25 + 12,5 + ...) × 210 000 förklarar taket. Gruvarbetare kan göra anspråk på mindre än den tillåtna subventionen men aldrig mer, annars blir blocket ogiltigt. Eftersom subventionerna krymper över successiva halveringar blir transaktionsavgifter en allt viktigare del av gruvarbetarnas intäkter och den långsiktiga nätverkssäkerheten.


## Nätverkskommunikation och Merkle-träd

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>


![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


### Bitcoin Nätverksarkitektur


Bitcoin:s peer-to-peer-nätverk fungerar som ett decentraliserat skvallersystem där noder vidarebefordrar transaktioner och block utan att lita på varandra. Nya noder startas genom att kontakta hårdkodade DNS-frön som underhålls av kärnutvecklare. Dessa DNS-frön returnerar IP-adresser för aktiva peers, vilket gör det möjligt för noder att upptäcka nätverket och sedan begära ytterligare peers via getaddr. Nätverk är avsiktligt inte konsensuskritiska, så implementeringar kan skilja sig åt så länge som konsensusreglerna förblir oförändrade.


### Meddelandestruktur och handskakning


Alla Bitcoin P2P-meddelanden använder ett fast kuvert: ett magiskt värde på 4 byte (F9BEB4D9 för mainnet), ett ASCII-kommando på 12 byte, en nyttolastlängd på 4 byte i little-endian, en kontrollsumma på 4 byte (de första 4 byte av hash256) och nyttolasten. Vanliga kommandon är version, verack, inv, getdata, tx, block, getheaders, headers, ping och pong.


Handskakningen börjar med att en anslutande nod skickar ett versionsmeddelande. Mottagaren svarar med verack och sin egen version. När båda sidor har utbytt dessa två meddelanden är anslutningen aktiv och noderna kan börja vidarebefordra inventarier och data.


### Merkle-träd och Merkle-rötter


Bitcoin lagrar en enda Merkle-rot på 32 byte i varje blockhuvud som ett åtagande för alla transaktioner i blocket. Transaktionerna hashas (hash256), paras ihop, sammankopplas och hashas upprepade gånger tills en hash återstår. När en nivå har ett udda antal dupliceras den sista hashen. Internt är hasharna big-endian, medan serialiserad blockdata använder little-endian, vilket kräver reversering före och efter trädkonstruktion.


#### Merkle-bevis och SPV

Merkle-bevis gör det möjligt att verifiera att en transaktion ingår i ett block utan att ladda ner hela blocket. Beviset består av syskonhashar längs vägen till roten. Lättviktiga SPV-klienter lagrar endast blockhuvuden och begär dessa bevis från fullständiga noder. Eftersom ett Merkle-träd växer logaritmiskt krävs det bara några hundra byte för att bevisa att en transaktion ingår i ett block med tusentals transaktioner.


Taproot utvidgar detta koncept genom att binda utgiftsvillkor till ett Merklized script tree (MAST) och endast avslöja den exekverade grenen tillsammans med ett Merkle-bevis. Detta förbättrar både effektiviteten och integriteten.


### Nätverksdrift och blocksynkronisering


Noder använder getdata för att begära transaktioner eller block, och anger ett typ-ID (1=tx, 2=block, 3=filtrerat block, 4=kompakt block) plus en 32-bytes identifierare. För kedjesynkronisering skickar noderna getheaders med en hash för startblocket och får upp till 2000 headers som svar. Varje returnerat huvud är 80 byte följt av ett dummy-transaktionsantal på noll.


Fullständig verifiering av mottagna block kräver två kontroller:

1. Blockets hash måste ligga under det mål som kodas i bits-fältet.

2. Den Merkle-rot som beräknas från alla transaktioner (med korrekt hantering av endianness) måste matcha rubrikens rot.


Endast om båda villkoren uppfylls accepterar en nod blockeringen, vilket återspeglar Bitcoin:s princip "lita inte på, verifiera".


## Avancerad nodkommunikation och segregerat vittne

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>


![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)


Den här sessionen förenar avancerat P2P-nätverk med Segregated Witness och visar hur modern Bitcoin-programvara interagerar direkt med noder samtidigt som den använder SegWit-medvetna transaktionsstrukturer. Utvecklare lär sig att hämta block, söka efter relevanta transaktioner och konstruera transaktioner med hjälp av endast rå nätverkskommunikation - inga blockutforskare krävs.


### Blockbaserad transaktionshämtning och sekretess


Plånböcker måste upptäcka inkommande betalningar genom att skanna block efter utdata som matchar deras scriptPubKey. Att hämta hela block skyddar integriteten bättre än att begära enskilda transaktioner, vilket läcker starka signaler om användaraktivitet. Även blockförfrågningar kan läcka information om kedjor med låg volym, vilket gör kompakta blockfilter (BIP158) viktiga för integritetsskyddande lätta klienter. Filter kan ge falska positiva resultat men aldrig falska negativa, vilket gör att klienter endast kan ladda ner potentiellt relevanta block utan att avslöja specifika adresser.


### Trustless Interaktion mellan nätverk


Arbetsflödet `get_block` visar korrekt nätverksanvändning: skicka getdata, ta emot ett block och verifiera sedan oberoende dess Merkle-rot och proof of work. Ett block accepteras endast om den mottagna headerhashningen matchar den begärda hashningen och dess beräknade Merkle-rot matchar headern. Detta är ett uttryck för "lita inte på, verifiera", vilket säkerställer att inte ens illasinnade kamrater kan lura noder att acceptera ändrade data.


#### Hämtning av transaktioner från block

Ett blocks transaktioner kan skannas efter matchande scriptPubKeys med hjälp av enkel iteration. Produktionsplånböcker utför detta kontinuerligt när nya block anländer, vilket bevisar äganderätten till utgångar strikt genom kryptografisk validering snarare än att förlita sig på API:er från tredje part.


### SegWit Mål och design


Segregerat vittne (SegWit) löste problemet med transaktionsmissbruk genom att ta bort signaturdata från beräkningen av txid. Detta möjliggjorde tillförlitliga för-signerade transaktionskedjor och gjorde Lightning Network praktisk. SegWit ökade också blockkapaciteten med hjälp av "blockvikt": gamla noder ser fortfarande ≤1 MB-block, medan uppgraderade noder validerar upp till 4 MB inklusive vittnesdata. Versionerade vittnesprogram (v0-v1 hittills) skapar en strukturerad uppgraderingsväg för framtida skripttyper.


#### P2WPKH (ursprunglig SegWit)


P2WPKH ersätter den äldre P2PKH-strukturen med ett skript på 22 byte: OP_0 + push20 + hash160(pubkey). Utgifter flyttar signaturen och pubnyckeln till ett separat vittnesfält.


- Pre-SegWit noder: se "vem som helst kan spendera", behandla det som giltigt.
- Noder efter SegWit: känner igen OP_0 + 20-byte hash och validerar med hjälp av vittnesdata.


Denna separation åtgärdar formbarheten och minskar avgifterna. Vittnet använder en varint count följt av signaturen och pubkey.


#### P2SH-P2WPKH (bakåtkompatibel med SegWit)


För att gamla plånböcker ska kunna skicka till SegWit-adresser kan P2WPKH-skript paketeras i P2SH.


- scriptPubKey: standard P2SH hash160(redeemScript)
- scriptSig: redeemScript (programmet P2WPKH)
- vittne: signatur + pubnyckel


Valideringslager:

1. Pre-BIP16-noder accepterar redeemScript som giltigt.

2. Post-BIP16-noderna utvärderar den och lämnar OP_0 + hash på stacken.

3. SegWit-noderna utför fullständig vittnesvalidering.


#### P2WSH för komplexa skript


P2WSH generaliserar SegWit för multisig och avancerade skript genom att använda SHA256(skript) istället för hash160. En typisk 2-av-3 multisig vittnesstack:


- tomt element (CHECKMULTISIG-bugg)
- sig1
- sig2
- vittnesskrift (multisigskrift)


SegWit-noderna verifierar att SHA256(witnessScript) matchar scriptPubKey-hashen och kör den sedan. Genom att använda SHA256 och en 32-byte-hash kan P2WSH särskiljas från P2WPKH och säkerheten stärkas.


#### P2SH-P2WSH (maximal kompatibilitet)


Komplexa SegWit-skript kan också vara P2SH-förpackade:


- scriptSig: redeemScript (OP_0 + 32-byte hash)
- vittne: signaturer + vittnesskrift


Validering passerar genom tre generationer av regler precis som med P2SH-P2WPKH. Detta omslag var viktigt för tidiga Lightning-distributioner som behövde multisig utan formbarhet. Även om inbyggd P2WSH föredras idag, säkerställer den omslutna formen kompatibilitet mellan äldre wallet-system.


### SegWit:s inverkan


SegWit tillhandahålls:


- iD för stabila transaktioner
- lägre avgifter genom rabatterade vittnesuppgifter
- högre blockgenomströmning via blockvikt
- kompatibilitet för gamla noder
- en ren uppgraderingsväg för Taproot och framtida tillägg


Tillsammans med tillförlitlig nätverksinteraktion utgör dessa verktyg ryggraden i modern Bitcoin-utveckling.



# Sista avsnittet


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Recensioner & betyg


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>

## Slutlig tentamen


<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>



<isCourseExam>true</isCourseExam>

## Slutsats



<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>


<isCourseConclusion>true</isCourseConclusion>