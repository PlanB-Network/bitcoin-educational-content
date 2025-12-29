---
name: Alby

description: Nettleserutvidelse for Bitcoin og Lightning Network
---

![cover](assets/cover.webp)




Å gjøre betalinger stadig enklere med bitcoin er utfordringen mange selskaper i sektoren står overfor. Alby skiller seg ut fra mengden med sin Alby wallet-utvidelse for nettlesere. Denne utvidelsen har som mål å sette opp et flytende rammeverk som automatisk oppdager adresser og lar deg foreta friksjonsløse bitcoin-betalinger. I denne veiledningen utforsker vi Alby-utvidelsen og tester hvordan den muliggjør betalinger fra nettleseren.




![video](https://youtu.be/nd5fX2vHuDw)




## Alby forlengelse



Alby-utvidelsen er et verktøy som gjør det mulig for nettleseren din å samhandle enkelt og sikkert med Bitcoin-nettverket og dets Lightning Network-lag. Det kjennetegnes av tre aspekter:




- Lightning Network wallet: Koble til Alby-noden eller -kontoen din for å sende og motta bitcoin raskt og billig via Lightning Network-laget.
- Flytende betalinger via nettet: Det eliminerer behovet for å skanne QR-koder eller bytte mellom applikasjoner for bitcoin-betalinger på nettsteder som støtter Lightning. Det muliggjør smidige transaksjoner med ett enkelt klikk, eller uten bekreftelse hvis du har satt opp et budsjett.
- En Nostr-administrator: Utvidelsen administrerer Nostr-nøklene dine, noe som gjør det enkelt å koble til og samhandle med Nostr-applikasjoner som fungerer som en sikker signatar uten å eksponere den private nøkkelen din for alle plattformer.



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Koble til utvidelsen



I denne veiledningen bruker vi Alby-utvidelsen i Firefox-nettleseren under et Ubuntu-operativsystem. Den er imidlertid også tilgjengelig på Windows og med nettlesere som Chrome.



Du kan legge til Alby-utvidelsen i nettleseren din ved å gå til [Firefox]-utvidelsesbutikken (https://addons.mozilla.org/fr/firefox/addon/alby/) eller [Chrome]-utvidelsesbutikken (https://chromewebstore.google.com/detail/alby-bitcoin-wallet-for-l/iokeahhehimjnekafflcihljlcjccdbe).



![firefox](assets/fr/01.webp)



![chrome](assets/fr/02.webp)



ℹ️ Det er viktig å sjekke at forfatteren av utvidelsen faktisk er den offisielle Alby-kontoen, for å unngå enhver form for piratkopiering eller tyveri av bitcoinsene dine.



Legg til utvidelsen i nettleseren din ved å klikke på knappen til høyre.


Gi de nødvendige tillatelsene til å installere og bruke utvidelsen, og fest deretter utvidelsen til verktøylinjen for enkel gjenfinning.



![pin](assets/fr/03.webp)



Du bør også definere en opplåsingskode (svært viktig), som garanterer sikker tilgang til Lightning wallet fra nettleseren din. Vi foreslår at du angir et sterkt alfanumerisk passord.



ℹ️ Lagre dette passordet på et trygt sted slik at du har tilgang til det hvis du glemmer det, ettersom det kan endres, men ikke hentes frem igjen.



https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

![pass](assets/fr/04.webp)



Alby demonstrerer sin tilpasningsevne ved å tilby deg to valg:




- Fortsett med en Alby-konto hvis du vil ha glede av applikasjonene samtidig som du beholder kontrollen over bitcoinsene dine.
- Koble til din egen wallet- eller Lightning-node hvis du allerede har en som støttes av utvidelsen.



https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


I denne veiledningen velger vi å fortsette med Alby-kontoen for å dra nytte av funksjonene i Alby-økosystemet.



https://planb.academy/tutorials/wallet/mobile/alby-go-40202802-b346-4a3c-9863-465c3bde9903

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Logg inn på Alby-kontoen din, eller opprett en hvis du ikke har en ennå.



![signup](assets/fr/05.webp)



## Gjør dine første innbetalinger



Når du er logget inn, kan du klikke på Alby-utvidelsen i verktøylinjen for å få tilgang til porteføljen din.



![buzzin](assets/fr/06.webp)



Når du har opprettet en Alby-konto, må du koble den til en wallet for å kunne bruke satoshier. For å koble bitcoin wallet til Alby-kontoen din, foreslår vi at du bruker en Alby Hub-node, som du enten kan sette opp på datamaskinen din eller abonnere på et abonnement som tilbys av Alby.



![hubplan](assets/fr/13.webp)




I denne veiledningen støttes Alby-kontoen vår av en lokal installasjon på maskinen vår.


Hvis du vil bygge din egen Alby-node, anbefaler vi vår Alby Hub-veiledning.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Med denne noden kan du opprette selvforvaltende Lightning-porteføljer og effektivt administrere Lightning-kanalene dine for å sende og motta satoshier.



![channels](assets/fr/14.webp)



Åpne mottakskanaler som definerer det totale antallet satoshier du kan motta.



![receivechanal](assets/fr/15.webp)



Åpne sendekanaler ved å blokkere satoshier på en bitcoin onchain-adresse. Satoshiene du har blokkert, definerer det totale antallet satoshier du kan bruke.



![spend](assets/fr/16.webp)



Du kan nå sende og motta satoshier via Alby-utvidelsen.



![exchange](assets/fr/08.webp)



Fra dette tidspunktet kan Alby-utvidelsen oppdage Lightning-adresser og fakturaer som er tilgjengelige på nettsidene du besøker, og vil foreslå at du betaler dem i bitcoin eller Lightning direkte fra utvidelsen din.



![suggest](assets/fr/09.webp)



![pay](assets/fr/10.webp)




## Sikring av gjenopprettingsnøkler med hovednøkkelen



Hovednøkkelen som tilbys av Alby-utvidelsen, fungerer som et beskyttende overlegg som gjør det mulig å kommunisere sikkert med hovednettverkslaget Bitcoin (Onchain), Nostr-systemet og gjør det mulig å aktivere Lightning-tilkoblingen med Nostr-applikasjoner.



![masterKey](assets/fr/11.webp)



Denne hovednøkkelen består av 12 ord som ligner på gjenopprettingsfrasen din. Vi anbefaler derfor at du lagrer den på en sikker måte for å sikre at du alltid har tilgang til den.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


![masterKey](assets/fr/12.webp)



Du kan nå oppleve friksjonsfrie bitcoin- og Lightning-betalinger med Alby-utvidelsen. Hvis du likte denne veiledningen, anbefaler vi Alby Hub-veiledningen vår for å sette opp din egen Alby-node og kontrollere alle aspekter av Alby-lommebøkene dine fra et enkelt og kraftig grensesnitt.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a