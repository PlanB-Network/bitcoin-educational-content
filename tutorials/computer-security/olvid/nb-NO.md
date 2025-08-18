---
name: Olvid
description: Private meldinger for alle
---
![cover](assets/cover.webp)



Olvid er en fransk direktemeldingsapplikasjon som ble lansert i 2019, og som er designet for å tilby et høyt sikkerhetsnivå uten å gå på akkord med personvernet. I motsetning til WhatsApp eller Signal ber Olvid ikke om personopplysninger ved registrering: ikke noe telefonnummer, ingen e-post, ingenting. Identifikasjon mellom brukere er basert på en Exchange-nøkkel, uten katalogserver eller delt Address-bok.



Alle meldinger krypteres fra ende til ende ved hjelp av en original kryptografisk protokoll, som også beskytter metadata: Ingen vet hvem du snakker med, eller når. Klientkoden er åpen kildekode, men den sentrale serveren som brukes til å rute krypterte meldinger, er fortsatt proprietær og ligger hos AWS.

Olvid sitt sikkerhetsmodell bygger på et viktig prinsipp: fraværet av enhver betrodd tredjepart i etableringen av digitale identiteter. I motsetning til de fleste krypterte meldingsapper som bruker et sentralisert register for å administrere brukeridentiteter, er ikke Olvid avhengig av noen sentral infrastruktur for å sikre integriteten i kommunikasjonen. Denne arkitekturen eliminerer dermed risikoen forbundet med kompromittering av et slikt register.

Olvid benytter imidlertid en sentral server for meldingsdistribusjon, men denne er strengt begrenset til en logistisk rolle: den sørger for asynkron overføring av krypterte meldinger. Serveren deltar ikke i noen krypteringsprosess, kjenner verken brukernes virkelige identitet eller innholdet eller metadataene i meldingene (bortsett fra mottakerens offentlige nøkkel som trengs for ruting). Den kan derfor anses som fiendtlig per definisjon, uten at det svekker sikkerheten. Selv om den skulle kompromitteres, gir den ikke tilgang til innholdet i kommunikasjonen. Olvid sentraliserer meldingsdistribusjonen (av hensyn til effektivitet og tjenestekvalitet), men garanterer en sikkerhet som er uavhengig av denne infrastrukturen.


Olvid tilbyr en gratisversjon og en abonnementsversjon til 4,99 euro per måned. Gratisversjonen tilbyr full funksjonalitet, med unntak av å foreta lyd- og videosamtaler (selv om det er mulig å motta dem), og tillater ikke kontosynkronisering på tvers av flere enheter. Så hvis du planlegger å bruke smarttelefonen din utelukkende, og ikke trenger å ringe, er Olvid en utmerket løsning.



Olvid er sertifisert av ANSSI (den franske cybersikkerhetsmyndigheten). Denne applikasjonen er et utmerket alternativ til tradisjonelle meldingstjenester (WhatsApp, Facebook Messenger, WeChat...) for de som ønsker personvern samtidig som det er enkelt å bruke.


| Applikasjon          | E2EE 1:1     | E2EE grupper | Anonym registrering | Åpen kildekode klient-lisens | Åpen kildekode server-lisens | Desentralisert server | Opprettelsesår |
| -------------------- | ------------ | ------------ | ------------------- | ---------------------------- | ---------------------------- | --------------------- | -------------- |
| WhatsApp             | ✅            | ✅            | ❌                   | ❌                            | ❌                            | ❌                     | 2009           |
| WeChat               | ❌            | ❌            | ❌                   | ❌                            | ❌                            | ❌                     | 2011           |
| Facebook Messenger   | ✅            | 🟡 (valgfri) | ❌                   | ❌                            | ❌                            | ❌                     | 2011           |
| Telegram             | 🟡 (valgfri) | ❌            | 🟡                  | ✅                            | ❌                            | ❌                     | 2013           |
| LINE                 | ✅            | ✅            | ❌                   | ❌                            | ❌                            | ❌                     | 2011           |
| Signal               | ✅            | ✅            | ❌                   | ✅                            | ✅                            | ❌                     | 2014           |
| Threema              | ✅            | ✅            | ✅                   | ✅                            | ❌                            | ❌                     | 2012           |
| Element (Matrix)     | ✅            | ✅            | ✅                   | ✅                            | ✅                            | 🟡 (føderert)         | 2016           |
| Delta Chat           | ✅            | ✅            | ✅                   | ✅                            | N/A                          | 🟡 (via e-post)       | 2017           |
| Conversations (XMPP) | ✅            | ✅            | ✅                   | ✅                            | ✅                            | 🟡 (føderert)         | 2014           |
| Session              | ✅            | ✅            | ✅                   | ✅                            | ✅                            | ✅                     | 2020           |
| SimpleX              | ✅            | ✅            | ✅                   | ✅                            | ✅                            | ✅                     | 2021           |
| **Olvid**            | **✅**        | **✅**        | **✅**               | **✅**                        | **❌**                        | 🟡(ingen katalog)     | **2019**       |
| Keet                 | ✅            | ✅            | ✅                   | ❌                            | N/A                          | ✅                     | 2022           |
| Jami                 | ✅            | ✅            | ✅                   | ✅                            | N/A                          | ✅                     | 2005           |
| Briar                | ✅            | ✅            | ✅                   | ✅                            | N/A                          | ✅                     | 2018           |
| Tox                  | ✅            | ✅            | ✅                   | ✅                            | N/A                          | ✅                     | 2013           |

