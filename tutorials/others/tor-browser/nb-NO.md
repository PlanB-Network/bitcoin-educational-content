---
name: Tor Browser
description: Hvordan bruke Tor Browser?
---
![cover](assets/cover.webp)

Som navnet antyder, er en nettleser programvare som brukes til å navigere på internett. Den fungerer som en portal mellom brukerens maskin og nettet, og oversetter nettsiders kode til interaktive og lesbare sider. Valget av din nettleser er veldig viktig, da det ikke bare påvirker din nettleseropplevelse, men også din online sikkerhet og personvern.

Vær forsiktig så du ikke forveksler nettleseren med søkemotoren. Nettleseren er programvaren du bruker for å få tilgang til internett (som Chrome eller Firefox), mens søkemotoren er en tjeneste, som for eksempel Google eller Bing, som hjelper deg med å finne informasjon online.

I dag er Google Chrome den desidert mest brukte nettleseren. Den står for omtrent 65% av det globale markedet i 2024. Chrome er verdsatt for sin hastighet og ytelse, men det er ikke nødvendigvis det beste valget for alle, spesielt hvis personvern er en prioritet for deg. Chrome tilhører Google, et selskap kjent for å samle inn og analysere enorme mengder data om brukerne sine. Og faktisk, deres egen nettleser er i hjertet av deres overvåkningsstrategi. Denne programvaren er en sentral komponent i flertallet av dine online interaksjoner. Å mestre datainnsamling på din nettleser er et viktig tema for Google.
![TOR BROWSER](assets/notext/01.webp)
*Kilde: [gs.statcounter.com](https://gs.statcounter.com/browser-market-share)*

Det finnes flere store familier av nettlesere, hver basert på en spesifikk rendering-motor. Nettlesere som Google Chrome, Microsoft Edge, Brave, Opera, eller Vivaldi er alle etablert på Chromium-nettleseren, en lettvekt og åpen kildekode-versjon av Chrome utviklet av Google. Alle disse nettleserne bruker Blink rendering-motoren, som er en forgrening av WebKit, selv avledet fra KHTML. Dominansen av Chromium i markedet gjør nettlesere som er avledet fra den spesielt effektive, ettersom webutviklere har en tendens til å optimalisere sine sider primært for Blink.

Safari, Apples nettleser, bruker WebKit, som også kommer fra KHTML.

På den andre siden, nettlesere som Mozilla Firefox, LibreWolf, og Tor Browser stoler på Gecko, en annen rendering-motor, opprinnelig fra Netscape-nettleseren.

Å velge den riktige nettleseren avhenger av dine behov. Men hvis du i det minste er bekymret for ditt personvern, og derfor din sikkerhet, anbefaler jeg å gå med Firefox for generell bruk og Tor Browser for enda mer personvern. I denne veiledningen vil jeg vise deg hvordan du enkelt kan komme i gang med Tor Browser.
![TOR BROWSER](assets/notext/02.webp)

## Introduksjon til Tor Browser

Tor Browser er en nettleser spesifikt designet for sikker og så privat som mulig internett-navigasjon. Nettleseren er basert på Firefox, og derfor på Gecko rendering-motoren.
Tor Browser bruker Tor-nettverket for å kryptere og rute trafikken din gjennom flere reléservere før den overføres til destinasjonen. Denne prosessen med flerlags ruting, kjent som "*løkruting*", bidrar til å skjule din virkelige IP-adresse, noe som gjør det vanskelig å identifisere din lokasjon og online aktiviteter. Imidlertid er nettlesingen nødvendigvis tregere enn med en standard nettleser som ikke bruker Tor-nettverket, da den er indirekte.
I motsetning til andre nettlesere, integrerer Tor Browser spesifikke funksjoner for å forhindre sporing av dine online aktiviteter, som å isolere hvert besøkt nettsted og automatisk slette informasjonskapsler og historikk ved lukking. Den er også designet for å minimere risikoen for fingerprinting, ved å gjøre alle brukere så like som mulig for de besøkte sidene.
Du kan godt bruke Tor Browser for å få tilgang til en standard nettside (`.com`, `.org`, osv.). I dette tilfellet blir trafikken din anonymisert ved å passere gjennom flere Tor-noder før den når en utgangsnod som kommuniserer med det endelige nettstedet på clearnet. ![TOR BROWSER](assets/notext/03.webp)
Du kan også bruke Tor Browser for å få tilgang til skjulte tjenester (adresser som slutter på `.onion`). I dette scenarioet forblir all trafikk innenfor Tor-nettverket, uten en utgangsnod, noe som sikrer totalt personvern for både brukeren og destinasjonsserveren. Denne driftsmåten brukes spesielt for å få tilgang til det som noen ganger kalles "*dark web*," en del av internett som ikke er indeksert av tradisjonelle søkemotorer.
![TOR BROWSER](assets/notext/04.webp)

## Hva er forskjellen mellom Tor-nettverket og Tor-browseren?

Tor-nettverket og Tor-browseren er to forskjellige ting som ikke bør forveksles, men de er komplementære. Tor-nettverket er en global infrastruktur av reléservere, drevet av brukere, som anonymiserer internett-trafikk ved å sende den gjennom flere noder før den dirigeres til sin endelige destinasjon. Dette er den berømte løkrutingen.

Tor-browseren, derimot, er en spesifikk nettleser designet for å lette tilgangen til dette nettverket på en enkel måte. Den integrerer som standard alle nødvendige innstillinger for å koble til Tor-nettverket og bruker en modifisert versjon av Firefox for å tilby en kjent nettleseropplevelse samtidig som den maksimerer personvern og sikkerhet.

Tor-nettverket brukes ikke bare av Tor-browseren. Det kan brukes av ulike programvarer og applikasjoner for å sikre deres kommunikasjon. For eksempel er det mulig å aktivere kommunikasjon via Tor-nettverket på din Bitcoin-node for å skjule din IP-adresse fra andre brukere og forhindre overvåking av din Bitcoin-relaterte trafikk av din internettleverandør.
For å oppsummere, Tor-nettverket er infrastrukturen som gir personvern i vår internettlesing, og Tor Browser er programvaren som lar oss bruke dette nettverket som en del av vår nettlesing.

## Hvordan installere Tor Browser?

Tor Browser er tilgjengelig for Windows, Linux og macOS for datamaskiner, samt for Android på smarttelefoner. For å installere Tor Browser på datamaskinen din, besøk [den offisielle Tor Project nettsiden](https://www.torproject.org/).
![TOR BROWSER](assets/notext/05.webp)
Klikk på "*Last ned Tor Browser*" knappen.
![TOR BROWSER](assets/notext/06.webp)
Velg versjonen som passer for ditt operativsystem.
![TOR BROWSER](assets/notext/07.webp)
Klikk på den kjørbare filen for å starte installasjonen, deretter velg ditt språk.
![TOR BROWSER](assets/notext/08.webp)
Velg mappen der programvaren skal installeres, deretter klikk på "*Installer*" knappen.
![TOR BROWSER](assets/notext/09.webp)
Vent til installasjonen er fullført.
![TOR BROWSER](assets/notext/10.webp)
Til slutt, klikk på "*Fullfør*" knappen.
![TOR BROWSER](assets/notext/11.webp)

## Hvordan bruke Tor Browser?

Tor Browser brukes som en standard nettleser.
![TOR BROWSER](assets/notext/12.webp)
Ved første oppstart presenterer nettleseren deg for en side som inviterer deg til å koble til Tor-nettverket. Klikk bare på "*Koble til*" knappen for å etablere forbindelsen.
![TOR BROWSER](assets/notext/13.webp)
Hvis du vil at programvaren automatisk skal koble til Tor-nettverket under dine fremtidige bruk, merk av for "*Koble alltid til automatisk*" alternativet.
![TOR BROWSER](assets/notext/14.webp)
Når du er koblet til Tor-nettverket, vil du ankomme hjemmesiden.
![TOR BROWSER](assets/notext/15.webp)For å utføre et søk på Internett, skriv inn søkeforespørselen din i søkefeltet og trykk på "*enter*-tasten".
![TOR BROWSER](assets/notext/16.webp)
Deretter vil du få resultatene fra søkemotoren din på samme måte som med andre nettlesere.
![TOR BROWSER](assets/notext/17.webp)
"*Onionize*-alternativet på DuckDuckGo lar deg bruke søkemotoren via dens skjulte tjeneste på Tor-nettverket, ved å få tilgang til dens `.onion`-adresse.
![TOR BROWSER](assets/notext/18.webp)

## Hvordan konfigurere Tor Browser?

Øverst på nettleserskjermen finner du et alternativ for å importere dine favoritter. Dette lar deg automatisk integrere bokmerkene fra din gamle nettleser inn i Tor Browser.
![TOR BROWSER](assets/notext/19.webp)
Du har også muligheten til å legge til nye bokmerker ved å klikke på stjerneikonet som er plassert øverst til høyre på nettsiden du besøker.
![TOR BROWSER](assets/notext/20.webp)
I menyen til høyre får du tilgang til ulike alternativer.
![TOR BROWSER](assets/notext/21.webp)"*Ny identitet*-knappen lar deg endre din Tor-identitet. Spesifikt gjør dette at du kan starte en ny brukersesjon på Tor, noe som betyr å endre din IP-adresse og tilbakestille informasjonskapsler og åpne sesjoner.
![TOR BROWSER](assets/notext/22.webp)
"*Bokmerker*-menyen lar deg administrere dine bokmerker.
![TOR BROWSER](assets/notext/23.webp)
"*Historikk*" gir deg tilgang til din nettleserhistorikk hvis du har aktivert det i innstillingene.
![TOR BROWSER](assets/notext/24.webp)
"*Tillegg og temaer*-menyen lar deg tilpasse utseendet på nettleseren din eller legge til utvidelser. Siden Tor Browser er basert på Mozilla Firefox, kan du bruke temaer og utvidelser tilgjengelig for Firefox.
![TOR BROWSER](assets/notext/25.webp)
Til slutt gir "*Innstillinger*-knappen deg tilgang til nettleserens innstillinger.
![TOR BROWSER](assets/notext/26.webp)
I "*Generelt*-fanen i innstillingene finnes det ulike alternativer som lar deg tilpasse brukergrensesnittet til Tor Browser.
![TOR BROWSER](assets/notext/27.webp)
I "*Hjem*-fanen kan du velge å endre standard siden som vises når du åpner Tor Browser og når du åpner nye faner.
![TOR BROWSER](assets/notext/28.webp)
I "*Søk*-fanen kan du velge søkemotoren. Tor Browser bruker som standard DuckDuckGo, en søkemotor fokusert på å beskytte brukernes personvern, men du kan også velge Google eller Startpage, for eksempel.
![TOR BROWSER](assets/notext/29.webp)
Du kan også sette opp snarveier i søkemotoren din.
![TOR BROWSER](assets/notext/30.webp)
For eksempel kan du skrive "*@wikipedia*" etterfulgt av søkeordet ditt, som "*Bitcoin*", i nettleserens søkefelt.
![TOR BROWSER](assets/notext/31.webp)
Denne funksjonen utfører da et søk etter termen din direkte på Wikipedia-nettstedet.
![TOR BROWSER](assets/notext/32.webp)
Du kan dermed sette opp andre egendefinerte snarveier for ulike nettsteder.

Videre, i "*Personvern & Sikkerhet*-fanen, vil du finne alle innstillingene relatert til personvern og sikkerhet.
![TOR BROWSER](assets/notext/33.webp)
Du har muligheten til å beholde eller slette din nettleserhistorikk.
![TOR BROWSER](assets/notext/34.webp)Du kan også administrere tilgangstillatelsene du gir til forskjellige nettsteder.
![TOR BROWSER](assets/notext/35.webp)
For den generelle sikkerheten til nettleseren din, tillater modusene "*Safer*" og "*Safest*" deg å justere webfunksjonaliteter og skript som utføres av nettstedene du besøker. Dette minimerer risikoen for utnyttelse av sårbarheter, men det vil også påvirke visningen og interaktiviteten til nettstedene i retur. ![TOR BROWSER](assets/notext/36.webp) Du vil finne andre sikkerhetsalternativer, inkludert en blokkering av farlig innhold og HTTPS-only-modus, som sikrer at forbindelser med nettsteder konsekvent respekterer dette protokollen. ![TOR BROWSER](assets/notext/37.webp) Til slutt, i "*Connection*" fanen, vil du finne alle innstillingene relatert til å koble til Tor-nettverket. Dette er hvor du kan konfigurere en bro for å få tilgang til Tor fra regioner hvor tilgangen kan være sensurert. ![TOR BROWSER](assets/notext/38.webp) Og der har du det, du er nå klar til å navigere på Internett på en tryggere og mer privat måte! Hvis online personvern er et tema som interesserer deg, anbefaler jeg også å oppdage denne andre opplæringen om Mullvad VPN:

https://planb.network/tutorials/others/general/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8