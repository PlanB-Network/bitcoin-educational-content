---
name: Signal
description: Uttrykk deg fritt
---
![cover](assets/cover.webp)



Signal er en ende-til-ende-kryptert meldingsapplikasjon som er utviklet for å tilby god konfidensialitet som standard. Alle meldinger, samtaler og filer er beskyttet av Signal-protokollen, som er anerkjent som en av de mest robuste meldingsprotokollene. Den gjenbrukes av mange andre applikasjoner, blant annet WathsApp, Facebook Messenger, Skype og Google Messages for RCS-kommunikasjon.



Signal ble lansert i 2014 av Moxie Marlinspike (pseudonym) og har siden 2018 blitt utviklet av Signal Foundation, en ideell organisasjon som ble opprettet med støtte fra Brian Acton (medgrunnlegger av WhatsApp).



![Image](assets/fr/01.webp)



Sammenlignet med WhatsApp skiller Signal seg ut ved sin åpenhet: Applikasjonens kode, både på klient- og serversiden, er helt åpen kildekode. Dette gjør det mulig for hvem som helst å kontrollere den, og spesielt å sjekke at krypteringen brukes som annonsert.



Signal er imidlertid avhengig av å bruke et telefonnummer, noe som er den største svakheten når det gjelder anonymitet sammenlignet med andre løsninger. Til tross for dette er applikasjonen etter min mening en av de mest pålitelige når det gjelder sikkerhet og konfidensialitet, takket være den helt åpne arkitekturen og en allment vedtatt krypteringsprotokoll, og den er derfor testet og revidert, i motsetning til andre mer marginale applikasjoner.



| Applikasjon          | E2EE 1:1       | E2EE grupper   | Anonym registrering | Åpen kildekode klient-lisens | Åpen kildekode server-lisens | Desentralisert server    | Opprettelsesår    |
| -------------------- | -------------- | -------------- | ------------------- | ---------------------------- | ---------------------------- | ------------------------ | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                            | ❌                            | ❌                        | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                            | ❌                            | ❌                        | 2011              |
| Facebook Messenger   | ✅              | 🟡 (valgfri)   | ❌                   | ❌                            | ❌                            | ❌                        | 2011              |
| Telegram             | 🟡 (valgfri)   | ❌              | 🟡                  | ✅                            | ❌                            | ❌                        | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                            | ❌                            | ❌                        | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                            | ✅                            | ❌                        | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                            | ❌                            | ❌                        | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                            | ✅                            | 🟡 (føderert)           | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                            | N/A                          | 🟡 (via e-post)         | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                            | ✅                            | 🟡 (føderert)           | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                            | ✅                            | ✅                        | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                            | ✅                            | ✅                        | 2021              |
| Olvid                | ✅              | ✅              | ✅                   | ✅                            | ❌                            | 🟡(ingen katalog)      | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                            | N/A                          | ✅                        | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                            | N/A                          | ✅                        | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                            | N/A                          | ✅                        | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                            | N/A                          | ✅                        | 2013              |

*E2EE = ende-til-ende-kryptering*




## Installer Signal-applikasjonen



Signal er tilgjengelig på alle plattformer. Du kan laste ned applikasjonen direkte fra applikasjonsbutikken på telefonen din:




