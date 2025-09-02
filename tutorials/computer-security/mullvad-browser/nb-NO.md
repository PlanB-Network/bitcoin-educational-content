---
name: Mullvad nettleser
description: Slik bruker du Mullvad-nettleseren for personvern
---

![cover](assets/cover.webp)



I en verden der digital overvåking er i ferd med å bli allestedsnærværende, har det aldri vært viktigere å beskytte personvernet ditt på nettet. Selskaper bruker sofistikerte teknikker for å spore deg:





- Tredjeparts informasjonskapsler**: små filer som lagres av eksterne nettsteder for å følge deg fra ett nettsted til et annet
- Fingeravtrykk**: samler inn unike egenskaper ved nettleseren og enheten din (skjermoppløsning, installerte fonter, plugins osv.) for å identifisere deg uten informasjonskapsler
- Sporingsskript**: usynlige JavaScript-koder som analyserer surfeatferden din (klikk, rulling, tidsbruk)
- IP Address-analyse**: geografisk plassering og identifisering av internettleverandøren din



Disse dataene kombineres deretter for å lage detaljerte profiler av nettatferden din, og det tjenes penger på dem, ofte uten at du vet om det. Denne virkeligheten reiser et grunnleggende spørsmål: Hvordan kan du surfe på Internett samtidig som du bevarer anonymiteten og konfidensialiteten din?



Svaret ligger i stor grad i ditt valg av nettleser. Dette verktøyet, som vi bruker hver dag for å få tilgang til informasjon, foreta kjøp eller kommunisere, spiller en avgjørende rolle i beskyttelsen av personopplysningene våre. Dessverre er populære nettlesere som Google Chrome (som har rundt 65 % av det globale markedet) utviklet rundt forretningsmodeller basert på massiv innsamling av brukerdata.



![MULLVAD BROWSER](assets/fr/01.webp)


*Mullvad Browser skiller seg ut med sin eksepsjonelt effektive blokkering av sporing, som langt overgår forbrukernes nettlesere*



I møte med denne utfordringen dukker det nå opp nye aktører med en annen filosofi, nemlig å sette personvernet i sentrum for designet. Blant dem skiller Mullvad Browser seg ut som en innovativ løsning som kombinerer den beste personvernbeskyttelsen med en flytende og tilgjengelig nettleseropplevelse.



I motsetning til tradisjonelle nettlesere som forsøker å tilpasse opplevelsen din ved å samle inn data om deg, går Mullvad Browser motsatt vei: Den får alle brukerne til å se identiske ut på nettsidene, noe som gjør individualisert sporing praktisk talt umulig.



I denne veiledningen skal vi sammen finne ut hvordan Mullvad Browser kan forandre måten du surfer på Internett på, og gi deg robust beskyttelse mot overvåking uten at det går på bekostning av brukervennligheten.




## Vi introduserer Mullvad Browser



**Mullvad Browser** er en personvernfokusert nettleser utviklet i samarbeid med Tor-prosjektet og distribuert gratis av det svenske selskapet Mullvad VPN. Den ble lansert i april 2023 og presenterer seg selv som en **"Tor-nettleser uten Tor-nettverket"**, designet for å minimere sporing og fingeravtrykk på nettet, samtidig som den lar brukerne surfe via et pålitelig VPN i stedet for Tor-nettverket.



Mullvad Browser er en gratis nettleser med åpen kildekode, basert på Firefox ESR (langtidsversjonen av Mozilla Firefox) og herdet av eksperter fra Tor-prosjektet. Konkret inkluderer den de fleste **beskyttelsesfunksjonene i Tor Browser**, men **ruter ikke trafikken via Tor-nettverket**. I stedet kan (og bør) brukerne koble den til et pålitelig kryptert VPN for å anonymisere IP Address.



