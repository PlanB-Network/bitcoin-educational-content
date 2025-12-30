---
name: Kulturarv
description: En Bitcoin-portefølje med integrert arvemekanisme via Taproot-skript
---

![cover](assets/cover.webp)



Å gi bitcoins videre i tilfelle død eller uførhet representerer en stor utfordring for alle som eier kryptoaktiva. Uten en egnet arveplan blir disse eiendelene ugjenkallelige for dine nærmeste.



Heritage gir et elegant svar ved å implementere en dødmannsbrytermekanisme direkte i Bitcoin-blokkjeden. Denne wallet med åpen kildekode gjør det mulig å konfigurere on-chain-suksesjonsbetingelser: Hvis eieren ikke foretar ytterligere transaksjoner i en definert periode, kan forhåndsdefinerte alternative nøkler frigjøre midlene.



## Hva er Heritage?



Heritage er en Bitcoin-portefølje som integrerer en arvemekanisme via Taproot-skript. Denne programvaren med åpen kildekode er utviklet under MIT-lisens av Jérémie Rodon, og garanterer åpenhet og holdbarhet.



Heritage bruker Taproot-skript som er kodet i Bitcoin-adresser. Hver UTXO integrerer to typer utgiftsbetingelser:





- Primær sti** : Eieren kan når som helst bruke sine bitcoins med sin primærnøkkel
- Alternative veier**: For hver utpekt arving kombinerer et skript den offentlige nøkkelen med en tidslås



Hver eiertransaksjon utsetter automatisk aktiveringsdatoen for arveklausulene. Ved langvarig inaktivitet (død, arbeidsuførhet) utløses vilkårene automatisk.



## Kulturarvservice (valgfritt)



Heritage tilbyr to bruksalternativer:



**Gjør det selv (gratis)**: Applikasjonen med åpen kildekode alene. Du administrerer alt autonomt med din egen node. Dette alternativet tilbyr innebygd sikkerhetskopitilgang, innebygd arv og eksklusiv kontroll over bitcoinsene dine. Du må imidlertid opprette dine egne varsler (kalender, påminnelser) slik at du ikke glemmer å fornye tidslåsene dine, og det er ingen automatiske varsler til arvingene dine.



**Bruk tjenesten (0,05 % per år)** : Tjenesten btc-heritage.com legger til funksjoner for å forenkle administrasjonen:




- Automatiske påminnelser før fristene dine utløper
- Automatisk varsling til arvinger for å veilede dem gjennom gjenopprettingsprosessen
- Prioritert støtte
- Forenklet håndtering av deskriptorer



Gebyr: 0,05 % av forvaltet beløp per år, minimum 0,5 mBTC/år. Første året er gratis.



Tjenesten er ikke depotbasert: De private nøklene dine forlater aldri enheten din. Heritage har ikke tilgang til midlene dine.



## Heritage CLI



For avanserte brukere som foretrekker terminalen, tilbyr Heritage et kommandolinjeverktøy (CLI) for detaljert kontroll og luftgapet maskindrift.



![Page Heritage CLI](assets/fr/03.webp)



