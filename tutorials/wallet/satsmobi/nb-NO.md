---
name: Sats.mobi

description: En Telegram-tilgjengelig forvaringsenhet Wallet
---

![cover](assets/cover.webp)


_Denne opplæringen ble skrevet av_ [Bitcoin Campus] (https://linktr.ee/bitcoincampus_)


## Sats.Mobi

SatsMobi er en Wallet som opererer på Telegram, med alle funksjonene til en Lightning Network (custodial) Wallet, pluss en rekke veldig underholdende funksjoner. Den stammer fra en Fork av den nå nedlagte LightningTipBot, og arver alle dens funksjoner samtidig som den legger til flere aktuelle funksjoner, og dermed gjør den mer moderne. I likhet med LNTipBot omfavner Sats.Mobi også åpen kildekode-filosofien. Wallet kan konfigureres og administreres uavhengig ved å klone den fra dette [repository] (https://github.com/massmux/SatsMobiBot).


Hvis du foretrekker å bruke det enkelt, vil det å starte en chat på Telegram avsløre at det er en bot.


## Innstillinger

Fra Telegram-søkefeltet, se etter "satsmobi", og lenken til [bot] (@SatsMobiBot) vises.


**Attention**: Hvis du ikke er sikker på om du vil søke via Telegram, kan du få sikker tilgang til boten ved å bruke følgende [link] (https://t.me/SatsMobiBot)


![image](assets/it/01.webp)


Alt du trenger å gjøre for å komme i gang, er å trykke _START_


![image](assets/it/02.webp)


For å utforske Wallet kan du velge _Menu_ nederst til venstre.


![image](assets/it/03.webp)


Velg nå _/help_ blant hovedkommandoene.


![image](assets/it/04.webp)


Sats.Mobi ønsker oss velkommen ved å vise en melding som viser alle hovedfunksjonalitetene. Ved oppstart opprettet boten også en LN Address, knyttet til det valgte håndtaket på Telegram (som er unikt som standard). Kommandoer for å sende og motta Sats med denne Wallet er synlige, så vel som andre funksjoner vi vil se senere. Det er interessant å også ta en titt på _/avansert_-menyen


![image](assets/it/05.webp)


Det er merkbart at Sats.Mobi også opprettet en anonym LN Address, som skal brukes til å få personvern. Boten fungerer med kommandoer: bare klikk på det tilsvarende ordet, eller skriv skråstreken "/" i meldingsfeltet, etterfulgt av kommandoen du vil utføre. Selv om Wallet nettopp har blitt opprettet, velger du for eksempel _/transaksjoner_


![image](assets/it/06.webp)


Denne kommandoen viser listen over de siste transaksjonene, i dette tilfellet lik null.


![image](assets/it/07.webp)


## Mottak av Sats

Kommandoen for å opprette en Invoice og motta Sats er _/invoice_. Sats.Mobi opererer utelukkende i Satoshi, den minste enheten i Bitcoin; derfor, for å opprette Invoice, er det nødvendig å skrive beløpet i Sats i meldingslinjen og deretter sende det i chatten med boten.

![image](assets/it/08.webp)


I det følgende eksempelet ble det valgt å motta et beløp på 210 Sats.


![cover](assets/it/09.webp)


Etter å ha ventet noen øyeblikk på at Invoice skal klargjøres, er den tilgjengelig som tekst og som en QR-kode. Når du betaler Invoice, viser Wallet saldoen. Hvis totalsummen av en eller annen grunn ikke er oppdatert, skriver du _/saldo_ og trykker på `enter`.


![image](assets/it/10.webp)


## Sende Sats


Selv om Sats er en ekstremt verdifull ressurs, som man ikke bør skille seg fra lett, Sats.Mobi gjør denne delen tiltalende, og det vil ikke være noe problem å utføre noen korte tester (dvs. et par prøvetransaksjoner).


### Betale en Invoice


Den enkleste måten å betale en Invoice på er å kopiere meldingsstrengen `lnbc1xxxxx` og lime den inn i meldingsfeltet etter at du har skrevet inn kommandoen _/pay_. **Korrekt syntaks** krever at det er et mellomrom etter kommandoen.


![image](assets/it/11.webp)


Wallet sender en melding og ber om bekreftelse. Ved å klikke på _Pay_ blir Invoice betalt.


![image](assets/it/12.webp)


Sats.Mobi kan stole på en effektiv og godt tilkoblet Lightning-node, og det er sjelden at betalinger mislykkes fordi den alltid klarer å finne riktig ruting.


### Betale komfortabelt fra mobilen


Sats.Mobi er også tilgjengelig på mobil. Den mest praktiske funksjonen for å betale med mobilen er å skanne en QR-kode, men denne Wallet mangler det av design, siden den ikke er en frittstående app, men finnes i et sosialt nettverk. Sats.Mobi er derfor programmert for å gjøre mobilopplevelsen så enkel som mulig: Den kan faktisk dekode et bilde, for eksempel et fotografi tatt av QR-koden til Invoice du vil betale med.


Anta for eksempel at du ønsker å betale en Invoice på 50 Sats.


![image](assets/it/20.webp)


Når dette vises til oss, kan vi ta et bilde av den tilhørende QR-koden.


![image](assets/it/21.webp)


Deretter åpner vi Telegram på mobilen, og i chatten med Sats.Mobi legger vi ved bildet som nettopp er tatt av QR-koden


![cover](assets/it/22.webp)


Når den er valgt, sender vi den til boten:


![image](assets/it/23.webp)

Sats.Mobi avkoder bildet og **presenterer umiddelbart betalingsforespørselen**, med riktig beskrivelse. Chatten ber om bekreftelse, for å fortsette må du trykke _/betale_

![image](assets/it/24.webp)


Vennligst vent et øyeblikk slik at betalingen kan behandles.


![image](assets/it/25.webp)


Invoice for 50 Sats har blitt betalt, et resultat som oppnås uten bruk av kamera og den integrerte skannefunksjonen.


### Sats.Mobi i Telegramgrupper


![image](assets/it/27.webp)


Blant funksjonene som gjorde LNTipBot berømt, og som Sats.Mobi bringer til Telegram, er den som gjør opplevelsen morsom og interaktiv for medlemmene i en gruppe.

Eiere kan invitere boten til å bli med i gruppechatten og deretter utnevne Sats.Mobi som administrator. Fra det øyeblikket begynner moroa, fordi medlemmene kan begynne å belønne andre brukere for deres bidrag til gruppen.


- _/tip_ legger til et tips ved å svare på en melding;
- _/send_ sender penger med en LN Address eller et Telegram-handle som mottaker;
- _/faucet_ (i _/avansert_-menyen) gjør det mulig å lage en serie med tips som de raskeste medlemmene i gruppen kan samle inn ved å klikke på _/collect_;
- _/tipjar_ (i _/avansert_-menyen) oppretter en annen type distribusjon som kan sendes til brukerne i gruppen.


Hver av disse kommandoene har sin egen syntaks, som er forklart i hovedkommandomenyen.


Og hvis vi ikke er eier av en gruppe? Ikke noe problem: bare be grunnleggeren om å invitere Sats.Mobi, legg det til som administrator av gruppen, så er alt klart!


## Salgssted (POS)


Når Sats.Mobi startes for første gang, oppretter boten også en annen funksjon for brukeren: **POS**. "Enheten" aktiveres av brukeren med kommandoen _/pos_ eller ved å klikke på den relaterte knappen fra konsollen nederst til høyre. Faktisk er POS en webapp, som åpnes som en popup på Telegram-chatten


![image](assets/it/14.webp)


Interface viser brukerens personlige Telegram-håndtak øverst til venstre, og brukes på samme måte som alle andre POS: ved å skrive inn beløpet på tastaturet. La oss anta at vi ønsker å kreve inn 21 eurocent for en tjeneste. Siden Sats.Mobi kun håndterer Sats, er det ikke lett å gjøre konverteringen i hodet. Tvert imot viser POS-en euroen som regningsenhet, samtidig som den viser tilsvarende i Satoshi.


![image](assets/it/15.webp)

Ved å klikke på _/OK_ vises Invoice som kan vises til kunden via en QR-kode, eller som kan sendes som en streng via direktemeldinger, slik at den kan betales.

![image](assets/it/16.webp)

![image](assets/it/17.webp)


POS er naturligvis også tilgjengelig på mobiltelefoner, og nås på samme måte som vist tidligere.


![image](assets/it/18.webp)


Den vises også godt på mobiltelefonens skjerm:


![image](assets/it/19.webp)


## Ytterligere funksjoner


Det finnes andre funksjoner som kompletterer tilbudet til Sats.Mobi Wallet, som, som vi har sett, utvider konseptet med en Wallet utover det å motta og sende betalinger:


- _/nostr_: for å koble Wallet til din egen Nostr-bruker for å motta zaps;
- _/cashback_: viser en kode som kan presenteres for en forhandler for å få cashback på et kjøp;
- _/buy_: starter en guidet prosedyre i boten, som gjør det mulig å kjøpe Sats for euro;
- _/activatecard_: for å be om aktivering av et NFC-debetkort, som kan lades opp via Sats.Mobi Wallet og som varsler kan aktiveres for;
- _/link_: oppretter en kobling til din egen Zeus eller Blue Wallet, som kan brukes som fjernkontroller for denne Wallet.


## Konklusjon

Sats.Mobi er en hyggelig og morsom Wallet å bruke, som bringer tilbake opplevelsene man hadde med LNTipBot ved hjelp av de mer avanserte funksjonene i LNBits. Det er imidlertid viktig å huske at **det er en depottjeneste**. Derfor bør den brukes til å holde svært få Sats, det er ikke en hoved Wallet for Lightning Network-midlene dine. Det er også en iboende kapasitetsgrense, lik 500 000 Sats, en grense som det anbefales å ikke overskride.


Hvis du er på utkikk etter lommebøker som ikke er frihetsberøvende Lightning Network, er det absolutt tilrådelig å se på andre produkter.


---
### Dokumentasjon


- [Github] (https://github.com/massmux/SatsMobiBot)
- Spilleliste med [videoer] (https://www.youtube.com/results?search_query=Sats.mobi) demo