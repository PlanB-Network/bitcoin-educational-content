---
name: Blockstream Green - Watch-Only
description: Konfigurasjon av kun overvåkingsportefølje
---
![cover](assets/cover.webp)

I denne veiledningen lærer du hvordan du enkelt kan sette opp en "watch-only"-portefølje på mobilen ved hjelp av Blockstream Green-applikasjonen.

## Hva er en Watch-Only Wallet?

En skrivebeskyttet lommebok, eller "watch-only wallet", er en type programvare som er utformet slik at brukeren kan observere transaksjoner knyttet til en eller flere spesifikke offentlige Bitcoin-nøkler, uten å ha tilgang til de tilsvarende private nøklene.

Denne typen applikasjon lagrer kun de dataene som trengs for å overvåke en Bitcoin-lommebok, særlig for å se saldoen og transaksjonshistorikken, men den har ingen tilgang til private nøkler. Som et resultat er det umulig å bruke Bitcoins som oppbevares av lommeboken i applikasjonen som kun overvåker.

![GREEN-WATCH-ONLY](assets/fr/01.webp)

Watch-only brukes vanligvis sammen med en maskinvarelommebok. Dette gjør det mulig å lagre lommebokens private nøkler på en sikker måte, på maskinvare som ikke er koblet til Internett og har en svært liten angrepsflate, og dermed isolerer de private nøklene fra potensielt sårbare miljøer. Watch-only-applikasjonen lagrer derimot utelukkende den utvidede offentlige nøkkelen (`xpub`, `zpub`, osv.) til Bitcoin-lommeboken. Denne overordnede nøkkelen kan ikke brukes til å finne de tilknyttede private nøklene, og kan derfor ikke brukes til å bruke Bitcoins. Den gjør det imidlertid mulig å avlede offentlige nøkler og mottaksadresser. Takket være maskinvarelommebokens kunnskap om sikre lommebokadresser kan watch-only-applikasjonen spore disse transaksjonene i Bitcoin-nettverket, slik at brukeren kan overvåke saldoen sin og generere nye mottakeradresser uten å måtte koble til maskinvarelommeboken hver gang.

I denne veiledningen vil jeg introdusere deg for en av de mest populære løsningene for mobile lommebøker som kun er beregnet på klokker: **Blockstream Green**.

![GREEN-WATCH-ONLY](assets/fr/02.webp)

## Vi introduserer Blockstream Green

Blockstream Green er en programvare som er tilgjengelig på mobil og PC. Denne porteføljen var tidligere kjent som Green Address, men ble et Blockstream-prosjekt etter oppkjøpet i 2016.

Green er et svært brukervennlig program, noe som gjør det spesielt egnet for nybegynnere. Det tilbyr en rekke funksjoner, for eksempel administrasjon av hot wallets, hardware wallets og Liquid sidechain wallets.

I denne veiledningen konsentrerer vi oss utelukkende om å opprette en portefølje som kun inneholder klokker. Hvis du vil utforske andre bruksområder for Green, kan du se våre andre dedikerte veiledninger:

https://planb.network/tutorials/wallet/desktop/blockstream-green-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da
https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143
## Installere og konfigurere Blockstream Green-applikasjonen

Det første trinnet er selvfølgelig å laste ned Green-applikasjonen. Gå til applikasjonsbutikken din:

