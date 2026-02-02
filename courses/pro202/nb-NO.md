---
name: Programmering Bitcoin
goal: Bygg et komplett Bitcoin-bibliotek fra bunnen av og forstå Bitcoins kryptografiske grunnlag
objectives: 

 - Implementere aritmetikk for finitte felt og elliptiske kurveoperasjoner i Python
 - Konstruere og analysere Bitcoin-transaksjoner programmatisk
 - Opprette testnettadresser og kringkaste transaksjoner over nettverket
 - Beherske det matematiske grunnlaget som ligger til grunn for Bitcoins sikkerhetsmodell

---
# En reise inn i Bitcoins skript og programmer


Dette intensive todagerskurset, undervist av Jimmy Song, tar deg dypt inn i Bitcoins tekniske grunnlag ved å bygge et komplett Bitcoin-bibliotek fra grunnen av. Du starter med den grunnleggende matematikken i finitte felt og elliptiske kurver, og går videre gjennom transaksjonsparsing, skriptkjøring og nettverkskommunikasjon. Gjennom praktiske kodingsøvelser i Jupyter-notatbøker oppretter du din egen testnettadresse, konstruerer transaksjoner manuelt og sender dem direkte til nettverket - alt mens du får en dyp forståelse av de kryptografiske prinsippene som gjør Bitcoin sikkert og tillitsløst.


Nyt reisen!


+++

# Innledning


<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>


## Kursoversikt


<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>


Velkommen til kurset PRO 202 _**Programmering av Bitcoin**_, en intensiv reise som tar deg fra finite field-aritmetikk hele veien til å bygge og kringkaste ekte transaksjoner på Bitcoins Testnet.


I dette kurset vil du gradvis bygge et Bitcoin-bibliotek i Python, samtidig som du tilegner deg det kryptografiske, protokoll- og programvaregrunnlaget som er nødvendig for å resonnere nøyaktig om Bitcoins sikkerhet og indre virkemåte. PRO 202-tilnærmingen er gjennomgående praktisk: Hvert konsept blir umiddelbart implementert i Jupyter-notatbøker, slik at teori og kode styrker hverandre.


### Grunnleggende matematiske begreper for Bitcoin


I denne første delen etableres det uunnværlige matematiske grunnlaget. Du vil implementere aritmetikk for endelige felt og elliptiske kurveoperasjoner (gruppelov, addisjon, dobling, skalarmultiplikasjon...) - forutsetningene for ECDSA. Målet er todelt: å forstå den algebraiske strukturen som gjør kryptografiske signaturer mulige, og å bygge pålitelige Python-verktøy for å manipulere dem.


Deretter formaliserer du komponentene i ECDSA: nøkkelgenerering, punktformatering, hashing, oppretting av signaturer og verifisering. Denne delen knytter teori direkte til praksis, og legger vekt på implementeringsdetaljer og robustheten til den underliggende sikkerhetsmodellen.


### Bitcoin Transaksjonens indre funksjoner


I den andre delen vil du dissekere strukturen i en Bitcoin-transaksjon: UTXO-er, innganger/utganger, sekvenser, skript, kodinger og mer. Du vil skrive kode for å konstruere, signere og verifisere transaksjoner, og du vil få en presis forståelse av hva som er forpliktet av hashen og hvorfor.


Deretter skal du implementere en minimal _Script_-kjører, gå gjennom viktige operasjonskoder og validere utgiftsveier. Målet er å gjøre deg i stand til å revidere transaksjonsatferd, diagnostisere valideringsfeil og resonnere om sikkerheten til utgiftspolicyer.


### Bitcoin-nettverkets indre funksjoner


I den tredje delen skal du plassere transaksjoner i et bredere system: blokkstruktur, overskrifter, vanskelighetsgrad og Proof-of-Work-mekanismen. Du skal håndtere protokollmeldinger, blokkhoder og Merkle-trær.


Til slutt vil du studere node-til-node-kommunikasjon, meldingsoptimalisering og introduksjonen av SegWit.


Som med alle kurs om Plan ₿ Academy inneholder den siste delen en evaluering som er utformet for å konsolidere forståelsen din. Er du klar til å avdekke hvordan Bitcoin fungerer og skrive koden som driver den? La oss begynne!










# Grunnleggende matematiske begreper for Bitcoin

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Matematikk for implementering av Bitcoin

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>