*E2EE = ende-til-ende-kryptering*



## Installer Olvid-applikasjonen



Olvid er tilgjengelig på alle plattformer. Du kan laste ned applikasjonen direkte fra appbutikken på telefonen din:




- [Google Play] (https://play.google.com/store/apps/details?id=io.olvid.messenger);
- [App Store] (https://apps.apple.com/app/olvid/id1414865219);



På Android er det også mulig å [installere via APK] (https://www.olvid.io/download/).



I denne veiledningen konsentrerer vi oss om mobilversjonen, men vær oppmerksom på at [datamaskinversjoner også er tilgjengelige](https://www.olvid.io/download/) (MacOS, Linux og Windows). Hvis du velger betalingsversjonen, kan du synkronisere kontoen din på flere enheter.



![Image](assets/fr/01.webp)



## Opprett en konto på Olvid



Når du starter programmet for første gang, klikker du på knappen "*Jeg er en ny bruker*".



![Image](assets/fr/02.webp)



Velg et kallenavn eller skriv inn for- og etternavnet ditt.



![Image](assets/fr/03.webp)



Legg til et profilbilde.



![Image](assets/fr/04.webp)



Kontoen din er nå opprettet.



![Image](assets/fr/05.webp)



For å forhindre tap av tilgang til Olvid-kontoen din, anbefaler vi at du setter opp automatiske sikkerhetskopier. Dette gjør du ved å åpne innstillingene ved å klikke på de tre prikkene øverst til høyre i Interface, og deretter velge "*Innstillinger*".

⚠️ **Advarsel**: siden Olvid versjon 3.7 har prosedyren for å sikkerhetskopiere profilene og kontaktene dine blitt erstattet av en ny. Denne veiledningen presenterer fortsatt den gamle versjonen. Du kan oppdage den nye versjonen i deres FAQ: [💾 Sikkerhetskopiere profilene dine](https://www.olvid.io/faq/sauvegarder-vos-profils/)

![Image](assets/fr/06.webp)



Gå til menyen "*Lagre taster og kontakter*".



![Image](assets/fr/07.webp)



Klikk deretter på "*generate en sikkerhetskopinøkkel*". Denne nøkkelen krypterer sikkerhetskopiene dine. Hvis du trenger å gjenopprette kontoen din på en annen enhet og ikke lenger har tilgang til den, trenger du både en sikkerhetskopi og denne nøkkelen for å dekryptere den.



![Image](assets/fr/08.webp)



Oppbevar denne nøkkelen på et sikkert sted. Du kan også ta en papirkopi.



![Image](assets/fr/09.webp)



Du kan deretter velge å lage en lokal sikkerhetskopi eller en automatisk sikkerhetskopi på en skytjeneste. Det andre alternativet anbefales på det sterkeste for å garantere tilgang til Olvid-kontoen din under alle omstendigheter, selv om du mister telefonen.



![Image](assets/fr/10.webp)



Kontroller at alternativet "*Aktiver automatisk sikkerhetskopiering*" er merket av.



![Image](assets/fr/11.webp)



Du kan også utforske de andre innstillingene som er tilgjengelige for å tilpasse programmet til dine behov.



![Image](assets/fr/12.webp)



## Sende meldinger med Olvid



For å kunne sende meldinger må du først legge til kontakter. Klikk på den blå "*+*"-knappen på startsiden.



![Image](assets/fr/13.webp)



Olvid viser deretter bruker-ID-en din. Den kan du så gi videre til dem du ønsker å kommunisere med, slik at de kan legge deg til som kontakt.



Du kan legge til en person ved å skanne ID-en med kameraet eller lime den inn manuelt ved å klikke på de tre små prikkene øverst i høyre hjørne.



![Image](assets/fr/14.webp)



Når ID-en er skannet, kan du enten be kontakten din om å skanne QR-koden som vises, eller sende dem en forespørsel om ekstern tilkobling ved å klikke på "*Fjernkontakt*".



![Image](assets/fr/15.webp)



Forbindelsen er nå opprettet.



![Image](assets/fr/16.webp)



Nå kan du begynne å utveksle meldinger og annet innhold med korrespondenten din!



![Image](assets/fr/17.webp)



Fra startsiden finner du alle samtalene dine.



![Image](assets/fr/18.webp)



Den andre fanen inneholder alle kontaktene dine.



![Image](assets/fr/19.webp)



Du kan også opprette gruppediskusjoner.



![Image](assets/fr/20.webp)



Gratulerer, du er nå i gang med å bruke Olvid messaging, et flott alternativ til WathsApp! Hvis du synes denne veiledningen var nyttig, vil jeg være veldig takknemlig hvis du legger igjen en Green-tommel nedenfor. Del gjerne denne veiledningen på dine sosiale nettverk. Tusen takk skal du ha!



Jeg anbefaler også denne andre veiledningen, der jeg introduserer deg for Proton Mail, et mye mer personvernvennlig alternativ til Gmail :



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2