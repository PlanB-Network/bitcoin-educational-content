---
name: F-Cold
description: Katalogen over gratis applikasjoner med åpen kildekode.
---

![cover](assets/cover.webp)



I den digitale tidsalderen arbeider store selskaper og institusjoner for å gjøre Internett mer sentralisert, legge kontrollen over det i sine egne hender og dermed hindre personvernet og friheten til alle brukere. Dette er ingen utopi, det skjer allerede. Som bitcoiner er desentralisering, respekt for personvern og individuelle friheter prinsipper som du setter høyt, spesielt i verktøyene du bruker til daglig. Android har, i motsetning til iOS, i årevis tillatt flere appbutikker å sameksistere i økosystemet, noe som gir deg friheten til å finne og installere apper fra dine favorittkilder.



I denne veiledningen skal vi ta en titt på F-droid, en applikasjonskatalog som representerer et alternativ til applikasjonsbutikker som Google Play Store og Microsoft Store.



## Komme i gang med F-Droid



F-Droid er en applikasjons- og verktøybutikk som lar deg installere gratis applikasjoner med åpen kildekode på Android-plattformen. F-droid er et åpen kildekode-prosjekt som ble startet i 2010 av Ciaran Gultnieks og flere andre bidragsytere. Hovedmålet med prosjektet er å gjøre applikasjoner med åpen kildekode tilgjengelige, og å gjøre det mulig for initiativtakere til åpen kildekode-prosjekter å finne en plattform der de kan publisere verktøyene sine uten å måtte henvise til Google Play Store.



F-Droid er dessverre ikke et program som er tilgjengelig på iOS, og inneholder mange verktøy designet for Android-systemer.



Du kan laste ned F-droid fra [det offisielle nettstedet] (https://f-droid.org/) i APK-format og installere det manuelt på Android-telefonen din.



![download](assets/fr/02.webp)



På Android må du sørge for at du gir installasjonstillatelser for nettleseren du lastet ned F-Droid fra.



Når installasjonen er fullført, vil F-Droid starte en oppdatering av Open Source-applikasjonskatalogene for å berike applikasjonene i butikken.



![repositories](assets/fr/03.webp)



Du kan nå installere programmer på telefonen uten å gå via Google Play Store.



## F-Droid-bokhandelen



I applikasjonsbutikken finner du flere kategorier av applikasjoner som passer til dine behov. Under fanen **Kategorier** finner du over 20 typer applikasjoner, fra nettlesere til fritekstredigeringsprogrammer, som alle krever minimalt med informasjon fra din side.



Ønsker du å installere en bestemt applikasjon? Klikk på knappen **Søk**, og skriv deretter inn navnet på programmet du leter etter.



![search](assets/fr/04.webp)



F-Droid gir omfattende informasjon om alle applikasjoner du ønsker å installere.



Ved å klikke på applikasjonen finner du blant annet:




- Funksjoner og endringer som er lagt til i den nyeste tilgjengelige versjonen
- En detaljert beskrivelse av applikasjonen, dens funksjoner, grunnene til å bruke den og Open Source-fellesskapet som står bak prosjektet.



![features](assets/fr/05.webp)





- Lisensen som brukes av prosjektet, lenker til kildekoden og til problemer som oppstår ved bruk av applikasjonen
- Tillatelser som kreves av applikasjonen



![permissions](assets/fr/06.webp)



Finn ut mer i vår Thunderbird-veiledning:



https://planb.network/tutorials/computer-security/communication/thunderbird-91d02325-0361-4641-b152-8975890284a8

F-Droid gir deg all den informasjonen du trenger for å avgjøre om bruken av en applikasjon beskytter dataene dine og forbedrer personvernet ditt. Skann alle applikasjonene du ønsker å bruke, og klikk deretter på **Install**-knappen for å laste ned og installere applikasjonen.


Gi F-Droid installasjonsrettigheter ved å aktivere alternativet i innstillingene dine.



![settings](assets/fr/07.webp)



## Exchange-applikasjonene dine



F-Droid oppmuntrer til åpen kildekode og bidrag fra lokalsamfunnet, særlig via alternativet **Near By** Exchange. Koble deg til brukerne rundt deg via:




- Bluetooth-deteksjon;
- Det samme Wi-Fi-nettverket;
- QR-kode eller IP:PORT Address for å gå inn i nettleseren din.



Med dette alternativet kan du dele og motta applikasjoner som er installert på Android-telefonen din, med venner og familie på bare noen få trinn.



![swap](assets/fr/08.webp)



## Oppdateringer



Under fanen **Oppdatering** finner du en liste over tilgjengelige oppdateringer, og du bør også lese informasjonen om nye versjoner av hvert program for å finne ut om det har skjedd noen større endringer i den versjonen du bruker.



![updates](assets/fr/09.webp)



Du kan også oppdatere listen over tilgjengelige programmer ved å oppdatere siden (bla nedover).



## Legg til dine egne applikasjoner



F-Droid er et Open Source-prosjekt som oppfordrer til å bidra til applikasjoner som prioriterer brukernes personvern. Du kan legge til din egen Android-mobilapp i butikken ved å bidra til kildekoden i F-Droid GitLab.



Applikasjonen din må være åpen kildekode, med kildekoden offentlig tilgjengelig på for eksempel GitHub eller GitLab.


Du må deretter utarbeide en YAML-fil (metadataene) som beskriver applikasjonen din, inkludert all informasjon og alle tillatelser som kreves for å bruke den, i henhold til [metadatamalen] (https://f-droid.org/docs/Build_Metadata_Reference/) som er foreslått av F-Droid.



I **Developers**-delen av [documentation](https://f-droid.org/en/docs/) finner du alle ressursene du trenger for å publisere og vedlikeholde applikasjonene dine på F-Droid.



### Integritet og sikkerhet



Å legge en applikasjon i åpen kildekode er ofte synonymt med økt sikkerhet, men også med betydelig risiko. Hvordan kan du sikre at det ikke finnes ondsinnede endringer i kildekoden til en applikasjon som er tilgjengelig på F-Droid?



F-Droid kompilerer applikasjoner på sine egne servere, basert på den offisielle kildekoden og kompileringsinstruksjonene. Hver publiserte applikasjon gjenoppbygges og verifiseres for å sikre at den ikke har blitt kompromittert. Dette sikrer at APK-en som tilbys er tro mot kildekoden som er publisert av utviklerne. I tillegg er hver applikasjon som installeres via F-Droid digitalt signert, og deretter sammenlignes signaturfingeravtrykket med det som er kunngjort av applikasjonens utviklere på det offisielle nettstedet eller på Git-depotet.



Hvis du likte denne veiledningen, kan du lese mer om kurset vårt i IT-sikkerhet og datahåndtering:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1