---
name: Wallet av Satoshi
description: Den enkleste Wallet for å komme i gang
---
![cover](assets/cover.webp)

_Denne opplæringen ble skrevet av_ [Bitcoin Campus] (https://linktr.ee/bitcoincampus_)


## Nedlasting, konfigurering og bruk av Wallet i Satoshi


Wallet av Satoshi er en Lightning Network Wallet, forvaring og veldig enkel å bruke.

I forbindelse med kurset [BTC105 - Finding Now] (https://planb.network/it/courses/trovarsi-ora-d1370810-63f6-4aba-b822-e3a66bf225a5) brukes det til Redeem Lightning Network-kuponger.


**Husk alltid**: _ikke nøklene dine, ikke myntene dine_


Depotlommebøker gir ikke brukerne full kontroll over midlene sine. De anbefales normalt ikke, bortsett fra for nybegynnere. WoS bør brukes som en overgangs-Wallet eller til å oppbevare lommepenger, ikke til langsiktig fondsoppbygging.


---

Wallet of Satoshi (WoS) er et depotprodukt, men det har et visst omdømme. Det er rimelig at vi kan benytte oss av et verktøy som WoS, for eksempel for å øke vår evne til å motta likviditet. Vi delegerer midlertidig "drittjobben" med å administrere likviditeten i kanalene for oss til WoS. Når et visst beløp er nådd, tømmer vi WoS On-Chain til vår ikke-frihetsberøvende Wallet.


**WARNING⚠️: Det anbefales å lese hele veiledningen før du fortsetter**


### Nedlasting av Wallet av Satoshi


Gå til Play Store og last ned WoS


![image](assets/it/01.webp)


**WoS lastes bare ned fra offisielle butikker. Hvis enhetens operativsystem er programmert, må operativsystemet selv verifisere WoS før det kan åpnes. Etter verifiseringsfasen velger du _Åpne_.


![image](assets/it/02.webp)


Wallet av Satoshi åpnes med følgende skjermbilde, og det er nødvendig å klikke på _Start_


![image](assets/it/03.webp)


### Registrering av en konto for WoS


På dette tidspunktet er Wallet allerede i drift, men for større sikkerhet fortsetter vi med å sette opp en pålogging: det vil være nødvendig for å gjenopprette midler i tilfelle funksjonsfeil eller tap av enheten. Velg derfor menyen øverst til venstre.


![image](assets/it/04.webp)


Hele menyvinduet åpnes, der du utelukkende må stille inn valutaen (Wallet av Satoshi presenterer som standard den amerikanske dollaren som referansevaluta) og temafargen (lys / mørk), etter smak. Ikke bruk de andre kommandoene.


Siden WoS er et depotverktøy, kan vi ikke sikkerhetskopiere Wallet med Mnemonic-frasen, men vi kan gjøre det mulig for WoS å gjenopprette midlene våre, i tilfelle tap eller manglende bruk av den mobile enheten, ved å klikke på _Login/Register_

Det vises et vindu der vi blir bedt om å oppgi en e-post Address. Det kan være **en Proton-mail** (anbefales), men den må være funksjonell, da den vil gjøre det mulig for oss å få tilbake pengene i Wallet i tilfelle tap/tyveri eller skade på mobiltelefonen.


![image](assets/it/08.webp)


Wallet av Satoshi har sendt en melding til den angitte e-postinnboksen.


![image](assets/it/09.webp)


I postkassen finner vi to ord, som vi må skrive inn, omskrive dem, på plassen som tilbys av appen.


- ikke aktiver oversetteren: ordene er og må forbli på engelsk**
- skriv om de to ordene og ta hensyn til store og små bokstaver**


![image](assets/it/10.webp)


Når du har transkribert de to ordene, klikker du på _OK_.


![image](assets/it/11.webp)


Resultatet skal være et bilde som vises øverst, med avkrysningssymbolet for bekreftelse.


![image](assets/it/12.webp)


mens du er i innstillingsdelen, viser den røde _Login/Register_-linjen nå brukerens e-post Address.


![image](assets/it/13.webp)


### Mottak av betalinger


For å motta på WoS klikker du på _Receive_, og en rekke kommandoer vises.


![image](assets/it/14.webp)


Du kan motta


- via LN-Address **a**
- via LN, ved å stille inn Invoice **b**
- on chain (WoS støtter Bitcoin-nettverket, men med betalte ubåtbytter) **c**
- ved å skanne QR-koden til en LNurl-p **d**


![image](assets/it/15.webp)


### Opprette en Invoice


Klikk på _Receive_, og velg kommandoen med Lightning Network-symbolet.


![image](assets/it/16.webp)


Menyen for oppretting av Invoice vises, der vi klikker på _Add Amount_ for å skrive det nøyaktige beløpet og legge til en beskrivelse, i dette eksempelet "Min første Invoice".


![image](assets/it/17.webp)


Med tastaturet stiller vi inn beløpet.


![image](assets/it/18.webp)


for deretter å få utbetalt Invoice. Den mottatte betalingen ser slik ut:


![image](assets/it/19.webp)


### Henting fra POS


Wallet av Satoshi har en standardfunksjon, som gjør den spesielt egnet for selgere: POS. La oss se hvordan du aktiverer den.


Velg menyen øverst til høyre på hovedskjermen.


![image](assets/it/20.webp)


Velg deretter _Point of Sale_.


![image](assets/it/21.webp)


Med den nyeste utgaven av WoS må du sørge for å velge _Keypad_.


![image](assets/it/22.webp)

og skriv deretter inn beløpet på tastaturet, i eksempelet som følger lik 10 cent / 118 Sats. Legg til en beskrivelse for samlingen, i dette tilfellet "min andre med POS". En stor Green-knapp lyser opp, og den skal klikkes på

![image](assets/it/23.webp)


til generate Invoice og vise den - for eksempel - til en kunde.


![image](assets/it/24.webp)


Denne betalingen blir også innkrevd!


![image](assets/it/25.webp)


### Sende betalinger


Enkelhet er en styrke ved WoS' hovedskjermbilde. For å betale en Invoice klikker du på _Send_


![image](assets/it/26.webp)


Ved første gangs bruk ber WoS om tillatelse til å få tilgang til kameraet


![image](assets/it/27.webp)


Fra dette øyeblikket aktiveres kameraet


![image](assets/it/28.webp)


Ved å ramme inn Invoice ser vi at det er bedt om en betaling på 210 Sats. En beskrivelse leses også, hvis rekvirenten har angitt en. Dette skjermbildet er sammendraget og også en forespørsel om bekreftelse: WoS "ber om autorisasjon" til å sende betalingen, noe som gis ved å klikke på Green _Send_-knappen


![image](assets/it/29.webp)


Når betalingen når destinasjonen, varsler WoS med dette skjermbildet


![image](assets/it/30.webp)


Fra hovedskjermbildet, ved å klikke på _Historikk_ (rett under saldoen), vises listen over transaksjoner


![image](assets/it/31.webp)


#### Gjenoppretting av WoS-kontoen


Nå skal vi se hvordan du installerer WoS på en ny enhet; dette vil også være nyttig i tilfeller av tyveri, tap eller manglende evne til å betjene mobiltelefonen som Wallet tidligere var installert på. Når du har installert på nytt, må du gjøre om kontoregistreringsprosedyren som nettopp er forklart, med en enkelt variant: på slutten av forespørselen om å logge på med den tidligere angitte e-postadressen, vil WoS vises slik:


![image](assets/it/33.webp)


Vi får en melding om at det er sendt en e-post med informasjon om hvordan du reaktiverer kontoen. Du må åpne e-postinnboksen din.


**VIKTIG**: åpne e-posten fra en PC eller i alle fall fra en annen enhet enn den du er i ferd med å gjenopprette WoS-kontoen på. I innboksen finner vi en melding som viser oss en QR-kode for å ramme inn


![image](assets/it/34.webp)


Når QR-koden er innrammet, vises den gjenopprettede kontoen på hovedsiden til WoS, med saldo og historikk.