Når det gjelder brukeropplevelse, ligner Mullvad Browser en klassisk nettleser, med flytende navigering. Den er tilgjengelig gratis på Windows, macOS og Linux (ingen mobilversjon). Du trenger ikke å være Mullvad VPN-abonnent for å bruke den, men **bruk av Mullvad Browser uten å maskere IP-en din gir ikke fullstendig anonymitet** - så det anbefales på det sterkeste å bruke den sammen med et pålitelig VPN.



### Mål: personvern og antisporing



Mullvad-nettleseren er utviklet med ett hovedmål i tankene: **beskytte brukernes personvern** på nettet og motvirke vanlige sporings- og profileringsteknikker. Hovedmålene inkluderer:





- Reduser annonsesporing og sporing** fra nettsteder og reklamebyråer drastisk. Som standard blokkerer Mullvad Browser tredjepartssporere, sporingskapsler og fingeravtrykk-skript som kan identifisere deg.





- Standardiser nettleserens fingeravtrykk** for å **"smelte inn i mengden"**. Fingeravtrykket er som et unikt "identitetskort" som skapes ved å kombinere alle egenskapene til nettleseren din. Mullvad Browser sørger for at alle brukerne har nøyaktig samme "identitetskort", noe som gjør det umulig å skille dem fra hverandre.





- Tilbyr umiddelbar beskyttelse uten ekstra utvidelser**. Mullvad Browser leveres i en "klar til bruk"-konfigurasjon: brukeren trenger ikke å installere en rekke utvidelser eller endre noen innstillinger for å bli beskyttet.





- Ikke ofre ytelse eller ergonomi** mer enn nødvendig. Uten Tor-ruting tilbyr Mullvad Browser mye raskere surfing enn Tor Browser, og nærmer seg ytelsen til en standard nettleser kombinert med et VPN.



### Viktige funksjoner i Mullvad Browser



Mullvad Browser inneholder en rekke **sikkerhets- og personvernfunksjoner** som er direkte inspirert av Tor Browser:





- Privat surfing til enhver tid:** Privat surfemodus er aktivert som standard og kan ikke deaktiveres. **Ingen historikk, informasjonskapsler eller hurtigbuffer lagres fra en økt til den neste**. Så snart du lukker Mullvad Browser, slettes alle nettleserdata.





- Forbedret beskyttelse mot fingeravtrykk:** Nettleseren bruker strenge innstillinger for å hindre digitale fingeravtrykk. Dette inkluderer:
 - Standardisering av brukeragent** og nettleserversjon
 - Tidssone satt til UTC** for alle brukere
 - Letterboxing**: en teknikk som automatisk legger til grå marginer rundt nettsidene for å standardisere visningsstørrelsen og forhindre identifikasjon ut fra skjermdimensjonene dine
 - Blokker fingeravtrykk-API-er**: Canvas (2D-tegning), WebGL (3D-grafikk) og AudioContext (lydbehandling) er deaktivert fordi de kan avsløre unike detaljer om maskinvaren din
 - Standardiserte systemfonter** for å unngå identifikasjon av installerte fonter





- Blokkering av sporere og reklame:** Mullvad Browser integrerer **uBlock Origin**-utvidelsen (forhåndsinstallert) med ekstra beskyttelseslister for å blokkere **tredjepartssporere, reklameskript og annet ondsinnet innhold**. Denne beskyttelsen ledsages av **First-Party Isolation**: en teknikk som lagrer informasjonskapsler i separate "potter" for hvert nettsted, slik at ett nettsted ikke kan lese informasjonskapsler som er lagret av et annet.





- Tilbakestillingsknapp for økter:** I likhet med Tor-nettleserens "New Identity"-knapp har Mullvad Browser en knapp for **rask omstart av nettleseren med en ny, tom økt**.





- Justerbare sikkerhetsnivåer:** Du kan justere sikkerhetsnivået (*Normal*, *Safer*, *Safest*) i innstillingene, akkurat som i Tor Browser.



## Innebygde utvidelser som standard