![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


### Bitcoin Grunnleggende programmering: Matematiske kjernestrukturer


Dette kurset kondenserer den essensielle matematikken bak Bitcoins kryptografiske systemer til en svært praktisk arbeidsflyt. Konsepter blir forklart, demonstrert med eksempler og deretter implementert i Jupyter Notebook. Den ledende ideen er enkel: Du forstår en kryptografisk primitivitet først når du koder den. I løpet av de to dagene kurset varer, skal studentene generate testnettadresser, bygge og kringkaste transaksjoner, og til slutt samhandle med nettverket uten blokkutforskere. Alt dette krever et solid grunnlag i finitte felt og elliptiske kurver.


### Finite felt: Kryptografiens aritmetiske motor


Et endelig felt F(p) er et aritmetisk system definert av et primtall p, som inneholder elementene 0 til og med p-1. Primtallsfelt sikrer at alle elementer som ikke er null, har en invers, og at alle operasjoner forblir innenfor feltet. Aritmetikk omslutter modulo p for addisjon, subtraksjon og multiplikasjon. Pythons `pow(base, exp, mod)` muliggjør effektiv modulær eksponentiering, noe som er avgjørende for store eksponenter som brukes i ekte kryptografiske operasjoner.


#### Multiplikativ oppførsel

Ved å multiplisere et hvilket som helst element k som ikke er null, med alle elementene i et primtallfelt, får man en permutasjon av feltet. Denne egenskapen garanterer ensartethet og forhindrer strukturelle svakheter, noe som gjør primtallsfelt ideelle for sikker nøkkelgenerering og digitale signaturer.


#### Divisjon og Fermats lille læresetning

Divisjon implementeres ved hjelp av multiplikative inverser. Fermats lille teorem sier at

n^(p-1) ≡ 1 (mod p),

så den inverse er n^(p-2). Python støtter dette direkte med `pow(n, -1, p)`. Disse operasjonene forekommer stadig i ECDSA og Bitcoins underliggende kryptografiske rutiner.


### Elliptiske kurver: Ikke-lineære strukturer for sikkerhet med offentlige nøkler


Elliptiske kurver følger ligningen y² = x³ + ax + b. Bitcoin bruker secp256k1, definert som y² = x³ + 7 over et endelig felt. Punkter på en elliptisk kurve danner en matematisk gruppe under punktaddering. En linje trukket gjennom to punkter P og Q skjærer kurven i et tredje punkt R; ved å speile R over x-aksen får man P + Q. Dette systemet er assosiativt og inkluderer et identitetselement: punktet i uendelig.


Ved dobling av et punkt brukes en tangentlinje i stedet for en sekantlinje, med helning avledet fra kurvens deriverte. Selv om disse formlene involverer kalkulus over reelle tall, blir de helt diskrete og eksakte når kurven er definert over et endelig felt - den konteksten som brukes i Bitcoin.


### Fra matematikk tBitcoin-kryptografi


Finitte felt gir deterministisk, inverterbar aritmetikk, mens elliptiske kurver gir en ikke-lineær struktur der det er enkelt å beregne k-P, men ugjennomførbart å reversere den. Kombinasjonen av begge gir grunnlaget for Bitcoins offentlige/private nøkler, ECDSA-signaturer og transaksjonssikkerhet. Når studentene forstår disse grunnleggende prinsippene, er de godt rustet til å implementere nøkler, transaksjoner og signaturer direkte - uten abstraksjoner eller eksterne verktøy.


## Elliptisk kurvekryptografi

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>


![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


Dette kapittelet introduserer elliptiske kurver definert over endelige felt og forklarer hvorfor de utgjør den matematiske ryggraden i Bitcoins kryptografi. Mens elliptiske kurver over reelle tall ser glatte og kontinuerlige ut, skaper anvendelsen av de samme ligningene over et endelig felt et diskret, spredt sett med punkter. Til tross for den visuelle forskjellen oppfører alle punktaddisjonsformler, helninger og algebraiske regler seg på nøyaktig samme måte - det er bare aritmetikken som endres til modulær aritmetikk. Bitcoin bruker kurven y² = x³ + 7 (secp256k1), som bevarer symmetri og ikke-lineær oppførsel, noe som er avgjørende for kryptografisk sikkerhet.


### Verifiseringspunkter og implementering av endelige felt


Et punkt ligger på en elliptisk kurve med endelig felt hvis koordinatene tilfredsstiller kurvelikningen under modulo p. For å verifisere et punkt som (73,128) på F₁₃₇ må man kontrollere at y² mod p er lik x³ + 7 mod p. For å implementere dette i kode må man lage klasser for elementer i endelig felt og kurvepunkter. Operatoroverbelastning sørger for at all aritmetikk - addisjon, multiplikasjon, eksponentiering, divisjon - automatisk utføres modulo p. Når disse abstraksjonene finnes, blir det enkelt å skrive og resonnere om mer avanserte kryptografiske operasjoner.


#### Gruppeegenskaper og punktaddering

Elliptiske kurvepunkter danner en matematisk gruppe under addisjon. Gruppen tilfredsstiller kravene til lukking, assosiativitet, identitet (punktet i uendeligheten) og invers (refleksjon over x-aksen). Geometriske konstruksjoner bekrefter disse egenskapene, og gjør skalarmultiplikasjon (P addert til seg selv gjentatte ganger) veldefinert. Disse gruppereglene muliggjør elliptisk kurvekryptografi og sikrer konsistent, forutsigbar oppførsel under gjentatte punktoperasjoner.


### Sykliske grupper og det diskrete logaritmeproblemet


Ved å velge et generatorpunkt G på en kurve kan vi generate en syklisk gruppe: G, 2G, 3G, ..., nG = 0. Punktene virker ikke-lineære og uforutsigbare, selv når de genereres sekvensielt. Denne uforutsigbarheten danner grunnlaget for det diskrete logaritmeproblemet: Det er enkelt å beregne P = sG, men å bestemme s ut fra P er beregningsmessig ugjennomførbart for store grupper. Det er denne enveisfunksjonen som gjør kryptografi med offentlig nøkkel sikker. Skalarer (private nøkler) skrives med små bokstaver, mens punkter (offentlige nøkler) skrives med store bokstaver.


#### Effektiv skalarmultiplikasjon

For å beregne sG effektivt bruker implementeringer dobbelt-og-add-algoritmen: Skanning av skalarens binære representasjon, dobling av punktet i hvert trinn og addisjon av G bare når biten er 1. Dette reduserer beregningen fra O(n) addisjoner til O(log n), noe som muliggjør praktiske kryptografiske operasjoner selv med 256-biters skalarer.


#### Secp256k1-kurven i Bitcoin


Bitcoin bruker kurven secp256k1, definert av y² = x³ + 7 over et primtallfelt der p = 2²⁵⁶ - 2³² - 977. Generatorpunktet G har faste koordinater som velges ved hjelp av en deterministisk NUMS-prosedyre ("nothing up my sleeve"). Gruppens orden n er et stort primtall nær 2²⁵⁶, noe som sikrer at alle punkter som ikke er null, genererer den samme gruppen. Størrelsen på 2²⁵⁶ (~10⁷⁷) er astronomisk stor, noe som gjør det fysisk umulig å tvinge frem private nøkler. Selv en trillion superdatamaskiner som kjører i en trillion år, vil ikke redusere nøkkelområdet i nevneverdig grad.


### Offentlige nøkler, private nøkler og SEC-serialisering


En privat nøkkel er en tilfeldig skalar s, mens den offentlige nøkkelen er P = sG. Fordi det er umulig å løse det diskrete log-problemet, kan P deles uten å avsløre s. Offentlige nøkler må serialiseres for overføring ved hjelp av SEC-format. Ukomprimert SEC-format bruker 65 byte: prefiks 0x04 + x-koordinat + y-koordinat. Det komprimerte formatet bruker bare 33 byte: prefiks 0x02 eller 0x03 (avhengig av ys paritet) + x-koordinat. Bitcoin brukte opprinnelig ukomprimerte nøkler, men foretrekker nå komprimerte nøkler av effektivitetshensyn.


#### Bitcoin Address Opprettelse


Bitcoin-adresser er hashkoder av offentlige nøkler, ikke selve rånøklene. For å generate en adresse, serialiser den offentlige nøkkelen i SEC-format, beregn hash160 (SHA-256 og deretter RIPEMD-160), legg til nettverksprefikset (0x00 for mainnet, 0x6F for testnet), beregn en sjekksum ved hjelp av dobbel SHA-256, legg til de fire første byte med sjekksum, og kod resultatet med Base58. Denne kodingen fjerner tvetydige tegn og inkluderer sjekksummen for å forhindre transkripsjonsfeil. Flertrinnsløsningen skjuler den offentlige nøkkelen til det skjer et forbruk, legger til nettverksidentifikasjon og sikrer adresser som kan leses av mennesker og er motstandsdyktige mot feil.


# Bitcoin Transaksjonens indre funksjoner

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin Transaksjonsparsing og ECDSA-signaturer

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>


![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


### Forstå ECDSA: Bitcoins grunnlag for digital signatur


Bitcoin baserer seg på ECDSA, et elliptisk kurvebasert signaturskjema som gir sterk sikkerhet med langt mindre nøkkelstørrelser enn RSA. Sikkerheten kommer fra det elliptiske logaritmeproblemet: Gitt P = eG, er det enkelt å beregne P, men det er ugjennomførbart å utlede e fra P. Denne asymmetrien muliggjør kryptering med offentlig nøkkel, samtidig som private nøkler holdes sikre.


#### DER-koding av ECDSA-signaturer


Bitcoin koder ECDSA-signaturer ved hjelp av DER-formatet:


- 0x30 (sekvensmarkør)
- lengdebyte
- 0x02 + lengde + R byte
- 0x02 + lengde + S byte


Dette gir ekstra kostnader, og utvider en signatur på 64 byte til ~71-72 byte. Taproot eliminerer denne ineffektiviteten ved å ta i bruk Schnorr-signaturer med fast størrelse.


### Signaturforpliktelser og signeringsprosessen


ECDSA-signaturer baserer seg på en forpliktelsesligning: UG + VP = KG. Underskriveren velger U- og V-verdier som ikke er null, og en tilfeldig nonce K, som beviser kjennskap til den private nøkkelen uten å avsløre den. Meldingen hashes inn i Z, en tilfeldig K genereres, R er x-koordinaten til KG, og S = (Z + RE)/K. Signaturen er paret (R, S). Sikkerheten er kritisk avhengig av at det brukes en unik, uforutsigbar K - hvis K gjenbrukes eller lekker ut, er den private nøkkelen kompromittert. Moderne implementeringer bruker deterministisk K-generering (RFC 6979) for å unngå RNG-feil.


#### Verifisering av signatur

Gitt Z, (R, S) og den offentlige nøkkelen P, beregner verifikatoren U = Z/S og V = R/S, og sjekker deretter om x-koordinaten til UG + VP er lik R. Dette fungerer fordi verifikasjonsalgebraen rekonstruerer KG uten å trenge den private nøkkelen. For å forfalske signaturer må man løse det diskrete loggproblemet eller bryte hashfunksjonen.


#### Schnorr-signaturer og historisk kontekst


Schnorr-signaturer er matematisk renere og støtter aggregeringsfunksjoner, men var patentert da Bitcoin ble lansert. ECDSA tilbød et gratis alternativ, men med mer kompleksitet og større signaturer. Da patentene utløp, la Bitcoin til Schnorr-signaturer via Taproot, noe som ga faste 64-byte-signaturer og forbedret personvern. ECDSA støttes fortsatt av hensyn til kompatibilitet med eldre systemer.



### Transaksjonsstruktur og innganger/utganger


En Bitcoin-transaksjon består av:


- versjon (4 byte, little-endian)
- inputliste
- utdataliste
- locktime (4 byte)


Inndata refererer til tidligere UTXO-er ved hjelp av transaksjonshash og utgangsindeks, og inkluderer et opplåsingsskript (scriptSig) og et sekvensnummer som brukes for tidssperrer eller RBF. Utdata spesifiserer beløpet (8 byte) og låseskriptet (scriptPubKey), som definerer utgiftsbetingelser. Bitcoin-adresser er representasjoner av disse skriptene.


#### UTXO-modellen

Bitcoin sporer ubrukte utganger i stedet for kontosaldoer. UTXO-er må brukes i sin helhet - delvis bruk er umulig. For å bruke 1 BTC fra en UTXO på 100 BTC, må en transaksjon inkludere en endringsutgang. Hvis du glemmer endringsutgangen, blir resten til en gruvearbeideravgift.


#### Serialisering og parsing av transaksjoner


Transaksjoner bruker et kompakt binært format. Etter versjonsfeltet kommer en varint som koder for antall inndata. Innganger inkluderer:


- forrige tx-hash (32 byte)
- utgangsindeks (4 byte)
- scriptSig (varstr)
- sekvens (4 byte)


Utdataene inkluderer et beløp på 8 byte og scriptPubKey (varstr). Locktime styrer når transaksjonen blir gyldig. Serialisering bruker little-endian-orden for de fleste heltall. Parsere bruker byte sekvensielt og delegerer til spesialiserte klasser for innganger, utganger og skript.


### Avgifter, endring og formbarhet


Avgifter er implisitte:

avgift = sum(inngangsverdier) - sum(utgangsverdier).

Enhver verdi som ikke er tilordnet, blir gebyret, noe som gjør det viktig å konstruere korrekt endringsutdata. Før SegWit tillot signaturer manipulerbarhet - ved å endre S til N-S produserte man en ny, gyldig transaksjon med en annen ID. Bitcoin håndhever nå en regel om lav S, og SegWit isolerer signaturer fra txid-beregningen, noe som gjør ID-er stabile og muliggjør andrelagsprotokoller som Lightning.


## Bitcoin Skript- og transaksjonsvalidering

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>


![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


Bitcoin Script er et lite, stakkbasert smartkontraktspråk som definerer hvordan mynter kan brukes. Hver utgang har en scriptPubKey (låseskript), og hver inngang har en scriptSig (opplåsingsskript). Sammen danner de et program som må evaluere til "true" for at bruken skal være gyldig. Script er med vilje ikke Turing-komplett, slik at alle kjøringsveier er forutsigbare og enkle å validere på tvers av nettverket.


### Skriptoperasjoner og utførelsesmodell


Et skript er en sekvens av dataelementer og opkoder. Datapushes (signaturer, offentlige nøkler, hasher) plasseres i stakken, mens opkoder som begynner med `OP_`, transformerer stakken. Etter kjøring må det øverste stabelelementet være forskjellig fra null for å lykkes. Eksempler på dette: `OP_DUP` dupliserer det øverste elementet, `OP_HASH160` bruker SHA256 og deretter RIPEMD160, og `OP_CHECKSIG` verifiserer en signatur mot transaksjonens sighash og en offentlig nøkkel, og skyver 1 for gyldig, 0 for ugyldig. Parsing-reglene skiller mellom rådata (lengdeprefiks) og opkoder (slått opp etter byteverdi), og en liten virtuell maskin utfører dem deterministisk på hver node.


### P2PK og P2PKH: Kjernebetalingsmønstre


Det tidligste mønsteret, Pay-to-Public-Key (P2PK), låste mynter direkte til en fullstendig offentlig nøkkel: scriptPubKey er `<pubkey> OP_CHECKSIG`, og scriptSig er bare en signatur. Det er enkelt, men plassbesparende, og avslører den offentlige nøkkelen før myntene er brukt.


#### P2PKH og adresser

Pay-to-Public-Key-Hash (P2PKH) forbedrer dette ved å låse til en 20-byte hash av den offentlige nøkkelen. ScriptPubKey er `OP_DUP OP_HASH160 <pubkey_hash> OP_EQUALVERIFY OP_CHECKSIG`, og scriptSig gir `<signature> <pubkey>`. Kjøringen kontrollerer at den oppgitte offentlige nøkkelen hashes til den bekreftede verdien, og verifiserer deretter signaturen. Dette skjuler den offentlige nøkkelen til brukstiden, reduserer størrelsen og samsvarer med det velkjente "1..." mainnet-adresseformatet.


### Transaksjonsvalidering og signaturhashing


En node som validerer en transaksjon, må sikre:

1) Hver inngang refererer til en eksisterende, ubrukt utgang.

2) Total inngangsverdi ≥ total utgangsverdi (differansen er avgiften).

3) Hver scriptSig låser opp sin refererte scriptPubKey på riktig måte.


Signaturverifisering krever at man konstruerer den nøyaktige meldingen som ble signert, kalt sighash. For eldre ECDSA tømmer valideringen alle scriptSigs, erstatter scriptSig for den aktuelle inndataen med den tilsvarende scriptPubKey, legger til en 4-bytes hashtype (vanligvis `SIGHASH_ALL`) og dobbel-hashes resultatet. Den 256-biters verdien er det `OP_CHECKSIG` bruker. Alternative hashtyper (f.eks. `SINGLE`, `NONE`, med eller uten `ANYONECANPAY`) endrer hvilke deler av transaksjonen som er forpliktet, noe som muliggjør nisje-brukstilfeller som samarbeidsfinansiering eller delvis spesifiserte transaksjoner, men de brukes sjelden i praksis.


#### Kvadratisk hashing og SegWit

Fordi hver inndata i en eldre transaksjon krever sin egen sukkberegning over en struktur som omfatter alle inndataene, kan valideringstiden vokse kvadratisk med antallet inndata. Store transaksjoner med flere inndata forårsaket tidligere merkbare valideringsforsinkelser. SegWit redesignet sighash-beregningen slik at delte deler bufres og kompleksiteten reduseres til lineær tid, noe som forbedrer skalerbarheten og gjør tjenestenektangrep vanskeligere.


### Skriptgåter og leksjoner i sikkerhet


Skript kan uttrykke langt mer enn bare "en signatur låser opp disse myntene" Script-gåter demonstrerer dette ved å kode vilkårlige forhold - matteproblemer, hash preimage-utfordringer eller til og med kollisjonspremier - der alle som oppgir de riktige dataene, kan bruke myntene. Utganger som kun baserer seg på offentlige data (ingen signaturer), er imidlertid sårbare for "miner front-running": Når en gyldig løsning dukker opp i mempoolen, kan enhver miner kopiere den og omdirigere utbetalingen til seg selv.


Den praktiske lærdommen er at kontrakter i den virkelige verden nesten alltid inkluderer signaturkontroller, selv når de inneholder mer kompleks logikk som multisig, tidslås eller hashlock. Signaturer binder løsningen til en spesifikk part, bevarer insentiver og hindrer andre i å stjele utbetalingen. Å forstå Skripts stakemodell, standardmønstre og subtile fallgruver er avgjørende for å utforme sikre Bitcoin-smartkontrakter og for å kunne resonnere om hvordan transaksjoner faktisk valideres i nettverket.


## Transaksjonskonstruksjon og betal-til-skript Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>


![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


### Bygning Bitcoin Transaksjoner og P2SH


Bitcoin-transaksjonskonstruksjon bygger bro mellom teoretisk protokollkunnskap og praktisk implementering. En transaksjon velger UTXO-er som skal brukes, bygger utganger med låseskript, oppretter signaturer for hver inngang og serialiserer alt i nøyaktig det formatet nodene forventer. Prosessen krever forståelse av generering av sukk, skriptoppførsel og korrekt avgifts- og endringshåndtering.


### Grunnleggende transaksjonskonstruksjon


Hver transaksjonsinngang refererer til en tidligere utgang med txid og indeks. Utdataene angir beløp i satoshier og låseskript. Differansen mellom totale inndata og totale utdata er avgiften. For å signere en input serialiseres en modifisert versjon av transaksjonen, dens sighash beregnes, og den private nøkkelen signerer den. Den resulterende signaturen og den offentlige nøkkelen danner ScriptSig. Når alle inndata er signert, kan den rå transaksjonen sendes ut til nettverket.


### Transaksjoner med flere signaturer


Bare multisig bruker `OP_CHECKMULTISIG` for å kreve m-av-n-signaturer. På grunn av en tidlig off-by-one-feil bruker OP_CHECKMULTISIG et ekstra stabelelement, noe som krever en innledende `OP_0` i ScriptSig. Bare multisig er funksjonelt, men ineffektivt: Alle offentlige nøkler vises som on-chain, noe som gjør scriptPubKeys store, dyre og vanskelige å kode som adresser. Disse begrensningene motiverte innføringen av pay-to-script-hash.


#### P2SH Arkitektur

P2SH skjuler komplekse skript bak en 20-byte HASH160. ScriptPubKey er fast: `OP_HASH160 <20-byte hash> OP_EQUAL`. Det underliggende innløsningsskriptet - som inneholder multisig, tidssperrer eller andre betingelser - avsløres og utføres bare når det brukes. Avsenderen ser bare hashen, mens mottakeren administrerer innløsningsskriptet privat. Dette designet reduserer on-chain-størrelsen, forbedrer personvernet og muliggjør komplekse kontrakter uten å belaste avsendere.


### P2SH Utgifter og implementering


For å bruke en P2SH-utgang må ScriptSig inneholde de nødvendige opplåsingsdataene *pluss* selve innløsningsskriptet. Validering skjer i to trinn:

1) HASH160(redeem_script) må samsvare med scriptPubKey-hashverdien.

2) Etter verifisering kjøres redeem-skriptet med de oppgitte dataene.