Full CLI-dokumentasjon er tilgjengelig på [btc-heritage.com/heritage-cli] (https://btc-heritage.com/heritage-cli). Her finner du instruksjoner for nedlasting, tilkobling til tjenesten, opprettelse av lommebøker (med Ledger eller lokale nøkler), administrasjon av arvinger og transaksjoner.



Denne veiledningen fokuserer på skrivebordsprogrammet, som er mer tilgjengelig for de fleste brukere.



## Heritage Desktop



Heritage Desktop er et grafisk program med et intuitivt grensesnitt som veileder brukeren gjennom hvert trinn i konfigurasjonsprosessen.



### Last ned



Gå til [btc-heritage.com] (https://btc-heritage.com) og klikk på "Last ned applikasjon".



![Page d'accueil Heritage](assets/fr/01.webp)



Velg den versjonen som passer til operativsystemet ditt (Linux 64bits eller Windows 64bits). Binærfiler er ikke digitalt signerte, noe som kan utløse sikkerhetsadvarsler.



![Page de téléchargement](assets/fr/02.webp)



### Installasjon på Linux



På Linux distribueres programmet i AppImage-format. Før du kan kjøre det, må du installere avhengigheten `libfuse2`:



```bash
sudo apt install libfuse2
```



![Installation libfuse2](assets/fr/04.webp)



Deretter gjør du filen kjørbar og kjører den:



```bash
chmod +x Heritage-GUI-vX.X.X.AppImage
./Heritage-GUI-vX.X.X.AppImage
```



### Første lansering



Ved første oppstart gir veiviseren deg tre valg:



![Onboarding initial](assets/fr/05.webp)





- Sett opp en Heritage Wallet**: Opprett en ny wallet med kulturarvsplan
- Arv bitcoins**: Få tilbake bitcoins som arving
- Utforsk på egen hånd**: Utforsk funksjoner uten hjelp



Velg "Setup an Heritage Wallet" for å opprette din første wallet.



### Bitcoin nettverkstilkobling



Velg hvordan du vil koble deg til Bitcoin-nettverket:



![Choix connexion](assets/fr/06.webp)





- Bruk av Heritage Service**: Forvaltet infrastruktur, enklere for arvingene
- Bruker min egen node**: Koble til din egen Bitcoin Core- eller Electrum-node



I denne opplæringen bruker vi vår egen node.



### Håndtering av private nøkler



Velg hvordan du vil administrere de private nøklene dine:



![Gestion des clés](assets/fr/07.webp)





- Med en Ledger maskinvareenhet** : Maksimal sikkerhet med wallet-maskinvare (anbefalt)
- Lokal lagring med passord**: Lokalt lagrede nøkler med passordbeskyttelse
- Gjenopprett en eksisterende wallet** : Gjenopprett fra en eksisterende seed



### Nodekonfigurasjon



Hvis du bruker din egen node, veileder programmet deg gjennom konfigurasjonen. Sørg for at Bitcoin- eller Electrum-noden din er :




- Installert og i drift
- Synkronisert med Bitcoin-nettverket
- Konfigurert til å godta RPC-tilkoblinger (for Bitcoin Core)



![Configuration nœud](assets/fr/08.webp)



Klikk på "Min Bitcoin-node er oppe og går" når noden er klar.



### Statuspanel



Klikk på "Status" øverst i høyre hjørne, og deretter på "Open Configuration" for å få tilgang til tilkoblingsparametrene.



![Panneau Status](assets/fr/09.webp)



Angi URL-adressen til Electrum-serveren din (f.eks. `umbrel.local:50001` hvis du bruker Umbrel).



![Configuration Electrum](assets/fr/10.webp)



### Opprettelse av wallet



Når forbindelsen er opprettet, klikker du på "Create Wallet" i WALLETS-fanen.



![Créer wallet](assets/fr/11.webp)



Et popup-vindu forklarer den delte arkitekturen til Heritage :



![Architecture split](assets/fr/12.webp)



1. **Nøkkelleverandør (frakoblet)**: Administrerer dine private nøkler og signerer transaksjoner. Kan være en Ledger eller en wallet-programvare.


2. **Online Wallet**: Håndterer synkronisering med Bitcoin-nettverket, opprettelse av adresser og transaksjonssending.



Fyll ut opprettelsesskjemaet :



![Formulaire création wallet](assets/fr/13.webp)





- Wallet Navn**: Et unikt navn for å identifisere din wallet
- Nøkkelleverandør**: Velg Local Key Storage for denne opplæringen
- Ny/gjenopprett**: Velg "Ny" for å opprette en ny generate seed
- Antall ord**: 24 ord anbefales for maksimal sikkerhet



Skriv inn et sterkt passord og velg alternativer for Online Wallet :



![Options Online Wallet](assets/fr/14.webp)





- Lokal node**: Bruker din egen Electrum- eller Bitcoin Core-node
- Heritage-tjenesten**: Bruker Heritage-tjenesten (anbefales for varslingsfunksjoner)



Klikk på "Opprett Wallet" for å fullføre opprettelsen.



### Interface fra wallet



Din wallet er nå opprettet. Grensesnittet viser :



![Interface wallet](assets/fr/15.webp)





- Balanse
- SEND- og MOTTAK-knappene
- Transaksjonshistorikk
- Arv konfigurasjon historie
- wallet-adresser



### Opprette arvinger



Gå til fanen "ARVINGER" for å opprette arvingene dine.



![Page Heirs](assets/fr/16.webp)



Popup-vinduet med informasjon forklarer:




- Arvinger er Bitcoin offentlige nøkler knyttet til enkeltpersoner
- Hver arving har sin egen huskeregel
- Den første arvingen skal være en "backup" for deg selv (i tilfelle du mister din viktigste wallet)



#### Opprettelse av backup-arvinger



Klikk på "Opprett arving", og gi den navnet "Backup".



![Création héritier Backup](assets/fr/17.webp)



Popup-vinduet forklarer hvorfor en setning på 12 ord uten passphrase er trygg for arvingene:


1. **Ingen umiddelbar tilgang**: Arvenøkler kan ikke få tilgang til midler før tidssperren er utløpt


2. **Kompromitteringsdeteksjon**: Hvis noen får tilgang til frasen, kan du oppdatere Heritage-konfigurasjonen


3. **Langsiktig tilgjengelighet**: En passphrase kan bli glemt etter mange år



Konfigurer arvingen :



![Configuration héritier](assets/fr/18.webp)





- Nøkkelleverandør** : Lokal lagring av nøkler
- Ny**: Generer en ny seed
- Antall ord**: 12 ord



Fullfør opprettelsen :



![Finalisation héritier](assets/fr/19.webp)





- Type arving**: Utvidet offentlig nøkkel
- Eksporter til tjeneste**: Valgfritt, muliggjør automatisk varsling av arvinger



Backup-arvingen er nå opprettet:



![Héritier créé](assets/fr/20.webp)



#### Lagre arvingens minneord



Klikk på Backup-arvingen og deretter på "Vis Mnemonic" :



![Afficher mnemonic](assets/fr/21.webp)



**VIKTIG: Noter disse 12 ordene, og oppbevar dem på et trygt sted. Dette er nøkkelen til å få tilbake pengene.



![Phrase mnémotechnique](assets/fr/22.webp)



#### Fjerne seed fra applikasjonen



Når du har skrevet ned frasen, åpner du arveparametrene (tannhjulikonet):



![Paramètres héritier](assets/fr/23.webp)



Bruk "Strip Heir Seed" for å fjerne den private nøkkelen fra programmet. Bekreft at du har lagret frasen.



![Strip Heir Seed](assets/fr/24.webp)



Dette er et sikkerhetstiltak: Bare den offentlige nøkkelen forblir i applikasjonen, noe som er tilstrekkelig for å konfigurere arv.



#### Opprettelse av en annen arving



Gjenta prosessen for å opprette en annen arving (f.eks. "Satoshi"). Du vil nå ha to arvinger:



![Deux héritiers](assets/fr/25.webp)





- Sikkerhetskopi**: Din personlige nødnøkkel
- Satoshi**: En utpekt arving



### Heritage-konfigurasjon



Gå tilbake til wallet og klikk på Innstillinger-ikonet:



![Paramètres wallet](assets/fr/26.webp)



I delen "Heritage Configuration" klikker du på "Create":



![Heritage Configuration](assets/fr/27.webp)



Sett tidsbegrensninger for hver arving:



![Configuration délais](assets/fr/28.webp)





- Sikkerhetskopiering**: 180 dager (6 måneder) - Forfallsdato: 2026-06-18
- Satoshi**: 455 dager (15 måneder) - Forfallsdato: 2027-03-20



**Viktig**: Hver arving må ha en lengre forsinkelse enn den forrige. Den første arvingen (Backup) vil få tilgang til midlene først.



Konfigurer også :



![Configuration finale](assets/fr/29.webp)





- Referansedato**: Startdato for beregning av ledetid
- Minimum forfallsforsinkelse**: Minimum forsinkelse etter en transaksjon (10 dager anbefales)



Klikk på "Opprett" for å bekrefte konfigurasjonen.



Heritage-konfigurasjonen er nå aktiv:



![Configuration active](assets/fr/30.webp)



Den viser begge arvingene med deres respektive frister og utløpsdatoer.



### Lagring av deskriptorer



**Viktig**: Ta vare på wallet-beskrivelsene dine. Uten dem, selv med den mnemoniske frasen, er det umulig å gjenopprette fondet.



Klikk på "Backup Descriptors" :



![Bouton Backup](assets/fr/31.webp)



Lagre JSON-filen som inneholder Bitcoin-beskrivelsene dine:



![Backup descripteurs](assets/fr/32.webp)



Denne filen bør gis videre til arvingene dine, sammen med de respektive minneordene.



### Motta bitcoins



Klikk på "RECEIVE" for å velge en mottaksadresse i generate:



![Recevoir bitcoins](assets/fr/33.webp)



Gratulerer med dagen! Din Heritage Wallet er klar til å motta bitcoins. Hver genererte adresse inkorporerer automatisk Heritage-betingelsene dine.



Etter at du har mottatt en transaksjon, oppdateres saldoen din:



![Solde mis à jour](assets/fr/34.webp)



Historikken viser transaksjonen og den tilhørende Heritage-konfigurasjonen.



---

## Inndrivelse av en arving



Når den fastsatte tiden er utløpt, kan arvingen kreve pengene tilbake.



### Forutsetninger



Arvingen trenger :


1. Hans huskeregel på 12 ord


2. Den opprinnelige wallet-beskrivelsesfilen (JSON)



### Opprette en arving Wallet



I fanen "ARV" får du opp en popup som minner deg om disse forutsetningene:



![Page Heir Wallets](assets/fr/35.webp)



**Vær oppmerksom**: Uten sikkerhetskopifilen er det UMULIG å få tilgang til midlene, selv med riktig huskeregel.



Klikk på "Opprett arving Wallet" :



![Créer Heir Wallet](assets/fr/36.webp)



Vennligst fyll ut skjemaet:



![Formulaire Heir Wallet](assets/fr/37.webp)





- Arving Wallet Navn**: Et navn for å identifisere denne arvingen wallet
- Nøkkelleverandør** : Lokal lagring av nøkler
- Gjenopprett**: Velg dette alternativet for å angi en eksisterende frase



Skriv inn de 12 ordene i arvingens mnemotekniske frase og konfigurer Heritage Provider:



![Entrée mnemonic](assets/fr/38.webp)





- Heritage Provider**: "Local" for å bruke din egen node med sikkerhetskopifilen



Last inn JSON-sikkerhetskopifilen og klikk på "Opprett arving Wallet" :



![Chargement backup](assets/fr/39.webp)



### Interface Arving Wallet



Arvingen Wallet opprettes. Hvis tidssperren ennå ikke har utløpt, er ingen arv tilgjengelig:



![Pas d'héritage disponible](assets/fr/40.webp)



Når forsinkelsen har gått ut og midlene er synkronisert med Bitcoin-nettverket, vises de i listen over arvinger:



![Héritage disponible](assets/fr/41.webp)



Grensesnittet viser :




- Nøkkeltype og fingeravtrykk
- Sum arvelige midler
- Gjeldende beløp som kan brukes (0 satt hvis tidssperren ennå ikke er utløpt)
- Forfalls- og utløpsdatoer



Når forfallsdatoen er nådd, overfører "Spend"-knappen bitcoinsene til en personlig wallet.



---

## Beste praksis



### Lagring av deskriptorer



wallet-beskrivelser er avgjørende for å rekonstruere Heritage-adressene dine. **Uten deskriptorene vil du ikke kunne finne fondene dine, selv ikke med huskereglene dine.



### Nøkkelsikkerhet





- Bruk en Ledger som hovednøkkel hvis mulig
- Oppbevar aldri arvingers setninger på samme sted som dine egne
- Spred informasjon på flere medier og steder



### Dokumentasjon for dine nærmeste



Skriv tydelige instruksjoner som forklarer hvert trinn i gjenopprettingsprosessen. Det er ikke sikkert at arvingene dine er kjent med Bitcoin i det kritiske øyeblikket.



## Alternativer



Det finnes andre løsninger for å administrere overføringen av bitcoins, inkludert Liana og Bitcoin Keeper. Du finner veiledningene våre nedenfor:



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

## Konklusjon



Heritage lar deg planlegge Bitcoin-etterfølgeren din på en suveren måte via skrivebordsprogrammet. Implementering krever gjennomtenkt vurdering av passende tidsrammer og sikring av hemmeligheter. Ikke glem å overlevere til arvingene dine:




- Deres 12 ord lange huskeregel
- Filen for sikkerhetskopiering av deskriptoren
- Instruksjoner for gjenoppretting



## Ressurser





- [Heritage offisielle nettsted](https://btc-heritage.com)
- [Dokumentasjon CLI](https://btc-heritage.com/heritage-cli)
- [GitHub Heritage CLI](https://github.com/crypto7world/heritage-cli)
- [GitHub Heritage Desktop] (https://github.com/crypto7world/heritage-gui)