Mullvad Browser inkluderer **tre forhåndsinstallerte utvidelser** som utgjør kjernen i antisporingsbeskyttelsen. **Det er viktig å aldri fjerne dem eller endre konfigurasjonene**, da dette vil gjøre deg unik blant Mullvad Browser-brukere:



### **uBlock Origin**


Denne utvidelsen for blokkering av annonser og sporere leveres forhåndskonfigurert med **optimaliserte filterlister** for å blokkere:




- Påtrengende reklame
- Tredjepartssporere som samler inn dataene dine
- Skadelige skript
- Atferdssporing Elements



uBlock Origin i Mullvad Browser bruker standardiserte parametere for å sikre at alle brukere blokkerer nøyaktig samme Elements, slik at de digitale fotavtrykkene forblir enhetlige.



### **NoScript**


NoScript kjører i bakgrunnen for å administrere nettleserens **sikkerhetsnivåer**. Dette:




- Kontrollerer kjøring av JavaScript** i henhold til valgt nivå (Normal/Mest sikker/Mest sikker)
- Filtrerer automatisk bort XSS**-angrep (Cross-Site Scripting)
- Blokkerer farlig** aktivt innhold på nettsteder som ikke er https
- Ikonet er skjult som standard, men kan vises via "Tilpass verktøylinjen"



### **Mullvad Browser**-utvidelse


Denne Mullvad-spesifikke utvidelsen tilbyr ulike funksjoner avhengig av om du er Mullvad VPN-kunde eller ikke:



#### **Uten Mullvad VPN-abonnement:**




- Grunnleggende tilkoblingssjekk**: viser din nåværende offentlige IP og noe tilkoblingsinformasjon
- Personvernanbefalinger**: tips om hvordan du kan forbedre sikkerhetsinnstillingene dine (DNS, kun HTTPS, søkemotor)
- WebRTC**-kontroll: aktiver/deaktiver for å forhindre IP Address-lekkasjer
- Kan slettes uten innvirkning** på ditt digitale fotavtrykk hvis du ikke bruker Mullvad VPN



#### **Med Mullvad VPN-abonnement:**


Utvidelsen avslører sitt fulle potensial med avanserte funksjoner:





- Integrert SOCKS5-proxy**: tilkobling til Mullvad VPN-serverproxy med ett klikk
 - Fast IP Address**: I motsetning til et VPN, som kan endre sin IP Address, garanterer en proxy alltid den samme utgangs-Address
 - Automatisk nødstopp**: Hvis VPN kobles fra, blokkeres nettlesertrafikken umiddelbart
 - Støtte for IPv6**: IPv6-tilkobling selv om VPN-tilkoblingen din ikke har det aktivert





- Multihop (dobbelt VPN)**: mulighet til å endre proxy-plassering for å opprette en tunnel i tunnelen
 - Trafikken din går først gjennom VPN-serveren din, og "hopper" deretter til en annen Mullvad-server
 - Bruk en annen lokalisering kun for nettleseren





- Avansert tilkoblingsovervåking**: sanntidsovervåking av VPN-status, tilkoblet server og DNS-lekkasjedeteksjon





- Tilgang til Mullvad Leta**: privat søkemotor forbeholdt abonnenter (men ikke anbefalt av Mullvad på grunn av korrelasjon med kontoen din)



Disse tre utvidelsene fungerer sammen for å skape et sammenhengende økosystem av beskyttelse, der alle brukere drar nytte av nøyaktig det samme forsvaret uten mulighet for tilpasning som ville kompromittere den kollektive anonymiteten.



## Fordeler og ulemper med Mullvad Browser



### Fordeler





- Utmerket personvern som standard:** Mullvad Browser bruker svært strenge personverninnstillinger helt fra starten av, uten behov for manuell konfigurasjon.





- Bedre ytelse enn Tor Browser:** I fravær av onion-routing er Mullvad Browser **betydelig raskere og mer responsiv** enn Tor Browser for klassisk nettsurfing.





