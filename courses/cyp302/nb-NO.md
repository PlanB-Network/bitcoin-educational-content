---
name: Introduksjon til formell kryptografi
goal: En dypdykk i vitenskapen om og praktiseringen av kryptografi.
objectives: 

  - Utforsk Beale-chiffer og moderne kryptografiske metoder for å forstå grunnleggende og historiske begreper innen kryptografi.
  - Fordyp deg i tallteori, grupper og felt for å mestre sentrale matematiske begreper som ligger til grunn for kryptografi.
  - Studer RC4-strømmekryptering og AES med en 128-biters nøkkel for å lære om symmetriske kryptografiske algoritmer.
  - Undersøk RSA-kryptosystemet, nøkkeldistribusjon og hashfunksjoner for å utforske asymmetrisk kryptografi.

---
# Dypdykk i kryptografi

Det er vanskelig å finne mye materiale som tilbyr en god mellomting i kryptografiundervisningen.

På den ene siden finnes det lange, formelle avhandlinger som egentlig bare er tilgjengelige for dem som har en solid bakgrunn i matematikk, logikk eller en annen formell disiplin. På den andre siden finnes det introduksjoner på et svært høyt nivå som egentlig skjuler for mange av detaljene for alle som er i det minste litt nysgjerrige.

Denne introduksjonen til kryptografi forsøker å finne en mellomting. Selv om den bør være relativt utfordrende og detaljert for alle som er nye i kryptografi, er den ikke et kaninhull av en typisk grunnleggende avhandling.

+++
# Innledning

<partId>bbed2f46-d64c-5fb5-b892-d726032f2494</partId>

## Kort beskrivelse

<chapterId>bb8a8b73-7fb2-50da-bf4e-98996d79887b</chapterId>

Denne boken gir en grundig innføring i vitenskapen om og utøvelsen av kryptografi. Der det er mulig, fokuserer den på konseptuell snarere enn formell fremstilling av materialet.

