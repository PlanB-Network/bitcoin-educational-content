---
name: PlanB Professor
description: Hvordan legge til din professorprofil på PlanB-nettverket?
---
![cover](assets/cover.webp)

Målet med PlanB er å tilby førsteklasses utdanningsressurser om Bitcoin, på så mange språk som mulig. Alt innhold publisert på nettstedet er åpen kildekode og hostet på GitHub, noe som lar hvem som helst delta i å berike plattformen. Bidrag kan ta forskjellige former: korrigering og korrekturlesing av eksisterende tekster, produksjon av opplæringskurs, oversettelse til andre språk, oppdatering av informasjon, eller oppretting av nye veiledninger som ennå ikke er tilgjengelige på nettstedet vårt.

Hvis du ønsker å legge til en ny komplett veiledning eller et kurs på PlanB-nettverket, må du opprette din professorprofil. Dette vil tillate deg å bli korrekt kreditert for innholdet du produserer på nettstedet.
![tutorial](assets/1.webp)
Hvis du tidligere har bidratt til PlanB-nettverket, har du sannsynligvis allerede et bidragsyter-ID. Du kan finne det i din professor-mappe tilgjengelig [via denne siden](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors). Hvis dette er tilfellet, kan du hoppe over denne veiledningen og begynne å bidra direkte.
![tutorial](assets/2.webp)

La oss sammen oppdage hvordan vi legger til en ny professor i denne veiledningen!

## Forutsetninger

