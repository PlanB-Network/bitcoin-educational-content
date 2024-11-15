---
name: Introduksjon til formell kryptografi
goal: En grundig introduksjon til vitenskapen og praksisen med kryptografi.
objectives:
  - Utforske Beale-chiffer og moderne kryptografiske metoder for å forstå grunnleggende og historiske konsepter innen kryptografi.
  - Dykke ned i tallteori, grupper og felt for å mestre nøkkelmatematiske konsepter som ligger til grunn for kryptografi.
  - Studere RC4-strømchifferet og AES med en 128-bits nøkkel for å lære om symmetriske kryptografiske algoritmer.
  - Undersøke RSA-kryptosystemet, nøkkeldistribusjon og hash-funksjoner for å utforske asymmetrisk kryptografi.

---
# Grundig dykk i kryptografi

Det er vanskelig å finne mange materialer som tilbyr et godt mellomnivå i kryptografiutdanning.

På den ene siden finnes det lange, formelle avhandlinger, som virkelig bare er tilgjengelige for de med en sterk bakgrunn i matematikk, logikk eller noen annen formell disiplin. På den andre siden finnes det veldig overfladiske introduksjoner som virkelig skjuler for mange av detaljene for noen som er i det minste litt nysgjerrige.

Denne introduksjonen til kryptografi søker å fange mellomnivået. Selv om den skal være relativt utfordrende og detaljert for alle som er nye til kryptografi, er det ikke kaninhullet til en typisk grunnleggende avhandling.

+++

# Introduksjon
<partId>bbed2f46-d64c-5fb5-b892-d726032f2494</partId>

## Kort beskrivelse
<chapterId>bb8a8b73-7fb2-50da-bf4e-98996d79887b</chapterId>

Denne boken tilbyr en grundig introduksjon til vitenskapen og praksisen med kryptografi. Der det er mulig fokuserer den på konseptuell, snarere enn formell fremstilling av materialet.

