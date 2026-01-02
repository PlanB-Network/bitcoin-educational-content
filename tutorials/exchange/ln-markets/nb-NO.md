---
name: LN Markets
description: Bitcoin handelsplattform på Lightning Network
---

![cover](assets/cover.webp)



LN Markets er den første ekte Lightning-innfødte Bitcoin-handelsplattformen, slik at du kan handle Bitcoin-derivater direkte fra din wallet Lightning, uten KYC, øyeblikkelige oppgjør og minimal depot. Den ble lansert i 2020 og eliminerer friksjonene ved tradisjonelle børser: ingen identitetsbekreftelse, ingen blokkerte innskudd, ingen venting på blokkjede-bekreftelser. Din wallet Lightning blir din handelskonto.



## Hva er LN Markets?



LN Markets tilbyr **Futures** (evigvarende kontrakter med belåning på opptil 100×) og **Options** (Call/Put med risiko begrenset til den betalte premien). Plattformen fungerer som et likviditetsaggregeringslag som konsoliderer flere handelsplasser for optimal utførelse uten slippage. Midlene dine er kun låst i den eksakte varigheten av de aktive posisjonene dine, ikke dager eller uker som med en tradisjonell depotkonto.



### Tilgjengelige handelsprodukter



**Futures (evigvarende kontrakter)**



Evigvarende kontrakter er futures uten utløpsdato, slik at du kan spekulere i Bitcoin-prisutviklingen med gearing. LN Markets tilbyr to marginstyringsmoduser:



**Isolert modus**: Hver posisjon har sin egen dedikerte margin. Kun midlene som er allokert til denne spesifikke posisjonen er i fare. Hvis posisjonen når likvidasjonsprisen, er det **kun denne posisjonen som likvideres**, og dine andre posisjoner og gjenværende saldo påvirkes ikke. Ideell for å begrense risikoen per handel.



**Kryssmodus (kryssmargin)** : Marginen deles mellom alle dine åpne posisjoner. Den totale kontosaldoen din fungerer som sikkerhet for alle posisjonene dine. Hvis en posisjon går dårlig, trekker systemet på hele den tilgjengelige saldoen din for å unngå likvidasjon. **Risiko**: Hvis den totale saldoen din går tom, kan alle posisjonene dine bli likvidert samtidig. Anbefales kun for erfarne tradere som ønsker å maksimere kapitaleffektiviteten.



**Stillingsstyring** :





- Lang posisjon**: du satser på at BTC/USD stiger. Hvis prisen stiger, vinner du; hvis den faller, taper du. **Eksempel**: Bitcoin til 100 000 dollar, du åpner en long med 10 000 sats og 10× gearing. Hvis Bitcoin stiger til 105 000 USD (+5 %), vinner posisjonen din 50 % (5 % × 10), dvs. ~5 000 sats i fortjeneste. Hvis Bitcoin faller til 95 000 USD (-5 %), taper du 50 %, dvs. et tap på ~5 000 sats.





- Kort posisjon**: Du satser på at BTC/USD faller. Hvis prisen går ned, vinner du; hvis den går opp, taper du. **Eksempel**: Bitcoin til 100 000 dollar, du åpner en short med 10 000 sats og 10× gearing. Hvis Bitcoin faller til 95 000 dollar (-5 %), vinner du 50 %, dvs. ~5 000 sats. Hvis Bitcoin stiger til 105 000 dollar (+5 %), taper du 50 %.



Giring (opptil 100×) forsterker gevinster og tap proporsjonalt. En **finansieringsrate**-mekanisme (periodiske avgifter hver 8. time) balanserer lange og korte posisjoner. Du kan administrere opptil 100 futuresposisjoner samtidig.



**Alternativer**



En opsjon er som en **lottokupong med utløpsdato**. Du betaler en premie for å satse på retningen på Bitcoin-prisen. **Stor fordel**: Du kan aldri tape mer enn premien du har betalt, ingen likvidasjon er mulig.





- Kjøpsopsjon (bullish veddemål)**: Du vedder på at Bitcoin vil stige over strike før utløp. Du vinner hvis kursen stiger, og tapet er begrenset til premien hvis kursen faller.