- Kjent Interface-enkelhet:** Mullvad Browser er basert på Firefox' Interface. Hvis du er vant til Firefox eller til og med Tor Browser, vil du ikke føle deg malplassert.





- Pålitelig samarbeid og revidert kode:** Mullvad Browser drar nytte av ekspertisen i Tor-prosjektet, og all kildekode er tilgjengelig for ekstern revisjon.



### Ulemper





- Ingen nettverksanonymitet uten VPN:** Det viktigste poenget er at **Mullvad Browser ikke skjuler din IP Address av seg selv** (som alle andre nettlesere, bortsett fra Tor Browser). Din IP Address er som din "post Address" på Internett: den avslører hvor du befinner deg og din ISP. Den er derfor **avhengig av et VPN** (virtuelt privat nettverk) for å skjule denne viktige informasjonen.





- Ingen mobilversjon:** Mullvad Browser er foreløpig bare tilgjengelig på PC (Windows, Mac, Linux).





- Uforenlig med visse vaner:** **Den **permanente private modusen** betyr at du ikke kan beholde en økt fra én bruk til den neste. Det er umulig å forbli tilkoblet en nettkonto fra én økt til den neste.





- Begrensede funksjoner:** For å bevare fingeravtrykkets ensartethet har Mullvad Browser **deaktivert flere funksjoner** som finnes i Firefox, og er ikke beregnet for tilpasning.



## Installere Mullvad Browser