**Programvare som kreves for å følge min veiledning:**
- [GitHub Desktop](https://desktop.github.com/)
- En kodeeditor ([VSC](https://code.visualstudio.com/) eller [Sublime Text](https://www.sublimetext.com/))
![tutorial](assets/3.webp)
**Forutsetninger før du starter veiledningen:**
- Å ha en [GitHub-konto](https://github.com/signup).
- Å ha en fork av [PlanB Network-kilderepositoriet](https://github.com/PlanB-Network/bitcoin-educational-content).

**Hvis du trenger hjelp til å skaffe disse forutsetningene, vil mine andre veiledninger guide deg:**
**[Forstå Git og GitHub](https://planb.network/tutorials/others/basics-of-github)**
**[Opprette en GitHub-konto](https://planb.network/tutorials/others/create-github-account)**
**[Sette opp ditt arbeidsmiljø](https://planb.network/tutorials/others/github-desktop-work-environment)**

## Hvordan opprette en ny professorprofil?

- Åpne nettleseren din og naviger til siden for din fork av PlanB-repositoriet. URL-en til din fork bør se slik ut: `https://github.com/[brukernavn]/sovereign-university-data`
![tutorial](assets/4.webp)
- Sørg for at du er på hovedgrenen `dev` og klikk deretter på `Sync fork`-knappen. Hvis din fork ikke er oppdatert, vil GitHub tilby å oppdatere grenen din. Fortsett med denne synkroniseringen.

- Hvis, derimot, din gren allerede er oppdatert, vil GitHub informere deg:
![tutorial](assets/5.webp)- Åpne GitHub Desktop og sørg for at din fork er korrekt valgt i øvre venstre hjørne av vinduet:
![tutorial](assets/6.webp)
- Klikk på `Fetch origin`-knappen.

- Hvis ditt lokale repositorium allerede er oppdatert, vil GitHub Desktop ikke foreslå noen videre handling. Ellers vil `Pull origin`-alternativet dukke opp. Klikk på denne knappen for å oppdatere ditt lokale repositorium:
![tutorial](assets/7.webp)
- Sørg for at du er på hovedgrenen `dev`:
![tutorial](assets/8.webp)
- Klikk på denne grenen, og klikk deretter på `New Branch`-knappen:
![tutorial](assets/9.webp)
- Sørg for at den nye grenen er basert på kildearkivet, nemlig `DecouvreBitcoin/sovereign-university-data`.
- Navngi din gren på en måte som tittelen er klar over dens formål, ved å bruke bindestreker for å skille hvert ord. Siden denne grenen er ment for å legge til en professorprofil, kan et eksempelnavn være: `add-professor-[ditt-navn]`. Etter å ha skrevet inn navnet, klikk på `Create branch` for å bekrefte opprettelsen:
![opplæring](assets/10.webp)
- Klikk nå på `Publish branch`-knappen for å lagre din nye arbeidsgren til din online fork på GitHub:
![opplæring](assets/11.webp)
- På dette tidspunktet, på GitHub Desktop, bør du være på din nye gren. Dette betyr at alle endringer gjort lokalt på datamaskinen din vil bli eksklusivt registrert på denne spesifikke grenen. Så lenge denne grenen forblir valgt på GitHub Desktop, tilsvarer filene som er synlige lokalt på maskinen din de på denne grenen (`add-professor-ditt-navn`), og ikke til de på hovedgrenen (`dev`):
![opplæring](assets/12.webp)
- For å legge til din professorprofil, åpne filutforskeren din og naviger til ditt lokale arkiv, i `professors`-mappen. Du vil finne den under stien: `\GitHub\sovereign-university-data\professors`.

- Innenfor denne mappen, opprett en ny mappe navngitt med ditt navn eller pseudonym. Sørg for at det ikke er mellomrom i mappenavnet. Så, hvis ditt navn er "Loic Pandul" og ingen andre professorer har dette navnet, vil mappen som skal opprettes være navngitt `loic-pandul`:
![opplæring](assets/13.webp)
- For å gjøre ting enklere, kan du allerede kopiere og lime inn alle dokumentene fra en annen professor inn i din egen mappe. Vi vil deretter fortsette med å endre disse dokumentene for å tilpasse dem i henhold til din profil:
![opplæring](assets/14.webp)
- Start med å navigere til `assets`-mappen. Slett profilbildet til professoren som du tidligere kopierte, og erstatt det med ditt eget profilbilde. Det er avgjørende at dette bildet er i `.webp`-formatet og at det er navngitt `profile`, og gir dermed det komplette filnavnet `profile.webp`. Vær oppmerksom, dette bildet vil bli publisert på Internett og tilgjengelig for alle: ![opplæring](assets/15.webp)
- Deretter, åpne `professor.yml`-filen med din kodeeditor (VSC eller Sublime Text, for eksempel). Du vil komme til filen kopiert fra en eksisterende professor:
![opplæring](assets/16.webp)
- Du må deretter oppdatere den eksisterende informasjonen med din egen:
	- **name:** skriv ditt navn eller pseudonym;
	- **links:** angi dine kontoer på sosiale nettverk som Twitter og Nostr, samt URL-en til ditt personlige nettsted (valgfritt);
	- **affiliation:** nevn navnet på selskapet som ansetter deg (valgfritt);
	- **tags:** spesifiser dine spesialiseringsområder fra følgende liste, vel vitende om at du kan legge til dine egne temaer. Sørg imidlertid for å begrense antall tags til maksimalt 4 for å sikre et godt UI:
	    - privacy,
	    - cryptography,
	    - bitcoin,
	    - mining,
	    - lightning-network,
	    - economy,
	    - history,
	    - merchants,
	    - security,
	    - ...
	- **tips:** oppgi din Lightning-adresse for donasjoner for å tillate lesere av dine fremtidige opplæringsprogrammer å sende deg noen sats (valgfritt);
	- **company:** hvis du eier en, angi navnet på selskapet ditt (valgfritt). Du må deretter oppdatere den eksisterende informasjonen med din egen:
![opplæring](assets/17.webp)- Du må også endre `contributor-id`. Denne identifikatoren brukes til å gjenkjenne deg på nettstedet, men blir ikke offentliggjort utenfor GitHub. Du står fritt til å velge en hvilken som helst kombinasjon av to ord, med referanse til [den engelske listen over 2048 ord fra BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt). Ikke glem å sette inn et bindestrek mellom de to valgte ordene. For eksempel, her valgte jeg `crazy-cactus`:
![opplæring](assets/18.webp)
- Når du har fullført endringen av `professor.yml`-dokumentet, klikk på `File > Save` for å lagre filen din. Du kan deretter lukke kodeeditoren din:
![opplæring](assets/19.webp)
- Innenfor din professor-mappe, kan du slette dokumenter skrevet på språk som ikke angår deg, som opprinnelig ble kopiert fra en annen professor. Behold kun filen som tilsvarer ditt morsmål. For eksempel, i mitt tilfelle, beholdt jeg kun `fr.yml`-filen, siden mitt språk er fransk: ![opplæring](assets/20.webp)
- Dobbeltklikk på denne filen for å åpne den med kodeeditoren din.

- I denne filen har du muligheten til å skrive din komplette biografi under `bio`-seksjonen og et sammendrag eller en kort tittel under `short_bio`:
![opplæring](assets/21.webp)
- Etter å ha lagret `fr.yml`-dokumentet ditt, må du lage en kopi av denne filen for hver av de følgende åtte språkene:
    - Tysk (DE);
    - Engelsk (EN);
    - Fransk (FR);
    - Spansk (ES);
    - Italiensk (IT);
    - Portugisisk (PT);
    - Japansk (JA);
    - Vietnamesisk (VI).

- Fortsett å kopiere og lime inn din originale fil, og oversett deretter hvert dokument til det tilsvarende språket. Hvis du behersker språket, kan du utføre oversettelsen manuelt. Ellers, føl deg fri til å bruke et automatisk oversettelsesverktøy eller en chatbot:
![opplæring](assets/22.webp)
- Hvis du foretrekker, er det også mulig å kun beholde biografien på ditt morsmål; vi vil da håndtere oversettelsen etter innsendingen av din Pull Request.

- Din professor-mappe bør dermed se slik ut:
![opplæring](assets/23.webp)
```plaintext
fornavn-etternavn/
├── fr.yml
├── it.yml
├── es.yml
├── en.yml
├── de.yml
├── pt.yml
├── ja.yml
├── vi.yml
├── professor.yml
└── assets/
    └── profile.webp
```
- Nå returner til GitHub Desktop.
- På venstre side av vinduet ditt, bør du observere alle modifikasjonene gjort til dokumentene, spesifikt for din gren. Sørg for at disse modifikasjonene er korrekte:
![opplæring](assets/24.webp)
- Hvis modifikasjonene ser riktige ut for deg, legg til en tittel for ditt commit. Et commit er en lagring av modifikasjonene gjort til grenen, ledsaget av en beskrivende melding, som tillater å følge evolusjonen av et prosjekt over tid.
- Når tittelen er inntastet, trykk på den blå `Commit to [din gren]`-knappen for å validere disse modifikasjonene:
![opplæring](assets/25.webp)
- Deretter klikker du på `Push origin`-knappen. Dette vil sende ditt commit til din fork:
![opplæring](assets/26.webp)
- Hvis du har fullført dine modifikasjoner for denne grenen, klikk nå på `Preview Pull Request`-knappen:
![opplæring](assets/27.webp)
- Du kan sjekke en siste gang at endringene dine er korrekte, og deretter klikke på `Create pull request`-knappen: ![tutorial](assets/28.webp)- Du vil automatisk bli omdirigert til nettleseren din på GitHub til forberedelsessiden for Pull Request. En Pull Request er en forespørsel om å integrere endringene fra din gren til hovedgrenen til PlanB Network-repositoriet, som tillater gjennomgang og diskusjon av endringene før de slås sammen: ![tutorial](assets/29.webp)
- På denne forberedelsessiden, angi en tittel som kort oppsummerer endringene du ønsker å slå sammen med kilde-repositoriet.
- Legg til en kort kommentar som beskriver disse endringene.
- Etter å ha fullført disse stegene, klikk på den grønne `Create pull request`-knappen for å bekrefte sammenslåingsforespørselen: ![tutorial](assets/30.webp)
- Din PR vil da være synlig i `Pull Request`-fanen til hovedrepositoriet til PlanB Network. Alt du trenger å gjøre nå er å vente til en administrator kontakter deg for å bekrefte sammenslåingen av ditt bidrag eller for å be om eventuelle ytterligere endringer: ![tutorial](assets/31.webp)
- Etter sammenslåingen av din PR med hovedgrenen, anbefales det å slette din arbeidsgren (`add-professor-your-name`) for å opprettholde en ren historikk på din fork. GitHub vil automatisk tilby deg denne muligheten på din PR-side: ![tutorial](assets/32.webp)
- På GitHub Desktop-programvaren kan du bytte tilbake til hovedgrenen til din fork (`dev`): ![tutorial](assets/8.webp)
- Hvis du ønsker å gjøre endringer i profilen din etter å allerede ha sendt inn din PR, avhenger prosedyren av den nåværende tilstanden til din PR:
	- Hvis din PR fortsatt er åpen og ikke ennå er slått sammen, gjør endringene lokalt mens du forblir på samme gren. Når endringene er ferdigstilt, bruk `Push origin`-knappen for å legge til en ny commit til din fortsatt åpne PR;
	- I tilfelle der din PR allerede har blitt slått sammen med hovedgrenen, må du starte prosessen på nytt ved å opprette en ny gren, og deretter sende inn en ny PR. Sørg for at ditt lokale repositorium er synkronisert med PlanB Network kilde-repositorium før du fortsetter.