- [Google Play] (https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms);
- [App Store] (https://apps.apple.com/us/app/signal-private-messenger/id874139669);



På Android er det også mulig å [installere via APK] (https://github.com/signalapp/Signal-Android/releases).



I denne veiledningen konsentrerer vi oss om mobilversjonen, men vær oppmerksom på at [desktop-versjoner også er tilgjengelige](https://signal.org/fr/download/) (MacOS, Linux og Windows). Du må imidlertid først konfigurere mobilapplikasjonen før du kan synkronisere kontoen din med skrivebordsversjonen.



## Opprett en konto på Signal



Når du starter programmet for første gang, klikker du på knappen "*Fortsett*".



![Image](assets/fr/02.webp)



Skriv inn telefonnummeret ditt, og klikk deretter på "*Neste*".



![Image](assets/fr/03.webp)



Du får tilsendt en bekreftelseskode på SMS. Skriv inn denne koden i Signal-applikasjonen.



![Image](assets/fr/04.webp)



Velg en PIN-kode for å sikre Signal-kontoen din. Denne koden krypterer dataene dine, og kan brukes til å gjenopprette tilgangen til kontoen din hvis du mister enheten din. Det er derfor viktig å velge en robust PIN-kode som er så lang og tilfeldig som mulig, og å føre en pålitelig oversikt over den.



![Image](assets/fr/05.webp)



Bekreft PIN-koden en gang til.



![Image](assets/fr/06.webp)



Du kan nå tilpasse brukerprofilen din. Velg et bilde, skriv inn navnet ditt eller et kallenavn. På dette stadiet kan du også definere hvem som kan finne deg på Signal via nummeret ditt. Velg "*Alle*" hvis du vil være synlig, eller "*Ingen*" hvis du ikke vil kunne spores via telefonnummeret ditt (du kan da bare legges til med "*Brukernavn*"). Når du har gjort dine valg, klikker du på "*Neste*".



![Image](assets/fr/07.webp)



Du er nå koblet til Signal og klar til å sende Exchange-meldinger.



![Image](assets/fr/08.webp)



## Sette opp Signal-kontoen din



Klikk på profilbildet ditt øverst i venstre hjørne for å få tilgang til applikasjonsinnstillingene.



![Image](assets/fr/09.webp)



I menyen "*Account*" kan du administrere profilinnstillingene dine. Jeg anbefaler at du beholder standardinnstillingene. Du kan også aktivere alternativet "*Registreringslås*", som beskytter kontoen din mot visse typer angrep. Denne menyen inneholder også alternativene du trenger for å overføre kontoen din til en ny enhet.



![Image](assets/fr/10.webp)



Hvis du klikker på profilbildet ditt i innstillingene igjen, kommer du til alternativene for å tilpasse profilen din. Jeg anbefaler at du angir et "*Brukernavn*": Dette vil gjøre det mulig for deg å komme i kontakt med andre uten å oppgi telefonnummeret ditt.



![Image](assets/fr/11.webp)



Ved å velge "*QR-kode eller lenke*" får du informasjonen du trenger for å dele med noen som ønsker å legge deg til i Signal.



![Image](assets/fr/12.webp)



Menyen "*Privacy*" er spesielt viktig. Her finner du alternativer for å kontrollere synligheten til nummeret ditt, administrasjonen av meldingene dine med kontaktene dine, samt ulike autorisasjoner som er gitt i applikasjonen.



![Image](assets/fr/13.webp)



Utforsk gjerne menyene "*Autseende*", "*Chatter*" og "*Varsler*" for å skreddersy Interface og programmets funksjonalitet til dine personlige behov.



## Koble til skrivebordsapplikasjonen



For å koble til skrivebordsapplikasjonen må du starte med å installere programvaren på datamaskinen (se første del av denne veiledningen). Deretter går du til Innstillinger på telefonen og åpner delen "*Linked devices*".



![Image](assets/fr/14.webp)



Klikk på knappen "*Lenke til en ny enhet*".



![Image](assets/fr/15.webp)



Start programvaren på datamaskinen din, og skann deretter QR-koden som vises på skjermen med telefonen. Hvis du ønsker å importere samtalene dine, velger du alternativet "*Overfør meldingshistorikk*".



![Image](assets/fr/16.webp)



Enhetene dine er nå fullstendig synkronisert.



![Image](assets/fr/17.webp)



## Sende meldinger med Signal



For å kommunisere med noen på Signal må du først legge dem til som en kontakt. Det finnes flere alternativer: Du kan legge dem til via telefonnummeret deres (hvis personen har aktivert muligheten for å bli funnet på denne måten), eller du kan bruke Signal-ID-en deres.



Klikk på blyantikonet nederst i høyre hjørne av Interface.



![Image](assets/fr/18.webp)



I mitt tilfelle ønsker jeg å legge til personen etter brukernavn. Så jeg klikker på "*Finn etter brukernavn*".



![Image](assets/fr/19.webp)



Deretter kan du enten lime inn påloggingen eller skanne QR-koden.



![Image](assets/fr/20.webp)



Send ham en melding for å opprette kontakt.



![Image](assets/fr/21.webp)



Samtalen vises deretter på startsiden. Hvis personen godtar kontaktforespørselen din, ser du navnet og profilbildet deres.



![Image](assets/fr/22.webp)



Gratulerer, du er nå i gang med å bruke Signal-meldinger, et flott alternativ til WathsApp! Hvis du synes denne veiledningen var nyttig, vil jeg være veldig takknemlig hvis du legger igjen en Green-tommel nedenfor. Del gjerne denne veiledningen på dine sosiale nettverk. Tusen takk skal du ha!



Jeg anbefaler også denne andre veiledningen, der jeg introduserer deg for Proton Mail, et mye mer personvernvennlig alternativ til Gmail:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2