> Dette kurset er basert på [JWBurgers' repo] (https://github.com/JWBurgers/An_Introduction_to_Cryptography). All right til ham. Innholdet er ennå ikke ferdig og er bare her for å vise hvordan vi kan integrere det hvis JWburger er enig.
### Motivasjon og mål

Det er vanskelig å finne mye materiale som tilbyr en god mellomting i kryptografiundervisningen.

På den ene siden finnes det lange, formelle avhandlinger som egentlig bare er tilgjengelige for dem som har en solid bakgrunn i matematikk, logikk eller en annen formell disiplin. På den andre siden finnes det introduksjoner på et svært høyt nivå som egentlig skjuler for mange av detaljene for alle som er i det minste litt nysgjerrige.

Denne introduksjonen til kryptografi forsøker å finne en mellomting. Selv om den bør være relativt utfordrende og detaljert for alle som er nye i kryptografi, er den ikke et kaninhull av en typisk grunnleggende avhandling.

### Målgruppe

Denne boken er nyttig for alle som ønsker mer enn en overfladisk forståelse av kryptografi, fra utviklere til intellektuelt nysgjerrige. Hvis målet ditt er å mestre kryptografifaget, er denne boken også et godt utgangspunkt.

### Retningslinjer for lesing

Boken inneholder for tiden syv kapitler: "Hva er kryptografi?" (kapittel 1), "Kryptografiens matematiske grunnlag I" (kapittel 2), "Kryptografiens matematiske grunnlag II" (kapittel 3), "Symmetrisk kryptografi" (kapittel 4), "RC4 og AES" (kapittel 5), "Asymmetrisk kryptografi" (kapittel 6) og "RSA-kryptosystemet" (kapittel 7). Et siste kapittel, "Kryptografi i praksis", vil fortsatt bli lagt til. Det fokuserer på ulike kryptografiske anvendelser, blant annet transportlagssikkerhet, onion routing og Bitcoins verdiutvekslingssystem.

Med mindre du har en sterk bakgrunn i matematikk, er tallteori sannsynligvis det vanskeligste emnet i denne boken. Jeg gir en oversikt over det i kapittel 3, og det dukker også opp i fremstillingen av AES i kapittel 5 og RSA-kryptosystemet i kapittel 7.

Hvis du virkelig sliter med de formelle detaljene i disse delene av boken, anbefaler jeg at du nøyer deg med å lese dem på et høyt nivå første gang.

### Erkjennelser

Den boken som har hatt størst innflytelse på denne, er Jonathan Katz og Yehuda Lindells _Introduction to Modern Cryptography_, CRC Press (Boca Raton, FL), 2015. Et tilhørende kurs er tilgjengelig på Coursera under tittelen "Cryptography"

De viktigste tilleggskildene som har vært nyttige for å skape oversikten i denne boken, er Simon Singh, _The Code Book_, Fourth Estate (London, 1999); Christof Paar og Jan Pelzl, _Understanding Cryptography_, Springer (Heidelberg, 2010) og [et kurs basert på boken til Paar kalt "Introduction to Cryptography"] (https://www.youtube.com/channel/UC1usFRN4LCMcfIV7UjHNuQg); og Bruce Schneier, Applied Cryptography, 2nd edn, 2015 (Indianapolis, IN: John Wiley & Sons).

Jeg vil bare sitere helt spesifikk informasjon og resultater jeg har hentet fra disse kildene, men jeg vil gjerne anerkjenne min generelle gjeld til dem her.

For de leserne som ønsker å oppsøke mer avansert kunnskap om kryptografi etter denne introduksjonen, anbefaler jeg Katz og Lindells bok på det varmeste. Katz' kurs på Coursera er noe mer tilgjengelig enn boken.

### Bidrag

Ta en titt på [bidragsfilen i depotet] (https://github.com/JWBurgers/An_Introduction_to_Cryptography/blob/master/Contributions.md) for å finne noen retningslinjer for hvordan du kan støtte prosjektet.

### Notasjon

**Nøkkelord:**

Nøkkelbegrepene i grunnbøkene introduseres ved å gjøre dem fete. For eksempel vil introduksjonen av Rijndael-chifferet som nøkkelbegrep se ut som følger: **Rijndael-chiffer**.

Nøkkelbegreper defineres eksplisitt, med mindre det dreier seg om egennavn eller betydningen er åpenbar ut fra diskusjonen.

En definisjon gis vanligvis ved introduksjonen av et nøkkelbegrep, men noen ganger er det mer praktisk å vente med definisjonen til et senere tidspunkt.

**Fremhevede ord og uttrykk:**

Ord og fraser fremheves med kursiv skrift. For eksempel vil frasen "Husk passordet ditt" se ut som følger: *Husk passordet ditt*.

**Formal notasjon:**

Den formelle notasjonen gjelder hovedsakelig variabler, tilfeldige variabler og mengder.


- Variabler: Disse angis vanligvis bare med en liten bokstav (f.eks. "x" eller "y"). Noen ganger skrives de med stor forbokstav for å gjøre det tydeligere (f.eks. "M" eller "K").
- Tilfeldige variabler: Disse angis alltid med en stor bokstav (f.eks. "X" eller "Y")
- Sett: Disse er alltid angitt med fete, store bokstaver (f.eks. **S**)

# Hva er kryptografi?

<partId>48e4d6d5-cd00-5c00-8adb-ae8477ff47c4</partId>

## Beale-chiffrene

<chapterId>ae674346-4789-5ab1-9b6f-c8989d83be89</chapterId>

La oss starte vår undersøkelse av kryptografien med en av de mer sjarmerende og underholdende episodene i dens historie: Beale-chiffrene. [1]

Historien om Beale-chiffrene er etter min mening mer sannsynlig fiksjon enn virkelighet. Men det skal ha foregått på følgende måte.

Både vinteren 1820 og 1822 bodde en mann ved navn Thomas J. Beale på et vertshus eid av Robert Morriss i Lynchburg (Virginia). Ved slutten av Beales andre opphold overrakte han Morriss en jernboks med verdifulle papirer til oppbevaring.

Noen måneder senere mottok Morriss et brev fra Beale datert 9. mai 1822. Brevet understreket den store verdien av innholdet i jernskrinet og ga Morriss noen instrukser: Hvis verken Beale eller noen av hans medarbeidere noen gang kom for å gjøre krav på skrinet, skulle han åpne det nøyaktig ti år etter brevets dato (det vil si 9. mai 1832). Noen av papirene i esken ville være skrevet med vanlig tekst. Flere andre ville imidlertid være "uforståelige uten hjelp av en nøkkel" Denne "nøkkelen" skulle altså bli levert til Morriss av en ikke navngitt venn av Beale i juni 1832.

Til tross for de klare instruksene åpnet ikke Morriss skrinet i mai 1832, og Beales mystiske venn dukket aldri opp i juni samme år. Først i 1845 bestemte kroverten seg endelig for å åpne esken. I esken fant Morriss en lapp som forklarte hvordan Beale og hans kompanjonger hadde funnet gull og sølv i Vesten og gravd det ned sammen med noen smykker for å ta vare på det. I tillegg inneholdt esken tre **krypteringstekster**, det vil si tekster skrevet i kode som krever en **kryptografisk nøkkel**, eller en hemmelighet, og en tilhørende algoritme for å låses opp. Denne prosessen med å låse opp en chiffertekst kalles **dekryptering**, mens låseprosessen kalles **kryptering**. (Som forklart i kapittel 3, kan begrepet chiffer ha ulike betydninger. I navnet "Beale ciphers" er det en forkortelse for ciphertexts)

De tre chiffertekstene som Morriss fant i jernskrinet, består hver av en rekke tall adskilt med komma. Ifølge Beales notat inneholder disse chiffertekstene hver for seg informasjon om hvor skatten befinner seg, innholdet i skatten og en liste over navnene på de rettmessige arvingene til skatten og deres andeler (sistnevnte informasjon er relevant i tilfelle Beale og hans kompanjonger aldri kom for å gjøre krav på skrinet).

Morris forsøkte å dekryptere de tre krypteringstekstene i tjue år. Med nøkkelen ville dette ha vært enkelt. Men Morriss hadde ikke nøkkelen, og han lyktes ikke i sine forsøk på å gjenopprette de opprinnelige tekstene, eller **plaintexts** som de vanligvis kalles i kryptografi.

På slutten av sitt liv ga Morriss boksen videre til en venn i 1862. Denne vennen publiserte deretter en pamflett i 1885, under pseudonymet J.B. Ward. Den inneholdt en beskrivelse av boksens (påståtte) historie, de tre chiffertekstene og en løsning som han hadde funnet for den andre chifferteksten. (Tilsynelatende er det én nøkkel for hver chiffertekst, og ikke én nøkkel som fungerer på alle tre chiffertekstene, slik Beale opprinnelig ser ut til å ha antydet i brevet til Morriss)

Du kan se den andre krypteringsteksten i *Figur 2* nedenfor. [Nøkkelen til denne krypteringsteksten er USAs uavhengighetserklæring. Dekrypteringsprosedyren går ut på å bruke følgende to regler:


- Finn det n-te ordet i USAs uavhengighetserklæring for et hvilket som helst tall n i krypteringsteksten
- Erstatt tallet n med den første bokstaven i ordet du fant

*Figur 1: Beale-chiffer nr. 2*

![Figure 1: Beale cipher no 2.](assets/Figure1-1.webp "Figure 1: Beale cipher no. 2")

For eksempel er det første tallet i den andre chifferteksten 115. Det 115. ordet i uavhengighetserklæringen er "instituted", så den første bokstaven i klarteksten er "i" Krypteringsteksten angir ikke direkte ordavstand og store bokstaver. Men etter å ha dekryptert de første ordene, kan du logisk utlede at det første ordet i klarteksten rett og slett var "I" (Klarteksten starter med setningen "I have deposited in the county of Bedford.")

Etter dekryptering gir den andre meldingen en detaljert beskrivelse av skattens innhold (gull, sølv og juveler), og antyder at den ble begravd i jerngryter og dekket med steiner i Bedford County (Virginia). Folk elsker gode mysterier, så det har blitt lagt ned mye arbeid i å dekryptere de to andre Beale-krypteringene, særlig den som beskriver hvor skatten befinner seg. Til og med flere fremtredende kryptografer har forsøkt seg på dem. Men foreløpig har ingen klart å dekryptere de to andre chiffertekstene.

**Noter:**

[1] For en god oppsummering av historien, se Simon Singh, *The Code Book*, Fourth Estate (London, 1999), s. 82-99. Andrew Allen laget en kortfilm av historien i 2010. Du finner filmen, "The Thomas Beale Cipher", [på nettsiden] (http://www.thomasbealecipher.com/).

[2] Dette bildet er tilgjengelig på Wikipedia-siden for Beale-chiffrene.

## Moderne kryptografi

<chapterId>d07d576f-8a4b-5890-b182-2e5763f550f4</chapterId>

Fargerike historier som den om Beale-chiffrene er det de fleste av oss forbinder med kryptografi. Moderne kryptografi skiller seg imidlertid fra denne typen historiske eksempler på minst fire viktige måter.

For det første har kryptografi historisk sett kun vært opptatt av **hemmelighet** (eller konfidensialitet). [Krypteringstekster ble laget for å sikre at bare visse parter kunne få tilgang til informasjonen i klartekstene, som i tilfellet med Beale-kryptering. For at et krypteringsopplegg skal tjene dette formålet på en god måte, bør det bare være mulig å dekryptere chifferteksten hvis du har nøkkelen.

Moderne kryptografi er opptatt av et bredere spekter av temaer enn bare hemmeligholdelse. Disse temaene omfatter først og fremst (1) **meldingsintegritet** - det vil si å sikre at en melding ikke har blitt endret; (2) **meldingsautentisitet** - det vil si å sikre at en melding virkelig kommer fra en bestemt avsender; og (3) **uavviselighet** - det vil si å sikre at en avsender ikke senere kan nekte for at hun har sendt en melding. [4]

Et viktig skille å huske på er derfor mellom et **krypteringsopplegg** og et **kryptografisk opplegg**. Et krypteringsopplegg handler bare om hemmelighold. Selv om et krypteringsopplegg er et kryptografisk opplegg, er ikke det motsatte tilfelle. Et kryptografisk skjema kan også tjene de andre hovedtemaene i kryptografi, inkludert integritet, autentisitet og uavviselighet.

Temaene integritet og autentisitet er like viktige som hemmeligholdelse. Våre moderne kommunikasjonssystemer ville ikke kunne fungere uten garantier for kommunikasjonens integritet og autentisitet. Uavviselighet er også viktig, for eksempel i forbindelse med digitale kontrakter, men det er ikke like nødvendig i kryptografiske anvendelser som hemmelighold, integritet og autentisitet.

For det andre involverer klassiske krypteringsmetoder, som Beale-chiffrene, alltid én nøkkel som deles mellom alle de relevante partene. Mange moderne krypteringsmetoder involverer imidlertid ikke bare én, men to nøkler: en **privat** og en **offentlig nøkkel**. Mens førstnevnte skal forbli privat i alle anvendelser, er sistnevnte vanligvis offentlig kjent (derav de respektive navnene). Når det gjelder kryptering, kan den offentlige nøkkelen brukes til å kryptere meldingen, mens den private nøkkelen kan brukes til dekryptering.

Den delen av kryptografien som omhandler systemer der alle parter deler én nøkkel, kalles **symmetrisk kryptografi**. Den ene nøkkelen i et slikt system kalles vanligvis den **private nøkkelen** (eller den hemmelige nøkkelen). Den grenen av kryptografien som omhandler systemer som krever et privat-offentlig nøkkelpar, kalles **asymmetrisk kryptografi**. Disse grenene omtales noen ganger også som henholdsvis **privatnøkkelkryptografi** og **offentlignøkkelkryptografi** (selv om dette kan skape forvirring, ettersom kryptografiske systemer med offentlig nøkkel også har private nøkler).

Fremveksten av asymmetrisk kryptografi på slutten av 1970-tallet har vært en av de viktigste hendelsene i kryptografiens historie. Uten den ville de fleste av våre moderne kommunikasjonssystemer, inkludert Bitcoin, ikke vært mulige, eller i det minste svært upraktiske.

Det er viktig å merke seg at moderne kryptografi ikke utelukkende er studiet av symmetriske og assymetriske nøkkelkryptografiske systemer (selv om det dekker store deler av feltet). Kryptografi handler for eksempel også om hashfunksjoner og pseudotilfeldige tallgeneratorer, og du kan bygge applikasjoner på disse primitivene som ikke er relatert til symmetrisk eller assymetrisk nøkkelkryptografi.

For det tredje var klassiske krypteringsskjemaer, som de som ble brukt i Beale-chiffrene, mer kunst enn vitenskap. Den opplevde sikkerheten var i stor grad basert på intuisjoner om kompleksiteten. De ble vanligvis oppdatert når man oppdaget et nytt angrep på dem, eller droppet helt hvis angrepet var spesielt alvorlig. Moderne kryptografi er imidlertid en streng vitenskap med en formell, matematisk tilnærming til både utvikling og analyse av kryptografiske ordninger. [5]

Moderne kryptografi er sentrert rundt formelle **sikkerhetsbevis**. Ethvert sikkerhetsbevis for et kryptografisk system består av tre trinn:

1.	En **kryptografisk definisjon av sikkerhet**, det vil si et sett med sikkerhetsmål og den trusselen som angriperen utgjør.

2.	Angivelse av eventuelle matematiske antagelser med hensyn til beregningskompleksiteten til opplegget. Et kryptografisk system kan for eksempel inneholde en pseudotilfeldige tallgenerator. Selv om vi ikke kan bevise at disse finnes, kan vi anta at de gjør det.

3.	En matematisk **bevis for sikkerhet** for ordningen på grunnlag av det formelle sikkerhetsbegrepet og eventuelle matematiske antagelser.

For det fjerde: Mens kryptografi historisk sett først og fremst ble brukt i militære sammenhenger, har det i den digitale tidsalderen kommet til å gjennomsyre våre daglige aktiviteter. Enten du bruker nettbank, legger ut innlegg på sosiale medier, kjøper et produkt fra Amazon med kredittkortet ditt eller gir en venn bitcoin i tips, er kryptografi en uunnværlig del av vår digitale tidsalder.

På bakgrunn av disse fire aspektene ved moderne kryptografi kan vi karakterisere moderne **kryptografi** som vitenskapen som er opptatt av formell utvikling og analyse av kryptografiske ordninger for å sikre digital informasjon mot motstanderangrep. [6] Sikkerhet bør her forstås bredt som å forhindre angrep som skader hemmelighold, integritet, autentisering og/eller uavviselighet i kommunikasjon.

Kryptografi kan best ses på som en underdisiplin av **cybersikkerhet**, som handler om å forhindre tyveri, skade og misbruk av datasystemer. Merk at mange cybersikkerhetsproblemer har liten eller bare delvis tilknytning til kryptografi.

Hvis et selskap for eksempel har dyre servere lokalt, kan de være opptatt av å sikre denne maskinvaren mot tyveri og skade. Selv om dette er et cybersikkerhetsproblem, har det lite med kryptografi å gjøre.

Et annet eksempel er **phishing-angrep**, som er et vanlig problem i vår moderne tid. Disse angrepene går ut på å lure folk til å oppgi sensitiv informasjon, for eksempel passord eller kredittkortnummer, via e-post eller andre medier. Kryptografi kan til en viss grad bidra til å håndtere phishing-angrep, men en helhetlig tilnærming krever mer enn bare å bruke litt kryptografi.

**Noter:**

[3] For å være helt nøyaktig har de viktigste bruksområdene for kryptografiske systemer dreid seg om hemmeligholdelse. Barn, for eksempel, bruker ofte enkle kryptografiske ordninger for "moro skyld". Hemmelighold er ikke noe problem i slike tilfeller.

[4] Bruce Schneier, *Applied Cryptography*, 2. utgave, 2015 (Indianapolis, IN: John Wiley & Sons), s. 2.

[5] Se Jonathan Katz og Yehuda Lindell, *Introduction to Modern Cryptography*, CRC Press (Boca Raton, FL: 2015), spesielt s. 16-23, for en god beskrivelse.

[6] Jf. Katz og Lindell, ibid. s. 3. Jeg synes karakteristikken deres er problematisk, og presenterer derfor en litt annen versjon av uttalelsen deres her.

## Åpen kommunikasjon

<chapterId>cb23d0a6-ba9a-5dc6-a55a-258405ae4117</chapterId>

Moderne kryptografi er utviklet for å gi sikkerhetsgarantier i et **åpent kommunikasjonsmiljø**. Hvis kommunikasjonskanalen vår er så godt beskyttet at avlyttere ikke har noen mulighet til å manipulere eller bare observere meldingene våre, er kryptografi overflødig. De fleste av våre kommunikasjonskanaler er imidlertid neppe så godt beskyttet.

Ryggraden i kommunikasjonen i den moderne verden er et enormt nettverk av fiberoptiske kabler. Telefonsamtaler, TV-titting og surfing på nettet i en moderne husholdning er vanligvis avhengig av dette nettverket av fiberoptiske kabler (en liten andel kan være avhengig av satellitter). Det er sant at du kan ha forskjellige datatilkoblinger i hjemmet ditt, for eksempel koaksialkabel, (asymmetrisk) digital abonnentlinje og fiberoptisk kabel. Men, i hvert fall i den utviklede verden, kobles disse ulike datamediene raskt sammen utenfor huset ditt til en node i et enormt nettverk av fiberoptiske kabler som forbinder hele kloden. Unntaket er enkelte avsidesliggende områder i den utviklede verden, som i USA og Australia, der datatrafikken fortsatt kan gå over store avstander via tradisjonelle kobbertelefonledninger.

Det ville være umulig å hindre potensielle angripere i å få fysisk tilgang til dette kabelnettverket og infrastrukturen som støtter det. Faktisk vet vi allerede at de fleste av dataene våre fanges opp av ulike nasjonale etterretningstjenester ved viktige knutepunkter på Internett[7]. Dette omfatter alt fra Facebook-meldinger til nettadresser du besøker.

Mens overvåking av data i stor skala krever en mektig motstander, for eksempel en nasjonal etterretningstjeneste, kan angripere med få ressurser enkelt forsøke å snoke i mer lokal skala. Selv om dette kan skje ved avlytting av ledninger, er det langt enklere å avlytte trådløs kommunikasjon.

Mesteparten av de lokale nettverksdataene våre - enten det er hjemme, på kontoret eller på en kafé - sendes nå via radiobølger til trådløse aksesspunkter på alt-i-ett-rutere, i stedet for gjennom fysiske kabler. En angriper trenger derfor lite ressurser for å snappe opp lokal trafikk. Dette er spesielt bekymringsfullt ettersom de fleste gjør svært lite for å beskytte dataene som sendes via det lokale nettverket. I tillegg kan potensielle angripere også angripe de mobile bredbåndsforbindelsene våre, som 3G, 4G og 5G. All denne trådløse kommunikasjonen er et lett mål for angripere.

Derfor er ideen om å holde kommunikasjonen hemmelig ved å beskytte kommunikasjonskanalen en håpløs vrangforestilling for store deler av den moderne verden. Alt vi vet, gir grunn til alvorlig paranoia: Du må alltid regne med at noen lytter. Og kryptografi er det viktigste verktøyet vi har for å oppnå noen form for sikkerhet i dette moderne miljøet.

**Noter:**

[7] Se for eksempel Olga Khazan, "The creepy, long-standing practice of undersea cable tapping", *The Atlantic*, 16. juli 2013 (tilgjengelig på [The Atlantic] (https://www.theatlantic.com/international/archive/2013/07/the-creepy-long-standing-practice-of-undersea-cable-tapping/277855/)).

# Kryptografiens matematiske grunnlag 1

<partId>1bf9f0aa-0f68-5493-83fb-2167238ff9de</partId>

## Tilfeldige variabler

<chapterId>b623a7d0-3dff-5803-bd4e-8257ff73dd69</chapterId>

Kryptografi er avhengig av matematikk. Og hvis du ønsker å bygge opp mer enn en overfladisk forståelse av kryptografi, må du være komfortabel med denne matematikken.

Dette kapittelet introduserer det meste av den grunnleggende matematikken du vil støte på når du skal lære deg kryptografi. Emnene inkluderer tilfeldige variabler, modulooperasjoner, XOR-operasjoner og pseudotilfeldighet. Du bør beherske stoffet i disse avsnittene for å få en forståelse av kryptografi som ikke er overfladisk.

Neste avsnitt handler om tallteori, som er mye mer utfordrende.

### Tilfeldige variabler

En tilfeldig variabel betegnes vanligvis med en stor bokstav som ikke er fet. Vi kan for eksempel snakke om en tilfeldig variabel $X$, en tilfeldig variabel $Y$ eller en tilfeldig variabel $Z$. Det er denne notasjonen jeg også vil bruke fra nå av.

En **tilfeldig variabel** kan anta to eller flere mulige verdier, hver med en viss positiv sannsynlighet. De mulige verdiene er oppført i **utfallssettet**.

Hver gang du **prøver** en tilfeldig variabel, trekker du en bestemt verdi fra utfallsmengden i henhold til de definerte sannsynlighetene.

La oss ta et enkelt eksempel. Anta en variabel X som er definert på følgende måte:


- X har utfallsmengden $\{1,2\}$

$$
Pr[X = 1] = 0.5
$$

$$
Pr[X = 2] = 0.5
$$

Det er lett å se at $X$ er en tilfeldig variabel. For det første finnes det to eller flere mulige verdier som $X$ kan anta, nemlig $1$ og $2$. For det andre har hver av de mulige verdiene en positiv sannsynlighet for å inntreffe når du tar et utvalg av $X$, nemlig $0,5$.

Alt en tilfeldig variabel krever, er en utfallsmengde med to eller flere muligheter, der hver mulighet har en positiv sannsynlighet for å inntreffe ved prøvetaking. I prinsippet kan en tilfeldig variabel altså defineres abstrakt, uten noen kontekst. I dette tilfellet kan du tenke på "prøvetaking" som å gjennomføre et naturlig eksperiment for å bestemme verdien av den tilfeldige variabelen.

Variabelen $X$ ovenfor ble definert abstrakt. Du kan derfor tenke på prøvetaking av variabelen $X$ ovenfor som å kaste en rettferdig mynt og tildele "2" i tilfelle kron og "1" i tilfelle mynt. For hvert utvalg av $X$ kaster du mynten på nytt.

Alternativt kan du også tenke på prøvetaking av $X$ som å kaste en rettferdig terning og tildele "2" hvis terningen lander på $1$, $3$ eller $4$, og tildele "1" hvis terningen lander på $2$, $5$ eller $6$. Hver gang du prøver $X$, kaster du terningen på nytt.

Egentlig kan man tenke seg et hvilket som helst naturlig eksperiment som gjør det mulig å definere sannsynlighetene for de mulige verdiene av $X$ ovenfor med hensyn til tegningen.

Ofte introduseres imidlertid ikke tilfeldige variabler bare abstrakt. I stedet har settet av mulige utfallsverdier en eksplisitt betydning i den virkelige verden (snarere enn bare som tall). I tillegg kan disse utfallsverdiene være definert i forhold til en bestemt type eksperiment (i stedet for som et hvilket som helst naturlig eksperiment med disse verdiene).

La oss nå se på et eksempel på en variabel $X$ som ikke er definert abstrakt. X defineres på følgende måte for å avgjøre hvilket av to lag som starter en fotballkamp:


- $X$ har utfallsmengden {rød starter,blå starter}
- Slå en bestemt mynt $C$: mynt = "rød sparker av"; krone = "blå sparker av"

$$
Pr [X = \text{red kicks off}] = 0.5
$$

$$
Pr [X = \text{blue kicks off}] = 0.5
$$

I dette tilfellet er utfallsmengden til X gitt en konkret betydning, nemlig hvilket lag som starter i en fotballkamp. I tillegg er de mulige utfallene og deres tilhørende sannsynligheter bestemt av et konkret eksperiment, nemlig å kaste en bestemt mynt $C$.

I diskusjoner om kryptografi introduseres tilfeldige variabler vanligvis mot en utfallsmengde som har betydning i den virkelige verden. Det kan være mengden av alle meldinger som kan krypteres, kjent som meldingsrommet, eller mengden av alle nøkler som partene som bruker krypteringen, kan velge mellom, kjent som nøkkelrommet.

I diskusjoner om kryptografi defineres imidlertid tilfeldige variabler vanligvis ikke i forhold til et bestemt naturlig eksperiment, men i forhold til ethvert eksperiment som kan gi de riktige sannsynlighetsfordelingene.

Tilfeldige variabler kan ha diskrete eller kontinuerlige sannsynlighetsfordelinger. Tilfeldige variabler med en **diskret sannsynlighetsfordeling** - det vil si diskrete tilfeldige variabler - har et begrenset antall mulige utfall. Den tilfeldige variabelen $X$ i begge eksemplene som er gitt så langt, var diskret.

**Kontinuerlige tilfeldige variabler** kan i stedet anta verdier i ett eller flere intervaller. Du kan for eksempel si at en tilfeldig variabel ved prøvetaking vil anta en hvilken som helst reell verdi mellom 0 og 1, og at hvert reelle tall i dette intervallet er like sannsynlig. Innenfor dette intervallet finnes det uendelig mange mulige verdier.

For kryptografiske diskusjoner trenger du bare å forstå diskrete tilfeldige variabler. Alle diskusjoner om tilfeldige variabler heretter skal derfor forstås som diskrete tilfeldige variabler, med mindre noe annet er spesifikt angitt.

### Grafisk fremstilling av tilfeldige variabler

De mulige verdiene og tilhørende sannsynlighetene for en tilfeldig variabel kan enkelt visualiseres ved hjelp av en graf. Ta for eksempel den tilfeldige variabelen $X$ fra forrige avsnitt med et utfallssett på $\{1, 2\}$, og $Pr [X = 1] = 0,5$ og $Pr [X = 2] = 0,5$. Vi vil vanligvis vise en slik tilfeldig variabel i form av et søylediagram som i *Figur 1*.

*Figur 1: Tilfeldig variabel X*

![Figure 1: Random variable X.](assets/Figure2-1.webp)

De brede søylene i *Figur 1* er selvsagt ikke ment å antyde at den tilfeldige variabelen $X$ faktisk er kontinuerlig. I stedet er søylene gjort brede for å være mer visuelt tiltalende (bare en linje rett opp gir en mindre intuitiv visualisering).

### Ensartede variabler

I uttrykket "tilfeldig variabel" betyr begrepet "tilfeldig" bare "probabilistisk". Med andre ord betyr det bare at to eller flere mulige utfall av variabelen inntreffer med en viss sannsynlighet. Disse utfallene trenger imidlertid *ikke nødvendigvis* å være like sannsynlige (selv om begrepet "tilfeldig" faktisk kan ha den betydningen i andre sammenhenger).

En **uniform variabel** er et spesialtilfelle av en tilfeldig variabel. Den kan anta to eller flere verdier, alle med samme sannsynlighet. Den tilfeldige variabelen $X$ i *Figur 1* er helt klart en uniform variabel, ettersom begge de mulige utfallene inntreffer med sannsynligheten $0,5$. Det finnes imidlertid mange tilfeldige variabler som ikke er forekomster av uniforme variabler.

Tenk for eksempel på den tilfeldige variabelen $Y$. Den har et utfallssett $\{1, 2, 3, 8, 10\}$ og følgende sannsynlighetsfordeling:

$$
\Pr[Y = 1] = 0.25
$$

$$
\Pr[Y = 2] = 0.35
$$

$$
\Pr[Y = 3] = 0.1
$$

$$
\Pr[Y = 8] = 0.25
$$

$$
\Pr[Y = 10] = 0.05
$$

Selv om to mulige utfall faktisk har like stor sannsynlighet for å inntreffe, nemlig $1$ og $8$, kan $Y$ også anta visse verdier med andre sannsynligheter enn $0,25$ ved prøvetaking. Selv om $Y$ faktisk er en tilfeldig variabel, er den altså ikke en uniform variabel.

En grafisk fremstilling av $Y$ er vist i *Figur 2*.

*Figur 2: Tilfeldig variabel Y*

![Figure 2: Random variable Y.](assets/Figure2-2.webp "Figure 2: Random variable Y")

Et siste eksempel er den tilfeldige variabelen Z. Den har utfallsmengden {1,3,7,11,12} og følgende sannsynlighetsfordeling:

$$
\Pr[Z = 2] = 0.2
$$

$$
\Pr[Z = 3] = 0.2
$$

$$
\Pr[Z = 9] = 0.2
$$

$$
\Pr[Z = 11] = 0.2
$$

$$
\Pr[Z = 12] = 0.2
$$

Du kan se det avbildet i *Figur 3*. Den tilfeldige variabelen Z er, i motsetning til Y, en uniform variabel, ettersom alle sannsynlighetene for de mulige verdiene ved prøvetaking er like store.

*Figur 3: Tilfeldig variabel Z*

![Figure 3: Random variable Z.](assets/Figure2-3.webp "Figure 3: Random variable Z")

### Betinget sannsynlighet

Anta at Bob har til hensikt å velge en dag fra det siste kalenderåret. Hva er sannsynligheten for at den valgte dagen er en sommerdag?

Så lenge vi tror at Bobs prosess faktisk vil være helt uniform, bør vi konkludere med at det er 1/4 sannsynlighet for at Bob velger en dag om sommeren. Dette er den **ubetingede sannsynligheten** for at den tilfeldig valgte dagen er en sommerdag.

Anta nå at Bob i stedet for å trekke en kalenderdag jevnt, bare velger jevnt blant de dagene der middagstemperaturen ved Crystal Lake (New Jersey) var 21 grader Celcius eller høyere. Gitt denne tilleggsinformasjonen, hva kan vi da si om sannsynligheten for at Bob velger en sommerdag?

Vi burde egentlig trekke en annen konklusjon enn tidligere, selv uten ytterligere spesifikk informasjon (f.eks. temperaturen ved middagstid hver dag i forrige kalenderår).

Når vi vet at Crystal Lake ligger i New Jersey, kan vi ikke forvente at temperaturen midt på dagen vil være 21 grader Celsius eller høyere om vinteren. I stedet er det mye mer sannsynlig at det er en varm dag om våren eller høsten, eller en dag et sted om sommeren. Når vi vet at temperaturen ved Crystal Lake på den valgte dagen var 21 grader Celsius eller høyere, blir sannsynligheten for at den dagen Bob velger, er en sommerdag, mye høyere. Dette er den **betingede sannsynligheten** for at den tilfeldig valgte dagen er en sommerdag, gitt at middagstemperaturen ved Crystal Lake var 21 grader Celsius eller høyere.

I motsetning til i det forrige eksempelet kan sannsynligheten for to hendelser også være helt uavhengig av hverandre. I så fall sier vi at de er **uavhengige**.

Anta for eksempel at en viss mynt har slått krone. Hva er da sannsynligheten for at det vil regne i morgen, gitt dette faktumet? Den betingede sannsynligheten bør i dette tilfellet være den samme som den ubetingede sannsynligheten for at det vil regne i morgen, ettersom et myntkast generelt ikke har noen innvirkning på været.

Vi bruker et "|"-symbol for å skrive ut betingede sannsynlighetssetninger. For eksempel kan sannsynligheten for hendelse $A$ gitt at hendelse $B$ har inntruffet, skrives på følgende måte:

$$
Pr[A|B]
$$

Så når to hendelser, $A$ og $B$, er uavhengige, så:

$$
Pr[A|B] = Pr[A] \text{ and } Pr[B|A] = Pr[B]
$$

Betingelsen for uavhengighet kan forenkles på følgende måte:

$$
Pr[A, B] = Pr[A] \cdot Pr[B]
$$

Et sentralt resultat i sannsynlighetsteori er kjent som **Bayes teorem**. Det sier i utgangspunktet at $Pr[A|B]$ kan omskrives på følgende måte:

$$
Pr[A|B] = \frac{Pr[B|A] \cdot Pr[A]}{Pr[B]}
$$

I stedet for å bruke betingede sannsynligheter for spesifikke hendelser, kan vi også se på betingede sannsynligheter for to eller flere tilfeldige variabler over et sett med mulige hendelser. Anta to tilfeldige variabler, $X$ og $Y$. Vi kan betegne enhver mulig verdi for $X$ med $x$, og enhver mulig verdi for $Y$ med $y$. Vi kan da si at to tilfeldige variabler er uavhengige hvis følgende utsagn holder:

$$
Pr[X = x, Y = y] = Pr[X = x] \cdot Pr[Y = y]
$$

for alle $x$ og $y$.

La oss være litt mer eksplisitte om hva dette utsagnet betyr.

Anta at utfallssettene for $X$ og $Y$ er definert som følger: **X** = $\{x_1, x_2, \ldots, x_i, \ldots, x_n\}$ og **Y** = $\{y_1, y_2, \ldots, y_i, \ldots, y_m\}$. (Det er vanlig å angi verdisett med store bokstaver med fet skrift)

Anta nå at du tar et utvalg $Y$ og observerer $y_1$. Utsagnet ovenfor forteller oss at sannsynligheten for at vi nå får $x_1$ fra et utvalg av $X$ er nøyaktig den samme som om vi aldri hadde observert $y_1$. Dette gjelder for alle $y_i$ vi kunne ha trukket fra vårt opprinnelige utvalg av $Y$. Til slutt, dette gjelder ikke bare for $x_1$. For enhver $x_i$ påvirkes ikke sannsynligheten for at den inntreffer av utfallet av en prøvetaking av $Y$. Alt dette gjelder også for tilfellet der $X$ samples først.

La oss avslutte diskusjonen med et litt mer filosofisk poeng. I enhver situasjon i den virkelige verden blir sannsynligheten for en hendelse alltid vurdert på bakgrunn av et bestemt sett med informasjon. Det finnes ingen "ubetinget sannsynlighet" i streng forstand.

Tenk deg for eksempel at jeg spør deg om sannsynligheten for at griser kommer til å fly innen 2030. Selv om jeg ikke gir deg ytterligere informasjon, vet du åpenbart mye om verden som kan påvirke din vurdering. Du har aldri sett griser fly. Du vet at folk flest ikke forventer at de skal kunne fly. Du vet at de egentlig ikke er bygget for å fly. Og så videre.

Når vi snakker om "ubetinget sannsynlighet" for en eller annen hendelse i en virkelig kontekst, kan dette begrepet derfor bare ha mening hvis vi forstår det som "sannsynligheten uten ytterligere eksplisitt informasjon". Enhver forståelse av en "betinget sannsynlighet" bør derfor alltid forstås i lys av en eller annen spesifikk informasjon.

Jeg kan for eksempel spørre deg om sannsynligheten for at griser kommer til å fly innen 2030, etter at jeg har gitt deg bevis på at noen geiter på New Zealand har lært seg å fly etter noen års trening. I så fall vil du sannsynligvis justere din vurdering av sannsynligheten for at grisene kommer til å fly innen 2030. Sannsynligheten for at griser vil fly innen 2030, er altså betinget av dette beviset om geiter på New Zealand.

## Modulo-operasjonen

<chapterId>709b34e5-b155-53d2-abbd-97d67e56db00</chapterId>

### Modulo

Det mest grunnleggende uttrykket med **modulo-operasjonen** er av følgende form: $x \mod y$.

Variabelen $x$ kalles dividenden og variabelen $y$ divisoren. For å utføre en modulooperasjon med en positiv dividende og en positiv divisor, bestemmer du bare resten av divisjonen.

Se for eksempel på uttrykket $25 \mod 4$. Tallet 4 går inn i tallet 25 totalt 6 ganger. Resten av denne divisjonen er 1. Derfor er $25 \mod 4$ lik 1. På samme måte kan vi evaluere uttrykkene nedenfor:


- $29 \mod 30 = 29$ (ettersom 30 går inn i 29 totalt 0 ganger og resten er 29)
- $42 \mod 2 = 0$ (ettersom 2 går inn i 42 totalt 21 ganger og resten er 0)
- $12 \mod 5 = 2$ (ettersom 5 går inn i 12 totalt 2 ganger og resten er 2)
- $20 \mod 8 = 4$ (ettersom 8 går inn i 20 totalt 2 ganger og resten er 4)

Når dividenden eller divisoren er negativ, kan modulooperasjoner håndteres annerledes av programmeringsspråk.

Du vil garantert støte på tilfeller med negativt utbytte i kryptografi. I disse tilfellene er den typiske fremgangsmåten som følger:


- Finn først den nærmeste verdien *lavere enn eller lik* dividenden som divisoren deler med en rest på null. Kall denne verdien $p$.
- Hvis dividenden er $x$, er resultatet av modulo-operasjonen verdien av $x - p$.

Anta for eksempel at dividenden er $-20$ og divisoren 3. Den nærmeste verdien lavere enn eller lik $-20$ som 3 deler jevnt i, er $-21$. Verdien av $x - p$ er i dette tilfellet $-20 - (-21)$. Dette er lik 1, og dermed er $-20 \mod 3$ lik 1. På samme måte kan vi evaluere uttrykkene nedenfor:


- $-8 \mod 5 = 2$
- $-19 \mod 16 = 13$
- $-14 \mod 6 = 4$

Når det gjelder notasjon, vil du typisk se følgende typer uttrykk: $x = [y \mod z]$. På grunn av parentesene gjelder modulo-operasjonen i dette tilfellet bare for høyresiden av uttrykket. Hvis $y$ er lik 25 og $z$ er lik 4, for eksempel, blir $x$ evaluert til 1.

Uten parenteser virker modulo-operasjonen på *begge sider* av et uttrykk. Anta for eksempel følgende uttrykk: $x = y \mod z$. Hvis $y$ er lik 25 og $z$ er lik 4, vet vi bare at $x \mod 4$ evalueres til 1. Dette er konsistent med en hvilken som helst verdi for $x$ fra mengden $\{\ldots,-7, -3, 1, 5, 9,\ldots\}$.

Den grenen av matematikken som involverer modulooperasjoner på tall og uttrykk, kalles **modulær aritmetikk**. Du kan se på denne grenen som aritmetikk for tilfeller der tallinjen ikke er uendelig lang. Selv om vi vanligvis støter på modulooperasjoner for (positive) heltall innen kryptografi, kan du også utføre modulooperasjoner med alle reelle tall.

### Shift-krypteringen

Modulo-operasjonen er ofte brukt innen kryptografi. For å illustrere dette kan vi ta for oss et av de mest kjente krypteringsskjemaene i historien: shift-chifferet.

La oss først definere den. Anta at vi har en ordbok *D* som sidestiller alle bokstavene i det engelske alfabetet, i rekkefølge, med tallmengden $\{0, 1, 2, \ldots, 25\}$. Anta et meldingsrom **M**. **shift cipher** er da et krypteringsskjema som er definert som følger:


- Velg en nøkkel $k$ fra nøkkelrommet **K**, hvor **K** = $\{0, 1, 2, \ldots, 25\}$ [1]
- Krypter en melding $m \in \mathbf{M}$ på følgende måte:
    - Separer $m$ i de enkelte bokstavene $m_0, m_1, \ldots, m_i, \ldots, m_l$
    - Konverter hver $m_i$ til et tall i henhold til *D*
    - For hver $m_i$, $c_i = [(m_i + k) \mod 26]$
    - Konverter hver $c_i$ til en bokstav i henhold til *D*
    - Kombiner deretter $c_0, c_1, \ldots, c_l$ for å få krypteringsteksten $c$
- Dekrypter en krypteringstekst $c$ på følgende måte:
    - Konverter hver $c_i$ til et tall i henhold til *D*
    - For hver $c_i$, $m_i = [(c_i - k) \mod 26]$
    - Konverter hver $m_i$ til en bokstav i henhold til *D*
    - Kombiner deretter $m_0, m_1, \ldots, m_l$ for å få den opprinnelige meldingen $m$

Modulooperatoren i skiftchiffreringen sørger for at bokstavene brytes rundt, slik at alle bokstavene i chifferteksten blir definert. For å illustrere dette kan vi se på anvendelsen av shift-chiffer på ordet "DOG".

Anta at du har valgt en nøkkel med verdien 17. Bokstaven "O" tilsvarer 15. Uten modulo-operasjonen ville addisjonen av dette klarteksttallet og nøkkelen gitt et chifferteksttall på 32. Dette chifferteksttallet kan imidlertid ikke gjøres om til en chifferbokstav, ettersom det engelske alfabetet bare har 26 bokstaver. Modulo-operasjonen sikrer at chifferteksttallet faktisk er 6 (resultatet av $32 \mod 26$), noe som tilsvarer chiffertekstbokstaven "G".

Hele krypteringen av ordet "DOG" med nøkkelverdien 17 er som følger:


- Melding = DOG = D,O,G = 3,15,6
- $c_0 = [(3 + 17) \mod 26] = [(20) \mod 26] = 20 = U$
- $c_1 = [(15 + 17) \mod 26] = [(32) \mod 26] = 6 = G$
- $c_2 = [(6 + 17) \mod 26] = [(23) \mod 26] = 23 = X$
- $c = UGX$

Alle kan intuitivt forstå hvordan shift-chifferet fungerer og sannsynligvis bruke det selv. For å utvikle kunnskapen din om kryptografi er det imidlertid viktig å begynne å bli mer komfortabel med formalisering, ettersom skjemaene vil bli mye vanskeligere. Derfor ble trinnene for skiftchifferet formalisert.

**Noter:**

[1] Vi kan definere dette utsagnet nøyaktig ved å bruke terminologien fra forrige avsnitt. La en uniform variabel $K$ ha $K$ som sitt sett av mulige utfall. Det vil si

$$
Pr[K = 0] = \frac{1}{26}
$$

$$
Pr[K = 1] = \frac{1}{26}
$$

...og så videre. Sample den uniforme variabelen $K$ én gang for å få en bestemt nøkkel.

## XOR-operasjonen

<chapterId>22f185cc-c516-5b33-950b-0908f2f881fe</chapterId>

Alle datamaskindata behandles, lagres og sendes over nettverk på bitnivå. Alle kryptografiske systemer som brukes på datamaskindata, opererer også på bitnivå.

Anta for eksempel at du har skrevet en e-post i e-postprogrammet ditt. Krypteringen du bruker, skjer ikke direkte på ASCII-tegnene i e-posten. I stedet brukes den på bit-representasjonen av bokstavene og andre symboler i e-posten.

En matematisk operasjon som er viktig å forstå i moderne kryptografi, i tillegg til modulo-operasjonen, er **XOR-operasjonen**, eller "eksklusiv eller"-operasjonen. Denne operasjonen tar to biter som input og gir en annen bit som output. XOR-operasjonen betegnes ganske enkelt som "XOR". Den gir 0 hvis de to bitene er like, og 1 hvis de to bitene er forskjellige. Du kan se de fire mulighetene nedenfor. Symbolet $\oplus$ representerer "XOR":


- $0 \oplus 0 = 0$
- $0 \oplus 1 = 1$
- $1 \oplus 0 = 1$
- $1 \oplus 1 = 0$

For å illustrere dette kan vi anta at du har en melding $m_1$ (01111001) og en melding $m_2$ (01011001). XOR-operasjonen av disse to meldingene kan ses nedenfor.


- $m_1 \oplus m_2 = 01111001 \oplus 01011001 = 00100000$$

Prosessen er enkel. Du XOR'er først bitene lengst til venstre i $m_1$ og $m_2$. I dette tilfellet er det $0 \oplus 0 = 0$. Deretter XOR-ODER du det andre paret av biter fra venstre. I dette tilfellet er det $1 \oplus 1 = 0$. Du fortsetter denne prosessen til du har utført XOR-operasjonen på bitene lengst til høyre.

Det er lett å se at XOR-operasjonen er kommutativ, nemlig at $m_1 \oplus m_2 = m_2 \oplus m_1$. I tillegg er XOR-operasjonen også assosiativ. Det vil si at $(m_1 \oplus m_2) \oplus m_3 = m_1 \oplus (m_2 \oplus m_3)$.

En XOR-operasjon på to strenger av ulik lengde kan tolkes på ulike måter, avhengig av konteksten. Vi skal ikke her ta for oss XOR-operasjoner på strenger av ulik lengde.

En XOR-operasjon tilsvarer spesialtilfellet med å utføre en modulooperasjon på addisjonen av biter når divisoren er 2. Du kan se ekvivalensen i de følgende resultatene:


- $(0 + 0) \mod 2 = 0 \oplus 0 = 0$$
- $(1 + 0) \mod 2 = 1 \oplus 0 = 1$$
- $(0 + 1) \mod 2 = 0 \oplus 1 = 1$$
- $(1 + 1) \mod 2 = 1 \oplus 1 = 0$$

## Pseudotilfeldighet

<chapterId>20463fc5-3e92-581f-a1b7-3151279bd95e</chapterId>

I diskusjonen om tilfeldige og uniforme variabler skilte vi spesifikt mellom "tilfeldig" og "uniform". Dette skillet opprettholdes vanligvis i praksis når man beskriver tilfeldige variabler. I vår nåværende sammenheng er det imidlertid nødvendig å droppe dette skillet, og "tilfeldig" og "uniform" brukes synonymt. Jeg vil forklare hvorfor på slutten av avsnittet.

Til å begynne med kan vi kalle en binær streng av lengde $n$ **tilfeldig** (eller **uniform**) hvis den er resultatet av et utvalg av en uniform variabel $S$ som gir hver binær streng av en slik lengde $n$ like stor sannsynlighet for å bli valgt.

Anta for eksempel mengden av alle binære strenger med lengde 8: $\{0000\ 0000, 0000\ 0001, \ldots, 1111\ 1111\}$. (Det er vanlig å skrive en 8-biters streng i to kvartetter, hver kalt en **nibble**) La oss kalle dette settet av strenger **$S_8$**.

I henhold til definisjonen ovenfor kan vi kalle en bestemt binær streng med lengde 8 tilfeldig (eller uniform) hvis den er resultatet av et utvalg av en uniform variabel $S$$ som gir hver streng i **$S_8$** like stor sannsynlighet for å bli valgt. Gitt at mengden **$S_8$** inneholder $2^8$ elementer, må sannsynligheten for utvelgelse ved prøvetaking være $1/2^8$ for hver streng i mengden.

Et viktig aspekt ved tilfeldigheten til en binær streng er at den er definert med referanse til prosessen den ble valgt ut gjennom. Formen til en bestemt binær streng i seg selv sier derfor ingenting om hvor tilfeldig den ble valgt ut.

Mange tenker intuitivt at en streng som $1111\ 1111$ for eksempel ikke kan ha blitt valgt tilfeldig. Men dette er helt klart feil.

Hvis vi definerer en uniform variabel $S$ over alle binære strenger med lengde 8, er sannsynligheten for å velge $1111\ 1111$ fra mengden **$S_8$** den samme som for en streng som $0111\ 0100$. Du kan altså ikke si noe om hvor tilfeldig en streng er, bare ved å analysere selve strengen.

Vi kan også snakke om tilfeldige strenger uten å mene binære strenger. Vi kan for eksempel snakke om en tilfeldig hex-streng $AF\\ 02\ 82$. I dette tilfellet ville strengen ha blitt valgt tilfeldig fra mengden av alle hex-strenger med lengde 6. Dette tilsvarer å tilfeldig velge en binær streng med lengde 24, ettersom hvert hex-sifret representerer 4 bits.

Vanligvis refererer uttrykket "en tilfeldig streng", uten forbehold, til en streng som er tilfeldig valgt fra mengden av alle strenger med samme lengde. Det er slik jeg har beskrevet det ovenfor. En streng med lengden $n$ kan selvfølgelig også velges tilfeldig fra en annen mengde. For eksempel en som bare utgjør en delmengde av alle strengene med lengde $n$, eller kanskje en mengde som inneholder strenger av varierende lengde. I slike tilfeller vil vi imidlertid ikke kalle det en "tilfeldig streng", men heller "en streng som er tilfeldig valgt fra en mengde **S**".

Et nøkkelbegrep innen kryptografi er pseudotilfeldighet. En **pseudotil tilfeldig streng** av lengde $n$ ser ut *som* den er resultatet av et utvalg av en uniform variabel $S$ som gir hver streng i **$S_n$** like stor sannsynlighet for å bli valgt. I virkeligheten er strengen imidlertid resultatet av et utvalg av en uniform variabel $S'$ som bare definerer en sannsynlighetsfordeling - ikke nødvendigvis en med like sannsynligheter for alle mulige utfall - på en delmengde av **$S_n$**. Det avgjørende poenget her er at ingen egentlig kan skille mellom prøver fra $S$ og $S'$, selv om du tar mange av dem.

Anta for eksempel en tilfeldig variabel $S$. Utfallssettet er **$S_{256}$**, som er settet av alle binære strenger med lengde 256. Dette settet har $2^{256}$ elementer. Hvert element har like stor sannsynlighet for å bli valgt, $1/2^{256}$, ved prøvetaking.

Anta i tillegg en tilfeldig variabel $S'$. Utfallssettet inkluderer bare $2^{128}$ binære strenger med lengde 256. Den har en viss sannsynlighetsfordeling over disse strengene, men denne fordelingen er ikke nødvendigvis uniform.

Anta at jeg nå har tatt 1000 stikkprøver fra $S$ og 1000 stikkprøver fra $S'$ og gitt deg de to settene med resultater. Jeg forteller deg hvilket sett med utfall som er knyttet til hvilken tilfeldig variabel. Deretter tar jeg et utvalg fra en av de to tilfeldige variablene. Men denne gangen forteller jeg deg ikke hvilken tilfeldig variabel jeg tar et utvalg fra. Hvis $S'$ var pseudotilfeldige, er tanken at sannsynligheten for at du gjetter riktig med hensyn til hvilken tilfeldig variabel jeg har valgt, praktisk talt ikke er bedre enn $1/2$.

En pseudotilfeldige streng av lengde $n$ produseres vanligvis ved å velge en tilfeldig streng av størrelse $n - x$, der $x$ er et positivt heltall, og bruke den som input til en ekspanderende algoritme. Denne tilfeldige strengen av størrelsen $n - x$ kalles **frøet**.

Pseudotilfeldige strenger er et nøkkelkonsept for å gjøre kryptografi praktisk. Tenk for eksempel på stream ciphers. Med en strømkryptering kobles en tilfeldig valgt nøkkel til en ekspanderende algoritme for å produsere en mye større pseudotilfeldige streng. Denne pseudotilfeldige strengen kombineres deretter med klarteksten via en XOR-operasjon for å produsere en chiffertekst.

Hvis vi ikke kunne produsere denne typen pseudotilfeldige strenger for en stream cipher, ville vi trenge en nøkkel som er like lang som meldingen for å sikre den. Dette er i de fleste tilfeller ikke et særlig praktisk alternativ.

Begrepet pseudotilfeldighet som diskuteres i dette avsnittet, kan defineres mer formelt. Det kan også brukes i andre sammenhenger. Men vi trenger ikke å gå inn på den diskusjonen her. Alt du egentlig trenger å forstå intuitivt for mye av kryptografien, er forskjellen mellom en tilfeldig og en pseudotil tilfeldig streng. [2]

Grunnen til at vi har droppet skillet mellom "tilfeldig" og "uniform" i diskusjonen vår, bør nå også være klar. I praksis bruker alle begrepet pseudotilfeldige for å betegne en streng som ser ut **som om** den er resultatet av et utvalg av en uniform variabel $S$. Strengt tatt burde vi kalle en slik streng for "pseudouniform", slik vi brukte tidligere. Siden begrepet "pseudouniform" både er klumpete og ikke brukes av noen, vil vi ikke introdusere det her for klarhetens skyld. I stedet dropper vi bare skillet mellom "tilfeldig" og "uniform" i denne sammenhengen.

**Noter**

[2] Hvis du er interessert i en mer formell fremstilling av disse spørsmålene, kan du lese Katz og Lindells *Introduction to Modern Cryptography*, spesielt kapittel 3.

# Matematisk grunnlag for kryptografi 2

<partId>d7245cc9-bb6d-5403-b3d5-9c703d9a2f81</partId>

## Hva er tallteori?

<chapterId>c0051c34-fd5d-539c-93e2-5c6dfd4c3355</chapterId>

Dette kapittelet tar for seg et mer avansert emne innen kryptografiens matematiske grunnlag: tallteori. Selv om tallteori er viktig for symmetrisk kryptografi (for eksempel i Rijndael-krypteringen), er den spesielt viktig i kryptografi med offentlig nøkkel.

Hvis du synes detaljene i tallteorien er tungvint, vil jeg anbefale deg å lese på et høyt nivå første gang. Du kan alltid komme tilbake til det på et senere tidspunkt.

___

Du kan karakterisere **tallteori** som studiet av egenskapene til heltall og matematiske funksjoner som arbeider med heltall.

Tenk for eksempel på at to tall $a$ og $N$ er **koprim** (eller **relative primtal**) hvis deres største felles divisor er lik 1. Anta nå et bestemt heltall $N$. Hvor mange heltall mindre enn $N$ er koprim med $N$? Kan vi si noe generelt om svarene på dette spørsmålet? Dette er typiske spørsmål som tallteorien søker å besvare.

Moderne tallteori baserer seg på verktøyene i abstrakt algebra. Feltet **abstrakt algebra** er en underdisiplin av matematikken der de viktigste analyseobjektene er abstrakte objekter kjent som algebraiske strukturer. En **algebraisk struktur** er et sett av elementer som oppfyller visse aksiomer, og som er forbundet med én eller flere operasjoner. Ved hjelp av algebraiske strukturer kan matematikere få innsikt i spesifikke matematiske problemer ved å abstrahere fra detaljene i dem.

Feltet abstrakt algebra kalles også moderne algebra. Du kan også støte på begrepet **abstrakt matematikk** (eller **ren matematikk**). Sistnevnte begrep er ikke en referanse til abstrakt algebra, men betyr snarere studiet av matematikk for matematikkens egen skyld, og ikke bare med tanke på potensielle anvendelser.

Mengdene fra abstrakt algebra kan håndtere mange typer objekter, fra formbevarende transformasjoner på en likesidet trekant til tapetmønstre. I tallteori ser vi bare på mengder av elementer som inneholder heltall eller funksjoner som fungerer med heltall.

## Grupper

<chapterId>3209b270-f9cd-5224-803e-0ed19fbf7826</chapterId>

Et grunnleggende begrep i matematikken er en mengde av elementer. En mengde betegnes vanligvis med akkolade-tegn med elementene atskilt med komma.

For eksempel er mengden av alle heltall $\{..., -2, -1, 0, 1, 2, ...\}$. Ellipsene her betyr at et bestemt mønster fortsetter i en bestemt retning. Mengden av alle heltall inkluderer altså også $3, 4, 5, 6$ og så videre, i tillegg til $-3, -4, -5, -6$ og så videre. Denne mengden av alle heltall betegnes vanligvis med $\mathbb{Z}$.

Et annet eksempel på en mengde er $\mathbb{Z} \mod 11$, eller mengden av alle heltall modulo 11. I motsetning til hele mengden $\mathbb{Z}$ inneholder denne mengden bare et begrenset antall elementer, nemlig $\{0, 1, \ldots, 9, 10\}$.

En vanlig feil er å tro at mengden $\mathbb{Z} \mod 11$ faktisk er $\{-10, -9, \ldots, 0, \ldots, 9, 10\}$. Men dette er ikke tilfelle, gitt måten vi definerte modulooperasjonen på tidligere. Alle negative heltall som reduseres med modulo 11, går inn i $\{0, 1, \ldots, 9, 10\}$. For eksempel vil uttrykket $-2 \mod 11$ omsluttes av $9$, mens uttrykket $-27 \mod 11$ omsluttes av $5$.

Et annet grunnleggende begrep i matematikken er binære operasjoner. Dette er alle operasjoner som tar to elementer for å produsere et tredje. Fra grunnleggende aritmetikk og algebra er du for eksempel kjent med fire grunnleggende binære operasjoner: addisjon, subtraksjon, multiplikasjon og divisjon.

Disse to grunnleggende matematiske begrepene, mengder og binære operasjoner, brukes til å definere begrepet gruppe, som er den viktigste strukturen i abstrakt algebra.

Nærmere bestemt, anta en binær operasjon $\circ$. I tillegg antar vi at en mengde elementer **S** er utstyrt med denne operasjonen. Alt "utstyrt" betyr her at operasjonen $\circ$ kan utføres mellom to elementer i mengden **S**.

Kombinasjonen $\langle \mathbf{S}, \circ \rangle$ er altså en **gruppe** hvis den oppfyller fire spesifikke betingelser, kjent som gruppeaksiomene.

1. For alle $a$ og $b$ som er elementer av $\mathbf{S}$, er $a \circ b$ også et element av $\mathbf{S}$. Dette er kjent som **lukkingsbetingelsen**.

2. For alle $a$, $b$ og $c$ som er elementer i $\mathbf{S}$, er det slik at $(a \circ b) \circ c = a \circ (b \circ c)$. Dette er kjent som **assosiativitetsbetingelsen**.

3. Det finnes et unikt element $e$ i $\mathbf{S}$, slik at for hvert element $a$ i $\mathbf{S}$ gjelder følgende likning: $e \circ a = a \circ e = a$. Siden det bare finnes ett slikt element $e$, kalles det **identitetselementet**. Denne betingelsen er kjent som **identitetsbetingelsen**.

4. For hvert element $a$ i $\mathbf{S}$ finnes det et element $b$ i $\mathbf{S}$, slik at følgende ligning gjelder: $a \circ b = b \circ a = e$, hvor $e$ er identitetselementet. Elementet $b$ er her kjent som det **inverse elementet**, og det betegnes vanligvis som $a^{-1}$. Denne betingelsen er kjent som **inversbetingelsen** eller **invertibilitetsbetingelsen**.

La oss utforske grupper litt nærmere. Betegn mengden av alle heltall med $\mathbb{Z}$. Denne mengden kombinert med standard addisjon, eller $\langle \mathbb{Z}, + \rangle$, passer helt klart til definisjonen av en gruppe, ettersom den oppfyller de fire aksiomene ovenfor.

1. For alle $x$ og $y$ som er elementer av $\mathbb{Z}$, er $x + y$ også et element av $\mathbb{Z}$. Så $\langle \mathbb{Z}, + \rangle$ oppfyller lukkingsbetingelsen.

2. For alle $x$, $y$ og $z$ som er elementer i $\mathbb{Z}$, er $(x + y) + z = x + (y + z)$. Så $\langle \mathbb{Z}, + \rangle$ oppfyller assosiativitetsbetingelsen.

3. Det finnes et identitetselement i $\langle \mathbb{Z}, + \rangle$, nemlig 0. For enhver $x$ i $\mathbb{Z}$ gjelder det nemlig at: $0 + x = x + 0 = x$. Så $\langle \mathbb{Z}, + \rangle$ oppfyller identitetsbetingelsen.

4. Til slutt, for hvert element $x$ i $\mathbb{Z}$, finnes det et $y$ slik at $x + y = y + x = 0$. Hvis $x$ for eksempel var 10, ville $y$ være $-10$ (i tilfelle $x$ er 0, er $y$ også 0). Så $\langle \mathbb{Z}, + \rangle$ oppfyller den inverse betingelsen.

Det er viktig å merke seg at det at mengden av heltall med addisjon utgjør en gruppe, ikke betyr at den utgjør en gruppe med multiplikasjon. Du kan verifisere dette ved å teste $\langle \mathbb{Z}, \cdot \rangle$ mot de fire gruppeaksiomene (hvor $\cdot$ betyr standardmultiplikasjon).

De to første aksiomene holder åpenbart. I tillegg kan elementet 1 fungere som identitetselement under multiplikasjon. Ethvert heltall $x$ multiplisert med 1 gir nemlig $x$. Imidlertid oppfyller ikke $\langle \mathbb{Z}, \cdot \rangle$ den inverse betingelsen. Det vil si at det ikke finnes et unikt element $y$ i $\mathbb{Z}$ for hver $x$ i $\mathbb{Z}$, slik at $x \cdot y = 1$.

Anta for eksempel at $x = 22$. Hvilken verdi $y$ fra mengden $\mathbb{Z}$ multiplisert med $x$ vil gi identitetselementet 1? Verdien $1/22$ ville fungere, men denne finnes ikke i mengden $\mathbb{Z}$. Faktisk støter du på dette problemet for alle heltall $x$, bortsett fra verdiene 1 og -1 (hvor $y$ må være henholdsvis 1 og -1).

Hvis vi tillater reelle tall for mengden vår, forsvinner problemene våre i stor grad. For ethvert element $x$ i mengden gir multiplikasjon med $1/x$ 1. Siden brøker er inkludert i mengden av reelle tall, kan man finne en invers for alle reelle tall. Unntaket er null, ettersom enhver multiplikasjon med null aldri vil gi identitetselementet 1. Derfor er mengden av reelle tall som ikke er null, og som er utstyrt med multiplikasjon, faktisk en gruppe.

Noen grupper oppfyller en femte generell betingelse, kjent som **kommutativitetsbetingelsen**. Denne betingelsen er som følger:


- Anta en gruppe $G$ med en mengde **S** og en binær operator $\circ$. Anta at $a$ og $b$ er elementer i **S**. Hvis det er slik at $a \circ b = b \circ a$ for to elementer $a$ og $b$ i **S**, så oppfyller $G$ kommutativitetsbetingelsen.

Enhver gruppe som oppfyller kommutativitetsbetingelsen, kalles en **kommutativ gruppe**, eller en **Abelsk gruppe** (etter Niels Henrik Abel). Det er lett å verifisere at både mengden av reelle tall over addisjon og mengden av heltall over addisjon er abelske grupper. Mengden heltall over multiplikasjon er ikke en gruppe i det hele tatt, så den kan ipso facto ikke være en abelsk gruppe. Mengden av reelle tall uten null over multiplikasjon er derimot også en abelsk gruppe.

Du bør ta hensyn til to viktige notasjonskonvensjoner. For det første vil tegnene "+" eller "×" ofte bli brukt for å symbolisere gruppeoperasjoner, selv når elementene faktisk ikke er tall. I slike tilfeller skal du ikke tolke disse tegnene som vanlig aritmetisk addisjon eller multiplikasjon. I stedet er det snakk om operasjoner som bare har en abstrakt likhet med disse aritmetiske operasjonene.

Med mindre du spesifikt refererer til aritmetisk addisjon eller multiplikasjon, er det enklere å bruke symboler som $\circ$ og $\diamond$ for gruppeoperasjoner, ettersom disse ikke har særlig kulturelt forankrede konnotasjoner.

For det andre, av samme grunn som "+" og "×" ofte brukes for å indikere ikke-aritmetiske operasjoner, blir identitetselementene i grupper ofte symbolisert med "0" og "1", selv når elementene i disse gruppene ikke er tall. Med mindre du refererer til identitetselementet i en gruppe med tall, er det enklere å bruke et mer nøytralt symbol som "$e$" for å angi identitetselementet.

Mange ulike og svært viktige verdimengder i matematikken som er utstyrt med visse binære operasjoner, er grupper. Kryptografiske anvendelser arbeider imidlertid bare med mengder av heltall eller i det minste elementer som beskrives av heltall, det vil si innenfor tallteoriens domene. Derfor brukes ikke mengder med andre reelle tall enn heltall i kryptografiske anvendelser.

La oss avslutte med å gi et eksempel på elementer som kan "beskrives av heltall", selv om de ikke er heltall. Et godt eksempel er punktene på elliptiske kurver. Selv om ethvert punkt på en elliptisk kurve åpenbart ikke er et heltall, er et slikt punkt faktisk beskrevet av to heltall.

Elliptiske kurver er for eksempel avgjørende for Bitcoin. Ethvert standard privat og offentlig Bitcoin-nøkkelpar velges fra settet av punkter som er definert av følgende elliptiske kurve:

$$
x^3 + 7 = y^2 \mod 2^{256} – 2^{32} – 29 – 28 – 27 – 26 - 24 - 1
$$

(det største primtallet mindre enn $2^{256}$). Koordinaten $x$ er den private nøkkelen, og koordinaten $y$ er din offentlige nøkkel.

Transaksjoner i Bitcoin innebærer vanligvis at utdata låses til en eller flere offentlige nøkler på en eller annen måte. Verdien fra disse transaksjonene kan deretter låses opp ved å lage digitale signaturer med de tilsvarende private nøklene.

## Sykliske grupper

<chapterId>bfa5c714-7952-5fef-88b1-ca5b07edd886</chapterId>

Et viktig skille vi kan trekke, er mellom en **endelig** og en **uendelig gruppe**. Førstnevnte har et endelig antall elementer, mens sistnevnte har et uendelig antall elementer. Antallet elementer i en endelig gruppe kalles gruppens **orden**. All praktisk kryptografi som involverer bruk av grupper, baserer seg på endelige (tallteoretiske) grupper.

Innenfor offentlig nøkkelkryptografi er en bestemt klasse av endelige abelske grupper, såkalte sykliske grupper, spesielt viktige. For å forstå sykliske grupper må vi først forstå begrepet eksponentiering av gruppeelementer.

Anta en gruppe $G$ med en gruppeoperasjon $\circ$, og at $a$ er et element i $G$. Uttrykket $a^n$ skal da tolkes som elementet $a$ kombinert med seg selv totalt $n - 1$ ganger. For eksempel betyr $a^2$ $a \circ a$, $a^3$ betyr $a \circ a \circ a$, og så videre. (Merk at eksponentiering her ikke nødvendigvis er eksponentiering i standard aritmetisk forstand)

La oss se på et eksempel. Anta at $G = \langle \mathbb{Z} \mod 7, + \rangle$, og at vår verdi for $a$ er lik 4. I dette tilfellet er $a^2 = [4 + 4 \mod 7] = [8 \mod 7] = 1 \mod 7$. Alternativt vil $a^4$ representere $[4 + 4 + 4 + 4 + 4 \mod 7] = [16 \mod 7] = 2 \mod 7$.

Noen abelske grupper har ett eller flere elementer som kan gi alle andre gruppeelementer gjennom fortsatt eksponentiering. Disse elementene kalles **generatorer** eller **primitive elementer**.

En viktig klasse av slike grupper er $\langle \mathbb{Z}^* \mod N, \cdot \rangle$, hvor $N$ er et primtall. Notasjonen $\mathbb{Z}^*$ betyr her at gruppen inneholder alle positive heltall som er mindre enn $N$. En slik gruppe har derfor alltid $N - 1$ elementer.

Tenk for eksempel på $G = \langle \mathbb{Z}^* \mod 11, \cdot \rangle$. Denne gruppen har følgende elementer: $\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$. Rekkefølgen til denne gruppen er 10 (som faktisk er lik $11 - 1$).

La oss utforske eksponentiering av elementet 2 fra denne gruppen. Beregningene opp til $2^{12}$ er vist nedenfor. Legg merke til at eksponenten på venstre side av ligningen refererer til eksponentiering av gruppeelementer. I vårt eksempel innebærer dette aritmetisk eksponentiering på høyre side av ligningen (men det kunne også ha involvert f.eks. addisjon). For å gjøre det tydeligere har jeg skrevet ut den gjentatte operasjonen, og ikke eksponentformen på høyresiden.


- $2^1 = 2 \mod 11$
- $2^2 = 2 \cdot 2 \mod 11 = 4 \mod 11$$
- $2^3 = 2 \cdot 2 \cdot 2 \mod 11 = 8 \mod 11$$
- $2^4 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 16 \mod 11 = 5 \mod 11$
- $2^5 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 32 \mod 11 = 10 \mod 11$
- $2^6 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 64 \mod 11 = 9 \mod 11$
- $2^7 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 128 \mod 11 = 7 \mod 11$
- $2^8 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 256 \mod 11 = 3 \mod 11$$
- $2^9 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 512 \mod 11 = 6 \mod 11$
- $2^{10} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 1024 \mod 11 = 1 \mod 11$
- $2^{11} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 2048 \mod 11 = 2 \mod 11$
- $2^{12} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 4096 \mod 11 = 4 \mod 11$

Hvis du ser nøye etter, kan du se at eksponentiering av elementet 2 går gjennom alle elementene i $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ i følgende rekkefølge: 2, 4, 8, 5, 10, 9, 7, 3, 6, 1. Etter $2^{10}$ vil fortsatt eksponentiering av elementet 2 sykle gjennom alle elementene igjen og i samme rekkefølge. Derfor er elementet 2 en generator i $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$.

Selv om $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ har flere generatorer, er ikke alle elementene i denne gruppen generatorer. Se for eksempel på elementet 3. Ved å gå gjennom de 10 første eksponentieringene, uten å vise de omstendelige utregningene, får vi følgende resultater:


- $3^1 = 3 \mod 11$
- $3^2 = 9 \mod 11$
- $3^3 = 5 \mod 11$
- $3^4 = 4 \mod 11$
- $3^5 = 1 \mod 11$
- $3^6 = 3 \mod 11$
- $3^7 = 9 \mod 11$
- $3^8 = 5 \mod 11$
- $3^9 = 4 \mod 11$
- $3^{10} = 1 \mod 11$$

I stedet for å sykle gjennom alle verdiene i $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, fører eksponentiering av elementet 3 bare til en delmengde av disse verdiene: 3, 9, 5, 4 og 1. Etter den femte eksponentialiseringen begynner disse verdiene å gjenta seg.

Vi kan nå definere en **syklisk gruppe** som en hvilken som helst gruppe med minst én generator. Det vil si at det finnes minst ett gruppeelement som du kan produsere alle andre gruppeelementer fra ved hjelp av eksponentiering.

Du har kanskje lagt merke til at både $2^{10}$ og $3^{10}$ er lik $1 \mod 11$ i eksempelet vårt ovenfor. Selv om vi ikke skal utføre beregningene, vil eksponentiering med 10 av et hvilket som helst element i gruppen $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ faktisk gi $1 \mod 11$. Hvorfor er dette tilfellet?

Dette er et viktig spørsmål, men det krever en del arbeid å besvare.

Til å begynne med antar vi to positive heltall $a$ og $N$. Et viktig teorem i tallteori sier at $a$ har en multiplikativ invers modulo $N$ (det vil si et heltall $b$ slik at $a \cdot b = 1 \mod N$) hvis og bare hvis den største felles divisoren mellom $a$ og $N$ er lik 1. Det vil si hvis $a$ og $N$ er koprim.

For enhver gruppe av heltall som er utstyrt med multiplikasjon modulo $N$, er det bare de mindre koprimene med $N$ som er inkludert i mengden. Vi kan betegne denne mengden med $\mathbb{Z}^c \mod N$.

Anta for eksempel at $N$ er 10. Bare heltallene 1, 3, 7 og 9 er koprim med 10. Så mengden $\mathbb{Z}^c \mod 10$ inkluderer bare $\{1, 3, 7, 9\}$. Du kan ikke lage en gruppe med heltallsmultiplikasjon modulo 10 ved å bruke andre heltall mellom 1 og 10. For denne gruppen er de inverse parene 1 og 9, og 3 og 7.

I tilfellet der $N$ selv er primtall, er alle heltallene fra 1 til og med $N - 1$ koprim med $N$. En slik gruppe har dermed en orden på $N - 1$. Ved å bruke vår tidligere notasjon er $\mathbb{Z}^c \mod N$ lik $\mathbb{Z}^* \mod N$ når $N$ er primtall. Gruppen vi valgte for vårt tidligere eksempel, $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, er en spesiell forekomst av denne klassen av grupper.

Deretter beregner funksjonen $\phi(N)$ antall koprim opp til et tall $N$, og er kjent som **Eulers Phi-funksjon**. [1] I henhold til **Eulers teorem** gjelder følgende når to heltall $a$ og $N$ er koprimale:


- $a^{\phi(N)} \mod N = 1 \mod N$

Dette har en viktig implikasjon for klassen av grupper $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ der $N$ er primtall. For disse gruppene representerer eksponentiering av gruppeelementer aritmetisk eksponentiering. Det vil si at $a^{\phi(N)} \mod N$ representerer den aritmetiske operasjonen $a^{\phi(N)} \mod N$. Ettersom ethvert element $a$ i disse multiplikative gruppene er koprim med $N$, betyr det at $a^{\phi(N)} \mod N = a^{N - 1} \mod N = 1 \mod N$.

Eulers teorem er et veldig viktig resultat. Til å begynne med innebærer det at alle elementer i $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ bare kan sykle gjennom et antall verdier ved eksponentiering som deler seg i $N - 1$. I tilfellet $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ betyr dette at hvert element bare kan sykle gjennom 2, 5 eller 10 elementer. Gruppeverdiene som et element sykler gjennom ved eksponentiering, er kjent som elementets **orden**. Et element med en orden som tilsvarer ordenen til en gruppe, er en generator.

Videre innebærer Eulers teorem at vi alltid kan vite resultatet av $a^{N - 1} \mod N$ for enhver gruppe $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ der $N$ er primtall. Dette gjelder uansett hvor kompliserte de faktiske beregningene måtte være.

Anta for eksempel at gruppen vår er $\mathbb{Z}^* \mod 160,481,182$ (der 160,481,182 faktisk er et primtall). Vi vet at alle heltallene 1 til og med 160,481,181 må være elementer i denne gruppen, og at $\phi(n) = 160,481,181$. Selv om vi ikke kan gjøre alle trinnene i beregningene, vet vi at uttrykk som $514^{160,481,181}$, $2,005^{160,481,181}$ og $256,212^{160,481,181}$ alle må evaluere til $1 \mod 160,481,182$.

**Noter:**

[1] Funksjonen fungerer på følgende måte. Ethvert heltall $N$ kan faktoriseres til et produkt av primtall. Anta at et bestemt $N$ er faktorisert på følgende måte: $p_1^{e1} \cdot p_2^{e2} \cdot \ldots \cdot p_m^{em}$ hvor alle $p$ er primtall og alle $e$ er heltall større enn eller lik 1. Da:

$$
\phi(N) = \sum_{i=1}^m \left[p_i^{e_i} - p_i^{e_i - 1}\right]
$$

Eulers Phi-funksjonsformel for primfaktorisering av $N$.

## Felt

<chapterId>fad52d86-3a22-5c9f-979e-3bec9eaa008e</chapterId>

En gruppe er den grunnleggende algebraiske strukturen i abstrakt algebra, men det finnes mange flere. Den eneste andre algebraiske strukturen du trenger å kjenne til, er et **felt**, nærmere bestemt et **endelig felt**. Denne typen algebraisk struktur brukes ofte i kryptografi, for eksempel i Advanced Encryption Standard. Sistnevnte er det viktigste symmetriske krypteringsskjemaet du vil støte på i praksis.

Et felt er avledet fra begrepet gruppe. Nærmere bestemt er et **felt** en mengde elementer **S** utstyrt med to binære operatorer $\circ$ og $\diamond$, som oppfyller følgende betingelser:

1. Mengden **S** utstyrt med $\circ$ er en abelsk gruppe.

2. Mengden **S** utstyrt med $\diamond$ er en abelsk gruppe for "ikke-null"-elementene.

3. Mengden **S** som er utstyrt med de to operatorene, oppfyller det som kalles den distributive betingelsen: Anta at $a$, $b$ og $c$ er elementer i **S**. Da oppfyller **S** utstyrt med de to operatorene den distributive egenskapen når $a \circ (b \diamond c) = (a \circ b) \diamond (a \circ c)$.

Merk at definisjonen av et felt er svært abstrakt, akkurat som for grupper. Den sier ingenting om elementtypene i **S**, eller om operasjonene $\circ$ og $\diamond$. Den sier bare at et felt er en hvilken som helst mengde elementer med to operasjoner der de tre ovennevnte betingelsene holder. (Nullelementet i den andre abelske gruppen kan tolkes abstrakt)

Så hva kan være et eksempel på et felt? Et godt eksempel er mengden $\mathbb{Z} \mod 7$, eller $\{0, 1, \ldots, 7\}$ definert over standard addisjon (i stedet for $\circ$ ovenfor) og standard multiplikasjon (i stedet for $\diamond$ ovenfor).

For det første oppfyller $\mathbb{Z} \mod 7$ betingelsen for å være en abelsk gruppe over addisjon, og den oppfyller betingelsen for å være en abelsk gruppe over multiplikasjon hvis du bare tar hensyn til elementene som ikke er null. For det andre oppfyller kombinasjonen av mengden med de to operatorene den distributive betingelsen.

Det er didaktisk interessant å utforske disse påstandene ved å bruke noen bestemte verdier. La oss ta de eksperimentelle verdiene 5, 2 og 3, noen tilfeldig valgte elementer fra mengden $\mathbb{Z} \mod 7$, for å inspisere feltet $\langle \mathbb{Z} \mod 7, +, \cdot \rangle$. Vi vil bruke disse tre verdiene i rekkefølge, etter behov for å undersøke spesielle forhold.

La oss først undersøke om $\mathbb{Z} \mod 7$ utstyrt med addisjon er en abelsk gruppe.

1. **Lukkingsbetingelse**: La oss ta 5 og 2 som våre verdier. I så fall er $[5 + 2] \mod 7 = 7 \mod 7 = 0$. Dette er faktisk et element i $\mathbb{Z} \mod 7$, så resultatet er i samsvar med lukkingsbetingelsen.

2. **Assosiativitetsbetingelse**: La oss ta 5, 2 og 3 som våre verdier. I så fall er $[(5 + 2) + 3] \mod 7 = [5 + (2 + 3)] \mod 7 = 10 \mod 7 = 3$. Dette er i samsvar med assosiativitetsbetingelsen.

3. **Identitetsbetingelse**: La oss ta 5 som verdi. I så fall er $[5 + 0] \mod 7 = [0 + 5] \mod 7 = 5$. Så 0 ser ut til å være identitetselementet for addisjon.

4. **Invers tilstand**: Tenk på den inverse av 5. Det må være tilfelle at $[5 + d] \mod 7 = 0$, for en viss verdi av $d$. I dette tilfellet er den unike verdien fra $\mathbb{Z} \mod 7$ som oppfyller denne betingelsen er 2.

5. **Kommutativitetsbetingelse**: La oss ta 5 og 3 som våre verdier. I så fall er $[5 + 3] \mod 7 = [3 + 5] \mod 7 = 1$. Dette er i samsvar med kommutativitetsbetingelsen.

Mengden $\mathbb{Z} \mod 7$ utstyrt med addisjon ser helt klart ut til å være en abelsk gruppe. La oss nå undersøke om $\mathbb{Z} \mod 7$ utstyrt med multiplikasjon er en abelsk gruppe for alle elementene som ikke er null.

1. **Lukkingsbetingelse**: La oss ta 5 og 2 som våre verdier. I så fall er $[5 \cdot 2] \mod 7 = 10 \mod 7 = 3$. Dette er også et element i $\mathbb{Z} \mod 7$, så resultatet er i samsvar med lukkingsbetingelsen.

2. **Assosiativitetsbetingelse**: La oss ta 5, 2 og 3 som våre verdier. I så fall er $[(5 \cdot 2) \cdot 3] \mod 7 = [5 \cdot (2 \cdot 3)] \mod 7 = 30 \mod 7 = 2$. Dette er i samsvar med assosiativitetsbetingelsen.

3. **Identitetsbetingelse**: La oss ta 5 som verdi. I så fall er $[5 \cdot 1] \mod 7 = [1 \cdot 5] \mod 7 = 5$. Så 1 ser ut til å være identitetselementet for multiplikasjon.

4. **Invers tilstand**: Tenk på den inverse av 5. Det må være slik at $[5 \cdot d] \mod 7 = 1$, for en viss verdi av $d$. Den unike verdien fra $\mathbb{Z} \mod 7$ som oppfyller denne betingelsen er 3. Dette er i samsvar med den inverse betingelsen.

5. **Kommutativitetsbetingelse**: La oss ta 5 og 3 som våre verdier. I så fall er $[5 \cdot 3] \mod 7 = [3 \cdot 5] \mod 7 = 15 \mod 7 = 1$. Dette er i samsvar med kommutativitetsbetingelsen.

Mengden $\mathbb{Z} \mod 7$ ser helt klart ut til å oppfylle reglene for å være en abelsk gruppe når den kombineres med enten addisjon eller multiplikasjon over elementene som ikke er null.

Til slutt ser det ut til at dette settet kombinert med begge operatorene oppfyller den distributive betingelsen. La oss ta 5, 2 og 3 som våre verdier. Vi kan se at $[5 \cdot (2 + 3)] \mod 7 = [5 \cdot 2 + 5 \cdot 3] \mod 7 = 25 \mod 7 = 4$.

Vi har nå sett at $\mathbb{Z} \mod 7$ utstyrt med addisjon og multiplikasjon oppfyller aksiomene for et endelig felt når vi tester med spesielle verdier. Vi kan selvfølgelig også vise det generelt, men vil ikke gjøre det her.

Et viktig skille går mellom to typer felt: endelige og uendelige felt.

Et **uendelig felt** er et felt der mengden **S** er uendelig stor. Mengden av reelle tall $\mathbb{R}$ utstyrt med addisjon og multiplikasjon er et eksempel på et uendelig felt. Et **endelig felt**, også kjent som et **Galois-felt**, er et felt der mengden **S** er endelig. Vårt eksempel ovenfor med $\langle \mathbb{Z} \mod 7, +, \cdot \rangle$ er et endelig felt.

I kryptografi er vi først og fremst interessert i endelige felt. Generelt kan det vises at det finnes et endelig felt for en viss mengde elementer **S** hvis og bare hvis det har $p^m$ elementer, der $p$ er et primtall og $m$ et positivt heltall som er større enn eller lik én. Med andre ord, hvis rekkefølgen til en mengde **S** er et primtall ($p^m$ der $m = 1$) eller en primpotens ($p^m$ der $m > 1$), så kan du finne to operatorer $\circ$ og $\diamond$ slik at betingelsene for et felt er oppfylt.

Hvis et endelig felt har et primtall av elementer, kalles det et **primfelt**. Hvis antallet elementer i det begrensede feltet er en primtallspotensial, kalles feltet et **utvidelsesfelt**. I kryptografi er vi interessert i både prim- og ekstensjonsfelt. [2]

De viktigste primtallfeltene av interesse for kryptografi er de der mengden av alle heltall er modulert av et eller annet primtall, og operatorene er standard addisjon og multiplikasjon. Denne klassen av endelige felt inkluderer $\mathbb{Z} \mod 2$, $\mathbb{Z} \mod 3$, $\mathbb{Z} \mod 5$, $\mathbb{Z} \mod 7$, $\mathbb{Z} \mod 11$, $\mathbb{Z} \mod 13$, og så videre. For ethvert primtallsfelt $\mathbb{Z} \mod p$, er mengden av heltall i feltet som følger: $\{0, 1, \ldots, p - 2, p - 1\}$.

I kryptografi er vi også interessert i utvidelsesfelt, spesielt alle felt med $2^m$ elementer der $m > 1$. Slike endelige felt brukes for eksempel i Rijndael-chifferet, som danner grunnlaget for Advanced Encryption Standard. Selv om primtalsfelt er relativt intuitive, er disse base 2-utvidelsesfeltene sannsynligvis ikke noe for alle som ikke er kjent med abstrakt algebra.

Til å begynne med er det faktisk sant at enhver mengde heltall med $2^m$ elementer kan tilordnes to operatorer som gjør kombinasjonen av dem til et felt (så lenge $m$ er et positivt heltall). Men bare fordi et felt eksisterer, betyr det ikke nødvendigvis at det er lett å oppdage eller spesielt praktisk for visse anvendelser.

Det viser seg at spesielt anvendelige utvidelsesfelt av $2^m$ i kryptografi er de som er definert over bestemte sett av polynomuttrykk, i stedet for over et sett av heltall.

Anta for eksempel at vi ønsket et utvidelsesfelt med $2^3$ (dvs. 8) elementer i mengden. Det kan finnes mange forskjellige sett som kan brukes for felt av denne størrelsen, men ett slikt sett inneholder alle unike polynomer av formen $a_2x^2 + a_1x + a_0$, der hver koeffisient $a_i$ enten er 0 eller 1. Denne mengden **S** inneholder derfor følgende elementer:

1. $0$: Tilfellet der $a_2 = 0$, $a_1 = 0$ og $a_0 = 0$.

2. $1$: Tilfellet der $a_2 = 0$, $a_1 = 0$ og $a_0 = 1$.

3. $x$: Tilfellet der $a_2 = 0$, $a_1 = 1$ og $a_0 = 0$.

4. $x + 1$: Tilfellet der $a_2 = 0$, $a_1 = 1$ og $a_0 = 1$.

5. $x^2$: Tilfellet der $a_2 = 1$, $a_1 = 0$ og $a_0 = 0$.

6. $x^2 + 1$: Tilfellet der $a_2 = 1$, $a_1 = 0$ og $a_0 = 1$.

7. $x^2 + x$: Tilfellet der $a_2 = 1$, $a_1 = 1$ og $a_0 = 0$.

8. $x^2 + x + 1$: Tilfellet der $a_2 = 1$, $a_1 = 1$ og $a_0 = 1$.

Så **S** vil være mengden $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + x + 1\}$. Hvilke to operasjoner kan defineres over denne mengden av elementer for å sikre at kombinasjonen av dem er et felt?

Den første operasjonen på mengden **S** ($\circ$) kan defineres som standard polynomadisjon modulo 2. Alt du trenger å gjøre er å legge sammen polynomene som du vanligvis ville gjort, og deretter bruke modulo 2 på hver av koeffisientene i det resulterende polynomet. Her er noen eksempler:


- $[(x^2) + (x^2 + x + 1)] \mod 2 = [2x^2 + x + 1] \mod 2 = x + 1$$
- $[(x^2 + x) + (x)] \mod 2 = [x^2 + 2x] \mod 2 = x^2$ $[(x^2 + x) + (x)] \mod 2 = x^2
- $[(x + 1) + (x^2 + x + 1)] \mod 2 = [x^2 + 2x + 2] \mod 2 = x^2 + 1$$

Den andre operasjonen på mengden **S** ($\diamond$) som er nødvendig for å lage feltet, er mer komplisert. Det er en slags multiplikasjon, men ikke en standard multiplikasjon fra aritmetikken. I stedet må du se hvert element som en vektor og forstå operasjonen som en multiplikasjon av disse to vektorene modulert med et irreduserbart polynom.

La oss først se nærmere på ideen om et irreduserbart polynom. Et **irreduktibelt polynom** er et polynom som ikke kan faktoriseres (på samme måte som et primtall ikke kan faktoriseres i andre komponenter enn 1 og primtallet selv). For vårt formål er vi interessert i polynomer som er irreduserbare med hensyn til mengden av alle heltall. (Merk at du kan være i stand til å faktorisere visse polynomer ved hjelp av for eksempel de reelle eller komplekse tallene, selv om du ikke kan faktorisere dem ved hjelp av heltall)

Se for eksempel på polynomet $x^2 - 3x + 2$. Dette kan omskrives som $(x - 1)(x - 2)$. Derfor er dette ikke irreduserbart. Se nå på polynomet $x^2 + 1$. Det er ikke mulig å faktorisere dette uttrykket ytterligere ved å bruke bare heltall. Derfor er dette et irreduserbart polynom med hensyn til heltallene.

Nå skal vi se nærmere på begrepet vektormultiplikasjon. Vi skal ikke gå i dybden på dette emnet, men du trenger bare å forstå en grunnleggende regel: Enhver vektordivisjon kan finne sted så lenge dividenden har en grad som er høyere enn eller lik divisorens grad. Hvis dividenden har en lavere grad enn divisoren, kan dividenden ikke lenger divideres med divisoren.

Se for eksempel på uttrykket $x^6 + x + 1 \mod x^5 + x^2$. Dette reduseres tydeligvis ytterligere ettersom graden til dividenden, 6, er høyere enn graden til divisoren, 5. Se nå på uttrykket $x^5 + x + 1 \mod x^5 + x^2$. Dette reduseres også ytterligere, ettersom graden til dividenden, 5, og divisoren, 5, er lik.

Men, se nå på uttrykket $x^4 + x + 1 \mod x^5 + x^2$. Dette kan ikke reduseres ytterligere, ettersom graden til dividenden, 4, er lavere enn graden til divisoren, 5.

På grunnlag av denne informasjonen er vi nå klare til å finne vår andre operasjon for mengden $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + x + 1\}$.

Jeg har allerede sagt at den andre operasjonen skal forstås som vektormultiplikasjon modulo et irreduserbart polynom. Dette irreduserbare polynomet skal sikre at den andre operasjonen definerer en abelsk gruppe over **S** og er konsistent med den distributive betingelsen. Så hva skal det irreduserbare polynomet være?

Siden alle vektorene i mengden er av grad 2 eller lavere, må det irreduserbare polynomet være av grad 3. Hvis enhver multiplikasjon av to vektorer i mengden gir et polynom av grad 3 eller høyere, vet vi at modulo et polynom av grad 3 alltid gir et polynom av grad 2 eller lavere. Dette er tilfellet fordi ethvert polynom av grad 3 eller høyere alltid er delelig med et polynom av grad 3. I tillegg må polynomet som fungerer som divisor, være irreduserbart.

Det viser seg at det finnes flere irreduserbare polynomer av grad 3 som vi kan bruke som divisor. Hvert av disse polynomene definerer et annet felt i forbindelse med vår mengde **S** og addisjon modulo 2. Dette betyr at du har flere alternativer når du bruker utvidelsesfelt $2^m$ i kryptografi.

I vårt eksempel velger vi polynomet $x^3 + x + 1$. Dette er irreduserbart, fordi du ikke kan faktorisere det ved hjelp av heltall. I tillegg vil den sikre at enhver multiplikasjon av to elementer vil gi et polynom av grad 2 eller mindre.

La oss gå gjennom et eksempel på den andre operasjonen ved å bruke polynomet $x^3 + x + 1$ som divisor for å illustrere hvordan den fungerer. Anta at du multipliserer elementene $x^2 + 1$ med $x^2 + x$ i vår mengde **S**. Vi må da beregne uttrykket $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1$. Dette kan forenkles på følgende måte:


- $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1 =$$
- $[x^2 \cdot x^2 + x^2 \cdot x + 1 \cdot x^2 + 1 \cdot x] \mod x^3 + x + 1 =$
- $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$ $[x^4 + x^3 + x^2 + x

Vi vet at $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$ kan reduseres ettersom dividenden har en høyere grad (4) enn divisoren (3).

Til å begynne med kan du se at uttrykket $x^3 + x + 1$ går inn i $x^4 + x^3 + x^2 + x$ totalt $x$ ganger. Dette kan du verifisere ved å multiplisere $x^3 + x + 1$ med $x$, som er $x^4 + x^2 + x$. Siden det siste leddet er av samme grad som dividenden, nemlig 4, vet vi at dette fungerer. Du kan beregne resten av denne divisjonen med $x$ på følgende måte:


- $[(x^4 + x^3 + x^2 + x) - (x^4 + x^2 + x)] \mod x^3 + x + 1 =$$
- $[x^3] \mod x^3 + x + 1 =$
- $x^3$

Så etter å ha dividert $x^4 + x^3 + x^2 + x$ med $x^3 + x + 1$ til sammen $x$ ganger, har vi en rest på $x^3$. Kan denne divideres ytterligere med $x^3 + x + 1$?

Intuitivt kan det være tiltalende å si at $x^3$ ikke lenger kan divideres med $x^3 + x + 1$, fordi det siste leddet virker større. Husk imidlertid diskusjonen vår om vektordivisjon tidligere. Så lenge dividenden har en grad som er større eller lik divisoren, kan uttrykket reduseres ytterligere. Uttrykket $x^3 + x + 1$ kan nemlig gå inn i $x^3$ nøyaktig 1 gang. Resten beregnes på følgende måte:

$$
[(x^3) - (x^3 + x + 1)] \mod x^3 + x + 1 = [x + 1] \mod x^3 + x + 1 = x + 1
$$

Du lurer kanskje på hvorfor $(x^3) - (x^3 + x + 1)$ evalueres til $x + 1$ og ikke $-x - 1$. Husk at den første operasjonen i feltet vårt er definert modulo 2. Derfor gir subtraksjon av to vektorer nøyaktig samme resultat som addisjon av to vektorer.

For å oppsummere multiplikasjonen av $x^2 + 1$ og $x^2 + x$: Når du multipliserer disse to leddene, får du et grad 4-polynom, $x^4 + x^3 + x^2 + x$, som må reduseres modulo $x^3 + x + 1$. Polynomet av grad 4 er delelig med $x^3 + x + 1$ nøyaktig $x + 1$ ganger. Resten etter å ha delt $x^4 + x^3 + x^2 + x$ med $x^3 + x + 1$ nøyaktig $x + 1$ ganger er $x + 1$. Dette er faktisk et element i vår mengde $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + x + 1\}$.

Hvorfor kan utvidelsesfelt med base 2 over polynomsett, som i eksempelet ovenfor, være nyttige for kryptografi? Grunnen er at du kan se på koeffisientene i polynomene i slike sett, enten 0 eller 1, som elementer i binære strenger med en bestemt lengde. Mengden **S** i eksempelet vårt ovenfor kan for eksempel i stedet betraktes som en mengde **S** som inkluderer alle binære strenger med lengde 3 (000 til 111). Operasjonene på **S** kan da også brukes til å utføre operasjoner på disse binære strengene og produsere en binær streng med samme lengde.

**Noter:**

[2] Utvidelsesfelt blir svært kontraintuitive. I stedet for å ha elementer av heltall, har de sett av polynomer. I tillegg utføres alle operasjoner modulo et irreduserbart polynom.

## Abstrakt algebra i praksis

<chapterId>ed35b98d-18b4-5790-9911-1078e0f84f92</chapterId>

Til tross for det formelle språket og den abstrakte diskusjonen, burde det ikke være så vanskelig å forstå gruppebegrepet. Det er bare en mengde elementer sammen med en binær operasjon, der utførelsen av den binære operasjonen på disse elementene oppfyller fire generelle betingelser. En abelsk gruppe har bare en ekstra betingelse som kalles kommutativitet. En syklisk gruppe er på sin side en spesiell type abelsk gruppe, nemlig en gruppe som har en generator. Et felt er bare en mer kompleks konstruksjon av det grunnleggende gruppebegrepet.

Men hvis du er en praktisk anlagt person, lurer du kanskje på dette punktet: Hvem bryr seg? Har det noen relevans i den virkelige verden å vite at en mengde elementer med en operator er en gruppe, eller til og med en abelsk eller syklisk gruppe? Har det noen betydning å vite at noe er et felt?

Uten å gå for mye i detalj, er svaret "ja". Grupper ble først skapt på 1800-tallet av den franske matematikeren Evariste Galois. Han brukte dem til å trekke konklusjoner om løsning av polynomlikninger av en grad høyere enn fem.

Siden den gang har gruppebegrepet bidratt til å kaste lys over en rekke problemer i blant annet matematikken. På grunnlag av gruppeteori kunne for eksempel fysikeren Murray-Gellman forutsi eksistensen av en partikkel før den faktisk ble observert i eksperimenter [3]. [Et annet eksempel er kjemikere som bruker gruppeteori til å klassifisere molekylers form. Matematikere har til og med brukt gruppebegrepet til å trekke konklusjoner om noe så konkret som veggpapir!

Å vise at en mengde elementer med en eller annen operator er en gruppe, betyr at det du beskriver har en bestemt symmetri. Ikke en symmetri i vanlig forstand, men i en mer abstrakt form. Og dette kan gi betydelig innsikt i spesielle systemer og problemer. De mer komplekse begrepene fra abstrakt algebra gir oss bare tilleggsinformasjon.

Det viktigste er at du vil se betydningen av tallteoretiske grupper og felt i praksis gjennom deres anvendelse i kryptografi, spesielt offentlig nøkkelkryptografi. Vi har allerede sett hvordan utvidelsesfelt brukes i for eksempel Rijndael-krypteringen. Vi skal se nærmere på dette eksemplet i *Kapittel 5*.

For videre diskusjon om abstrakt algebra vil jeg anbefale den utmerkede videoserien om abstrakt algebra fra Socratica. [4] Jeg vil spesielt anbefale følgende videoer: "Hva er abstrakt algebra?", "Gruppedefinisjon (utvidet)", "Ringdefinisjon (utvidet)" og "Feltdefinisjon (utvidet)" Disse fire videoene vil gi deg ytterligere innsikt i mye av diskusjonen ovenfor. (Vi har ikke diskutert ringer, men et felt er bare en spesiell type ring)

For videre diskusjon om moderne tallteori kan du konsultere mange avanserte diskusjoner om kryptografi. Jeg vil foreslå Jonathan Katz og Yehuda Lindells Introduction to Modern Cryptography eller Christof Paar og Jan Pelzls Understanding Cryptography for videre diskusjon. [5]

**Noter:**

[3] Se [YouTube-video] (https://www.youtube.com/watch?v=NOMUnMuxDZY&feature=youtu.be)

[4] Socratica, [Abstrakt algebra] (https://www.socratica.com/subject/abstract-algebra)

[5] Katz og Lindell, *Introduction to Modern Cryptography*, 2. utgave, 2015 (CRC Press: Boca Raton, FL). Paar og Pelzl, *Understanding Cryptography*, 2010 (Springer-Verlag: Berlin).

# Symmetrisk kryptografi

<partId>ef768d0e-fe7b-510c-87d6-6febb3de1039</partId>

## Alice og Bob

<chapterId>47345330-be2d-5faf-afd0-d289a8d21bf1</chapterId>

En av de to hovedgrenene innen kryptografi er symmetrisk kryptografi. Den omfatter både krypteringssystemer og systemer for autentisering og integritet. Frem til 1970-tallet besto all kryptografi av symmetriske krypteringsmetoder.

Hoveddiskusjonen starter med å se på symmetriske krypteringsmetoder og det viktige skillet mellom streamchiffre og blokkchiffre. Deretter tar vi for oss meldingsautentiseringskoder, som er metoder for å sikre meldingens integritet og autentisitet. Til slutt ser vi på hvordan symmetriske krypteringssystemer og meldingsautentiseringskoder kan kombineres for å garantere sikker kommunikasjon.

I dette kapittelet diskuteres ulike symmetriske kryptografiske skjemaer fra praksis i forbifarten. Neste kapittel gir en detaljert redegjørelse for kryptering med henholdsvis RC4 og AES, som er en strømkryptering og en blokkryptering fra praksis.

Før vi begynner diskusjonen om symmetrisk kryptografi, vil jeg kort kommentere illustrasjonene av Alice og Bob i dette og de påfølgende kapitlene.

___

Når man skal illustrere prinsippene i kryptografi, bruker man ofte eksempler som involverer Alice og Bob. Det vil jeg også gjøre.

Spesielt hvis du er ny i kryptografi, er det viktig å være klar over at disse eksemplene med Alice og Bob kun er ment som illustrasjoner av kryptografiske prinsipper og konstruksjoner i et forenklet miljø. Prinsippene og konstruksjonene kan imidlertid brukes i et mye bredere spekter av virkelige sammenhenger.

Her er fem viktige punkter du bør ha i bakhodet når det gjelder eksempler som involverer Alice og Bob i kryptografi:

1. De kan enkelt oversettes til eksempler med andre typer aktører, for eksempel bedrifter eller offentlige organisasjoner.

2. De kan enkelt utvides til å omfatte tre eller flere aktører.

3. I eksemplene er Bob og Alice vanligvis aktive deltakere i opprettelsen av hver enkelt melding og i anvendelsen av kryptografiske ordninger på meldingen. Men i virkeligheten er elektronisk kommunikasjon i stor grad automatisert. Når du for eksempel besøker et nettsted som bruker transportlagssikkerhet, håndteres kryptografien vanligvis av datamaskinen din og webserveren.

4. I forbindelse med elektronisk kommunikasjon er "meldingene" som sendes over en kommunikasjonskanal, vanligvis TCP/IP-pakker. Disse kan tilhøre en e-post, en Facebook-melding, en telefonsamtale, en filoverføring, et nettsted, en programvareopplasting og så videre. De er ikke meldinger i tradisjonell forstand. Kryptografer vil likevel ofte forenkle denne virkeligheten ved å si at meldingen for eksempel er en e-post.

5. Eksemplene fokuserer vanligvis på elektronisk kommunikasjon, men de kan også utvides til å omfatte tradisjonelle kommunikasjonsformer som brev.

## Symmetriske krypteringsordninger

<chapterId>41bfdbe1-6d41-5272-98bb-81f24b2fd6af</chapterId>

Vi kan definere et **symmetrisk krypteringsopplegg** som et hvilket som helst kryptografisk opplegg med tre algoritmer:

1. En **nøkkelgenereringsalgoritme** som genererer en privat nøkkel.

2. En **krypteringsalgoritme**, som tar den private nøkkelen og en klartekst som inndata og sender ut en chiffertekst.

3. En **dekrypteringsalgoritme**, som tar den private nøkkelen og krypteringsteksten som inndata og sender ut den opprinnelige klarteksten.

Et krypteringsskjema - enten det er symmetrisk eller asymmetrisk - tilbyr vanligvis en mal for kryptering basert på en kjernealgoritme, i stedet for en nøyaktig spesifikasjon.

Ta for eksempel Salsa20, et symmetrisk krypteringsopplegg. Den kan brukes med både 128- og 256-biters nøkkellengder. Valget av nøkkellengde påvirker noen mindre detaljer i algoritmen (antall runder i algoritmen, for å være nøyaktig).

Men man kan ikke si at Salsa20 med en 128-bits nøkkel er et annet krypteringsopplegg enn Salsa20 med en 256-bits nøkkel. Kjernealgoritmen forblir den samme. Det er først når kjernealgoritmen endres, at vi virkelig kan snakke om to forskjellige krypteringsskjemaer.

Symmetriske krypteringsordninger er vanligvis nyttige i to typer tilfeller: (1) tilfeller der to eller flere agenter kommuniserer på avstand og ønsker å holde innholdet i kommunikasjonen hemmelig, og (2) tilfeller der én agent ønsker å holde innholdet i en melding hemmelig over tid.

Du kan se en illustrasjon av situasjon (1) i *Figur 1* nedenfor. Bob ønsker å sende en melding $M$ til Alice over en viss avstand, men ønsker ikke at andre skal kunne lese meldingen.

Bob krypterer først meldingen $M$ med den private nøkkelen $K$. Deretter sender han chifferteksten $C$ til Alice. Når Alice har mottatt chifferteksten, kan hun dekryptere den ved hjelp av nøkkelen $K$ og lese klarteksten. Med et godt krypteringsopplegg bør en angriper som snapper opp krypteringsteksten $C$, ikke være i stand til å finne ut noe av reell betydning om meldingen $M$.

Du kan se en illustrasjon av situasjon (2) i *Figur 2* nedenfor. Bob ønsker å hindre andre i å se visse opplysninger. En typisk situasjon kan være at Bob er en ansatt som lagrer sensitive data på datamaskinen sin, som verken utenforstående eller kolleger skal kunne lese.

Bob krypterer meldingen $M$ på tidspunkt $T_0$ med nøkkelen $K$ for å produsere chifferteksten $C$. På tidspunkt $T_1$ trenger han meldingen igjen, og dekrypterer chifferteksten $C$ med nøkkelen $K$. En eventuell angriper som kan ha kommet over krypteringsteksten $C$ i mellomtiden, skal ikke ha vært i stand til å utlede noe vesentlig om $M$ fra den.

*Figur 1: Hemmelighold på tvers av rommet*

![Figure 1: Secrecy across space](assets/Figure4-1.webp "Figure 1: Secrecy across space")

*Figur 2: Hemmelighold over tid*

![Figure 2: Secrecy across time](assets/Figure4-2.webp "Figure 2: Secrecy across time")

## Et eksempel: Shift-krypteringen

<chapterId>7b179ae8-8d15-5e80-a43f-22c970d87b5e</chapterId>

I kapittel 2 så vi på shift-chifferet, som er et eksempel på et svært enkelt symmetrisk krypteringsskjema. La oss se på det igjen her.

Anta at det finnes en ordbok *D* som sidestiller alle bokstavene i det engelske alfabetet, i rekkefølge, med tallmengden $\{0,1,2,\dots,25\}$. Anta at det finnes et sett med mulige meldinger **M**. Shift-chifferet er da et krypteringsskjema som er definert på følgende måte:


- Velg tilfeldig en nøkkel $k$ fra settet av mulige nøkler **K**, der **K** = $\{0,1,2,\dots,25\}$
- Krypter en melding $m \in$ **M** på følgende måte:
    - Del $m$ inn i de enkelte bokstavene $m_0, m_1,\dots, m_i, \dots, m_l$
    - Konverter hver $m_i$ til et tall i henhold til *D*
    - For hver $m_i$, $c_i = [(m_i + k) \mod 26]$
    - Konverter hver $c_i$ til en bokstav i henhold til *D*
    - Kombiner deretter $c_0, c_1,\dots, c_l$ for å få krypteringsteksten $c$
- Dekrypter en krypteringstekst $c$ på følgende måte:
    - Konverter hver $c_i$ til et tall i henhold til *D*
    - For hver $c_i$, $m_i = [(c_i - k) \mod 26]$
    - Konverter hver $m_i$ til en bokstav i henhold til *D*
    - Kombiner deretter $m_0, m_1,\dots, m_l$ for å få den opprinnelige meldingen $m$

Det som gjør shift cipher til et symmetrisk krypteringsskjema, er at den samme nøkkelen brukes til både kryptering og dekryptering. Anta for eksempel at du ønsker å kryptere meldingen "DOG" ved hjelp av shift cipher, og at du tilfeldig har valgt "24" som nøkkel. Hvis du krypterer meldingen med denne nøkkelen, får du "BME". Den eneste måten å få tilbake den opprinnelige meldingen på, er ved å bruke den samme nøkkelen, "24", til dekrypteringsprosessen.

Denne Shift-krypteringen er et eksempel på en **monoalfabetisk substitusjonskryptering**: et krypteringsopplegg der krypteringstekstens alfabet er fast (dvs. at det bare brukes ett alfabet). Hvis vi antar at dekrypteringsalgoritmen er deterministisk, kan hvert symbol i substitusjonskrypteringsteksten maksimalt referere til ett symbol i klarteksten.

Frem til 1700-tallet var mange krypteringsapplikasjoner avhengig av monoalfabetiske substitusjonskrypteringer, selv om disse ofte var mye mer komplekse enn Shift-krypteringen. Man kunne for eksempel velge en tilfeldig bokstav fra alfabetet for hver bokstav i den opprinnelige teksten, under forutsetning av at hver bokstav bare forekommer én gang i chiffertekstens alfabet. Det betyr at du ville ha 26 mulige private nøkler, noe som var enormt i tiden før datamaskinenes tid.

Vær oppmerksom på at du ofte vil støte på begrepet **cipher** innen kryptografi. Vær oppmerksom på at dette begrepet har ulike betydninger. Jeg kjenner faktisk til minst fem forskjellige betydninger av begrepet innenfor kryptografi.

I noen tilfeller refererer det til et krypteringsskjema, slik det gjør i Shift cipher og monoalfabetisk substitusjonskryptering. Begrepet kan imidlertid også referere spesifikt til krypteringsalgoritmen, den private nøkkelen eller bare krypteringsteksten i et slikt krypteringsskjema.

Til slutt kan begrepet chiffer også referere til en kjernealgoritme som du kan konstruere kryptografiske skjemaer ut fra. Det kan dreie seg om ulike krypteringsalgoritmer, men også andre typer kryptografiske skjemaer. Denne betydningen av begrepet blir relevant i forbindelse med blokkchiffre (se avsnittet "Blokkchiffre" nedenfor).

Du kan også støte på begrepene **kryptere** eller **dekryptere**. Disse begrepene er bare synonymer for kryptering og dekryptering.

## Brute force-angrep og Kerckhoffs prinsipp

<chapterId>2d73ef97-26c5-5d11-8815-0ddbe89c8003</chapterId>

Shift-kryptering er et svært usikkert symmetrisk krypteringsskjema, i hvert fall i den moderne verden. [1] En angriper kan bare forsøke å dekryptere en hvilken som helst krypteringstekst med alle 26 mulige nøkler for å se hvilket resultat som gir mening. Denne typen angrep, der angriperen bare går gjennom nøklene for å se hva som fungerer, kalles et **brute force-angrep** eller **uttømmende nøkkelsøk**.

For at et krypteringssystem skal oppfylle et minimumskrav til sikkerhet, må det ha et sett med mulige nøkler, eller **nøkkelrom**, som er så stort at brute-force-angrep er ugjennomførbare. Alle moderne krypteringssystemer oppfyller denne standarden. Det er kjent som **tilstrekkelig nøkkelrom-prinsippet**. Et lignende prinsipp gjelder vanligvis i ulike typer kryptografiske systemer.

For å få en fornemmelse av den enorme størrelsen på nøkkelområdet i moderne krypteringssystemer kan vi tenke oss at en fil er kryptert med en 128-biters nøkkel i henhold til den avanserte krypteringsstandarden. Dette betyr at en angriper har et sett med $2^{128}$ nøkler som hun må gå gjennom for å utføre et brute force-angrep. En sjanse på 0,78 % for å lykkes med denne strategien vil kreve at angriperen går gjennom omtrent 2,65 ganger 10^{36}$ nøkler.

Anta at vi optimistisk antar at en angriper kan prøve $10^{16}$ nøkler per sekund (dvs. 10 kvadrillioner nøkler per sekund). For å teste 0,78 % av alle nøklene i nøkkelområdet må angrepet hennes vare i 2,65 ganger 10^{20}$ sekunder. Dette tilsvarer omtrent 8,4 billioner år. Så selv et brute force-angrep fra en absurd kraftig motstander er ikke realistisk med et moderne 128-bits krypteringsskjema. Dette er prinsippet om tilstrekkelig nøkkelplass.

Er shift-krypteringen sikrere hvis angriperen ikke kjenner krypteringsalgoritmen? Kanskje, men ikke mye.

Moderne kryptografi forutsetter uansett alltid at sikkerheten til et symmetrisk krypteringsopplegg kun er avhengig av at den private nøkkelen holdes hemmelig. Angriperen antas alltid å kjenne til alle de andre detaljene, inkludert meldingsområdet, nøkkelområdet, chiffertekstrommet, algoritmen for valg av nøkkel, krypteringsalgoritmen og dekrypteringsalgoritmen.

Ideen om at sikkerheten til et symmetrisk krypteringssystem bare kan baseres på hemmeligholdelsen av den private nøkkelen, er kjent som **Kerckhoffs prinsipp**.

Slik Kerckhoffs opprinnelig tenkte seg, gjelder prinsippet bare for symmetriske krypteringssystemer. En mer generell versjon av prinsippet gjelder imidlertid også for alle andre moderne typer kryptografiske systemer: Det må ikke kreves at et kryptografisk system må være hemmelig for at det skal være sikkert; hemmeligholdet kan bare omfatte noen strenger med informasjon, typisk en privat nøkkel.

Kerckhoffs prinsipp er sentralt i moderne kryptografi av fire grunner. [For det første finnes det bare et begrenset antall kryptografiske ordninger for bestemte typer applikasjoner. For eksempel bruker de fleste moderne symmetriske krypteringsapplikasjoner Rijndael-krypteringen. Så hemmeligholdet ditt når det gjelder utformingen av et skjema er svært begrenset. Det er imidlertid mye mer fleksibelt å holde en privat nøkkel for Rijndael-krypteringen hemmelig.

For det andre er det lettere å bytte ut en streng med informasjon enn et helt kryptografisk system. Anta at alle de ansatte i en bedrift har den samme krypteringsprogramvaren, og at to og to ansatte har hver sin private nøkkel for å kommunisere konfidensielt. I dette scenariet er det vanskelig å kompromittere nøkler, men selskapet kan i det minste beholde programvaren med slike sikkerhetsbrudd. Hvis selskapet var avhengig av at ordningen var hemmelig, ville ethvert brudd på denne hemmeligheten kreve at all programvaren ble byttet ut.

For det tredje åpner Kerckhoffs prinsipp for standardisering og kompatibilitet mellom brukere av kryptografiske systemer. Dette har enorme fordeler for effektiviteten. Det er for eksempel vanskelig å forestille seg hvordan millioner av mennesker skulle kunne koble seg sikkert til Googles webservere hver dag, hvis sikkerheten krevde at kryptografiske ordninger ble holdt hemmelige.

For det fjerde åpner Kerckhoffs prinsipp for offentlig granskning av kryptografiske ordninger. Denne typen granskning er helt nødvendig for å oppnå sikre kryptografiske systemer. Den viktigste kjernealgoritmen innen symmetrisk kryptografi, Rijndael-krypteringen, var resultatet av en konkurranse som ble arrangert av National Institute of Standards and Technology mellom 1997 og 2000.

Ethvert system som forsøker å oppnå **sikkerhet gjennom uklarhet**, er et system som baserer seg på å holde detaljene i utformingen og/eller implementeringen hemmelig. Innenfor kryptografi vil dette spesifikt være et system som baserer seg på å holde designdetaljene i det kryptografiske opplegget hemmelig. Security by obscurity står altså i direkte kontrast til Kerckhoffs prinsipp.

Åpenhetens evne til å styrke kvaliteten og sikkerheten gjelder også mer enn bare kryptografi i den digitale verden. Linux-distribusjoner med fri og åpen kildekode, som for eksempel Debian, har generelt flere fordeler i forhold til Windows og MacOS når det gjelder personvern, stabilitet, sikkerhet og fleksibilitet. Selv om det kan ha flere årsaker, er det viktigste prinsippet sannsynligvis, som Eric Raymond formulerte det i sitt berømte essay "The Cathedral and the Bazaar", at "gitt nok øyne, er alle feil overfladiske" [3] Det er dette prinsippet som har gitt Linux sin største suksess.

Man kan aldri entydig si at et kryptografisk system er "sikkert" eller "usikkert" I stedet finnes det ulike sikkerhetsbegreper for kryptografiske ordninger. Hver **definisjon av kryptografisk sikkerhet** må spesifisere (1) sikkerhetsmål, samt (2) en angripers evner. Ved å analysere kryptografiske ordninger opp mot en eller flere spesifikke sikkerhetsbegreper får man innsikt i deres bruksområder og begrensninger.

Vi skal ikke gå inn på alle detaljene i de ulike begrepene om kryptografisk sikkerhet, men du bør vite at to antakelser er gjennomgående for alle moderne kryptografiske sikkerhetsbegreper knyttet til symmetriske og asymmetriske systemer (og i en eller annen form for andre kryptografiske primitiver):


- Angriperens kunnskap om opplegget er i samsvar med Kerckhoffs prinsipp.
- Angriperen kan ikke utføre et brute force-angrep på systemet. Trusselmodellene for kryptografiske sikkerhetsbegreper tillater vanligvis ikke engang brute force-angrep, ettersom de antar at slike angrep ikke er relevante.

**Noter:**

[1] Ifølge Seutonius brukte Julius Cæsar en skiftchiffer med en konstant nøkkelverdi på 3 i sin militære kommunikasjon. A ville altså alltid bli D, B alltid E, C alltid F, og så videre. Denne spesielle versjonen av skiftchifferet har derfor blitt kjent som **Caesar-chifferet** (selv om det egentlig ikke er et chiffer i moderne forstand, ettersom nøkkelverdien er konstant). Cæsar-chifferet kan ha vært sikkert i det første århundret f.Kr. hvis Romas fiender var svært ukjente med kryptering. Men det ville helt klart ikke vært et særlig sikkert system i moderne tid.

[2] Jonathan Katz og Yehuda Lindell, _Introduction to Modern Cryptography_, CRC Press (Boca Raton, FL: 2015), s. 7f.

[3] Eric Raymond, "The Cathedral and the Bazaar", artikkel presentert på Linux-kongressen i Würzburg, Tyskland (27. mai 1997). Det finnes en rekke senere versjoner og en bok. Mine sitater er fra side 30 i boken: Eric Raymond, _The Cathedral and the Bazaar: Musings on Linux and Open Source by an Accidental Revolutionary_, revidert utg. (2001), O'Reilly: Sebastopol, CA.

## Stream ciphers

<chapterId>479aa6f4-45c4-59ca-8616-8cf8e61fc871</chapterId>

Symmetriske krypteringsmetoder deles vanligvis inn i to typer: **strømkryptering** og **blokkryptering**. Dette skillet er imidlertid noe problematisk, ettersom folk bruker disse begrepene på en inkonsekvent måte. I de neste avsnittene vil jeg gjøre rede for skillet på den måten jeg mener er best. Du bør imidlertid være klar over at mange vil bruke disse begrepene på en noe annen måte enn jeg gjør.

La oss først se på strømkryptering. En **strømkryptering** er et symmetrisk krypteringsskjema der krypteringen består av to trinn.

Først produseres en streng som er like lang som klarteksten ved hjelp av en privat nøkkel. Denne strengen kalles **nøkkelstrømmen**.

Deretter kombineres nøkkelstrømmen matematisk med klarteksten for å produsere en krypteringstekst. Denne kombinasjonen er vanligvis en XOR-operasjon. For dekryptering kan du bare reversere operasjonen. (Merk at $A \oplus B = B \oplus A$, i tilfelle $A$ og $B$ er bitstrenger. Rekkefølgen på en XOR-operasjon i en stream cipher spiller altså ingen rolle for resultatet. Denne egenskapen er kjent som **kommutativitet**)

En typisk XOR-strømkryptering er vist i *Figur 3*. Først tar du en privat nøkkel $K$ og bruker den til å generere en nøkkelstrøm. Nøkkelstrømmen kombineres deretter med klarteksten via en XOR-operasjon for å produsere krypteringsteksten. Enhver agent som mottar krypteringsteksten, kan enkelt dekryptere den hvis de har nøkkelen $K$. Alt hun trenger å gjøre, er å opprette en nøkkelstrøm som er like lang som krypteringsteksten i henhold til den spesifiserte prosedyren i ordningen, og XOR-kombinere den med krypteringsteksten.

*Figur 3: En XOR-strømkryptering*

![Figure 3: An XOR stream cipher](assets/Figure4-3.webp "Figure 3: An XOR stream cipher")

Husk at et krypteringsskjema vanligvis er en mal for kryptering med samme kjernealgoritme, snarere enn en nøyaktig spesifikasjon. I forlengelsen av dette er en stream cipher vanligvis en mal for kryptering der du kan bruke nøkler av ulik lengde. Selv om nøkkellengden kan påvirke noen mindre detaljer i skjemaet, vil det ikke påvirke den grunnleggende formen.

Shift-chifferet er et eksempel på et svært enkelt og usikkert strømchiffer. Ved hjelp av én enkelt bokstav (den private nøkkelen) kan du produsere en streng med bokstaver som er like lang som meldingen (nøkkelstrømmen). Denne nøkkelstrømmen kombineres deretter med klarteksten via en modulooperasjon for å produsere en chiffertekst. (Denne modulooperasjonen kan forenkles til en XOR-operasjon når bokstavene representeres i bits).

Et annet berømt eksempel på et stream-chiffer er **Vigenere-chifferet**, etter Blaise de Vigenere, som utviklet det fullt ut på slutten av 1500-tallet (selv om andre hadde gjort mye arbeid før ham). Det er et eksempel på en **polyalfabetisk substitusjonschiffer**: et krypteringsskjema der chifferalfabetet for et klartekstsymbol endres avhengig av symbolets posisjon i teksten. I motsetning til en monoalfabetisk substitusjonskryptering kan chiffertekstsymboler knyttes til mer enn ett klartekstsymbol.

Etter hvert som kryptering ble populært i renessansens Europa, ble også **krypteringsanalyse** - det vil si knekking av krypteringstekster - populært, særlig ved hjelp av **frekvensanalyse**. Sistnevnte benytter statistiske regelmessigheter i språket vårt til å knekke krypteringstekster, og ble oppdaget av arabiske lærde allerede på 800-tallet. Det er en teknikk som fungerer spesielt godt med lengre tekster. Og selv de mest sofistikerte monoalfabetiske substitionskrypteringene var ikke lenger tilstrekkelige mot frekvensanalyse på 1700-tallet i Europa, særlig i militære og sikkerhetsmessige sammenhenger. Vigenere-chifferet innebar en betydelig forbedring av sikkerheten, og det ble derfor populært i denne perioden og var utbredt på slutten av 1700-tallet.

Uformelt sett fungerer krypteringsopplegget på følgende måte:

1. Velg et ord med flere bokstaver som privat nøkkel.

2. For en hvilken som helst melding bruker du skiftkrypteringen på hver bokstav i meldingen ved å bruke den tilsvarende bokstaven i nøkkelordet som skift.

3. Hvis du har gått gjennom nøkkelordet, men fortsatt ikke har kryptert klarteksten fullstendig, kan du igjen bruke bokstavene i nøkkelordet som en skiftkode på de tilsvarende bokstavene i resten av teksten.

4. Fortsett denne prosessen til hele meldingen er kryptert.

For å illustrere, anta at den private nøkkelen din er "GOLD", og at du ønsker å kryptere meldingen "CRYPTOGRAPHY". I så fall vil du gå frem på følgende måte i henhold til Vigenère-krypteringen:


- $c_0 = [(2 + 6) \mod 26] = 8 = I$
- $c_1 = [(17 + 14) \mod 26] = 5 = F$
- $c_2 = [(24 + 11) \mod 26] = 9 = J$
- $c_3 = [(15 + 3) \mod 26] = 18 = S$
- $c_4 = [(19 + 6) \mod 26] = 25 = Z$
- $c_5 = [(14 + 14) \mod 26] = 2 = C$
- $c_6 = [(6 + 11) \mod 26] = 17 = R$
- $c_7 = [(17 + 3) \mod 26] = 20 = U$
- $c_8 = [(0 + 6) \mod 26] = 6 = G$
- $c_9 = [(15 + 14) \mod 26] = 3 = D$
- $c_{10} = [(7 + 11) \mod 26] = 18 = S$
- $c_{11} = [(24 + 3) \mod 26] = 1 = B$

Dermed er krypteringsteksten $c$ = "IFJSZCRUGDSB".

Et annet kjent eksempel på en stream cipher er **one-time pad**. Med en one-time pad lager du ganske enkelt en streng med tilfeldige biter som er like lange som klartekstmeldingen, og produserer krypteringsteksten ved hjelp av XOR-operasjonen. Den private nøkkelen og nøkkelstrømmen er derfor ekvivalente med en one-time pad.

Mens Shift-chiffrene og Vigenere-chiffrene er svært usikre i moderne tid, er engangskoden svært sikker hvis den brukes riktig. Den mest kjente anvendelsen av engangskoden var, i hvert fall frem til 1980-tallet, for **Washington-Moskva-hotlinen**. [4]

Hotlinen er en direkte kommunikasjonslinje mellom Washington og Moskva for hastesaker som ble opprettet etter Cubakrisen. Teknologien har endret seg i årenes løp. I dag omfatter den en direkte fiberoptisk kabel samt to satellittforbindelser (for redundans), som gjør det mulig å sende e-post og tekstmeldinger. Forbindelsen ender på forskjellige steder i USA. Pentagon, Det hvite hus og Raven Rock Mountain er kjente endepunkter. I motsetning til hva mange tror, har hotlinen aldri involvert telefoner.

I hovedsak fungerte engangskoden på følgende måte. Både Washington og Moskva hadde to sett med tilfeldige tall. Ett sett med tilfeldige tall, laget av russerne, gjaldt kryptering og dekryptering av alle meldinger på russisk. Ett sett med tilfeldige tall, laget av amerikanerne, gjaldt kryptering og dekryptering av alle meldinger på engelsk. Fra tid til annen ble flere tilfeldige tall levert til den andre siden av betrodde kurerer.

Washington og Moskva kunne da kommunisere i hemmelighet ved å bruke disse tilfeldige tallene til å lage engangskoder. Hver gang man skulle kommunisere, brukte man den neste porsjonen med tilfeldige tall til meldingen.

Selv om engangskoden er svært sikker, har den betydelige praktiske begrensninger: Nøkkelen må være like lang som meldingen, og ingen del av en engangskode kan brukes om igjen. Det betyr at du må holde styr på hvor du befinner deg i engangskoden, lagre et enormt antall biter og utveksle tilfeldige biter med motpartene dine fra tid til annen. Derfor brukes ikke engangskoden ofte i praksis.

I stedet er de vanligste strømmechiffrene som brukes i praksis, **pseudotilfeldige strømmechiffre**. Salsa20 og en nært beslektet variant kalt ChaCha er eksempler på mye brukte pseudotilfeldige strømchiffre.

Med disse pseudotilfeldige strømchiffrene velger du først en tilfeldig nøkkel K som er kortere enn lengden på klarteksten. En slik tilfeldig nøkkel K lages vanligvis av datamaskinen vår på grunnlag av uforutsigbare data som den samler inn over tid, for eksempel tiden mellom nettverksmeldinger, musebevegelser og så videre.

Denne tilfeldige nøkkelen $K$ settes deretter inn i en ekspansjonsalgoritme som lager en pseudotilfeldige nøkkelstrøm som er like lang som meldingen. Du kan spesifisere nøyaktig hvor lang nøkkelstrømmen skal være (f.eks. 500 bits, 1000 bits, 1200 bits, 29 117 bits osv.).

En pseudotil tilfeldig nøkkelstrøm ser ut *som om* den er valgt helt tilfeldig fra mengden av alle strenger med samme lengde. Kryptering med en pseudotilfeldige nøkkelstrøm ser derfor ut som om den hadde blitt gjort med en one-time pad. Men det er selvfølgelig ikke tilfelle.

Ettersom den private nøkkelen vår er kortere enn nøkkelstrømmen, og ekspansjonsalgoritmen vår må være deterministisk for at krypterings-/dekrypteringsprosessen skal fungere, kan ikke alle nøkkelstrømmer av den aktuelle lengden ha blitt resultatet av ekspansjonsoperasjonen vår.

Anta for eksempel at den private nøkkelen vår har en lengde på 128 bits, og at vi kan sette den inn i en utvidelsesalgoritme for å skape en mye lengre nøkkelstrøm, for eksempel på 2500 bits. Ettersom ekspansjonsalgoritmen vår må være deterministisk, kan algoritmen vår maksimalt velge $1/2^{128}$ strenger med en lengde på 2500 bit. En slik nøkkelstrøm kan altså aldri velges helt tilfeldig fra alle strengene med samme lengde.

Vår definisjon av en stream cipher har to aspekter: (1) en nøkkelstrøm som er like lang som klarteksten, genereres ved hjelp av en privat nøkkel, og (2) denne nøkkelstrømmen kombineres med klarteksten, vanligvis ved hjelp av en XOR-operasjon, for å produsere chifferteksten.

Noen ganger defineres betingelse (1) strengere, ved å hevde at nøkkelstrømmen spesifikt må være pseudotilfeldige. Dette betyr at verken shift cipher eller one-time pad regnes som stream ciphers.

Jeg mener at en bredere definisjon av betingelse (1) gjør det enklere å organisere krypteringssystemer. I tillegg betyr det at vi ikke trenger å slutte å kalle et bestemt krypteringsopplegg for en strømkryptering bare fordi vi finner ut at det faktisk ikke baserer seg på pseudotilfeldige nøkkelstrømmer.

**Noter:**

[4] Crypto Museum, "Washington-Moscow hotline", 2013, tilgjengelig på [https://www.cryptomuseum.com/crypto/hotline/index.htm](https://www.cryptomuseum.com/crypto/hotline/index.htm).

## Blokkchiffer

<chapterId>2df52d51-943d-5df7-9d49-333e4c5d97b7</chapterId>

Den første måten en **blokkchiffer** vanligvis forstås på, er som noe mer primitivt enn en streamchiffer: En kjernealgoritme som utfører en lengdebevarende transformasjon på en streng av en passende lengde ved hjelp av en nøkkel. Denne algoritmen kan brukes til å lage krypteringsskjemaer og kanskje også andre typer kryptografiske skjemaer.

En blokkchiffer kan ofte ta inndatastrenger av varierende lengde, for eksempel 64, 128 eller 256 bits, samt nøkler av varierende lengde, for eksempel 128, 192 eller 256 bits. Selv om noen detaljer i algoritmen kan endres avhengig av disse variablene, endres ikke selve kjernealgoritmen. Hvis den gjorde det, ville vi snakket om to forskjellige blokkchiffre. Merk at bruken av terminologien for kjernealgoritmen her er den samme som for krypteringsskjemaer.

En illustrasjon av hvordan en blokkchiffer fungerer, kan ses i *Figur 4* nedenfor. En melding $M$ med lengde $L$ og en nøkkel $K$ fungerer som inndata til blokkchiffreringen. Den sender ut en melding $M'$ av lengde $L$. Nøkkelen trenger ikke nødvendigvis å være like lang som $M$ og $M'$ for de fleste blokkchiffre.

*Figur 4: En blokkchiffer*

![Figure 4: A block cipher](assets/Figure4-4.webp "Figure 4: A block cipher")

En blokkchiffer i seg selv er ikke et krypteringsskjema. Men en blokkchiffer kan brukes med ulike **operasjonsmåter** for å produsere forskjellige krypteringsskjemaer. En operasjonsmåte legger ganske enkelt til noen ekstra operasjoner utenfor blokkchiffreringen.

For å illustrere hvordan dette fungerer, kan vi tenke oss en blokkchiffer (BC) som krever en 128-biters inndatastreng og en 128-biters privat nøkkel. Figur 5 nedenfor viser hvordan denne blokkchiffreringen kan brukes sammen med **elektronisk kodebokmodus** (**ECB-modus**) for å lage et krypteringsskjema. (Ellipsene til høyre indikerer at du kan gjenta dette mønsteret så lenge det er nødvendig).

*Figur 5: En blokkchiffer med ECB-modus*

![Figure 5: A block cipher with ECB mode](assets/Figure4-5.webp "Figure 5: A block cipher with ECB mode")

Prosessen for elektronisk kodebokskryptering med blokkchiffer er som følger. Se om du kan dele opp klartekstmeldingen i 128-bits blokker. Hvis ikke, legger du til **padding** i meldingen, slik at resultatet kan deles jevnt med blokkstørrelsen på 128 bits. Dette er dataene som brukes til krypteringsprosessen.

Del nå dataene i biter av 128-biters strenger ($M_1$, $M_2$, $M_3$, og så videre). Kjør hver 128-biters streng gjennom blokkchiffreringen med 128-biters nøkkelen for å produsere 128-biters biter med chiffertekst ($C_1$, $C_2$, $C_3$, og så videre). Når disse delene kombineres på nytt, danner de den fullstendige krypteringsteksten.

Dekryptering er bare den omvendte prosessen, selv om mottakeren trenger en gjenkjennelig måte å fjerne eventuell utfylling fra de dekrypterte dataene på for å produsere den opprinnelige meldingen i klartekst.

Selv om det er relativt enkelt, mangler en blokkchiffer med elektronisk kodebokmodus sikkerhet. Dette skyldes at den fører til **deterministisk kryptering**. To identiske 128-biters datastrenger blir kryptert på nøyaktig samme måte. Denne informasjonen kan utnyttes.

I stedet bør ethvert krypteringsskjema som er konstruert fra en blokkchiffer, være **probabilistisk**: Det vil si at krypteringen av en hvilken som helst melding $M$, eller en hvilken som helst spesifikk del av $M$, generelt sett bør gi et annet resultat hver gang. [5]

**CBC-modus** (**CBC-modus**) er sannsynligvis den vanligste modusen som brukes sammen med en blokkchiffer. Kombinasjonen gir, hvis den gjøres riktig, et probabilistisk krypteringsskjema. Du kan se en illustrasjon av denne modusen i *Figur 6* nedenfor.

*Figur 6: En blokkchiffer med CBC-modus*

![Figure 6: A block cipher with CBC mode](assets/Figure4-6.webp "Figure 6: A block cipher with CBC mode")

Anta at blokkstørrelsen igjen er 128 bits. Da må du igjen sørge for at den opprinnelige klartekstmeldingen får den nødvendige utfyllingen.

Deretter XOR-ekvivalerer du den første 128-biters delen av klarteksten med en **initialiseringsvektor** på 128 bits. Resultatet plasseres i blokkchiffreringen for å produsere en chiffertekst for den første blokken. For den andre blokken på 128 bits XOR'er du først klarteksten med chifferteksten fra den første blokken, før du setter den inn i blokkchiffreringen. Du fortsetter denne prosessen til du har kryptert hele klartekstmeldingen.

Når du er ferdig, sender du den krypterte meldingen sammen med den ukrypterte initialiseringsvektoren til mottakeren. Mottakeren må kjenne til initialiseringsvektoren, ellers kan hun ikke dekryptere chifferteksten.

Denne konstruksjonen er mye sikrere enn elektronisk kodebokmodus når den brukes riktig. Du bør først sørge for at initialiseringsvektoren er en tilfeldig eller pseudotil tilfeldig streng. I tillegg bør du bruke en annen initialiseringsvektor hver gang du bruker dette krypteringsskjemaet.

Initialiseringsvektoren bør med andre ord være en tilfeldig eller pseudotil tilfeldig nonce, der en **nonce** står for "et tall som bare brukes én gang" Hvis du følger denne praksisen, vil CBC-modus med en blokkchiffer sørge for at to identiske klartekstblokker som regel krypteres forskjellig hver gang.

Til slutt skal vi se nærmere på **output feedback-modus** (**OFB-modus**). Du kan se en illustrasjon av denne modusen i *Figur 7*.

*Figur 7: En blokkchiffer med OFB-modus*

![Figure 7: A block cipher with OFB mode](assets/Figure4-7.webp "Figure 7: A block cipher with OFB mode")

I OFB-modus velger du også en initialiseringsvektor. Men her settes initialiseringsvektoren for den første blokken direkte inn i blokkchiffreringen med nøkkelen din. De resulterende 128 bitene behandles deretter som en nøkkelstrøm. Denne nøkkelstrømmen XOR-es med klarteksten for å produsere krypteringsteksten for blokken. For påfølgende blokker bruker du nøkkelstrømmen fra den forrige blokken som input i blokkchiffreringen, og gjentar trinnene.

Hvis du ser nøye etter, ser du at det som faktisk er skapt her fra blokkchiffreringen med OFB-modus, er en strømchiffer. Du genererer nøkkelstrømpartier på 128 bits til du har lengden på klarteksten (ved å forkaste de bitene du ikke trenger fra den siste 128-biters nøkkelstrømpartiet). Deretter XOR-ekvivalerer du nøkkelstrømmen med klartekstmeldingen for å få krypteringsteksten.

I forrige avsnitt om strømmekryptering sa jeg at man produserer en nøkkelstrøm ved hjelp av en privat nøkkel. For å være helt nøyaktig trenger den ikke bare å opprettes med en privat nøkkel. Som du kan se i OFB-modus, produseres nøkkelstrømmen med støtte fra både en privat nøkkel og en initialiseringsvektor.

Merk at det, som med CBC-modus, er viktig å velge en pseudotilgjengelig eller tilfeldig nonce for initialiseringsvektoren hver gang du bruker en blokkchiffer i OFB-modus. Ellers vil den samme 128-biters meldingsstrengen som sendes i forskjellige kommunikasjoner, bli kryptert på samme måte. Dette er én måte å skape probabilistisk kryptering med en stream cipher.

Noen strømchiffre bruker bare en privat nøkkel til å opprette en nøkkelstrøm. For disse strømmekrypteringskrypteringene er det viktig at du bruker en tilfeldig nonce til å velge den private nøkkelen for hver enkelt kommunikasjon. Hvis ikke vil resultatet av kryptering med disse strømchiffrene også være deterministisk, noe som kan føre til sikkerhetsproblemer.

Den mest populære moderne blokkchiffren er **Rijndael-chiffren**. Det var vinnerbidraget av femten bidrag til en konkurranse som ble arrangert av National Institute of Standards and Technology (NIST) mellom 1997 og 2000 for å erstatte en eldre krypteringsstandard, **data encryption standard** (**DES**).

Rijndael-krypteringen kan brukes med ulike spesifikasjoner for nøkkellengder og blokkstørrelser, samt i ulike driftsmodi. Komiteen for NIST-konkurransen vedtok en begrenset versjon av Rijndael-krypteringen - nemlig en som krever 128-biters blokkstørrelser og nøkkellengder på enten 128 bits, 192 bits eller 256 bits - som en del av **advanced encryption standard** (**AES**). Dette er egentlig hovedstandarden for symmetriske krypteringsapplikasjoner. Den er så sikker at til og med NSA tilsynelatende er villig til å bruke den med 256-bits nøkler for topphemmelige dokumenter. [6]

AES-blokkchiffrering forklares i detalj i *Kapittel 5*.

**Noter:**

[5] Betydningen av probabilistisk kryptering ble først understreket av Shafi Goldwasser og Silvio Micali, "Probabilistic encryption", _Journal of Computer and System Sciences_, 28 (1984), 270-99.

[6] Se NSA, "Commercial National Security Algorithm Suite", [https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm](https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm).

## Rydd opp i forvirringen

<chapterId>121c1858-27e3-5862-b0ce-4ff2f70f9f0f</chapterId>

Forvirringen rundt skillet mellom blokkchiffre og streamchiffre oppstår fordi folk av og til forstår begrepet blokkchiffer som en *blokkchiffer med en blokkmodus for kryptering*.

Se på ECB- og CBC-modusene i forrige avsnitt. Disse krever spesifikt at dataene som skal krypteres, er delelige med blokkstørrelsen (noe som betyr at du kanskje må bruke utfylling for den opprinnelige meldingen). I tillegg blir dataene i disse modusene også behandlet direkte av blokkchiffreringen (og ikke bare kombinert med resultatet av en blokkchifferoperasjon som i OFB-modus).

Alternativt kan du definere en **blokkchiffer** som et krypteringsskjema som opererer på blokker med fast lengde av meldingen om gangen (hvor hver blokk må være lengre enn en byte, ellers kollapser den til en streamchiffer). Både krypteringsdataene og krypteringsteksten må dele seg jevnt i denne blokkstørrelsen. Vanligvis er blokkstørrelsen 64, 128, 192 eller 256 bits lang. En stream cipher kan derimot kryptere alle meldinger i biter på én bit eller byte om gangen.

Med denne mer spesifikke forståelsen av blokkchiffer kan man faktisk hevde at moderne krypteringsskjemaer enten er stream- eller blokkchiffer. Heretter vil jeg bruke begrepet blokkchiffer i den mer generelle betydningen, med mindre noe annet er spesifisert.

Diskusjonen om OFB-modus i forrige avsnitt reiser også et annet interessant poeng. Noen strømchiffre er bygget opp fra blokkchiffre, som Rijndael med OFB. Andre, som Salsa20 og ChaCha, er ikke laget av blokkchiffre. Man kan kalle de sistnevnte for **primitive strømchiffre**. (Det finnes egentlig ikke noe standardisert begrep for å referere til slike strømmechiffre)

Når man snakker om fordeler og ulemper ved stream ciphers og block ciphers, sammenligner man vanligvis primitive stream ciphers med krypteringsopplegg basert på block ciphers.

Mens du alltid enkelt kan konstruere en stream cipher fra en block cipher, er det vanligvis svært vanskelig å konstruere en type konstruksjon med en blokk-krypteringsmodus (for eksempel med CBC-modus) fra en primitiv stream cipher.

Ut fra denne diskusjonen bør du nå forstå *Figur 8*. Den gir en oversikt over symmetriske krypteringsskjemaer. Vi bruker tre typer krypteringsskjemaer: primitive strømchiffre, blokkchiffre og blokkchiffre i blokkmodus (også kalt "blokkchiffre" i diagrammet).

*Figur 8: Oversikt over symmetriske krypteringsmetoder*

![Figure 8: Overview of symmetric encryption schemes](assets/Figure4-8.webp "Figure 8: Overview of symmetric encryption schemes")

## Autentiseringskoder for meldinger

<chapterId>19fa7c00-db59-56a0-9654-5350a137939d</chapterId>

Kryptering handler om hemmeligholdelse. Men kryptografi handler også om bredere temaer, som meldingsintegritet, autentisitet og uavviselighet. Såkalte **message authentication codes** (MACs) er symmetriske kryptografiske systemer som støtter autentisitet og integritet i kommunikasjon.

Hvorfor er det behov for noe annet enn hemmeligholdelse i kommunikasjon? Anta at Bob sender Alice en melding med praktisk talt ubrytelig kryptering. En angriper som snapper opp denne meldingen, vil ikke kunne få noen vesentlig innsikt i innholdet. Angriperen har imidlertid fortsatt minst to andre angrepsvektorer tilgjengelig:

1. Hun kunne snappe opp krypteringsteksten, endre innholdet og sende den endrede krypteringsteksten videre til Alice.

2. Hun kan blokkere Bobs melding helt og holdent og sende sin egen krypteringstekst.

I begge disse tilfellene er det ikke sikkert at angriperen har innsikt i innholdet i krypteringstekstene (1) og (2). Men hun kan likevel forårsake betydelig skade på denne måten. Det er her autentiseringskoder for meldinger blir viktige.

Meldingsautentiseringskoder er løst definert som symmetriske kryptografiske skjemaer med tre algoritmer: en nøkkelgenereringsalgoritme, en tagggenereringsalgoritme og en verifiseringsalgoritme. En sikker MAC sikrer at taggene er **eksistensielt uforfalskelige** for alle angripere - det vil si at de ikke kan opprette en tagg på meldingen som verifiseres, med mindre de har den private nøkkelen.

Bob og Alice kan bekjempe manipulering av en bestemt melding ved hjelp av en MAC. Anta at de for øyeblikket ikke bryr seg om hemmeligholdelse. De vil bare forsikre seg om at meldingen Alice har mottatt, faktisk kommer fra Bob og ikke er endret på noen måte.

Prosessen er illustrert i *Figur 9*. For å bruke en **MAC** (Message Authentication Code), må de først generere en privat nøkkel $K$ som deles mellom dem. Bob lager en tagg $T$ for meldingen ved hjelp av den private nøkkelen $K$. Deretter sender han meldingen og taggen til Alice. Hun kan så verifisere at Bob faktisk har laget taggen ved å kjøre den private nøkkelen, meldingen og taggen gjennom en verifiseringsalgoritme.

*Figur 9: Oversikt over symmetriske krypteringsmetoder*

![Figure 9: Overview of symmetric encryption schemes](assets/Figure4-9.webp "Figure 9: Overview of symmetric encryption schemes")

På grunn av **eksistensiell uforfalskbarhet** kan en angriper ikke endre meldingen $M$ på noen måte eller lage sin egen melding med en gyldig tag. Dette gjelder selv om angriperen observerer taggene til mange meldinger mellom Bob og Alice som bruker den samme private nøkkelen. En angriper kan i beste fall hindre Alice i å motta meldingen $M$ (et problem som kryptografi ikke kan løse).

En MAC garanterer at en melding faktisk ble opprettet av Bob. Denne autentisiteten innebærer automatisk meldingsintegritet - det vil si at hvis Bob har opprettet en melding, så er den ipso facto ikke endret på noen måte av en angriper. Så fra nå av bør enhver bekymring for autentisering automatisk forstås som en bekymring for integritet.

Selv om jeg har skilt mellom autentisitet og integritet i min diskusjon, er det også vanlig å bruke disse begrepene som synonymer. De refererer da til ideen om meldinger som både er skapt av en bestemt avsender og ikke er endret på noen måte. I denne ånden kalles meldingsautentiseringskoder ofte også **meldingsintegritetskoder**.

## Godkjent kryptering

<chapterId>33f2ec9b-9fb4-5c61-8fb4-50836270a144</chapterId>

Vanligvis ønsker man å garantere både hemmelighold og autentisitet i kommunikasjonen, og derfor brukes krypteringsordninger og MAC-ordninger vanligvis sammen.

Et **autentisert krypteringsopplegg** er et opplegg som kombinerer kryptering med en MAC på en svært sikker måte. Det må oppfylle standardene for eksistensiell uforfalskbarhet samt et svært sterkt begrep om hemmelighold, nemlig et som er motstandsdyktig mot **angrep med utvalgt chiffertekst**. [7]

For at et krypteringsopplegg skal være motstandsdyktig mot angrep med valgt chiffertekst, må det oppfylle kravene til **ikke-malleabilitet**: Det vil si at enhver endring av en chiffertekst som utføres av en angriper, enten skal gi en ugyldig chiffertekst eller en chiffertekst som dekrypteres til en klartekst som ikke har noe forhold til den opprinnelige. [8]

Ettersom et autentisert krypteringsskjema sikrer at en chiffertekst som opprettes av en angriper, alltid er ugyldig (ettersom taggen ikke blir verifisert), oppfyller det standardene for motstand mot valgt chiffertekst-angrep. Interessant nok kan du bevise at et autentisert krypteringsskjema alltid kan opprettes ut fra kombinasjonen av en eksistensielt uforfalskelig MAC og et krypteringsskjema som oppfyller et mindre sterkt sikkerhetsbegrep, kjent som **sikkerhet mot valgte klartekst-angrep**.

Vi skal ikke gå inn på alle detaljene i konstruksjonen av autentiserte krypteringssystemer. Men det er viktig å kjenne til to detaljer i konstruksjonen.

For det første håndterer et autentisert krypteringsopplegg først krypteringen og oppretter deretter en meldingstagg på krypteringsteksten. Det viser seg at andre tilnærminger - for eksempel å kombinere krypteringsteksten med en tagg på klarteksten, eller først opprette en tagg og deretter kryptere både klarteksten og taggen - er usikre. I tillegg må begge operasjonene ha sin egen tilfeldig valgte private nøkkel, ellers er sikkerheten alvorlig kompromittert.

Det nevnte prinsippet gjelder mer generelt: *du bør alltid bruke forskjellige nøkler når du kombinerer grunnleggende kryptografiske ordninger*.

Et autentisert krypteringsopplegg er vist i *Figur 10*. Bob oppretter først en chiffertekst $C$ fra meldingen $M$ ved hjelp av en tilfeldig valgt nøkkel $K_C$. Deretter lager han en meldingstagg $T$ ved å kjøre krypteringsteksten og en annen tilfeldig valgt nøkkel $K_T$ gjennom tagggenereringsalgoritmen. Både krypteringsteksten og meldingstaggen sendes til Alice.

Alice sjekker nå først om taggen er gyldig, gitt chifferteksten $C$ og nøkkelen $K_T$. Hvis den er gyldig, kan hun deretter dekryptere meldingen ved hjelp av nøkkelen $K_C$. Ikke bare er hun sikret en meget sterk grad av hemmelighold i kommunikasjonen, men hun vet også at meldingen ble opprettet av Bob.

*Figur 10: Et autentisert krypteringsopplegg*

![Figure 10: An authenticated encryption scheme](assets/Figure4-10.webp "Figure 10: An authenticated encryption scheme")

Hvordan opprettes MAC-er? MAC-er kan opprettes på flere måter, men en vanlig og effektiv måte å opprette dem på er ved hjelp av **kryptografiske hashfunksjoner**.

Vi kommer til å introdusere kryptografiske hashfunksjoner mer grundig i *Kapittel 6*. Inntil videre skal du bare vite at en **hash-funksjon** er en effektivt beregnbar funksjon som tar inndata av vilkårlig størrelse og gir utdata med fast lengde. Den populære hashfunksjonen **SHA-256** (secure hash algorithm 256) genererer for eksempel alltid en 256-biters utdata, uavhengig av størrelsen på inndataene. Noen hashfunksjoner, som SHA-256, har nyttige bruksområder innen kryptografi.

Den vanligste typen tagg som produseres med en kryptografisk hashfunksjon, er **hash-basert meldingsautentiseringskode** (HMAC). Prosessen er illustrert i *Figur 11*. En part produserer to forskjellige nøkler fra en privat nøkkel $K$, den indre nøkkelen $K_1$ og den ytre nøkkelen $K_2$. Klarteksten $M$ eller chifferteksten $C$ blir deretter hashet sammen med den indre nøkkelen. Resultatet $T'$ hashes deretter med den ytre nøkkelen for å produsere meldingstaggen $T$.

Det finnes en rekke hashfunksjoner som kan brukes til å opprette en HMAC. Den mest brukte hashfunksjonen er SHA-256.

*Figur 11: HMAC*

![Figure 11: HMAC](assets/Figure4-11.webp "Figure 11: HMAC")

**Noter:**

[7] De spesifikke resultatene som diskuteres i dette avsnittet, er hentet fra Katz og Lindell, s. 131-47.

[8] Teknisk sett er definisjonen av angrep med valgt chiffertekst en annen enn begrepet ikke-malleabilitet. Men du kan vise at disse to sikkerhetsbegrepene er ekvivalente.

## Sikre kommunikasjonsøkter

<chapterId>c7f7dcd3-bbed-53ed-a43d-039da0f180c5</chapterId>

Anta at to parter er i en kommunikasjonsøkt, slik at de sender flere meldinger frem og tilbake.

En autentisert krypteringsmetode gjør det mulig for en mottaker av en melding å verifisere at den er opprettet av partneren i kommunikasjonsøkten (så lenge den private nøkkelen ikke har lekket). Dette fungerer godt nok for en enkelt melding. Vanligvis sender imidlertid to parter meldinger frem og tilbake i en kommunikasjonsøkt. I en slik situasjon vil en enkel, autentisert krypteringsmetode som beskrevet i forrige avsnitt, ikke gi tilstrekkelig sikkerhet.

Hovedårsaken er at et autentisert krypteringsopplegg ikke gir noen garanti for at meldingen faktisk også ble sendt av den agenten som opprettet den i en kommunikasjonsøkt. Se på følgende tre angrepsvektorer:

1. **Replay-angrep**: En angriper sender på nytt en chiffertekst og en tagg som hun har snappet opp mellom to parter på et tidligere tidspunkt.

2. **Rekkefølgeangrep**: En angriper fanger opp to meldinger på forskjellige tidspunkter og sender dem til mottakeren i omvendt rekkefølge.

3. **Refleksjonsangrep**: En angriper observerer en melding som sendes fra A til B, og sender også denne meldingen til A.

Selv om angriperen ikke har kjennskap til krypteringsteksten og ikke kan lage forfalskede krypteringstekster, kan angrepene ovenfor likevel forårsake betydelig skade på kommunikasjonen.

Anta for eksempel at en bestemt melding mellom de to partene innebærer overføring av finansielle midler. Et replay-angrep kan overføre pengene en gang til. Et vanlig, autentisert krypteringssystem har ikke noe forsvar mot slike angrep.

Heldigvis kan denne typen angrep enkelt avverges i en kommunikasjonsøkt ved hjelp av **identifikatorer** og **relative tidsindikatorer**.

Identifikatorer kan legges til i klartekstmeldingen før kryptering. Dette vil hindre eventuelle refleksjonsangrep. En relativ tidsindikator kan for eksempel være et sekvensnummer i en bestemt kommunikasjonsøkt. Hver part legger til et sekvensnummer i en melding før kryptering, slik at mottakeren vet i hvilken rekkefølge meldingene ble sendt. Dette eliminerer muligheten for omordningsangrep. Det eliminerer også replay-angrep. Enhver melding som en angriper sender videre, vil ha et gammelt sekvensnummer, og mottakeren vil vite at meldingen ikke skal behandles på nytt.

For å illustrere hvordan sikre kommunikasjonsøkter fungerer, antar vi at Alice og Bob gjør det samme. De sender til sammen fire meldinger frem og tilbake. I *Figur 11* nedenfor kan du se hvordan et autentisert krypteringsopplegg med identifikatorer og sekvensnumre vil fungere.

Kommunikasjonsøkten starter med at Bob sender en krypteringstekst $C_{0,B}$ til Alice med en meldingstag $T_{0,B}$. Krypteringsteksten inneholder meldingen, i tillegg til en identifikator (BOB) og et sekvensnummer (0). Taggen $T_{0,B}$ er laget over hele krypteringsteksten. I den påfølgende kommunikasjonen opprettholder Alice og Bob denne protokollen, og oppdaterer feltene etter behov.

*Figur 12: En sikker kommunikasjonsøkt*

![Figure 12: A secure communication session](assets/Figure4-12.webp "Figure 12: A secure communication sessesion")

# RC4 og AES

<partId>a48c4a7d-0a41-523f-a4ab-1305b4430324</partId>

## RC4-strømkryptering

<chapterId>5caec5bd-5a77-56c9-b5e6-1e86f0d294aa</chapterId>

I dette kapittelet skal vi se nærmere på detaljene i et krypteringsopplegg med en moderne primitiv stream cipher, RC4 (eller "Rivest cipher 4"), og en moderne block cipher, AES. Mens RC4-krypteringen har falt i unåde som krypteringsmetode, er AES standarden for moderne symmetrisk kryptering. Disse to eksemplene bør gi et bedre inntrykk av hvordan symmetrisk kryptering fungerer under panseret.

___

For å få en forståelse av hvordan moderne pseudotilfeldige strømchiffre fungerer, vil jeg fokusere på RC4-strømchiffret. Dette er en pseudotilfeldige strømchiffer som ble brukt i sikkerhetsprotokollene WEP og WAP for trådløse aksesspunkter, samt i TLS. Ettersom RC4 har mange påviste svakheter, har den falt i unåde. Faktisk forbyr Internet Engineering Task Force nå bruk av RC4-suiter i klient- og serverapplikasjoner i alle tilfeller av TLS. Likevel fungerer den godt som et eksempel for å illustrere hvordan en primitiv stream cipher fungerer.

Først vil jeg vise hvordan man krypterer en klartekstmelding med en baby RC4-kryptering. Anta at klartekstmeldingen vår er "SOUP" Krypteringen med baby-RC4-krypteringen vår går da i fire trinn.

### Trinn 1

Først definerer du en matrise **S** med $S[0] = 0$ til $S[7] = 7$. En matrise betyr her ganske enkelt en foranderlig samling av verdier organisert etter en indeks, også kalt en liste i noen programmeringsspråk (f.eks. Python). I dette tilfellet går indeksen fra 0 til 7, og verdiene går også fra 0 til 7. Så **S** er som følger:


- $S = [0, 1, 2, 3, 4, 5, 6, 7]$

Verdiene her er ikke ASCII-tall, men desimalverdiene av 1-byte-strenger. Verdien 2 vil altså være lik $0000 \ 0011$. Lengden på matrisen **S** er dermed 8 byte.

### Trinn 2

For det andre definerer du en nøkkelmatrise **K** på 8 byte ved å velge en nøkkel på mellom 1 og 8 byte (ingen brøkdeler av byte er tillatt). Ettersom hver byte er på 8 bits, kan du velge et hvilket som helst tall mellom 0 og 255 for hver byte i nøkkelen.

Anta at vi velger nøkkelen **k** som $[14, 48, 9]$, slik at den har en lengde på 3 byte. Hver indeks i nøkkelarrayen vår blir da satt i henhold til desimalverdien for det aktuelle elementet i nøkkelen, i rekkefølge. Hvis du går gjennom hele nøkkelen, begynner du på nytt fra begynnelsen, helt til du har fylt de 8 sporene i nøkkelmatrisen. Nøkkelmatrisen vår er altså som følger:


- $K = [14, 48, 9, 14, 48, 9, 14, 48]$

### Trinn 3

For det tredje transformerer vi matrisen **S** ved hjelp av nøkkelmatrisen **K**, i en prosess som kalles **nøkkelplanlegging**. Prosessen er som følger i pseudokode:


- Opprett variablene **j** og **i**
- Sett variabelen $j = 0$
- For hver $i$ fra 0 til 7:
    - Sett $j = (j + S[i] + K[i]) \mod 8$
    - Bytt om $S[i]$ og $S[j]$

Transformasjonen av matrisen **S** er beskrevet i *Tabell 1*.

Til å begynne med kan du se den opprinnelige tilstanden til **S** som $[0, 1, 2, 3, 4, 5, 6, 7]$ med en innledende verdi på 0 for **j**. Dette vil bli transformert ved hjelp av nøkkelmatrisen $[14, 48, 9, 14, 48, 9, 14, 48]$.

For-løkken starter med $i = 0$. I henhold til pseudokoden vår ovenfor blir den nye verdien av **j** 6 ($j = (j + S[0] + K[0]) \mod 8 = (0 + 0 + 14) \mod 8 = 6 \mod 8$). Ved å bytte om $S[0]$ og $S[6]$ blir tilstanden til **S** etter én runde $[6, 1, 2, 3, 4, 5, 0, 7]$.

I neste rad er $i = 1$. Ved å gå gjennom for-løkken igjen får **j** verdien 7 ($j = (j + S[1] + K[1]) \mod 8 = (6 + 1 + 48) \mod 8 = 55 \mod 8 = 7 \mod 8$). Ved å bytte ut $S[1]$ og $S[7]$ fra den nåværende tilstanden til **S**, $[6, 1, 2, 3, 4, 5, 0, 7]$, får vi $[6, 7, 2, 3, 4, 5, 0, 1]$ etter runde 2.

Vi fortsetter med denne prosessen til vi får den siste raden nederst for matrisen **S**, $[6, 4, 1, 0, 3, 7, 5, 2]$.

*Tabell 1: Nøkkeltabell for planlegging*

| S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] | S[8] | S[9] | S[10

| ------- | --- | --- | --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |



| Initial | | 0 | | 0 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | | 1 | 2 | 3 | 4 | 5 | 6 | 7

| 1 | 0 | 6 | | 6 | 1 | 2 | 3 | 4 | 5 | 0 | 7 |

| 2 | 1 | 7 | | 6 | 7 | 2 | 3 | 4 | 5 | 0 | 1 |

| 3 | 2 | 2 | | 6 | 7 | 2 | 3 | 4 | 5 | 0 | 1 |

| 4 | 3 | 3 | | 6 | 7 | 2 | 3 | 4 | 5 | 0 | 1 |

| 5 | 4 | 3 | | 6 | 7 | 2 | 0 | 3 | 5 | 4 | 1 |

| 6 | 5 | 6 | | 6 | 4 | 2 | 0 | 3 | 7 | 5 | 1 |

| 7 | 6 | 1 | | 6 | 4 | 2 | 0 | 3 | 7 | 5 | 2 |

| 8 | 7 | 2 | | 6 | 4 | 1 | 0 | 3 | 7 | 5 | 2 |

### Trinn 4

Som et fjerde trinn produserer vi **keystream**. Dette er en pseudotilfeldige streng med en lengde som tilsvarer meldingen vi ønsker å sende. Denne vil bli brukt til å kryptere den opprinnelige meldingen "SOUP" Siden nøkkelstrømmen må være like lang som meldingen, trenger vi en nøkkelstrøm på 4 byte.

Nøkkelstrømmen produseres ved hjelp av følgende pseudokode:


- Opprett variablene **j**, **i** og **t**.
- Sett $j = 0$.
- For hver $i$ i klarteksten, fra $i = 1$ til $i = 4$, produseres hver byte av nøkkelstrømmen på følgende måte:
    - $j = (j + S[i]) \mod 8$$
    - Bytt om $S[i]$ og $S[j]$.
    - $t = (S[i] + S[j]) \mod 8$$
    - Den $i^{tredje}$ byten av nøkkelstrømmen = $S[t]$

Du kan følge beregningene i *Tabell 2*.

Den opprinnelige tilstanden til **S** er $S = [6, 4, 1, 0, 3, 7, 5, 2]$. Ved å sette $i = 1$ blir verdien av **j** 4 ($j = (j + S[i]) \mod 8 = (0 + 4) \mod 8 = 4$). Deretter bytter vi om $S[1]$ og $S[4]$ for å få transformasjonen av **S** i den andre raden, $[6, 3, 1, 0, 4, 7, 5, 2]$. Verdien av **t** er da 7 ($t = (S[i] + S[j]) \mod 8 = (3 + 4) \mod 8 = 7$). Til slutt er byten for nøkkelstrømmen $S[7]$, eller 2.

Deretter fortsetter vi å produsere de andre bytene til vi har følgende fire byte: 2, 6, 3 og 7. Hver av disse byte kan deretter brukes til å kryptere hver bokstav i klarteksten, "SOUP".

Til å begynne med kan vi ved hjelp av en ASCII-tabell se at "SOUP" kodet av desimalverdiene til de underliggende bytestrengene er "83 79 85 80". Kombinasjon med nøkkelstrømmen "2 6 3 7" gir "85 85 88 87", som forblir den samme etter en modulo 256-operasjon. I ASCII er krypteringsteksten "85 85 88 87" lik "UUXW".

Hva skjer hvis ordet som skal krypteres er lengre enn matrisen **S**? I så fall fortsetter matrisen **S** bare å transformere seg på denne måten for hver byte **i** i klarteksten, helt til vi har et antall byte i nøkkelstrømmen som tilsvarer antall bokstaver i klarteksten.

*Tabell 2: Generering av nøkkelstrømmer*

i | j | t | Keystream | S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] | S[7] | S[8] | S[9] | S[10

| --- | --- | --- | --------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |



| | 0 | | | 6 | 4 | 1 | 0 | 3 | 7 | 5 | 2 |

| 1 | 4 | 7 | 2 | 6 | 3 | 1 | 0 | 4 | 7 | 5 | 2 |

| 2 | 5 | 0 | 6 | 6 | 3 | 7 | 0 | 4 | 1 | 5 | 2 |

| 3 | 5 | 1 | 3 | 6 | 3 | 7 | 1 | 4 | 0 | 5 | 2 |

| 4 | 1 | 7 | 2 | 6 | 4 | 7 | 1 | 3 | 0 | 5 | 2 |

Eksemplet vi nettopp diskuterte, er bare en utvannet versjon av **RC4 stream cipher**. Den faktiske RC4-strømmekrypteringen har en **S**-array på 256 byte, ikke 8 byte, og en nøkkel som kan være mellom 1 og 256 byte, ikke mellom 1 og 8 byte. Nøkkelarrayen og nøkkelstrømmene produseres deretter med utgangspunkt i **S**-arrayens lengde på 256 byte. Beregningene blir enormt mye mer komplekse, men prinsippene forblir de samme. Ved å bruke den samme nøkkelen, [14,48,9], med standard RC4-kryptering, blir klartekstmeldingen "SOUP" kryptert som 67 02 ed df i heksadesimalt format.

En strømmekryptering der nøkkelstrømmen oppdateres uavhengig av klartekstmeldingen eller chifferteksten, er en **synkron strømmekryptering**. Nøkkelstrømmen er kun avhengig av nøkkelen. RC4 er et klart eksempel på en synkron strømkryptering, ettersom nøkkelstrømmen ikke har noe forhold til klarteksten eller chifferteksten. Alle de primitive strømkrypteringene vi nevnte i forrige kapittel, inkludert skiftkrypteringen, Vigenère-krypteringen og engangskrypteringen, var også av den synkrone varianten.

En **asynkron strømchiffer** har derimot en nøkkelstrøm som produseres av både nøkkelen og tidligere elementer i chifferteksten. Denne typen chiffer kalles også **selvsynkroniserende chiffer**.

Det er viktig å merke seg at nøkkelstrømmen som produseres med RC4, bør behandles som en engangsnøkkel, og du kan ikke produsere nøkkelstrømmen på nøyaktig samme måte neste gang. I stedet for å endre nøkkelen hver gang, er den praktiske løsningen å kombinere nøkkelen med en **nonce** for å produsere bystrømmen.

## AES med en 128-biters nøkkel

<chapterId>0b30886f-e620-5b8d-807b-9d84685ca8ff</chapterId>

Som nevnt i forrige kapittel, avholdt National Institute of Standards and Technology (NIST) en konkurranse mellom 1997 og 2000 for å finne en ny standard for symmetrisk kryptering. **Rijndael-krypteringen** viste seg å være det vinnende bidraget. Navnet er et ordspill på navnene til de belgiske skaperne, Vincent Rijmen og Joan Daemen.

Rijndael-krypteringen er en **blokk-kryptering**, noe som betyr at det finnes en kjernealgoritme som kan brukes med ulike spesifikasjoner for nøkkellengder og blokkstørrelser. Du kan dermed bruke den med ulike driftsmåter for å konstruere krypteringsskjemaer.

Komiteen for NIST-konkurransen vedtok en begrenset versjon av Rijndael-krypteringen - nemlig en som krever 128-bits blokkstørrelser og nøkkellengder på enten 128 bits, 192 bits eller 256 bits - som en del av **Advanced Encryption Standard (AES)**. Denne begrensede versjonen av Rijndael-krypteringen kan også brukes under flere driftsmodi. Spesifikasjonen for standarden er det som kalles **Advanced Encryption Standard (AES)**.

For å vise hvordan Rijndael-krypteringen, kjernen i AES, fungerer, vil jeg illustrere prosessen for kryptering med en 128-biters nøkkel. Nøkkelstørrelsen har innvirkning på antall runder som holdes for hver krypteringsblokk. For 128-bits nøkler kreves det 10 runder. Med 192 bits og 256 bits ville det ha vært henholdsvis 12 og 14 runder.

I tillegg vil jeg anta at AES brukes i **ECB-modus**. Dette gjør fremstillingen litt enklere og spiller ingen rolle for Rijndael-algoritmen. ECB-modus er riktignok ikke sikker i praksis, fordi den fører til deterministisk kryptering. Den mest brukte sikre modusen med AES er **CBC** (Cipher Block Chaining).

La oss kalle nøkkelen $K_0$. Konstruksjonen med de ovennevnte parameterne ser da ut som i *Figur 1*, der $M_i$ står for en del av klartekstmeldingen på 128 bits og $C_i$ for en del av krypteringsteksten på 128 bits. Padding legges til klarteksten for den siste blokken, hvis klarteksten ikke kan deles jevnt med blokkstørrelsen.

*Figur 1: AES-ECB med en 128-biters nøkkel*

![Figure 1: AES-ECB with a 128-bit key](assets/Figure5-1.webp "Figure 1: AES-ECB with a 128-bit key")

Hver 128-biters tekstblokk går gjennom ti runder i Rijndael-krypteringsskjemaet. Dette krever en separat rundenøkkel for hver runde ($K_1$ til $K_{10}$). Disse produseres for hver runde fra den opprinnelige 128-biters nøkkelen $K_0$ ved hjelp av en **nøkkelutvidelsesalgoritme**. For hver tekstblokk som skal krypteres, vil vi derfor bruke den opprinnelige nøkkelen $K_0$ i tillegg til ti separate rundenøkler. Merk at de samme 11 nøklene brukes for hver 128-biters blokk med klartekst som skal krypteres.

Algoritmen for nøkkelutvidelse er lang og kompleks. Det har liten didaktisk nytte å gå gjennom den. Du kan se gjennom nøkkelutvidelsesalgoritmen på egen hånd, hvis du ønsker det. Når rundenøklene er produsert, vil Rijndael-krypteringen manipulere den første 128-biters blokken med klartekst, $M_1$, som vist i *Figur 2*. Vi vil nå gå gjennom disse trinnene.

*Figur 2: Manipulering av $M_1$ med Rijndael-krypteringen:*

**Runde 0:**


- XOR $M_1$ og $K_0$ for å produsere $S_0$

---
**Runde n for n = {1,...,9}:**


- XOR $S_{n-1}$ og $K_n$
- Bytesubstitusjon
- Skift rader
- Bland kolonner
- XOR $S$ og $K_n$ for å produsere $S_n$

---
**Runde 10:**


- XOR $S_9$ og $K_{10}$
- Bytesubstitusjon
- Skift rader
- XOR $S$ og $K_{10}$ for å produsere $S_{10}$
- $S_{10}$ = $C_1$

### Runde 0

Runde 0 av Rijndael-krypteringen er enkel. En matrise $S_0$ produseres ved en XOR-operasjon mellom 128-biters klartekst og den private nøkkelen. Det vil si at


- $S_0 = M_1 \oplus K_0$

### Runde 1

I runde 1 kombineres først matrisen $S_0$ med rundenøkkelen $K_1$ ved hjelp av en XOR-operasjon. Dette produserer en ny tilstand på $S$.

For det andre utføres operasjonen **byte substitusjon** på den nåværende tilstanden til $S$. Den fungerer ved å ta hver byte i $S$-arrayen på 16 byte og erstatte den med en byte fra en array som kalles **Rijndaels S-boks**. Hver byte har en unik transformasjon, og resultatet er en ny tilstand for $S$. Rijndaels S-boks er vist i *Figur 3*.

*Figur 3: Rijndaels S-boks*

| 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 0A | 0B | 0C | 0D | 0E | 0F | | 0B | 0C | 0D | 0E | 0F

| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| 00 | 63 | 7C | 77 | 7B | F2 | 6B | 6F | C5 | 30 | 01 | 67 | 2B | FE | D7 | AB | 76 |

| 10 | CA | 82 | C9 | 7D | FA | 59 | 47 | F0 | AD | D4 | A2 | AF | 9C | A4 | 72 | C0 |

| 20 | B7 | FD | 93 | 26 | 36 | 3F | F7 | CC | 34 | A5 | E5 | F1 | 71 | D8 | 31 | 15 |

| 30 | 04 | C7 | 23 | C3 | 18 | 96 | 05 | 9A | 07 | 12 | 80 | E2 | EB | 27 | B2 | 75 |

| 40 | 09 | 83 | 2C | 1A | 1B | 6E | 5A | A0 | 52 | 3B | D6 | B3 | 29 | E3 | 2F | 84 |

| 50 | 53 | D1 | 00 | ED | 20 | FC | B1 | 5B | 6A | CB | BE | 39 | 4A | 4C | 58 | CF | | 50 | 53 | D1 | 00 | ED | 20 | FC | B1 | 5B | 6A | CB | BE | 39 | 4A | 4C | 58 | CF

| 60 | D0 | EF | AA | FB | 43 | 4D | 33 | 85 | 45 | F9 | 02 | 7F | 50 | 3C | 9F | A8 |

| 70 | 51 | A3 | 40 | 8F | 92 | 9D | 38 | F5 | BC | B6 | DA | 21 | 10 | FF | F3 | D2 |

| 80 | CD | 0C | 13 | EC | 5F | 97 | 44 | 17 | C4 | A7 | 7E | 3D | 64 | 5D | 19 | 73 |

| 90 | 60 | 81 | 4F | DC | 22 | 2A | 90 | 88 | 46 | EE | B8 | 14 | DE | 5E | 0B | DB |

| A0 | E0 | 32 | 3A | 0A | 49 | 06 | 24 | 5C | C2 | D3 | AC | 62 | 91 | 95 | E4 | 79 |

| B0 E7 C8 37 6D 8D D5 4E A9 6C 56 F4 EA 65 7A AE 08

| C0 | BA | 78 | 25 | 2E | 1C | A6 | B4 | C6 | E8 | DD | 74 | 1F | 4B | BD | 8B | 8A |

| D0 70 3E B5 66 48 03 F6 0E 61 35 57 B9 86 C1 1D 9E

| E0 | E1 | F8 | 98 | 11 | 69 | D9 | 8E | 94 | 9B | 1E | 87 | E9 | CE | 55 | 28 | DF |

| F0 | 8C | A1 | 89 | 0D | BF | E6 | 42 | 68 | 41 | 99 | 2D | 0F | B0 | 54 | BB | 16 |

Denne S-Boxen er et av stedene der abstrakt algebra kommer inn i bildet i Rijndael-krypteringen, nærmere bestemt **Galois-felt**.

Til å begynne med definerer du hvert mulige byteelement 00 til FF som en 8-bits vektor. Hver slik vektor er et element i **Galois-feltet GF(2^8)**, der det irreduserbare polynomet for modulo-operasjonen er $x^8 + x^4 + x^3 + x + 1$. Galois-feltet med disse spesifikasjonene kalles også **Rijndaels endelige felt**.

Deretter lager vi det som kalles **Nyberg S-Box** for hvert mulige element i feltet. I denne boksen mappes hver byte til sin **multiplikative inverse** (dvs. slik at produktet av dem er lik 1). Deretter tilordner vi disse verdiene fra Nybergs S-boks til Rijndaels S-boks ved hjelp av **affin transformasjon**.

Den tredje operasjonen på **S**-matrisen er **shift rows**-operasjonen. Den tar tilstanden til **S** og lister opp alle de seksten byte i en matrise. Fyllingen av matrisen starter øverst til venstre og går rundt ved å gå fra topp til bunn og deretter, hver gang en kolonne fylles, forskyve en kolonne til høyre og til toppen.

Når matrisen **S** er konstruert, forskyves de fire radene. Den første raden forblir den samme. Den andre raden flyttes én rad til venstre. Den tredje flytter to over til venstre. Den fjerde flytter tre over til venstre. Et eksempel på prosessen er vist i *Figur 4*. Den opprinnelige tilstanden til **S** er vist øverst, og den resulterende tilstanden etter skifting av rader er vist under.

*Figur 4: Operasjon med skiftrader*

| F1 | A0 | B1 | 23 | 23

|------|------|------|------|

| 59 EF 09 82

| 97 01 B0 CC

| D4 | 72 | 04 | 21 |

| F1 | A0 | B1 | 23 | 23

|------|------|------|------|

| EF | 09 | 82 | 59 | | | 59

| B0 CC 97 01

| 21 | D4 | 72 | 04 |

I det fjerde trinnet dukker **Galois-feltene** opp igjen. Til å begynne med multipliseres hver kolonne i **S**-matrisen med kolonnen i 4 x 4-matrisen i *Figur 5*. Men i stedet for å være en vanlig matrisemultiplikasjon, er det en vektormultiplikasjon **modulo et irreduserbart polynom**, $x^8 + x^4 + x^3 + x + 1$. De resulterende vektorkoeffisientene representerer de enkelte bitene i en byte.

*Figur 5: Blandingskolonnematrise*

| 02 | 03 | 01 | 01 |

|------|------|------|------|

| 01 | 02 | 03 | 01 |

| 01 | 01 | 02 | 03 |

| 03 | 01 | 01 | 02 |

Multiplikasjon av den første kolonnen i **S**-matrisen med 4 x 4-matrisen ovenfor gir resultatet i *Figur 6*.

*Figur 6: Multiplikasjon av den første kolonnen:*

$$
\begin{matrix}
02 \cdot F1 + 03 \cdot EF + 01 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 02 \cdot EF + 03 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 01 \cdot EF + 02 \cdot B0 + 03 \cdot 21 \\
03 \cdot F1 + 01 \cdot EF + 01 \cdot B0 + 02 \cdot 21
\end{matrix}
$$

Som et neste trinn må alle leddene i matrisen gjøres om til polynomer. F1 representerer for eksempel 1 byte og blir $x^7 + x^6 + x^5 + x^4 + 1$, og 03 representerer 1 byte og blir $x + 1$.

Alle multiplikasjonene utføres deretter **modulo** $x^8 + x^4 + x^3 + x + 1$. Dette resulterer i en addisjon av fire polynomer i hver av de fire cellene i kolonnen. Etter å ha utført disse addisjonene **modulo 2**, vil du ende opp med fire polynomer. Hvert av disse polynomene representerer en 8-bits streng, eller 1 byte, av **S**. Vi skal ikke utføre alle disse beregningene her på matrisen i *Figur 6*, da de er svært omfattende.

Når den første kolonnen er behandlet, behandles de tre andre kolonnene i **S**-matrisen på samme måte. Til slutt vil dette gi en matrise med seksten byte som kan transformeres til en matrise.

Som et siste trinn kombineres matrisen **S** med rundenøkkelen igjen i en **XOR**-operasjon. Dette produserer tilstanden $S_1$. Det vil si at


- $S_1 = S \oplus K_0$

### Runde 2 til og med runde 10

Runde 2 til 9 er bare en repetisjon av runde 1, *mutatis mutandis*. Den siste runden ligner veldig på de foregående rundene, bortsett fra at trinnet **bland kolonner** er eliminert. Det vil si at runde 10 utføres på følgende måte:


- $S_9 \oplus K_{10}$
- Bytesubstitusjon
- Skift rader
- $S_{10} = S \oplus K_{10}$$

Tilstanden $S_{10}$ er nå satt til $C_1$, de første 128 bitene av krypteringsteksten. Ved å fortsette gjennom de resterende 128-biters klartekstblokkene får man den fullstendige krypteringsteksten **C**.

### Operasjonene i Rijndael-krypteringen

Hva er tankegangen bak de ulike operasjonene i Rijndael-krypteringen?

Uten å gå inn på detaljene vurderes krypteringsopplegg ut fra i hvilken grad de skaper forvirring og spredning. Hvis krypteringsopplegget har en høy grad av **forvirring**, betyr det at krypteringsteksten ser drastisk annerledes ut enn klarteksten. Hvis krypteringsopplegget har en høy grad av **diffusjon**, betyr det at enhver liten endring i klarteksten gir en drastisk annerledes krypteringstekst.

Begrunnelsen for operasjonene bak Rijndael-krypteringen er at de gir både en høy grad av forvirring og spredning. Forvirringen skapes av byttesubstitusjonsoperasjonen, mens diffusjonen skapes av operasjonene shift rows og mix columns.

# Asymmetrisk kryptografi

<partId>868bd9dd-6e1c-5ea9-9ece-54affc13ba05</partId>

## Problemet med nøkkeldistribusjon og -håndtering

<chapterId>1bb651ba-689a-5a89-a7d3-0b9cc3b694f7</chapterId>

I likhet med symmetrisk kryptografi kan asymmetriske systemer brukes til å sikre både hemmelighold og autentisering. Disse systemene bruker imidlertid to nøkler i stedet for én: en privat og en offentlig nøkkel.

Vi begynner med å se nærmere på oppdagelsen av asymmetrisk kryptografi, og særlig på problemene som lå til grunn for utviklingen. Deretter diskuterer vi hvordan asymmetriske krypterings- og autentiseringsmetoder fungerer på et overordnet nivå. Deretter introduserer vi hashfunksjoner, som er nøkkelen til å forstå asymmetriske autentiseringsskjemaer, og som også er relevante i andre kryptografiske sammenhenger, for eksempel for de hashbaserte meldingsautentiseringskodene vi diskuterte i kapittel 4.

___

Anta at Bob ønsker å kjøpe en ny regnfrakk fra Jim's Sporting Goods, en nettbutikk med millioner av kunder i Nord-Amerika. Dette blir hans første kjøp hos dem, og han ønsker å bruke kredittkortet sitt. Bob må derfor først opprette en konto hos Jim's Sporting Goods, noe som krever at han sender inn personlige opplysninger som adresse og kredittkortinformasjon. Deretter kan han gå gjennom trinnene som trengs for å kjøpe regnjakken.

Bob og Jim's Sporting Goods vil sørge for at kommunikasjonen er sikker gjennom hele denne prosessen, siden Internett er et åpent kommunikasjonssystem. De vil for eksempel sørge for at ingen potensielle angripere kan få tak i Bobs kredittkort- og adresseopplysninger, og at ingen potensielle angripere kan gjenta kjøpene hans eller opprette falske kjøp på hans vegne.

Et avansert, autentisert krypteringsopplegg, som diskutert i forrige kapittel, kan absolutt gjøre kommunikasjonen mellom Bob og Jim's Sporting Goods sikker. Men det finnes helt klart praktiske hindringer for å implementere en slik ordning.

For å illustrere disse praktiske hindringene kan vi tenke oss at vi levde i en verden der det bare fantes verktøy for symmetrisk kryptografi. Hva kunne Jim's Sporting Goods og Bob da gjøre for å sikre sikker kommunikasjon?

Under slike omstendigheter vil de stå overfor betydelige kostnader for å kommunisere sikkert. Ettersom Internett er et åpent kommunikasjonssystem, kan de ikke bare utveksle et sett med nøkler over det. Derfor må Bob og en representant for Jim's Sporting Goods foreta en personlig nøkkelutveksling.

En mulighet er at Jim's Sporting Goods oppretter spesielle nøkkelutvekslingssteder, der Bob og andre nye kunder kan hente et sett med nøkler for sikker kommunikasjon. Dette vil selvsagt medføre betydelige organisatoriske kostnader og redusere effektiviteten når nye kunder skal gjøre sine innkjøp.

Alternativt kan Jim's Sporting Goods sende Bob et par nøkler med en pålitelig kurer. Dette er sannsynligvis mer effektivt enn å organisere nøkkelutvekslingssteder. Men det vil likevel medføre betydelige kostnader, spesielt hvis mange kunder bare gjør ett eller noen få kjøp.

En symmetrisk ordning for autentisert kryptering tvinger også Jim's Sporting Goods til å lagre separate sett med nøkler for alle kundene sine. Dette ville være en betydelig praktisk utfordring for tusenvis av kunder, for ikke å snakke om millioner.

For å forstå dette siste poenget kan vi anta at Jim's Sporting Goods gir hver kunde det samme nøkkelparet. Da kan hver kunde - eller hvem som helst som kan få tak i dette nøkkelparet - lese og til og med manipulere all kommunikasjon mellom Jim's Sporting Goods og kundene. Da kan du like gjerne la være å bruke kryptografi i kommunikasjonen din i det hele tatt.

Selv det å gjenta et sett med nøkler for bare noen kunder er en forferdelig sikkerhetspraksis. Enhver potensiell angriper kan forsøke å utnytte denne egenskapen ved systemet (husk at angripere antas å vite alt om et system bortsett fra nøklene, i samsvar med Kerckhoffs prinsipp)

Jim's Sporting Goods må altså lagre et nøkkelpar for hver kunde, uavhengig av hvordan disse nøkkelparene er fordelt. Dette byr helt klart på flere praktiske problemer.


- Jim's Sporting Goods ville måtte lagre millioner av nøkkelpar, ett sett for hver kunde.
- Disse nøklene må sikres godt, da de vil være et sikkert mål for hackere. Eventuelle brudd på sikkerheten ville kreve gjentatte kostbare nøkkelutvekslinger, enten på spesielle nøkkelutvekslingssteder eller med kurer.
- Enhver kunde hos Jim's Sporting Goods må oppbevare et par nøkler trygt hjemme. Tap og tyveri vil forekomme, noe som krever gjentatte nøkkelutvekslinger. Kundene vil også måtte gå gjennom denne prosessen for alle andre nettbutikker eller andre typer enheter de ønsker å kommunisere og handle med over Internett.

Disse to hovedutfordringene var helt frem til slutten av 1970-tallet helt grunnleggende. De var kjent som henholdsvis **nøkkelfordelingsproblemet** og **nøkkelhåndteringsproblemet**.

Disse problemene hadde selvfølgelig alltid eksistert, og de skapte ofte hodebry tidligere. Militære styrker måtte for eksempel hele tiden distribuere bøker med nøkler for sikker kommunikasjon til personell i felten, noe som medførte stor risiko og store kostnader. Men disse problemene ble verre etter hvert som verden i stadig større grad gikk over til digital kommunikasjon over lange avstander, særlig for ikke-statlige enheter.

Hvis disse problemene ikke hadde blitt løst på 1970-tallet, ville det sannsynligvis ikke ha vært mulig å handle effektivt og sikkert hos Jim's Sporting Goods. Faktisk ville det meste av vår moderne verden med praktisk og sikker e-post, nettbank og shopping sannsynligvis bare vært en fjern fantasi. Noe som ligner på Bitcoin kunne ikke ha eksistert i det hele tatt.

Så hva skjedde på 1970-tallet? Hvordan er det mulig at vi umiddelbart kan handle på nettet og surfe sikkert på World Wide Web? Hvordan er det mulig at vi umiddelbart kan sende Bitcoins over hele verden fra smarttelefonene våre?

## Nye retninger innen kryptografi

<chapterId>7a9dd9a3-496e-5f9d-93e0-b5028a7dd0f1</chapterId>

På 1970-tallet hadde problemene med nøkkeldistribusjon og nøkkelhåndtering fanget oppmerksomheten til en gruppe amerikanske akademiske kryptografer: Whitfield Diffie, Martin Hellman og Ralph Merkle. Til tross for stor skepsis fra de fleste av sine fagfeller, dristet de seg til å finne en løsning på problemet.

I hvert fall en av hovedmotivasjonene bak satsingen deres var at de forutså at åpen datakommunikasjon ville påvirke verden på en dyptgripende måte. Som Diffie og Helmann bemerker i 1976,

> Utviklingen av datastyrte kommunikasjonsnettverk lover enkel og billig kontakt mellom mennesker eller datamaskiner på hver sin side av jordkloden, og erstatter det meste av post og mange utflukter med telekommunikasjon. For mange bruksområder må disse kontaktene gjøres sikre både mot avlytting og mot tilførsel av uautoriserte meldinger. I dag ligger imidlertid løsningen av sikkerhetsproblemene langt etter andre områder av kommunikasjonsteknologien. *Moderne kryptografi er ikke i stand til å oppfylle kravene, i og med at bruken av den ville medføre så store ulemper for brukerne av systemet at mange av fordelene ved teleprosessering ville bli eliminert* [1]
Diffie, Hellman og Merkles utholdenhet ga resultater. Den første publikasjonen av resultatene deres var en artikkel av Diffie og Hellman i 1976 med tittelen "New Directions in Cryptography" Her presenterte de to originale måter å løse problemene med nøkkeldistribusjon og nøkkeladministrasjon på.

Den første løsningen de tilbød, var en ekstern *nøkkelutvekslingsprotokoll*, det vil si et sett med regler for utveksling av en eller flere symmetriske nøkler over en usikker kommunikasjonskanal. Denne protokollen er nå kjent som *Diffie-Helmann-nøkkelutveksling* eller *Diffie-Helmann-Merkle-nøkkelutveksling*. [2]

Ved Diffie-Helmann-nøkkelutveksling utveksler to parter først noe informasjon offentlig på en usikker kanal, for eksempel Internett. På grunnlag av denne informasjonen lager de deretter uavhengig av hverandre en symmetrisk nøkkel (eller et par symmetriske nøkler) for sikker kommunikasjon. Selv om begge parter lager nøklene sine uavhengig av hverandre, sørger informasjonen de har delt offentlig for at denne nøkkelprosessen gir samme resultat for dem begge.

Det er viktig å merke seg at selv om alle kan observere informasjonen som utveksles offentlig mellom partene via den usikre kanalen, er det bare de to partene som deltar i informasjonsutvekslingen, som kan lage symmetriske nøkler av den.

Dette høres selvfølgelig helt kontraintuitivt ut. Hvordan kan to parter utveksle informasjon offentlig slik at bare de kan lage symmetriske nøkler av den? Hvorfor skulle ikke andre som observerer informasjonsutvekslingen, kunne lage de samme nøklene?

Det bygger selvfølgelig på vakker matematikk. Diffie-Helmann-nøkkelutveksling fungerer via en enveisfunksjon med en falldør. La oss diskutere betydningen av disse to begrepene i tur og orden.

Anta at du får en funksjon $f(x)$ og resultatet $f(a) = y$, der $a$ er en bestemt verdi for $x$. Vi sier at $f(x)$ er en **enveisfunksjon** hvis det er enkelt å beregne verdien $y$ når $a$ og $f(x)$ er gitt, men det er beregningsmessig ugjennomførbart å beregne verdien $a$ når $y$ og $f(x)$ er gitt. Navnet **enveisfunksjon** kommer selvfølgelig av at en slik funksjon bare er praktisk å beregne i én retning.

Noen enveisfunksjoner har det som kalles en **felleåpning**. Selv om det er praktisk talt umulig å beregne $a$ gitt bare $y$ og $f(x)$, finnes det en viss informasjon $Z$ som gjør det mulig å beregne $a$ ut fra $y$. Denne informasjonen $Z$ er kjent som **trapdoor**. Enveisfunksjoner som har en falldør, kalles **trappdørfunksjoner**.

Vi skal ikke gå inn på detaljene i Diffie-Helmann-nøkkelutveksling her. Men i bunn og grunn skaper hver deltaker noe informasjon, hvorav en del deles offentlig og en del forblir hemmelig. Hver part bruker så sin hemmelige del av informasjonen og den offentlige informasjonen som er delt av den andre parten, til å lage en privat nøkkel. Og på mirakuløst vis ender begge parter opp med den samme private nøkkelen.

En part som bare observerer den offentlig delte informasjonen mellom de to partene i en Diffie Helmann-nøkkelutveksling, kan ikke gjenskape disse beregningene. For å kunne gjøre det må de ha den private informasjonen fra en av de to partene.

Selv om den grunnleggende versjonen av Diffie-Helmann-nøkkelutvekslingen som ble presentert i artikkelen fra 1976, ikke er særlig sikker, er sofistikerte versjoner av den grunnleggende protokollen fortsatt i bruk i dag. Det viktigste er at alle nøkkelutvekslingsprotokollene i den nyeste versjonen av transportlagssikkerhetsprotokollen (versjon 1.3) egentlig er en forbedret versjon av protokollen som ble presentert av Diffie og Hellman i 1976. Transport Layer Security Protocol er den dominerende protokollen for sikker utveksling av informasjon som er formatert i henhold til hypertext transfer protocol (http), som er standarden for utveksling av webinnhold.

Det er viktig å merke seg at Diffie-Helmann-nøkkelutveksling ikke er et asymmetrisk system. Strengt tatt tilhører det nok snarere symmetrisk nøkkelkryptografi. Men siden både Diffie-Helmann-nøkkelutveksling og asymmetrisk kryptografi baserer seg på enveis tallteoretiske funksjoner med falldører, blir de vanligvis diskutert sammen.

Den andre måten Diffie og Helmann foreslo å løse problemet med nøkkeldistribusjon og -administrasjon på i sin artikkel fra 1976, var selvsagt asymmetrisk kryptografi.

I motsetning til deres presentasjon av Diffie-Hellman-nøkkelutveksling, ga de bare de generelle konturene av hvordan asymmetriske kryptografiske systemer kunne konstrueres. De presenterte ingen enveisfunksjon som spesifikt kunne oppfylle betingelsene som trengs for å oppnå rimelig sikkerhet i slike systemer.

En praktisk implementering av et asymmetrisk system ble imidlertid funnet et år senere av tre forskjellige akademiske kryptografer og matematikere: Ronald Rivest, Adi Shamir og Leonard Adleman. [3] Kryptosystemet de introduserte, ble kjent som **RSA-kryptosystemet** (etter etternavnene deres).

Lukefunksjonene som brukes i asymmetrisk kryptografi (og Diffie Helmann-nøkkelutveksling), er alle knyttet til to **beregningsmessig vanskelige problemer**: primtallsfaktorisering og beregning av diskrete logaritmer.

**Primtallsfaktorisering** går, som navnet tilsier, ut på å bryte ned et heltall i dets primfaktorer. RSA-problemet er det desidert mest kjente eksemplet på et kryptosystem knyttet til primfaktorisering.

Det **diskrete logaritmeproblemet** er et problem som oppstår i sykliske grupper. Gitt en generator i en bestemt syklisk gruppe, må man beregne den unike eksponenten som trengs for å produsere et annet element i gruppen fra generatoren.

Diskrete logaritmebaserte systemer baserer seg på to hovedtyper sykliske grupper: multiplikative grupper av heltall og grupper som inkluderer punkter på elliptiske kurver. Den opprinnelige Diffie Helmann-nøkkelutvekslingen som ble presentert i "New Directions in Cryptography", fungerer med en syklisk multiplikativ gruppe av heltall. Bitcoins digitale signaturalgoritme og det nylig introduserte Schnorr-signaturskjemaet (2021) er begge basert på det diskrete logaritmeproblemet for en bestemt syklisk gruppe av elliptiske kurver.

I det følgende skal vi se nærmere på en oversikt over hemmelighold og autentisering i asymmetriske omgivelser. Før vi gjør det, må vi imidlertid komme med en kort historisk notis.

Det virker nå sannsynlig at en gruppe britiske kryptografer og matematikere som arbeidet for Government Communications Headquarters (GCHQ), uavhengig av hverandre hadde gjort de nevnte oppdagelsene noen år tidligere. Denne gruppen besto av James Ellis, Clifford Cocks og Malcolm Williamson.

Ifølge deres egne og GCHQs egne beretninger var det James Ellis som først utviklet konseptet med offentlig nøkkelkryptografi i 1969. Deretter skal Clifford Cocks ha oppdaget RSA-kryptografisystemet i 1973, og Malcolm Williamson konseptet Diffie Helmann-nøkkelutveksling i 1974. [4] Oppdagelsene deres ble imidlertid angivelig ikke avslørt før i 1997, på grunn av den hemmelige karakteren til arbeidet som ble utført ved GCHQ.

**Noter:**

[1] Whitfield Diffie og Martin Hellman, "New directions in cryptography", _IEEE Transactions on Information Theory_ IT-22 (1976), s. 644-654, på s. 644.

[2] Ralph Merkle diskuterer også en nøkkelutvekslingsprotokoll i "Secure communications over insecure channels", _Communications of the Association for Computing Machinery_, 21 (1978), 294-99. Merkle leverte denne artikkelen før artikkelen til Diffie og Hellman, men den ble publisert senere. Merkles løsning er ikke eksponentielt sikker, i motsetning til Diffie-Hellmans.

[3] Ron Rivest, Adi Shamir og Leonard Adleman, "A method for obtaining digital signatures and public-key cryptosystems", _Communications of the Association for Computing Machinery_, 21 (1978), s. 120-26.

[4] En god oversikt over disse oppdagelsene finnes i Simon Singh, _The Code Book_, Fourth Estate (London, 1999), kapittel 6.

## Asymmetrisk kryptering og autentisering

<chapterId>2f6f0f03-3c3d-5025-90f0-5211139bc0cc</chapterId>

En oversikt over **asymmetrisk kryptering** ved hjelp av Bob og Alice er vist i *Figur 1*.

Alice oppretter først et nøkkelpar bestående av en offentlig nøkkel ($K_P$) og en privat nøkkel ($K_S$), der "P" i $K_P$ står for "offentlig" og "S" i $K_S$ for "hemmelig". Denne offentlige nøkkelen distribuerer hun så fritt til andre. Vi kommer tilbake til detaljene i denne distribusjonsprosessen litt senere. Men for øyeblikket antar vi at hvem som helst, inkludert Bob, kan få tak i Alices offentlige nøkkel $K_P$ på en sikker måte.

På et senere tidspunkt ønsker Bob å skrive en melding $M$ til Alice. Siden den inneholder sensitiv informasjon, vil han at innholdet skal forbli hemmelig for alle andre enn Alice. Bob krypterer derfor først meldingen $M$ ved hjelp av $K_P$. Deretter sender han den resulterende krypteringsteksten $C$ til Alice, som dekrypterer $C$ med $K_S$ for å produsere den opprinnelige meldingen $M$.

*Figur 1: Asymmetrisk kryptering*

![Figure 1: Asymmetric encryption](assets/Figure6-1.webp "Figure 1: Asymmetric encryption")

Enhver motstander som lytter på Bob og Alices kommunikasjon, kan observere $C$. Hun kjenner også $K_P$ og krypteringsalgoritmen $E(\cdot)$. Det er imidlertid viktig å merke seg at denne informasjonen ikke gjør det mulig for angriperen å dekryptere chifferteksten $C$. Dekryptering krever spesifikt $K_S$, som angriperen ikke har.

Symmetriske krypteringssystemer må generelt være sikre mot en angriper som kan kryptere klartekstmeldinger på en gyldig måte (kjent som sikkerhet mot "chosen-ciphertext"-angrep). Det er imidlertid ikke utformet med det eksplisitte formålet å tillate at en angriper eller noen andre lager slike gyldige krypteringstekster.

Dette står i sterk kontrast til en asymmetrisk krypteringsmetode, der hele formålet er å tillate hvem som helst, inkludert angripere, å produsere gyldige krypteringstekster. Asymmetriske krypteringsmetoder kan derfor betegnes som **multiple access ciphers**.

For å forstå bedre hva som skjer, kan vi tenke oss at Bob i stedet for å sende en melding elektronisk, ønsker å sende et fysisk brev i hemmelighet. En måte å sikre hemmeligholdet på er at Alice sender en sikker hengelås til Bob, men beholder nøkkelen til å låse den opp. Etter å ha skrevet brevet kunne Bob legge brevet i en eske og lukke den med Alices hengelås. Deretter kan han sende den låste esken med meldingen til Alice, som har nøkkelen til å låse den opp.

Selv om Bob kan låse hengelåsen, kan verken han eller noen annen person som snapper opp esken, åpne hengelåsen hvis den faktisk er sikret. Det er bare Alice som kan låse den opp og se innholdet i Bobs brev, fordi hun har nøkkelen.

En asymmetrisk kryptering er grovt sett en digital versjon av denne prosessen. Hengelåsen er det samme som den offentlige nøkkelen, og hengelåsnøkkelen er det samme som den private nøkkelen. Fordi hengelåsen er digital, er det imidlertid mye enklere og ikke så kostbart for Alice å distribuere den til alle som måtte ønske å sende hemmelige meldinger til henne.

For autentisering i den asymmetriske settingen bruker vi **digitale signaturer**. Disse har dermed samme funksjon som meldingsautentiseringskoder i den symmetriske settingen. En oversikt over digitale signaturer finnes i *Figur 2*.

Bob oppretter først et nøkkelpar bestående av den offentlige nøkkelen ($K_P$) og den private nøkkelen ($K_S$), og distribuerer den offentlige nøkkelen sin. Når han ønsker å sende en autentisert melding til Alice, bruker han først meldingen $M$ og sin private nøkkel til å lage en **digital signatur** $D$. Bob sender deretter meldingen til Alice sammen med den digitale signaturen.

Alice setter inn meldingen, den offentlige nøkkelen og den digitale signaturen i en **verifiseringsalgoritme**. Denne algoritmen produserer enten **sant** for en gyldig signatur, eller **falsk** for en ugyldig signatur.

En digital signatur er, som navnet tydelig antyder, det digitale motstykket til en skriftlig signatur på brev, kontrakter og så videre. Faktisk er en digital signatur vanligvis mye sikrere. En skriftlig signatur kan med litt anstrengelse forfalskes, noe som gjøres enklere av at skriftlige signaturer ofte ikke blir nøye kontrollert. En sikker digital signatur er imidlertid, på samme måte som en sikker meldingsautentiseringskode, **eksistensielt uforfalskelig**: Det vil si at med en sikker digital signaturordning kan ingen lage en signatur for en melding som består verifiseringsprosedyren, med mindre de har den private nøkkelen.

*Figur 2: Asymmetrisk autentisering*

![Figure 2: Asymmetric authentication](assets/Figure6-2.webp "Figure 2: Asymmetric authentication")

I likhet med asymmetrisk kryptering ser vi en interessant kontrast mellom digitale signaturer og meldingsautentiseringskoder. I sistnevnte tilfelle kan verifiseringsalgoritmen bare brukes av én av partene som har innsyn i den sikre kommunikasjonen. Dette er fordi den krever en privat nøkkel. I den asymmetriske settingen kan imidlertid hvem som helst verifisere en digital signatur $S$ laget av Bob.

Alt dette gjør digitale signaturer til et ekstremt kraftfullt verktøy. Det danner for eksempel grunnlaget for å lage signaturer på kontrakter som kan verifiseres for juridiske formål. Hvis Bob hadde laget en signatur på en kontrakt i utvekslingen ovenfor, kan Alice vise meldingen $M$, kontrakten og signaturen $S$ til en domstol. Domstolen kan deretter verifisere signaturen ved hjelp av Bobs offentlige nøkkel. [5]

Et annet eksempel er digitale signaturer, som er et viktig aspekt ved sikker distribusjon av programvare og programvareoppdateringer. Denne typen offentlig verifiserbarhet ville aldri kunne skapes bare ved hjelp av meldingsautentiseringskoder.

Som et siste eksempel på kraften i digitale signaturer kan vi ta Bitcoin. En av de vanligste misforståelsene om Bitcoin, særlig i media, er at transaksjoner er krypterte. I stedet fungerer Bitcoin-transaksjoner med digitale signaturer for å garantere sikkerheten.

Bitcoins finnes i batcher som kalles ubrukte transaksjonsutganger (eller **UTXO-er**). Anta at du mottar tre betalinger på en bestemt Bitcoin-adresse for 2 bitcoins hver. Teknisk sett har du nå ikke 6 bitcoins på den adressen. I stedet har du tre batcher med 2 bitcoins som er låst av et kryptografisk problem knyttet til den adressen. For enhver betaling du foretar, kan du bruke én, to eller alle tre av disse batchene, avhengig av hvor mye du trenger for transaksjonen.

Beviset på eierskap over ubrukte transaksjonsutganger vises vanligvis via en eller flere digitale signaturer. Bitcoin fungerer nettopp fordi gyldige digitale signaturer på ubrukte transaksjonsutganger er beregningsmessig ugjennomførbare å lage, med mindre du er i besittelse av den hemmelige informasjonen som kreves for å lage dem.

Bitcoin-transaksjoner inkluderer for øyeblikket all informasjon som må verifiseres av deltakerne i nettverket, for eksempel opprinnelsen til de ubrukte transaksjonsutbetalingene som brukes i transaksjonen. Selv om det er mulig å skjule noe av denne informasjonen og likevel tillate verifisering (slik noen alternative kryptovalutaer som Monero gjør), skaper dette også spesielle sikkerhetsrisikoer.

Det oppstår av og til forvirring om digitale signaturer og skriftlige signaturer som er tatt opp digitalt. I sistnevnte tilfelle tar du et bilde av den skriftlige signaturen din og limer den inn i et elektronisk dokument, for eksempel en arbeidsavtale. Dette er imidlertid ikke en digital signatur i kryptografisk forstand. En digital signatur er bare et langt tall som bare kan produseres hvis man er i besittelse av en privat nøkkel.

På samme måte som for symmetriske nøkler kan du også bruke asymmetrisk kryptering og autentisering sammen. De samme prinsippene gjelder. Først og fremst bør du bruke forskjellige private og offentlige nøkkelpar til kryptering og til å lage digitale signaturer. I tillegg bør du først kryptere en melding og deretter autentisere den.

Det er viktig å merke seg at asymmetrisk kryptografi i mange applikasjoner ikke brukes gjennom hele kommunikasjonsprosessen. I stedet brukes den vanligvis bare til å *utveksle symmetriske nøkler* mellom partene som de faktisk skal kommunisere med.

Dette er for eksempel tilfelle når du kjøper varer på nettet. Når du kjenner selgerens offentlige nøkkel, kan hun sende deg digitalt signerte meldinger som du kan verifisere ektheten av. På grunnlag av dette kan du følge en av flere protokoller for utveksling av symmetriske nøkler for å kommunisere sikkert.

Hovedgrunnen til at denne tilnærmingen er så vanlig, er at asymmetrisk kryptografi er mye mindre effektiv enn symmetrisk kryptografi når det gjelder å oppnå et bestemt sikkerhetsnivå. Dette er en av grunnene til at vi fortsatt trenger symmetrisk nøkkelkryptografi ved siden av offentlig kryptografi. I tillegg er symmetrisk nøkkelkryptografi mye mer naturlig i spesielle bruksområder, for eksempel når en datamaskinbruker krypterer sine egne data.

Så hvordan løser egentlig digitale signaturer og kryptering med offentlig nøkkel problemene med nøkkeldistribusjon og nøkkelhåndtering?

Det finnes ikke bare ett svar her. Asymmetrisk kryptografi er et verktøy, og det finnes ikke én måte å bruke dette verktøyet på. Men la oss ta det tidligere eksemplet fra Jim's Sporting Goods for å vise hvordan problemene vanligvis ville blitt løst i dette eksempelet.

Jim's Sporting Goods vil sannsynligvis begynne med å henvende seg til en **sertifikatmyndighet**, en organisasjon som støtter distribusjon av offentlige nøkler. Sertifikatutstederen vil registrere noen opplysninger om Jim's Sporting Goods og gi dem en offentlig nøkkel. Deretter vil den sende Jim's Sporting Goods et sertifikat, et såkalt **TLS/SSL-sertifikat**, med Jim's Sporting Goods' offentlige nøkkel digitalt signert ved hjelp av sertifikatmyndighetens egen offentlige nøkkel. På denne måten bekrefter sertifikatutstederen at en bestemt offentlig nøkkel faktisk tilhører Jim's Sporting Goods.

Nøkkelen til å forstå denne prosessen med TLS/SSL-sertifikater er at selv om du vanligvis ikke har Jim's Sporting Goods' offentlige nøkkel lagret noe sted på datamaskinen din, er de offentlige nøklene til anerkjente sertifikatmyndigheter faktisk lagret i nettleseren eller i operativsystemet ditt. Disse lagres i det som kalles **rotsertifikater**.

Når Jim's Sporting Goods gir deg TLS/SSL-sertifikatet sitt, kan du derfor verifisere sertifikatmyndighetens digitale signatur via et rotsertifikat i nettleseren eller operativsystemet ditt. Hvis signaturen er gyldig, kan du være relativt sikker på at den offentlige nøkkelen på sertifikatet faktisk tilhører Jim's Sporting Goods. På dette grunnlaget er det enkelt å sette opp en protokoll for sikker kommunikasjon med Jim's Sporting Goods.

Nøkkeldistribusjonen har nå blitt mye enklere for Jim's Sporting Goods. Det er ikke vanskelig å se at nøkkelhåndteringen også har blitt mye enklere. I stedet for å måtte lagre tusenvis av nøkler, trenger Jim's Sporting Goods bare å lagre en privat nøkkel som gjør det mulig å lage signaturer for den offentlige nøkkelen på SSL-sertifikatet. Hver gang en kunde kommer til Jim's Sporting Goods' nettsted, kan de opprette en sikker kommunikasjonsøkt fra denne offentlige nøkkelen. Kundene trenger heller ikke å lagre noen informasjon (annet enn de offentlige nøklene til anerkjente sertifikatmyndigheter i operativsystemet og nettleseren).

**Noter:**

[5] Alle ordninger som forsøker å oppnå uavviselighet, det andre temaet vi diskuterte i kapittel 1, vil i utgangspunktet måtte involvere digitale signaturer.

## Hash-funksjoner

<chapterId>ea8327ab-b0e3-5635-941c-4b51f396a648</chapterId>

Hash-funksjoner er allestedsnærværende i kryptografi. De er verken symmetriske eller asymmetriske, men faller inn i en egen kryptografisk kategori.

Vi kom allerede innom hashfunksjoner i kapittel 4 i forbindelse med opprettelsen av hashbaserte autentiseringsmeldinger. De er også viktige i forbindelse med digitale signaturer, men av en litt annen grunn: Digitale signaturer lages nemlig vanligvis over hashverdien til en (kryptert) melding, i stedet for den faktiske (krypterte) meldingen. I dette avsnittet vil jeg gi en grundigere innføring i hashfunksjoner.

La oss begynne med å definere en hash-funksjon. En **hash-funksjon** er en hvilken som helst effektivt beregnbar funksjon som tar inndata av vilkårlig størrelse og gir utdata med fast lengde.

En **kryptografisk hashfunksjon** er bare en hashfunksjon som er nyttig for anvendelser innen kryptografi. Resultatet av en kryptografisk hash-funksjon kalles vanligvis **hash**, **hash-verdi** eller **message digest**.

I kryptografisammenheng refererer en "hashfunksjon" vanligvis til en kryptografisk hashfunksjon. Jeg vil følge denne praksisen fra nå av.

Et eksempel på en populær hashfunksjon er **SHA-256** (secure hash algorithm 256). Uansett størrelsen på inndataene (f.eks. 15 bit, 100 bit eller 10 000 bit), vil denne funksjonen gi en 256-biters hashverdi. Nedenfor kan du se noen eksempler på utdata fra SHA-256-funksjonen.

"Hello": `185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969`

"52398": `a3b14d2bf378c1bd47e7f8eaec63b445150a3d7a80465af16dd9fd319454ba90`

"Kryptografi er gøy": `3cee2a5c7d2cc1d62db4893564c34ae553cc88623992d994e114e344359b146c`

Alle utdataene er nøyaktig 256 bits skrevet ut i heksadesimalt format (hvert heksesiffer kan representeres av fire binære sifre). Så selv om du hadde satt inn Tolkiens bok *Ringenes Herre* i SHA-256-funksjonen, ville utdataene fortsatt vært 256 bits.

Hashfunksjoner som SHA-256 brukes til ulike formål innen kryptografi. Hvilke egenskaper som kreves av en hash-funksjon, avhenger av konteksten for den aktuelle anvendelsen. Det er to hovedegenskaper som vanligvis ønskes av hashfunksjoner i kryptografi: [6]

1.	Motstand mot kollisjon

2.	Gjemmer seg

En hashfunksjon $H$ sies å være **kollisjonsresistent** hvis det er umulig å finne to verdier, $x$ og $y$, slik at $x \neq y$, men likevel $H(x)= H(y)$.

Kollisjonsresistente hash-funksjoner er viktige, for eksempel ved verifisering av programvare. Anta at du ønsker å laste ned Windows-versjonen av Bitcoin Core 0.21.0 (en serverapplikasjon for behandling av Bitcoin-nettverkstrafikk). De viktigste stegene du må ta for å verifisere programvarens legitimitet, er som følger:

1.	Du må først laste ned og importere de offentlige nøklene til en eller flere bidragsytere til Bitcoin Core til programvare som kan verifisere digitale signaturer (f.eks. Kleopetra). Du finner disse offentlige nøklene [her] (https://github.com/bitcoin/bitcoin/blob/master/contrib/builder-keys/keys.txt). Det anbefales at du verifiserer Bitcoin Core-programvaren med de offentlige nøklene fra flere bidragsytere.

2.	Deretter må du verifisere de offentlige nøklene du har importert. Du bør i det minste kontrollere at de offentlige nøklene du har funnet, er de samme som er publisert på andre steder. Du kan for eksempel sjekke de personlige nettsidene, Twitter-sidene eller Github-sidene til personene du har importert de offentlige nøklene til. Vanligvis gjøres denne sammenligningen av offentlige nøkler ved å sammenligne en kort hash av den offentlige nøkkelen, et såkalt fingeravtrykk.

3.	Deretter må du laste ned den kjørbare filen for Bitcoin Core fra deres [nettsted] (www.bitcoincore.org). Det vil være pakker tilgjengelig for Linux-, Windows- og MAC-operativsystemer.

4.	Deretter må du finne to utgivelsesfiler. Den første inneholder den offisielle SHA-256-hashingen for den kjørbare filen du lastet ned, sammen med hashene for alle de andre pakkene som ble utgitt. En annen utgivelsesfil vil inneholde signaturene fra ulike bidragsytere over utgivelsesfilen med pakkehashene. Begge disse utgivelsesfilene skal finnes på Bitcoin Core-nettstedet.

5.	 Deretter må du beregne SHA-256-hashingen av den kjørbare filen du lastet ned fra Bitcoin Core-nettstedet på din egen datamaskin. Deretter sammenligner du dette resultatet med den offisielle pakkehashingen for den kjørbare filen. De bør være de samme.

6.	Til slutt må du verifisere at en eller flere av de digitale signaturene over utgivelsesfilen med de offisielle pakkehashene faktisk tilsvarer en eller flere offentlige nøkler du importerte (utgivelser av Bitcoin Core er ikke alltid signert av alle). Du kan gjøre dette med et program som Kleopetra.

Denne prosessen med programvareverifisering har to hovedfordeler. For det første sikrer den at det ikke var noen feil i overføringen under nedlastingen fra Bitcoin Core sitt nettsted. For det andre sikrer den at ingen angripere kan ha fått deg til å laste ned modifisert, ondsinnet kode, enten ved å hacke Bitcoin Core-nettstedet eller ved å avlytte trafikken.

Hvordan beskytter programvareverifiseringsprosessen ovenfor mot disse problemene?

Hvis du har verifisert de offentlige nøklene du har importert, kan du være ganske sikker på at disse nøklene faktisk er deres og ikke har blitt kompromittert. Gitt at digitale signaturer er eksistensielt uforfalskelige, vet du at bare disse bidragsyterne kan ha laget en digital signatur over de offisielle pakkehashene i utgivelsesfilen.

Anta at signaturene på utgivelsesfilen du lastet ned, stemmer. Du kan nå sammenligne hashverdien du har beregnet lokalt for den nedlastede Windows-kjørbare filen, med hashverdien i den korrekt signerte utgivelsesfilen. Som du vet er SHA-256-hashfunksjonen kollideringsmotstandsdyktig, og en match betyr at den kjørbare filen din er nøyaktig den samme som den offisielle kjørbare filen.

La oss nå se nærmere på den andre vanlige egenskapen ved hashfunksjoner: **skjuling**. En hash-funksjon $H$ sies å ha egenskapen skjult hvis det er umulig å finne $x$ for en hvilken som helst tilfeldig valgt $x$ fra et svært stort område når man bare får $H(x)$.

Nedenfor kan du se SHA-256-utdataene fra en melding jeg skrev. For å sikre tilstrekkelig tilfeldighet inkluderte meldingen en tilfeldig generert tegnstreng på slutten. Siden SHA-256 har en skjulende egenskap, vil ingen kunne dechiffrere denne meldingen.


- `b194221b37fa4cd1cfce15aaef90351d70de17a98ee6225088b523b586c32ded`

Men jeg vil ikke la deg vente i uvisshet til SHA-256 blir svakere. Den opprinnelige meldingen jeg skrev var som følger:


- "Dette er et veldig tilfeldig budskap, eller i hvert fall litt tilfeldig. Denne første delen er ikke det, men jeg vil avslutte med noen relativt tilfeldige tegn for å sikre en svært uforutsigbar melding. XLWz4dVG3BxUWm7zQ9qS".

En vanlig måte å bruke hashfunksjoner med skjulegenskaper på er i passordadministrasjon (kollisjonsresistens er også viktig i denne sammenhengen). Alle anstendige kontobaserte tjenester på nettet, som Facebook eller Google, lagrer ikke passordene dine direkte for å administrere tilgangen til kontoen din. I stedet lagrer de bare en hash av passordet. Hver gang du skriver inn passordet ditt i en nettleser, beregnes det først en hash. Kun denne hashen sendes til tjenesteleverandørens server og sammenlignes med hashen som er lagret i back-end-databasen. Skjulegenskapen kan bidra til å sikre at angripere ikke kan gjenopprette det fra hash-verdien.

Passordhåndtering via hasher fungerer selvsagt bare hvis brukerne faktisk velger vanskelige passord. Skjulegenskapen forutsetter at x velges tilfeldig fra et veldig stort utvalg. Å velge passord som "1234", "mypassword" eller bursdagsdatoen din gir ingen reell sikkerhet. Det finnes lange lister med vanlige passord og hash-verdier av disse, som angripere kan utnytte hvis de noen gang får tak i hash-verdien av passordet ditt. Denne typen angrep er kjent som **ordbokangrep**. Hvis angriperne kjenner noen av personopplysningene dine, kan de også forsøke å gjette seg frem til dem. Derfor trenger du alltid lange, sikre passord (helst lange, tilfeldige strenger fra en passordbehandler).

Noen ganger kan en applikasjon ha behov for en hashfunksjon som både er kollisjonssikker og skjult. Men absolutt ikke alltid. I programvareverifiseringsprosessen vi diskuterte, for eksempel, kreves det bare at hashfunksjonen har kollisjonsresistens, og skjuling er ikke viktig.

Kollisjonsresistens og skjuling er de viktigste egenskapene som etterspørres hos hashfunksjoner i kryptografi, men i visse bruksområder kan det også være ønskelig med andre typer egenskaper.

**Noter:**

[6] Terminologien "skjuler" er ikke vanlig språkbruk, men er hentet fra Arvind Narayanan, Joseph Bonneau, Edward Felten, Andrew Miller og Steven Goldfeder, *Bitcoin and Cryptocurrency Technologies*, Princeton University Press (Princeton, 2016), kapittel 1.

# RSA-kryptosystemet

<partId>864dca42-2a8d-530f-bb94-2e1f68b3f411</partId>

## Faktoriseringsproblemet

<chapterId>a31a66e4-52ea-539c-9953-4769ad565d7e</chapterId>

Mens symmetrisk kryptografi vanligvis er ganske intuitivt for de fleste, er dette vanligvis ikke tilfellet med asymmetrisk kryptografi. Selv om du sannsynligvis er komfortabel med den generelle beskrivelsen som er gitt i de foregående avsnittene, lurer du sikkert på hva enveisfunksjoner egentlig er, og hvordan de brukes til å konstruere asymmetriske systemer.

I dette kapittelet vil jeg fjerne noe av mystikken rundt asymmetrisk kryptografi ved å se nærmere på et spesifikt eksempel, nemlig RSA-kryptosystemet. I den første delen vil jeg introdusere faktoriseringsproblemet som RSA-problemet er basert på. Deretter vil jeg gå gjennom en rekke sentrale resultater fra tallteori. I den siste delen setter vi denne informasjonen sammen for å forklare RSA-problemet, og hvordan dette kan brukes til å lage asymmetriske kryptografiske systemer.

Det er ingen enkel oppgave å gi denne dybden til diskusjonen vår. Det krever at vi introduserer en del tallteoretiske teoremer og setninger. Men ikke la deg avskrekke av matematikken. Å arbeide deg gjennom denne diskusjonen vil gi deg en betydelig bedre forståelse av hva som ligger til grunn for asymmetrisk kryptografi, og det er en verdifull investering.

La oss nå først se på faktoriseringsproblemet.

___

Når du multipliserer to tall, for eksempel $a$ og $b$, refererer vi til tallene $a$ og $b$ som **faktorer**, og resultatet som **produkt**. Forsøk på å skrive et tall $N$ om til multiplikasjon av to eller flere faktorer kalles **faktorisering** eller **faktorering**. [1] Du kan kalle ethvert problem som krever dette, for et **faktoriseringsproblem**.

For rundt 2500 år siden oppdaget den greske matematikeren Euklid av Alexandria et sentralt teorem om faktorisering av hele tall. Det kalles ofte **det unike faktoriseringsteoremet** og sier følgende:

**Setning 1**. Ethvert heltall $N$ som er større enn 1 er enten et primtall, eller kan uttrykkes som et produkt av primtallsfaktorer.

Alt den siste delen av dette utsagnet betyr er at du kan ta et hvilket som helst ikke-primtal $N$ større enn 1, og skrive det ut som en multiplikasjon av primtall. Nedenfor er det flere eksempler på ikke-prime heltall skrevet som produktet av primtallsfaktorer.


- $18 = 2 \cdot 3 \cdot 3 = 2 \cdot 3^2$$
- $84 = 2 \cdot 2 \cdot 3 \cdot 7 = 2^2 \cdot 3 \cdot 7$$
- $144 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 3 \cdot 3 = 2^4 \cdot 3^2$$

For alle de tre heltallene ovenfor er det relativt enkelt å beregne primtallsfaktorene, selv om du bare har $N$. Du starter med det minste primtallet, nemlig 2, og ser hvor mange ganger heltallet $N$ er delelig med det. Deretter går du videre til å teste delbarheten av $N$ med 3, 5, 7 og så videre. Du fortsetter denne prosessen helt til heltallet $N$ er skrevet som et produkt av bare primtall.

Ta for eksempel heltallet 84. Nedenfor ser du prosessen for å finne primtallsfaktorene. For hvert trinn tar vi ut den minste gjenværende primtallsfaktoren (til venstre) og bestemmer restleddet som skal faktoriseres. Vi fortsetter til restleddet også er et primtall. Ved hvert trinn vises den aktuelle faktoriseringen av 84 helt til høyre.


- Primfaktor = 2: restleddet = 42 ($84 = 2 \cdot 42$)
- Primfaktor = 2: restleddet = 21 ($84 = 2 \cdot 2 \cdot 21$)
- Primfaktor = 3: restledd = 7 ($84 = 2 \cdot 2 \cdot 3 \cdot 7$)
- Ettersom 7 er et primtall, blir resultatet $2 \cdot 2 \cdot 3 \cdot 7$, eller $2^2 \cdot 3 \cdot 7$.

Anta nå at $N$ er veldig stort. Hvor vanskelig vil det være å redusere $N$ til sine primfaktorer?

Det avhenger virkelig av $N$. Anta for eksempel at $N$ er 50 450 400. Selv om dette tallet ser skremmende ut, er beregningene ikke så kompliserte og kan enkelt gjøres for hånd. Som ovenfor begynner du bare med 2 og jobber deg videre. Nedenfor kan du se resultatet av denne prosessen på samme måte som ovenfor.


- 2: 25 225 200 (50 450 400 $ = 2 \cdot 25 225 200 $)
- 2: 12 612 600 (50 450 400 $ = 2^2 \cdot 12 612 600 $)
- 2: 6 306 300 $ (50 450 400 $ = 2^3 \cdot 6 306 300 $)
- 2: 3 153 150 (50 450 400 $ = 2^4 \cdot 3 153 150 $)
- 2: 1 576 575 (50 450 400 $ = 2^5 \cdot 1 576 575 $)
- 3: 525 525 (50 450 400 $ = 2^5 \cdot 3 \cdot 525 525 $)
- 3: 175 175 (50 450 400 $ = 2^5 \cdot 3^2 \cdot 175 175$)
- 5: 35 035 (50 450 400 $ = 2^5 \cdot 3^2 \cdot 5 \cdot 35 035$)
- 5: 7 007 (50 450 400 $ = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7 007$)
- 7: 1 001 (50 450 400 $ = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7 \cdot 1 001$)
- 7: 143 ($50 450 400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 143$)
- 11: 13 (50 450 400 $ = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 11 \cdot 13$)
- Ettersom 13 er et primtall, blir resultatet $2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 11 \cdot 13$.

Det tar litt tid å regne ut dette problemet for hånd. En datamaskin kan selvsagt gjøre alt dette på en brøkdel av et sekund. Faktisk kan en datamaskin ofte til og med faktorisere ekstremt store heltall på en brøkdel av et sekund.

Det finnes imidlertid visse unntak. Anta at vi først velger to svært store primtall tilfeldig. Det er vanlig å kalle disse $p$ og $q$, og jeg vil benytte meg av den konvensjonen her.

La oss si at $p$ og $q$ begge er 1024-biters primtall, og at de faktisk krever minst 1024 bits for å kunne representeres (så den første biten må være 1). Så for eksempel 37 kan ikke være et av primtallene. Du kan absolutt representere 37 med 1024 bits. Men det er klart at *du ikke trenger* så mange bits for å representere det. Du kan representere 37 med en hvilken som helst streng som har 6 bits eller mer. (Med 6 bits kan 37 representeres som $100101$).

Det er viktig å forstå hvor store $p$ og $q$ er hvis de velges under betingelsene ovenfor. Som et eksempel har jeg valgt et tilfeldig primtall som trenger minst 1024 bits for representasjon nedenfor.


- 14,752,173,874,503,595,484,930,006,383,670,759,559,764,562,721,397,166,747,289,220,945,457,932,666,751,048,198,854,920,097,085,690,793,755,254,946,188,163,753,506,778,089,706,699,671,722,089,715,624,760,049,594,106,189,662,669,156,149,028,900,805,928,183,585,427,782,974,951,355,515,394,807,209,836,870,484,558,332,897,443,152,653,214,483,870,992,618,171,825,921,582,253,023,974,514,209,142,520,026,807,636,589

Anta nå at vi etter å ha valgt primtallene $p$ og $q$ tilfeldig, multipliserer dem for å få et heltall $N$. Dette tallet er derfor et 2048-biters tall som krever minst 2048 bits for å bli representert. Det er mye, mye større enn både $p$ og $q$.

Anta at du bare gir en datamaskin $N$, og ber den om å finne de to 1024 bit primfaktorene til $N$. Sannsynligheten for at datamaskinen finner $p$ og $q$ er ekstremt liten. Du kan si at det er umulig for alle praktiske formål. Dette gjelder selv om du skulle bruke en superdatamaskin eller til og med et nettverk av superdatamaskiner.

Til å begynne med kan vi anta at datamaskinen forsøker å løse problemet ved å sykle gjennom 1024 bit-tall, og i hvert tilfelle teste om de er primtall og om de er faktorer av $N$. Settet med primtall som skal testes, er da omtrent $1,265 \cdot 10^{305}$. [2]

Selv om du tar alle datamaskinene på planeten og lar dem forsøke å finne og teste 1024-biters primtall på denne måten, vil en sjanse på 1 til en milliard for å finne en primtallsfaktor av $N$ kreve en beregningsperiode som er mye lengre enn universets alder.

I praksis kan en datamaskin gjøre det bedre enn den grove prosedyren som nettopp er beskrevet. Det finnes flere algoritmer som datamaskinen kan bruke for å komme fram til en faktorisering raskere. Poenget er imidlertid at selv med disse mer effektive algoritmene er datamaskinens oppgave fortsatt ugjennomførbar. [3]

Det er viktig å merke seg at faktoriseringens vanskelighetsgrad under de betingelsene som nettopp er beskrevet, hviler på antakelsen om at det ikke finnes regneeffektive algoritmer for beregning av primtallsfaktorer. Vi kan ikke bevise at det ikke finnes en effektiv algoritme. Likevel er denne antakelsen svært plausibel: Til tross for omfattende anstrengelser gjennom hundrevis av år har vi ennå ikke funnet en slik beregningseffektiv algoritme.

Derfor kan faktoriseringsproblemet, under visse omstendigheter, antas å være et vanskelig problem. Når $p$ og $q$ er veldig store primtall, er produktet $N$ ikke vanskelig å beregne, men faktorisering bare gitt $N$ er praktisk talt umulig.

**Noter:**

[1] Faktorisering kan også være viktig for å arbeide med andre typer matematiske objekter enn tall. For eksempel kan det være nyttig å faktorisere polynomuttrykk som $x^2 - 2x + 1$. I vår diskusjon vil vi kun fokusere på faktorisering av tall, nærmere bestemt heltall.

[2] Ifølge **primtallsteoremet** er antallet primtall som er mindre enn eller lik $N$, omtrent $N/\ln(N)$. Dette betyr at du kan beregne antallet primtall med lengden 1024 bits ved å:

$$ \frac{2^{1024}}{\ln(2^{1024})} - \frac{2^{1023}}{\ln(2^{1023})} $$

...som tilsvarer omtrent 1,265 ganger 10^{305}$.

[Det samme gjelder for diskrete logaritmeproblemer. Derfor fungerer asymmetriske konstruksjoner med mye større nøkler enn symmetriske kryptografiske konstruksjoner.

## Tallteoretiske resultater

<chapterId>23cd2186-8d97-5709-a4a7-b984f1eb9999</chapterId>

Dessverre kan ikke faktoriseringsproblemet brukes direkte til asymmetriske kryptografiske systemer. Vi kan imidlertid bruke et mer komplekst, men beslektet problem til dette formålet: RSA-problemet.

For å forstå RSA-problemet må vi forstå en rekke teoremer og setninger fra tallteorien. Disse presenteres i dette avsnittet i tre underavsnitt: (1) rekkefølgen til N, (2) invertibilitet modulo N og (3) Eulers teorem.

Noe av stoffet i de tre underkapitlene er allerede introdusert i *Kapittel 3*. Men for enkelhets skyld gjengir jeg det her.

### Rekkefølgen av N

Et heltall $a$ er **koprim** eller et **relativt primtall** med et heltall $N$ hvis den største felles divisoren mellom dem er 1. Selv om 1 per konvensjon ikke er et primtall, er det et koprim til alle heltall (i likhet med $-1$).

Se for eksempel på tilfellet der $a = 18$ og $N = 37$. Disse er helt klart koprim. Det største heltallet som deler seg i både 18 og 37 er 1. Se derimot på tilfellet der $a = 42$ og $N = 16$. Disse er helt klart ikke koprim. Begge tallene er delelige med 2, som er større enn 1.

Vi kan nå definere ordenen til $N$ på følgende måte. Anta at $N$ er et heltall større enn 1. **Ordningen til N** er da antallet av alle koprim med $N$ som er slik at for hvert koprim $a$ gjelder følgende betingelse: $1 \leq a < N$.

Hvis for eksempel $N = 12$, er 1, 5, 7 og 11 de eneste koprimene som oppfyller kravet ovenfor. Derfor er ordenen til 12 lik 4.

Anta at $N$ er et primtall. Da er ethvert heltall som er mindre enn $N$, men større eller lik 1, koprim med det. Dette inkluderer alle elementene i følgende mengde: $\{1,2,3,....,N - 1\}$. Når $N$ er primtall, er derfor rekkefølgen til $N$ $N - 1$. Dette fremgår av proposisjon 1, hvor $\phi(N)$ angir ordenen til $N$.

**Proposisjon 1**. $\phi(N) = N - 1$ når $N$ er primtall

Anta at $N$ ikke er et primtall. Da kan du beregne rekkefølgen ved hjelp av **Eulers Phi-funksjon**. Mens det er relativt enkelt å beregne ordenen til et lite heltall, blir Eulers Phi-funksjon spesielt viktig for større heltall. Nedenfor følger en setning om Eulers Phi-funksjon.

**Setning 2**. La $N$ være lik $p_1^{e_1} \cdot p_2^{e_2} \cdot \ldots \cdot p_i^{e_i} \cdot \ldots \cdot p_n^{e_n}$, hvor mengden $\{p_i\}$ består av alle de distinkte primtallsfaktorene til $N$ og hver $e_i$ angir hvor mange ganger primtallsfaktoren $p_i$ forekommer for $N$. I så fall

$$\phi(N) = p_1^{e_1 - 1} \cdot (p_1 - 1) \cdot p_2^{e_2 - 1} \cdot (p_1 - 1) \cdot p_2^{e_2 - 1} \cdot (p_2 - 1) \cdot (p_2 - 1) \cdot \ldots \cdot p_n^{e_n - 1} \cdot (p_n - 1) \cdot (p_n - 1)$$$

**Setning 2** viser at når du har brutt ned et ikke-primtal $N$ i dets forskjellige primfaktorer, er det enkelt å beregne rekkefølgen til $N$.

Anta for eksempel at $N = 270$. Dette er åpenbart ikke et primtall. Ved å dele opp $N$ i sine primtallsfaktorer får vi uttrykket: $2 \cdot 3^3 \cdot 5$. I henhold til Eulers Phi-funksjon er rekkefølgen til $N$ da som følger:

$$\phi(N) = 2^{1 - 1} \cdot (2 - 1) + 3^{3 - 1} \cdot (3 - 1) + 5^{1 - 1} \cdot (5 - 1) = 1 \cdot 1 + 9 \cdot 2 + 1 \cdot 4 = 1 + 18 + 4 = 23$$$

Anta videre at $N$ er et produkt av to primtal, $p$ og $q$. **Setning 2** ovenfor sier da at rekkefølgen til $N$ er som følger:

$$p^{1 - 1} \cdot (p - 1) \cdot q^{1 - 1} \cdot (q - 1) = (p - 1) \cdot (q - 1)$$$

Dette er et nøkkelresultat for RSA-problemet spesielt, og er beskrevet i **Proposisjon 2** nedenfor.

**Proposisjon 2**. Hvis $N$ er produktet av to primtal, $p$ og $q$, er rekkefølgen til $N$ produktet $(p - 1) \cdot (q - 1)$.

For å illustrere dette kan vi anta at $N = 119$. Dette heltallet kan deles opp i to primtall, nemlig 7 og 17. Eulers Phi-funksjon antyder derfor at rekkefølgen til 119 er som følger:

$$\phi(119) = (7 - 1) \cdot (17 - 1) = 6 \cdot 16 = 96$$$

Med andre ord har heltallet 119 96 koprim i området fra 1 til 119. Faktisk inkluderer dette settet alle heltall fra 1 til 119 som ikke er multipler av verken 7 eller 17.

Fra nå av betegner vi mengden av koprim som bestemmer rekkefølgen av $N$ som $C_N$. For vårt eksempel der $N = 119$, er mengden $C_{119}$ altfor stor til å liste opp i sin helhet. Men noen av elementene er som følger:

$$C_{119} = \{1, 2, \prikkene 6, 8 \prikkene 13, 15, 16, 18, \prikkene 33, 35 \prikkene 96\}$$$

### Invertibilitet modulo N

Vi kan si at et heltall $a$ er **invertibelt modulo N**, hvis det finnes minst ett heltall $b$ slik at $a \cdot b \mod N = 1 \mod N$$. Ethvert slikt heltall $b$ kalles en **invers** (eller **multiplikativ invers**) av $a$ gitt reduksjon ved modulo $N$.

Anta for eksempel at $a = 5$ og $N = 11$. Det finnes mange heltall som du kan multiplisere 5 med, slik at $5 \cdot b \mod 11 = 1 \mod 11$. Tenk for eksempel på heltallene 20 og 31. Det er lett å se at begge disse heltallene er invertere av 5 for reduksjon modulo 11.


- $5 \cdot 20 \mod 11 = 100 \mod 11 = 1 \mod 11$
- $5 \cdot 31 \mod 11 = 155 \mod 11 = 1 \mod 11$

Selv om 5 har mange inverser med reduksjon modulo 11, kan du vise at det bare finnes én positiv invers av 5 som er mindre enn 11. Dette er faktisk ikke unikt for vårt spesielle eksempel, men et generelt resultat.

**Proposisjon 3**. Hvis heltallet $a$ er inversibelt modulo $N$, må det være slik at nøyaktig én positiv invers av $a$ er mindre enn $N$. (Denne unike inversen av $a$ må altså komme fra mengden $\{1, \dots, N - 1\}$).

La oss betegne den unike inversen til $a$ fra **Proposisjon 3** som $a^{-1}$. For tilfellet når $a = 5$ og $N = 11$, kan du se at $a^{-1} = 9$, gitt at $5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$.

Legg merke til at du også kan få verdien 9 for $a^{-1}$ i eksempelet vårt ved å redusere en hvilken som helst annen invers av $a$ med modulo 11. For eksempel $20 \mod 11 = 31 \mod 11 = 9 \mod 11$. Så når et heltall $a > N$ er inversibelt modulo $N$, må $a \mod N$ også være inversibelt modulo $N$.

Det er ikke nødvendigvis slik at det finnes en invers av $a$ reduksjon modulo $N$. Anta for eksempel at $a = 2$ og $N = 8$. Det finnes ingen $b$, eller noen $a^{-1}$ spesielt, slik at $2 \cdot b \mod 8 = 1 \mod 8$. Dette er fordi enhver verdi av $b$ alltid vil gi et multiplum av 2, slik at ingen divisjon med 8 noen gang kan gi en rest som er lik 1.

Hvordan vet vi egentlig om et heltall $a$ har en invers for et gitt $N$? Som du kanskje la merke til i eksemplet ovenfor, er den største felles divisoren mellom 2 og 8 høyere enn 1, nemlig 2. Og dette er faktisk illustrerende for følgende generelle resultat:

**Proposisjon 4**. Det finnes en invers til et heltall $a$ gitt reduksjon modulo $N$, og spesielt en unik positiv invers som er mindre enn $N$, hvis og bare hvis den største felles divisoren mellom $a$ og $N$ er 1 (det vil si hvis de er koprim).

For tilfellet der $a = 5$ og $N = 11$, konkluderte vi med at $a^{-1} = 9$, gitt at $5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$. Det er viktig å merke seg at det omvendte også gjelder. Det vil si at når $a = 9$ og $N = 11$, er det tilfelle at $a^{-1} = 5$.

### Eulers teorem

Før vi går videre til RSA-problemet, må vi forstå enda et viktig teorem, nemlig **Eulers teorem**. Den sier følgende:

**Setning 3**. Anta at to heltall $a$ og $N$ er koprimale. Da er $a^{\phi(N)} \mod N = 1 \mod N$.

Dette er et oppsiktsvekkende resultat, men litt forvirrende til å begynne med. La oss se på et eksempel for å forstå det.

Anta at $a = 5$ og $N = 7$. Disse er faktisk koprim, slik Eulers teorem krever. Vi vet at ordenen til 7 er lik 6, gitt at 7 er et primtall (se **Proposisjon 1**).

Eulers teorem sier nå at $5^6 \mod 7$ må være lik $1 \mod 7$. Nedenfor følger beregningene som viser at dette faktisk er sant.


- $5^6 \mod 7 = 15 625 \mod 7 = 1 \mod N$

Heltallet 7 deler seg på 15 624 i alt 2 233 ganger. Resten av 16 625 dividert med 7 er derfor 1.

Ved hjelp av Eulers Phi-funksjon, **Setning 2**, kan du utlede **Setning 5** nedenfor.

**Proposisjon 5**. $\phi(a \cdot b) = \phi(a) \cdot \phi(b)$ for alle positive heltall $a$ og $b$.

Vi skal ikke vise hvorfor dette er tilfelle. Men merk bare at du allerede har sett bevis for denne proposisjonen ved at $\phi(p \cdot q) = \phi(p) \cdot \phi(q) = (p - 1) \cdot (q - 1)$ når $p$ og $q$ er primtall, som angitt i **Proposisjon 2**.

Eulers teorem sammenholdt med **Proposisjon 5** har viktige implikasjoner. Se for eksempel hva som skjer i uttrykkene nedenfor, der $a$ og $N$ er koprim.


- $a^{2 \cdot \phi(N)} \mod N = a^{\phi(N)} \cdot a^{\phi(N)} \mod N = 1 \cdot 1 \mod N = 1 \mod N$
- $a^{\phi(N) + 1} \mod N = a^{\phi(N)} \cdot a^1 \mod N = 1 \cdot a^1 \mod N = a \mod N$
- $a^{8 \cdot \phi(N) + 3} \mod N = a^{8 \cdot \phi(N)} \cdot a^3 \mod N = 1 \cdot a^3 \mod N = a^3 \mod N$

Kombinasjonen av Eulers teorem og **Setning 5** gjør at vi enkelt kan beregne en rekke uttrykk. Generelt kan vi oppsummere innsikten som i **Setning 6**.

**Proposisjon 6**. $a^x \mod N = a^{x \mod \phi(N)}$$

Nå må vi sette alt sammen i et vanskelig siste trinn.

På samme måte som $N$ har en orden $\phi(N)$ som inkluderer elementene i mengden $C_N$, vet vi at heltallet $\phi(N)$ i sin tur også må ha en orden og et sett av koprim. La oss sette $\phi(N) = R$. Da vet vi at det også finnes en verdi for $\phi(R)$ og et sett med koprim $C_R$.

Anta at vi nå velger et heltall $e$ fra mengden $C_R$. Vi vet fra **Proposisjon 3** at dette heltallet $e$ bare har én unik positiv invers som er mindre enn $R$. Det vil si at $e$ har én unik invers fra mengden $C_R$. La oss kalle denne inversen $d$. Gitt definisjonen av en invers, betyr dette at $e \cdot d = 1 \mod R$.

Vi kan bruke dette resultatet til å si noe om vårt opprinnelige heltall $N$. Dette er oppsummert i **Proposisjon 7**.

**Proposisjon 7**. Anta at $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Da må det for ethvert element $a$ i mengden $C_N$ være slik at $a^{e \cdot d \mod \phi(N)} = a^{1 \mod \phi(N)} = a \mod N$.

Vi har nå alle de tallteoretiske resultatene som trengs for å formulere RSA-problemet på en klar måte.

## RSA-kryptosystemet

<chapterId>0253c2f7-b8a4-5d0e-bd60-812ed6b6c7a9</chapterId>

Vi er nå klare til å formulere RSA-problemet. Anta at du oppretter et sett med variabler som består av $p$, $q$, $N$, $\phi(N)$, $e$, $d$ og $y$. Kall dette settet $\Pi$. Det opprettes på følgende måte:

1. Generer to tilfeldige primtall $p$ og $q$ av samme størrelse og beregn deres produkt $N$.

2. Beregn ordenen til $N$, $\phi(N)$, ved hjelp av følgende produkt: $(p - 1) \cdot (q - 1)$.

3. Velg en $e > 2$ slik at den er mindre og koprim til $\phi(N)$.

4. Beregn $d$ ved å sette $e \cdot d \mod \phi(N) = 1$.

5. Velg en tilfeldig verdi $y$ som er mindre og koprim til $N$.

RSA-problemet består i å finne en $x$ slik at $x^e = y$, samtidig som man bare får en delmengde av informasjon om $\Pi$, nemlig variablene $N$, $e$ og $y$. Når $p$ og $q$ er svært store, vanligvis anbefales det at de er 1024 bits store, anses RSA-problemet å være vanskelig. Du kan nå se hvorfor dette er tilfelle, gitt den foregående diskusjonen.

En enkel måte å beregne $x$ når $x^e \mod N = y \mod N$ er ganske enkelt ved å beregne $y^d \mod N$. Vi vet at $y^d \mod N = x \mod N$ ved hjelp av følgende beregninger:

$$ y^d \mod N = x^{e \cdot d} \mod N = x^{e \cdot d \mod \phi(N)} \mod N = x^{1 \mod \phi(N)} \mod N = x \mod N. $$$

Problemet er at vi ikke kjenner verdien $d$, siden den ikke er gitt i oppgaven. Derfor kan vi ikke direkte beregne $y^d \mod N$ for å produsere $x \mod N$.

Vi kan imidlertid kanskje indirekte beregne $d$ ut fra ordenen til $N$, $\phi(N)$, siden vi vet at $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Men forutsetningsvis gir problemet heller ikke en verdi for $\phi(N)$.

Til slutt kan rekkefølgen beregnes indirekte ved hjelp av primfaktorene $p$ og $q$, slik at vi til slutt kan beregne $d$. Men forutsetningen var at vi heller ikke fikk oppgitt verdiene $p$ og $q$.

Strengt tatt kan vi ikke bevise at selv om faktoriseringsproblemet i et RSA-problem er vanskelig, kan vi ikke bevise at RSA-problemet også er vanskelig. Det kan nemlig finnes andre måter å løse RSA-problemet på enn gjennom faktorisering. Det er imidlertid allment akseptert og antatt at hvis faktoriseringsproblemet i RSA-problemet er vanskelig, så er også RSA-problemet i seg selv vanskelig.

Hvis RSA-problemet virkelig er vanskelig, produserer det en enveisfunksjon med en falldør. Funksjonen her er $f(g) = g^e \mod N$. Med kunnskap om $f(g)$ kan hvem som helst enkelt beregne en verdi $y$ for en bestemt $g = x$. Det er imidlertid praktisk talt umulig å beregne en bestemt verdi $x$ bare ved å kjenne verdien $y$ og funksjonen $f(g)$. Unntaket er når du får en opplysning $d$, den såkalte falldøren. I så fall kan du ganske enkelt beregne $y^d$ for å få $x$.

La oss gå gjennom et konkret eksempel for å illustrere RSA-problemet. Jeg kan ikke velge et RSA-problem som ville blitt ansett som vanskelig under de ovennevnte betingelsene, ettersom tallene ville blitt uhåndterlige. I stedet skal dette eksemplet bare illustrere hvordan RSA-problemet generelt fungerer.

Anta at du velger to tilfeldige primtall, 13 og 31. Så $p = 13$ og $q = 31$. Produktet $N$ av disse to primtallene er lik 403. Vi kan enkelt beregne rekkefølgen av 403. Det tilsvarer $(13 - 1) \cdot (31 - 1) = 360$.

Deretter må vi, som foreskrevet i trinn 3 i RSA-problemet, velge et koprim for 360 som er større enn 2 og mindre enn 360. Vi trenger ikke å velge denne verdien tilfeldig. Anta at vi velger 103. Dette er et koprim til 360, siden den største felles divisoren med 103 er 1.

Trinn 4 krever nå at vi beregner en verdi $d$ slik at $103 \cdot d \mod 360 = 1$. Dette er ikke en enkel oppgave for hånd når verdien for $N$ er stor. Det krever at vi bruker en prosedyre som kalles den **utvidede euklidske algoritmen**.

Selv om jeg ikke viser fremgangsmåten her, gir den verdien 7 når $e = 103$. Du kan verifisere at verdiparet 103 og 7 faktisk oppfyller den generelle betingelsen $e \cdot d \mod \phi(n) = 1$ ved hjelp av beregningene nedenfor.


- $103 \cdot 7 \mod 360 = 721 \mod 360 = 1 \mod 360$$

Det er viktig å merke seg at gitt *Proposisjon 4*, vet vi at ingen andre heltall mellom 1 og 360 for $d$ vil gi resultatet at $103 \cdot d = 1 \mod 360$. I tillegg impliserer proposisjonen at valg av en annen verdi for $e$ vil gi en annen unik verdi for $d$.

I trinn 5 av RSA-problemet må vi velge et positivt heltall $y$ som er et mindre koprim av 403. Anta at vi setter $y = 2^{103}$. Eksponentiering av 2 med 103 gir resultatet nedenfor.


- $2^{103} \mod 403 = 10 141 204 801 825 835 835 211 973 625 643 008 \mod 403 = 349 \mod 403$

RSA-problemet i dette eksemplet er nå som følger: Du får $N = 403$, $e = 103$ og $y = 349 \mod 403$. Du må nå beregne $x$ slik at $x^{103} = 349 \mod 403$. Det vil si at du må finne ut at den opprinnelige verdien før eksponentiering med 103 var 2.

Det ville være enkelt (i hvert fall for en datamaskin) å beregne $x$ hvis vi visste at $d = 7$. I så fall kunne du bare bestemme $x$ som nedenfor.


- $x = y^7 \mod 403 = 349^7 \mod 403 = 630 634 881 591 804 949 \mod 403 = 2 \mod 403$ $x = y^7 \mod 403 = 349^7

Problemet er at du ikke har fått informasjon om at $d = 7$. Du kan selvfølgelig regne ut $d$ ut fra det faktum at $103 \cdot d = 1 \mod 360$. Problemet er at du heller ikke har fått informasjon om at rekkefølgen til $N = 360$. Til slutt kan du også beregne rekkefølgen av 403 ved å beregne følgende produkt: $(p - 1) \cdot (q - 1)$. Men du får heller ikke vite at $p = 13$ og $q = 31$.

En datamaskin kan selvfølgelig fortsatt løse RSA-problemet for dette eksemplet relativt enkelt, fordi primtallene som er involvert, ikke er så store. Men når primtallene blir veldig store, blir det en praktisk talt umulig oppgave.

Vi har nå presentert RSA-problemet, et sett med betingelser for at det er vanskelig, og den underliggende matematikken. Hvordan hjelper dette oss med asymmetrisk kryptografi? Nærmere bestemt, hvordan kan vi gjøre RSA-problemets vanskelighetsgrad under visse betingelser om til et krypteringsopplegg eller et digitalt signaturopplegg?

En tilnærming er å ta utgangspunkt i RSA-problemet og bygge opp ordninger på en enkel måte. Anta for eksempel at du har generert et sett med variabler $\Pi$ som beskrevet i RSA-problemet, og sørg for at $p$ og $q$ er tilstrekkelig store. Du setter din offentlige nøkkel lik $(N, e)$ og deler denne informasjonen med omverdenen. Som beskrevet ovenfor holder du verdiene for $p$, $q$, $\phi(n)$ og $d$ hemmelige. Faktisk er $d$ din private nøkkel.

Den som ønsker å sende deg en melding $m$ som er et element i $C_N$, kan ganske enkelt kryptere den på følgende måte: $c = m^e \mod N$. (Krypteringsteksten $c$ her tilsvarer verdien $y$ i RSA-problemet.) Du kan enkelt dekryptere denne meldingen ved å bare beregne $c^d \mod N$.

Du kan prøve å lage et digitalt signaturskjema på samme måte. Anta at du ønsker å sende noen en melding $m$ med en digital signatur $S$. Du kan bare sette $S = m^d \mod N$ og sende paret $(m,S)$ til mottakeren. Hvem som helst kan verifisere den digitale signaturen ved å sjekke om $S^e \mod N = m \mod N$. Enhver angriper vil imidlertid ha svært vanskelig for å lage en gyldig $S$ for en melding, gitt at de ikke har $d$.

Dessverre er det ikke så enkelt å gjøre det som i seg selv er et vanskelig problem, RSA-problemet, om til et kryptografisk opplegg. For det enkle krypteringsopplegget kan du bare velge koprim av $N$ som meldinger. Det gir oss ikke mange mulige meldinger, i hvert fall ikke nok til standard kommunikasjon. I tillegg må disse meldingene velges tilfeldig. Det virker noe upraktisk. Til slutt vil enhver melding som velges to ganger, gi nøyaktig samme krypteringstekst. Dette er ekstremt uønsket i et krypteringsopplegg, og det oppfyller ingen strenge, moderne standardkrav til sikkerhet i kryptering.

Problemene blir enda verre for vår enkle digitale signaturordning. Slik det er nå, kan enhver angriper enkelt forfalske digitale signaturer bare ved først å velge et koprim av $N$ som signatur og deretter beregne den tilsvarende originale meldingen. Dette bryter helt klart med kravet om eksistensiell uforfalskbarhet.

Likevel kan RSA-problemet brukes til å lage et sikkert krypteringssystem med offentlig nøkkel og et sikkert system for digital signatur ved å legge til litt ekstra kompleksitet. Vi vil ikke gå inn på detaljene i slike konstruksjoner her. [4] Det er imidlertid viktig å merke seg at denne ekstra kompleksiteten ikke endrer det grunnleggende RSA-problemet som disse systemene er basert på.

**Noter:**

[4] Se for eksempel Jonathan Katz og Yehuda Lindell, _Introduction to Modern Cryptography_, CRC Press (Boca Raton, FL: 2015), s. 410-32 om RSA-kryptering og s. 444-41 om RSA-digitale signaturer.

# Konklusjon

<partId>e538fb79-bf28-40cd-a5c3-badf864d8567</partId>

## Anmeldelse & Vurdering

<chapterId>366d6fd0-ceb2-4299-bf37-8c6dfcb681d5</chapterId>
<isCourseReview>true</isCourseReview>
 
## Avsluttende Eksamen


<chapterId>44882d2b-63cd-4fde-8485-f76f14d8b2fe</chapterId>
<isCourseExam>true</isCourseExam>

## Konklusjon

<chapterId>f1905f78-8cf7-5031-949a-dfa8b76079b4</chapterId>
<isCourseConclusion>true</isCourseConclusion>
