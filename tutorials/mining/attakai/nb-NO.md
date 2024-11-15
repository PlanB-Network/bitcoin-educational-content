---
name: Attakaï

description: transformerer en S9 til et hjemmevarmesystem
---

![cover](assets/cover.webp)

# Attakai - gjør hjemmemining mulig og tilgjengelig!

Initiativet "Attakaï" utforsker Bitcoin-mining ved bruk av generert varme. Guiden tilbyr løsninger for å gjøre minere egnet for bruk som radiatorer i hjem, noe som gir mer komfort og energisparing. Bitcoin justerer automatisk miningvanskeligheten og belønner minerne for deres arbeid. Imidlertid kan konsentrasjonen av hashrate utgjøre risikoer for nettverksnøytraliteten. "Attakaï" gir en praktisk guide for økonomisk retrofitting av minere, som lar deltakerne redusere sine strømregninger og bli belønnet med sats uten KYC.

## Introduksjon

"Attakaï", som betyr "ideell temperatur" på japansk, er navnet på initiativet rettet mot å oppdage bitcoin-mining gjennom gjenbruk av varme lansert av @ajelexBTC og @BlobOnChain med Découvre Bitcoin. Denne ASIC-retrofitting-guiden vil tjene som et grunnlag for å lære mer om mining, dens drift, nylig historie og den underliggende økonomien.

### Hvorfor gjenbruke varmen fra en ASIC?

Det er viktig å forstå forholdet mellom energi og varmeproduksjon i et elektrisk system.

For en investering av 1 kW elektrisk energi, produserer en elektrisk radiator 1 kW varme, verken mer eller mindre. Nye radiatorer er ikke mer effektive enn tradisjonelle radiatorer. Deres fordel ligger i deres evne til å distribuere varmen kontinuerlig og jevnt i et rom, noe som gir mer komfort sammenlignet med tradisjonelle radiatorer som veksler mellom høy varmeeffekt og ingen oppvarming, og dermed genererer regelmessige temperaturvariasjoner og ubehag.

En datamaskin, eller mer bredt et elektronisk kort, forbruker ikke energi for å utføre beregninger; den trenger bare energi til å strømme gjennom komponentene for å fungere. Energiforbruket skyldes den elektriske motstanden i komponentene, som produserer tap og dermed genererer varme, som er kjent som Joule-effekten.
Noen selskaper har kommet med ideen om å samle behovet for databehandlingskraft og oppvarmingsbehov gjennom radiator/servere. Ideen er å distribuere et selskaps servere i små enheter som kunne plasseres i hjem eller kontorer. Imidlertid møter denne ideen flere problemer. Behovet for servere er ikke relatert til behovet for oppvarming, og selskaper kan ikke bruke databehandlingskapasiteten til serverne sine fleksibelt. Det er også grenser for båndbredden som enkeltpersoner kan besitte. Alle disse begrensningene hindrer selskapet i å gjøre disse kostbare installasjonene lønnsomme eller tilby en stabil online serverløsning uten datasentre som kan ta over når oppvarming ikke er nødvendig.

> "Varmen fra datamaskinen din er ikke bortkastet hvis du trenger å varme opp hjemmet ditt. Hvis du bruker elektrisk oppvarming der du bor, så er varmen fra datamaskinen din ikke bortkastet. Det koster det samme om du genererer denne varmen med datamaskinen din. Hvis du har et billigere oppvarmingssystem enn elektrisk, så er avfallet bare i kostnadsforskjellen. Hvis det er sommer og du bruker klimaanlegg, så er det dobbelt.
> Bitcoin-mining bør finne sted der det er billigere. Kanskje det vil være der klimaet er kaldt og hvor oppvarmingen er elektrisk, der mining kunne bli gratis."
> Satoshi Nakamoto - 8. august 2010
Bitcoin og dets proof of work skiller seg ut fordi de automatisk justerer vanskelighetsgraden for mining basert på mengden databehandling utført av hele nettverket, denne mengden kalles hashrate og uttrykkes i hasher per sekund. I dag er den anslått til 280 Exahash per sekund, eller 280 milliarder milliarder hasher per sekund. Denne hashraten representerer arbeid og derfor en mengde energi brukt. Jo høyere hashrate, desto høyere øker vanskelighetsgraden, og omvendt. Således kan en Bitcoin-miner aktiveres eller deaktiveres når som helst uten noen innvirkning på nettverket, i motsetning til radiator/servere som må forbli stabile for å tilby tjenesten sin. Mineren belønnes for arbeidet som er gjort i forhold til andres arbeid, uansett hvor liten denne deltakelsen kan være.
Oppsummert produserer både en elektrisk radiator og en Bitcoin-miner 1 kW varme for 1 kW elektrisitet forbrukt. Men, mineren mottar også bitcoins som belønning. Uavhengig av prisen på elektrisitet, prisen på bitcoin, eller konkurransen om miningaktivitet på Bitcoin-nettverket, er det økonomisk mer fordelaktig å varme opp med en miner enn en elektrisk radiator.