- Salgsopsjon (bearish veddemål)**: Du vedder på at Bitcoin vil falle under innløsningskursen. Du vinner hvis kursen faller, og tapet er begrenset til premien hvis kursen stiger.





- Straddle (volatilitetsveddemål)**: Du kjøper en Call OG en Put samtidig. Du vinner hvis Bitcoin gjør en stor bevegelse i en hvilken som helst retning, du taper begge premiene hvis prisen forblir stabil.



Begrensning: 50 samtidige posisjoner. Ideell for nybegynnere som vil begynne å handle med belåning uten frykt for likvidasjon.



**sats ↔ sUSD**: Konverter satoshiene dine umiddelbart til syntetiske dollar (sUSD) for å beskytte deg mot volatilitet, eller omvendt for å gjenvinne Bitcoin-eksponering.



## Tilgang til plattformen og opprettelse av konto



### Gå til LN Markets



Gå til [lnmarkets.com](https://lnmarkets.com) og klikk på "Åpne app".



![Page d'accueil LN Markets](assets/fr/01.webp)



### Opprett kontoen din



Velkomstskjermen tilbyr flere tilkoblingsmetoder:



![Méthodes de connexion](assets/fr/02.webp)



**Tilgjengelige alternativer** :


1. **Registrer deg med en Lightning wallet** (anbefalt) : LNURL-auth med Phoenix, Breez, Zeus eller BlueWallet


2. **Registrer med e-post**: klassisk konto (begrenser Lightning-opplevelsen)


3. **Alby** eller **Ledger**: nettleserutvidelser



### Tilkobling via Lightning (LNURL-auth)



Klikk på "Registrer deg med en Lightning wallet". Skann QR-koden med din wallet Lightning :



![QR code LNURL-auth](assets/fr/03.webp)



Din wallet signerer automatisk en kryptografisk forespørsel, og kontoen din opprettes umiddelbart, uten e-post eller passord. Sterk sikkerhet og total anonymitet.



### Opprinnelig konfigurasjon



![Configuration post-connexion](assets/fr/04.webp)



**Tilgjengelige parametere** :




- Brukernavn**: Tilpass brukernavnet ditt
- Automatiske uttak**: aktiver automatiske uttak til din wallet etter at handelen er avsluttet
- To-faktor autentisering**: forbedret sikkerhet med 2FA
- Dokumentasjon**: tilgang til offisielle ressurser



## Interface-tur



LN Markets-grensesnittet er organisert i flere seksjoner som er tilgjengelige fra sidemenyen:



### Dashbord



![Dashboard](assets/fr/06.webp)



Viser resultatene dine etter produkttype (Futures Cross, Futures Isolated, Options) med P&L, omsatte volumer og din personlige Address Lightning (f.eks. `pivi@lnmarkets.com`).



### Profil



![Profil trader](assets/fr/07.webp)



Detaljert statistikk: antall handler, tradertype (SCALPER osv.), median posisjonsvarighet, Long/Short-fordeling, gevinstprosent, gjennomsnitt (mengde, margin, gearing) og progressiv gebyrstruktur i henhold til volum.



### Handel



![Historique des trades](assets/fr/08.webp)



Fanen Handler viser en fullstendig historikk over posisjonene dine, med alle viktige data: opprettelsesdato, retning (Long/Short), posisjonsstørrelse (antall), forpliktet margin, inngangs- og utgangskurs, realisert gevinst/tap (P&L) og handelsgebyrer. Du kan filtrere etter produkttype (futures/opsjoner) og eksportere dataene dine for ekstern analyse eller regnskap.



### Innstillinger



![Paramètres de la plateforme](assets/fr/05.webp)



Fanen Innstillinger inneholder to faner: **Konto** og **Interface**.



*fanen *Konto**:



Kontoadministrasjon med redigerbare felt :




- Brukernavn**: endre brukernavnet ditt (f.eks. "pivi") med "Oppdater"-knappen
- E-post**: legg til/rediger e-postadressen din
- Innskudds bitcoin-adresse**: bitcoin-adressen du kan bruke til å sette inn on-chain-midler.



**Tre konfigurasjonsbrytere** :




- Vises på topplister**: velg om du vil vises på offentlige topplister eller ikke
- Bruk Taproot-adresser**: bruk Bitcoin-adresser Taproot for on-chain-innskudd/uttak
- Aktiver automatiske uttak**: aktiver automatiske uttak til wallet Lightning etter at handelen er avsluttet



**Migrering av konto**: Her kan du migrere Lightning-kontoen din til klassisk e-post-/passordautentisering.



**Session-administrasjon**: knappen "Tøm økt og lokale data" for å koble fra og rense lokale nettleserdata.



*fanen *Interface**:



Tilpass brukeropplevelsen med sju brytere:




- Hopp over ordrebekreftelse**: deaktiver bekreftelsesmodal før handelen utføres (rask handel)
- Vis verktøytips**: Vis verktøytips når du holder musepekeren over elementer
- Privat modus (maskerer sensitive data)**: maskerer mengder og sensitive data i grensesnittet (personvernmodus)
- Vis netto PL i profilen**: Vis netto resultat i den offentlige profilen din
- Bruk enhetsikoner**: Vis ikoner for valutaenheter (sats, $)
- Aktiver lydvarsler**: aktiver lydvarsler for handelshendelser
- Aktiver skrivebordsvarsler**: aktiver skrivebordsvarsler fra operativsystemet



### Wallet



![Wallet](assets/fr/09.webp)



Bitcoin og syntetiske USD-saldoer med historikk for innskudd, uttak, kryssoverføringer, swapper, finansiering og on chain adressehåndtering.



### API



![API V3](assets/fr/10.webp)



LN Markets tilbyr en komplett API REST (V2 og V3) for å automatisere handelen din fullt ut via skript eller roboter. Du kan opprette API-nøkler med tilpassbare tillatelser (skrivebeskyttet, handel, uttak) direkte fra grensesnittet. Offisielle TypeScript- og Python-SDK-er er tilgjengelige for enkel integrering. Full API V3-dokumentasjon er tilgjengelig på [api.lnmarkets.com/v3](https://api.lnmarkets.com/v3).



## Første innskudd av midler



Klikk på "Innskudd". Tre metoder er tilgjengelige:



![Modal de dépôt](assets/fr/11.webp)



1. **LNURL**: skann QR-koden med din wallet Lightning


2. **Invoice**: skriv inn et beløp og skann deretter lynfakturaen


3. **On-Chain**: depot Bitcoin on chain



## Handel i praksis



### Handle futures long: sats på oppsiden



Fra dashbordet klikker du på "Futures" og deretter på "Isolated". Klikk på **"Buy"** for å åpne en Long-posisjon.



![Interface Futures Long](assets/fr/12.webp)



Klikk på **kalkulator**-ikonet ved siden av "Kjøp"-knappen for å vise posisjonskalkulatoren:



![Calculateur de position Long](assets/fr/13.webp)



**Konkret eksempel** :




- Antall**: $100 (posisjonsstørrelse)
- Handelsmargin**: 12.336 sats (forpliktet margin)
- Utnyttelse **: 7.73 × (hver 1% BTC-variasjon = 7.73% på kapitalen din)
- Inngangspris** : $104,863.5
- Likvidasjon**: 92 852 dollar (kritisk automatisk avviklingspris)
- Utgangspris**: 110 000 dollar (for beregning av fortjeneste)
- PL** : 4 492 sats (fortjeneste ved utgang på 110 000 dollar)



**Scenarioer** :




- Økning +4,9 %** (110 000 dollar) : +4 492 sats fortjeneste (+36,4 %)
- Nøytral** (104 863 dollar) : -185 sats (kun gebyrer)
- Ned -11,5 %** (92 852 USD): total likvidasjon (-100 %)



Klikk på "Kjøp"-knappen for å bekrefte handelen. **To mulige tilfeller** :





- Hvis du har nok likviditet** på kontoen din, vises en bekreftelsesmodal direkte (bildet nedenfor). Klikk på "Ja" for å utføre handelen umiddelbart.



![Confirmation trade Long](assets/fr/14.webp)





- Hvis du ikke har nok kontanter**: en Lightning QR-kode vises i stedet. Skann den med din wallet Lightning for å betale den nødvendige marginen. Handelen åpnes automatisk ved mottak av betaling



### Handle futures short: satse på nedsiden



Klikk på **"Selg"** for å åpne en short-posisjon (du vinner hvis kursen faller). Åpne kalkulatoren med kalkulatorikonet for å sette opp posisjonen din:



![Calculateur de position Short](assets/fr/15.webp)



Klikk på "Selg" for å bekrefte. Når det gjelder Long, **to mulige tilfeller**:





- Hvis du har nok kontanter**: direkte bekreftelsesmodus, klikk på "Ja"
- Hvis du ikke har nok kontanter**: En Lightning QR-kode vises (bildet nedenfor). Skann den med din wallet Lightning for å betale den nødvendige marginen:



![Paiement Lightning pour Short](assets/fr/16.webp)



Når Lightning-betalingen er mottatt, åpnes short-posisjonen din automatisk. Du kan deretter administrere den fra handelsgrensesnittet.



#### Stenge en posisjon



For å stenge posisjonen din (Long eller Short) klikker du på **det lille krysset nederst i høyre hjørne** i administrasjonsgrensesnittet:



![Interface de clôture](assets/fr/17.webp)



En bekreftelsesdialogboks vises for å bekrefte avslutningen av handelen:



![Confirmation clôture](assets/fr/18.webp)



Modalvinduet viser ditt nåværende resultatregnskap (fortjeneste eller tap). Klikk på "Ja" for å lukke. Saldoen blir umiddelbart lagt til (overskudd) eller trukket fra (underskudd) fra Wallet via Lightning.



### Trade Options Call: betinget rett til å kjøpe



Opsjoner tilbyr **risiko begrenset** til den betalte premien, uten mulighet for avvikling. En call gir deg rett (ikke plikt) til å kjøpe Bitcoin til innløsningskursen før utløp. I motsetning til futures kan du aldri tape mer enn den investerte premien.



Fra dashbordet klikker du på "Alternativer" og velger deretter "Anrop"-fanen.



![Interface Options Call](assets/fr/19.webp)



Konfigurer handelen med følgende parametere:




- Antall**: $100 (størrelsen på kontrakten din)
- Utløpsdato** : 2025-11-15 (utløpsdato)
- Strike**: 96 000 dollar (målpris)



De andre feltene beregnes automatisk:




- Margin**: 1.045 sats (premie som skal betales, din investering)
- Breakeven**: 96 923 dollar (pris for å få tilbake innsatsen din)
- Delta**: 40 (Bitcoin prisfølsomhet)



**Hvordan beregne gevinsten din?



Fortjenesten din avhenger av Bitcoin-prisen ved utløp. Formel: **(BTC-pris - Strike) × Contract-størrelse - Betalt premie**.



**Konkrete eksempler** :





- Bitcoin til 96 000 USD** (nåværende pris) : Indre verdi = $ 0. **Tap: -1,045 sats** (du taper premien)





- Bitcoin til 97 000 dollar**: Egenverdi = (97 000 - 96 000) × 0,00105 BTC = 1,05 USD. Omregnet til sats ≈ 2 175 sats. **Gevinst: 2,175 - 1,045 = +1,130 sats** (+108 % gevinst)





- Bitcoin til 98 000 USD**: egenverdi = 2 000 USD ≈ 3 224 sats. **Gevinst +2 179 sats** (+208 % gevinst)





- Bitcoin til 100 000 USD**: egenverdi = 4 000 USD ≈ 5 263 sats. **Gevinst +4 218 sats** (+403 % gevinst)





- Bitcoin under 96 000 dollar**: Opsjonen utløper verdiløs. **Begrenset tap: -1 045 sats**, ingen avvikling mulig



Klikk på "Buy Call". En dialogboks med bekreftelse vises:



![Confirmation Call option](assets/fr/20.webp)



Klikk på "Buy Call" igjen for å bekrefte. Opsjonen vises i "Running Options". Ved utløp beregner LN Markets automatisk den indre verdien og justerer gevinst/tap.



**Note om salgsopsjoner** : Operasjonen er identisk med en call, men i omvendt rekkefølge. Med en salgsopsjon satser du på at Bitcoin-prisen går **ned**. Hvis Bitcoin faller under strike, vinner du; hvis den holder seg over, taper du bare premien du har betalt. Beregningen av gevinster følger samme logikk: **(Strike - BTC-pris) × Contract-størrelse - Betalt premie**.



### Uttak av lynfond



Klikk på "Trekk ut":



![Modal de retrait](assets/fr/21.webp)



**Metoder** : LNURL, Invoice, Lightning Address, On-Chain.



**Invoice-prosedyre** :


1. Generer en lynfaktura fra din wallet


2. Kopier fakturaen (begynner med `lnbc...`)


3. Lim den inn i LN Markets-feltet


4. Bekreft uttak


5. wallet blir kreditert i løpet av 1-3 sekunder



Ingen gebyrer for lynuttak, kun minimale dirigeringskostnader (<0,1 % i praksis).



## Risikoer og beste praksis



**Hovedrisiko** :




- Total likvidasjon**: høy belåning kan utradere 100 % av marginen på få minutter
- Eksperimentell tjeneste**: alfa-fase, teknologisk usikkerhet
- Motpartsrisiko**: plattformen forblir én motpart



**Beste praksis** :



1. ** Kapitalforvaltning**: Vedta en risikostyringsstrategi som er skreddersydd til din profil. For eksempel: allokere 5 % av de totale eiendelene dine til giret handel, og risikere maksimalt 1 % av denne kapitalen per handel (f.eks.: 1 BTC eiendel → 5M sats til handel → 50k sats maks risiko per posisjon)



2. **Systematisk stop-loss**: Konfigurer stop-loss for å begrense tapene dine per handel. Med en risikoregel på 1 %, for eksempel, vil selv 10 tapende handler på rad bare utgjøre 10 % av handelskapitalen din



3. **Start i det små**: Test først med noen få tusen satellitter for å forstå mekanismene før du tar i bruk kapitalforvaltningsstrategien din



4. **Ta ut fortjenesten din regelmessig**: sikre fortjenesten din på din viktigste wallet, og la bare aktiv handelskapital være igjen på plattformen



5. **Pass på belåning**: Unngå belåning >20× med mindre du er fullstendig klar over likvidasjonsrisikoen



**Kostnader**: ingen lyninnskudd / uttaksgebyrer, spread ~ 0,1% per handel (faller til 0,06% avhengig av volum).



## Fordeler og begrensninger



**Fordeler** :




- Ikke-frihetsberøvende (total kontroll eksklusive handelsperioder)
- KYC-fri (anonymitet via Lightning/Nostr)
- Øyeblikkelige oppgjør (innskudd/uttak på sekunder)
- Utførelse uten slippage med likviditetsaggregering
- API offentlig og Nostr støtte



**Begrensninger** :




- Tjeneste alfa (mulig utvikling)
- Lavere likviditet enn Binance/Deribit
- Forbudt for innbyggere i USA



## Konklusjon



LN Markets representerer en viktig videreutvikling av Bitcoin-handel ved å integrere Lightning Network for å gi kontrollen tilbake til brukerne. For kyndige bitcoinere som ønsker å spekulere uten å gå på akkord med sin egen suverenitet, er dette et unikt alternativ til tradisjonelle sentraliserte børser.



Plattformen fortsetter å utvikle seg med USDT lineære futures og ikke-depotbasert handel via Discreet Log Contracts (DLC) under utvikling. Ved å bruke god risikostyringspraksis (små beløp, stop-loss, regelmessige uttak) blir LN Markets et kraftig verktøy for å utforske Bitcoin-gearing på en ansvarlig måte.



Begynn i det små, test med noen få tusen satellitter, og utforsk gradvis denne nye Lightning Network-fronten. God suverenitetshandel ⚡️!



## Ressurser





- [LN Markets offisielle nettside](https://lnmarkets.com)
- [Dokumentasjon](https://docs.lnmarkets.com)