- [For Android] (https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet);
- [For Apple] (https://apps.apple.com/us/app/green-bitcoin-wallet/id1402243590).
![GREEN-WATCH-ONLY](assets/fr/03.webp)

For Android-brukere kan du også installere applikasjonen via `.apk`-filen [tilgjengelig på Blockstreams GitHub] (https://github.com/Blockstream/green_android/releases).

![GREEN-WATCH-ONLY](assets/fr/04.webp)

Start programmet, og kryss av i boksen "Jeg godtar vilkårene...*".

![GREEN-WATCH-ONLY](assets/fr/05.webp)

Når du åpner Green for første gang, vises startskjermbildet uten en konfigurert portefølje. Hvis du senere oppretter eller importerer porteføljer, vil de vises i dette grensesnittet. Før du går videre til å opprette en portefølje, anbefaler jeg at du justerer programinnstillingene slik at de passer til dine behov. Klikk på "Programinnstillinger".

![GREEN-WATCH-ONLY](assets/fr/06.webp)

Alternativet "*Avansert personvern*", som kun er tilgjengelig på Android, forbedrer personvernet ved å deaktivere skjermbilder og skjule forhåndsvisninger av applikasjoner. Det låser også automatisk tilgangen til applikasjoner så snart telefonen låses, noe som gjør det vanskeligere å eksponere dataene dine.

![GREEN-WATCH-ONLY](assets/fr/07.webp)

For de som ønsker å forbedre personvernet sitt, tilbyr applikasjonen muligheten til å roote trafikken din via Tor, et nettverk som krypterer alle forbindelsene dine og gjør det vanskelig å spore aktivitetene dine. Selv om dette alternativet kan gjøre applikasjonen litt tregere, anbefales det på det sterkeste for å beskytte personvernet ditt, spesielt hvis du ikke bruker din egen komplette node.

![GREEN-WATCH-ONLY](assets/fr/08.webp)

For brukere som har sin egen komplette node, tilbyr Green Wallet muligheten til å koble seg til den via en Electrum-server, noe som garanterer total kontroll over Bitcoin-nettverksinformasjon og distribusjon av transaksjoner.

![GREEN-WATCH-ONLY](assets/fr/09.webp)

En annen alternativ funksjon er alternativet "*SPV Verification*", som lar deg verifisere visse blokkjededata direkte og dermed redusere behovet for å stole på Blockstreams standardnode, selv om denne metoden ikke gir alle garantiene til en full node.

![GREEN-WATCH-ONLY](assets/fr/10.webp)

Når du har tilpasset disse innstillingene til dine behov, klikker du på "*Lagre*"-knappen og starter programmet på nytt.

![GREEN-WATCH-ONLY](assets/fr/11.webp)

## Opprett en portefølje som kun kan overvåkes på Blockstream Green

Du er nå klar til å opprette en portefølje som kun skal overvåkes. Klikk på knappen "*Gå i gang*".

![GREEN-WATCH-ONLY](assets/fr/12.webp)

Du kan velge mellom flere typer lommebøker. I denne veiledningen ønsker vi å opprette en portefølje som kun inneholder klokker, så klikk på den tilsvarende knappen.

![GREEN-WATCH-ONLY](assets/fr/13.webp)

Velg alternativet "Enkel signatur".

![GREEN-WATCH-ONLY](assets/fr/14.webp)

Velg deretter "*Bitcoin*". For min del gjør jeg denne veiledningen på en testnet-lommebok, men prosedyren forblir identisk på mainnet.

![GREEN-WATCH-ONLY](assets/fr/15.webp)

Du blir bedt om å oppgi enten en utvidet offentlig nøkkel (`xpub`, `zpub` osv.) eller en skriptdeskriptor for utdata.

![GREEN-WATCH-ONLY](assets/fr/16.webp)

Du må derfor hente denne informasjonen fra lommeboken du ønsker å spore, via watch-only-lommeboken din. Den utvidede offentlige nøkkelen er ikke sensitiv med tanke på sikkerhet, ettersom den ikke gir tilgang til private nøkler, men den er sensitiv med tanke på konfidensialiteten din, ettersom den avslører alle dine offentlige nøkler og dermed alle dine Bitcoin-transaksjoner.

Hvis du bruker Sparrow Wallet til å administrere lommeboken din på en maskinvarelommebok, finner du denne informasjonen i "*Settings*"-delen. Hvor du finner denne informasjonen avhenger av programvaren du bruker, men den finnes vanligvis i innstillingene.

![GREEN-WATCH-ONLY](assets/fr/17.webp)

Kopier den utvidede offentlige nøkkelen din, skriv den inn i Green-applikasjonen, og klikk deretter på "Connect".

![GREEN-WATCH-ONLY](assets/fr/18.webp)

Du vil da kunne se saldoen som er knyttet til denne nøkkelen, samt transaksjonshistorikken.

![GREEN-WATCH-ONLY](assets/fr/19.webp)

Ved å klikke på "*Receive*" kan du generere en mottaksadresse for å motta bitcoins på maskinvarelommeboken din. Jeg vil imidlertid fraråde å bruke dette alternativet uten først å sjekke på skjermen til maskinvarelommeboken at den har den private nøkkelen som er knyttet til den genererte adressen, før du bruker den til å låse bitcoins. Dette er en god praksis å følge.

![GREEN-WATCH-ONLY](assets/fr/20.webp)

Med "*Balayer*"-alternativet kan du manuelt legge inn en privat nøkkel for å bruke penger direkte fra Green-applikasjonen. Bortsett fra i svært spesielle tilfeller anbefaler jeg ikke å bruke denne funksjonen, ettersom den krever at du oppgir privatnøkkelen din på en telefon, som er langt mer sårbar for dataangrep enn maskinvarelommeboken din.

![GREEN-WATCH-ONLY](assets/fr/21.webp)

Nå vet du hvordan du enkelt kan sette opp en lommebok kun for klokker på smarttelefonen din! Det er et praktisk verktøy for å overvåke en lommebok på en maskinvarelommebok uten å måtte koble til og låse den opp hver gang.

Hvis du fant denne opplæringen nyttig, ville jeg være takknemlig hvis du legger igjen en grønn tommel nedenfor. Del gjerne denne artikkelen på dine sosiale nettverk. Tusen takk skal du ha!

Jeg anbefaler også at du sjekker ut denne andre omfattende veiledningen om Blockstream Green-applikasjonen for å sette opp en hot wallet:

https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143