![Videopresentasjon](https://youtu.be/gKoh44UCSnE)

### Den tilføyde verdien for Bitcoin

Vi vil ikke gå inn på detaljene i miningoperasjonen her (ressurser tilgjengelig på akademiet om nødvendig). Det som er viktig å forstå, er hvordan mining bidrar til desentraliseringen av Bitcoin. Flere eksisterende teknologier har blitt genialt kombinert for å bringe Nakamotos konsensus til liv. Denne konsensusen økonomisk belønner ærlige aktører for deres deltakelse i driften av Bitcoin-nettverket, samtidig som den avskrekker uærlige aktører. Dette er et av nøkkelpunktene som lar nettverket eksistere bærekraftig.

Ærlige aktører, de som miner i henhold til reglene, konkurrerer alle med hverandre for å oppnå den største mulige andelen av belønningen for å produsere nye blokker. Denne økonomiske insentiven fører naturlig til en form for sentralisering ettersom selskaper velger å spesialisere seg på denne lukrative aktiviteten ved å redusere kostnadene gjennom stordriftsfordeler. Disse industrielle aktørene har en fordelaktig posisjon for kjøp og vedlikehold av maskiner, samt forhandling om strømpriser i bulk.

> "I begynnelsen ville de fleste brukere kjøre nettverksnoder, men etter hvert som nettverket vokste utover et visst punkt, ville det bli overlatt mer og mer til spesialister med serverfarmer av spesialisert maskinvare. En serverfarm ville bare trenge å kjøre en node på nettverket og resten av LAN kobler seg med den ene noden." - Satoshi Nakamoto - 2. november 2008

Visse enheter holder en betydelig prosentandel av den totale hashraten i store miningfarmer. Vi kan observere den nylige kuldebølgen i USA hvor en betydelig del av hashraten ble tatt offline for å omdirigere energi til husholdninger med et eksepsjonelt behov for elektrisitet. I flere dager ble minerne økonomisk incentivert til å slå av gårdene sine, og dermed kan vi se denne eksepsjonelle værsituasjonen på Bitcoin hashrate-kurven.

Dette problemet kan bli problematisk og utgjøre en betydelig risiko for nettverkets nøytralitet. En aktør som besitter mer enn 51% av hashraten, kunne lettere sensurere transaksjoner om de ønsket. Derfor er det viktig å distribuere hashraten blant flere aktører i stedet for sentraliserte enheter som kunne bli lettere beslaglagt av en regjering, for eksempel.

**Hvis minerne er spredt over tusenvis, eller til og med millioner, av husholdninger rundt om i verden, blir det veldig komplisert for en stat å ta kontroll over dem.**
På fabrikken er en miner ikke egnet til å brukes som en radiator i en bolig, på grunn av to hovedproblemer: overdreven støy og mangel på justering. Disse problemene kan imidlertid enkelt løses gjennom enkle modifikasjoner gjort på maskinvaren og programvaren, noe som tillater en mye stillere miner som kan konfigureres og automatiseres som moderne elektriske varmeovner.
**Attakaï er et utdanningsinitiativ som lærer deg hvordan du kan oppgradere Antminer S9 på den mest kostnadseffektive måten mulig.**

Dette er en utmerket mulighet til å lære ved å praktisere. I tillegg til å redusere strømregningen din, blir du belønnet for din deltakelse med gratis KYC sats.

## Kapittel 1: Kjøpsguide for en Brukt ASIC

I denne delen vil vi diskutere beste praksiser for å kjøpe en brukt Bitmain Antminer S9, maskinen som dette radiatormodifiseringstutorialet vil være basert på. Denne guiden gjelder også for andre ASIC-modeller ettersom det er en generell kjøpsguide for brukt gruveutstyr.

Antminer S9 er en enhet tilbudt av Bitmain siden mai 2016. Den forbruker 1323W med elektrisitet og produserer 13,5 TH/s. Selv om den anses som gammel, forblir den et utmerket alternativ for å starte gruvedrift. Siden den har blitt produsert i store mengder, er det enkelt å finne reservedeler rikelig i mange regioner av verden. Den kan generelt kjøpes peer-to-peer på nettsteder som Ebay eller LeBonCoin, ettersom profesjonelle forhandlere ikke lenger tilbyr den på grunn av dens lavere konkurranseevne sammenlignet med nyere maskiner. Den er mindre effektiv enn ASIC-er som Antminer S19, introdusert siden mars 2020, men dette gjør den til en rimelig brukt maskinvare og mer egnet for modifikasjonene vi vil gjøre.

Antminer S9 kommer i flere varianter (i, j) som bringer mindre modifikasjoner til maskinvaren fra første generasjon. Vi tror ikke at dette bør påvirke kjøpsbeslutningen din, og denne guiden vil fungere for alle disse variantene.

Prisen på ASIC-er varierer avhengig av mange faktorer som prisen på bitcoin, nettverksvanskeligheter, maskineffektivitet og strømkostnad. Derfor er det vanskelig å gi et nøyaktig estimat for kjøp av en brukt maskin. I februar 2023 varierer den forventede prisen i Frankrike generelt mellom €100 og €200, men disse prisene kan endre seg raskt.

![bilde](assets/guide-achat/1.webp)

Antminer S9 består av følgende deler:

- 3 hashboards hvor brikkene som produserer hashkraften er plassert

![bilde](assets/guide-achat/2.webp)

- Et kontrollkort som inkluderer en spor for et SD-kort, en Ethernet-port og kontakter for hashboards og vifter. Dette er hjernen til din ASIC.
  ![bilde](assets/guide-achat/3.webp)

- 3 datakabler som kobler hashboards til kontrollkortet.

![bilde](assets/guide-achat/4.webp)

- Strømforsyningen som opererer på 220V og kan plugges inn som en vanlig husholdningsapparat.

![bilde](assets/guide-achat/5.webp)

- 2 120mm vifter.

![bilde](assets/guide-achat/6.webp)

- En hann C13-kabel.

![bilde](assets/guide-achat/7.webp)
Når du kjøper en brukt maskin, er det viktig å sjekke at alle deler er inkludert og fungerer. Under utvekslingen bør du be selgeren om å slå på maskinen for å verifisere at den fungerer som den skal. Det er viktig å sjekke at enheten slår seg på korrekt, og deretter sjekke internettforbindelsen ved å koble til en Ethernet-kabel og få tilgang til Bitmain-tilkoblingsgrensesnittet via en nettleser på samme lokale nettverk. Du kan finne denne IP-adressen ved å koble til grensesnittet på din internett-router og se etter tilkoblede enheter. Denne adressen bør ha følgende format: 192.168.x.x
![bilde](assets/guide-achat/8.webp)

Sjekk også at standard påloggingsinformasjon fungerer (brukernavn: root, passord: root). Hvis standard påloggingsinformasjon ikke fungerer, må du utføre en tilbakestilling av maskinen.

![bilde](assets/guide-achat/9.webp)

Når du er tilkoblet, bør du kunne se statusen for hver hashboard på dashbordet. Hvis miner er tilkoblet en pool, bør du se at alle hashboards fungerer. Det er viktig å merke seg at minere lager mye støy, noe som er normalt. Sørg også for at viftene fungerer som de skal.

Du kan deretter fjerne den forrige eierens miningpool for å sette opp din egen senere. Om ønskelig, kan du også inspisere hashboards ved å demontere maskinen. Dette steget er imidlertid mer komplekst og krever mer tid og visse verktøy. Hvis du ønsker å fortsette med denne demonteringen, kan du referere til neste del av denne veiledningen som detaljerer hvordan du gjør det. Det er viktig å merke seg at minere samler mye støv og krever regelmessig vedlikehold. Du kan observere denne støvakkumuleringen og vedlikeholdskvaliteten ved å demontere maskinen.
Etter å ha gjennomgått alle disse punktene, kan du kjøpe maskinen din med høy grad av tillit. Hvis du er i tvil, ta kontakt med fellesskapet, og hvis du trenger utstyr for å fullføre denne veiledningen, er du velkommen til å sende oss en melding.
For å oppsummere denne veiledningen i én setning: **"Ikke stol, verifiser."**

## Kapittel 2: Kjøpsguide for Modifikasjonsdeler

![bilde](assets/piece/1.webp)

### Hvordan forvandle din Antminer S9 til en stille og tilkoblet varmeovn?

Hvis du eier en Antminer S9, vet du sannsynligvis hvor høy og klumpete den kan være. Det er imidlertid mulig å forvandle den til en stille og tilkoblet varmeovn ved å følge noen enkle trinn. I denne artikkelen vil vi presentere det nødvendige utstyret for å gjøre modifikasjonene, mens en senere artikkel vil forklare i detalj trinnene for å gjøre disse endringene.

### 1. Bytt ut viftene

De originale viftene til Antminer S9 er for høye til å bruke den som en varmeovn. Løsningen er å erstatte dem med stillere vifter. Teamet vårt har testet flere modeller fra Noctua-merket og valgt Noctua NF-A14 iPPC-2000 PWM som det beste kompromisset. Sørg for å velge 12V-versjonen av viftene. Denne 140mm viften kan produsere opptil 1300W varme samtidig som den opprettholder et teoretisk støynivå på 31 dB. For å montere disse 140mm viftene, trenger du en 140mm til 120mm adapter, som du kan finne i DécouvreBitcoin-butikken. Vi vil også legge til 140mm beskyttelsesgriller.

![bilde](assets/piece/1.webp)
![bilde](assets/piece/2.webp)
![bilde](assets/piece/3.webp)
Strømforsyningens vifte er også ganske støyende og trenger å bli byttet ut. Vi anbefaler Noctua NF-A6x25 PWM. Merk at kontaktene til Noctua-viftene ikke er de samme som de originale, så du vil trenge en kontaktadapter for å koble dem til. To burde være nok. Igjen, sørg for å velge 12V-versjonen av viften.
![bilde](assets/piece/4.webp)
![bilde](assets/piece/5.webp)

### 2. Legg til en WIFI/Ethernet-bro

I stedet for å bruke en Ethernet-kabel, kan du koble din Antminer til WIFI ved å legge til en WIFI/Ethernet-bro. Vi har valgt vonets vap11g-300 fordi den enkelt lar deg hente WIFI-signalet fra din Internett-boks og overføre det til din Antminer via Ethernet uten å skape et subnett. Hvis du har elektriske ferdigheter, kan du strømforsyne den direkte med Antminerens strømforsyning uten behov for å legge til en USB-lader. For dette, vil du trenge en kvinnelig 5.5mmx2.1mm jack.

![bilde](assets/piece/6.webp)
![bilde](assets/piece/7.webp)

### 3. Valgfritt: Legg til en smart plugg

Hvis du ønsker å slå på/av din Antminer fra smarttelefonen din og overvåke strømforbruket, kan du legge til en smart plugg. Vi testet ANTELA-pluggen i 16A-versjonen, kompatibel med smartlife-applikasjonen. Denne smarte pluggen lar deg sjekke daglig og månedlig strømforbruk og kobles direkte til din Internett-boks via WIFI.
![bilde](assets/piece/8.webp)

> Liste over utstyr og lenker
>
> - 2X 3D adapterstykke 140mm til 120mm
> - 2X NF-A14 iPPC-2000 PWM [lenke](https://www.amazon.fr/Noctua-nf-polarized-A14-industrialppc-PWM-2000/dp/B00KESSUDW/ref=sr_1_2?__mk_fr_FR=ÅMÅŽÕÑ&crid=JCNLC31F3ECM&keywords=NF-A14+iPPC-2000+PWM&qid=1676819936&sprefix=nf-a14+ippc-2000+pwm%2Caps%2C114&sr=8-2)
> - 2X 140mm viftegriller [lenke](https://www.amazon.fr/dp/B06XD4FTSQ?psc=1&ref=ppx_yo2ov_dt_b_product_details)
> - Noctua NF-A6x25 PWM [lenke](https://www.amazon.fr/Noctua-nf-a6-25-PWM-Ventilateur-Marron/dp/B00VXTANZ4/ref=sr_1_1_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=3T313ABZA5EDE&keywords=Noctua+NF-A6x25+PWM&qid=1676819329&sprefix=noctua+nf-a6x25+pwm%2Caps%2C71&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1&smid=A38F5RZ72I2JQ)
> - Elektrikerens sukker 2.5mm2 [link](https://www.amazon.fr/Legrand-LEG98433-Borne-raccordement-Nylbloc/dp/B00BBHXLYS/ref=sr_1_3?__mk_fr_FR=ÅMÅŽÕÑ&crid=25IRJD7A0YN2A&keywords=sucre%2Belectrique%2B2mm2&qid=1676820815&sprefix=sucre%2Belectrique%2B2mm2%2Caps%2C84&sr=8-3&th=1)
> - Vonets VAP11G-300 https://www.amazon.fr/Vonets-VAP11G-300-Bridge-convertit-Ethernet/dp/B014SK2H6W/ref=sr_1_3_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=13Q33UHRKCKG5&keywords=vonet&qid=1676819146&s=electronics&sprefix=vonet%2Celectronics%2C98&sr=1-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1
> - Valgfri: ANTELA smart plugg https://www.amazon.fr/dp/B09YYMVXJZ/ref=twister_B0B5X46QLW?_encoding=UTF8&psc=1

## Kapittel 3 - VEILEDNING: Hvordan gjøre en miner til en varmeovn?

![bilde](assets/hardware/0.webp)

Hvis du er en dyktig DIY-entusiast og ser etter å gjøre en miner til en varmeovn, er denne veiledningen for deg. Vi ønsker å advare deg om at modifisering av en elektronisk enhet kan medføre elektriske og brannrisikoer. Det er essensielt å ta alle nødvendige forholdsregler for å unngå skader eller personskader.
Rett fra fabrikken er ikke en miner egentlig brukbar som en radiator i et hjem fordi den er for støyende og ikke justerbar. Det er imidlertid mulig å gjøre enkle modifikasjoner for å løse disse problemene.

> ADVARSEL: Det er essensielt å ha installert Braiins OS+ på din miner eller annen programvare som kan redusere maskinens ytelse tidligere. Dette tiltaket er kritisk fordi vi, for å redusere støy, vil installere mindre kraftige vifter som kan avlede mindre varme.

### Nødvendige materialer

- 2 stykker 3D-adapter 140mm til 120mm
- 2 Noctua NF-A14 iPPC-2000 PWM-vifter
- 2 140mm viftegriller
- 1 Noctua NF-A6x25 PWM-vifte
- 2.5mm2 elektrikerens sukker
- Vonets VAP11G-300
- Valgfritt: ANTELA smart plugg

### Erstatte viftene

Vi starter med å erstatte strømforsyningsviften.

> ADVARSEL: Først og fremst, før du starter, sørg for at du har trukket ut støpselet til mineren for å unngå risiko for elektrisk støt.

![bilde](assets/hardware/1.webp)

Vi starter med å erstatte strømforsyningsviften.

Først, fjern de 6 skruene på siden av kabinettet som holder det lukket. Når skruene er fjernet, åpne forsiktig kabinettet for å fjerne plastdekselet som beskytter komponentene.

![bilde](assets/hardware/2.webp)
![bilde](assets/hardware/3.webp)
Neste steg er å fjerne den originale viften, og være forsiktig så du ikke skader de andre komponentene. For å gjøre dette, fjern skruene som holder den på plass og forsiktig skrell av den hvite limen rundt kontakten. Det er viktig å fortsette forsiktig for å unngå å skade ledningene eller kontaktene.

Når den originale viften er fjernet, vil du legge merke til at kontaktene til den nye Noctua-viften ikke passer med de til den originale viften. Faktisk har den nye viften 3 ledninger, inkludert en gul ledning som tillater hastighetskontroll. Imidlertid vil ikke denne ledningen bli brukt i dette spesifikke tilfellet. For å koble til den nye viften, anbefales det å bruke en spesiell adapter. Det er imidlertid viktig å merke seg at denne adapteren noen ganger kan være vanskelig å finne.

Hvis du ikke har denne adapteren, kan du fortsatt fortsette med å koble til den nye viften ved å bruke en ledningsmutter. For å gjøre dette, må du kutte kablene til både den gamle og den nye viften.

På den nye viften, bruk en kutter og kutt forsiktig konturene av hovedkappen på 1cm uten å kutte kappene til kablene nedenfor.

Deretter, ved å trekke hovedkappen nedover, kutt kappene til de røde og svarte kablene på samme måte som før. Og kutt den gule kabelen helt ned.

På den gamle viften er det mer delikat å kutte hovedkappen uten å skade kappene til de røde og svarte ledningene. For dette brukte vi en nål som vi skled mellom hovedkappen og de røde og svarte ledningene.

Når de røde og svarte ledningene er eksponert, kutt kappene forsiktig for å unngå å skade de elektriske ledningene.

Deretter, koble kablene med en ledningsmutter, den svarte ledningen med den svarte og den røde ledningen med den røde. Du kan også legge til elektrisk tape.

Når tilkoblingen er gjort, er det på tide å installere den nye Noctua-viften med grillen og de gamle skruene, de nye skruene som er i boksen vil bli gjenbrukt senere. Sørg for å plassere den med riktig orientering. Du vil legge merke til en pil på den ene siden av viften, som indikerer luftstrømmens retning. Det er viktig å plassere viften slik at denne pilen peker mot innsiden av kabinettet. Deretter, koble til viften igjen.

> Valgfritt: Hvis du er dyktig i elektrisitet, kan du direkte legge til en kvinnelig 5,5mm jack-kontakt til 12V strømutgangen, som vil tillate deg å direkte strømforsyne Vonet Wi-Fi-broen. Imidlertid, hvis du er usikker på dine elektriske ferdigheter, er det best å bruke USB-kontakten med en smarttelefonlader for å unngå risiko for kortslutning eller elektrisk skade.

Når tilkoblingene er gjort, sørg for å plassere plastdekselet over plastkassen og ikke inni.
Til slutt, sett på dekselet igjen og skru de 6 skruene på sidene for å holde alt sikkert på plass. Og der har du det, strømforsyningkabinettet ditt er nå utstyrt med en ny vifte.
### Bytte av de 2 hovedviftene

1. Først, koble fra viftene og skru dem ut.
   ![bilde](assets/hardware/19.webp)

2. Kontaktene til de nye Noctua-viftene passer ikke til de originale, men ikke få panikk! Ta frem din kutter og klipp forsiktig de små plastikkflikene slik at kontaktene passer perfekt med din miner.

![bilde](assets/hardware/20.webp)
![bilde](assets/hardware/21.webp)

3. Nå er det på tide å installere 3D-delene!
   Fest dem på begge sider av mineren ved hjelp av skruene du fjernet fra viftene. Skru til skruehodet går inn i 3D-delen og den holdes sikkert på plass. Vær forsiktig så du ikke strammer for mye, da du kan deformere delen og en av skruene kan berøre en kondensator! Klipp deretter forsiktig de små plastikkflikene slik at kontaktene passer perfekt med din miner.

![bilde](assets/hardware/22.webp)

4. Nå, la oss gå videre til viftene.
   Fest dem til 3D-delene ved hjelp av skruene som følger med i esken. Vær oppmerksom på luftstrømmens retning, pilene på sidene av viftene vil indikere retningen å følge. Gå fra Ethernet-port-siden til den andre siden. Se bildet nedenfor.

![bilde](assets/hardware/23.webp)
![bilde](assets/hardware/24.webp)
![bilde](assets/hardware/25.webp)

5. Siste steg: Koble til viftene og fest grillene på toppen med de ubrukte skruene fra vifteesken. Du har bare 4, men 2 per grill i motsatte hjørner vil være nok. Du kan også se etter andre lignende skruer i en jernvarehandel om nødvendig.

![bilde](assets/hardware/26.webp)
'![bilde](assets/hardware/27.webp)

Mens du venter på å kunne tilby et mer tiltalende kabinett for din nye varmeovn, kan du feste kabinettet og strømforsyningen sammen med elektrikerstrips.

![bilde](assets/hardware/28.webp)

Og for den siste finishen, koble Vonet-broen til Ethernet-porten på strømforsyningen. Hvis du ikke allerede har gjort det, kan du følge denne veiledningen for å sette opp broen din.

![bilde](assets/hardware/29.webp)

Og der har du det, gratulerer! Du har nettopp byttet ut hele den mekaniske delen av din miner. Du bør nå høre mye mindre støy.

## Kapittel 4 - Programvaremodifikasjon - Tilbakestilling av en Antminer S9

**Artikkelserie foreslått av BlobOnChain & Ajelex - 15/02/2023**

### Tilbakestilling via "Reset"-knappen

Denne metoden kan anvendes innen 10 minutter etter at mineren er startet.

Etter å ha slått på mineren i 2 minutter, vennligst trykk på "Reset"-knappen i 5 sekunder, og slipp den deretter. Mineren vil bli gjenopprettet til fabrikkinnstillingene innen 4 minutter og vil automatisk starte på nytt (det er ikke nødvendig å slå den av).

![bilde](assets/software/1.webp)

Gjenopprett via websiden

Logg inn på brukergrensesnittet til mineren din, klikk på "Oppgrader" >> "Utfør en tilbakestilling", deretter klikk "OK" i popup-vinduet.

### Originalt operativsystem
For denne delen vil vi anta at maskinen fungerer, kjører, og at dens originale operativsystem er installert. Vi vil kort se på grensesnittet til det originale operativsystemet tilbudt av Bitmain.
Først, koble til maskinen din gjennom ditt lokale nettverk:

![bilde](assets/software/2.webp)

Når du er på innloggingssiden, må du logge inn på ASIC-en ved hjelp av standard påloggingsinformasjon:

- brukernavn: root
- passord: root

(Hvordan tilbakestille hvis standardpassordet ikke fungerer?)

Det primære operativsystemet er relativt grunnleggende. Med de 4 fanene: System, Miner Configuration, Miner Status, Network. I fanen Miner Configuration, kan du konfigurere opptil 3 mining-pools.

![bilde](assets/software/3.webp)

I fanen Miner Status, kan du observere ulike informasjoner om den direkte driften av ASIC-en. Hashraten uttrykt i GH/s, mer detaljert informasjon om poolen, samt detaljer om statusen til hver hashboard og viftehastigheten i rotasjoner/minutt.

![bilde](assets/software/4.webp)

### Braiins OS+'

Nå vil vi studere programvaren for ASIC-er, Braiins OS+ (https://braiins.com/os/plus). Programvaren er utviklet av selskapet Braiins (https://braiins.com/), som er morselskapet til mining-poolen Braiins Pool (https://braiins.com/pool). Denne mining-poolen har for øyeblikket 4,39% av den globale hashraten (https://mempool.space/fr/mining/pool/slushpool) på tidspunktet for skrivingen av disse linjene. Det Praha-baserte selskapet var tidligere kjent som Slushpool og er den første mining-poolen som startet i november 2010. I dag tilbyr selskapet, med sine ulike aktiviteter, lønnsomhetsstudieverktøy for mining (https://insights.braiins.com/en), løsninger for styring av mining-gårder parallelt med sin pool-aktivitet, og sin optimaliseringsprogramvare for ASIC-er. Det tilbyr også mining ved bruk av det nye Stratum V2-protokollen (https://braiins.com/bitcoin-mining-stack-upgrade).

Vi vil derfor studere mer detaljert driften av Bitmain-enheter, som for øyeblikket er de eneste kompatible modellene:

- S19, S19 Pro, S19j, S19j Pro, T19,

- 17, S17 Pro, S17+, S17e, T17, T17+, T17e & S9 [i, j]

Braiins OS-programvaren kan enkelt installeres på alle de ovennevnte maskinene. Den vil tillate mer presis kontroll av en maskin ved å tillate overklokking eller underklokking. Den tillater også finjustering av frekvensen til hver brikke gjennom en automatisk optimaliseringsfunksjon kalt autotuning. Siden hver hashingbrikke er litt forskjellig på grunn av sin produksjonsprosess, tester programvaren den optimale frekvensen for hver brikke for å oppnå maksimal effektivitet (W/THs). Programvaren hevder å oppnå ytelse som kan være 25% høyere enn det originale. Ifølge våre målinger, er det mulig å oppnå disse tallene.

## Installasjon av Braiins OS+

Det er flere måter å installere Braiins OS+ på en ASIC. Du kan referere til denne guiden samt den offisielle dokumentasjonen fra Braiins og videotutorials.
Lær hvordan du enkelt kan installere Braiins OS+ direkte på minnet til din Antminer ved hjelp av BOS toolbox, erstatte det originale operativsystemet, gjennom de detaljerte trinnene nedenfor. Hvis du ønsker å beholde det originale OS parallelt, kan du installere Braiins OS+ på et SD-kort.
1. Slå på din Antminer og koble den til internettboksen din.
2. Last ned BOS-verktøykassen for Windows / Linux.
3. Pakk ut den nedlastede filen og åpne bos-toolbox.bat-filen, velg språk, og etter et øyeblikk vil du se dette vinduet:
   ![bilde](assets/software/5.webp)

4. BOS-verktøykassen vil gjøre det enkelt for deg å finne IP-adressen til din Antminer og installere Braiins OS+. Hvis du allerede kjenner IP-adressen til maskinen din, kan du hoppe over til trinn 8. Ellers, gå til skannefanen.

![bilde](assets/software/6.webp)

5. Vanligvis, på hjemmenettverk, er IP-adresseområdet mellom 192.168.1.1 og 192.168.1.255, så skriv inn "192.168.1.0/24" i feltet for IP-område. Hvis nettverket ditt er annerledes, vennligst endre disse adressene. Deretter klikker du på "Start".

6. Vær oppmerksom, hvis Antmineren har et passord, vil ikke deteksjonen fungere. Hvis det er tilfellet, er den enkleste løsningen å utføre en fabrikkinnstilling.

7. Du bør se alle Antminerene på nettverket ditt, her er IP-adressen 192.168.1.37.

![bilde](assets/software/7.webp)

8. Klikk på Tilbake, deretter gå til installasjonsfanen, skriv inn den tidligere funnete IP-adressen i Miner(s)-feltet og "admin" (eller "root") i Passord-feltet, som er standardpassordet, deretter klikker du på "Start".
   Hvis installasjonen ikke fungerer med "admin" eller "root" som passord, kan det være nødvendig å utføre en fabrikkinnstilling og prøve igjen.

![bilde](assets/software/8.webp)

9. Etter noen øyeblikk vil din Antminer starte på nytt, og du vil kunne få tilgang til Braiins OS+-grensesnittet på den aktuelle IP-adressen, her 192.168.1.37, direkte i adressefeltet til nettleseren din. Standard brukernavn er "root" og det er ikke noe standard passord.
   Installere Braiins OS+ på et SD-kort

![bilde](assets/software/9.webp)

![bilde](assets/software/10.webp)

Den andre metoden bruker det originale grensesnittet til din Antminer. Denne metoden fungerer for maskiner med et operativsystem som dateres fra før 2019.

### Antminer-grensesnitt

1. Last ned det nye operativsystemet som skal installeres her.
2. Som i forrige seksjon, koble til maskinen din gjennom ditt lokale nettverk.
3. Gå til System-fanen og deretter Oppgradering.
4. Last opp filen du lastet ned og flash bildet.

![bilde](assets/software/11.webp)

### Micro SD-kort

En annen metode lar deg bruke et micro SD-kort. Denne metoden fungerer kun med maskiner med et operativsystem som dateres fra etter 2019.

1. Last ned det nye operativsystemet som skal installeres her.

2. Flash det nedlastede bildet på et micro SD-kort. For dette kan du bruke Etcher. Det vil ikke fungere å bare kopiere filen til micro SD-kortet.
3. Hvis du eier en Antminer S9 og dens varianter (S9i, S9j), må du justere jumperne for å tvinge din ASIC til å starte fra filen på micro SD-kortet i stedet for NAND. Hvis du har en annen modell, kan du hoppe over til del 4. Jumperne er plassert på kontrollkortet på den øvre delen av ASIC-en, nær Ethernet-porten. Du må fjerne det ved å skyve det bakover. Når jumperposisjonen er endret som vist på bildene nedenfor BOOT FROM SD, kan du sette inn kontrollkortet på nytt og koble til S9 igjen.
![bilde](assets/software/12.webp)

![bilde](assets/software/13.webp)

4. Sett inn micro SD-kortet i ASIC-en.
5. Start ASIC-en. Hvis den automatiske installasjonsversjonen ble brukt, vil det nye operativsystemet bli installert automatisk. Installasjonen er fullført når begge LED-lysene lyser samtidig. Du kan starte ASIC-en på nytt og fjerne micro SD-kortet. Hvis den andre versjonen ble lastet ned, må du la micro SD-kortet være inne i ASIC-en.

For mer informasjon om installasjon, kan du besøke denne delen av Braiins-nettstedet.

## Grensesnittet

Du må koble til din ASIC på en lignende måte. Ved å bruke den lokale IP-adressen til enheten din på nettverket gjennom en nettleser.

Standard påloggingsinformasjon er den samme som det opprinnelige operativsystemet.

- brukernavn: root
- passord: root

Du vil da bli møtt av Brains OS+ Dashboard.

### Dashboard

![bilde](assets/software/14.webp)

På denne første siden kan du observere maskinens sanntidsytelse.

- Tre sanntidsgrafer som viser temperaturen, hashraten og den generelle statusen til maskinen din.
- På høyre side, den reelle hashraten, gjennomsnittstemperaturen på chipen, estimert effektivitet i W/THs, og strømforbruk.
- Nedenfor, viftehastigheten i prosent av maksimal hastighet og antall rotasjoner per minutt.

![bilde](assets/software/15.webp)

- Lenger ned, vil du finne en detaljert visning av hvert hashbord. Gjennomsnittstemperaturen på kortet og chipene det inneholder, spenning, og frekvens.
- Detaljer om de aktive gruvebassengene i Pools.
- Statusen for autotuning i Tuner Status.
- På høyre side, detaljer om aksjene overført til bassenget.

### Konfigurasjon

![bilde](assets/software/16.webp)

### System

![bilde](assets/software/17.webp)

### Hurtigaksjoner

![bilde](assets/software/18.webp)

Konfigurering av et basseng
Man kan forestille seg en gruvepool som et landbrukskooperativ. Bønder samler sin produksjon sammen for å redusere variansen i tilbud og etterspørsel og dermed oppnå en mer stabil inntekt for sin virksomhet. En gruvepool fungerer på samme måte, og det råmaterialet som samles sammen er hasher. Faktisk tillater oppdagelsen av en enkelt gyldig hash opprettelsen av en blokk og dermed vinning av coinbase eller belønningen, som for øyeblikket er 6,25 BTC pluss transaksjonsgebyrene inkludert i blokken. Hvis du miner alene, vil du kun bli belønnet når du finner en blokk. Ved å være i konkurranse mot alle andre minere på planeten, ville du ha veldig liten sjanse for å vinne denne store lotteriet, og du måtte fortsatt betale gebyrene forbundet med å bruke din miner uten noen garanti for suksess. Gruvepooler adresserer dette problemet ved å samle databehandlingskraften til flere (tusenvis av) minere og dele deres belønninger basert på prosentandelen av deltakelse i poolens hashrate når en blokk blir funnet. For å visualisere sjansene dine for å mine en blokk alene, kan du bruke dette verktøyet. Ved å legge inn informasjonen til en Antminer S9, kan vi se at sjansene for å finne en hash som tillater opprettelsen av en blokk er 1 i 24,777,849 for hver blokk eller 1 i 172,068 per dag. I gjennomsnitt (med en konstant hashrate og vanskelighetsgrad), ville det ta 471 år å finne en blokk.
Men, siden alt i Bitcoin er sannsynlighet, skjer det noen ganger at solo-minere blir belønnet for å ta denne risikoen: Solo Bitcoin Miner Løser Blokk Med Hash Rate på Bare 10 TH/s, Slår Ekstremt Usannsynlige Odds – Decrypt

Hvis du liker å gamble, kan du prøve det, men vår guide vil ikke fokusere i den retningen. I stedet vil vi konsentrere oss om gruvepoolen som best passer våre behov for å skape et oppvarmingssystem.
Hensynene man må ta når man velger en gruvepool er driften av poolens belønninger, som kan være forskjellige, samt minimumsbeløpet før man kan ta ut belønningene til en adresse. For eksempel, Braiins, som tilbyr programvaren vi snakker om her, tilbyr også en pool. Denne poolen har et belønningssystem kalt "Score" som oppmuntrer minere til å mine over lange perioder. Deltakelse inkluderer en aktivitetstidsfaktor som uttrykkes med en "scoring hashrate". I vårt tilfelle, der vi ønsker et oppvarmingssystem som kan slås på bare noen få minutter, er dette ikke det ideelle belønningssystemet. Vi foretrekker et belønningssystem som gir oss en lik belønning for hver deltakelse. I tillegg er minimumsuttaksbeløpet for Braiins Pool 100 000 sats og On-Chain. Så vi taper noen sats i transaksjonsgebyrer, og en del av vår belønning kan bli låst hvis vi ikke miner nok i løpet av vinteren.

Belønningsmodellen som interesserer oss er PPS, som står for "pay-per-share". Dette betyr at miner vil motta en belønning for hver gyldig andel. Det finnes også en variant av dette systemet, FPPS (Full Pay Per Share), som ikke bare deler coinbase-belønningen, men også transaksjonsgebyrene inkludert i blokken. Gruvepoolene vi anbefaler for å koble til ditt mining/oppvarming er Linecoin Pool (FPPS) og Nicehash (PPS).

- Nicehash: Fordelen med Nicehash er at uttak kan gjøres ved hjelp av Lightning med minimale gebyrer. I tillegg er minimumsuttaksbeløpet 2000 sats. Ulempen er at Nicehash bruker sin hashrate for den mest lønnsomme blockchain, uten å virkelig gi kontroll til brukeren, så det kan ikke nødvendigvis delta i Bitcoin hashrate.
- Linecoin: Fordelen med Linecoin er antallet funksjoner som tilbys, som et detaljert dashbord, muligheten til å gjøre uttak med en Paynym (BIP 47) for bedre personvernbeskyttelse, og integreringen av en Telegram-bot samt direkte konfigurerbare automatiseringer i mobilapplikasjonen. Denne poolen miner kun Bitcoin-blokker, men det minste beløpet for uttak forblir høyt på 100 000 sats. Vi vil undersøke grensesnittet til en av disse poolene mer detaljert i en fremtidig artikkel.
For å konfigurere en pool i Braiins OS+, må du opprette en konto i en av poolene du velger. Her vil vi ta eksemplet med Linecoin:

![bilde](assets/software/19.webp)

Når kontoen din er opprettet, klikk på Koble til Pool

Deretter kopierer du Stratum-adressen samt brukernavnet ditt:

![bilde](assets/software/20.webp)

Du kan nå gå tilbake til Braiins OS+-grensesnittet for å legge inn disse legitimasjonene. For passordet, kan du la feltet stå tomt.

![bilde](assets/software/21.webp)

### Overklokking og Underklokking

Overklokking og autotuning innebærer begge justering av frekvenser på hashingkort for å forbedre ASIC-ytelsen. Forskjellen mellom de to ligger i kompleksiteten av disse frekvensinnstillingene.

**Overklokking** er en enkel justering som innebærer å øke frekvensen på hashingkort for å øke maskinens hash rate. Underklokking, derimot, innebærer å redusere klokkefrekvensen til en integrert krets under dens nominelle frekvens. Ved å redusere klokkefrekvensen til en ASIC gjennom underklokking, reduseres også varmen som genereres av maskinvaren. Dette tillater en reduksjon i hastigheten på viftene som trengs for å kjøle ned ASIC-en, ettersom de ikke må jobbe like hardt for å opprettholde en passende temperatur. Ved å redusere viftehastigheten, reduseres også støyen som genereres av ASIC-en. Dette kan være spesielt nyttig for brukere som bruker ASIC-er hjemme og ser etter å minimere støyforstyrrelser forårsaket av mining-maskinvare.

Det er viktig å merke seg at underklokking kan resultere i en reduksjon i ASIC-ytelsen, så det er viktig å finne en god balanse mellom ytelse og støy.

Braiins OS+ støtter overklokking, underklokking av ASIC-er, og autotuning. Det lar brukere justere klokkefrekvensen på maskinvaren sin fleksibelt for å maksimere ytelse eller spare energi i henhold til deres preferanser.

### Autotuning

Før 2018 hadde gruvearbeidere to måter å oppnå en fordel i sin aktivitet: å finne elektrisitet til en rimelig kostnad og kjøpe mer effektiv maskinvare. Imidlertid, i 2018, ble en ny fremskritt oppdaget innen feltet for mining-programvare og firmware, kalt AsicBoost. Denne teknikken lar gruvearbeidere redusere kostnadene sine med omtrent 13% ved å modifisere firmwaren som kjører på enhetene deres.
I dag finnes det en ny fremskritt innen programvare- og firmware-sektoren for mining kalt autotuning, som tilbyr en enda større fordel enn AsicBoost. ASIC-er består av mange små databrikker som utfører hashing. Disse brikkene er laget av silisium, det samme elementet som er mye brukt i halvledere og andre mikroelektroniske komponenter. Nøkkelforståelsen her er at ikke alle silisiumbrikker er identiske - hver enkelt kan variere litt i sine elektriske egenskaper. Maskinvareprodusenter vet dette og publiserer ytelsesspesifikasjonene til sine mining-maskiner basert på den nedre grensen av deres toleranser. Med andre ord, produsentene kjenner frekvensen som fungerer best for gjennomsnittlige brikker, og de bruker denne frekvensen ensartet for alle brikkene i maskinen.
Dette setter en øvre grense for hash-raten som en maskin kan ha. Autotuning er en prosess der algoritmer evaluerer de optimale frekvensene for hashing chip-for-chip, i stedet for å behandle hele maskinen som en enkelt enhet. Dette betyr at en chip av høyere kvalitet som kan utføre flere hasher per sekund vil få en høyere frekvens, og en chip av lavere kvalitet som kan utføre relativt færre hasher vil få en lavere frekvens. Autotuning på chip-nivå er i hovedsak en måte å optimalisere ytelsen til en ASIC gjennom programvaren og firmwaren som kjører på den.

Sluttresultatet er en høyere hash-rate per watt med elektrisitet, noe som betyr større fortjenestemarginer for gruvearbeidere. Grunnen til at maskiner ikke distribueres med denne typen programvare er at maskinvarians er uønsket, ettersom kunder ønsker å vite nøyaktig hva de får, og det er derfor en dårlig idé for produsenter å selge et produkt som ikke har konsekvent og forutsigbar ytelse fra en maskin til en annen. I tillegg krever autotuning på chip-nivå betydelige utviklingsressurser, ettersom det er komplekst å implementere. Produsenter bruker allerede mye ressurser på å utvikle sine egne firmware. Det finnes programvareløsninger som tillater autotuning, slik som Braiins OS+. I tillegg til å forbedre ASIC-ytelsen med opptil 20%.

> Guide laget av DecouvreBitcoin, mer info om MINAGE 201 - kreditt Jim og Ajelex'