Mullvad Browser er gratis tilgjengelig for Windows, macOS og Linux. For å installere den, gå til [det offisielle Mullvad-nettstedet] (https://mullvad.net/browser).



![MULLVAD BROWSER](assets/fr/02.webp)



*Offisiell hjemmeside for Mullvad Browser med nedlastningsknapp uthevet *



![MULLVAD BROWSER](assets/fr/03.webp)



*Velg operativsystem på nedlastingssiden for Mullvad Browser.*



Klikk på **"Last ned"**-knappen som tilsvarer operativsystemet ditt.



For Linux kan du velge mellom ulike formater, avhengig av distribusjonen din. Når nedlastingen er fullført:



### På Windows


Kjør den nedlastede `.exe`-filen og følg installasjonsinstruksjonene.



### På macOS


Åpne den nedlastede .dmg-filen, og dra Mullvad Browser-applikasjonen inn i Programmer-mappen.



### På Linux


Pakk ut `.tar.xz`-arkivet i katalogen du ønsker, og kjør filen `start-mullvad-browser.desktop`.



## Konfigurasjon og første gangs bruk



Når du starter Mullvad Browser for første gang, ser du en Interface som ligner veldig på Tor Browser. Nettleseren er forhåndskonfigurert for personvern og krever ingen spesielle modifikasjoner.



![MULLVAD BROWSER](assets/fr/04.webp)



*Interface Mullvad Browser-startside med utvidelser, kost-ikon til generate en ny identitet og applikasjonsmeny øverst til høyre*



**Viktig:** Mullvad Browser maskerer ikke din IP Address som standard. For fullstendig beskyttelse anbefaler vi sterkt at du bruker et VPN parallelt. Du kan bruke Mullvad VPN eller en annen pålitelig VPN-tjeneste.



Nettleseren inkluderer også **DNS-over-HTTPS (DoH)** ved hjelp av Mullvads DNS-tjeneste: Denne teknologien krypterer DNS-forespørslene dine (oversetter nettstedsnavn til IP-adresser) for å forhindre at Internett-leverandøren din overvåker nettstedene du besøker.



### Sikkerhetsinnstillinger



Du kan justere sikkerhetsnivået ved å klikke på **applikasjonsmenyen** (tre horisontale streker) øverst til høyre, deretter **"Innstillinger"** og deretter fanen **"Personvern og sikkerhet"**. Bla ned til delen **"Sikkerhet"**:



![MULLVAD BROWSER](assets/fr/05.webp)



*Valg av sikkerhetsnivåer: pilene viser veien fra applikasjonsmenyen til fanen "Personvern og sikkerhet" til sikkerhetsalternativene*



Mullvad Browser tilbyr tre sikkerhetsnivåer:





- Normal** (nåværende standardnivå): Alle nettleser- og nettstedsfunksjoner er aktivert





- Tryggere**: Deaktiverer ofte farlige nettstedsfunksjoner, noe som kan føre til tap av funksjonalitet på enkelte nettsteder:
 - JavaScript er deaktivert for nettsteder som ikke har HTTPS
 - Noen skrifter og matematiske symboler er deaktivert
 - Lyd og video (HTML5 media) samt WebGL er "klikk for å spille"





- Den tryggeste**: Tillater bare de nettstedsfunksjonene som kreves for statiske nettsteder og grunnleggende tjenester:
 - JavaScript er deaktivert som standard for alle nettsteder
 - Noen skrifter, ikoner, bilder og matematiske symboler er deaktivert
 - Lyd og video (HTML5 media) samt WebGL er "klikk for å spille"



### Ny økt-knapp



Hvis du vil starte på nytt med en tom økt uten å lukke nettleseren, klikker du på kost-ikonet eller bruker programmenyen > **"Ny økt"**.



![MULLVAD BROWSER](assets/fr/06.webp)



*Tilbakestill identiteten din"-funksjonen for å starte nettleseren på nytt med en helt ny økt*



## Hverdagsbruk



### Normal navigering



Mullvad Browser oppfører seg som en klassisk nettleser for daglig surfing. Alle nettsteder er tilgjengelige som vanlig, med den ekstra fordelen av forbedret beskyttelse mot sporing.



### Administrasjon av informasjonskapsler og pålogging



På grunn av den permanente private modusen må du koble deg til kontoene dine på nytt hver gang du logger deg på. Dette er prisen du betaler for maksimal konfidensialitet.



### Utvidelser



Mullvad Browser lar deg teknisk sett installere flere utvidelser fra Firefox-katalogen, men **det er viktig å forstå implikasjonene**. Hver utvidelse som legges til, endrer ditt digitale fotavtrykk og skiller deg fra andre Mullvad Browser-brukere, noe som strider mot nettleserens grunnleggende prinsipp: å få alle brukere til å fremstå som identiske.



Som Mullvad forklarer: *"Noen ganger er det bedre å ikke ha noe spesifikt forsvar enn å ha et. Når du ønsker å øke personvernet på nettet, installerer du utvidelser som til syvende og sist gjør deg enda mer synlig. "*



Hvis du likevel velger å installere utvidelser, må du være klar over at du oppretter et unikt fingeravtrykk som kan brukes til å spore deg fra nettsted til nettsted. For maksimal beskyttelse er det best å holde seg til de tre forhåndsinstallerte utvidelsene, som er identiske for alle brukere.



## Beste praksis med Mullvad Browser



1. **Bruk alltid et VPN: Mullvad Browser maskerer ikke IP-en din. Et VPN er avgjørende for fullstendig anonymitet.



2. **Ikke tilpass nettleseren**: Unngå å endre innstillinger eller legge til utvidelser, da dette kan gjøre deg identifiserbar.



3. **Bruk knappen for ny økt**: Mellom ulike aktiviteter kan du bruke tilbakestillingsfunksjonen til å dele opp øktene dine.



4. **Velg det sikkerhetsnivået som passer best til dine behov**:




   - Normal (anbefalt)**: For daglig surfing. Gir allerede utmerket beskyttelse samtidig som nettsteder fungerer. Dette er den beste balansen for 95 % av brukerne.
   - Tryggere**: Hvis du besøker ukjente eller potensielt farlige nettsteder, eller for ekstra beskyttelse på offentlige Wi-Fi-nettverk. Noen nettsteder kan fungere feil.
   - Mest sikker**: Forbeholdt høyrisikosituasjoner (undersøkende journalistikk, sensitiv kommunikasjon, fiendtlige miljøer). De fleste moderne nettsteder vil bli ødelagt, men det er prisen for maksimal sikkerhet.



5. **Se jevnlig etter oppdateringer**: Hold nettleseren oppdatert med de nyeste sikkerhetsoppdateringene.



6. **Bruk personvernvennlige søkemotorer**: Velg DuckDuckGo, Startpage eller Searx fremfor Google.



7. **Aktiver kun HTTPS-modus**: I innstillingene må du sørge for at "Kun HTTPS"-modus er aktivert for å tvinge frem sikre tilkoblinger.



8. **Ikke endre noen avanserte innstillinger**: I motsetning til andre nettlesere er Mullvad Browser utformet slik at ALLE brukere har nøyaktig samme konfigurasjon. Hvis du endrer innstillingene i `about:config` eller endrer uBlock Origin/NoScript-innstillingene, vil det gjøre deg unik og fullstendig oppheve nettleserens anonymitet.



## Anbefalt DNS-konfigurasjon



Mullvad Browser integrerer automatisk Mullvad DNS-over-HTTPS. Hvis du bruker Mullvad VPN, vil utvidelsen anbefale at du **deaktiverer Mullvad DoH**, siden det er raskere å bruke VPN-serverens DNS-server. Hvis du ikke bruker Mullvad VPN, bør du beholde Mullvad DoH aktivert for å unngå DNS-overvåking fra Internett-leverandøren din.



## Konklusjon



Mullvad Browser er en utmerket løsning for deg som ønsker å surfe på nettet på en personvernvennlig måte uten ytelsesbegrensningene til Tor-nettverket. Kombinert med et VPN av høy kvalitet gir den robust beskyttelse mot sporing og overvåking på nettet.



Selv om den har visse begrensninger (ingen mobilversjon, ikke-vedvarende økter), er Mullvad Browser et verdifullt verktøy i arsenalet til alle som ønsker å gjenvinne kontrollen over sitt digitale personvern. Brukervennligheten og standardkonfigurasjonen gjør den til et klokt valg for personvernbevisste brukere, enten de er nybegynnere eller erfarne.



## Ressurser



### Offisiell dokumentasjon




- [Offisielt nettsted for Mullvad Browser](https://mullvad.net/fr/browser)
- [Nedlastingsside for Mullvad Browser] (https://mullvad.net/en/download/browser)
- [Detaljerte tekniske spesifikasjoner] (https://mullvad.net/en/browser/Hard-facts)
- [Mullvad nettleserutvidelse] (https://mullvad.net/en/help/mullvad-browser-extension)



### Veiledninger og forklaringer




- [Hvorfor personvern er viktig] (https://mullvad.net/en/why-privacy-matters/how-mass-surveillance-companies-collect-your-data)
- [Tor uten Tor: Mullvad Browser-konseptet] (https://mullvad.net/en/browser/tor-without-tor)
- [Hvordan velge en personvernvennlig nettleser] (https://mullvad.net/en/browser/things-to-look-for-when-choosing-a-browser)
- [Forstå fingeravtrykk fra nettlesere] (https://mullvad.net/en/browser/browser-fingerprinting)



### Støtte og hjelp




- [Mullvad Browser Help Center] (https://mullvad.net/en/help/tag/mullvad-browser)
- [Første skritt mot personvern på nettet] (https://mullvad.net/en/help/first-steps-towards-online-privacy)



### Fellesskapets ressurser




- [Mullvad Browser Guide - Privacy Guides](https://www.privacyguides.org/en/desktop-browsers/)
- [Fellesskapsdiskusjoner] (https://discuss.privacyguides.net/t/about-changing-settings-in-mullvad-browser/18330)