Når det genereres signaturer for en P2SH-inndata, bruker sighash-prosessen redeem-skriptet i stedet for scriptPubKey. Hver underskriver må ha det fullstendige redeem-skriptet for å generate gyldige signaturer. P2SH-adresser bruker versjonsbyte 0x05 på mainnet ("3..."-adresser) og 0xC4 på testnet ("2..."-adresser).


#### Praktiske sikkerhetsoverveielser


Hvis du mister et innløsningsskript, mister du penger: For å bruke penger kreves både de private nøklene og selve innløsningsskriptet. Multisig-deltakere må verifisere at de offentlige nøklene deres er korrekt inkludert før de godtar innskudd. P2SH støtter avanserte konstruksjoner som multisig, timelocks og hashlocks, men feil i skriptlogikken kan låse midler permanent, så det er viktig å teste på testnet.


P2SH forbedrer personvernet ved å skjule utgiftsbetingelsene frem til den første utgiften, men når innløsningsskriptet vises on-chain, blir det permanent synlig. Til tross for dette gjorde fordelene med redusert størrelse, bakoverkompatibilitet og fleksibel kontraktsstøtte P2SH til en viktig milepæl, noe som påvirket senere oppgraderinger som SegWit og Taproot.


# Bitcoin-nettverkets indre funksjoner

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Bitcoin-blokker og Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>


