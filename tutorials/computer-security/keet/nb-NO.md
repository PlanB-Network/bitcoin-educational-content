---
name: Keet
description: Peer-to-peer-chat
---
![cover](assets/cover.webp)



Keet er en applikasjon for direktemeldinger som er designet for å fungere uten servere. Applikasjonen ble lansert i 2022 av Holepunch (et selskap finansiert av Tether og Bitfinex), og er i sin helhet basert på et peer-to-peer-nettverk og har en radikalt desentralisert tilnærming: meldinger, samtaler og filer utveksles direkte mellom brukerne, uten mellomledd.



Keet krypterer all kommunikasjon fra ende til ende og ber ikke om personopplysninger. Registreringen er anonym, og det kreves verken telefonnummer eller e-postadresse. I tillegg til utveksling av tekstmeldinger tilbyr Keet videosamtaler av svært høy kvalitet, samt ubegrenset fildeling. Applikasjonen kan derfor brukes på en hybrid måte, både til privat og profesjonell bruk.



![Image](assets/fr/01.webp)



For øyeblikket (april 2025) er Keet ikke helt åpen kildekode. Noe av kildekoden er tilgjengelig på [Holepunchs GitHub-repository] (https://github.com/holepunchto), særlig kryptografi- og nettverkskomponentene, men klienten Interface er ikke det ennå. Holepunch har imidlertid kunngjort at de har til hensikt å gjøre hele applikasjonen åpen kildekode etter hvert. Avhengig av når du oppdager denne veiledningen, kan dette allerede ha blitt gjort.




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



## Installer Keet



Keet er tilgjengelig på alle plattformer. Du kan laste ned applikasjonen direkte fra appbutikken på telefonen din:




- [Google Play] (https://play.google.com/store/apps/details?id=io.keet.app&pli=1);
- [App Store] (https://apps.apple.com/us/app/keet-by-holepunch/id6443880549);



På Android er det også mulig å [installere via APK] (https://github.com/holepunchto/keet-mobile-releases/releases).



I denne veiledningen konsentrerer vi oss om mobilversjonen, men vær oppmerksom på at [datamaskinversjoner også er tilgjengelige](https://keet.io/) (MacOS, Linux og Windows). Det er også mulig å synkronisere kontoen din på flere enheter.



## Opprett en konto på Keet



Ved første lansering kan du ignorere presentasjonsskjermene.



![Image](assets/fr/02.webp)



Klikk på knappen "*Jeg er en ny bruker*".



![Image](assets/fr/03.webp)



Godta vilkårene for bruk, og klikk deretter på "*Hurtigoppsett*".



![Image](assets/fr/04.webp)



Velg et navn eller kallenavn, og klikk deretter på "*Fullfør oppsett*".



![Image](assets/fr/05.webp)



Profilen din er nå opprettet. Klikk på "*Fullfør oppsett*" igjen for å fullføre.



![Image](assets/fr/06.webp)



Du kan når som helst tilpasse profilen din under fanen "*Profil*".



## Lagre Keet-kontoen din



Det første du må gjøre med den nye Keet-kontoen din, er å lagre gjenopprettingsfrasen din. Dette er en sekvens på 24 ord som gjør det mulig for deg å gjenopprette tilgangen til kontoen din hvis du skulle miste den eller bytte enhet. Denne frasen gir full tilgang til kontoen din til alle som kjenner til den, så det er viktig å ta en pålitelig sikkerhetskopi og aldri røpe den.



Dette gjør du ved å klikke på "*Profil*"-fanen nederst til høyre i Interface.



![Image](assets/fr/07.webp)



Åpne deretter menyen "*Innstillinger*".



![Image](assets/fr/08.webp)



Velg "*Privatliv og sikkerhet*".



![Image](assets/fr/09.webp)



Klikk deretter på "*Gjenopprettingsfrase*".



![Image](assets/fr/10.webp)



Trykk på knappen "*Vis frase*" for å vise gjenopprettingsfrasen din. Kopier den nøye og oppbevar den på et trygt sted.



![Image](assets/fr/11.webp)



## Sende meldinger med Keet



For å kommunisere på Keet må du opprette "*Rom*". Dette gjør du ved å klikke på blyantikonet øverst til høyre i Interface.



![Image](assets/fr/12.webp)



Velg "*Ny gruppechat*".



![Image](assets/fr/13.webp)



Velg et navn og en beskrivelse for "*Room*", og klikk deretter på "*Opprett gruppechat*".



![Image](assets/fr/14.webp)



Ditt "*Rom*" er nå opprettet. Klikk på "*+*"-ikonet øverst til høyre for å invitere deltakere.



![Image](assets/fr/15.webp)



Definer hvilke rettigheter du vil gi nye medlemmer via invitasjonslenken, samt hvor lenge lenken skal være gyldig. Klikk deretter på "*generate-invitasjon*".



![Image](assets/fr/16.webp)



Keet vil generate en lenke for å bli med i "*Rommet*" ditt. Du kan enten kopiere den og dele den, eller få QR-koden skannet av personene du ønsker å invitere.



![Image](assets/fr/17.webp)



Du kan nå begynne å utveksle meldinger og multimediefiler. For å starte en samtale klikker du på telefonikonet øverst i høyre hjørne.



![Image](assets/fr/18.webp)



Fra denne gruppen kan du også sende private meldinger til et bestemt medlem. Klikk på gruppens profilbilde, og velg deretter ønsket medlem i delen "*Members*".



![Image](assets/fr/19.webp)



Klikk på knappen "*Send DM-forespørsel*", og skriv inn meldingen din.



![Image](assets/fr/20.webp)



Når DM-forespørselen er akseptert, finner du denne kontakten på startsiden, der du kan snakke med ham privat.



![Image](assets/fr/21.webp)



## Synkroniser kontoen din på flere enheter



Nå som du vet hvordan du bruker Keet og har en konto, kan du også synkronisere den på en annen enhet, for eksempel en datamaskin. Dette gjør du ved å åpne applikasjonen på mobilen, klikke på "*Profil*" og gå til "*Innstillinger*".



![Image](assets/fr/22.webp)



Gå deretter til menyen "*Mine enheter*".



![Image](assets/fr/23.webp)



Klikk på "*Legg til enhet*". Keet vil generate en lenke for å synkronisere en ny enhet. Kopier denne koblingen.



![Image](assets/fr/24.webp)



Installer Keet på den andre enheten din. På startskjermen velger du alternativet "*Jeg er en nåværende bruker*".



![Image](assets/fr/25.webp)



Klikk deretter på "*Link device*".



![Image](assets/fr/26.webp)



Lim inn lenken fra den første enheten din, og klikk deretter på "*Start synkronisering*".



![Image](assets/fr/27.webp)



På den første enheten klikker du på "*Bekreft koblingsenheter*" for å godkjenne tilkoblingen.



![Image](assets/fr/28.webp)



På den andre enheten fullfører du prosessen ved å klikke på "*Link devices*".



![Image](assets/fr/29.webp)



Du kan nå få tilgang til alle dine "*Room*" og samtaler fra denne nye enheten.



![Image](assets/fr/30.webp)



Gratulerer, du er nå i gang med å bruke Keet messaging, et flott alternativ til WathsApp! Hvis du synes denne veiledningen var nyttig, vil jeg være veldig takknemlig hvis du legger igjen en Green-tommel nedenfor. Del gjerne denne veiledningen på dine sosiale nettverk. Tusen takk skal du ha!



Jeg anbefaler også denne andre veiledningen, der jeg introduserer deg for Proton Mail, et mye mer personvernvennlig alternativ til Gmail:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2