> Dette kurset er basert på [JWBurgers's repo](https://github.com/JWBurgers/An_Introduction_to_Cryptography). Alle rettigheter til ham. Innholdet er ikke ferdig ennå og er bare her for å vise hvordan vi kunne integrere det hvis JWburger er enig.

### Motivasjon og mål

Det er vanskelig å finne mange materialer som tilbyr et godt mellomnivå i kryptografiutdanning.

På den ene siden finnes det lange, formelle avhandlinger, som virkelig bare er tilgjengelige for de med en sterk bakgrunn i matematikk, logikk eller noen annen formell disiplin. På den andre siden finnes det veldig overfladiske introduksjoner som virkelig skjuler for mange av detaljene for noen som er i det minste litt nysgjerrige.

Denne introduksjonen til kryptografi søker å fange mellomnivået. Selv om den skal være relativt utfordrende og detaljert for alle som er nye til kryptografi, er det ikke kaninhullet til en typisk grunnleggende avhandling.

### Målgruppe

Fra utviklere til intellektuelt nysgjerrige, denne boken er nyttig for alle som ønsker mer enn en overfladisk forståelse av kryptografi. Hvis målet ditt er å mestre feltet kryptografi, så er denne boken også et godt utgangspunkt.

### Leserveiledning

Boken inneholder for øyeblikket syv kapitler: "Hva er kryptografi?" (Kapittel 1), "Matematiske grunnlag for kryptografi I" (Kapittel 2), "Matematiske grunnlag for kryptografi II" (Kapittel 3), "Symmetrisk kryptografi" (Kapittel 4), "RC4 og AES" (Kapittel 5), "Asymmetrisk kryptografi" (Kapittel 6), og "RSA-kryptosystemet" (Kapittel 7). Et siste kapittel, "Kryptografi i praksis", vil fortsatt bli lagt til. Det fokuserer på ulike kryptografiske applikasjoner, inkludert transportlagsikkerhet, onion routing og Bitcoins verdioverføringssystem.
Med mindre du har en solid bakgrunn i matematikk, er tallteori sannsynligvis det vanskeligste emnet i denne boken. Jeg gir en oversikt over det i Kapittel 3, og det dukker også opp i fremstillingen av AES i Kapittel 5 og RSA-kryptosystemet i Kapittel 7.
Hvis du virkelig sliter med de formelle detaljene i disse delene av boken, anbefaler jeg at du nøyer deg med en høy-nivå lesning av dem første gangen.

### Anerkjennelser

Den mest innflytelsesrike boken i utformingen av denne har vært Jonathan Katz og Yehuda Lindells _Introduction to Modern Cryptography_, CRC Press (Boca Raton, FL), 2015. Et tilhørende kurs er tilgjengelig på Coursera kalt "Cryptography."

De viktigste tilleggsressursene som har vært nyttige i å skape oversikten i denne boken er Simon Singh, _The Code Book_, Fourth Estate (London, 1999); Christof Paar og Jan Pelzl, _Understanding Cryptography_, Springer (Heidelberg, 2010) og [et kurs basert på boken av Paar kalt “Introduction to Cryptography”](https://www.youtube.com/channel/UC1usFRN4LCMcfIV7UjHNuQg); og Bruce Schneier, Applied Cryptography, 2. utg, 2015 (Indianapolis, IN: John Wiley & Sons).

Jeg vil bare sitere veldig spesifikk informasjon og resultater jeg tar fra disse kildene, men ønsker å anerkjenne min generelle gjeld til dem her.

For de leserne som ønsker å søke ut mer avansert kunnskap om kryptografi etter denne introduksjonen, anbefaler jeg sterkt Katz og Lindells bok. Katzs kurs på Coursera er noe mer tilgjengelig enn boken.

### Bidrag

Vennligst ta en titt på [bidragsfilen i repositoriet](https://github.com/JWBurgers/An_Introduction_to_Cryptography/blob/master/Contributions.md) for noen retningslinjer om hvordan du kan støtte prosjektet.

### Notasjon

**Nøkkelbegreper:**

Nøkkelbegreper i grunnleggende tekster blir introdusert ved å gjøre dem fete. For eksempel, introduksjonen av Rijndael-sifferet som et nøkkelbegrep ville se slik ut: **Rijndael-sifferet**.

Nøkkelbegreper er eksplisitt definert, med mindre de er egennavn eller deres betydning er åpenbar fra diskusjonen.

Enhver definisjon er vanligvis gitt ved introduksjonen av et nøkkelbegrep, selv om det noen ganger er mer praktisk å utsette definisjonen til et senere punkt.

**Fremhevede ord og uttrykk:**

Ord og uttrykk blir fremhevet via kursiv. For eksempel, uttrykket "Husk passordet ditt" ville se slik ut: *Husk passordet ditt*.

**Formell notasjon:**

Den formelle notasjonen angår hovedsakelig variabler, tilfeldige variabler og sett.

* Variabler: Disse er vanligvis bare indikert med en liten bokstav (f.eks., "x" eller "y"). Noen ganger er de skrevet med stor bokstav for klarhet (f.eks., "M" eller "K").
* Tilfeldige variabler: Disse er alltid indikert med en stor bokstav (f.eks., "X" eller "Y")
* Sett: Disse er alltid indikert med fete, store bokstaver (f.eks., **S**)

# Hva er kryptografi?
<partId>48e4d6d5-cd00-5c00-8adb-ae8477ff47c4</partId>

## Beale-chifferne
<chapterId>ae674346-4789-5ab1-9b6f-c8989d83be89</chapterId>
La oss starte vår utforskning av kryptografifeltet med en av de mer sjarmerende og underholdende episodene i dets historie: den om Beale-chifferne. [1]
Historien om Beale-chifferne er, etter min mening, mer sannsynlig fiksjon enn virkelighet. Men den skal angivelig ha skjedd som følger.

Både vinteren 1820 og 1822 bodde en mann ved navn Thomas J. Beale på et vertshus eid av Robert Morriss i Lynchburg (Virginia). Ved slutten av Beales andre opphold, overleverte han Morriss en jernboks med verdifulle papirer for oppbevaring.

Noen måneder senere mottok Morriss et brev fra Beale datert 9. mai 1822. Det understreket den store verdien av innholdet i jernboksen og relaterte noen instruksjoner til Morriss: hvis verken Beale eller noen av hans medarbeidere noen gang kom for å kreve boksen, skulle han åpne den nøyaktig ti år fra datoen for brevet (det vil si 9. mai 1832). Noen av papirene inne ville være skrevet i vanlig tekst. Flere andre, derimot, ville være "uforståelige uten hjelp av en nøkkel." Denne "nøkkelen" ville da bli levert til Morriss av en unevnt venn av Beale i juni 1832.

Til tross for de klare instruksjonene, åpnet ikke Morriss boksen i mai 1832, og Beales mystiske venn dukket aldri opp i juni det året. Det var ikke før i 1845 at vertshuseieren endelig bestemte seg for å åpne boksen. I den fant Morriss et notat som forklarte hvordan Beale og hans medarbeidere oppdaget gull og sølv i vest og begravde det, sammen med noe smykker, for sikkerhets skyld. I tillegg inneholdt boksen tre **chiffertekster**: det vil si tekster skrevet i kode som krever en **kryptografisk nøkkel**, eller en hemmelighet, og en tilhørende algoritme for å låse opp. Denne prosessen med å låse opp en chiffertekst er kjent som **dekryptering**, mens låseprosessen er kjent som **kryptering**. (Som forklart i Kapittel 3, kan begrepet chiffer ta på seg ulike betydninger. I navnet "Beale-chifferne", er det kort for chiffertekster.)

De tre chiffertekstene som Morriss fant i jernboksen består hver av en serie tall skilt med komma. Ifølge Beales notat gir disse chiffertekstene separat plasseringen av skatten, innholdet i skatten, og en liste over navn med rettmessige arvinger til skatten og deres andeler (den sistnevnte informasjonen er relevant i tilfelle Beale og hans medarbeidere aldri kom for å kreve boksen).

Morris forsøkte å dekryptere de tre chiffertekstene i tjue år. Dette ville ha vært enkelt med nøkkelen. Men Morriss hadde ikke nøkkelen og var mislykket i sine forsøk på å gjenvinne de opprinnelige tekstene, eller **klartekster** som de vanligvis kalles i kryptografi.

Nær slutten av sitt liv, overleverte Morriss boksen til en venn i 1862. Denne vennen publiserte senere en pamflett i 1885, under pseudonymet J.B. Ward. Den inkluderte en beskrivelse av den (påståtte) historien om boksen, de tre chiffertekstene, og en løsning som han hadde funnet for den andre chifferteksten. (Åpenbart er det en nøkkel for hver chiffertekst, og ikke en nøkkel som fungerer på alle tre chiffertekstene som Beale opprinnelig ser ut til å ha foreslått i sitt brev til Morriss.)

Du kan se den andre chifferteksten i *Figur 2* nedenfor. [2] Nøkkelen til denne chifferteksten er USAs uavhengighetserklæring. Dekrypteringsprosedyren kommer ned til å anvende følgende to regler:
* For ethvert tall n i chifferteksten, finn det n-te ordet i USAs uavhengighetserklæring* Erstatt tallet n med den første bokstaven i ordet du fant


*Figur 1: Beale-chiffer nr. 2*

![Figur 1: Beale-chiffer nr. 2](assets/Figure1-1.webp "Figur 1: Beale-chiffer nr. 2")


For eksempel, det første tallet i den andre chifferteksten er 115. Det 115. ordet i uavhengighetserklæringen er “instituted,” så den første bokstaven i klarteksten er “i.” Chifferteksten indikerer ikke direkte ordspasering og store bokstaver. Men etter å ha dekryptert de første få ordene, kan man logisk utlede at det første ordet i klarteksten var rett og slett “I.” (Klarteksten starter med frasen “I have deposited in the county of Bedford.”)

Etter dekryptering gir den andre meldingen detaljerte innholdet av skatten (gull, sølv og juveler), og antyder at den var begravet i jernpotter og dekket med steiner i Bedford County (Virginia). Folk elsker et godt mysterium, så store anstrengelser har blitt gjort for å dekryptere de andre to Beale-chiffrene, spesielt den som beskriver skattens plassering. Selv ulike fremtredende kryptografer har prøvd seg på dem. Imidlertid har ingen så langt klart å dekryptere de to andre chiffertekstene.


**Notater:**

[1] For en god oppsummering av historien, se Simon Singh, *The Code Book*, Fourth Estate (London, 1999), s. 82-99. En kortfilm av historien ble laget av Andrew Allen i 2010. Du kan finne filmen, “The Thomas Beale Cipher,” [på dens nettside](http://www.thomasbealecipher.com/).

[2] Dette bildet er tilgjengelig på Wikipedia-siden for Beale-chiffrene.


## Moderne kryptografi
<chapterId>d07d576f-8a4b-5890-b182-2e5763f550f4</chapterId>

Fargerike historier som den om Beale-chiffrene er hva de fleste av oss forbinder med kryptografi. Likevel, moderne kryptografi skiller seg på minst fire viktige måter fra disse typer historiske eksempler.

Først, historisk sett har kryptografi kun vært opptatt av **hemmelighold** (eller konfidensialitet). [3] Chiffertekster ville bli skapt for å sikre at bare visse parter kunne være inneforstått med informasjonen i klartekstene, som i tilfellet med Beale-chiffrene. For at et krypteringssystem skal tjene dette formålet godt, bør dekryptering av chifferteksten bare være gjennomførbar hvis du har nøkkelen.

Moderne kryptografi er opptatt av et bredere spekter av temaer enn bare hemmelighold. Disse temaene inkluderer primært (1) **meldingsintegritet**—det vil si, å forsikre at en melding ikke har blitt endret; (2) **meldingsautentisitet**—det vil si, å forsikre at en melding virkelig kommer fra en bestemt avsender; og (3) **ikke-avvisning**—det vil si, å forsikre at en avsender ikke kan falskt benekte senere at hun sendte en melding. [4]

En viktig forskjell å huske på er dermed mellom et **krypteringssystem** og et **kryptografisk system**. Et krypteringssystem er kun opptatt av hemmelighold. Mens et krypteringssystem er et kryptografisk system, er det motsatte ikke sant. Et kryptografisk system kan også tjene de andre hovedtemaene i kryptografi, inkludert integritet, autentisitet og ikke-avvisning.
Temaene integritet og autentisitet er like viktige som hemmelighold. Våre moderne kommunikasjonssystemer ville ikke kunne fungere uten garantier angående integritet og autentisitet i kommunikasjonen. Ikke-avvisning er også en viktig bekymring, som for digitale kontrakter, men mindre allestedsnærværende nødvendig i kryptografiske applikasjoner enn hemmelighold, integritet og autentisitet.
For det andre involverte klassiske krypteringsskjemaer, som Beale-chifferne, alltid én nøkkel som ble delt blant alle relevante parter. Mange moderne kryptografiske skjemaer involverer imidlertid ikke bare én, men to nøkler: en **privat** og en **offentlig nøkkel**. Mens den førstnevnte bør forbli privat i alle applikasjoner, er den sistnevnte typisk offentlig kjent (derav deres respektive navn). Innenfor krypteringens verden kan den offentlige nøkkelen brukes til å kryptere meldingen, mens den private nøkkelen kan brukes for dekryptering.

Grenen av kryptografi som håndterer skjemaer hvor alle parter deler én nøkkel, er kjent som **symmetrisk kryptografi**. Den enkelte nøkkelen i et slikt skjema kalles vanligvis den **private nøkkelen** (eller hemmelige nøkkelen). Grenen av kryptografi som håndterer skjemaer som krever et par av private-offentlige nøkler, er kjent som **asymmetrisk kryptografi**. Disse grenene refereres noen ganger også til som **privat nøkkelkryptografi** og **offentlig nøkkelkryptografi**, henholdsvis (selv om dette kan skape forvirring, ettersom offentlig nøkkel kryptografiske skjemaer også har private nøkler).

Innføringen av asymmetrisk kryptografi på slutten av 1970-tallet har vært en av de viktigste hendelsene i kryptografiens historie. Uten den, ville de fleste av våre moderne kommunikasjonssystemer, inkludert Bitcoin, ikke være mulige, eller i det minste veldig upraktiske.

Viktig, moderne kryptografi er ikke utelukkende studiet av symmetriske og asymmetriske nøkkelkryptografiske skjemaer (selv om det dekker mye av feltet). For eksempel er kryptografi også opptatt av hash-funksjoner og pseudotilfeldige nummergeneratorer, og du kan bygge applikasjoner på disse primitivene som ikke er relatert til symmetrisk eller asymmetrisk nøkkelkryptografi.

For det tredje var klassiske krypteringsskjemaer, som de som ble brukt i Beale-chifferne, mer kunst enn vitenskap. Deres oppfattede sikkerhet var i stor grad basert på intuisjoner angående deres kompleksitet. De ville typisk bli lappet når et nytt angrep på dem ble lært, eller droppet helt hvis angrepet var spesielt alvorlig. Moderne kryptografi, derimot, er en streng vitenskap med en formell, matematisk tilnærming til både utvikling og analyse av kryptografiske skjemaer. [5]

Spesifikt, moderne kryptografi sentrerer på formelle **sikkerhetsbevis**. Ethvert sikkerhetsbevis for et kryptografisk skjema utføres i tre trinn:

1.	Uttrykket for en **kryptografisk definisjon av sikkerhet**, det vil si et sett med sikkerhetsmål og trusselen som angriperen utgjør.
2.	Uttrykket for eventuelle matematiske antakelser med hensyn til den beregningsmessige kompleksiteten av skjemaet. For eksempel kan et kryptografisk skjema inneholde en pseudotilfeldig nummergenerator. Selv om vi ikke kan bevise at disse eksisterer, kan vi anta at de gjør det.
3.	Fremleggelsen av et matematisk **sikkerhetsbevis** for skjemaet på grunnlag av den formelle sikkerhetsnotasjonen og eventuelle matematiske antakelser.

For det fjerde, mens kryptografi historisk sett primært ble brukt i militære innstillinger, har det kommet til å gjennomsyre våre daglige aktiviteter i den digitale tidsalderen. Enten du driver med nettbank, poster på sosiale medier, kjøper et produkt fra Amazon med kredittkortet ditt, eller tipser en venn i bitcoin, er kryptografi en absolutt nødvendighet i vår digitale tidsalder.

Gitt disse fire aspektene ved moderne kryptografi, kan vi karakterisere moderne **kryptografi** som vitenskapen som er opptatt av den formelle utviklingen og analysen av kryptografiske skjemaer for å sikre digital informasjon mot fiendtlige angrep. [6] Sikkerhet her bør forstås bredt som å forhindre angrep som skader hemmelighold, integritet, autentisering og/eller ikke-avvisning i kommunikasjon.
Kryptografi er best sett på som en underdisiplin av **cybersikkerhet**, som handler om å forhindre tyveri, skade og misbruk av datasystemer. Merk at mange cybersikkerhetsbekymringer har lite eller bare delvis tilknytning til kryptografi.
For eksempel, hvis et selskap har dyre servere lokalt, kan de være bekymret for å sikre dette maskinvaret mot tyveri og skade. Selv om dette er en cybersikkerhetsbekymring, har det lite å gjøre med kryptografi.

For et annet eksempel, **phishing-angrep** er et vanlig problem i vår moderne tid. Disse angrepene forsøker å lure folk via en e-post eller et annet meldingsmedium til å gi fra seg sensitiv informasjon som passord eller kredittkortnumre. Selv om kryptografi kan bidra til å adressere phishing-angrep til en viss grad, krever en omfattende tilnærming mer enn bare å bruke litt kryptografi.

**Notater:**

[3] For å være nøyaktig, har de viktige anvendelsene av kryptografiske ordninger vært opptatt av hemmelighold. Barn, for eksempel, bruker ofte enkle kryptografiske ordninger for "moro". Hemmelighold er egentlig ikke en bekymring i disse tilfellene.

[4] Bruce Schneier, *Applied Cryptography*, 2. utg., 2015 (Indianapolis, IN: John Wiley & Sons), s. 2.

[5] Se Jonathan Katz og Yehuda Lindell, *Introduction to Modern Cryptography*, CRC Press (Boca Raton, FL: 2015), spesielt ss. 16–23, for en god beskrivelse.

[6] Jf. Katz og Lindell, ibid., s. 3. Jeg tror deres karakterisering har noen problemer, så jeg presenterer en litt annen versjon av deres uttalelse her.

## Åpen kommunikasjon
<chapterId>cb23d0a6-ba9a-5dc6-a55a-258405ae4117</chapterId>

Moderne kryptografi er designet for å gi sikkerhetsforsikringer i et **åpent kommunikasjons** miljø. Hvis vår kommunikasjonskanal er så godt beskyttet at avlyttere ikke har noen sjanse til å manipulere eller til og med bare observere våre meldinger, da er kryptografi overflødig. De fleste av våre kommunikasjonskanaler er imidlertid langt fra så godt voktet.

Rygraden i kommunikasjon i den moderne verden er et massivt nettverk av fiber optiske kabler. Å ringe, se på fjernsyn og surfe på nettet i et moderne husholdning stoler generelt på dette nettverket av fiber optiske kabler (en liten prosentandel kan stole rent på satellitter). Det er sant at du kanskje har forskjellige dataforbindelser i hjemmet ditt, som koaksialkabel, (asymmetrisk) digital abonnentlinje og fiber optisk kabel. Men, i hvert fall i den utviklede verden, slutter disse forskjellige datamediene raskt utenfor huset ditt til en node i et massivt nettverk av fiber optiske kabler som kobler hele kloden. Unntakene er noen avsidesliggende områder i den utviklede verden, som i USA og Australia, hvor datatrafikk fortsatt også kan reise betydelige avstander over tradisjonelle kobber telefonledninger.

Det ville være umulig å forhindre potensielle angripere fra fysisk tilgang til dette nettverket av kabler og dets støtteinfrastruktur. Faktisk vet vi allerede at de fleste av våre data blir avlyttet av ulike nasjonale etterretningsbyråer ved kritiske kryss av internettet.[7] Dette inkluderer alt fra Facebook-meldinger til nettsideadresser du besøker.

Selv om overvåking av data i stor skala krever en kraftig motstander, som et nasjonalt etterretningsbyrå, kan angripere med bare få ressurser enkelt forsøke å snuse på en mer lokal skala. Selv om dette kan skje på nivået av å tappe ledninger, er det langt enklere å bare avlytte trådløs kommunikasjon.
De fleste av våre lokale nettverksdata—enten det er hjemme, på kontoret, eller i en kafé—reiser nå via radiobølger til trådløse tilgangspunkter på alt-i-ett-rutere, i stedet for gjennom fysiske kabler. Så en angriper trenger lite ressurser for å avlytte noe av din lokale trafikk. Dette er spesielt bekymringsfullt ettersom de fleste mennesker gjør svært lite for å beskytte dataene som reiser over deres lokale nettverk. I tillegg kan potensielle angripere også målrette våre mobile bredbåndsforbindelser, som 3G, 4G og 5G. Alle disse trådløse kommunikasjonene er et lett mål for angripere.
Derfor er ideen om å holde kommunikasjon hemmelig ved å beskytte kommunikasjonskanalen en håpløst illusorisk ambisjon for mye av den moderne verden. Alt vi vet berettiger alvorlig paranoia: du bør alltid anta at noen lytter. Og kryptografi er det viktigste verktøyet vi har for å oppnå noen form for sikkerhet i dette moderne miljøet.

**Notater:**

[7] Se, for eksempel, Olga Khazan, “The creepy, long-standing practice of undersea cable tapping”, *The Atlantic*, 16. juli 2013 (tilgjengelig på [The Atlantic](https://www.theatlantic.com/international/archive/2013/07/the-creepy-long-standing-practice-of-undersea-cable-tapping/277855/)).

# Matematiske grunnlag for kryptografi 1
<partId>1bf9f0aa-0f68-5493-83fb-2167238ff9de</partId>

## Tilfeldige variabler
<chapterId>b623a7d0-3dff-5803-bd4e-8257ff73dd69</chapterId>

Kryptografi er avhengig av matematikk. Og hvis du ønsker å bygge mer enn en overfladisk forståelse av kryptografi, må du være komfortabel med den matematikken.

Dette kapittelet introduserer det meste av den grunnleggende matematikken du vil møte i læringen av kryptografi. Emnene inkluderer tilfeldige variabler, modulo-operasjoner, XOR-operasjoner og pseudotilfeldighet. Du bør mestre materialet i disse seksjonene for enhver ikke-overfladisk forståelse av kryptografi.

Neste seksjon omhandler tallteori, som er mye mer utfordrende.

### Tilfeldige variabler

En tilfeldig variabel betegnes vanligvis med en ikke-fet, stor bokstav. Så, for eksempel, kan vi snakke om en tilfeldig variabel $X$, en tilfeldig variabel $Y$, eller en tilfeldig variabel $Z$. Dette er notasjonen jeg også vil bruke heretter.

En **tilfeldig variabel** kan ta to eller flere mulige verdier, hver med en viss positiv sannsynlighet. De mulige verdiene er oppført i **utfallssettet**.

Hver gang du **prøver** en tilfeldig variabel, trekker du en bestemt verdi fra utfallssettet i henhold til de definerte sannsynlighetene.

La oss se på et enkelt eksempel. Anta en variabel X som er definert som følger:

- X har utfallssettet $\{1,2\}$

$$
Pr[X = 1] = 0.5
$$

$$
Pr[X = 2] = 0.5
$$

Det er lett å se at $X$ er en tilfeldig variabel. Først, det er to eller flere mulige verdier som $X$ kan ta, nemlig $1$ og $2$. For det andre, hver mulig verdi har en positiv sannsynlighet for å inntreffe når du prøver $X$, nemlig $0.5$.
Alt som kreves av en tilfeldig variabel er et utfallssett med to eller flere muligheter, der hver mulighet har en positiv sannsynlighet for å inntreffe ved prøvetaking. I prinsippet kan derfor en tilfeldig variabel defineres abstrakt, uten noen kontekst. I dette tilfellet kan du tenke på "prøvetaking" som å utføre et naturlig eksperiment for å bestemme verdien av den tilfeldige variabelen.
Variabelen $X$ ovenfor ble definert abstrakt. Du kan dermed tenke på prøvetaking av variabelen $X$ ovenfor som å kaste en rettferdig mynt og tildele "2" i tilfelle av kron og "1" i tilfelle av mynt. For hver prøve av $X$, kaster du mynten på nytt.

Alternativt kan du også tenke på prøvetaking av $X$, som å rulle en rettferdig terning og tildele "2" i tilfelle terningen lander på $1$, $3$, eller $4$, og tildele "1" i tilfelle terningen lander på $2$, $5$, eller $6$. Hver gang du prøvetar $X$, ruller du terningen på nytt.

Virkelig, ethvert naturlig eksperiment som ville tillate deg å definere sannsynlighetene for de mulige verdiene av $X$ ovenfor, kan forestilles med hensyn til tegningen.

Ofte er imidlertid tilfeldige variabler ikke bare introdusert abstrakt. I stedet har settet med mulige utfallsverdier en eksplisitt virkelighetsnær betydning (i stedet for bare som tall). I tillegg kan disse utfallsverdiene være definert mot en spesifikk type eksperiment (i stedet for som ethvert naturlig eksperiment med disse verdiene).

La oss nå vurdere et eksempel på variabelen $X$ som ikke er definert abstrakt. X er definert som følger for å bestemme hvilket av to lag som starter en fotballkamp:

- $X$ har utfallssettet {rødt lag sparker i gang, blått lag sparker i gang}
- Kast en spesiell mynt $C$: mynt = “rødt lag sparker i gang”; kron = “blått lag sparker i gang”

$$
Pr [X = \text{rødt lag sparker i gang}] = 0.5
$$

$$
Pr [X = \text{blått lag sparker i gang}] = 0.5
$$

I dette tilfellet er utfallssettet til X gitt en konkret betydning, nemlig hvilket lag som starter i en fotballkamp. I tillegg er de mulige utfallene og deres tilknyttede sannsynligheter bestemt av et konkret eksperiment, nemlig å kaste en spesiell mynt $C$.

Innen diskusjoner om kryptografi blir tilfeldige variabler vanligvis introdusert mot et utfallssett med virkelighetsnær betydning. Det kan være settet med alle meldinger som kan krypteres, kjent som meldingsrommet, eller settet med alle nøkler partene som bruker krypteringen kan velge fra, kjent som nøkkelrommet.

Tilfeldige variabler i diskusjoner om kryptografi er imidlertid vanligvis ikke definert mot et spesifikt naturlig eksperiment, men mot ethvert eksperiment som kan gi de riktige sannsynlighetsfordelingene.

Tilfeldige variabler kan ha diskrete eller kontinuerlige sannsynlighetsfordelinger. Tilfeldige variabler med en **diskret sannsynlighetsfordeling**—det vil si diskrete tilfeldige variabler—har et endelig antall mulige utfall. Den tilfeldige variabelen $X$ i begge eksemplene som er gitt så langt, var diskret.

**Kontinuerlige tilfeldige variabler** kan derimot ta verdier i ett eller flere intervaller. Du kan for eksempel si at en tilfeldig variabel, ved prøvetaking, vil ta et hvilket som helst reelt tall mellom 0 og 1, og at hvert reelt tall i dette intervallet er like sannsynlig. Innenfor dette intervallet er det uendelig mange mulige verdier.

For kryptografiske diskusjoner trenger du bare å forstå diskrete tilfeldige variabler. Enhver diskusjon om tilfeldige variabler herfra og ut bør derfor forstås som å referere til diskrete tilfeldige variabler, med mindre noe annet er spesifikt angitt.

### Grafing av tilfeldige variabler
De mulige verdiene og tilhørende sannsynligheter for en tilfeldig variabel kan enkelt visualiseres gjennom et diagram. For eksempel, vurder den tilfeldige variabelen $X$ fra forrige avsnitt med et utfallssett på $\{1, 2\}$, og $Pr [X = 1] = 0.5$ og $Pr [X = 2] = 0.5$. Vi ville typisk vise en slik tilfeldig variabel i form av et søylediagram som i *Figur 1*.
*Figur 1: Tilfeldig variabel X*

![Figur 1: Tilfeldig variabel X.](assets/Figure2-1.webp)

De brede søylene i *Figur 1* betyr ikke å antyde at den tilfeldige variabelen $X$ faktisk er kontinuerlig. I stedet er søylene gjort brede for å være mer visuelt tiltalende (bare en linje rett opp gir en mindre intuitiv visualisering).

### Uniforme variabler

I uttrykket “tilfeldig variabel”, betyr termen “tilfeldig” bare “probabilistisk”. Med andre ord, det betyr bare at to eller flere mulige utfall av variabelen forekommer med visse sannsynligheter. Disse utfallene trenger imidlertid *ikke nødvendigvis* å være like sannsynlige (selv om termen “tilfeldig” faktisk kan ha den betydningen i andre sammenhenger).

En **uniform variabel** er et spesialtilfelle av en tilfeldig variabel. Den kan ta på seg to eller flere verdier alle med lik sannsynlighet. Den tilfeldige variabelen $X$ avbildet i *Figur 1* er tydeligvis en uniform variabel, ettersom begge mulige utfall forekommer med en sannsynlighet på $0.5$. Det finnes imidlertid mange tilfeldige variabler som ikke er eksempler på uniforme variabler.

Vurder for eksempel den tilfeldige variabelen $Y$. Den har et utfallssett $\{1, 2, 3, 8, 10\}$ og følgende sannsynlighetsfordeling:

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

Selv om to mulige utfall faktisk har en lik sannsynlighet for å inntreffe, nemlig $1$ og $8$, kan $Y$ også ta på seg visse verdier med forskjellige sannsynligheter enn $0.25$ ved sampling. Derfor, mens $Y$ faktisk er en tilfeldig variabel, er den ikke en uniform variabel.

En grafisk fremstilling av $Y$ er gitt i *Figur 2*.

*Figur 2: Tilfeldig variabel Y*

![Figur 2: Tilfeldig variabel Y.](assets/Figure2-2.webp "Figur 2: Tilfeldig variabel Y")

Som et siste eksempel, vurder den tilfeldige variabelen Z. Den har utfallssettet {1,3,7,11,12} og følgende sannsynlighetsfordeling:

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

Du kan se den avbildet i *Figur 3*. Den tilfeldige variabelen Z er, i motsetning til Y, en uniform variabel, ettersom alle sannsynlighetene for de mulige verdiene ved sampling er like.

*Figur 3: Tilfeldig variabel Z*
![Figur 3: Tilfeldig variabel Z.](assets/Figure2-3.webp "Figur 3: Tilfeldig variabel Z")

### Betinget sannsynlighet

Anta at Bob har til hensikt å uniformt velge en dag fra det siste kalenderåret. Hva bør vi konkludere med er sannsynligheten for at den valgte dagen er om sommeren?

Så lenge vi tror at Bobs prosess faktisk vil være helt uniform, bør vi konkludere med at det er 1/4 sannsynlighet for at Bob velger en dag om sommeren. Dette er **ubetinget sannsynlighet** for at den tilfeldig valgte dagen er om sommeren.

Anta nå at i stedet for å uniformt trekke en kalenderdag, velger Bob kun uniformt blant de dagene der middagstemperaturen ved Crystal Lake (New Jersey) var 21 grader Celsius eller høyere. Gitt denne tilleggsinformasjonen, hva kan vi konkludere om sannsynligheten for at Bob vil velge en dag om sommeren?

Vi bør virkelig trekke en annen konklusjon enn før, selv uten ytterligere spesifikk informasjon (f.eks., temperaturen ved middagstid hver dag siste kalenderår).

Ved å vite at Crystal Lake er i New Jersey, ville vi absolutt ikke forvente at temperaturen ved middagstid er 21 grader Celsius eller høyere om vinteren. I stedet er det mye mer sannsynlig at det er en varm dag om våren eller høsten, eller en dag et sted om sommeren. Derfor, ved å vite at middagstemperaturen ved Crystal Lake på den valgte dagen var 21 grader Celsius eller høyere, blir sannsynligheten for at dagen valgt av Bob er om sommeren mye høyere. Dette er **betinget sannsynlighet** for at den tilfeldig valgte dagen er om sommeren, gitt at middagstemperaturen ved Crystal Lake var 21 grader Celsius eller høyere.

I motsetning til i det forrige eksemplet, kan sannsynlighetene for to hendelser også være helt urelaterte. I så fall sier vi at de er **uavhengige**.

Anta, for eksempel, at en viss rettferdig mynt har landet på hode. Gitt dette faktum, hva er da sannsynligheten for at det vil regne i morgen? Den betingede sannsynligheten i dette tilfellet bør være den samme som den ubetingede sannsynligheten for at det vil regne i morgen, ettersom et myntkast generelt ikke har noen innvirkning på været.

Vi bruker et "|" symbol for å skrive ut betingede sannsynlighetsutsagn. For eksempel kan sannsynligheten for hendelse $A$ gitt at hendelse $B$ har skjedd skrives som følger:

$$
Pr[A|B]
$$

Så, når to hendelser, $A$ og $B$, er uavhengige, da:

$$
Pr[A|B] = Pr[A] \text{ og } Pr[B|A] = Pr[B]
$$

Betingelsen for uavhengighet kan forenkles som følger:

$$
Pr[A, B] = Pr[A] \cdot Pr[B]
$$

Et nøkkelresultat i sannsynlighetsteori er kjent som **Bayes' teorem**. Det sier i hovedsak at $Pr[A|B]$ kan skrives om som følger:

$$
Pr[A|B] = \frac{Pr[B|A] \cdot Pr[A]}{Pr[B]}
$$

I stedet for å bruke betingede sannsynligheter med spesifikke hendelser, kan vi også se på de betingede sannsynlighetene som er involvert med to eller flere tilfeldige variabler over et sett med mulige hendelser. Anta to tilfeldige variabler, $X$ og $Y$. Vi kan betegne enhver mulig verdi for $X$ med $x$, og enhver mulig verdi for $Y$ med $y$. Vi kan da si at to tilfeldige variabler er uavhengige hvis følgende utsagn holder:

$$
Pr[X = x, Y = y] = Pr[X = x] \cdot Pr[Y = y]
$$

for alle $x$ og $y$.

La oss være litt mer eksplisitte om hva dette utsagnet betyr.
Anta at utfallssettene for $X$ og $Y$ er definert som følger: **X** = $\{x_1, x_2, \ldots, x_i, \ldots, x_n\}$ og **Y** = $\{y_1, y_2, \ldots, y_i, \ldots, y_m\}$. (Det er vanlig å indikere sett med verdier med fet skrift og store bokstaver.)
Nå anta at du tar et utvalg fra $Y$ og observerer $y_1$. Uttalelsen ovenfor forteller oss at sannsynligheten for nå å oppnå $x_1$ fra utvalget av $X$ er nøyaktig den samme som om vi aldri hadde observert $y_1$. Dette gjelder for hvilken som helst $y_i$ vi kunne ha trukket fra vårt første utvalg av $Y$. Til slutt, dette holder ikke bare for $x_1$. For enhver $x_i$, er sannsynligheten for å forekomme ikke påvirket av utfallet av et utvalg av $Y$. Alt dette gjelder også i tilfellet hvor $X$ er utvalgt først.

La oss avslutte vår diskusjon med et litt mer filosofisk poeng. I enhver virkelig situasjon, vurderes sannsynligheten for en hendelse alltid mot et bestemt sett med informasjon. Det finnes ingen "ubetinget sannsynlighet" i noen veldig streng forstand av ordet.

For eksempel, anta at jeg spurte deg om sannsynligheten for at griser vil fly innen 2030. Selv om jeg ikke gir deg ytterligere informasjon, vet du tydelig mye om verden som kan påvirke din dom. Du har aldri sett griser fly. Du vet at de fleste ikke vil forvente at de skal fly. Du vet at de egentlig ikke er bygget for å fly. Og så videre.

Derfor, når vi snakker om en "ubetinget sannsynlighet" for en hendelse i en virkelig kontekst, kan det uttrykket egentlig bare ha mening hvis vi tar det til å bety noe som "sannsynligheten uten noen ytterligere eksplisitt informasjon". Enhver forståelse av en "betinget sannsynlighet" bør da alltid forstås mot et spesifikt stykke informasjon.

Jeg kan for eksempel spørre deg om sannsynligheten for at griser vil fly innen 2030, etter å ha gitt deg bevis for at noen geiter i New Zealand har lært å fly etter noen års trening. I dette tilfellet vil du sannsynligvis justere din dom over sannsynligheten for at griser vil fly innen 2030. Så sannsynligheten for at griser vil fly innen 2030 er betinget av dette beviset om geiter i New Zealand.

## Modulo-operasjonen
<chapterId>709b34e5-b155-53d2-abbd-97d67e56db00</chapterId>

### Modulo

Det mest grunnleggende uttrykket med **modulo-operasjonen** er av følgende form: $x \mod y$.

Variabelen $x$ kalles dividenden og variabelen $y$ divisoren. For å utføre en modulo-operasjon med en positiv dividende og en positiv divisor, bestemmer du bare resten av divisjonen.

For eksempel, vurder uttrykket $25 \mod 4$. Tallet 4 går inn i tallet 25 totalt 6 ganger. Resten av den divisjonen er 1. Derfor er $25 \mod 4$ lik 1. På lignende måte kan vi evaluere uttrykkene nedenfor:

* $29 \mod 30 = 29$ (ettersom 30 går inn i 29 totalt 0 ganger og resten er 29)
* $42 \mod 2 = 0$ (ettersom 2 går inn i 42 totalt 21 ganger og resten er 0)
* $12 \mod 5 = 2$ (ettersom 5 går inn i 12 totalt 2 ganger og resten er 2)
* $20 \mod 8 = 4$ (ettersom 8 går inn i 20 totalt 2 ganger og resten er 4)

Når dividenden eller divisoren er negativ, kan modulo-operasjoner håndteres forskjellig av programmeringsspråk.

Du vil definitivt støte på tilfeller med en negativ dividende i kryptografi. I disse tilfellene er den typiske tilnærmingen som følger:

* Først bestem den nærmeste verdien *lavere enn eller lik* dividenden som divisoren deler med en rest på null. Kall den verdien $p$.
* Hvis dividenden er $x$, så er resultatet av modulo-operasjonen verdien av $x – p$.

For eksempel, anta at dividenden er $–20$ og divisoren 3. Den nærmeste verdien lavere enn eller lik $–20$ som 3 deler jevnt inn i, er $–21$. Verdien av $x – p$ i dette tilfellet er $–20 – (–21)$. Dette blir 1 og, derfor, $–20 \mod 3$ blir 1. På lignende måte kan vi evaluere uttrykkene nedenfor:

* $–8 \mod 5 = 2$
* $–19 \mod 16 = 13$
* $–14 \mod 6 = 4$

Når det gjelder notasjon, vil du typisk se følgende typer uttrykk: $x = [y \mod z]$. På grunn av klammene, gjelder modulo-operasjonen i dette tilfellet bare for høyre side av uttrykket. Hvis $y$ er lik 25 og $z$ er lik 4, for eksempel, da evalueres $x$ til 1.

Uten klammer, virker modulo-operasjonen på *begge sider* av et uttrykk. Anta, for eksempel, følgende uttrykk: $x = y \mod z$. Hvis $y$ er lik 25 og $z$ er lik 4, da vet vi bare at $x \mod 4$ evalueres til 1. Dette er konsistent med enhver verdi for $x$ fra settet $\{\ldots,–7, –3, 1, 5, 9,\ldots\}$.

Grenen av matematikk som involverer modulo-operasjoner på tall og uttrykk, refereres til som **modulær aritmetikk**. Du kan tenke på denne grenen som aritmetikk for tilfeller der tallinjen ikke er uendelig lang. Selv om vi typisk kommer over modulo-operasjoner for (positive) heltall innen kryptografi, kan du også utføre modulo-operasjoner ved hjelp av hvilke som helst reelle tall.

### Skiftchifferet

Modulo-operasjonen møtes ofte innen kryptografi. For å illustrere, la oss vurdere et av de mest berømte historiske krypteringsskjemaene: skiftchifferet.

La oss først definere det. Anta en ordbok *D* som likestiller alle bokstavene i det engelske alfabetet, i rekkefølge, med settet av tall $\{0, 1, 2, \ldots, 25\}$. Anta et meldingsrom **M**. **Skiftchifferet** er da et krypteringsskjema definert som følger:

- Velg uniformt en nøkkel $k$ ut av nøkkelrommet **K**, hvor **K** = $\{0, 1, 2, \ldots, 25\}$ [1]
- Krypter en melding $m \in \mathbf{M}$, som følger:
    - Separer $m$ inn i sine individuelle bokstaver $m_0, m_1, \ldots, m_i, \ldots, m_l$
- Konverter hver $m_i$ til et tall i henhold til *D*
    - For hver $m_i$, $c_i = [(m_i + k) \mod 26]$
    - Konverter hver $c_i$ til en bokstav i henhold til *D*
    - Kombiner deretter $c_0, c_1, \ldots, c_l$ for å få kryptoteksten $c$
- Dekrypter en kryptotekst $c$ som følger:
    - Konverter hver $c_i$ til et tall i henhold til *D*
    - For hver $c_i$, $m_i = [(c_i – k) \mod 26]$
    - Konverter hver $m_i$ til en bokstav i henhold til *D*
    - Kombiner deretter $m_0, m_1, \ldots, m_l$ for å få den opprinnelige meldingen $m$

Modulo-operatoren i skiftkrypteringen sikrer at bokstavene går rundt, slik at alle kryptotekstbokstaver er definert. For å illustrere, vurder anvendelsen av skiftkryptering på ordet “HUND”.

Anta at du uniformt valgte en nøkkel til å ha verdien 17. Bokstaven “U” tilsvarer 21. Uten modulo-operasjonen, ville tillegg av dette klarteksttallet med nøkkelen beløpe seg til et kryptoteksttall på 38. Imidlertid kan ikke dette kryptoteksttallet bli gjort om til en kryptotekstbokstav, ettersom det engelske alfabetet bare har 26 bokstaver. Modulo-operasjonen sikrer at kryptoteksttallet faktisk er 12 (resultatet av $38 \mod 26$), som tilsvarer kryptotekstbokstaven “M”.

Hele krypteringen av ordet “HUND” med en nøkkelverdi på 17 er som følger:

* Melding = HUND = H,U,N,D = 8,21,14,4
* $c_0 = [(8 + 17) \mod 26] = [(25) \mod 26] = 25 = Y$
* $c_1 = [(21 + 17) \mod 26] = [(38) \mod 26] = 12 = M$
* $c_2 = [(14 + 17) \mod 26] = [(31) \mod 26] = 5 = F$
* $c_3 = [(4 + 17) \mod 26] = [(21) \mod 26] = 21 = V$
* $c = YMFV$

Alle kan intuitivt forstå hvordan skiftkryptering fungerer og sannsynligvis bruke det selv. For å avansere din kunnskap om kryptografi, er det imidlertid viktig å begynne å bli mer komfortabel med formalisering, ettersom ordningene vil bli mye mer kompliserte. Derfor ble trinnene for skiftkryptering formalisert.

**Notater:**

[1] Vi kan definere denne uttalelsen nøyaktig, ved å bruke terminologien fra forrige avsnitt. La en uniform variabel $K$ ha $K$ som sitt sett med mulige utfall. Så:

$$
Pr[K = 0] = \frac{1}{26}
$$

$$
Pr[K = 1] = \frac{1}{26}
$$

...og så videre. Prøv den uniforme variabelen $K$ én gang for å gi en spesiell nøkkel.

## XOR-operasjonen
<chapterId>22f185cc-c516-5b33-950b-0908f2f881fe</chapterId>

All datamaskindata behandles, lagres og sendes over nettverk på bitnivå. Eventuelle kryptografiske ordninger som anvendes på datamaskindata opererer også på bitnivå.

For eksempel, anta at du har skrevet en e-post i e-postapplikasjonen din. Enhver kryptering du anvender skjer ikke direkte på ASCII-tegnene i e-posten din. I stedet anvendes den på bitrepresentasjonen av bokstavene og andre symboler i e-posten din.
En nøkkelmatematisk operasjon å forstå for moderne kryptografi, i tillegg til modulo-operasjonen, er **XOR-operasjonen**, eller "eksklusiv eller"-operasjonen. Denne operasjonen tar to biter som inndata og gir en annen bit som utdata. XOR-operasjonen vil rett og slett bli betegnet som "XOR". Den gir 0 hvis de to bitene er like og 1 hvis de to bitene er forskjellige. Du kan se de fire mulighetene nedenfor. Symbolet $\oplus$ representerer "XOR":
* $0 \oplus 0 = 0$
* $0 \oplus 1 = 1$
* $1 \oplus 0 = 1$
* $1 \oplus 1 = 0$

For å illustrere, anta at du har en melding $m_1$ (01111001) og en melding $m_2$ (01011001). XOR-operasjonen av disse to meldingene kan ses nedenfor.

* $m_1 \oplus m_2 = 01111001 \oplus 01011001 = 00100000$

Prosessen er grei. Du først XOR den ytterste biten til venstre av $m_1$ og $m_2$. I dette tilfellet er det $0 \oplus 0 = 0$. Deretter XOR du det andre paret av biter fra venstre. I dette tilfellet er det $1 \oplus 1 = 0$. Du fortsetter denne prosessen til du har utført XOR-operasjonen på den ytterste biten til høyre.

Det er lett å se at XOR-operasjonen er kommutativ, nemlig at $m_1 \oplus m_2 = m_2 \oplus m_1$. I tillegg er også XOR-operasjonen assosiativ. Det vil si, $(m_1 \oplus m_2) \oplus m_3 = m_1 \oplus (m_2 \oplus m_3)$.

En XOR-operasjon på to strenger av alternative lengder kan ha forskjellige tolkninger, avhengig av konteksten. Vi vil ikke bekymre oss her for noen XOR-operasjoner på strenger av forskjellige lengder.

En XOR-operasjon er ekvivalent med det spesielle tilfellet av å utføre en modulo-operasjon på tillegget av biter når divisoren er 2. Du kan se ekvivalensen i følgende resultater:

* $(0 + 0) \mod 2 = 0 \oplus 0 = 0$
* $(1 + 0) \mod 2 = 1 \oplus 0 = 1$
* $(0 + 1) \mod 2 = 0 \oplus 1 = 1$
* $(1 + 1) \mod 2 = 1 \oplus 1 = 0$

## Pseudotilfeldighet
<chapterId>20463fc5-3e92-581f-a1b7-3151279bd95e</chapterId>

I vår diskusjon om tilfeldige og uniforme variabler, trakk vi en spesifikk distinksjon mellom "tilfeldig" og "uniform". Denne distinksjonen opprettholdes typisk i praksis når man beskriver tilfeldige variabler. Imidlertid, i vår nåværende kontekst, må denne distinksjonen droppes og "tilfeldig" og "uniform" brukes synonymt. Jeg vil forklare hvorfor mot slutten av seksjonen.

For å starte, kan vi kalle en binær streng av lengde $n$ **tilfeldig** (eller **uniform**), hvis den var resultatet av å sample en uniform variabel $S$ som gir hver binær streng av slik lengde $n$ en lik sannsynlighet for valg.
Anta, for eksempel, settet av alle binærstrenger med lengde 8: $\{0000\ 0000, 0000\ 0001, \ldots, 1111\ 1111\}$. (Det er vanlig å skrive en 8-bits streng i to kvartetter, hver kalt en **nibble**.) La oss kalle dette settet av strenger **$S_8$**.
I henhold til definisjonen ovenfor, kan vi da kalle en bestemt binærstreng med lengde 8 tilfeldig (eller uniform), hvis den var resultatet av å sample en uniform variabel $S$ som gir hver streng i **$S_8$** en lik sannsynlighet for utvalg. Gitt at settet **$S_8$** inkluderer $2^8$ elementer, måtte sannsynligheten for utvalg ved sampling være $1/2^8$ for hver streng i settet.

En nøkkelaspekt ved tilfeldigheten til en binærstreng er at den er definert med henvisning til prosessen ved hvilken den ble valgt. Formen på en bestemt binærstreng alene avslører derfor ingenting om dens tilfeldighet i utvalget.

For eksempel har mange mennesker intuitivt ideen om at en streng som $1111\ 1111$ ikke kunne ha blitt valgt tilfeldig. Men dette er klart feil.

Ved å definere en uniform variabel $S$ over alle binærstrengene med lengde 8, er sannsynligheten for å velge $1111\ 1111$ fra settet **$S_8$** den samme som for en streng som $0111\ 0100$. Dermed kan du ikke fortelle noe om tilfeldigheten til en streng, bare ved å analysere strengen selv.

Vi kan også snakke om tilfeldige strenger uten å spesifikt mene binærstrenger. Vi kan for eksempel snakke om en tilfeldig hex-streng $AF\ 02\ 82$. I dette tilfellet ville strengen ha blitt valgt tilfeldig fra settet av alle hex-strenger med lengde 6. Dette tilsvarer å tilfeldig velge en binærstreng med lengde 24, ettersom hver hex-siffer representerer 4 bits.

Vanligvis refererer uttrykket “en tilfeldig streng”, uten kvalifikasjon, til en streng tilfeldig valgt fra settet av alle strenger med samme lengde. Dette er hvordan jeg har beskrevet det ovenfor. En streng med lengde $n$ kan, selvfølgelig, også bli tilfeldig valgt fra et annet sett. Et, for eksempel, som kun utgjør et subsett av alle strengene med lengde $n$, eller kanskje et sett som inkluderer strenger med varierende lengde. I disse tilfellene, ville vi imidlertid ikke referere til den som en “tilfeldig streng”, men heller “en streng som er tilfeldig valgt fra et sett **S**”.

Et nøkkelkonsept innen kryptografi er det av pseudotilfeldighet. En **pseudotilfeldig streng** med lengde $n$ ser ut *som om* den var resultatet av å sample en uniform variabel $S$ som gir hver streng i **$S_n$** en lik sannsynlighet for utvalg. Faktisk er strengen imidlertid resultatet av å sample en uniform variabel $S'$ som kun definerer en sannsynlighetsfordeling—ikke nødvendigvis en med like sannsynligheter for alle mulige utfall—på et subsett av **$S_n$**. Det avgjørende punktet her er at ingen egentlig kan skille mellom prøver fra $S$ og $S'$, selv om du tar mange av dem.
Anta, for eksempel, en tilfeldig variabel $S$. Utfallssettet er **$S_{256}$**, dette er settet med alle binærstrenger med lengde 256. Dette settet har $2^{256}$ elementer. Hvert element har en lik sannsynlighet for utvalg, $1/2^{256}$, ved prøvetaking.
I tillegg, anta en tilfeldig variabel $S'$. Utfallssettet inkluderer kun $2^{128}$ binærstrenger med lengde 256. Den har en viss sannsynlighetsfordeling over disse strengene, men denne fordelingen er ikke nødvendigvis uniform.

Anta at jeg nå tok tusenvis av prøver fra $S$ og tusenvis av prøver fra $S'$ og ga de to settene med utfall til deg. Jeg forteller deg hvilket sett med utfall som er assosiert med hvilken tilfeldig variabel. Deretter tar jeg en prøve fra en av de to tilfeldige variablene. Men denne gangen forteller jeg deg ikke hvilken tilfeldig variabel jeg tar prøven fra. Hvis $S'$ var pseudotilfeldig, så er ideen at din sannsynlighet for å gjøre det riktige gjettet om hvilken tilfeldig variabel jeg prøvetok fra, er praktisk talt ikke bedre enn $1/2$.

Vanligvis produseres en pseudotilfeldig streng med lengde $n$ ved å tilfeldig velge en streng av størrelse $n – x$, hvor $x$ er et positivt heltall, og bruke den som inndata for en ekspansjonsalgoritme. Denne tilfeldige strengen av størrelse $n – x$ er kjent som **frøet**.

Pseudotilfeldige strenger er et nøkkelkonsept for å gjøre kryptografi praktisk. Vurder, for eksempel, strømkrypteringer. Med en strømkryptering blir en tilfeldig valgt nøkkel satt inn i en ekspansjonsalgoritme for å produsere en mye større pseudotilfeldig streng. Denne pseudotilfeldige strengen kombineres deretter med klarteksten via en XOR-operasjon for å produsere en kryptert tekst.

Hvis vi ikke var i stand til å produsere denne typen pseudotilfeldig streng for en strømkryptering, så ville vi trenge en nøkkel som er like lang som meldingen for dens sikkerhet. Dette er ikke en veldig praktisk mulighet i de fleste tilfeller.

Begrepet pseudotilfeldighet diskutert i dette avsnittet kan defineres mer formelt. Det strekker seg også til andre kontekster. Men vi trenger ikke å gå inn i den diskusjonen her. Alt du virkelig trenger å intuitivt forstå for mye av kryptografien er forskjellen mellom en tilfeldig og en pseudotilfeldig streng. [2]

Grunnen til at vi dropper distinksjonen mellom "tilfeldig" og "uniform" i vår diskusjon bør nå også være klar. I praksis bruker alle begrepet pseudotilfeldig for å indikere en streng som ser ut **som om** den var resultatet av prøvetaking av en uniform variabel $S$. Strengt tatt burde vi kalle en slik streng for "pseudo-uniform", ved å adoptere vårt språk fra tidligere. Siden begrepet "pseudo-uniform" er både klumpete og ikke brukt av noen, vil vi ikke introdusere det her for klarhets skyld. I stedet bare dropper vi distinksjonen mellom "tilfeldig" og "uniform" i den nåværende konteksten.

**Notater**

[2] Hvis du er interessert i en mer formell fremstilling av disse sakene, kan du konsultere Katz og Lindells *Introduction to Modern Cryptography*, spesielt kapittel 3.


# Matematiske Grunnlag for Kryptografi 2
<partId>d7245cc9-bb6d-5403-b3d5-9c703d9a2f81</partId>




## Hva er tallteori?
<chapterId>c0051c34-fd5d-539c-93e2-5c6dfd4c3355</chapterId>
Dette kapittelet dekker et mer avansert tema om de matematiske grunnlagene for kryptografi: tallteori. Selv om tallteori er viktig for symmetrisk kryptografi (som i Rijndael Cipher), er det spesielt viktig i sammenheng med offentlig nøkkelkryptografi.
Hvis du finner detaljene i tallteori tungvinte, vil jeg anbefale en overordnet lesning første gangen. Du kan alltid komme tilbake til det senere.

___

Du kan karakterisere **tallteori** som studiet av egenskapene til heltall og matematiske funksjoner som arbeider med heltall.

Tenk for eksempel på at to tall $a$ og $N$ er **relativt primtall** (eller **coprimes**) hvis deres største felles divisor er lik 1. Anta nå et bestemt heltall $N$. Hvor mange heltall mindre enn $N$ er relativt primtall med $N$? Kan vi gi generelle uttalelser om svarene på dette spørsmålet? Dette er de typiske typene spørsmål som tallteori søker å svare på.

Moderne tallteori støtter seg på verktøy fra abstrakt algebra. Feltet **abstrakt algebra** er en underdisiplin av matematikk hvor hovedobjektene for analyse er abstrakte objekter kjent som algebraiske strukturer. En **algebraisk struktur** er et sett med elementer sammenføyd med en eller flere operasjoner, som oppfyller visse aksiomer. Gjennom algebraiske strukturer kan matematikere få innsikt i spesifikke matematiske problemer, ved å abstrahere bort fra deres detaljer.

Feltet abstrakt algebra kalles noen ganger også moderne algebra. Du kan også komme over konseptet **abstrakt matematikk** (eller **ren matematikk**). Dette siste begrepet er ikke en referanse til abstrakt algebra, men betyr heller studiet av matematikk for sin egen skyld, og ikke bare med et øye på potensielle applikasjoner.

Mengdene fra abstrakt algebra kan håndtere mange typer objekter, fra formbevarende transformasjoner på en likesidet trekant til tapetmønstre. For tallteori, vurderer vi kun mengder av elementer som inneholder heltall eller funksjoner som arbeider med heltall.

## Grupper
<chapterId>3209b270-f9cd-5224-803e-0ed19fbf7826</chapterId>

Et grunnleggende konsept i matematikk er det å ha et sett med elementer. Et sett er vanligvis angitt med krøllparenteser med elementene adskilt av komma.

For eksempel er settet av alle heltall $\{…, -2, -1, 0, 1, 2, …\}$. Prikkene her betyr at et visst mønster fortsetter i en bestemt retning. Så settet av alle heltall inkluderer også $3, 4, 5, 6$ og så videre, samt $-3, -4, -5, -6$ og så videre. Dette settet av alle heltall er typisk angitt med $\mathbb{Z}$.

Et annet eksempel på et sett er $\mathbb{Z} \mod 11$, eller settet av alle heltall modulo 11. I motsetning til hele settet $\mathbb{Z}$, inneholder dette settet bare et endelig antall elementer, nemlig $\{0, 1, \ldots, 9, 10\}$.
En vanlig feil er å tenke at mengden $\mathbb{Z} \mod 11$ faktisk er $\{-10, -9, \ldots, 0, \ldots, 9, 10\}$. Men dette er ikke tilfellet, gitt måten vi definerte modulo-operasjonen tidligere. Alle negative heltall redusert med modulo 11 vikles til $\{0, 1, \ldots, 9, 10\}$. For eksempel, uttrykket $-2 \mod 11$ vikles rundt til $9$, mens uttrykket $-27 \mod 11$ vikles rundt til $5$.
Et annet grunnleggende konsept i matematikken er det som kalles en binær operasjon. Dette er enhver operasjon som tar to elementer for å produsere et tredje. For eksempel, fra grunnleggende aritmetikk og algebra, ville du være kjent med fire fundamentale binære operasjoner: addisjon, subtraksjon, multiplikasjon og divisjon.

Disse to grunnleggende matematiske konseptene, mengder og binære operasjoner, brukes til å definere begrepet en gruppe, den mest essensielle strukturen i abstrakt algebra.

Spesifikt, anta en binær operasjon $\circ$. I tillegg, anta en mengde av elementer **S** utstyrt med den operasjonen. Alt "utstyrt" betyr her er at operasjonen $\circ$ kan utføres mellom hvilke som helst to elementer i mengden **S**.

Kombinasjonen $\langle \mathbf{S}, \circ \rangle$ er da en **gruppe** hvis den oppfyller fire spesifikke betingelser, kjent som gruppeaksiomene.

1. For ethvert $a$ og $b$ som er elementer av $\mathbf{S}$, er $a \circ b$ også et element av $\mathbf{S}$. Dette er kjent som **lukkethetsbetingelsen**.
2. For ethvert $a$, $b$ og $c$ som er elementer av $\mathbf{S}$, er det slik at $(a \circ b) \circ c = a \circ (b \circ c)$. Dette er kjent som **assosiativitetsbetingelsen**.
3. Det finnes et unikt element $e$ i $\mathbf{S}$, slik at for hvert element $a$ i $\mathbf{S}$, holder følgende ligning: $e \circ a = a \circ e = a$. Siden det bare er ett slikt element $e$, kalles det **identitetselementet**. Denne betingelsen er kjent som **identitetsbetingelsen**.
4. For hvert element $a$ i $\mathbf{S}$, finnes det et element $b$ i $\mathbf{S}$, slik at følgende ligning holder: $a \circ b = b \circ a = e$, hvor $e$ er identitetselementet. Element $b$ her er kjent som **inverteringselementet**, og det er vanligvis betegnet som $a^{-1}$. Denne betingelsen er kjent som **inverteringsbetingelsen** eller **omvendbarhetsbetingelsen**.

La oss utforske grupper litt videre. Betegn mengden av alle heltall med $\mathbb{Z}$. Denne mengden kombinert med standard addisjon, eller $\langle \mathbb{Z}, + \rangle$, passer tydelig definisjonen av en gruppe, ettersom den oppfyller de fire aksiomene ovenfor.

1. For ethvert $x$ og $y$ som er elementer av $\mathbb{Z}$, er $x + y$ også et element av $\mathbb{Z}$. Så $\langle \mathbb{Z}, + \rangle$ oppfyller lukkethetsbetingelsen.
2. For ethvert $x$, $y$ og $z$ som er elementer av $\mathbb{Z}$, er $(x + y) + z = x + (y + z)$. Så $\langle \mathbb{Z}, + \rangle$ oppfyller assosiativitetsbetingelsen. 3. Det finnes et identitetselement i $\langle \mathbb{Z}, + \rangle$, nemlig 0. For ethvert $x$ i $\mathbb{Z}$, gjelder det nemlig at: $0 + x = x + 0 = x$. Så $\langle \mathbb{Z}, + \rangle$ oppfyller identitetsbetingelsen. 4. Til slutt, for hvert element $x$ i $\mathbb{Z}$, finnes det en $y$ slik at $x + y = y + x = 0$. Hvis $x$ var 10, for eksempel, ville $y$ være $-10$ (i tilfellet at $x$ er 0, er $y$ også 0). Så $\langle \mathbb{Z}, + \rangle$ oppfyller inversbetingelsen.

Det er viktig å merke seg at det at mengden av heltall med addisjon utgjør en gruppe, ikke betyr at den utgjør en gruppe med multiplikasjon. Du kan verifisere dette ved å teste $\langle \mathbb{Z}, \cdot \rangle$ mot de fire gruppeaksiomene (hvor $\cdot$ betyr standard multiplikasjon).

De to første aksiomene holder åpenbart. I tillegg kan elementet 1 tjene som identitetselement under multiplikasjon. Ethvert heltall $x$ multiplisert med 1, gir nemlig $x$. Men, $\langle \mathbb{Z}, \cdot \rangle$ oppfyller ikke inversbetingelsen. Det vil si, det finnes ikke et unikt element $y$ i $\mathbb{Z}$ for hvert $x$ i $\mathbb{Z}$, slik at $x \cdot y = 1$.

For eksempel, anta at $x = 22$. Hvilken verdi $y$ fra mengden $\mathbb{Z}$ multiplisert med $x$ ville gi identitetselementet 1? Verdien av $1/22$ ville fungere, men dette er ikke i mengden $\mathbb{Z}$. Faktisk støter du på dette problemet for ethvert heltall $x$, annet enn verdiene av 1 og -1 (hvor $y$ måtte være 1 og -1 henholdsvis).

Hvis vi tillot reelle tall for vår mengde, så forsvinner våre problemer stort sett. For ethvert element $x$ i mengden, gir multiplikasjon med $1/x$ 1. Ettersom brøker er inkludert i mengden av reelle tall, kan en invers finnes for hvert reelt tall. Unntaket er null, ettersom enhver multiplikasjon med null aldri vil gi identitetselementet 1. Derfor er mengden av ikke-null reelle tall utstyrt med multiplikasjon faktisk en gruppe.

Noen grupper oppfyller en femte generell betingelse, kjent som **kommutativitetsbetingelsen**. Denne betingelsen er som følger:

* Anta en gruppe $G$ med en mengde **S** og en binær operator $\circ$. Anta at $a$ og $b$ er elementer av **S**. Hvis det er tilfellet at $a \circ b = b \circ a$ for ethvert to elementer $a$ og $b$ i **S**, da oppfyller $G$ kommutativitetsbetingelsen.
Enhver gruppe som oppfyller kommutativitetsbetingelsen er kjent som en **kommutativ gruppe**, eller en **Abelsk gruppe** (etter Niels Henrik Abel). Det er enkelt å verifisere at både mengden av reelle tall over addisjon og mengden av heltall over addisjon er Abelske grupper. Mengden av heltall over multiplikasjon er ikke en gruppe i det hele tatt, så ipso facto kan den ikke være en Abelsk gruppe. Mengden av ikke-null reelle tall over multiplikasjon, derimot, er også en Abelsk gruppe.

Du bør merke deg to viktige konvensjoner om notasjon. Først, tegnene “+” eller “×” vil ofte bli brukt for å symbolisere gruppeoperasjoner, selv når elementene ikke faktisk er tall. I disse tilfellene bør du ikke tolke disse tegnene som standard aritmetisk addisjon eller multiplikasjon. I stedet er de operasjoner med kun en abstrakt likhet med disse aritmetiske operasjonene.

Med mindre du spesifikt refererer til aritmetisk addisjon eller multiplikasjon, er det enklere å bruke symboler som $\circ$ og $\diamond$ for gruppeoperasjoner, ettersom disse ikke har veldig kulturelt innarbeidede konnotasjoner.

For det andre, av samme grunn som “+” og “×” ofte brukes for å indikere ikke-aritmetiske operasjoner, blir identitetselementene i grupper ofte symbolisert med “0” og “1”, selv når elementene i disse gruppene ikke er tall. Med mindre du refererer til identitetselementet i en gruppe med tall, er det enklere å bruke et mer nøytralt symbol som “$e$” for å indikere identitetselementet.

Mange forskjellige og svært viktige mengder av verdier i matematikk utstyrt med visse binære operasjoner er grupper. Kryptografiske applikasjoner fungerer imidlertid kun med mengder av heltall eller i det minste elementer som er beskrevet av heltall, det vil si, innenfor tallteoriens domene. Derfor brukes ikke mengder med reelle tall annet enn heltall i kryptografiske applikasjoner.

La oss avslutte med å gi et eksempel på elementer som kan være “beskrevet av heltall”, selv om de ikke er heltall. Et godt eksempel er punktene på elliptiske kurver. Selv om ethvert punkt på en elliptisk kurve tydeligvis ikke er et heltall, er et slikt punkt faktisk beskrevet av to heltall.

Elliptiske kurver er for eksempel avgjørende for Bitcoin. Ethvert standard Bitcoin privat og offentlig nøkkelpar er valgt fra mengden av punkter som er definert av følgende elliptiske kurve:

$$
x^3 + 7 = y^2 \mod 2^{256} – 2^{32} – 29 – 28 – 27 – 26 - 24 - 1
$$

(det største primtallet mindre enn $2^{256}$). $x$-koordinaten er den private nøkkelen og $y$-koordinaten er din offentlige nøkkel.

Transaksjoner i Bitcoin involverer typisk å låse utganger til en eller flere offentlige nøkler på en eller annen måte. Verdien fra disse transaksjonene kan deretter låses opp ved å lage digitale signaturer med de tilsvarende private nøklene.

## Sykliske grupper
<chapterId>bfa5c714-7952-5fef-88b1-ca5b07edd886</chapterId>

En viktig distinksjon vi kan trekke er mellom en **endelig** og en **uendelig gruppe**. Den førstnevnte har et endelig antall elementer, mens den sistnevnte har et uendelig antall elementer. Antallet elementer i enhver endelig gruppe er kjent som **ordenen til gruppen**. All praktisk kryptografi som involverer bruk av grupper, stoler på endelige (tallteoretiske) grupper.

Innen offentlig nøkkelkryptografi er en viss klasse av endelige Abelske grupper kjent som sykliske grupper spesielt viktige. For å forstå sykliske grupper, må vi først forstå konseptet med eksponentiering av gruppeelementer.
Anta at en gruppe $G$ med en gruppeoperasjon $\circ$, og at $a$ er et element i $G$. Uttrykket $a^n$ bør da tolkes som elementet $a$ kombinert med seg selv totalt $n – 1$ ganger. For eksempel betyr $a^2$ at man har $a \circ a$, $a^3$ betyr $a \circ a \circ a$, og så videre. (Merk at eksponentiering her ikke nødvendigvis er eksponentiering i den standard aritmetiske forstand.)

La oss se på et eksempel. Anta at $G = \langle \mathbb{Z} \mod 7, + \rangle$, og at vår verdi for $a$ er lik 4. I dette tilfellet er $a^2 = [4 + 4 \mod 7] = [8 \mod 7] = 1 \mod 7$. Alternativt ville $a^4$ representere $[4 + 4 + 4 + 4 \mod 7] = [16 \mod 7] = 2 \mod 7$.

Noen abelske grupper har ett eller flere elementer, som kan generere alle andre gruppeelementer gjennom kontinuerlig eksponentiering. Disse elementene kalles **generatorer** eller **primitive elementer**.

En viktig klasse av slike grupper er $\langle \mathbb{Z}^* \mod N, \cdot \rangle$, hvor $N$ er et primtall. Notasjonen $\mathbb{Z}^*$ her betyr at gruppen inneholder alle ikke-null, positive heltall mindre enn $N$. En slik gruppe har derfor alltid $N – 1$ elementer.

Vurder for eksempel $G = \langle \mathbb{Z}^* \mod 11, \cdot \rangle$. Denne gruppen har følgende elementer: $\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$. Ordenen til denne gruppen er 10 (som faktisk er lik $11 – 1$).

La oss utforske eksponentieringen av elementet 2 fra denne gruppen. Beregningene frem til $2^{12}$ vises nedenfor. Merk at på venstre side av ligningen refererer eksponenten til gruppeelement eksponentiering. I vårt spesielle eksempel involverer dette faktisk aritmetisk eksponentiering på høyre side av ligningen (men det kunne også ha involvert for eksempel addisjon). For å klargjøre har jeg skrevet ut den gjentatte operasjonen, i stedet for eksponentformen på høyre side.

* $2^1 = 2 \mod 11$
* $2^2 = 2 \cdot 2 \mod 11 = 4 \mod 11$
* $2^3 = 2 \cdot 2 \cdot 2 \mod 11 = 8 \mod 11$
* $2^4 = 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 16 \mod 11 = 5 \mod 11$
* $2^5 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 32 \mod 11 = 10 \mod 11$
* $2^6 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 64 \mod 11 = 9 \mod 11$
* $2^7 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 128 \mod 11 = 7 \mod 11$
* $2^8 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 256 \mod 11 = 3 \mod 11$
* $2^9 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 512 \mod 11 = 6 \mod 11$
* $2^{10} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 1024 \mod 11 = 1 \mod 11$
* $2^{11} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 2048 \mod 11 = 2 \mod 11$
* $2^{12} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 4096 \mod 11 = 4 \mod 11$

Hvis du ser nøye etter, kan du se at utførelsen av eksponentiering på elementet 2 sykler gjennom alle elementene i $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ i følgende rekkefølge: 2, 4, 8, 5, 10, 9, 7, 3, 6, 1. Etter $2^{10}$, fortsetter eksponentiering av elementet 2 å sykle gjennom alle elementene igjen og i samme rekkefølge. Derfor er elementet 2 en generator i $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$.

Selv om $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ har flere generatorer, er ikke alle elementene i denne gruppen generatorer. Vurder for eksempel elementet 3. Å gå gjennom de første 10 eksponentieringene, uten å vise de omstendelige beregningene, gir følgende resultater:

* $3^1 = 3 \mod 11$
* $3^2 = 9 \mod 11$
* $3^3 = 5 \mod 11$
* $3^4 = 4 \mod 11$
* $3^5 = 1 \mod 11$
* $3^6 = 3 \mod 11$
* $3^7 = 9 \mod 11$
* $3^8 = 5 \mod 11$
* $3^9 = 4 \mod 11$
* $3^{10} = 1 \mod 11$
I stedet for å sykle gjennom alle verdiene i $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, fører eksponentiering av elementet 3 kun til et subsett av disse verdiene: 3, 9, 5, 4 og 1. Etter den femte eksponentieringen begynner disse verdiene å gjenta seg.
Vi kan nå definere en **syklisk gruppe** som enhver gruppe med minst én generator. Det vil si, det finnes minst ett gruppeelement som du kan produsere alle andre gruppeelementer gjennom eksponentiering med.

Du kan ha lagt merke til i vårt eksempel ovenfor at både $2^{10}$ og $3^{10}$ er lik $1 \mod 11$. Faktisk, selv om vi ikke vil utføre beregningene, vil eksponentieringen med 10 av ethvert element i gruppen $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ resultere i $1 \mod 11$. Hvorfor er det slik?

Dette er et viktig spørsmål, men det krever litt arbeid for å svare.

For å starte, anta to positive heltall $a$ og $N$. Et viktig teorem i tallteori hevder at $a$ har en multiplikativ invers modulo $N$ (det vil si, et heltall $b$ slik at $a \cdot b = 1 \mod N$) hvis og bare hvis den største felles divisoren mellom $a$ og $N$ er lik 1. Det vil si, hvis $a$ og $N$ er relativt primiske.

Så, for enhver gruppe av heltall utstyrt med multiplikasjon modulo $N$, inkluderes kun de mindre relativt primiske med $N$ i settet. Vi kan betegne dette settet med $\mathbb{Z}^c \mod N$.

For eksempel, anta at $N$ er 10. Kun heltallene 1, 3, 7 og 9 er relativt primiske med 10. Så settet $\mathbb{Z}^c \mod 10$ inkluderer kun $\{1, 3, 7, 9\}$. Du kan ikke skape en gruppe med heltallsmultiplikasjon modulo 10 ved å bruke noen andre heltall mellom 1 og 10. For denne spesifikke gruppen er inversene parene 1 og 9, og 3 og 7.

I tilfellet der $N$ selv er et primtall, er alle heltallene fra 1 til $N – 1$ relativt primiske med $N$. En slik gruppe har derfor en orden på $N – 1$. Ved å bruke vår tidligere notasjon, er $\mathbb{Z}^c \mod N$ lik $\mathbb{Z}^* \mod N$ når $N$ er et primtall. Gruppen vi valgte for vårt tidligere eksempel, $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, er et spesielt tilfelle av denne klassen av grupper.

Videre beregner funksjonen $\phi(N)$ antallet relativt primiske opp til et tall $N$, og er kjent som **Eulers Phi-funksjon**. [1] Ifølge **Eulers teorem**, når to heltall $a$ og $N$ er relativt primiske, gjelder følgende:

* $a^{\phi(N)} \mod N = 1 \mod N$
Dette har en viktig implikasjon for klassen av grupper $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ der $N$ er et primtall. For disse gruppene representerer gruppeelementeksponentiering aritmetisk eksponentiering. Det vil si, $a^{\phi(N)} \mod N$ representerer den aritmetiske operasjonen $a^{\phi(N)} \mod N$. Siden ethvert element $a$ i disse multiplikative gruppene er relativt primt med $N$, betyr det at $a^{\phi(N)} \mod N = a^{N – 1} \mod N = 1 \mod N$.
Eulers teorem er et virkelig viktig resultat. For å starte, innebærer det at alle elementer i $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ kun kan sykle gjennom et antall verdier ved eksponentiering som deler inn i $N – 1$. I tilfellet $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, betyr dette at hvert element kun kan sykle gjennom 2, 5, eller 10 elementer. Gruppeverdiene som ethvert element sykler gjennom ved eksponentiering er kjent som **elementets orden**. Et element med en orden tilsvarende gruppens orden er en generator.

Videre innebærer Eulers teorem at vi alltid kan kjenne resultatet av $a^{N – 1} \mod N$ for enhver gruppe $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ der $N$ er et primtall. Dette er slik uavhengig av hvor kompliserte de faktiske beregningene kan være.

For eksempel, anta at vår gruppe er $\mathbb{Z}^* \mod 160,481,182$ (der 160,481,182 faktisk er et primtall). Vi vet at alle heltall fra 1 til 160,481,181 må være elementer av denne gruppen, og at $\phi(n) = 160,481,181$. Selv om vi ikke kan gjøre alle stegene i beregningene, vet vi at uttrykk som $514^{160,481,181}$, $2,005^{160,481,181}$, og $256,212^{160,481,181}$ alle må evaluere til $1 \mod 160,481,182$.

**Notater:**

[1] Funksjonen fungerer som følger. Ethvert heltall $N$ kan faktoriseres til et produkt av primtall. Anta at et bestemt $N$ er faktorisert som følger: $p_1^{e1} \cdot p_2^{e2} \cdot \ldots \cdot p_m^{em}$ der alle $p$’ene er primtall og alle $e$’ene er heltall større enn eller lik 1. Da:

$$
\phi(N) = \sum_{i=1}^m \left[p_i^{e_i} - p_i^{e_i - 1}\right]
$$

Eulers Phi-funksjonsformel for primtallsfaktoriseringen av $N$.


## Felter
<chapterId>fad52d86-3a22-5c9f-979e-3bec9eaa008e</chapterId>

En gruppe er den grunnleggende algebraiske strukturen i abstrakt algebra, men det finnes mange flere. Den eneste andre algebraiske strukturen du trenger å være kjent med, er den som tilhører et **felt**, spesifikt det til et **endelig felt**. Denne typen algebraisk struktur brukes ofte i kryptografi, som i Advanced Encryption Standard. Sistnevnte er det viktigste symmetriske krypteringsskjemaet du vil møte i praksis.
Et felt er avledet fra begrepet en gruppe. Spesifikt er et **felt** et sett med elementer **S** utstyrt med to binære operatorer $\circ$ og $\diamond$, som oppfyller følgende betingelser:
1. Settet **S** utstyrt med $\circ$ er en Abelsk gruppe.
2. Settet **S** utstyrt med $\diamond$ er en Abelsk gruppe for de "ikke-null" elementene.
3. Settet **S** utstyrt med de to operatorene oppfyller det som er kjent som distribusjonsbetingelsen: Anta at $a$, $b$ og $c$ er elementer i **S**. Da oppfyller **S** utstyrt med de to operatorene distribusjonsegenskapen når $a \circ (b \diamond c) = (a \circ b) \diamond (a \circ c)$.

Merk at, som med grupper, er definisjonen av et felt veldig abstrakt. Den gjør ingen påstander om typene av elementer i **S**, eller om operasjonene $\circ$ og $\diamond$. Den sier bare at et felt er ethvert sett med elementer med to operasjoner for hvilke de tre ovennevnte betingelsene holder. (Det "null" elementet i den andre Abelske gruppen kan tolkes abstrakt.)

Så hva kan være et eksempel på et felt? Et godt eksempel er settet $\mathbb{Z} \mod 7$, eller $\{0, 1, \ldots, 7\}$ definert over standard addisjon (i stedet for $\circ$ ovenfor) og standard multiplikasjon (i stedet for $\diamond$ ovenfor).

Først, $\mathbb{Z} \mod 7$ oppfyller betingelsen for å være en Abelsk gruppe over addisjon, og det oppfyller betingelsen for å være en Abelsk gruppe over multiplikasjon hvis du bare vurderer de ikke-null elementene. For det andre, kombinasjonen av settet med de to operatorene oppfyller distribusjonsbetingelsen.

Det er didaktisk verdifullt å utforske disse påstandene ved å bruke noen spesifikke verdier. La oss ta de eksperimentelle verdiene 5, 2 og 3, noen tilfeldig valgte elementer fra settet $\mathbb{Z} \mod 7$, for å inspisere feltet $\langle \mathbb{Z} \mod 7, +, \cdot \rangle$. Vi vil bruke disse tre verdiene i rekkefølge, etter behov for å utforske spesifikke betingelser.

La oss først utforske om $\mathbb{Z} \mod 7$ utstyrt med addisjon er en Abelsk gruppe.

1. **Lukkethetsbetingelse**: La oss ta 5 og 2 som våre verdier. I så fall blir $[5 + 2] \mod 7 = 7 \mod 7 = 0$. Dette er faktisk et element av $\mathbb{Z} \mod 7$, så resultatet er konsistent med lukkethetsbetingelsen.
2. **Assosiativitetsbetingelse**: La oss ta 5, 2 og 3 som våre verdier. I så fall blir $[(5 + 2) + 3] \mod 7 = [5 + (2 + 3)] \mod 7 = 10 \mod 7 = 3$. Dette er konsistent med assosiativitetsbetingelsen.
3. **Identitetsbetingelse**: La oss ta 5 som vår verdi. I så fall blir $[5 + 0] \mod 7 = [0 + 5] \mod 7 = 5$. Så 0 ser ut til å være identitetselementet for addisjon.
4. **Invers betingelse**: Vurder inversen av 5. Det må være slik at $[5 + d] \mod 7 = 0$, for en eller annen verdi av $d$. I dette tilfellet er den unike verdien fra $\mathbb{Z} \mod 7$ som oppfyller denne betingelsen 2,5. **Kommutativitetsbetingelse**: La oss ta 5 og 3 som våre verdier. I så fall blir $[5 + 3] \mod 7 = [3 + 5] \mod 7 = 1$. Dette er i samsvar med kommutativitetsbetingelsen.

Mengden $\mathbb{Z} \mod 7$ utstyrt med addisjon ser tydelig ut til å være en Abelsk gruppe. La oss nå utforske om $\mathbb{Z} \mod 7$ utstyrt med multiplikasjon er en Abelsk gruppe for alle de ikke-null elementene.

1. **Lukkethetsbetingelse**: La oss ta 5 og 2 som våre verdier. I så fall blir $[5 \cdot 2] \mod 7 = 10 \mod 7 = 3$. Dette er også et element av $\mathbb{Z} \mod 7$, så resultatet er i samsvar med lukkethetsbetingelsen.
2. **Assosiativitetsbetingelse**: La oss ta 5, 2, og 3 som våre verdier. I så fall blir $[(5 \cdot 2) \cdot 3] \mod 7 = [5 \cdot (2 \cdot 3)] \mod 7 = 30 \mod 7 = 2$. Dette er i samsvar med assosiativitetsbetingelsen.
3. **Identitetsbetingelse**: La oss ta 5 som vår verdi. I så fall blir $[5 \cdot 1] \mod 7 = [1 \cdot 5] \mod 7 = 5$. Så 1 ser ut til å være identitetselementet for multiplikasjon.
4. **Invers betingelse**: Vurder inversen av 5. Det må være slik at $[5 \cdot d] \mod 7 = 1$, for en eller annen verdi av $d$. Den unike verdien fra $\mathbb{Z} \mod 7$ som oppfyller denne betingelsen er 3. Dette er i samsvar med invers betingelse.
5. **Kommutativitetsbetingelse**: La oss ta 5 og 3 som våre verdier. I så fall blir $[5 \cdot 3] \mod 7 = [3 \cdot 5] \mod 7 = 15 \mod 7 = 1$. Dette er i samsvar med kommutativitetsbetingelsen.

Mengden $\mathbb{Z} \mod 7$ ser tydelig ut til å oppfylle reglene for å være en Abelsk gruppe når den er sammenføyd med enten addisjon eller multiplikasjon over de ikke-null elementene.

Til slutt ser denne mengden kombinert med begge operatørene ut til å oppfylle distribusjonsbetingelsen. La oss ta 5, 2, og 3 som våre verdier. Vi kan se at $[5 \cdot (2 + 3)] \mod 7 = [5 \cdot 2 + 5 \cdot 3] \mod 7 = 25 \mod 7 = 4$.

Vi har nå sett at $\mathbb{Z} \mod 7$ utstyrt med addisjon og multiplikasjon oppfyller aksiomene for et endelig felt når det testes med bestemte verdier. Selvfølgelig kan vi også vise det generelt, men vil ikke gjøre det her.

En nøkkelforskjell er mellom to typer felt: endelige og uendelige felt.
Et **uendelig felt** involverer et felt hvor mengden **S** er uendelig stor. Mengden av reelle tall $\mathbb{R}$ utstyrt med addisjon og multiplikasjon er et eksempel på et uendelig felt. Et **endelig felt**, også kjent som et **Galois-felt**, er et felt hvor mengden **S** er endelig. Vårt eksempel ovenfor med $\langle \mathbb{Z} \mod 7, +, \cdot \rangle$ er et endelig felt.
I kryptografi er vi primært interessert i endelige felt. Generelt kan det vises at et endelig felt eksisterer for en viss mengde elementer **S** hvis og bare hvis det har $p^m$ elementer, hvor $p$ er et primtall og $m$ et positivt heltall større enn eller lik en. Med andre ord, hvis ordenen til en viss mengde **S** er et primtall ($p^m$ hvor $m = 1$) eller en primtallspotens ($p^m$ hvor $m > 1$), da kan du finne to operatorer $\circ$ og $\diamond$ slik at betingelsene for et felt er oppfylt.

Hvis et endelig felt har et primtall antall elementer, da kalles det et **primfelt**. Hvis antallet elementer i det endelige feltet er en primtallspotens, da kalles feltet et **utvidelsesfelt**. I kryptografi er vi interessert i både primfelt og utvidelsesfelt. [2]

De viktigste primfeltene av interesse i kryptografi er de hvor mengden av alle heltall moduleres av et visst primtall, og operatorene er standard addisjon og multiplikasjon. Denne klassen av endelige felt ville inkludere $\mathbb{Z} \mod 2$, $\mathbb{Z} \mod 3$, $\mathbb{Z} \mod 5$, $\mathbb{Z} \mod 7$, $\mathbb{Z} \mod 11$, $\mathbb{Z} \mod 13$, og så videre. For ethvert primfelt $\mathbb{Z} \mod p$, er mengden av heltall i feltet som følger: $\{0, 1, \ldots, p – 2, p – 1\}$.

I kryptografi er vi også interessert i utvidelsesfelt, spesielt ethvert felt med $2^m$ elementer hvor $m > 1$. Slike endelige felt brukes for eksempel i Rijndael Cipher, som danner grunnlaget for Advanced Encryption Standard. Mens primfelt er relativt intuitive, er disse base 2 utvidelsesfeltene sannsynligvis ikke for noen som er ukjent med abstrakt algebra.

For å starte, er det faktisk sant at enhver mengde heltall med $2^m$ elementer kan tildeles to operatorer som ville gjøre deres kombinasjon til et felt (så lenge $m$ er et positivt heltall). Men, bare fordi et felt eksisterer betyr ikke nødvendigvis at det er lett å oppdage eller spesielt praktisk for visse applikasjoner.

Som det viser seg, er spesielt anvendelige utvidelsesfelt av $2^m$ i kryptografi de som er definert over spesielle sett med polynomuttrykk, heller enn noen mengde av heltall.

For eksempel, anta at vi ønsket et utvidelsesfelt med $2^3$ (dvs., 8) elementer i settet. Selv om det kan være mange forskjellige sett som kan brukes for felt av den størrelsen, inkluderer ett slikt sett alle unike polynomer av formen $a_2x^2 + a_1x + a_0$, hvor hver koeffisient $a_i$ er enten 0 eller 1. Dermed inkluderer dette settet **S** følgende elementer:
1. $0$: Tilfellet der $a_2 = 0$, $a_1 = 0$, og $a_0 = 0$.
2. $1$: Tilfellet der $a_2 = 0$, $a_1 = 0$, og $a_0 = 1$.
3. $x$: Tilfellet der $a_2 = 0$, $a_1 = 1$, og $a_0 = 0$.
4. $x + 1$: Tilfellet der $a_2 = 0$, $a_1 = 1$, og $a_0 = 1$.
5. $x^2$: Tilfellet der $a_2 = 1$, $a_1 = 0$, og $a_0 = 0$.
6. $x^2 + 1$: Tilfellet der $a_2 = 1$, $a_1 = 0$, og $a_0 = 1$.
7. $x^2 + x$: Tilfellet der $a_2 = 1$, $a_1 = 1$, og $a_0 = 0$.
8. $x^2 + x + 1$: Tilfellet der $a_2 = 1$, $a_1 = 1$, og $a_0 = 1$.

Så **S** ville være mengden $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$. Hvilke to operasjoner kan defineres over denne mengden av elementer for å sikre at deres kombinasjon er et felt?

Den første operasjonen på mengden **S** ($\circ$) kan defineres som standard polynomaddisjon modulo 2. Alt du trenger å gjøre er å legge til polynomene som du normalt ville gjort, og deretter anvende modulo 2 på hver av koeffisientene til det resulterende polynomet. Her er noen eksempler:

* $[(x^2) + (x^2 + x + 1)] \mod 2 = [2x^2 + x + 1] \mod 2 = x + 1$
* $[(x^2 + x) + (x)] \mod 2 = [x^2 + 2x] \mod 2 = x^2$
* $[(x + 1) + (x^2 + x + 1)] \mod 2 = [x^2 + 2x + 2] \mod 2 = x^2 + 1$

Den andre operasjonen på mengden **S** ($\diamond$) som er nødvendig for å skape feltet er mer komplisert. Det er en slags multiplikasjon, men ikke standard multiplikasjon fra aritmetikk. I stedet må du se hvert element som en vektor og forstå operasjonen som multiplikasjonen av disse to vektorene modulo et irreduktibelt polynom.

La oss først se på ideen om et irreduktibelt polynom. Et **irreduktibelt polynom** er et som ikke kan faktoriseres (akkurat som et primtall ikke kan faktoriseres i komponenter annet enn 1 og primtallet selv). For vårt formål er vi interessert i polynomer som er irreduktible med hensyn til mengden av alle heltall. (Merk at du kan være i stand til å faktorisere visse polynomer ved for eksempel de reelle eller komplekse tallene, selv om du ikke kan faktorisere dem ved bruk av heltall.)
For eksempel, vurder polynomet $x^2 - 3x + 2$. Dette kan skrives om som $(x – 1)(x – 2)$. Derfor er dette ikke udelelig. Nå vurder polynomet $x^2 + 1$. Ved kun å bruke heltall, er det ingen måte å videre faktorisere dette uttrykket på. Derfor er dette et udelelig polynom med hensyn til heltallene.
Videre, la oss se på konseptet med vektor multiplikasjon. Vi vil ikke utforske dette emnet i dybden, men du trenger bare å forstå en grunnleggende regel: Enhver vektor divisjon kan finne sted så lenge dividenden har en grad høyere enn eller lik graden til divisoren. Hvis dividenden har en lavere grad enn divisoren, kan dividenden ikke lenger deles med divisoren.

For eksempel, vurder uttrykket $x^6 + x + 1 \mod x^5 + x^2$. Dette reduseres ytterligere ettersom graden av dividenden, 6, er høyere enn graden av divisoren, 5. Nå vurder uttrykket $x^5 + x + 1 \mod x^5 + x^2$. Dette reduseres også ytterligere, ettersom graden av dividenden, 5, og divisoren, 5, er like.

Men, nå vurder uttrykket $x^4 + x + 1 \mod x^5 + x^2$. Dette reduseres ikke ytterligere, ettersom graden av dividenden, 4, er lavere enn graden av divisoren, 5.

På grunnlag av denne informasjonen, er vi nå klare til å finne vår andre operasjon for settet $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$.

Jeg har allerede sagt at den andre operasjonen bør forstås som vektor multiplikasjon modulo et udelelig polynom. Dette udelelige polynomet bør sikre at den andre operasjonen definerer en abelsk gruppe over **S** og er konsistent med den distributive betingelsen. Så hva bør det udelelige polynomet være?

Siden alle vektorer i settet er av grad 2 eller lavere, bør det udelelige polynomet være av grad 3. Hvis noen multiplikasjon av to vektorer i settet gir et polynom av grad 3 eller høyere, vet vi at modulo et polynom av grad 3 alltid gir et polynom av grad 2 eller lavere. Dette er tilfellet fordi ethvert polynom av grad 3 eller høyere alltid er delelig med et polynom av grad 3. I tillegg må polynomet som fungerer som divisoren være udelelig.

Det viser seg at det er flere udelelige polynomer av grad 3 som vi kunne bruke som vår divisor. Hvert av disse polynomene definerer et forskjellig felt i forbindelse med vårt sett **S** og addisjon modulo 2. Dette betyr at du har flere alternativer når du bruker utvidelsesfelt $2^m$ i kryptografi.

For vårt eksempel, anta at vi velger polynomet $x^3 + x + 1$. Dette er faktisk udelelig, fordi du ikke kan faktorisere det ved å bruke heltall. I tillegg vil det sikre at enhver multiplikasjon av to elementer vil gi et polynom av grad 2 eller mindre.
La oss jobbe gjennom et eksempel på den andre operasjonen ved å bruke polynomet $x^3 + x + 1$ som divisor for å illustrere hvordan det fungerer. Anta at du multipliserer elementene $x^2 + 1$ med $x^2 + x$ i vårt sett **S**. Vi må da beregne uttrykket $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1$. Dette kan forenkles som følger:
* $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1 =$
* $[x^2 \cdot x^2 + x^2 \cdot x + 1 \cdot x^2 + 1 \cdot x] \mod x^3 + x + 1 =$
* $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$

Vi vet at $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$ kan reduseres ettersom dividenden har en høyere grad (4) enn divisoren (3).

For å starte, kan du se at uttrykket $x^3 + x + 1$ går inn i $x^4 + x^3 + x^2 + x$ totalt $x$ ganger. Du kan verifisere dette ved å multiplisere $x^3 + x + 1$ med $x$, som er $x^4 + x^2 + x$. Ettersom det siste leddet er av samme grad som dividenden, nemlig 4, vet vi at dette fungerer. Du kan beregne resten av denne divisjonen ved $x$ som følger:

* $[(x^4 + x^3 + x^2 + x) - (x^4 + x^2 + x)] \mod x^3 + x + 1 =$
* $[x^3] \mod x^3 + x + 1 =$
* $x^3$

Så etter å ha delt $x^4 + x^3 + x^2 + x$ med $x^3 + x + 1$ totalt $x$ ganger, har vi en rest på $x^3$. Kan dette ytterligere deles med $x^3 + x + 1$?

Intuitivt kan det virke tiltalende å si at $x^3$ ikke lenger kan deles med $x^3 + x + 1$, fordi det siste leddet ser større ut. Husk imidlertid vår diskusjon om vektordivisjon tidligere. Så lenge dividenden har en grad som er større eller lik divisoren, kan uttrykket ytterligere reduseres. Spesifikt kan uttrykket $x^3 + x + 1$ gå inn i $x^3$ nøyaktig 1 gang. Resten beregnes som følger:

$$
[(x^3) - (x^3 + x + 1)] \mod x^3 + x + 1 = [x + 1] \mod x^3 + x + 1 = x + 1
$$

Du lurer kanskje på hvorfor $(x^3) - (x^3 + x + 1)$ evalueres til $x + 1$ og ikke $-x - 1$. Husk at den første operasjonen i vårt felt er definert modulo 2. Derfor gir subtraksjonen av to vektorer nøyaktig samme resultat som addisjonen av to vektorer.
For å oppsummere multiplikasjonen av $x^2 + 1$ og $x^2 + x$: Når du multipliserer disse to leddene, får du et polynom av fjerde grad, $x^4 + x^3 + x^2 + x$, som må reduseres modulo $x^3 + x + 1$. Polynomet av fjerde grad er delelig med $x^3 + x + 1$ nøyaktig $x + 1$ ganger. Resten etter å ha delt $x^4 + x^3 + x^2 + x$ med $x^3 + x + 1$ nøyaktig $x + 1$ ganger er $x + 1$. Dette er faktisk et element i vårt sett $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$.
Hvorfor ville utvidede felt med base 2 over sett med polynomer, som i eksemplet ovenfor, være nyttige for kryptografi? Grunnen er at du kan se på koeffisientene i polynomene i slike sett, enten 0 eller 1, som elementer av binærstrenger med en bestemt lengde. Settet **S** i vårt eksempel ovenfor, kunne for eksempel i stedet ses på som et sett **S** som inkluderer alle binærstrenger med lengde 3 (000 til 111). Operasjonene på **S**, kan da også brukes til å utføre operasjoner på disse binærstrengene og produsere en binærstreng av samme lengde.

**Notater:**

[2] Utvidede felt blir veldig motintuitive. I stedet for å ha elementer av heltall, har de sett med polynomer. I tillegg utføres alle operasjoner modulo et visst irreduktibelt polynom.


## Abstrakt algebra i praksis
<chapterId>ed35b98d-18b4-5790-9911-1078e0f84f92</chapterId>

Til tross for det formelle språket og abstraktheten i diskusjonen, bør konseptet med en gruppe ikke være for vanskelig å forstå. Det er bare et sett med elementer sammen med en binær operasjon, hvor utførelsen av den binære operasjonen på disse elementene oppfyller fire generelle betingelser. En abelsk gruppe har bare en ekstra betingelse kjent som kommutativitet. En syklisk gruppe, derimot, er en spesiell type abelsk gruppe, nemlig en som har en generator. Et felt er bare en mer kompleks konstruksjon fra det grunnleggende gruppebegrepet.

Men hvis du er en praktisk orientert person, lurer du kanskje på dette tidspunktet: Hvem bryr seg? Har det å vite at et sett med elementer med en operator er en gruppe, eller til og med en abelsk eller syklisk gruppe, noen relevans i den virkelige verden? Har det å vite at noe er et felt?

Uten å gå for mye i detalj, er svaret "ja". Grupper ble først skapt på 1800-tallet av den franske matematikeren Evariste Galois. Han brukte dem til å trekke konklusjoner om løsning av polynomligninger av en grad høyere enn fem.

Siden den gang har konseptet med en gruppe hjulpet til med å kaste lys over en rekke problemer i matematikk og andre steder. På deres grunnlag, for eksempel, kunne fysikeren Murray-Gellman forutsi eksistensen av en partikkel før den faktisk ble observert i eksperimenter. [3] For et annet eksempel bruker kjemikere gruppeteori for å klassifisere formene på molekyler. Matematikere har til og med brukt konseptet med en gruppe til å trekke konklusjoner om noe så konkret som tapet!
Å vise at et sett med elementer med en viss operator utgjør en gruppe, betyr at det du beskriver har en spesiell symmetri. Ikke en symmetri i ordets vanlige forstand, men i en mer abstrakt form. Og dette kan gi betydelig innsikt i spesifikke systemer og problemer. De mer komplekse begrepene fra abstrakt algebra gir oss bare tilleggsinformasjon.
Viktigst, du vil se betydningen av tallteoretiske grupper og felt i praksis gjennom deres anvendelse i kryptografi, spesielt offentlig nøkkelkryptografi. Vi har allerede sett i vår diskusjon om felt, for eksempel, hvordan utvidelsesfelt brukes i Rijndael Cipher. Vi vil jobbe ut det eksemplet i *Kapittel 5*.

For videre diskusjon om abstrakt algebra, vil jeg anbefale den utmerkede videoserien om abstrakt algebra av Socratica. [4] Jeg vil spesielt anbefale følgende videoer: “What is abstract algebra?”, “Group definition (expanded)”, “Ring definition (expanded)”, og “Field definition (expanded).” Disse fire videoene vil gi deg noe tilleggsinnsikt i mye av diskusjonen ovenfor. (Vi diskuterte ikke ringer, men et felt er bare en spesiell type ring.)

For videre diskusjon om moderne tallteori, kan du konsultere mange avanserte diskusjoner om kryptografi. Jeg vil foreslå Jonathan Katz og Yehuda Lindells Introduction to Modern Cryptography eller Christof Paar og Jan Pelzls Understanding Cryptography for videre diskusjon. [5]

**Notater:**

[3] Se [YouTube Video](https://www.youtube.com/watch?v=NOMUnMuxDZY&feature=youtu.be)

[4] Socratica, [Abstract Algebra](https://www.socratica.com/subject/abstract-algebra)

[5] Katz og Lindell, *Introduction to Modern Cryptography*, 2. utg, 2015 (CRC Press: Boca Raton, FL). Paar og Pelzl, *Understanding Cryptography*, 2010 (Springer-Verlag: Berlin).

# Symmetrisk Kryptografi
<partId>ef768d0e-fe7b-510c-87d6-6febb3de1039</partId>

## Alice og Bob
<chapterId>47345330-be2d-5faf-afd0-d289a8d21bf1</chapterId>

En av de to hovedgrenene av kryptografi er symmetrisk kryptografi. Det inkluderer krypteringsskjemaer så vel som skjemaer som er opptatt av autentisering og integritet. Frem til 1970-tallet, ville all kryptografi ha bestått av symmetriske krypteringsskjemaer.

Hoveddiskusjonen starter med å se på symmetriske krypteringsskjemaer og gjøre det avgjørende skillet mellom strømkryptering og blokkryptering. Deretter går vi over til meldingsautentiseringskoder, som er skjemaer for å sikre meldingsintegritet og autentisitet. Til slutt utforsker vi hvordan symmetriske krypteringsskjemaer og meldingsautentiseringskoder kan kombineres for å sikre sikker kommunikasjon.

Dette kapittelet diskuterer ulike symmetriske kryptografiske skjemaer fra praksis i forbifarten. Det neste kapittelet tilbyr en detaljert fremstilling av kryptering med en strømkryptering og en blokkryptering fra praksis, nemlig RC4 og AES henholdsvis.

Før vi starter vår diskusjon om symmetrisk kryptografi, vil jeg kort gjøre noen bemerkninger om Alice og Bob-illustrasjonene i dette og påfølgende kapitler.

___

I illustrasjonen av prinsippene for kryptografi, stoler folk ofte på eksempler som involverer Alice og Bob. Jeg vil også gjøre det.

Spesielt hvis du er ny til kryptografi, er det viktig å innse at disse eksemplene med Alice og Bob kun er ment å tjene som illustrasjoner av kryptografiske prinsipper og konstruksjoner i et forenklet miljø. Prinsippene og konstruksjonene er imidlertid anvendelige på et mye bredere spekter av virkelige kontekster.
Her er fem nøkkelpunkter å huske på om eksempler som involverer Alice og Bob i kryptografi:
1. De kan enkelt oversettes til eksempler med andre typer aktører som selskaper eller offentlige organisasjoner.
2. De kan enkelt utvides til å inkludere tre eller flere aktører.
3. I eksemplene er Bob og Alice typisk aktive deltakere i å skape hver melding og i anvendelsen av kryptografiske skjemaer på den meldingen. Men i virkeligheten er elektronisk kommunikasjon stort sett automatisert. Når du besøker en nettside som bruker transportlagssikkerhet, for eksempel, håndteres kryptografien typisk helt av datamaskinen din og webserveren.
4. I konteksten av elektronisk kommunikasjon er "meldingene" som sendes over en kommunikasjonskanal vanligvis TCP/IP-pakker. Disse kan tilhøre en e-post, en Facebook-melding, en telefonsamtale, en filoverføring, en nettside, en programvareopplasting, og så videre. De er ikke meldinger i tradisjonell forstand. Likevel vil kryptografer ofte forenkle denne virkeligheten ved å si at meldingen er, for eksempel, en e-post.
5. Eksemplene fokuserer typisk på elektronisk kommunikasjon, men de kan også utvides til tradisjonelle former for kommunikasjon som brev.

## Symmetriske krypteringsskjemaer
<chapterId>41bfdbe1-6d41-5272-98bb-81f24b2fd6af</chapterId>

Vi kan løst definere et **symmetrisk krypteringsskjema** som ethvert kryptografisk skjema med tre algoritmer:

1. En **nøkkelgenereringsalgoritme**, som genererer en privat nøkkel.
2. En **krypteringsalgoritme**, som tar den private nøkkelen og en klartekst som inndata og gir en kryptert tekst som utdata.
3. En **dekrypteringsalgoritme**, som tar den private nøkkelen og den krypterte teksten som inndata og gir den opprinnelige klarteksten som utdata.

Typisk tilbyr et krypteringsskjema—enten det er symmetrisk eller asymmetrisk—en mal for kryptering basert på en kjernealgoritme, snarere enn en eksakt spesifikasjon.

For eksempel, vurder Salsa20, et symmetrisk krypteringsskjema. Det kan brukes med både 128- og 256-bits nøkkellengder. Valget angående nøkkellengde påvirker noen mindre detaljer i algoritmen (antall runder i algoritmen for å være nøyaktig).

Men man ville ikke si at å bruke Salsa20 med en 128-bits nøkkel er et annet krypteringsskjema enn Salsa20 med en 256-bits nøkkel. Kjernealgoritmen forblir den samme. Bare når kjernealgoritmen endres ville vi virkelig snakke om to forskjellige krypteringsskjemaer.

Symmetriske krypteringsskjemaer er typisk nyttige i to typer tilfeller: (1) De der to eller flere agenter kommuniserer over en avstand og ønsker å holde innholdet i kommunikasjonen hemmelig; og (2) de der en agent ønsker å holde innholdet i en melding hemmelig over tid.

Du kan se en fremstilling av situasjon (1) i *Figur 1* nedenfor. Bob ønsker å sende en melding $M$ til Alice over en avstand, men ønsker ikke at andre skal kunne lese den meldingen.

Bob krypterer først meldingen $M$ med den private nøkkelen $K$. Deretter sender han den krypterte teksten $C$ til Alice. Når Alice har mottatt den krypterte teksten, kan hun dekryptere den ved hjelp av nøkkelen $K$ og lese klarteksten. Med et godt krypteringsskjema, bør enhver angriper som avlytter den krypterte teksten $C$ ikke kunne lære noe av reell betydning om meldingen $M$.

Du kan se en fremstilling av situasjon (2) i *Figur 2* nedenfor. Bob ønsker å forhindre andre fra å se visse opplysninger. En typisk situasjon kan være at Bob er en ansatt som lagrer sensitiv data på datamaskinen sin, som verken utenforstående eller hans kolleger skal lese.
Bob krypterer meldingen $M$ på tidspunktet $T_0$ med nøkkelen $K$ for å produsere kryptoteksten $C$. På tidspunktet $T_1$ trenger han meldingen igjen, og dekrypterer kryptoteksten $C$ med nøkkelen $K$. Enhver angriper som måtte ha kommet over kryptoteksten $C$ i mellomtiden, burde ikke ha vært i stand til å utlede noe signifikant om $M$ fra den.

*Figur 1: Hemmelighold over rom*

![Figur 1: Hemmelighold over rom](assets/Figure4-1.webp "Figur 1: Hemmelighold over rom")

*Figur 2: Hemmelighold over tid*

![Figur 2: Hemmelighold over tid](assets/Figure4-2.webp "Figur 2: Hemmelighold over tid")

## Et eksempel: Forskyvningskrypteringen
<chapterId>7b179ae8-8d15-5e80-a43f-22c970d87b5e</chapterId>

I Kapittel 2 støtte vi på forskyvningskrypteringen, som er et eksempel på et veldig enkelt symmetrisk krypteringsskjema. La oss se på det igjen her.

Anta en ordbok *D* som likestiller alle bokstavene i det engelske alfabetet, i rekkefølge, med settet av tall $\{0,1,2,\dots,25\}$. Anta et sett med mulige meldinger **M**. Forskyvningskrypteringen er da et krypteringsskjema definert som følger:

- Velg tilfeldig en nøkkel $k$ ut av settet med mulige nøkler **K**, hvor **K** = $\{0,1,2,\dots,25\}$
- Krypter en melding $m \in$ **M**, som følger:
    - Separer $m$ inn i sine individuelle bokstaver $m_0, m_1,\dots, m_i, \dots, m_l$
    - Konverter hver $m_i$ til et tall i henhold til *D*
    - For hver $m_i$, $c_i = [(m_i + k) \mod 26]$
    - Konverter hver $c_i$ tilbake til en bokstav i henhold til *D*
    - Kombiner deretter $c_0, c_1,\dots, c_l$ for å gi kryptoteksten $c$
- Dekrypter en kryptotekst $c$ som følger:
    - Konverter hver $c_i$ til et tall i henhold til *D*
    - For hver $c_i$, $m_i = [(c_i - k) \mod 26]$
    - Konverter hver $m_i$ tilbake til en bokstav i henhold til *D*
    - Kombiner deretter $m_0, m_1,\dots, m_l$ for å gi den opprinnelige meldingen $m$

Det som gjør forskyvningskrypteringen til et symmetrisk krypteringsskjema, er at samme nøkkel brukes for både krypterings- og dekrypteringsprosessen. For eksempel, anta at du ønsker å kryptere meldingen “DOG” ved bruk av forskyvningskrypteringen, og at du tilfeldig har valgt "24" som nøkkel. Å kryptere meldingen med denne nøkkelen vil gi “BME”. Den eneste måten å hente den opprinnelige meldingen på, er ved å bruke samme nøkkel, "24", for dekrypteringsprosessen.

Denne forskyvningskrypteringen er et eksempel på en **monoalfabetisk substitusjonskryptering**: et krypteringsskjema hvor kryptotekstalfabetet er fast (dvs., kun ett alfabet brukes). Under forutsetning av at dekrypteringsalgoritmen er deterministisk, kan hvert symbol i substitusjonskryptoteksten maksimalt tilsvare ett symbol i klarteksten.
Frem til 1700-tallet var mange anvendelser av kryptering sterkt avhengige av monoalfabetiske substitusjonschiffer, selv om disse ofte var mye mer komplekse enn Shift-chifferet. Du kunne for eksempel tilfeldig velge en bokstav fra alfabetet for hver opprinnelige tekstbokstav under forutsetningen om at hver bokstav kun forekommer én gang i chifferalfabetet. Det betyr at du ville ha faktoriell 26 mulige private nøkler, noe som var enormt i før-datamaskinens tid.
Merk at du vil komme over termen **chiffer** mye i kryptografi. Vær oppmerksom på at dette begrepet har ulike betydninger. Faktisk kjenner jeg til minst fem distinkte betydninger av termen innen kryptografi.

I noen tilfeller refererer det til et krypteringsskjema, som det gjør i Shift-chiffer og monoalfabetisk substitusjonschiffer. Imidlertid kan termen også spesifikt referere til krypteringsalgoritmen, den private nøkkelen, eller bare chiffer-teksten til et slikt krypteringsskjema.

Til slutt kan termen chiffer også referere til en kjernealgoritme som du kan konstruere kryptografiske skjemaer fra. Disse kan inkludere ulike krypteringsalgoritmer, men også andre typer kryptografiske skjemaer. Denne betydningen av termen blir relevant i konteksten av blokkchiffer (se avsnittet "Blokkchiffer" nedenfor).

Du kan også komme over termene å **kryptere** eller å **dekryptere**. Disse termene er bare synonymer for kryptering og dekryptering.

## Brute force-angrep og Kerckhoffs prinsipp
<chapterId>2d73ef97-26c5-5d11-8815-0ddbe89c8003</chapterId>

Shift-chifferet er et veldig usikkert symmetrisk krypteringsskjema, i hvert fall i den moderne verden. [1] En angriper kunne bare forsøke dekryptering av hvilken som helst chiffer-tekst med alle 26 mulige nøkler for å se hvilket resultat som gir mening. Denne typen angrep, hvor angriperen bare sykler gjennom nøkler for å se hva som fungerer, er kjent som et **brute force-angrep** eller **utømmende nøkkelsøk**.

For at et krypteringsskjema skal møte en minimal oppfatning av sikkerhet, må det ha et sett med mulige nøkler, eller **nøkkelrom**, som er så stort at brute force-angrep er uoverkommelige. Alle moderne krypteringsskjemaer møter denne standarden. Dette er kjent som **prinsippet om tilstrekkelig nøkkelrom**. Et lignende prinsipp gjelder typisk i ulike typer kryptografiske skjemaer.

For å få en følelse av den massive nøkkelromsstørrelsen i moderne krypteringsskjemaer, anta at en fil har blitt kryptert med en 128-bits nøkkel ved bruk av den avanserte krypteringsstandarden. Dette betyr at en angriper har et sett med $2^{128}$ nøkler som hun trenger å sykle gjennom for et brute force-angrep. En sjanse på 0,78 % for suksess med denne strategien ville kreve at angriperen sykler gjennom omtrent $2.65 \times 10^{36}$ nøkler.

Anta at vi optimistisk antar at en angriper kan forsøke $10^{16}$ nøkler per sekund (dvs. 10 billioner nøkler per sekund). For å teste 0,78 % av alle nøkler i nøkkelrommet, måtte angrepet hennes vare $2.65 \times 10^{20}$ sekunder. Dette er omtrent 8,4 billioner år. Så selv et brute force-angrep fra en absurd kraftig motstander er ikke realistisk med et moderne 128-bits krypteringsskjema. Dette er prinsippet om tilstrekkelig nøkkelrom i spill.

Er Shift-chifferet sikrere hvis angriperen ikke kjenner til krypteringsalgoritmen? Kanskje, men ikke mye.
I alle tilfeller antar moderne kryptografi alltid at sikkerheten til ethvert symmetrisk krypteringssystem kun avhenger av å holde den private nøkkelen hemmelig. Angriperen antas alltid å kjenne alle de andre detaljene, inkludert meldingsrommet, nøkkelrommet, krypteringstekstområdet, nøkkelvalgalgoritmen, krypteringsalgoritmen og dekrypteringsalgoritmen.
Tanken om at sikkerheten til et symmetrisk krypteringssystem kun kan avhenge av hemmeligholdelsen av den private nøkkelen er kjent som **Kerckhoffs’ prinsipp**.

Som opprinnelig ment av Kerckhoffs, gjelder prinsippet kun for symmetriske krypteringssystemer. En mer generell versjon av prinsippet gjelder imidlertid også for alle andre moderne typer kryptografiske systemer: Et kryptografisk systems design trenger ikke å være hemmelig for at det skal være sikkert; hemmeligholdelsen kan kun utstrekke seg til noen strenger av informasjon, typisk en privat nøkkel.

Kerckhoffs’ prinsipp er sentralt i moderne kryptografi av fire grunner. [2] For det første finnes det bare et begrenset antall kryptografiske systemer for spesielle typer applikasjoner. For eksempel bruker de fleste moderne symmetriske krypteringsapplikasjoner Rijndael-chifferet. Så din hemmeligholdelse angående et systems design er bare veldig begrenset. Det er imidlertid mye mer fleksibilitet i å holde en privat nøkkel for Rijndael-chifferet hemmelig.

For det andre er det lettere å erstatte en streng med informasjon enn et helt kryptografisk system. Anta at de ansatte i et selskap alle har samme krypteringsprogramvare, og at hver to ansatte har en privat nøkkel for å kommunisere konfidensielt. Kompromisser av nøkler er et problem i dette scenarioet, men i det minste kunne selskapet beholde programvaren med slike sikkerhetsbrudd. Hvis selskapet var avhengig av systemets hemmelighet, ville ethvert brudd på den hemmeligheten kreve utskifting av all programvaren.

For det tredje tillater Kerckhoffs’ prinsipp standardisering og kompatibilitet mellom brukere av kryptografiske systemer. Dette har enorme fordeler for effektiviteten. For eksempel er det vanskelig å forestille seg hvordan millioner av mennesker kunne koble seg sikkert til Googles webservere hver dag, hvis den sikkerheten krevde å holde kryptografiske systemer hemmelige.

For det fjerde tillater Kerckhoffs’ prinsipp offentlig granskning av kryptografiske systemer. Denne typen granskning er absolutt nødvendig for å oppnå sikre kryptografiske systemer. Illustrativt var hovedalgoritmen i symmetrisk kryptografi, Rijndael-chifferet, resultatet av en konkurranse organisert av National Institute of Standards and Technology mellom 1997 og 2000.

Ethvert system som forsøker å oppnå **sikkerhet gjennom obskuritet** er et som er avhengig av å holde detaljene i sitt design og/eller implementasjon hemmelig. I kryptografi ville dette spesifikt være et system som er avhengig av å holde design detaljene av det kryptografiske systemet hemmelig. Så sikkerhet gjennom obskuritet er i direkte kontrast til Kerckhoffs’ prinsipp.

Evnen til åpenhet til å styrke kvalitet og sikkerhet strekker seg også bredere til den digitale verden enn bare kryptografi. Fri og åpen kildekode Linux-distribusjoner som Debian, har for eksempel generelt flere fordeler over sine Windows og MacOS-motstykker når det gjelder personvern, stabilitet, sikkerhet og fleksibilitet. Selv om det kan ha flere årsaker, er det mest sannsynlig viktigste prinsippet, som Eric Raymond formulerte det i sitt berømte essay "The Cathedral and the Bazaar," at "gitt nok øyne, er alle feil overfladiske." [3] Det er dette visdommen av folkets type prinsipp som ga Linux sin mest betydningsfulle suksess.
Man kan aldri utvetydig si at et kryptografisk skjema er "sikkert" eller "usikkert". I stedet finnes det ulike sikkerhetsbegreper for kryptografiske skjemaer. Hver **definisjon av kryptografisk sikkerhet** må spesifisere (1) sikkerhetsmål, så vel som (2) angriperens kapasiteter. Analyse av kryptografiske skjemaer mot en eller flere spesifikke sikkerhetsbegreper gir innsikt i deres anvendelser og begrensninger.
Selv om vi ikke vil gå inn på alle detaljene i de ulike sikkerhetsbegrepene for kryptografi, bør du vite at to antakelser er allestedsnærværende for alle moderne kryptografiske sikkerhetsbegreper relatert til symmetriske og asymmetriske skjemaer (og i noen form til andre kryptografiske primitiver):

* Angriperens kunnskap om skjemaet følger Kerckhoffs’ prinsipp.
* Angriperen kan ikke gjennomførbart utføre et brute force-angrep på skjemaet. Spesifikt tillater trusselmodellene for kryptografiske sikkerhetsbegreper typisk ikke engang brute force-angrep, da de antar at disse ikke er en relevant vurdering.

**Notater:**

[1] Ifølge Seutonius, ble et skiftchiffer med en konstant nøkkelverdi på 3 brukt av Julius Caesar i hans militærkommunikasjon. Så A ville alltid bli D, B alltid E, C alltid F, og så videre. Denne spesielle versjonen av skiftchifferet har derfor blitt kjent som **Caesar Cipher** (selv om det egentlig ikke er et chiffer i moderne forstand av ordet, ettersom nøkkelverdien er konstant). Caesar-chifferet kan ha vært sikkert i det første århundre f.Kr., hvis Romas fiender var veldig ukjente med kryptering. Men det ville tydeligvis ikke være et veldig sikkert skjema i moderne tider.

[2] Jonathan Katz og Yehuda Lindell, _Introduction to Modern Cryptography_, CRC Press (Boca Raton, FL: 2015), s. 7f.

[3] Eric Raymond, “The Cathedral and the Bazaar,” papiret ble presentert på Linux Kongress, Würzburg, Tyskland (27. mai 1997). Det finnes en rekke senere versjoner tilgjengelig samt en bok. Mine sitater er fra side 30 i boken: Eric Raymond, _The Cathedral and the Bazaar: Musings on Linux and Open Source by an Accidental Revolutionary_, revidert utg. (2001), O’Reilly: Sebastopol, CA.

## Strømchiffre
<chapterId>479aa6f4-45c4-59ca-8616-8cf8e61fc871</chapterId>

Symmetriske krypteringsskjemaer deles vanligvis inn i to typer: **strømchiffre** og **blokkchiffre**. Denne distinksjonen er imidlertid noe problematisk, ettersom folk bruker disse begrepene på en inkonsekvent måte. I de neste avsnittene vil jeg fastsette distinksjonen på den måten jeg mener er best. Du bør imidlertid være klar over at mange mennesker vil bruke disse begrepene noe annerledes enn det jeg legger frem.

La oss først se på strømchiffre. Et **strømchiffer** er et symmetrisk krypteringsskjema hvor kryptering består av to trinn.

Først produseres en streng med samme lengde som klarteksten via en privat nøkkel. Denne strengen kalles **nøkkelstrømmen**.

Deretter kombineres nøkkelstrømmen matematisk med klarteksten for å produsere en kryptert tekst. Denne kombinasjonen er typisk en XOR-operasjon. For dekryptering kan du bare reversere operasjonen. (Merk at $A \oplus B = B \oplus A$, i tilfellet $A$ og $B$ er bitstrenger. Så rekkefølgen av en XOR-operasjon i et strømchiffer spiller ingen rolle for resultatet. Denne egenskapen er kjent som **kommutativitet**.)
En typisk XOR-strømkryptering er avbildet i *Figur 3*. Du tar først en privat nøkkel $K$ og bruker den til å generere en nøkkelstrøm. Nøkkelstrømmen kombineres deretter med klarteksten via en XOR-operasjon for å produsere kryptoteksten. Enhver agent som mottar kryptoteksten kan enkelt dekryptere den hvis de har nøkkelen $K$. Alt hun trenger å gjøre er å skape en nøkkelstrøm like lang som kryptoteksten i henhold til den spesifiserte prosedyren for ordningen og XOR den med kryptoteksten.

*Figur 3: En XOR-strømkryptering*

![Figur 3: En XOR-strømkryptering](assets/Figure4-3.webp "Figur 3: En XOR-strømkryptering")

Husk at et krypteringsskjema typisk er en mal for kryptering med samme kjernealgoritme, snarere enn en eksakt spesifikasjon. Tilsvarende er en strømkryptering typisk en mal for kryptering der du kan bruke nøkler av forskjellige lengder. Selv om nøkkellengden kan påvirke noen mindre detaljer i ordningen, vil den ikke påvirke dens essensielle form.

Skiftkryptering er et eksempel på en veldig enkel og usikker strømkryptering. Ved å bruke en enkelt bokstav (den private nøkkelen), kan du produsere en rekke bokstaver like lang som meldingen (nøkkelstrømmen). Denne nøkkelstrømmen kombineres deretter med klarteksten via en modulo-operasjon for å produsere en kryptotekst. (Denne modulo-operasjonen kan forenkles til en XOR-operasjon når man representerer bokstavene i biter).

Et annet kjent eksempel på en strømkryptering er **Vigenère-krypteringen**, etter Blaise de Vigenère som fullt utviklet den på slutten av det 16. århundre (selv om andre hadde gjort mye forarbeid). Det er et eksempel på en **polyalfabetisk substitusjonskryptering**: et krypteringsskjema der kryptotekstalfabetet for et klartekstsymbol endres avhengig av dets posisjon i teksten. I motsetning til en monoalfabetisk substitusjonskryptering, kan kryptotekstsymboler være assosiert med mer enn ett klartekstsymbol.

Ettersom kryptering fikk popularitet i renessanse-Europa, gjorde også **kryptoanalyse**—det vil si, bryting av kryptotekster—spesielt ved bruk av **frekvensanalyse**. Sistnevnte bruker statistiske regelmessigheter i vårt språk for å bryte kryptotekster, og ble oppdaget av arabiske lærde allerede på det niende århundret. Det er en teknikk som fungerer spesielt godt med lengre tekster. Og selv de mest sofistikerte monoalfabetiske substitusjonskrypteringene var ikke lenger tilstrekkelige mot frekvensanalyse på 1700-tallet i Europa, spesielt i militære og sikkerhetsinnstillinger. Ettersom Vigenère-krypteringen tilbød en betydelig forbedring i sikkerhet, ble den populær i denne perioden og var utbredt innen slutten av 1700-tallet.

Uformelt sagt, fungerer krypteringsskjemaet som følger:

1. Velg et flerbokstavsord som den private nøkkelen.
2. For enhver melding, bruk skiftkrypteringen på hver bokstav i meldingen ved å bruke den tilsvarende bokstaven i nøkkelordet som skiftet.
3. Hvis du har syklet gjennom nøkkelordet, men fortsatt ikke har kryptert klarteksten helt, bruk igjen nøkkelordets bokstaver som en skiftkryptering på de tilsvarende bokstavene i resten av teksten.
4. Fortsett denne prosessen til hele meldingen har blitt kryptert.

For å illustrere, anta at din private nøkkel er "GOLD" og du ønsker å kryptere meldingen "CRYPTOGRAPHY". I så fall ville du fortsette som følger i henhold til Vigenère-krypteringen:

- $c_0  = [(2 + 6) \mod 26] = 8 = I$
- $c_1  = [(17 + 14) \mod 26] = 5 = F$
- $c_2  = [(24 + 11) \mod 26] = 9 = J$
- $c_3  = [(15 + 3) \mod 26] = 18 = S$
- $c_4  = [(19 + 6) \mod 26] = 25 = Z$
- $c_5  = [(14 + 14) \mod 26] = 2 = C$
- $c_6  = [(6 + 11) \mod 26] = 17 = R$
- $c_7  = [(17 + 3) \mod 26] = 20 = U$
- $c_8  = [(0 + 6) \mod 26] = 6 = G$
- $c_9  = [(15 + 14) \mod 26] = 3 = D$
- $c_{10} = [(7 + 11) \mod 26] = 18 = S$
- $c_{11} = [(24 + 3) \mod 26] = 1 = B$

Dermed blir krypteringsteksten $c$ = "IFJSZCRUGDSB".

Et annet kjent eksempel på en strømkryptering er **engangsblokk**. Med engangsblokk oppretter du ganske enkelt en streng med tilfeldige biter som er like lang som den opprinnelige meldingen og produserer krypteringsteksten via XOR-operasjonen. Dermed er den private nøkkelen og nøkkelstrømmen ekvivalente med en engangsblokk.

Mens Shift-kryptering og Vigenere-krypteringer er veldig usikre i den moderne tidsalder, er engangsblokk veldig sikker hvis den brukes korrekt. Sannsynligvis den mest kjente bruken av engangsblokk var, i det minste til 1980-tallet, for **Washington-Moskva-hotlinjen**. [4]

Hotlinjen er en direkte kommunikasjonslenke mellom Washington og Moskva for presserende saker som ble installert etter Cubakrisen. Teknologien for har transformert seg over årene. For tiden inkluderer den en direkte fiber optisk kabel samt to satellittlenker (for redundans), som muliggjør e-post og tekstmeldinger. Lenken ender på forskjellige steder i USA. Pentagon, Det hvite hus og Raven Rock Mountain er kjente endepunkter. I motsetning til populær oppfatning, har hotlinjen aldri involvert telefoner.

I sin essens fungerte engangsblokkordningen som følger. Både Washington og Moskva ville ha to sett med tilfeldige tall. Ett sett med tilfeldige tall, skapt av russerne, gjaldt kryptering og dekryptering av eventuelle meldinger på russisk. Ett sett med tilfeldige tall, skapt av amerikanerne, gjaldt kryptering og dekryptering av eventuelle meldinger på engelsk. Fra tid til annen ville flere tilfeldige tall bli levert til den andre siden av pålitelige kurerer.

Washington og Moskva kunne dermed kommunisere hemmelig ved å bruke disse tilfeldige tallene for å opprette engangsblokker. Hver gang du trengte å kommunisere, ville du bruke den neste delen av tilfeldige tall for meldingen din.

Selv om den er svært sikker, står engangsblokk overfor betydelige praktiske begrensninger: nøkkelen må være like lang som meldingen, og ingen del av en engangsblokk kan gjenbrukes. Dette betyr at du må holde styr på hvor du er i engangsblokk, lagre et massivt antall biter, og utveksle tilfeldige biter med dine motparter fra tid til annen. Som en konsekvens er ikke engangsblokk ofte brukt i praksis.

I stedet er de dominerende strømkrypteringene som brukes i praksis **pseudotilfeldige strømkrypteringer**. Salsa20 og en nært beslektet variant kalt ChaCha er eksempler på vanlig brukte pseudotilfeldige strømkrypteringer.
Med disse pseudotilfeldige strømkrypteringene velger du først tilfeldig en nøkkel $K$ som er kortere enn lengden på klarteksten. En slik tilfeldig nøkkel $K$ blir vanligvis skapt av datamaskinen vår på grunnlag av uforutsigbare data som den samler over tid, slik som tiden mellom nettverksmeldinger, musebevegelser, og så videre.
Denne tilfeldige nøkkelen $K$ settes deretter inn i en ekspansjonsalgoritme som skaper en pseudotilfeldig nøkkelstrøm like lang som meldingen. Du kan spesifisere nøyaktig hvor lang nøkkelstrømmen trenger å være (f.eks., 500 bits, 1000 bits, 1200 bits, 29,117 bits, og så videre).

En pseudotilfeldig nøkkelstrøm ser ut *som om* den var valgt helt tilfeldig fra settet av alle strenger med samme lengde. Derfor ser kryptering med en pseudotilfeldig nøkkelstrøm ut som om den hadde blitt gjort med en engangsnøkkel. Men det er selvfølgelig ikke tilfellet.

Ettersom vår private nøkkel er kortere enn nøkkelstrømmen og vår ekspansjonsalgoritme må være deterministisk for at kryptering/dekrypteringsprosessen skal fungere, kunne ikke hver nøkkelstrøm av den spesifikke lengden ha resultert som et utdata fra vår ekspansjonsoperasjon.

Anta, for eksempel, at vår private nøkkel har en lengde på 128 bits og at vi kan sette den inn i en ekspansjonsalgoritme for å skape en mye lengre nøkkelstrøm, si på 2,500 bits. Ettersom vår ekspansjonsalgoritme må være deterministisk, kan vår algoritme på det meste velge $1/2^{128}$ strenger med en lengde på 2,500 bits. Så en slik nøkkelstrøm kunne aldri bli valgt helt tilfeldig fra alle strengene av samme lengde.

Vår definisjon av en strømkryptering har to aspekter: (1) en nøkkelstrøm like lang som klarteksten genereres med hjelp av en privat nøkkel; og (2) denne nøkkelstrømmen kombineres med klarteksten, typisk via en XOR-operasjon, for å produsere kryptoteksten.

Noen ganger definerer folk betingelse (1) mer strengt, ved å hevde at nøkkelstrømmen spesifikt må være pseudotilfeldig. Dette betyr at verken skiftkrypteringen eller engangsnøkkelen ville bli betraktet som strømkrypteringer.

I mitt synspunkt gir det å definere betingelse (1) mer bredt en enklere måte å organisere krypteringsskjemaer på. I tillegg betyr det at vi ikke må slutte å kalle et spesifikt krypteringsskjema for en strømkryptering bare fordi vi lærer at det faktisk ikke stoler på pseudotilfeldige nøkkelstrømmer.

**Notater:**

[4] Crypto Museum, "Washington-Moskva direkte linje," 2013, tilgjengelig på [https://www.cryptomuseum.com/crypto/hotline/index.htm](https://www.cryptomuseum.com/crypto/hotline/index.htm).

## Blokk-krypteringer
<chapterId>2df52d51-943d-5df7-9d49-333e4c5d97b7</chapterId>

Den første måten som en **blokk-kryptering** vanligvis forstås på er som noe mer primitivt enn en strømkryptering: En kjernealgoritme som utfører en lengdebevarende transformasjon på en streng av passende lengde med hjelp av en nøkkel. Denne algoritmen kan brukes for å skape krypteringsskjemaer og kanskje andre typer kryptografiske skjemaer.
Ofte kan en blokkchiffer ta inngangsstrømmer av varierende lengder som 64, 128 eller 256 bit, samt nøkler av varierende lengder som 128, 192 eller 256 bit. Selv om noen detaljer i algoritmen kan endre seg avhengig av disse variablene, endres ikke kjernalgoritmen. Hvis den gjorde det, ville vi snakke om to forskjellige blokkchifre. Merk at bruken av terminologien kjernalgoritme her er den samme som for krypteringsskjemaer.
En fremstilling av hvordan en blokkchiffer fungerer kan ses i *Figur 4* nedenfor. En melding $M$ av lengde $L$ og en nøkkel $K$ fungerer som innganger til blokkchifferet. Det gir ut en melding $M'$ av lengde $L$. Nøkkelen trenger ikke nødvendigvis å være av samme lengde som $M$ og $M'$ for de fleste blokkchifre.

*Figur 4: En blokkchiffer*

![Figur 4: En blokkchiffer](assets/Figure4-4.webp "Figur 4: En blokkchiffer")

En blokkchiffer i seg selv er ikke et krypteringsskjema. Men en blokkchiffer kan brukes med ulike **driftsmoduser** for å produsere forskjellige krypteringsskjemaer. En driftsmodus legger ganske enkelt til noen ekstra operasjoner utenfor blokkchifferet.

For å illustrere hvordan dette fungerer, anta en blokkchiffer (BC) som krever en 128-bit inngangsstrøm og en 128-bit privat nøkkel. Figur 5 nedenfor viser hvordan den blokkchifferen kan brukes med **elektronisk kodebokmodus** (**ECB-modus**) for å skape et krypteringsskjema. (De tre prikkene til høyre indikerer at du kan gjenta dette mønsteret så lenge det er nødvendig).

*Figur 5: En blokkchiffer med ECB-modus*

![Figur 5: En blokkchiffer med ECB-modus](assets/Figure4-5.webp "Figur 5: En blokkchiffer med ECB-modus")

Prosessen for elektronisk kodebokkryptering med blokkchifferet er som følger. Se om du kan dele din klartekstmelding inn i 128-bit blokker. Hvis ikke, legg til **utfylling** til meldingen, slik at resultatet kan deles jevnt med blokkstørrelsen på 128 bit. Dette er dataene som brukes til krypteringsprosessen.

Del nå dataene inn i biter av 128-bit strenger ($M_1$, $M_2$, $M_3$, og så videre). Kjør hver 128-bit streng gjennom blokkchifferet med din 128-bit nøkkel for å produsere 128-bit biter av kryptert tekst ($C_1$, $C_2$, $C_3$, og så videre). Disse bitene, når de kombineres på nytt, danner den fullstendige krypterte teksten.

Dekryptering er bare den omvendte prosessen, selv om mottakeren trenger en gjenkjennelig måte å fjerne eventuell utfylling fra de dekrypterte dataene for å produsere den opprinnelige klartekstmeldingen.

Selv om det er relativt enkelt, mangler en blokkchiffer med elektronisk kodebokmodus sikkerhet. Dette er fordi det fører til **deterministisk kryptering**. To identiske 128-bit strenger av data krypteres nøyaktig på samme måte. Den informasjonen kan utnyttes.

I stedet bør ethvert krypteringsskjema konstruert fra en blokkchiffer være **probabilistisk**: det vil si at krypteringen av enhver melding $M$, eller enhver spesifikk bit av $M$, generelt bør gi et annet utfall hver gang. [5]

**Cipher block chaining-modus** (**CBC-modus**) er sannsynligvis den mest brukte modusen med en blokkchiffer. Kombinasjonen, hvis gjort riktig, produserer et probabilistisk krypteringsskjema. Du kan se en fremstilling av denne driftsmodusen i *Figur 6* nedenfor.

*Figur 6: En blokkchiffer med CBC-modus*
![Figure 6: En blokkchiffer med CBC-modus](assets/Figure4-6.webp "Figur 6: En blokkchiffer med CBC-modus")
Anta at blokkstørrelsen igjen er 128 bit. Så for å starte, må du igjen sørge for at din opprinnelige klartekstmelding mottar nødvendig utfylling.

Deretter XORer du den første 128-bit delen av klarteksten din med en **initialiseringsvektor** på 128 bit. Resultatet plasseres i blokkchifferet for å produsere en kryptert tekst for den første blokken. For den andre blokken på 128 bit, XORer du først klarteksten med den krypterte teksten fra den første blokken, før du setter den inn i blokkchifferet. Du fortsetter denne prosessen til du har kryptert hele klartekstmeldingen din.

Når du er ferdig, sender du den krypterte meldingen sammen med den ukrypterte initialiseringsvektoren til mottakeren. Mottakeren trenger å vite initialiseringsvektoren, ellers kan hun ikke dekryptere den krypterte teksten.

Denne konstruksjonen er mye sikrere enn elektronisk kodebokmodus når den brukes riktig. Du bør først sørge for at initialiseringsvektoren er en tilfeldig eller pseudotilfeldig streng. I tillegg bør du bruke en annen initialiseringsvektor hver gang du bruker dette krypteringsskjemaet.

Med andre ord, din initialiseringsvektor bør være en tilfeldig eller pseudotilfeldig engangstall, hvor et **engangstall** står for "et tall som bare brukes én gang." Hvis du holder denne praksisen, så sikrer CBC-modus med en blokkchiffer at to identiske klartekstblokker generelt vil bli kryptert forskjellig hver gang.

Til slutt, la oss rette oppmerksomheten mot **output feedback-modus** (**OFB-modus**). Du kan se en fremstilling av denne modusen i *Figur 7*.

*Figur 7: En blokkchiffer med OFB-modus*

![Figure 7: En blokkchiffer med OFB-modus](assets/Figure4-7.webp "Figur 7: En blokkchiffer med OFB-modus")

Med OFB-modus velger du også en initialiseringsvektor. Men her, for den første blokken, settes initialiseringsvektoren direkte inn i blokkchifferet med nøkkelen din. De resulterende 128 bitene behandles deretter som en nøkkelstrøm. Denne nøkkelstrømmen XORes med klarteksten for å produsere den krypterte teksten for blokken. For påfølgende blokker bruker du nøkkelstrømmen fra den forrige blokken som en inngang i blokkchifferet og gjentar trinnene.

Hvis du ser nøye etter, hva som faktisk har blitt skapt her fra blokkchifferet med OFB-modus er en strømchiffer. Du genererer nøkkelstrømdeler på 128 bit til du har lengden på klarteksten (forkaster bitene du ikke trenger fra den siste 128-bit nøkkelstrømdelen). Du XORer deretter nøkkelstrømmen med klartekstmeldingen din for å oppnå den krypterte teksten.

I den forrige seksjonen om strømchiffere, uttalte jeg at du produserer en nøkkelstrøm med hjelp av en privat nøkkel. For å være nøyaktig, trenger den ikke bare å bli skapt med en privat nøkkel. Som du kan se i OFB-modus, produseres nøkkelstrømmen med støtte av både en privat nøkkel og en initialiseringsvektor.

Merk at som med CBC-modus, er det viktig å velge et pseudotilfeldig eller tilfeldig engangstall for initialiseringsvektoren hver gang du bruker en blokkchiffer i OFB-modus. Ellers vil den samme 128-bit meldingsstrengen sendt i forskjellige kommunikasjoner bli kryptert på samme måte. Dette er en måte å skape probabilistisk kryptering med en strømchiffer på.
Noen strømkrypteringer bruker kun en privat nøkkel for å skape en nøkkelstrøm. For disse strømkrypteringene er det viktig at du bruker en tilfeldig nonce for å velge den private nøkkelen for hver kommunikasjonsinstans. Ellers vil resultatene av kryptering med disse strømkrypteringene også være deterministiske, noe som fører til sikkerhetsproblemer.
Den mest populære moderne blokkrypteringen er **Rijndael-krypteringen**. Den var det vinnende bidraget av femten innsendelser til en konkurranse holdt av National Institute of Standards and Technology (NIST) mellom 1997 og 2000 for å erstatte en eldre krypteringsstandard, **datakrypteringsstandarden** (**DES**).

Rijndael-krypteringen kan brukes med forskjellige spesifikasjoner for nøkkellengder og blokkstørrelser, samt i forskjellige driftsmoduser. Komiteen for NIST-konkurransen vedtok en begrenset versjon av Rijndael-krypteringen—nemlig en som krever 128-bits blokkstørrelser og nøkkellengder på enten 128 bits, 192 bits eller 256 bits—som en del av **avansert krypteringsstandard** (**AES**). Dette er virkelig hovedstandarden for symmetrisk krypteringsapplikasjoner. Den er så sikker at selv NSA tilsynelatende er villig til å bruke den med 256-bits nøkler for topphemmelige dokumenter. [6]

AES-blokkrypteringen vil bli forklart i detalj i *Kapittel 5*.


**Notater:**

[5] Viktigheten av probabilistisk kryptering ble først understreket av Shafi Goldwasser og Silvio Micali, “Probabilistisk kryptering,” _Journal of Computer and System Sciences_, 28 (1984), 270–99.

[6] Se NSA, "Commercial National Security Algorithm Suite", [https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm](https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm).



## Rydde opp i forvirringen
<chapterId>121c1858-27e3-5862-b0ce-4ff2f70f9f0f</chapterId>

Forvirringen om forskjellen mellom blokkrypteringer og strømkrypteringer oppstår fordi noen ganger vil folk forstå begrepet blokkryptering som spesifikt å referere til en *blokkryptering med en blokkmodus for kryptering*.

Vurder ECB- og CBC-modusene i forrige avsnitt. Disse krever spesifikt at dataene for kryptering må være delelige med blokkstørrelsen (noe som betyr at du kanskje må bruke utfylling for den opprinnelige meldingen). I tillegg opereres dataene i disse modusene også direkte av blokkrypteringen (og ikke bare kombinert med resultatet av en blokkrypteringsoperasjon som i OFB-modus).

Derfor kan du alternativt definere en **blokkryptering** som ethvert krypteringsskjema som opererer på fastlengde blokker av meldingen om gangen (hvor enhver blokk må være lengre enn en byte, ellers kollapser den til en strømkryptering). Både dataene for kryptering og kryptoteksten må deles jevnt inn i denne blokkstørrelsen. Typisk er blokkstørrelsen 64, 128, 192 eller 256 bits i lengde. I motsetning kan en strømkryptering kryptere meldinger i biter på ett bit eller byte om gangen.

Med denne mer spesifikke forståelsen av blokkryptering, kan du faktisk hevde at moderne krypteringsskjemaer enten er strøm- eller blokkrypteringer. Heretter vil jeg mene begrepet blokkryptering i den mer generelle forstanden med mindre annet er spesifisert.
Diskusjonen om OFB-modus i forrige seksjon reiser også et annet interessant poeng. Noen strømkrypteringer er bygget fra blokk-krypteringer, som Rijndael med OFB. Noen, som Salsa20 og ChaCha, er ikke skapt fra blokk-krypteringer. Du kan kalle sistnevnte for **primitive strømkrypteringer**. (Det finnes egentlig ikke et standardisert uttrykk for å referere til slike strømkrypteringer.)
Når folk snakker om fordelene og ulempene med strømkrypteringer og blokk-krypteringer, sammenligner de typisk primitive strømkrypteringer med krypteringsskjemaer basert på blokk-krypteringer.

Selv om du alltid enkelt kan konstruere en strømkryptering fra en blokk-kryptering, er det vanligvis veldig vanskelig å bygge en type konstruksjon med en blokkmodus for kryptering (som med CBC-modus) fra en primitiv strømkryptering.

Fra denne diskusjonen bør du nå forstå *Figur 8*. Den gir en oversikt over symmetriske krypteringsskjemaer. Vi bruker tre typer krypteringsskjemaer: primitive strømkrypteringer, blokk-kryptering strømkrypteringer, og blokk-krypteringer i en blokkmodus (også kalt "blokk-krypteringer" i diagrammet).

*Figur 8: Oversikt over symmetriske krypteringsskjemaer*

![Figur 8: Oversikt over symmetriske krypteringsskjemaer](assets/Figure4-8.webp "Figur 8: Oversikt over symmetriske krypteringsskjemaer")


## Meldingsautentiseringskoder
<chapterId>19fa7c00-db59-56a0-9654-5350a137939d</chapterId>

Kryptering handler om hemmelighold. Men kryptografi er også opptatt av bredere temaer, som meldingsintegritet, autentisitet og ikke-avvisning. Såkalte **meldingsautentiseringskoder** (MACs) er symmetriske nøkkelkryptografiske skjemaer som støtter autentisitet og integritet i kommunikasjon.

Hvorfor er noe annet enn hemmelighold nødvendig i kommunikasjon? Anta at Bob sender Alice en melding ved hjelp av praktisk talt ubrytelig kryptering. Enhver angriper som avlytter denne meldingen vil ikke kunne fastslå noen betydelige innsikter angående innholdet. Imidlertid har angriperen fortsatt minst to andre angrepsvektorer tilgjengelig for seg:

1. Hun kunne avlytte kryptoteksten, endre innholdet, og sende den endrede kryptoteksten videre til Alice.
2. Hun kunne blokkere Bobs melding helt og sende sin egen opprettede kryptotekst.

I begge disse tilfellene kan angriperen ikke ha noen innsikt i innholdet fra kryptotekstene (1) og (2). Men hun kunne fortsatt forårsake betydelig skade på denne måten. Dette er hvor meldingsautentiseringskoder blir viktige.

Meldingsautentiseringskoder er løst definert som symmetriske kryptografiske skjemaer med tre algoritmer: en nøkkelgenereringsalgoritme, en tag-genereringsalgoritme, og en verifiseringsalgoritme. En sikker MAC sikrer at tagger er **eksistensielt uforfalskbare** for enhver angriper – det vil si, de kan ikke lykkes med å skape en tag på meldingen som verifiserer, med mindre de har den private nøkkelen.

Bob og Alice kan bekjempe manipulasjonen av en bestemt melding ved hjelp av en MAC. Anta for øyeblikket at de ikke bryr seg om hemmelighold. De ønsker bare å sikre at meldingen mottatt av Alice faktisk var fra Bob og ikke endret på noen måte.

Prosessen er avbildet i *Figur 9*. For å bruke en **MAC** (Message Authentication Code), ville de først generere en privat nøkkel $K$ som deles mellom dem. Bob skaper en tag $T$ for meldingen ved hjelp av den private nøkkelen $K$. Han sender deretter meldingen samt meldingstagen til Alice. Hun kan da verifisere at Bob faktisk lagde tagen, ved å kjøre den private nøkkelen, meldingen, og tagen gjennom en verifiseringsalgoritme.

*Figur 9: Oversikt over symmetriske krypteringsskjemaer*
![Figur 9: Oversikt over symmetriske krypteringsskjemaer](assets/Figure4-9.webp "Figur 9: Oversikt over symmetriske krypteringsskjemaer")
På grunn av **eksistensiell uforfalskbarhet**, kan en angriper ikke endre meldingen $M$ på noen måte eller skape en egen melding med en gyldig tagg. Dette gjelder selv om angriperen observerer taggene til mange meldinger mellom Bob og Alice som bruker samme private nøkkel. I beste fall kunne en angriper blokkere Alice fra å motta meldingen $M$ (et problem som kryptografi ikke kan adressere).

En MAC garanterer at en melding faktisk ble opprettet av Bob. Denne autentisiteten innebærer automatisk meldingsintegritet – det vil si, hvis Bob har opprettet en melding, så ble den ipso facto ikke endret på noen måte av en angriper. Så fra nå av bør enhver bekymring for autentisering automatisk forstås som en bekymring for integritet.

Selv om jeg har trukket et skille mellom meldingsautentisitet og integritet i min diskusjon, er det også vanlig å bruke disse begrepene som synonymer. De refererer da til ideen om meldinger som både ble opprettet av en bestemt avsender og ikke endret på noen måte. I denne ånden kalles meldingsautentiseringskoder ofte også for **meldingsintegritetskoder**.


## Autentisert kryptering
<chapterId>33f2ec9b-9fb4-5c61-8fb4-50836270a144</chapterId>

Vanligvis vil du ønske å garantere både hemmelighold og autentisitet i kommunikasjon, og derfor brukes krypteringsskjemaer og MAC-skjemaer vanligvis sammen.

Et **autentisert krypteringsskjema** er et skjema som kombinerer kryptering med en MAC på en svært sikker måte. Spesifikt må det oppfylle standardene for eksistensiell uforfalskbarhet samt en veldig sterk form for hemmelighold, nemlig en som er motstandsdyktig mot **valgte-chiffer-tekst-angrep**. [7]

For at et krypteringsskjema skal være motstandsdyktig mot valgte-chiffer-tekst-angrep, må det oppfylle standardene for **ikke-foranderlighet**: det vil si at enhver modifikasjon av en chiffer-tekst av en angriper skal gi enten en ugyldig chiffer-tekst eller en som dekrypteres til en klartekst som ikke har noen relasjon til den opprinnelige. [8]

Ettersom et autentisert krypteringsskjema sikrer at en chiffer-tekst opprettet av en angriper alltid er ugyldig (siden taggen ikke vil bli verifisert), oppfyller det standardene for motstand mot valgte-chiffer-tekst-angrep. Interessant nok kan du bevise at et autentisert krypteringsskjema alltid kan skapes fra kombinasjonen av en eksistensielt uforfalskbar MAC og et krypteringsskjema som møter en mindre sterk sikkerhetsnotasjon, kjent som **valgt-klartekst-angrep-sikkerhet**.

Vi vil ikke gå inn på alle detaljene i konstruksjonen av autentiserte krypteringsskjemaer. Men det er viktig å kjenne til to detaljer ved deres konstruksjon.

Først håndterer et autentisert krypteringsskjema først krypteringen og deretter oppretter det en meldingstagg på chiffer-teksten. Det viser seg at andre tilnærminger – som å kombinere chiffer-teksten med en tagg på klarteksten, eller først opprette en tagg og deretter kryptere både klarteksten og taggen – er usikre. I tillegg har begge operasjonene sin egen tilfeldig valgte private nøkkel, ellers er sikkerheten din alvorlig kompromittert.

Det ovennevnte prinsippet gjelder mer generelt: *du bør alltid bruke distinkte nøkler når du kombinerer grunnleggende kryptografiske skjemaer*.

Et autentisert krypteringsskjema er avbildet i *Figur 10*. Bob oppretter først en chiffer-tekst $C$ fra meldingen $M$ ved hjelp av en tilfeldig valgt nøkkel $K_C$. Deretter oppretter han en meldingstagg $T$ ved å kjøre chiffer-teksten og en annen tilfeldig valgt nøkkel $K_T$ gjennom taggenereringsalgoritmen. Både chiffer-teksten og meldingstaggen sendes til Alice.
Alice sjekker nå først om taggen er gyldig gitt krypteringsteksten $C$ og nøkkelen $K_T$. Hvis gyldig, kan hun deretter dekryptere meldingen ved hjelp av nøkkelen $K_C$. Ikke bare er hun sikret en veldig sterk oppfatning av hemmelighold i deres kommunikasjon, men hun vet også at meldingen ble opprettet av Bob.
*Figur 10: Et autentisert krypteringsskjema*

![Figur 10: Et autentisert krypteringsskjema](assets/Figure4-10.webp "Figur 10: Et autentisert krypteringsskjema")

Hvordan lages MAC-er? Selv om MAC-er kan opprettes via flere metoder, er en vanlig og effektiv måte å lage dem på via **kryptografiske hash-funksjoner**.

Vi vil introdusere kryptografiske hash-funksjoner mer grundig i *Kapittel 6*. For nå, bare vit at en **hash-funksjon** er en effektivt beregnbar funksjon som tar inndata av vilkårlig størrelse og gir utdata med fast lengde. For eksempel genererer den populære hash-funksjonen **SHA-256** (secure hash algorithm 256) alltid en 256-bit utdata uavhengig av størrelsen på inndata. Noen hash-funksjoner, som SHA-256, har nyttige anvendelser i kryptografi.

Den mest vanlige typen tag produsert med en kryptografisk hash-funksjon er **hash-basert meldingsautentiseringskode** (HMAC). Prosessen er avbildet i *Figur 11*. En part produserer to distinkte nøkler fra en privat nøkkel $K$, den indre nøkkelen $K_1$ og den ytre nøkkelen $K_2$. Klarteksten $M$ eller krypteringsteksten $C$ hashes deretter sammen med den indre nøkkelen. Resultatet $T'$ hashes så med den ytre nøkkelen for å produsere meldingstaggen $T$.

Det finnes en palett av hash-funksjoner som kan brukes til å lage en HMAC. Den mest vanlig brukte hash-funksjonen er SHA-256.


*Figur 11: HMAC*

![Figur 11: HMAC](assets/Figure4-11.webp "Figur 11: HMAC")

**Notater:**

[7] De spesifikke resultatene diskutert i dette avsnittet er fra Katz og Lindell, s. 131–47.

[8] Teknisk sett er definisjonen av angrep med valgt krypteringstekst forskjellig fra begrepet ikke-malleabilitet. Men du kan vise at disse to sikkerhetsbegrepene er ekvivalente.



## Sikre kommunikasjonssesjoner
<chapterId>c7f7dcd3-bbed-53ed-a43d-039da0f180c5</chapterId>

Anta at to parter er i en kommunikasjonssesjon, så de sender flere meldinger frem og tilbake.

Et autentisert krypteringsskjema lar en mottaker av en melding verifisere at den ble opprettet av hennes partner i kommunikasjonssesjonen (så lenge den private nøkkelen ikke har lekket). Dette fungerer godt nok for en enkelt melding. Typisk vil imidlertid to parter sende meldinger frem og tilbake i en kommunikasjonssesjon. Og i den settingen kommer et rent autentisert krypteringsskjema til kort i å tilby sikkerhet.

Hovedgrunnen er at et autentisert krypteringsskjema ikke gir noen garantier for at meldingen faktisk også ble sendt av agenten som opprettet den innenfor en kommunikasjonssesjon. Vurder følgende tre angrepsvektorer:

1. **Replay-angrep**: En angriper sender på nytt en krypteringstekst og en tag som hun avlyttet mellom to parter på et tidligere tidspunkt.
2. **Rekkefølgeangrep**: En angriper avlytter to meldinger på forskjellige tidspunkter og sender dem til mottakeren i motsatt rekkefølge.
3. **Refleksjonsangrep**: En angriper observerer en melding sendt fra A til B, og sender også den meldingen til A.

Selv om angriperen ikke har kunnskap om krypteringsteksten og ikke kan lage forfalskede krypteringstekster, kan angrepene ovenfor fortsatt forårsake betydelig skade i kommunikasjonen.
Anta, for eksempel, at en bestemt melding mellom to parter involverer overføring av finansielle midler. Et replay-angrep kan overføre midlene en andre gang. Et vanlig autentisert krypteringsskjema har ingen forsvar mot slike angrep.
Heldigvis kan disse typene angrep enkelt avverges i en kommunikasjonssesjon ved bruk av **identifikatorer** og **relative tidsindikatorer**.

Identifikatorer kan legges til i klartekstmeldingen før kryptering. Dette ville forhindre eventuelle refleksjonsangrep. En relativ tidsindikator kan for eksempel være et sekvensnummer i en bestemt kommunikasjonssesjon. Hver part legger til et sekvensnummer i en melding før kryptering, slik at mottakeren vet i hvilken rekkefølge meldingene ble sendt. Dette eliminerer muligheten for omorganiseringsangrep. Det eliminerer også replay-angrep. Enhver melding en angriper sender videre vil ha et gammelt sekvensnummer, og mottakeren vil vite å ikke behandle meldingen igjen.

For å illustrere hvordan sikre kommunikasjonssesjoner fungerer, anta igjen Alice og Bob. De sender totalt fire meldinger frem og tilbake. Du kan se hvordan et autentisert krypteringsskjema med identifikatorer og sekvensnumre ville fungere nedenfor i *Figur 11*.

Kommunikasjonssesjonen starter med at Bob sender en kryptert tekst $C_{0,B}$ til Alice med en meldingstag $T_{0,B}$. Den krypterte teksten inneholder meldingen, samt en identifikator (BOB) og et sekvensnummer (0). Taggen $T_{0,B}$ er laget over hele den krypterte teksten. I deres påfølgende kommunikasjoner opprettholder Alice og Bob denne protokollen, og oppdaterer feltene etter behov.

*Figur 12: En sikker kommunikasjonssesjon*

![Figur 12: En sikker kommunikasjonssesjon](assets/Figure4-12.webp "Figur 12: En sikker kommunikasjonssesjon")

# RC4 og AES
<partId>a48c4a7d-0a41-523f-a4ab-1305b4430324</partId>

## RC4-strømkrypteringen
<chapterId>5caec5bd-5a77-56c9-b5e6-1e86f0d294aa</chapterId>

I dette kapittelet vil vi diskutere detaljene i et krypteringsskjema med en moderne primitiv strømkryptering, RC4 (eller "Rivest cipher 4"), og en moderne blokkryptering, AES. Selv om RC4-krypteringen har falt i unåde som en metode for kryptering, er AES standarden for moderne symmetrisk kryptering. Disse to eksemplene bør gi en bedre forståelse av hvordan symmetrisk kryptering fungerer under panseret.

___

For å ha en følelse av hvordan moderne pseudotilfeldige strømkrypteringer fungerer, vil jeg fokusere på RC4-strømkrypteringen. Det er en pseudotilfeldig strømkryptering som ble brukt i WEP- og WAP-trådløse tilgangspunkt sikkerhetsprotokoller samt i TLS. Ettersom RC4 har mange beviste svakheter, har den falt i unåde. Faktisk forbyr Internet Engineering Task Force nå bruk av RC4-suitene av klient- og serverapplikasjoner i alle instanser av TLS. Likevel fungerer den godt som et eksempel for å illustrere hvordan en primitiv strømkryptering fungerer.

For å starte, vil jeg først vise hvordan man krypterer en klartekstmelding med en baby RC4-kryptering. Anta at vår klartekstmelding er “SOUP.” Kryptering med vår baby RC4-kryptering skjer da i fire trinn.

### Trinn 1
Først, definer en matrise **S** med $S[0] = 0$ til $S[7] = 7$. En matrise her betyr ganske enkelt en foranderlig samling av verdier organisert av et indeks, også kalt en liste i noen programmeringsspråk (f.eks., Python). I dette tilfellet går indeksen fra 0 til 7, og verdiene går også fra 0 til 7. Så **S** er som følger:
- $S = [0, 1, 2, 3, 4, 5, 6, 7]$

Verdiene her er ikke ASCII-tall, men desimalverdi-representasjoner av 1-byte strenger. Så verdien 2 ville være lik $0000 \ 0011$. Lengden på matrisen **S** er derfor 8 bytes.

### Steg 2

For det andre, definer en nøkkelmatrise **K** med lengde på 8 bytes ved å velge en nøkkel mellom 1 og 8 bytes (uten brøkdeler av bytes tillatt). Siden hver byte er 8 bits, kan du velge et hvilket som helst tall mellom 0 og 255 for hver byte av nøkkelen din.

Anta at vi velger vår nøkkel **k** som $[14, 48, 9]$, slik at den har en lengde på 3 bytes. Hvert indeks av vår nøkkelmatrise settes da i henhold til desimalverdien for det spesifikke elementet av nøkkelen, i rekkefølge. Hvis du går gjennom hele nøkkelen, start på nytt ved begynnelsen, til du har fylt de 8 plassene i nøkkelmatrisen. Dermed er vår nøkkelmatrise som følger:

- $K = [14, 48, 9, 14, 48, 9, 14, 48]$

### Steg 3

For det tredje vil vi transformere matrisen **S** ved hjelp av nøkkelmatrisen **K**, i en prosess kjent som **nøkkelplanlegging**. Prosessen er som følger i pseudokode:

- Opprett variabler **j** og **i**
- Sett variabelen $j = 0$
- For hver $i$ fra 0 til 7:
    - Sett $j = (j + S[i] + K[i]) \mod 8$
    - Bytt om $S[i]$ og $S[j]$

Transformasjonen av matrisen **S** er fanget av *Tabell 1*.

For å starte, kan du se den opprinnelige tilstanden til **S** som $[0, 1, 2, 3, 4, 5, 6, 7]$ med en opprinnelig verdi på 0 for **j**. Dette vil bli transformert ved hjelp av nøkkelmatrisen $[14, 48, 9, 14, 48, 9, 14, 48]$.

For-løkken starter med $i = 0$. I henhold til vår pseudokode ovenfor, blir den nye verdien av **j** 6 ($j = (j + S[0] + K[0]) \mod 8 = (0 + 0 + 14) \mod 8 = 6 \mod 8$). Ved å bytte om $S[0]$ og $S[6]$, blir tilstanden til **S** etter 1 runde $[6, 1, 2, 3, 4, 5, 0, 7]$.
I neste rad er $i = 1$. Når vi går gjennom for-løkken igjen, får **j** en verdi på 7 ($j = (j + S[1] + K[1]) \mod 8 = (6 + 1 + 48) \mod 8 = 55 \mod 8 = 7 \mod 8$). Ved å bytte $S[1]$ og $S[7]$ fra den nåværende tilstanden til **S**, $[6, 1, 2, 3, 4, 5, 0, 7]$, resulterer det i $[6, 7, 2, 3, 4, 5, 0, 1]$ etter runde 2.
Vi fortsetter med denne prosessen til vi produserer den endelige raden nederst for arrayet **S**, $[6, 4, 1, 0, 3, 7, 5, 2]$.

*Tabell 1: Nøkkelskjematabell*

| Runde   | i   | j   |     | S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] |
| ------- | --- | --- | --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|         |     |     |     |      |      |      |      |      |      |      |      |
| Initial |     | 0   |     | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    |
| 1       | 0   | 6   |     | 6    | 1    | 2    | 3    | 4    | 5    | 0    | 7    |
| 2       | 1   | 7   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 3       | 2   | 2   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 4       | 3   | 3   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 5       | 4   | 3   |     | 6    | 7    | 2    | 0    | 3    | 5    | 4    | 1    |
| 6       | 5   | 6   |     | 6    | 4    | 2    | 0    | 3    | 7    | 5    | 1    |
| 7       | 6   | 1   |     | 6    | 4    | 2    | 0    | 3    | 7    | 5    | 2    |
| 8       | 7   | 2   |     | 6    | 4    | 1    | 0    | 3    | 7    | 5    | 2    |

### Steg 4
Som et fjerde steg, produserer vi **keystream**. Dette er den pseudotilfeldige strengen med en lengde lik meldingen vi ønsker å sende. Denne vil bli brukt til å kryptere den opprinnelige meldingen "SOUP." Ettersom keystream må være like lang som meldingen, trenger vi en som har 4 bytes.
Keystream produseres ved følgende pseudokode:

- Opprett variablene **j**, **i**, og **t**.
- Sett $j = 0$.
- For hver $i$ i klarteksten, start med $i = 1$ og fortsett til $i = 4$, produseres hver byte av keystream som følger:
    - $j = (j + S[i]) \mod 8$
    - Bytt om $S[i]$ og $S[j]$.
    - $t = (S[i] + S[j]) \mod 8$
    - Den $i^{te}$ byten av keystream = $S[t]$

Du kan følge beregningene i *Tabell 2*.

Den opprinnelige tilstanden til **S** er $S = [6, 4, 1, 0, 3, 7, 5, 2]$. Ved å sette $i = 1$, blir verdien av **j** 4 ($j = (j + S[i]) \mod 8 = (0 + 4) \mod 8 = 4$). Vi bytter deretter om $S[1]$ og $S[4]$ for å produsere transformasjonen av **S** i den andre raden, $[6, 3, 1, 0, 4, 7, 5, 2]$. Verdien av **t** blir deretter 7 ($t = (S[i] + S[j]) \mod 8 = (3 + 4) \mod 8 = 7$). Til slutt er byten for keystream $S[7]$, eller 2.

Vi fortsetter deretter å produsere de andre bytene til vi har følgende fire byter: 2, 6, 3, og 7. Hver av disse bytene kan deretter brukes til å kryptere hver bokstav i klarteksten, "SOUP".

For å starte, ved å bruke en ASCII-tabell, kan vi se at “SOUP” kodet av de desimale verdiene til de underliggende byte-strengene er “83 79 85 80”. Kombinasjon med keystream “2 6 3 7” gir “85 85 88 87”, som forblir det samme etter en modulo 256-operasjon. I ASCII, er krypteringsteksten “85 85 88 87” lik “UUXW”.

Hva skjer hvis ordet som skal krypteres var lengre enn arrayet **S**? I så fall, fortsetter arrayet **S** bare å transformere på denne måten vist ovenfor for hver byte **i** av klarteksten, til vi har et antall byter i keystream lik antall bokstaver i klarteksten.


*Tabell 2: Generering av Keystream*

| i   | j   | t   | Keystream | S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] |
| --- | --- | --- | --------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|     |     |     |           |      |      |      |      |      |      |      |      |
|     | 0   |     |           | 6    | 4    | 1    | 0    | 3    | 7    | 5    | 2    || 1   | 4   | 7   | 2         | 6    | 3    | 1    | 0    | 4    | 7    | 5    | 2    |
| 2   | 5   | 0   | 6         | 6    | 3    | 7    | 0    | 4    | 1    | 5    | 2    |
| 3   | 5   | 1   | 3         | 6    | 3    | 7    | 1    | 4    | 0    | 5    | 2    |
| 4   | 1   | 7   | 2         | 6    | 4    | 7    | 1    | 3    | 0    | 5    | 2    |

Eksemplet vi nettopp diskuterte er kun en forenklet versjon av **RC4-strømkrypteringen**. Den faktiske RC4-strømkrypteringen har en **S**-matrise på 256 byte i lengde, ikke 8 byte, og en nøkkel som kan være mellom 1 og 256 byte, ikke mellom 1 og 8 byte. Nøkkelmatrisen og nøkkelstrømmene produseres deretter alle med tanke på den 256-byte lange **S**-matrisen. Beregningene blir enormt mer komplekse, men prinsippene forblir de samme. Ved å bruke samme nøkkel, [14,48,9], med standard RC4-kryptering, blir den klartekstlige meldingen "SOUP" kryptert som 67 02 ed df i heksadesimalt format.

En strømkryptering hvor nøkkelstrømmen oppdateres uavhengig av den klartekstlige meldingen eller krypteringsteksten er en **synkron strømkryptering**. Nøkkelstrømmen er kun avhengig av nøkkelen. Klart, RC4 er et eksempel på en synkron strømkryptering, ettersom nøkkelstrømmen ikke har noen relasjon til klarteksten eller krypteringsteksten. Alle våre primitive strømkrypteringer nevnt i forrige kapittel, inkludert skiftkrypteringen, Vigenère-krypteringen, og engangspadden, var også av den synkrone typen.

I motsetning er en **asynkron strømkryptering** en kryptering hvor nøkkelstrømmen produseres av både nøkkelen og tidligere elementer av krypteringsteksten. Denne typen kryptering kalles også en **selvsynkroniserende kryptering**.

Det er viktig at nøkkelstrømmen produsert med RC4 behandles som en engangspad, og du kan ikke produsere nøkkelstrømmen på nøyaktig samme måte neste gang. I stedet for å endre nøkkelen hver gang, er den praktiske løsningen å kombinere nøkkelen med en **nonce** for å produsere bytestrømmen.

## AES med en 128-bit nøkkel
<chapterId>0b30886f-e620-5b8d-807b-9d84685ca8ff</chapterId>

Som nevnt i forrige kapittel, holdt National Institute of Standards and Technology (NIST) en konkurranse mellom 1997 og 2000 for å bestemme en ny symmetrisk krypteringsstandard. **Rijndael-krypteringen** viste seg å være det vinnende bidraget. Navnet er et ordspill på navnene til de belgiske skaperne, Vincent Rijmen og Joan Daemen.
Rijndael-chifferet er et **blokkchiffer**, noe som betyr at det er en kjernealgoritme, som kan brukes med forskjellige spesifikasjoner for nøkkellengder og blokkstørrelser. Du kan deretter bruke den med forskjellige driftsmoduser for å konstruere krypteringsskjemaer.
Komiteen for NIST-konkurransen vedtok en begrenset versjon av Rijndael-chifferet – nemlig en som krever 128-bits blokkstørrelser og nøkkellengder på enten 128 bits, 192 bits eller 256 bits – som en del av **Advanced Encryption Standard (AES)**. Denne begrensede versjonen av Rijndael-chifferet kan også brukes under flere driftsmoduser. Spesifikasjonen for standarden er det som er kjent som **Advanced Encryption Standard (AES)**.

For å vise hvordan Rijndael-chifferet fungerer, kjernen i AES, vil jeg illustrere prosessen for kryptering med en 128-bits nøkkel. Nøkkelstørrelsen har en innvirkning på antall runder som holdes for hver blokk av kryptering. For 128-bits nøkler kreves 10 runder. Med 192 bits og 256 bits, ville det ha vært 12 og 14 runder, henholdsvis.

I tillegg vil jeg anta at AES brukes i **ECB-modus**. Dette gjør fremstillingen litt enklere og spiller ingen rolle for Rijndael-algoritmen. For å være sikker, ECB-modus er ikke sikker i praksis fordi den fører til deterministisk kryptering. Den mest vanlig brukte sikre modusen med AES er **CBC** (Cipher Block Chaining).

La oss kalle nøkkelen $K_0$. Konstruksjonen med de ovennevnte parametrene ser da ut som i *Figur 1*, hvor $M_i$ står for en del av klartekstmeldingen på 128 bits og $C_i$ for en del av krypterteksten på 128 bits. Polstring legges til klarteksten for den siste blokken, hvis klarteksten ikke kan deles jevnt med blokkstørrelsen.

*Figur 1: AES-ECB med en 128-bits nøkkel*

![Figur 1: AES-ECB med en 128-bits nøkkel](assets/Figure5-1.webp "Figur 1: AES-ECB med en 128-bits nøkkel")

Hver 128-bits tekstblokk går gjennom ti runder i Rijndael-krypteringsskjemaet. Dette krever en separat rundnøkkel for hver runde ($K_1$ til $K_{10}$). Disse produseres for hver runde fra den opprinnelige 128-bits nøkkelen $K_0$ ved hjelp av en **nøkkelekspansjonsalgoritme**. Derfor, for hver tekstblokk som skal krypteres, vil vi bruke den opprinnelige nøkkelen $K_0$ samt ti separate rundnøkler. Merk at disse samme 11 nøklene brukes for hver 128-bits blokk av klartekst som krever kryptering.

Nøkkelekspansjonsalgoritmen er lang og kompleks. Å arbeide gjennom den har liten didaktisk nytte. Du kan se gjennom nøkkelekspansjonsalgoritmen på egen hånd, hvis du ønsker. Når rundnøklene er produsert, vil Rijndael-chifferet manipulere den første 128-bits blokken av klartekst, $M_1$, som sett i *Figur 2*. Vi vil nå gå gjennom disse stegene.

*Figur 2: Manipulasjonen av $M_1$ med Rijndael-chifferet:*

**Runde 0:**
- XOR $M_1$ og $K_0$ for å produsere $S_0$

---

**Runde n for n = {1,...,9}:**
- XOR $S_{n-1}$ og $K_n$
- Byte-substitusjon
- Skift rader
- Miks kolonner
- XOR $S$ og $K_n$ for å produsere $S_n$

---

**Runde 10:**
- XOR $S_9$ og $K_{10}$ - Byte-substitusjon
- Flytt rader
- XOR $S$ og $K_{10}$ for å produsere $S_{10}$
- $S_{10}$ = $C_1$

### Runde 0

Runde 0 av Rijndael-chifferet er grei. En matrise $S_0$ produseres ved en XOR-operasjon mellom 128-bits klarteksten og den private nøkkelen. Det vil si,

- $S_0 = M_1 \oplus K_0$

### Runde 1

I runde 1 kombineres matrisen $S_0$ først med rundenøkkelen $K_1$ ved hjelp av en XOR-operasjon. Dette produserer en ny tilstand av $S$.

For det andre utføres **byte-substitusjons**operasjonen på den nåværende tilstanden av $S$. Det fungerer ved å ta hver byte av 16-byte $S$-matrisen og erstatte den med en byte fra en matrise kalt **Rijndaels S-boks**. Hver byte har en unik transformasjon, og en ny tilstand av $S$ produseres som et resultat. Rijndaels S-boks vises i *Figur 3*.

*Figur 3: Rijndaels S-Boks*

|     | 00  | 01  | 02  | 03  | 04  | 05  | 06  | 07  | 08  | 09  | 0A  | 0B  | 0C  | 0D  | 0E  | 0F  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00  | 63  | 7C  | 77  | 7B  | F2  | 6B  | 6F  | C5  | 30  | 01  | 67  | 2B  | FE  | D7  | AB  | 76  |
| 10  | CA  | 82  | C9  | 7D  | FA  | 59  | 47  | F0  | AD  | D4  | A2  | AF  | 9C  | A4  | 72  | C0  |
| 20  | B7  | FD  | 93  | 26  | 36  | 3F  | F7  | CC  | 34  | A5  | E5  | F1  | 71  | D8  | 31  | 15  |
| 30  | 04  | C7  | 23  | C3  | 18  | 96  | 05  | 9A  | 07  | 12  | 80  | E2  | EB  | 27  | B2  | 75  |
| 40  | 09  | 83  | 2C  | 1A  | 1B  | 6E  | 5A  | A0  | 52  | 3B  | D6  | B3  | 29  | E3  | 2F  | 84  |
| 50  | 53  | D1  | 00  | ED  | 20  | FC  | B1  | 5B  | 6A  | CB  | BE  | 39  | 4A  | 4C  | 58  | CF  || 60  | D0  | EF  | AA  | FB  | 43  | 4D  | 33  | 85  | 45  | F9  | 02  | 7F  | 50  | 3C  | 9F  | A8  |
| 70  | 51  | A3  | 40  | 8F  | 92  | 9D  | 38  | F5  | BC  | B6  | DA  | 21  | 10  | FF  | F3  | D2  |
| 80  | CD  | 0C  | 13  | EC  | 5F  | 97  | 44  | 17  | C4  | A7  | 7E  | 3D  | 64  | 5D  | 19  | 73  |
| 90  | 60  | 81  | 4F  | DC  | 22  | 2A  | 90  | 88  | 46  | EE  | B8  | 14  | DE  | 5E  | 0B  | DB  |
| A0  | E0  | 32  | 3A  | 0A  | 49  | 06  | 24  | 5C  | C2  | D3  | AC  | 62  | 91  | 95  | E4  | 79  |
| B0  | E7  | C8  | 37  | 6D  | 8D  | D5  | 4E  | A9  | 6C  | 56  | F4  | EA  | 65  | 7A  | AE  | 08  |
| C0  | BA  | 78  | 25  | 2E  | 1C  | A6  | B4  | C6  | E8  | DD  | 74  | 1F  | 4B  | BD  | 8B  | 8A  |
| D0  | 70  | 3E  | B5  | 66  | 48  | 03  | F6  | 0E  | 61  | 35  | 57  | B9  | 86  | C1  | 1D  | 9E  |
| E0  | E1  | F8  | 98  | 11  | 69  | D9  | 8E  | 94  | 9B  | 1E  | 87  | E9  | CE  | 55  | 28  | DF  |
| F0  | 8C  | A1  | 89  | 0D  | BF  | E6  | 42  | 68  | 41  | 99  | 2D  | 0F  | B0  | 54  | BB  | 16  |

Denne S-boksen er et sted hvor abstrakt algebra kommer til anvendelse i Rijndael-chifferet, spesifikt **Galois-feltene**.

For å starte, definerer du hvert mulig byteelement fra 00 til FF som en 8-bits vektor. Hver slik vektor er et element av **Galois-feltet GF(2^8)** hvor det irreduktible polynomet for modulo-operasjonen er $x^8 + x^4 + x^3 + x + 1$. Galois-feltet med disse spesifikasjonene kalles også **Rijndaels endelige felt**.

Videre, for hvert mulig element i feltet, skaper vi det som kalles **Nyberg S-boksen**. I denne boksen kartlegges hver byte til sin **multiplikative invers** (dvs. slik at deres produkt blir 1). Vi kartlegger deretter disse verdiene fra Nyberg S-boksen til Rijndaels S-boks ved hjelp av **affin transformasjon**.

Den tredje operasjonen på **S**-arrayet er **shift rows**-operasjonen. Den tar tilstanden til **S** og lister opp alle de seksten bytene i en matrise. Fyllingen av matrisen starter øverst til venstre og arbeider seg rundt ved å gå fra topp til bunn og deretter, hver gang en kolonne er fylt, forskyve en kolonne til høyre og til toppen.

Når matrisen av **S** har blitt konstruert, blir de fire radene forskjøvet. Den første raden forblir den samme. Den andre raden flyttes en over til venstre. Den tredje flyttes to over til venstre. Den fjerde flyttes tre over til venstre. Et eksempel på prosessen er gitt i *Figur 4*. Den opprinnelige tilstanden til **S** vises på toppen, og den resulterende tilstanden etter shift rows-operasjonen vises under den.

*Figur 4: Shift rows-operasjon*

| F1   | A0   | B1   | 23   |
|------|------|------|------|
| 59   | EF   | 09   | 82   |
| 97   | 01   | B0   | CC   |
| D4   | 72   | 04   | 21   |

| F1   | A0   | B1   | 23   |
|------|------|------|------|
| EF   | 09   | 82   | 59   |
| B0   | CC   | 97   | 01   |
| 21   | D4   | 72   | 04   |


I det fjerde trinnet dukker **Galois-feltene** opp igjen. For å starte, multipliseres hver kolonne av **S**-matrisen med kolonnen av 4 x 4-matrisen sett i *Figur 5*. Men i stedet for å være vanlig matrisemultiplikasjon, er det vektormultiplikasjon **modulo et irreduktibelt polynom**, $x^8 + x^4 + x^3 + x + 1$. De resulterende vektorkoeffisientene representerer de individuelle bitene av en byte.

*Figur 5: Mix columns-matrise*

| 02   | 03   | 01   | 01   |
|------|------|------|------|
| 01   | 02   | 03   | 01   |
| 01   | 01   | 02   | 03   || 03   | 01   | 01   | 02   |

Multiplikasjon av den første kolonnen i **S**-matrisen med 4 x 4-matrisen over gir resultatet i *Figur 6*.

*Figur 6: Multiplikasjon av den første kolonnen:*

$$
\begin{matrix}
02 \cdot F1 + 03 \cdot EF + 01 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 02 \cdot EF + 03 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 01 \cdot EF + 02 \cdot B0 + 03 \cdot 21 \\
03 \cdot F1 + 01 \cdot EF + 01 \cdot B0 + 02 \cdot 21
\end{matrix}
$$

Som et neste steg, må alle leddene i matrisen gjøres om til polynomer. For eksempel representerer F1 1 byte og ville bli $x^7 + x^6 + x^5 + x^4 + 1$, og 03 representerer 1 byte og ville bli $x + 1$.

Alle multiplikasjonene utføres deretter **modulo** $x^8 + x^4 + x^3 + x + 1$. Dette resulterer i tillegg av fire polynomer i hver av de fire cellene i kolonnen. Etter å ha utført disse tilleggene **modulo 2**, ender du opp med fire polynomer. Hver av disse polynomene representerer en 8-bits streng, eller 1 byte, av **S**. Vi vil ikke utføre alle disse beregningene her på matrisen i *Figur 6* ettersom de er omfattende.

Når den første kolonnen har blitt behandlet, behandles de andre tre kolonnene i **S**-matrisen på samme måte. Til slutt vil dette gi en matrise med seksten bytes som kan transformeres til en rekke.

Som et siste steg kombineres rekken **S** med rundnøkkelen igjen i en **XOR**-operasjon. Dette produserer tilstanden $S_1$. Det vil si,

- $S_1 = S \oplus K_0$

### Runder 2 til 10

Rundene 2 til 9 er bare en gjentakelse av runde 1, *mutatis mutandis*. Den siste runden ser veldig lik ut som de foregående rundene, bortsett fra at **mix columns**-steget er eliminert. Det vil si, runde 10 utføres som følger:

- $S_9 \oplus K_{10}$
- Byte-substitusjon
- Shift Rows
- $S_{10} = S \oplus K_{10}$

Tilstanden $S_{10}$ er nå satt til $C_1$, de første 128 bitene av krypteringsteksten. Ved å fortsette gjennom de gjenværende 128-bits plaintext-blokkene oppnås den fullstendige krypteringsteksten **C**.

### Operasjonene i Rijndael-chifferet

Hva er begrunnelsen bak de forskjellige operasjonene sett i Rijndael-chifferet?

Uten å gå inn på detaljene, vurderes krypteringsskjemaer på grunnlag av i hvilken grad de skaper forvirring og spredning. Hvis krypteringsskjemaet har en høy grad av **forvirring**, betyr det at krypteringsteksten ser drastisk annerledes ut enn plaintext. Hvis krypteringsskjemaet har en høy grad av **spredning**, betyr det at enhver liten endring i plaintext produserer en drastisk annerledes krypteringstekst.
Begrunnelsen for operasjonene bak Rijndael-chifferet er at de produserer både en høy grad av forvirring og spredning. Forvirringen produseres av byte-substitusjonsoperasjonen, mens spredningen produseres av operasjonene for å skifte rader og blande kolonner.
# Asymmetrisk kryptografi
<partId>868bd9dd-6e1c-5ea9-9ece-54affc13ba05</partId>

## Problemet med nøkkeldistribusjon og -forvaltning
<chapterId>1bb651ba-689a-5a89-a7d3-0b9cc3b694f7</chapterId>

Som med symmetrisk kryptografi, kan asymmetriske ordninger brukes for å sikre både hemmelighold og autentisering. I motsetning til dette, benytter disse ordningene seg imidlertid av to nøkler i stedet for én: en privat og en offentlig nøkkel.

Vi starter vår undersøkelse med oppdagelsen av asymmetrisk kryptografi, spesielt problemene som førte til den. Deretter diskuterer vi hvordan asymmetriske ordninger for kryptering og autentisering fungerer på et høyt nivå. Vi introduserer deretter hash-funksjoner, som er nøkkelen til å forstå asymmetriske autentiseringsskjemaer, og som også har relevans i andre kryptografiske sammenhenger, som for de hash-baserte meldingsautentiseringskodene vi diskuterte i Kapittel 4.

___

Anta at Bob ønsker å kjøpe en ny regnjakke fra Jim’s Sporting Goods, en nettbasert sportsutstyrsforhandler med millioner av kunder i Nord-Amerika. Dette vil være hans første kjøp fra dem, og han ønsker å bruke sitt kredittkort. Så, Bob må først opprette en konto hos Jim’s Sporting Goods, noe som krever at han sender over personlige detaljer som sin adresse og kredittkortinformasjon. Deretter kan han gå gjennom trinnene som er nødvendige for å kjøpe regnjakken.

Bob og Jim’s Sporting Goods vil ønske å sikre at deres kommunikasjon er sikker gjennom hele denne prosessen, med tanke på at internett er et åpent kommunikasjonssystem. De vil for eksempel sikre at ingen potensielle angripere kan få tak i Bobs kredittkort- og adresseinformasjon, og at ingen potensielle angripere kan gjenta hans kjøp eller lage falske kjøp på hans vegne.

Et avansert autentisert krypteringsskjema som diskutert i forrige kapittel kunne helt sikkert gjøre kommunikasjonen mellom Bob og Jim’s Sporting Goods sikker. Men det er klart praktiske hindringer for å implementere et slikt skjema.

For å illustrere disse praktiske hindringene, anta at vi levde i en verden der kun verktøyene for symmetrisk kryptografi eksisterte. Hva kunne da Jim’s Sporting Goods og Bob gjøre for å sikre sikker kommunikasjon?

Under disse omstendighetene ville de stå overfor betydelige kostnader for å kommunisere sikkert. Ettersom internett er et åpent kommunikasjonssystem, kan de ikke bare utveksle et sett med nøkler over det. Derfor må Bob og en representant for Jim’s Sporting Goods møtes personlig for å utveksle nøkler.

En mulighet er at Jim’s Sporting Goods oppretter spesielle nøkkelutvekslingssteder, hvor Bob og andre nye kunder kan hente et sett med nøkler for sikker kommunikasjon. Dette ville åpenbart komme med betydelige organisatoriske kostnader og sterkt redusere effektiviteten som nye kunder kan gjøre kjøp på.

Alternativt kan Jim’s Sporting Goods sende Bob et par nøkler med en høyt betrodd budbringer. Dette er sannsynligvis mer effektivt enn å organisere nøkkelutvekslingssteder. Men dette ville fortsatt komme med betydelige kostnader, spesielt hvis mange kunder bare gjør ett eller noen få kjøp.

Videre tvinger et symmetrisk skjema for autentisert kryptering også Jim’s Sporting Goods til å lagre separate sett med nøkler for alle sine kunder. Dette ville være en betydelig praktisk utfordring for tusenvis av kunder, for ikke å snakke om millioner.
For å forstå dette siste punktet, anta at Jims Sportsutstyr gir hver kunde det samme paret med nøkler. Dette ville tillate hver kunde – eller hvem som helst som kunne få tak i dette nøkkelparet – å lese og til og med manipulere all kommunikasjon mellom Jims Sportsutstyr og kundene. Da kunne du like gjerne la være å bruke kryptografi i det hele tatt i kommunikasjonen din.
Selv å gjenta et sett med nøkler for bare noen få kunder er en forferdelig sikkerhetspraksis. Enhver potensiell angriper kunne forsøke å utnytte den funksjonen i ordningen (husk at angripere antas å vite alt om en ordning bortsett fra nøklene, i samsvar med Kerckhoffs' prinsipp.)

Så, Jims Sportsutstyr måtte lagre et par nøkler for hver kunde, uavhengig av hvordan disse nøkkelparene blir distribuert. Dette presenterer klart flere praktiske problemer.

- Jims Sportsutstyr måtte lagre millioner av nøkkelpar, ett sett for hver kunde.
- Disse nøklene måtte sikres ordentlig, ettersom de ville være et sikkert mål for hackere. Ethvert sikkerhetsbrudd ville kreve gjentakelse av kostbare nøkkelutvekslinger, enten på spesielle nøkkelutvekslingssteder eller via bud.
- Enhver kunde hos Jims Sportsutstyr måtte trygt lagre et par nøkler hjemme. Tap og tyverier vil forekomme, noe som krever en gjentakelse av nøkkelutvekslinger. Kunder måtte også gå gjennom denne prosessen for alle andre nettbutikker eller andre typer enheter de ønsker å kommunisere og handle med over internett.

Disse to hovedutfordringene som nettopp ble beskrevet, var veldig grunnleggende bekymringer frem til slutten av 1970-tallet. De var kjent som **nøkkeldistribusjonsproblemet** og **nøkkelhåndteringsproblemet**, henholdsvis.

Disse problemene hadde alltid eksistert, selvfølgelig, og ofte skapt hodebry i fortiden. Militære styrker, for eksempel, måtte konstant distribuere bøker med nøkler for sikker kommunikasjon til personell i felt med store risikoer og kostnader. Men disse problemene ble verre ettersom verden i økende grad beveget seg mot en av langdistanse, digital kommunikasjon, spesielt for ikke-statlige enheter.

Hvis disse problemene ikke hadde blitt løst på 1970-tallet, ville effektiv og sikker handel hos Jims Sportsutstyr sannsynligvis ikke ha eksistert. Faktisk ville mesteparten av vår moderne verden med praktisk og sikker e-post, nettbank og shopping sannsynligvis bare være en fjern fantasi. Noe som i det hele tatt lignet på Bitcoin kunne ikke ha eksistert i det hele tatt.

Så, hva skjedde på 1970-tallet? Hvordan er det mulig at vi kan gjøre kjøp på nettet umiddelbart og sikkert surfe på World Wide Web? Hvordan er det mulig at vi kan sende Bitcoins øyeblikkelig over hele verden fra våre smarttelefoner?

## Nye retninger i kryptografi
<chapterId>7a9dd9a3-496e-5f9d-93e0-b5028a7dd0f1</chapterId>

På 1970-tallet hadde nøkkeldistribusjons- og nøkkelhåndteringsproblemene fanget oppmerksomheten til en gruppe amerikanske akademiske kryptografer: Whitfield Diffie, Martin Hellman og Ralph Merkle. Til tross for alvorlig skepsis fra flertallet av deres kolleger, våget de seg til å utvikle en løsning på det.

Minst én primær motivasjon for deres foretak var forutseenheten om at åpen datamaskinkommunikasjon ville påvirke vår verden dyptgående. Som Diffie og Hellman bemerker i 1976,
Utviklingen av datamaskinstyrte kommunikasjonsnettverk lover enkel og billig kontakt mellom mennesker eller datamaskiner på motsatte sider av verden, og erstatter det meste av post og mange reiser med telekommunikasjon. For mange applikasjoner må disse kontaktene gjøres sikre mot både avlytting og injeksjon av illegitime meldinger. For øyeblikket henger imidlertid løsningen på sikkerhetsproblemer langt etter andre områder av kommunikasjonsteknologi. *Samtidskryptografi klarer ikke å møte kravene, i den forstand at bruken ville pålegge systembrukerne så alvorlige ulemper, at mange av fordelene med teleprosessering ville bli eliminert.* [1]

Utholdenheten til Diffie, Hellman og Merkle betalte seg. Den første publiseringen av resultatene deres var en artikkel av Diffie og Hellman i 1976 med tittelen "New Directions in Cryptography." I den presenterte de to originale måter å adressere nøkkeldistribusjons- og nøkkelhåndteringsproblemene på.

Den første løsningen de tilbød var et fjern *nøkkelutvekslingsprotokoll*, det vil si et sett med regler for utveksling av en eller flere symmetriske nøkler over en usikker kommunikasjonskanal. Denne protokollen er nå kjent som *Diffie-Hellman nøkkelutveksling* eller *Diffie-Hellman-Merkle nøkkelutveksling*. [2]

Med Diffie-Hellman nøkkelutveksling utveksler to parter først noe informasjon offentlig på en usikker kanal som Internett. På grunnlag av den informasjonen skaper de deretter, uavhengig av hverandre, en symmetrisk nøkkel (eller et par symmetriske nøkler) for sikker kommunikasjon. Selv om begge parter skaper sine nøkler uavhengig, sikrer informasjonen de delte offentlig at denne nøkkelskapingsprosessen gir samme resultat for dem begge.

Viktig er det at mens alle kan observere informasjonen som utveksles offentlig av partene over den usikre kanalen, kan bare de to partene som engasjerer seg i informasjonsutvekslingen skape symmetriske nøkler fra den.

Dette høres selvfølgelig helt motintuitivt ut. Hvordan kan to parter utveksle noe informasjon offentlig som bare vil tillate dem å skape symmetriske nøkler fra den? Hvorfor ville ikke noen andre som observerer informasjonsutvekslingen være i stand til å skape de samme nøklene?

Det stoler på noe vakkert matematikk selvfølgelig. Diffie-Hellman nøkkelutveksling fungerer via en enveisfunksjon med en luke. La oss diskutere betydningen av disse to begrepene etter tur.

Anta at du er gitt en funksjon $f(x)$ og resultatet $f(a) = y$, hvor $a$ er en bestemt verdi for $x$. Vi sier at $f(x)$ er en **enveisfunksjon** hvis det er lett å beregne verdien $y$ når man er gitt $a$ og $f(x)$, men det er beregningsmessig uoverkommelig å beregne verdien $a$ når man er gitt $y$ og $f(x)$. Navnet **enveisfunksjon**, kommer selvfølgelig av at en slik funksjon bare er praktisk å beregne i én retning.

Noen enveisfunksjoner har det som er kjent som en **luke**. Mens det praktisk talt er umulig å beregne $a$ gitt bare $y$ og $f(x)$, er det et bestemt stykke informasjon $Z$ som gjør det beregningsmessig gjennomførbart å beregne $a$ fra $y$. Dette stykket informasjon $Z$ er kjent som **luken**. Enveisfunksjoner som har en luke er kjent som **lukefunksjoner**.
Vi vil ikke gå i detalj om Diffie-Helmann nøkkelutveksling her. Men i hovedsak skaper hver deltaker noe informasjon, hvorav en del deles offentlig og noe forblir hemmelig. Hver part tar deretter sin hemmelige informasjonsbit og den offentlige informasjonen delt av den andre parten for å skape en privat nøkkel. Og på en eller annen mirakuløs måte, vil begge partene ende opp med samme private nøkkel. Enhver part som bare observerer den offentlig delte informasjonen mellom de to partene i en Diffie Helmann nøkkelutveksling, vil ikke kunne gjenskape disse beregningene. De ville trenge den private informasjonen fra en av de to partene for å kunne gjøre det.

Selv om den grunnleggende versjonen av Diffie-Helmann nøkkelutveksling presentert i 1976-papiret ikke er veldig sikker, er sofistikerte versjoner av det grunnleggende protokollen absolutt fortsatt i bruk i dag. Viktigst, hver nøkkelutvekslingsprotokoll i den nyeste versjonen av transportlagets sikkerhetsprotokoll (versjon 1.3) er i hovedsak en beriket versjon av protokollen presentert av Diffie og Hellman i 1976. Transportlagets sikkerhetsprotokoll er den dominerende protokollen for sikkert å utveksle informasjon formatert i henhold til hypertext transfer protocol (http), standarden for utveksling av webinnhold.

Viktig å merke seg er at Diffie-Helmann nøkkelutveksling ikke er et asymmetrisk skjema. Strengt tatt, kan det hevdes at det tilhører området for symmetrisk nøkkelkryptografi. Men ettersom både Diffie-Helmann nøkkelutveksling og asymmetrisk kryptografi er avhengige av enveis tallteoretiske funksjoner med feller, diskuteres de vanligvis sammen.

Den andre måten som Diffie og Helmann tilbød for å adressere nøkkeldistribusjons- og håndteringsproblemet i deres papir fra 1976 var, selvfølgelig, via asymmetrisk kryptografi.

I motsetning til deres presentasjon av Diffie-Hellman nøkkelutveksling, ga de kun de generelle omrissene av hvordan asymmetriske kryptografiske skjemaer plausibelt kunne konstrueres. De tilbød ikke noen enveisfunksjon som spesifikt kunne oppfylle betingelsene som trengs for rimelig sikkerhet i slike skjemaer.

En praktisk implementering av et asymmetrisk skjema ble imidlertid funnet et år senere av tre forskjellige akademiske kryptografer og matematikere: Ronald Rivest, Adi Shamir og Leonard Adleman. [3] Kryptosystemet de introduserte ble kjent som **RSA-kryptosystemet** (etter deres etternavn).

De trappefunksjonene som brukes i asymmetrisk kryptografi (og Diffie Helmann nøkkelutveksling) er alle relatert til to hoved **beregningstunge problemer**: primtallsfaktorisering og beregning av diskrete logaritmer.

**Primtallsfaktorisering** krever, som navnet antyder, å bryte ned et heltall i dets primfaktorer. RSA-problemet er langt det mest kjente eksemplet på et kryptosystem relatert til primtallsfaktorisering.

**Diskret logaritmeproblem** er et problem som oppstår i sykliske grupper. Gitt en generator i en bestemt syklisk gruppe, krever det beregningen av den unike eksponenten som trengs for å produsere et annet element i gruppen fra generatoren.

Skjemaer basert på diskrete logaritmer er avhengige av to hovedtyper av sykliske grupper: multiplikative grupper av heltall og grupper som inkluderer punktene på elliptiske kurver. Den opprinnelige Diffie Helmann nøkkelutvekslingen som presentert i "New Directions in Cryptography" fungerer med en syklisk multiplikativ gruppe av heltall. Bitcoins digitale signaturalgoritme og nylig introduserte Schnorr signaturskjema (2021) er begge basert på diskret logaritmeproblem for en spesiell elliptisk kurve syklisk gruppe.

Videre vil vi gå over til en høy-nivå oversikt over hemmelighold og autentisering i den asymmetriske innstillingen. Før vi gjør det, trenger vi imidlertid å gjøre en kort historisk merknad.
Det virker nå plausibelt at en gruppe britiske kryptografer og matematikere som jobbet for Government Communications Headquarters (GCHQ) hadde gjort oppdagelsene nevnt ovenfor uavhengig av hverandre noen år tidligere. Denne gruppen besto av James Ellis, Clifford Cocks og Malcolm Williamson.
Ifølge deres egne beretninger og det fra GCHQ, var det James Ellis som først kom på konseptet med offentlig nøkkelkryptografi i 1969. Angivelig oppdaget deretter Clifford Cocks RSA-krypteringssystemet i 1973, og Malcolm Williamson konseptet med Diffie-Hellman nøkkelutveksling i 1974. [4] Deres oppdagelser ble imidlertid angivelig ikke avslørt før i 1997, gitt det hemmelige arbeidet som ble utført ved GCHQ.

**Notater:**

[1] Whitfield Diffie og Martin Hellman, “New directions in cryptography,” _IEEE Transactions on Information Theory_ IT-22 (1976), s. 644–654, på s. 644.

[2] Ralph Merkle diskuterer også et nøkkelutvekslingsprotokoll i “Secure communications over insecure channels”, _Communications of the Association for Computing Machinery_, 21 (1978), 294–99. Selv om Merkle faktisk sendte inn denne artikkelen før artikkelen av Diffie og Hellman, ble den publisert senere. Merkles løsning er ikke eksponentielt sikker, i motsetning til Diffie-Hellmans.

[3] Ron Rivest, Adi Shamir, og Leonard Adleman, “A method for obtaining digital signatures and public-key cryptosystems”, _Communications of the Association for Computing Machinery_, 21 (1978), s. 120–26.

[4] En god historie om disse oppdagelsene er gitt av Simon Singh, _The Code Book_, Fourth Estate (London, 1999), Kapittel 6.

## Asymmetrisk kryptering og autentisering
<chapterId>2f6f0f03-3c3d-5025-90f0-5211139bc0cc</chapterId>

En oversikt over **asymmetrisk kryptering** med hjelp av Bob og Alice er gitt i *Figur 1*.

Alice lager først et par nøkler, bestående av én offentlig nøkkel ($K_P$) og én privat nøkkel ($K_S$), hvor “P” i $K_P$ står for “public” (offentlig) og “S” i $K_S$ for “secret” (hemmelig). Hun distribuerer deretter denne offentlige nøkkelen fritt til andre. Vi vil komme tilbake til detaljene i denne distribusjonsprosessen litt senere. Men for nå, anta at hvem som helst, inkludert Bob, kan sikkert skaffe seg Alices offentlige nøkkel $K_P$.

På et senere tidspunkt ønsker Bob å skrive en melding $M$ til Alice. Siden den inneholder sensitiv informasjon, ønsker han at innholdet skal forbli hemmelig for alle unntatt Alice. Så, Bob krypterer først meldingen sin $M$ ved hjelp av $K_P$. Han sender deretter den resulterende krypterte teksten $C$ til Alice, som dekrypterer $C$ med $K_S$ for å produsere den opprinnelige meldingen $M$.

*Figur 1: Asymmetrisk kryptering*

![Figur 1: Asymmetrisk kryptering](assets/Figure6-1.webp "Figur 1: Asymmetrisk kryptering")

Enhver motstander som lytter inn på kommunikasjonen mellom Bob og Alice kan observere $C$. Hun kjenner også $K_P$ og krypteringsalgoritmen $E(\cdot)$. Viktig er det imidlertid at denne informasjonen ikke lar angriperen dekryptere den krypterte teksten $C$ på en gjennomførbar måte. Dekryptering krever spesifikt $K_S$, som angriperen ikke besitter.
Symmetriske krypteringssystemer må generelt være sikre mot en angriper som kan gyldig kryptere klartekstmeldinger (kjent som sikkerhet mot valgt-chiffertekst-angrep). De er imidlertid ikke designet med det eksplisitte formålet å tillate skapelsen av slike gyldige chiffertekster av en angriper eller noen andre. 
Dette står i sterk kontrast til et asymmetrisk krypteringssystem, hvor hele formålet er å tillate hvem som helst, inkludert angripere, å produsere gyldige chiffertekster. Asymmetriske krypteringssystemer kan derfor merkes som **flerbrukerchiffre**.

For å bedre forstå hva som skjer, forestill deg at i stedet for å sende en melding elektronisk, ønsket Bob å sende et fysisk brev i hemmelighet. En måte å sikre hemmelighold på ville være for Alice å sende en sikker hengelås til Bob, men beholde nøkkelen for å låse den opp. Etter å ha skrevet brevet sitt, kunne Bob legge brevet i en boks og lukke den med Alices hengelås. Han kunne deretter sende den låste boksen med meldingen til Alice som har nøkkelen til å låse den opp.

Selv om Bob er i stand til å låse hengelåsen, kan verken han eller noen andre som avskjærer boksen åpne hengelåsen hvis den faktisk er sikker. Bare Alice kan låse den opp og se innholdet i Bobs brev fordi hun har nøkkelen.

Et asymmetrisk krypteringssystem er, grovt sagt, en digital versjon av denne prosessen. Hengelåsen tilsvarer den offentlige nøkkelen og nøkkelen til hengelåsen tilsvarer den private nøkkelen. Fordi hengelåsen er digital, er det imidlertid mye enklere og ikke så kostbart for Alice å distribuere den til hvem som helst som ønsker å sende hemmelige meldinger til henne.

For autentisering i det asymmetriske miljøet, bruker vi **digitale signaturer**. Disse har dermed samme funksjon som meldingsautentiseringskoder i det symmetriske miljøet. En oversikt over digitale signaturer er gitt i *Figur 2*.

Bob lager først et par nøkler, bestående av den offentlige nøkkelen ($K_P$) og den private nøkkelen ($K_S$), og distribuerer sin offentlige nøkkel. Når han ønsker å sende en autentisert melding til Alice, tar han først sin melding $M$ og sin private nøkkel for å lage en **digital signatur** $D$. Bob sender deretter Alice sin melding sammen med den digitale signaturen.

Alice setter inn meldingen, den offentlige nøkkelen, og den digitale signaturen i en **verifiseringsalgoritme**. Denne algoritmen produserer enten **sant** for en gyldig signatur, eller **falsk** for en ugyldig signatur.

En digital signatur er, som navnet tydelig antyder, den digitale ekvivalenten til en skriftlig signatur på brev, kontrakter, og så videre. Faktisk er en digital signatur vanligvis mye mer sikker. Med litt innsats kan du forfalske en skriftlig signatur; en prosess som er gjort enklere av det faktum at skriftlige signaturer ofte ikke nøye verifiseres. En sikker digital signatur, derimot, er, akkurat som en sikker meldingsautentiseringskode, **eksistensielt uforfalskbar**: det vil si, med et sikkert digitalt signatursystem, kan ingen realistisk skape en signatur for en melding som består verifiseringsprosedyren, med mindre de har den private nøkkelen.

*Figur 2: Asymmetrisk autentisering*

![Figur 2: Asymmetrisk autentisering](assets/Figure6-2.webp "Figur 2: Asymmetrisk autentisering")


Som med asymmetrisk kryptering, ser vi en interessant kontrast mellom digitale signaturer og meldingsautentiseringskoder. For sistnevnte kan verifiseringsalgoritmen bare brukes av en av partene som er involvert i den sikre kommunikasjonen. Dette er fordi den krever en privat nøkkel. I det asymmetriske miljøet, derimot, kan hvem som helst verifisere en digital signatur $S$ laget av Bob.
Alt dette gjør digitale signaturer til et ekstremt kraftig verktøy. Det danner grunnlaget, for eksempel, for å skape signaturer på kontrakter som kan verifiseres for juridiske formål. Hvis Bob hadde laget en signatur på en kontrakt i utvekslingen ovenfor, kan Alice vise meldingen $M$, kontrakten og signaturen $S$ til en domstol. Domstolen kan da verifisere signaturen ved å bruke Bobs offentlige nøkkel. [5]
For et annet eksempel, er digitale signaturer en viktig del av sikker programvare og distribusjon av programvareoppdateringer. Denne typen offentlig verifiserbarhet kunne aldri blitt skapt ved bare å bruke meldingsautentiseringskoder.

Som et siste eksempel på kraften til digitale signaturer, vurder Bitcoin. En av de mest vanlige misforståelsene om Bitcoin, spesielt i media, er at transaksjoner er kryptert: de er ikke det. I stedet fungerer Bitcoin-transaksjoner med digitale signaturer for å sikre sikkerheten.

Bitcoins eksisterer i partier kalt ubrukte transaksjonsutganger (eller **UTXO’er**). Anta at du mottar tre betalinger på en bestemt Bitcoin-adresse for 2 bitcoins hver. Teknisk sett har du ikke nå 6 bitcoins på den adressen. I stedet har du tre partier av 2 bitcoins som er låst av et kryptografisk problem assosiert med den adressen. For enhver betaling du gjør, kan du bruke en, to, eller alle tre av disse partiene, avhengig av hvor mye du trenger for transaksjonen.

Beviset på eierskap over ubrukte transaksjonsutganger vises vanligvis via en eller flere digitale signaturer. Bitcoin fungerer nettopp fordi gyldige digitale signaturer på ubrukte transaksjonsutganger er beregningsmessig umulige å lage, med mindre du er i besittelse av den hemmelige informasjonen som kreves for å lage dem.

For øyeblikket inkluderer Bitcoin-transaksjoner åpent all informasjonen som trenger å bli verifisert av deltakerne i nettverket, som opprinnelsen til de ubrukte transaksjonsutgangene som brukes i transaksjonen. Selv om det er mulig å skjule noe av den informasjonen og fortsatt tillate verifisering (som noen alternative kryptovalutaer som Monero gjør), skaper dette også spesielle sikkerhetsrisikoer.

Forvirring oppstår noen ganger over digitale signaturer og skriftlige signaturer fanget digitalt. I det sistnevnte tilfellet fanger du et bilde av din skriftlige signatur og limer den til et elektronisk dokument som en arbeidskontrakt. Dette er imidlertid ikke en digital signatur i den kryptografiske forstand. Sistnevnte er bare et langt tall som bare kan produseres ved å være i besittelse av en privat nøkkel.

Akkurat som i det symmetriske nøkkelmiljøet, kan du også bruke asymmetrisk kryptering og autentiseringsskjemaer sammen. Lignende prinsipper gjelder. Først og fremst bør du bruke forskjellige private-offentlige nøkkelpar for kryptering og laging av digitale signaturer. I tillegg bør du først kryptere en melding og deretter autentisere den.

Viktig, i mange applikasjoner brukes ikke asymmetrisk kryptografi gjennom hele kommunikasjonsprosessen. I stedet vil den typisk bare bli brukt til å *utveksle symmetriske nøkler* mellom partene som de faktisk vil kommunisere med.

Dette er tilfellet, for eksempel, når du kjøper varer på nettet. Ved å kjenne selgerens offentlige nøkkel, kan hun sende deg digitalt signerte meldinger som du kan verifisere for deres autentisitet. På dette grunnlaget kan du følge en av flere protokoller for å utveksle symmetriske nøkler for å kommunisere sikkert.

Hovedgrunnen til hyppigheten av den nevnte tilnærmingen er at asymmetrisk kryptografi er mye mindre effektivt enn symmetrisk kryptografi i å produsere et bestemt sikkerhetsnivå. Dette er en grunn til at vi fortsatt trenger symmetrisk nøkkelkryptografi ved siden av offentlig kryptografi. I tillegg er symmetrisk nøkkelkryptografi mye mer naturlig i bestemte applikasjoner, som en datamaskinbruker som krypterer sine egne data.

Så hvordan adresserer nøyaktig digitale signaturer og offentlig nøkkelkryptering nøkkeldistribusjons- og nøkkelhåndteringsproblemene?
Det finnes ikke ett enkelt svar her. Asymmetrisk kryptografi er et verktøy, og det finnes ikke bare én måte å bruke dette verktøyet på. Men la oss ta vårt tidligere eksempel fra Jims Sportsutstyr for å vise hvordan problemene vanligvis ville blitt adressert i dette eksemplet.
For å starte, ville Jims Sportsutstyr sannsynligvis henvende seg til en **sertifikatmyndighet**, en organisasjon som støtter distribusjon av offentlige nøkler. Sertifikatmyndigheten ville registrere noen detaljer om Jims Sportsutstyr og gi dem en offentlig nøkkel. Den ville deretter sende Jims Sportsutstyr et sertifikat, kjent som et **TLS/SSL-sertifikat**, med Jims Sportsutstyrs offentlige nøkkel digitalt signert ved bruk av sertifikatmyndighetens egen offentlige nøkkel. På denne måten bekrefter sertifikatmyndigheten at en spesifikk offentlig nøkkel faktisk tilhører Jims Sportsutstyr.

Nøkkelen til å forstå denne prosessen med TLS/SSL-sertifikater er at, selv om du generelt ikke vil ha Jims Sportsutstyrs offentlige nøkkel lagret noe sted på datamaskinen din, er de offentlige nøklene til anerkjente sertifikatmyndigheter faktisk lagret i nettleseren din eller i operativsystemet ditt. Disse er lagret i det som kalles **rot-sertifikater**.

Derfor, når Jims Sportsutstyr gir deg sitt TLS/SSL-sertifikat, kan du verifisere sertifikatmyndighetens digitale signatur via et rot-sertifikat i nettleseren din eller operativsystemet. Hvis signaturen er gyldig, kan du være relativt sikker på at den offentlige nøkkelen på sertifikatet faktisk tilhører Jims Sportsutstyr. På dette grunnlaget er det enkelt å sette opp et protokoll for sikker kommunikasjon med Jims Sportsutstyr.

Nøkkeldistribusjon har nå blitt betydelig enklere for Jims Sportsutstyr. Det er ikke vanskelig å se at nøkkelhåndtering også har blitt betydelig forenklet. I stedet for å måtte lagre tusenvis av nøkler, trenger Jims Sportsutstyr bare å lagre en privat nøkkel som lar dem lage signaturer for den offentlige nøkkelen på sitt SSL-sertifikat. Hver gang en kunde kommer til Jims Sportsutstyrs nettsted, kan de etablere en sikker kommunikasjonssesjon fra denne offentlige nøkkelen. Kunder trenger heller ikke å lagre noen informasjon (annet enn de offentlige nøklene til anerkjente sertifikatmyndigheter i deres operativsystem og nettleser).

**Notater:**

[5] Ethvert forsøk på å oppnå ikke-avvisning, det andre temaet vi diskuterte i Kapittel 1, vil i sin grunnleggende form trenge å involvere digitale signaturer.

## Hash-funksjoner
<chapterId>ea8327ab-b0e3-5635-941c-4b51f396a648</chapterId>

Hash-funksjoner er allestedsnærværende i kryptografi. De er verken symmetriske eller asymmetriske ordninger, men faller inn i en egen kryptografisk kategori.

Vi kom allerede over hash-funksjoner i Kapittel 4 med opprettelsen av hash-baserte autentiseringsmeldinger. De er også viktige i konteksten av digitale signaturer, selv om det er av en litt annen grunn: Digitale signaturer er nemlig typisk laget over hash-verdien av en (kryptert) melding, snarere enn den faktiske (krypterte) meldingen. I denne seksjonen vil jeg tilby en mer grundig introduksjon av hash-funksjoner.

La oss starte med å definere en hash-funksjon. En **hash-funksjon** er enhver effektivt beregnbar funksjon som tar inndata av vilkårlig størrelse og gir utdata med fast lengde.

En **kryptografisk hash-funksjon** er bare en hash-funksjon som er nyttig for applikasjoner i kryptografi. Utdataene fra en kryptografisk hash-funksjon kalles typisk **hash**, **hash-verdi**, eller **meldingssammendrag**.

I konteksten av kryptografi refererer "hash-funksjon" typisk til en kryptografisk hash-funksjon. Jeg vil adoptere den praksisen heretter.
Et eksempel på en populær hash-funksjon er **SHA-256** (secure hash algorithm 256). Uavhengig av størrelsen på inndata (f.eks., 15 bit, 100 bit, eller 10 000 bit), vil denne funksjonen gi en 256-bit hashverdi. Nedenfor kan du se noen eksempelutdata fra SHA-256-funksjonen.
“Hello”: `185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969`

“52398”: `a3b14d2bf378c1bd47e7f8eaec63b445150a3d7a80465af16dd9fd319454ba90`

“Kryptografi er gøy”: `3cee2a5c7d2cc1d62db4893564c34ae553cc88623992d994e114e344359b146c`

Alle utdataene er nøyaktig 256 bit skrevet ut i heksadesimalt format (hver heksadesimal siffer kan representeres med fire binære siffer). Så selv om du hadde satt inn Tolkiens *Ringenes Herre* bok i SHA-256-funksjonen, ville utdataen fortsatt være 256 bit.

Hash-funksjoner som SHA-256 brukes til ulike formål i kryptografi. Hvilke egenskaper som kreves fra en hash-funksjon avhenger virkelig av konteksten til en spesifikk applikasjon. Det er to hovedegenskaper som generelt er ønsket av hash-funksjoner i kryptografi: [6]

1.	Kollisjonsresistens
2.	Skjuling

En hash-funksjon $H$ sies å være **kollisjonsresistent** hvis det er uoverkommelig å finne to verdier, $x$ og $y$, slik at $x \neq y$, men $H(x) = H(y)$.

Kollisjonsresistente hash-funksjoner er viktige, for eksempel, i verifiseringen av programvare. Anta at du ønsket å laste ned Windows-utgaven av Bitcoin Core 0.21.0 (en serverapplikasjon for behandling av Bitcoin-nettverkstrafikk). Hovedtrinnene du måtte ta for å verifisere programvarens legitimitet, er som følger:

1.	Du må først laste ned og importere de offentlige nøklene til en eller flere bidragsytere til Bitcoin Core inn i programvare som kan verifisere digitale signaturer (f.eks. Kleopetra). Du kan finne disse offentlige nøklene [her](https://github.com/bitcoin/bitcoin/blob/master/contrib/builder-keys/keys.txt). Det anbefales at du verifiserer Bitcoin Core-programvaren med de offentlige nøklene fra flere bidragsytere.
2.	Deretter må du verifisere de offentlige nøklene som du importerte. Minst ett trinn du bør ta er å verifisere at de offentlige nøklene du fant er de samme som publisert på ulike andre steder. Du kan for eksempel konsultere de personlige nettsidene, Twitter-sidene, eller Github-sidene til personene hvis offentlige nøkler du importerte. Vanligvis gjøres denne sammenligningen av offentlige nøkler ved å sammenligne en kort hash av den offentlige nøkkelen kjent som et fingeravtrykk.
3.	Deretter må du laste ned den kjørbare filen for Bitcoin Core fra deres [nettsted](www.bitcoincore.org). Det vil være pakker tilgjengelig for Linux, Windows og MAC operativsystemer.
4.	Deretter må du finne to utgivelsesfiler. Den første inneholder den offisielle SHA-256-hashen for den nedlastede kjørbare filen sammen med hashene over alle de andre pakkene som ble utgitt. En annen utgivelsesfil vil inneholde signaturer fra ulike bidragsytere over utgivelsesfilen med pakkens hasher. Begge disse utgivelsesfilene bør være lokalisert på Bitcoin Core-nettstedet.
5. Neste steg er å beregne SHA-256-hashen av den kjørbare filen du lastet ned fra Bitcoin Core-nettstedet på din egen datamaskin. Deretter sammenligner du dette resultatet med det offisielle pakkehashet for den kjørbare filen. De bør være identiske.

6. Til slutt må du verifisere at en eller flere av de digitale signaturene over utgivelsesfilen med de offisielle pakkehashene faktisk tilsvarer en eller flere offentlige nøkler du har importert (utgivelser av Bitcoin Core er ikke alltid signert av alle). Dette kan du gjøre med en applikasjon som Kleopetra.

Denne prosessen med programvareverifisering har to hovedfordeler. For det første sikrer den at det ikke var noen feil i overføringen mens du lastet ned fra Bitcoin Cores nettsted. For det andre sikrer den at ingen angripere kunne ha fått deg til å laste ned modifisert, ondsinnet kode, enten ved å hacke Bitcoin Core-nettstedet eller ved å avlytte trafikken.

Hvordan beskytter den ovennevnte programvareverifiseringsprosessen mot disse problemene?

Hvis du nøye har verifisert de offentlige nøklene du importerte, kan du være ganske sikker på at disse nøklene faktisk er deres og ikke har blitt kompromittert. Gitt at digitale signaturer har eksistensiell uforgjengelighet, vet du at bare disse bidragsyterne kunne ha laget en digital signatur over de offisielle pakkehashene på utgivelsesfilen.

Anta at signaturene på utgivelsesfilen du lastet ned sjekker ut. Du kan nå sammenligne hashverdien du beregnet lokalt for den kjørbare Windows-filen du lastet ned med den som er inkludert i den riktig signerte utgivelsesfilen. Siden du vet at SHA-256 hashfunksjonen er kollisjonsresistent, betyr en match at din kjørbare fil er nøyaktig den samme som den offisielle kjørbare filen.

La oss nå vende oss til den andre vanlige egenskapen til hashfunksjoner: **skjuling**. Enhver hashfunksjon $H$ sies å ha egenskapen av skjuling hvis, for et tilfeldig valgt $x$ fra et veldig stort område, er det uoverkommelig å finne $x$ når man kun er gitt $H(x)$.

Nedenfor kan du se SHA-256-outputen av en melding jeg skrev. For å sikre tilstrekkelig tilfeldighet, inkluderte meldingen en tilfeldig generert streng med tegn på slutten. Gitt at SHA-256 har skjulingsegenskapen, ville ingen kunne dechiffrere denne meldingen.

- `b194221b37fa4cd1cfce15aaef90351d70de17a98ee6225088b523b586c32ded`

Men jeg vil ikke la deg være i spenning til SHA-256 blir svakere. Den opprinnelige meldingen jeg skrev var som følger:

* “Dette er en veldig tilfeldig melding, eller vel, slags tilfeldig. Denne begynnelsesdelen er ikke det, men jeg vil avslutte med noen relativt tilfeldige tegn for å sikre en veldig uforutsigbar melding. XLWz4dVG3BxUWm7zQ9qS”.

En vanlig måte hashfunksjoner med skjulingsegenskapen brukes på er i passordhåndtering (kollisjonsresistens er også viktig for denne applikasjonen). Enhver anstendig nettbasert tjeneste som Facebook eller Google vil ikke lagre passordene dine direkte for å håndtere tilgang til kontoen din. I stedet vil de kun lagre en hash av det passordet. Hver gang du fyller inn passordet ditt i en nettleser, beregnes en hash først. Bare den hashen sendes til tjenesteleverandørens server og sammenlignes med hashen lagret i backend-databasen. Skjulingsegenskapen kan bidra til å sikre at angripere ikke kan gjenopprette det fra hashverdien.
Passordhåndtering via hasher fungerer selvfølgelig bare hvis brukerne faktisk velger vanskelige passord. Egenskapen for skjuling antar at x er valgt tilfeldig fra et veldig stort område. Å velge passord som "1234", "mitt passord", eller din fødselsdato vil ikke gi noen reell sikkerhet. Lange lister over vanlige passord og deres hasher eksisterer, som angripere kan utnytte hvis de noen gang får tak i hashen av passordet ditt. Disse typene angrep er kjent som **ordbokangrep**. Hvis angripere kjenner noen av dine personlige detaljer, kan de også forsøke noen informerte gjetninger. Derfor trenger du alltid lange, sikre passord (helst lange, tilfeldige strenger fra en passordbehandler).
Noen ganger kan en applikasjon trenge en hashfunksjon som har både kollisjonsresistens og skjuling. Men absolutt ikke alltid. Programvareverifiseringsprosessen vi diskuterte, for eksempel, krever bare at hashfunksjonen viser kollisjonsresistens, skjuling er ikke viktig.

Selv om kollisjonsresistens og skjuling er de viktigste egenskapene søkt av hashfunksjoner i kryptografi, kan det i visse applikasjoner også være ønskelig med andre typer egenskaper.

**Notater:**

[6] Terminologien "skjuling" er ikke vanlig språk, men tatt spesifikt fra Arvind Narayanan, Joseph Bonneau, Edward Felten, Andrew Miller, og Steven Goldfeder, *Bitcoin and Cryptocurrency Technologies*, Princeton University Press (Princeton, 2016), Kapittel 1.

# RSA-kryptosystemet
<partId>864dca42-2a8d-530f-bb94-2e1f68b3f411</partId>

## Faktoriseringsproblemet
<chapterId>a31a66e4-52ea-539c-9953-4769ad565d7e</chapterId>

Mens symmetrisk kryptografi vanligvis er ganske intuitivt for de fleste, er dette vanligvis ikke tilfellet med asymmetrisk kryptografi. Selv om du sannsynligvis er komfortabel med den høynivåbeskrivelsen som tilbys i de foregående seksjonene, lurer du sannsynligvis på hva nøyaktig enveisfunksjoner er og hvordan de nøyaktig brukes til å konstruere asymmetriske ordninger.

I dette kapittelet vil jeg fjerne noe av mysteriet rundt asymmetrisk kryptografi, ved å se mer dyptgående på et spesifikt eksempel, nemlig RSA-kryptosystemet. I den første seksjonen vil jeg introdusere faktoriseringsproblemet som RSA-problemet er basert på. Jeg vil deretter dekke en rekke nøkkelresultater fra tallteori. I den siste seksjonen vil vi sette sammen denne informasjonen for å forklare RSA-problemet, og hvordan dette kan brukes til å skape asymmetriske kryptografiske ordninger.

Å legge til denne dybden i vår diskusjon er ikke en enkel oppgave. Det krever å introdusere ganske mange tallteoretiske teoremer og proposisjoner. Men la ikke matematikken avskrekke deg. Å jobbe gjennom denne diskusjonen vil betydelig forbedre din forståelse av hva som ligger til grunn for asymmetrisk kryptografi og er en verdifull investering.

La oss nå først vende oss til faktoriseringsproblemet.

___

Når du multipliserer to tall, si $a$ og $b$, refererer vi til tallene $a$ og $b$ som **faktorer**, og resultatet som **produktet**. Å forsøke å skrive et tall $N$ som multiplikasjonen av to eller flere faktorer kalles **faktorisering** eller **faktorisering**. [1] Du kan kalle ethvert problem som krever dette et **faktoriseringsproblem**.

For rundt 2,500 år siden oppdaget den greske matematikeren Euclid av Alexandria et nøkkelteorem om faktoriseringen av heltall. Det kalles vanligvis **det unike faktoriserings teoremet** og sier følgende:

**Teorem 1**. Ethvert heltall $N$ som er større enn 1 er enten et primtall, eller kan uttrykkes som et produkt av primtallsfaktorer.
Alt det siste delen av denne uttalelsen betyr, er at du kan ta et hvilket som helst ikke-primtall $N$ større enn 1, og skrive det ut som en multiplikasjon av primtall. Nedenfor er flere eksempler på ikke-primtall skrevet som produktet av primtallsfaktorer.
* $18 = 2 \cdot 3 \cdot 3 = 2 \cdot 3^2$
* $84 = 2 \cdot 2 \cdot 3 \cdot 7 = 2^2 \cdot 3 \cdot 7$
* $144 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 3 \cdot 3 = 2^4 \cdot 3^2$

For alle de tre heltallene ovenfor er det relativt enkelt å beregne deres primtallsfaktorer, selv om du bare får oppgitt $N$. Du starter med det minste primtallet, nemlig 2, og ser hvor mange ganger heltallet $N$ er delelig med det. Deretter går du videre til å teste deleligheten av $N$ med 3, 5, 7, og så videre. Du fortsetter denne prosessen til ditt heltall $N$ er skrevet som produktet av kun primtall.

Ta for eksempel heltallet 84. Nedenfor kan du se prosessen for å bestemme dets primtallsfaktorer. Ved hvert trinn tar vi ut den minste gjenværende primtallsfaktoren (til venstre) og bestemmer restleddet som skal faktoriseres. Vi fortsetter til restleddet også er et primtall. Ved hvert trinn vises den nåværende faktoriseringen av 84 på langt høyre.

* Primtallsfaktor = 2: restledd = 42 	($84 = 2 \cdot 42$)
* Primtallsfaktor = 2: restledd = 21 	($84 = 2 \cdot 2 \cdot 21$)
* Primtallsfaktor = 3: restledd = 7 	($84 = 2 \cdot 2 \cdot 3 \cdot 7$)
* Ettersom 7 er et primtall, er resultatet $2 \cdot 2 \cdot 3 \cdot 7$, eller $2^2 \cdot 3 \cdot 7$.

Anta nå at $N$ er veldig stort. Hvor vanskelig ville det være å redusere $N$ til dets primtallsfaktorer?

Det avhenger virkelig av $N$. Anta for eksempel at $N$ er 50,450,400. Selv om dette tallet ser skremmende ut, er ikke beregningene så kompliserte og kan enkelt gjøres for hånd. Som ovenfor, du starter bare med 2 og jobber deg videre. Nedenfor kan du se resultatet av denne prosessen på en lignende måte som ovenfor.

* 2: 25,225,200 	($50,450,400 = 2 \cdot 25,225,200$)  
* 2: 12,612,600 	($50,450,400 = 2^2 \cdot 12,612,600$)  
* 2: 6,306,300 	($50,450,400 = 2^3 \cdot 6,306,300$)  
* 2: 3,153,150 	($50,450,400 = 2^4 \cdot 3,153,150$)  
* 2: 1,576,575 	($50,450,400 = 2^5 \cdot 1,576,575$)
* 3: 525,525 ($50,450,400 = 2^5 \cdot 3 \cdot 525,525$)
* 3: 175,175 ($50,450,400 = 2^5 \cdot 3^2 \cdot 175,175$)
* 5: 35,035 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5 \cdot 35,035$)
* 5: 7,007 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7,007$)
* 7: 1,001 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7 \cdot 1,001$)
* 7: 143 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 143$)
* 11: 13 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 11 \cdot 13$)
* Siden 13 er et primtall, er resultatet $2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 11 \cdot 13$.

Å løse dette problemet for hånd tar litt tid. En datamaskin, selvfølgelig, kunne gjøre alt dette på en brøkdel av et sekund. Faktisk kan en datamaskin ofte faktorisere ekstremt store heltall på en brøkdel av et sekund.

Det er imidlertid visse unntak. Anta at vi først tilfeldig velger to veldig store primtall. Det er vanlig å merke disse med $p$ og $q$, og jeg vil følge den konvensjonen her.

For å være konkret, la oss si at $p$ og $q$ begge er 1024-bits primtall, og at de faktisk krever minst 1024 bits for å bli representert (så den første biten må være 1). Så, for eksempel, kunne ikke 37 være et av primtallene. Du kan absolutt representere 37 med 1024 bits. Men klart *du trenger ikke* så mange bits for å representere det. Du kan representere 37 med hvilken som helst streng som har 6 bits eller mer. (I 6 bits, ville 37 bli representert som $100101$).

Det er viktig å sette pris på hvor store $p$ og $q$ er hvis valgt under de ovennevnte forholdene. Som et eksempel har jeg valgt et tilfeldig primtall som trenger minst 1024 bits for representasjon nedenfor.
* 14 752 173 874 503 595 484 930 006 383 670 759 559 764 562 721 397 166 747 289 220 945 457 932 666 751 048 198 854 920 097 085 690 793 755 254 946 188 163 753 506 778 089 706 699 671 722 089 715 624 760 049 594 106 189 662 669 156 149 028 900 805 928 183 585 427 782 974 951 355 515 394 807 209 836 870 484 558 332 897 443 152 653 214 483 870 992 618 171 825 921 582 253 023 974 514 209 142 520 026 807 636 589

Anta nå at etter å ha valgt tilfeldige primtall $p$ og $q$, multipliserer vi dem for å få et heltall $N$. Dette siste tallet er derfor et 2048-bits tall som krever minst 2048 bits for sin representasjon. Det er mye, mye større enn enten $p$ eller $q$.

Anta at du bare gir en datamaskin $N$, og ber den om å finne de to 1024-bits primfaktorene til $N$. Sannsynligheten for at datamaskinen oppdager $p$ og $q$ er ekstremt liten. Du kan si at det er umulig for alle praktiske formål. Dette gjelder selv om du skulle bruke en superdatamaskin eller til og med et nettverk av superdatamaskiner.

For å starte, anta at datamaskinen forsøker å løse problemet ved å sykle gjennom 1024-bits tall, teste i hvert tilfelle om de er primtall og om de er faktorer av $N$. Mengden av primtall som skal testes er da omtrentlig $1.265 \cdot 10^{305}$. [2]

Selv om du tar alle datamaskinene på planeten og får dem til å forsøke å finne og teste 1024-bits primtall på denne måten, ville en 1 i en milliard sjanse for å lykkes med å finne en primfaktor av $N$ kreve en beregningsperiode mye lengre enn universets alder.

Nå i praksis kan en datamaskin gjøre det bedre enn den grove prosedyren som nettopp er beskrevet. Det finnes flere algoritmer som datamaskinen kan bruke for å komme til en faktorisering raskere. Poenget er imidlertid at selv ved å bruke disse mer effektive algoritmene, er datamaskinens oppgave fortsatt beregningsmessig uoverkommelig. [3]

Viktig er vanskeligheten med faktoriseringen under de nettopp beskrevne forholdene basert på antagelsen om at det ikke finnes noen beregningsmessig effektive algoritmer for å beregne primfaktorer. Vi kan faktisk ikke bevise at en effektiv algoritme ikke eksisterer. Likevel er denne antagelsen veldig plausibel: til tross for omfattende innsats som spenner over hundrevis av år, har vi ennå ikke funnet en slik beregningsmessig effektiv algoritme.

Derfor kan faktoriseringsproblemet, under visse omstendigheter, med rimelighet antas å være et vanskelig problem. Spesielt når $p$ og $q$ er veldig store primtall, er deres produkt $N$ ikke vanskelig å beregne; men faktorisering gitt kun $N$ er praktisk talt umulig.


**Notater:**

[1] Faktorisering kan også være viktig for å jobbe med andre typer matematiske objekter enn tall. For eksempel kan det være nyttig å faktorisere polynomuttrykk som $x^2 - 2x + 1$. I vår diskusjon vil vi kun fokusere på faktorisering av tall, spesifikt heltall.
[2] Ifølge **primtallsteoremet** er antallet av primtall mindre enn eller lik $N$ omtrentlig $N/\ln(N)$. Dette betyr at du kan tilnærme antallet av primtall med lengde 1024 bits ved:
$$ \frac{2^{1024}}{\ln(2^{1024})} - \frac{2^{1023}}{\ln(2^{1023})} $$

...som er omtrentlig $1.265 \times 10^{305}$.

[3] Det samme gjelder for diskrete logaritmeproblemer. Derfor fungerer asymmetriske konstruksjoner med mye større nøkler enn symmetriske kryptografiske konstruksjoner.

## Resultater fra tallteori
<chapterId>23cd2186-8d97-5709-a4a7-b984f1eb9999</chapterId>

Dessverre kan ikke faktoriseringsproblemet brukes direkte for asymmetriske kryptografiske skjemaer. Men vi kan bruke et mer komplekst, men relatert problem til dette formålet: RSA-problemet.

For å forstå RSA-problemet, må vi forstå en rekke teoremer og proposisjoner fra tallteori. Disse er presentert i dette avsnittet i tre underseksjoner: (1) ordenen til N, (2) omvendbarhet modulo N, og (3) Eulers teorem.

Noe av materialet i de tre underseksjonene har allerede blitt introdusert i *Kapittel 3*. Men jeg vil her gjenta det materialet for bekvemmelighet.

### Ordenen til N

Et heltall $a$ er **relativt primt** eller et **relativt primtall** med et heltall $N$, hvis den største felles divisoren mellom dem er 1. Selv om 1 ved konvensjon ikke er et primtall, er det et relativt primtall til hvert heltall (som er $-1$).

For eksempel, vurder tilfellet når $a = 18$ og $N = 37$. Disse er klart relativt primtall. Det største heltallet som deler både 18 og 37 er 1. I motsetning, vurder tilfellet når $a = 42$ og $N = 16$. Disse er klart ikke relativt primtall. Begge tallene er delbare med 2, som er større enn 1.

Vi kan nå definere ordenen til $N$ som følger. Anta at $N$ er et heltall større enn 1. **Ordenen til N** er da antallet av alle relativt primtall med $N$ slik at for hvert relativt primtall $a$, holder følgende betingelse: $1 \leq a < N$.

For eksempel, hvis $N = 12$, da er 1, 5, 7, og 11 de eneste relativt primtallene som møter kravet ovenfor. Derfor er ordenen til 12 lik 4.

Anta at $N$ er et primtall. Da er ethvert heltall mindre enn $N$ men større eller lik 1 relativt primt med det. Dette inkluderer alle elementene i følgende sett: $\{1,2,3,….,N - 1\}$. Derfor, når $N$ er et primtall, er ordenen til $N$ $N - 1$. Dette er uttalt i proposisjon 1, hvor $\phi(N)$ betegner ordenen til $N$.

**Proposisjon 1**. $\phi(N) = N - 1$ når $N$ er et primtall
Anta at $N$ ikke er et primtall. Du kan da beregne dets orden ved hjelp av **Eulers Phi-funksjon**. Selv om beregningen av ordenen til et lite heltall er relativt enkelt, blir Eulers Phi-funksjon spesielt viktig for større heltall. Forslaget til Eulers Phi-funksjon er uttalt nedenfor.
**Teorem 2**. La $N$ være lik $p_1^{e_1} \cdot p_2^{e_2} \cdot \ldots \cdot p_i^{e_i} \cdot \ldots \cdot p_n^{e_n}$, hvor settet $\{p_i\}$ består av alle de distinkte primfaktorene til $N$ og hver $e_i$ indikerer hvor mange ganger primfaktoren $p_i$ forekommer for $N$. Da er

$$\phi(N) = p_1^{e_1 - 1} \cdot (p_1 - 1) \cdot p_2^{e_2 - 1} \cdot (p_2 - 1) \cdot \ldots \cdot p_n^{e_n - 1} \cdot (p_n - 1)$$

**Teorem 2** viser at når du har brutt ned et ikke-primtall $N$ til dets distinkte primfaktorer, er det enkelt å beregne ordenen til $N$.

For eksempel, anta at $N = 270$. Dette er tydeligvis ikke et primtall. Å bryte ned $N$ til dets primfaktorer gir uttrykket: $2 \cdot 3^3 \cdot 5$. Ifølge Eulers Phi-funksjon, er da ordenen til $N$ som følger:

$$\phi(N) = 2^{1 - 1} \cdot (2 - 1) + 3^{3 - 1} \cdot (3 - 1) + 5^{1 - 1} \cdot (5 - 1) = 1 \cdot 1 + 9 \cdot 2 + 1 \cdot 4 = 1 + 18 + 4 = 23$$

Anta videre at $N$ er et produkt av to primtall, $p$ og $q$. **Teorem 2** ovenfor, sier da at ordenen til $N$ er som følger:

$$p^{1 - 1} \cdot (p - 1) \cdot q^{1 - 1} \cdot (q - 1) = (p - 1) \cdot (q - 1)$$

Dette er et nøkkelresultat for RSA-problemet spesielt, og er uttalt i **Forslag 2** nedenfor.

**Forslag 2**. Hvis $N$ er produktet av to primtall, $p$ og $q$, er ordenen til $N$ produktet $(p - 1) \cdot (q - 1)$.

For å illustrere, anta at $N = 119$. Dette heltallet kan faktoriseres til to primtall, nemlig 7 og 17. Derfor antyder Eulers Phi-funksjon at ordenen til 119 er som følger:

$$\phi(119) = (7 - 1) \cdot (17 - 1) = 6 \cdot 16 = 96$$

Med andre ord har heltallet 119 96 koprimtall i området fra 1 til 119. Faktisk inkluderer dette settet alle heltall fra 1 til 119, som ikke er multipler av enten 7 eller 17.
Fra nå av, la oss betegne mengden av relativt primtall som bestemmer ordenen til $N$ som $C_N$. For vårt eksempel der $N = 119$, er settet $C_{119}$ altfor stort til å listes opp fullstendig. Men noen av elementene er som følger:
$$C_{119} = \{1, 2, \dots 6, 8 \dots 13, 15, 16, 18, \dots 33, 35 \dots 96\}$$

### Omvendbarhet modulo N

Vi kan si at et heltall $a$ er **omvendbart modulo N**, hvis det finnes minst ett heltall $b$ slik at $a \cdot b \mod N = 1 \mod N$. Ethvert slikt heltall $b$ refereres til som en **invers** (eller **multiplikativ invers**) av $a$ gitt reduksjon ved modulo $N$.

Anta, for eksempel, at $a = 5$ og $N = 11$. Det finnes mange heltall som du kan multiplisere med 5, slik at $5 \cdot b \mod 11 = 1 \mod 11$. Vurder for eksempel heltallene 20 og 31. Det er lett å se at begge disse heltallene er inverser av 5 for reduksjon modulo 11.

* $5 \cdot 20 \mod 11 = 100 \mod 11 = 1 \mod 11$
* $5 \cdot 31 \mod 11 = 155 \mod 11 = 1 \mod 11$

Selv om 5 har mange inverser reduksjon modulo 11, kan du vise at det bare finnes en enkelt positiv invers av 5 som er mindre enn 11. Faktisk er dette ikke unikt for vårt spesielle eksempel, men et generelt resultat.

**Påstand 3**. Hvis heltallet $a$ er omvendbart modulo $N$, må det være slik at nøyaktig én positiv invers av $a$ er mindre enn $N$. (Så, denne unike inversen av $a$ må komme fra settet $\{1, \dots, N - 1\}$).

La oss betegne den unike inversen av $a$ fra **Påstand 3** som $a^{-1}$. For tilfellet når $a = 5$ og $N = 11$, kan du se at $a^{-1} = 9$, gitt at $5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$.

Merk at du også kan oppnå verdien 9 for $a^{-1}$ i vårt eksempel ved ganske enkelt å redusere enhver annen invers av $a$ ved modulo 11. For eksempel, $20 \mod 11 = 31 \mod 11 = 9 \mod 11$. Så når et heltall $a > N$ er omvendbart modulo $N$, må også $a \mod N$ være omvendbart modulo $N$.

Det er ikke nødvendigvis slik at en invers av $a$ eksisterer reduksjon modulo $N$. Anta, for eksempel, at $a = 2$ og $N = 8$. Det finnes ingen $b$, eller noen $a^{-1}$ spesifikt, slik at $2 \cdot b \mod 8 = 1 \mod 8$. Dette er fordi enhver verdi av $b$ alltid vil produsere et multiplum av 2, så ingen deling med 8 kan noensinne gi en rest som tilsvarer 1.
Hvordan vet vi nøyaktig om et heltall $a$ har en invers for et gitt $N$? Som du kanskje har lagt merke til i eksemplet over, er den største felles divisoren mellom 2 og 8 høyere enn 1, nemlig 2. Og dette er faktisk illustrerende for følgende generelle resultat:
**Proposisjon 4**. En invers eksisterer for et heltall $a$ gitt reduksjon modulo $N$, og spesifikt en unik positiv invers mindre enn $N$, hvis og bare hvis den største felles divisoren mellom $a$ og $N$ er 1 (det vil si, hvis de er relativt primære).

For tilfellet når $a = 5$ og $N = 11$, konkluderte vi med at $a^{-1} = 9$, gitt at $5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$. Det er viktig å merke seg at det motsatte også er sant. Det vil si, når $a = 9$ og $N = 11$, er det slik at $a^{-1} = 5$.

### Eulers teorem

Før vi går videre til RSA-problemet, må vi forstå enda et avgjørende teorem, nemlig **Eulers teorem**. Det sier følgende:

**Teorem 3**. Anta at to heltall $a$ og $N$ er relativt primære. Da er $a^{\phi(N)} \mod N = 1 \mod N$.

Dette er et bemerkelsesverdig resultat, men litt forvirrende i begynnelsen. La oss se på et eksempel for å forstå det.

Anta at $a = 5$ og $N = 7$. Disse er faktisk relativt primære som Eulers teorem krever. Vi vet at ordenen til 7 er lik 6, gitt at 7 er et primtall (se **Proposisjon 1**).

Det Eulers teorem nå sier er at $5^6 \mod 7$ må være lik $1 \mod 7$. Nedenfor er beregningene for å vise at dette faktisk er sant.

* $5^6 \mod 7 = 15,625 \mod 7 = 1 \mod N$

Heltallet 7 deler inn i 15,624 totalt 2,233 ganger. Derfor er resten av å dele 16,625 med 7 er 1.

Videre, ved å bruke Eulers Phi-funksjon, **Teorem 2**, kan du utlede **Proposisjon 5** nedenfor.

**Proposisjon 5**. $\phi(a \cdot b) = \phi(a) \cdot \phi(b)$ for alle positive heltall $a$ og $b$.

Vi vil ikke vise hvorfor dette er tilfellet. Men merk at du allerede har sett bevis på denne proposisjonen ved det faktum at $\phi(p \cdot q) = \phi(p) \cdot \phi(q) = (p - 1) \cdot (q - 1)$ når $p$ og $q$ er primtall, som angitt i **Proposisjon 2**.

Eulers teorem i forbindelse med **Proposisjon 5** har viktige implikasjoner. Se hva som skjer, for eksempel, i uttrykkene nedenfor, der $a$ og $N$ er relativt primære.

* $a^{2 \cdot \phi(N)} \mod N = a^{\phi(N)} \cdot a^{\phi(N)} \mod N = 1 \cdot 1 \mod N = 1 \mod N$
* $a^{\phi(N) + 1} \mod N = a^{\phi(N)} \cdot a^1 \mod N = 1 \cdot a^1 \mod N = a \mod N$
* $a^{8 \cdot \phi(N) + 3} \mod N = a^{8 \cdot \phi(N)} \cdot a^3 \mod N = 1 \cdot a^3 \mod N = a^3 \mod N$

Dermed tillater kombinasjonen av Eulers teorem og **Proposisjon 5** oss å enkelt beregne et antall uttrykk. Generelt kan vi oppsummere innsikten som i **Proposisjon 6**.

**Proposisjon 6**. $a^x \mod N = a^{x \mod \phi(N)}$

Nå må vi sette alt sammen i et vanskelig siste steg.

Akkurat som $N$ har en orden $\phi(N)$ som inkluderer elementene i settet $C_N$, vet vi at heltallet $\phi(N)$ må på sin side også ha en orden og et sett av koprimtall. La oss sette $\phi(N) = R$. Da vet vi at det også finnes en verdi for $\phi(R)$ og et sett av koprimtall $C_R$.

Anta at vi nå velger et heltall $e$ fra settet $C_R$. Vi vet fra **Proposisjon 3** at dette heltallet $e$ kun har en unik positiv invers mindre enn $R$. Det vil si, $e$ har en unik invers fra settet $C_R$. La oss kalle denne inversen $d$. Gitt definisjonen av en invers, betyr dette at $e \cdot d = 1 \mod R$.

Vi kan bruke dette resultatet til å gjøre en uttalelse om vårt opprinnelige heltall $N$. Dette er oppsummert i **Proposisjon 7**.

**Proposisjon 7**. Anta at $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Da må det for ethvert element $a$ i settet $C_N$ være slik at $a^{e \cdot d \mod \phi(N)} = a^{1 \mod \phi(N)} = a \mod N$.

Vi har nå alle de tallteoretiske resultatene som trengs for å klart formulere RSA-problemet.


## RSA-kryptosystemet
<chapterId>0253c2f7-b8a4-5d0e-bd60-812ed6b6c7a9</chapterId>

Vi er nå klare til å formulere RSA-problemet. Anta at du oppretter et sett med variabler bestående av $p$, $q$, $N$, $\phi(N)$, $e$, $d$, og $y$. Kall dette settet $\Pi$. Det opprettes som følger:

1. Generer to tilfeldige primtall $p$ og $q$ av lik størrelse og beregn deres produkt $N$.
2. Beregn ordenen til $N$, $\phi(N)$, ved følgende produkt: $(p - 1) \cdot (q - 1)$.
3. Velg et $e > 2$ slik at det er mindre og koprimt til $\phi(N)$.
4. Beregn $d$ ved å sette $e \cdot d \mod \phi(N) = 1$.
5. Velg en tilfeldig verdi $y$ som er mindre og koprimt til $N$.
RSA-problemet består i å finne en $x$ slik at $x^e = y$, mens man kun får oppgitt et delsett av informasjon om $\Pi$, nemlig variablene $N$, $e$, og $y$. Når $p$ og $q$ er veldig store, typisk anbefales det at de er 1024 bits i størrelse, antas RSA-problemet å være vanskelig. Du kan nå se hvorfor dette er tilfellet gitt den foregående diskusjonen.
En enkel måte å beregne $x$ på når $x^e \mod N = y \mod N$ er rett og slett ved å beregne $y^d \mod N$. Vi vet at $y^d \mod N = x \mod N$ ved følgende beregninger:

$$ y^d \mod N = x^{e \cdot d} \mod N = x^{e \cdot d \mod \phi(N)} \mod N = x^{1 \mod \phi(N)} \mod N = x \mod N. $$

Problemet er at vi ikke kjenner verdien $d$, ettersom den ikke er oppgitt i problemet. Derfor kan vi ikke direkte beregne $y^d \mod N$ for å produsere $x \mod N$.

Vi kan imidlertid være i stand til å indirekte beregne $d$ fra ordenen til $N$, $\phi(N)$, ettersom vi vet at $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Men ifølge antagelsen gir ikke problemet en verdi for $\phi(N)$ heller.

Til slutt kunne ordenen blitt beregnet indirekte med de primtallene $p$ og $q$, slik at vi til slutt kan beregne $d$. Men ifølge antagelsen ble ikke verdiene $p$ og $q$ gitt til oss heller.

Strengt tatt, selv om faktoriseringsproblemet innenfor et RSA-problem er vanskelig, kan vi ikke bevise at RSA-problemet også er vanskelig. Det kan nemlig være andre måter å løse RSA-problemet på enn gjennom faktorisering. Det er imidlertid generelt akseptert og antatt at hvis faktoriseringsproblemet innenfor et RSA-problem er vanskelig, så er også RSA-problemet vanskelig.

Hvis RSA-problemet faktisk er vanskelig, så produserer det en enveisfunksjon med en luke. Funksjonen her er $f(g) = g^e \mod N$. Med kunnskap om $f(g)$, kan hvem som helst enkelt beregne en verdi $y$ for en spesiell $g = x$. Det er imidlertid praktisk talt umulig å beregne en spesiell verdi $x$ kun ved å kjenne verdien $y$ og funksjonen $f(g)$. Unntaket er når du får oppgitt et stykke informasjon $d$, luken. I så fall kan du enkelt beregne $y^d$ for å gi $x$.

La oss gå gjennom et spesifikt eksempel for å illustrere RSA-problemet. Jeg kan ikke velge et RSA-problem som ville bli ansett som vanskelig under de ovennevnte forholdene, ettersom tallene ville være uhåndterlige. I stedet er dette eksemplet bare for å illustrere hvordan RSA-problemet generelt fungerer.

For å starte, anta at du velger to tilfeldige primtall 13 og 31. Så $p = 13$ og $q = 31$. Produktet $N$ av disse to primtallene blir 403. Vi kan enkelt beregne ordenen til 403. Den er lik $(13 - 1) \cdot (31 - 1) = 360$.
Neste, som diktert av trinn 3 i RSA-problemet, må vi velge en relativ prim (coprime) til 360 som er større enn 2 og mindre enn 360. Vi trenger ikke å velge denne verdien tilfeldig. Anta at vi velger 103. Dette er en relativ prim til 360 siden dens største felles divisor med 103 er 1.
Trinn 4 krever nå at vi beregner en verdi $d$ slik at $103 \cdot d \mod 360 = 1$. Dette er ikke en enkel oppgave for hånd når verdien for $N$ er stor. Det krever at vi bruker en prosedyre kalt **det utvidede euklidske algoritmen**.

Selv om jeg ikke viser prosedyren her, gir den verdien 7 når $e = 103$. Du kan verifisere at paret av verdier 103 og 7 faktisk oppfyller den generelle betingelsen $e \cdot d \mod \phi(n) = 1$ gjennom beregningene nedenfor.

* $103 \cdot 7 \mod 360 = 721 \mod 360 = 1 \mod 360$

Viktig, gitt *Proposisjon 4*, vet vi at ingen annen heltall mellom 1 og 360 for $d$ vil produsere resultatet at $103 \cdot d = 1 \mod 360$. I tillegg antyder proposisjonen at å velge en annen verdi for $e$, vil gi en annen unik verdi for $d$.

I trinn 5 av RSA-problemet, må vi velge et positivt heltall $y$ som er en mindre relativ prim til 403. Anta at vi setter $y = 2^{103}$. Eksponentiering av 2 med 103 gir resultatet nedenfor.

* $2^{103} \mod 403 = 10,141,204,801,825,835,211,973,625,643,008 \mod 403 = 349 \mod 403$

RSA-problemet i dette spesielle eksemplet er nå som følger: Du er gitt $N = 403$, $e = 103$, og $y = 349 \mod 403$. Du må nå beregne $x$ slik at $x^{103} = 349 \mod 403$. Det vil si, du må finne at den opprinnelige verdien før eksponentiering med 103 var 2.

Det ville være enkelt (for en datamaskin i det minste) å beregne $x$ hvis vi visste at $d = 7$. I så fall kunne du bare bestemme $x$ som nedenfor.

* $x = y^7 \mod 403 = 349^7 \mod 403 = 630,634,881,591,804,949 \mod 403 = 2 \mod 403$

Problemet er at du ikke har fått informasjonen at $d = 7$. Du kunne selvfølgelig beregne $d$ fra det faktum at $103 \cdot d = 1 \mod 360$. Problemet er at du heller ikke er gitt informasjonen at rekkefølgen av $N = 360$. Til slutt, du kunne også beregne rekkefølgen av 403 ved å beregne følgende produkt: $(p - 1) \cdot (q - 1)$. Men du er heller ikke fortalt at $p = 13$ og $q = 31$.

Selvfølgelig kunne en datamaskin fortsatt løse RSA-problemet for dette eksemplet relativt enkelt, fordi primtallene involvert ikke er store. Men når primtallene blir veldig store, står den overfor en praktisk umulig oppgave.
Vi har nå presentert RSA-problemet, et sett med forhold der det er vanskelig, og den underliggende matematikken. Hvordan hjelper noe av dette med asymmetrisk kryptografi? Spesifikt, hvordan kan vi gjøre vanskeligheten med RSA-problemet under visse forhold til et krypteringssystem eller et digitalt signatursystem?
En tilnærming er å ta RSA-problemet og bygge ordninger på en enkel måte. For eksempel, anta at du genererte et sett med variabler $\Pi$ som beskrevet i RSA-problemet, og sørge for at $p$ og $q$ er tilstrekkelig store. Du setter din offentlige nøkkel lik $(N, e)$ og deler denne informasjonen med verden. Som beskrevet ovenfor, holder du verdiene for $p$, $q$, $\phi(n)$, og $d$ hemmelig. Faktisk er $d$ din private nøkkel.

Alle som ønsker å sende deg en melding $m$ som er et element av $C_N$ kunne enkelt kryptere den som følger: $c = m^e \mod N$. (Krypteringsteksten $c$ her er ekvivalent med verdien $y$ i RSA-problemet.) Du kan enkelt dekryptere denne meldingen ved bare å beregne $c^d \mod N$.

Du kan forsøke å lage et digitalt signatursystem på samme måte. Anta at du ønsker å sende noen en melding $m$ med en digital signatur $S$. Du kunne bare sette $S = m^d \mod N$ og sende paret $(m,S)$ til mottakeren. Alle kan verifisere den digitale signaturen bare ved å sjekke om $S^e \mod N = m \mod N$. En angriper, derimot, ville ha en virkelig vanskelig tid med å skape en gyldig $S$ for en melding, gitt at de ikke besitter $d$.

Dessverre er det ikke så enkelt å gjøre RSA-problemet, som i seg selv er et vanskelig problem, til et kryptografisk skjema. For det enkle krypteringsskjemaet, kan du bare velge koprimtall av $N$ som dine meldinger. Det etterlater oss ikke med mange mulige meldinger, absolutt ikke nok for standard kommunikasjon. I tillegg må disse meldingene velges tilfeldig. Det virker noe upraktisk. Til slutt vil enhver melding som er valgt to ganger gi nøyaktig samme krypteringstekst. Dette er ekstremt uønsket i ethvert krypteringsskjema og møter ikke noen strenge moderne standardnotioner av sikkerhet i kryptering.

Problemene blir enda verre for vårt enkle digitale signaturskjema. Som det står, kan enhver angriper enkelt forfalske digitale signaturer bare ved først å velge et koprimtall av $N$ som signaturen og deretter beregne den tilsvarende opprinnelige meldingen. Dette bryter klart kravet om eksistensiell uforfalskbarhet.

Likevel, med å legge til litt smart kompleksitet, kan RSA-problemet brukes til å skape et sikkert offentlig nøkkelkrypteringsskjema samt et sikkert digitalt signaturskjema. Vi vil ikke gå inn på detaljene i slike konstruksjoner her. [4] Viktig, imidlertid, denne tilleggs kompleksiteten endrer ikke det grunnleggende underliggende RSA-problemet som disse skjemaene er basert på.


**Notater:**

[4] Se, for eksempel, Jonathan Katz og Yehuda Lindell, _Introduction to Modern Cryptography_, CRC Press (Boca Raton, FL: 2015), s. 410–32 om RSA-kryptering og s. 444–41 for RSA digitale signaturer.