![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


Bitcoin-blokker grupperer transaksjoner og sikrer dem ved hjelp av proof of work. Hver blokk inneholder en header på 80 byte samt en liste over transaksjoner. Til tross for at det koster mye energi å produsere en gyldig blokk, er det billig å verifisere den: Lagring av alle ~900 000 overskrifter krever bare ~72 MB, noe som gjør at selv små enheter kan verifisere kjedens proof of work på en effektiv måte.


### Coinbase-transaksjoner og Block Rewards


Hver blokk begynner med nøyaktig én Coinbase-transaksjon - den eneste måten nye bitcoin kommer i omløp på. Den har en nullstilt prev-tx-hash og en indeks på 0xffffffffffff, som identifiserer den unikt. Tilskuddet startet på 50 BTC og halveres hver 210 000. blokk (50, 25, 12,5, 6,25, 3,125, ...). Gruvearbeidere inkluderer også transaksjonsgebyrer. Fordi noncen på 4 byte er for liten for moderne ASIC-er, modifiserer utvinnere data i Coinbase-transaksjonen for å endre Merkle-roten og skape ekstra søkeplass. BIP34 krever at blokkhøyden legges inn i Coinbase scriptSig for å sikre at hver Coinbase txid er unik.


### Blokkhodefelt og Soft Fork-signalering


Toppteksten på 80 byte inneholder:


- versjon (4 byte)
- hash av forrige blokk (32 byte)
- Merkle-rot (32 byte)
- tidsstempel (4 byte)
- bits (vanskelighetsmål, 4 byte)
- nonce (4 byte)


Versjonsnumre utviklet seg til et bitfelt-signalsystem via BIP9, slik at utvinnere kan koordinere soft-fork-beredskapen. Tidsstempelet er en 32-biters Unix-tidsverdi og må oppdateres rundt år 2106.


#### Bits-felt og mål

Bits-feltet koder målet i kompakt form: mål = koeffisient × 256^(eksponent-3). Gyldige blokkhashes må være numerisk under dette målet. Fordi hasher tolkes som little-endian heltall, vises gyldige hasher ofte med mange etterfølgende nuller når de vises i hex.


### Vanskelighetsgrad, validering og justeringer


Vanskelighetsgrad er definert som lowest_target / current_target, og uttrykker hvor mye vanskeligere mining er i dag sammenlignet med den lettest mulige vanskelighetsgraden. Validering krever bare at man sammenligner hashen i overskriften med målet - ekstremt billig i forhold til mining.


Hver 2016-blokk justerer Bitcoin vanskelighetsgraden for å oppnå blokkintervaller på ~10 minutter. Justeringen sammenligner den faktiske tiden for de foregående 2016-blokkene med de forventede to ukene. Grensene begrenser justeringene til innenfor en faktor på fire. Store hendelser i den virkelige verden - som Kinas mining-forbud - demonstrerte denne mekanismens motstandsdyktighet da hashraten falt kraftig og vanskelighetsgraden ble justert nedover for å kompensere.


### Blokktilskudd og totalt Supply


Subsidien i høyden h beregnes som: subsidy = 5_000_000_000 >> (h // 210_000). Dette gir halveringsplanen som konvergerer mot et totalt tilbud på ~21 millioner BTC. Summen av den geometriske serien (50 + 25 + 12,5 + ...) × 210 000 forklarer taket. Utvinnere kan kreve mindre enn den tillatte subsidien, men aldri mer, ellers blir blokken ugyldig. Etter hvert som subsidiene krymper over flere halveringer, blir transaksjonsgebyrene en stadig viktigere del av utvinnernes inntekter og den langsiktige nettverkssikkerheten.


## Nettverkskommunikasjon og Merkle Trees

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>


![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


### Bitcoin Nettverksarkitektur


Bitcoins peer-to-peer-nettverk fungerer som et desentralisert sladdersystem der noder videresender transaksjoner og blokker uten å stole på hverandre. Nye noder starter opp ved å kontakte hardkodede DNS-frø som vedlikeholdes av kjerneutviklerne. Disse DNS-frøene returnerer IP-adresser til aktive jevnaldrende, slik at nodene kan oppdage nettverket og deretter be om flere jevnaldrende via getaddr. Nettverket er med vilje ikke konsensuskritisk, så implementeringen kan variere så lenge konsensusreglene forblir uendret.


### Meldingsstruktur og håndtrykk


Alle Bitcoin P2P-meldinger bruker en fast konvolutt: en magisk verdi på 4 byte (F9BEB4D9 for mainnet), en ASCII-kommando på 12 byte, en little-endian nyttelastlengde på 4 byte, en kontrollsum på 4 byte (de første 4 byte av hash256) og nyttelasten. Vanlige kommandoer inkluderer versjon, verack, inv, getdata, tx, block, getheaders, headers, ping og pong.


Håndtrykket begynner når en tilkoblet node sender en versjonsmelding. Mottakeren svarer med verack og sin egen versjon. Når begge sider har utvekslet disse to meldingene, er forbindelsen aktiv, og nodene kan begynne å videresende beholdninger og data.


### Merkle trær og Merkle røtter


Bitcoin lagrer en enkelt Merkle-rot på 32 byte i hvert blokkhode som en forpliktelse til alle transaksjonene i blokken. Transaksjonene hashes (hash256), pares, sammenkjedes og hashes gjentatte ganger til det gjenstår én hash. Når et nivå har et oddetall, dupliseres den siste hashen. Internt er hashene big-endian, mens serialiserte blokkdata bruker little-endian, noe som krever reversering før og etter trekonstruksjon.


#### Merkle Proofs og SPV

Merkle-bevis gjør det mulig å verifisere at en transaksjon er inkludert i en blokk uten å laste ned hele blokken. Beviset består av søskenhashes langs stien til roten. Lette SPV-klienter lagrer bare blokkhoder og ber om disse bevisene fra fulle noder. Fordi et Merkle-tre vokser logaritmisk, krever det bare noen få hundre byte å bevise inkludering i en blokk med tusenvis av transaksjoner.


Taproot utvider dette konseptet ved å overføre utgiftsbetingelser til et Merklized Script Tree (MAST), slik at bare den utførte grenen avsløres sammen med et Merkle-bevis. Dette forbedrer både effektiviteten og personvernet.


### Nettverksdrift og blokksynkronisering


Noder bruker getdata til å be om transaksjoner eller blokker, og spesifiserer en type-ID (1=tx, 2=blokk, 3=filtrert blokk, 4=kompakt blokk) pluss en 32-byte identifikator. For kjedesynkronisering sender noder getheaders med en startblokkhash, og mottar opptil 2000 headere som svar. Hver returnerte header består av 80 byte etterfulgt av et dummy-transaksjonstall på null.


Full verifisering av mottatte blokker krever to kontroller:

1. Blokkens hash må ligge under målet som er kodet i bits-feltet.

2. Merkle-roten som beregnes ut fra alle transaksjoner (med riktig endianness-håndtering), må samsvare med headerens rot.


Bare hvis begge betingelsene er oppfylt, godtar en node blokken, noe som gjenspeiler Bitcoins "ikke stol på, verifiser"-prinsipp.


## Avansert nodekommunikasjon og segregert vitne

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>


![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)


Denne økten forener avansert P2P-nettverk med Segregated Witness, og viser hvordan moderne Bitcoin-programvare samhandler direkte med noder samtidig som den bruker SegWit-bevisste transaksjonsstrukturer. Utviklere lærer å hente blokker, skanne etter relevante transaksjoner og konstruere transaksjoner kun ved hjelp av rå nettverkskommunikasjon - ingen blokkutforskere er nødvendig.


### Blokkbasert transaksjonsinnhenting og personvern


Lommebøker må oppdage innkommende betalinger ved å skanne blokker for utganger som samsvarer med scriptPubKey. Å hente hele blokker beskytter personvernet bedre enn å be om enkelttransaksjoner, som lekker sterke signaler om brukeraktivitet. Selv blokkforespørsler kan lekke informasjon om kjeder med lavt volum, noe som gjør kompakte blokkfiltre (BIP158) avgjørende for personvernbevarende lettklienter. Filtre kan gi falske positiver, men aldri falske negativer, slik at klienter bare kan laste ned potensielt relevante blokker uten å avsløre spesifikke adresser.


### Trustless Nettverksinteraksjon


Arbeidsflyten `get_block` demonstrerer riktig nettverksbruk: send getdata, motta en blokk, og verifiser deretter Merkle-roten og proof of work uavhengig av hverandre. En blokk godtas bare hvis den mottatte header-hashingen samsvarer med den forespurte hashen og den beregnede Merkle-roten samsvarer med headeren. Dette er et uttrykk for "ikke stol på, verifiser", som sikrer at selv ondsinnede motparter ikke kan lure noder til å godta endrede data.


#### Hente transaksjoner fra blokker

Transaksjonene i en blokk kan skannes etter matchende scriptPubKeys ved hjelp av enkel iterasjon. Produksjonslommebøker utfører dette kontinuerlig etter hvert som nye blokker ankommer, og beviser eierskap av utganger utelukkende gjennom kryptografisk validering i stedet for å stole på tredjeparts API-er.


### SegWit Målsettinger og design


Segregerte vitner (SegWit) løste problemet med transaksjonsfeil ved å fjerne signaturdata fra beregningen av txid. Dette muliggjorde pålitelige forhåndssignerte transaksjonskjeder og gjorde Lightning Network praktisk. SegWit økte også blokkkapasiteten ved hjelp av "blokkvekt": gamle noder ser fortsatt blokker på ≤1 MB, mens oppgraderte noder validerer opptil 4 MB inkludert vitnedata. Versjonsbaserte vitneprogrammer (v0-v1 så langt) skaper en strukturert oppgraderingsvei for fremtidige skripttyper.


#### P2WPKH (opprinnelig SegWit)


P2WPKH erstatter den gamle P2PKH-strukturen med et skript på 22 byte: OP_0 + push20 + hash160(pubkey). Utgifter flytter signaturen og pubkey til et separat vitnefelt.


- Noder fra før SegWit: se "hvem-som-helst-kan-spende", og behandle det som gyldig.
- Post-SegWit-noder: gjenkjenner OP_0 + 20-byte hash og validerer ved hjelp av vitnedata.


Denne separasjonen løser problemet med manipulerbarhet og reduserer avgiftene. Vitnet bruker en varint count etterfulgt av signaturen og pubkey.


#### P2SH-P2WPKH (bakoverkompatibel SegWit)


For at gamle lommebøker skal kunne sende til SegWit-adresser, kan P2WPKH-skript pakkes inn i P2SH.


- scriptPubKey: standard P2SH hash160(redeemScript)
- scriptSig: innløsningsskriptet (P2WPKH-programmet)
- vitne: signatur + pubkey


Valideringslag:

1. Pre-BIP16-noder godtar redeemScript som gyldig.

2. Post-BIP16-noder evaluerer den, og etterlater OP_0 + hash på stakken.

3. SegWit-noder utfører full vitnevalidering.


#### P2WSH for komplekse skript


P2WSH generaliserer SegWit for multisig og avanserte skript ved å bruke SHA256(skript) i stedet for hash160. En typisk 2-av-3 multisig-vitnestabel:


- tomt element (CHECKMULTISIG-feil)
- sig1
- sig2
- vitne-skript (multisig-skriptet)


SegWit-noder verifiserer at SHA256(witnessScript) samsvarer med scriptPubKey-hashingen, og kjører den deretter. Ved å bruke SHA256 og en 32-byte hash kan P2WSH skilles fra P2WPKH, noe som styrker sikkerheten.


#### P2SH-P2WSH (maksimal kompatibilitet)


Komplekse SegWit-skript kan også pakkes inn i P2SH:


- scriptSig: redeemScript (OP_0 + 32-byte hash)
- vitne: signaturer + vitneScript


Valideringen går gjennom tre generasjoner med regler, akkurat som med P2SH-P2WPKH. Denne innpakningen var avgjørende for tidlige Lightning-distribusjoner som trengte multisig uten formbarhet. Selv om opprinnelig P2WSH foretrekkes i dag, sikrer den innpakkede formen kompatibilitet på tvers av eldre wallet-systemer.


### SegWits innvirkning


SegWit levert:


- stabile transaksjons-ID-er
- lavere gebyrer via rabatterte vitnedata
- høyere blokkgjennomstrømning via blokkvekt
- kompatibilitet for gamle noder
- en ren oppgraderingsvei for Taproot og fremtidige utvidelser


Sammen med tillitsløs nettverksinteraksjon utgjør disse verktøyene ryggraden i moderne Bitcoin-utvikling.



# Siste del


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Anmeldelser og rangeringer


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>

## Avsluttende eksamen


<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>



<isCourseExam>true</isCourseExam>

## Konklusjon



<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>


<isCourseConclusion>true</isCourseConclusion>