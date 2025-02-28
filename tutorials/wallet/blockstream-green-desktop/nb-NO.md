---
name: Blockstream Green - Desktop
description: Bruke Green Wallet på datamaskinen din
---
![cover](assets/cover.webp)

I denne veiledningen forklarer vi hvordan du bruker Blockstream Green-programvaren på datamaskinen din til å administrere en sikker lommebok på en maskinvarelommebok. Når du bruker en maskinvarelommebok, er det viktig å bruke programvare på datamaskinen din for å administrere lommeboken. Denne administrasjonsprogramvaren har ingen tilgang til private nøkler; den brukes kun til å se saldoen i lommeboken, generere mottakeradresser og opprette og distribuere transaksjoner som skal signeres av maskinvarelommeboken. Green er bare én av de mange løsningene som er tilgjengelige for å administrere Bitcoin-maskinvarelommeboken din.

I 2024 er Blockstream Green kun kompatibel med Ledger Nano S (gammel versjon), Ledger Nano X, Trezor One, Trezor T og Blockstream Jade-enheter.

## Vi introduserer Blockstream Green

Blockstream Green er en programvare som er tilgjengelig på mobil og PC. Denne porteføljen var tidligere kjent som Green Address, men ble et Blockstream-prosjekt etter oppkjøpet i 2016.

Green er et svært brukervennlig program, noe som gjør det spesielt egnet for nybegynnere. Det tilbyr ulike funksjoner, for eksempel administrasjon av varme lommebøker, maskinvarelommebøker samt lommebøker på Liquid-sidekjeden. Du kan også bruke den til å sette opp en lommebok kun for klokker.

![GREEN-DESKTOP](assets/fr/01.webp)

I denne veiledningen konsentrerer vi oss utelukkende om å bruke programvaren på datamaskinen. Hvis du vil utforske andre bruksområder for Green, kan du se våre andre dedikerte veiledninger:

https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143
https://planb.network/tutorials/wallet/mobile/blockstream-green-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb
## Installere og konfigurere Blockstream Green-programvaren

Start med å installere Blockstream Green-programvaren på datamaskinen din. Gå til [det offisielle nettstedet] (https://blockstream.com/green/) og klikk på "*Last ned nå*"-knappen. Følg deretter installasjonsprosessen i henhold til operativsystemet ditt.

![GREEN-DESKTOP](assets/fr/02.webp)

Start programmet, og kryss av i boksen "Jeg godtar vilkårene...*".

![GREEN-DESKTOP](assets/fr/03.webp)

Når du åpner Green for første gang, vises startskjermbildet uten en konfigurert portefølje. Hvis du senere oppretter eller importerer porteføljer, vil de vises i dette grensesnittet. Før du oppretter en portefølje, anbefaler jeg at du justerer innstillingene i programmet slik at de passer til dine behov. Klikk på Innstillinger-ikonet nederst i venstre hjørne.

![GREEN-DESKTOP](assets/fr/04.webp)

I menyen "*General*" kan du endre programvarens språk og aktivere eksperimentelle funksjoner hvis du ønsker det.

![GREEN-DESKTOP](assets/fr/05.webp)

I menyen "*Nettverk*" kan du aktivere tilkobling via Tor, et nettverk som krypterer alle forbindelsene dine og gjør det vanskelig å spore aktivitetene dine. Selv om dette alternativet kan gjøre programmet litt tregere, anbefales det på det sterkeste for å beskytte personvernet ditt, spesielt hvis du ikke bruker din egen komplette node.

![GREEN-DESKTOP](assets/fr/06.webp)

For brukere som har sin egen komplette node, tilbyr Green muligheten til å koble seg til den via en Electrum-server, noe som garanterer total kontroll over Bitcoin-nettverksinformasjon og transaksjonsformidling. For å gjøre dette, klikk på menyen "*Tilpassede servere og validering*", og skriv deretter inn Electrum-serverdetaljene dine.

![GREEN-DESKTOP](assets/fr/07.webp)

En annen alternativ funksjon er alternativet "*SPV Verification*", som lar deg verifisere visse blokkjededata direkte og dermed redusere behovet for å stole på Blockstreams standardnode, selv om denne metoden ikke gir alle garantiene til en full node. Dette alternativet finner du også i menyen "*Custom servers and validation*".

![GREEN-DESKTOP](assets/fr/08.webp)

Når du har justert disse parameterne etter dine behov, kan du avslutte dette grensesnittet.

## Importer en Bitcoin-lommebok på Blockstream Green

Du er nå klar til å importere Bitcoin-lommeboken din. Klikk på "**Gå i gang**"-knappen.

![GREEN-DESKTOP](assets/fr/09.webp)

Du kan velge mellom å opprette en lokal programvarelommebok eller å administrere en kald lommebok via en maskinvarelommebok. I denne veiledningen konsentrerer vi oss om å administrere en maskinvarelommebok, så du må velge alternativet "*On Hardware Wallet*".

Med alternativet "*Watch-only*" kan du importere en utvidet offentlig nøkkel (`xpub`) for å se porteføljetransaksjoner uten å kunne bruke de tilknyttede midlene.

![GREEN-DESKTOP](assets/fr/10.webp)

Hvis du bruker en Jade, klikker du på den tilhørende knappen. Ellers velger du "*Connect a different Hardware Device*". I mitt tilfelle bruker jeg en Ledger Nano S. For Ledger-brukere må du sørge for å installere "*Bitcoin Legacy*"-applikasjonen på maskinvarelommeboken din, da Green kun støtter denne versjonen.

![GREEN-DESKTOP](assets/fr/11.webp)

Koble maskinvarelommeboken til datamaskinen, og velg Grønn.

![GREEN-DESKTOP](assets/fr/12.webp)

Vent til Green har importert porteføljeinformasjonen din, og deretter kan du få tilgang til den.

![GREEN-DESKTOP](assets/fr/13.webp)

På dette tidspunktet er det to mulige scenarier. Hvis du har brukt maskinvarelommeboken din før, bør du se kontoen din i programvaren. Men hvis du, som meg, nettopp har initialisert maskinvarelommeboken din ved å generere en mnemonisk frase uten å ha brukt den ennå, må du opprette en konto. Klikk på "*Opprett konto*".

![GREEN-DESKTOP](assets/fr/14.webp)

Velg "*Standard*" hvis du ønsker å bruke en klassisk lommebok.

![GREEN-DESKTOP](assets/fr/15.webp)

Du har nå tilgang til kontoen din.

![GREEN-DESKTOP](assets/fr/16.webp)

## Bruk av en maskinvarelommebok med Blockstream Green

Nå som Bitcoin-lommeboken din er satt opp, er du klar til å motta dine første sats! Bare klikk på "*Motta*"-knappen.

![GREEN-DESKTOP](assets/fr/17.webp)

Klikk på knappen "*Kopier adresse*" for å kopiere adressen, eller skann QR-koden.

![GREEN-DESKTOP](assets/fr/18.webp)

Når transaksjonen har blitt kringkastet i nettverket, vil den vises i lommeboken din. Vent til du har mottatt nok bekreftelser til at transaksjonen ikke kan endres.

![GREEN-DESKTOP](assets/fr/19.webp)

Med bitcoins i lommeboken din er du nå klar til å sende dem. Klikk på "*Send*"-knappen.

![GREEN-DESKTOP](assets/fr/20.webp)

På neste side skriver du inn mottakerens adresse. Du kan skrive den inn manuelt eller skanne en QR-kode med webkameraet ditt.

![GREEN-DESKTOP](assets/fr/21.webp)

Velg betalingsbeløpet.

![GREEN-DESKTOP](assets/fr/22.webp)

Nederst på skjermen kan du velge gebyrsats for denne transaksjonen. Du kan velge om du vil følge programmets anbefalinger eller tilpasse gebyrene selv. Jo høyere gebyret er i forhold til andre ventende transaksjoner, desto raskere vil transaksjonen bli behandlet. For informasjon om gebyrmarkedet, se [Mempool.space] (https://mempool.space/) i delen "*Transaksjonsgebyrer*".

![GREEN-DESKTOP](assets/fr/23.webp)

Hvis du ønsker å velge hvilke UTXO-er som skal brukes i transaksjonen, klikker du på knappen "*Manuelt myntvalg*".

![GREEN-DESKTOP](assets/fr/24.webp)

Kontroller transaksjonsparametrene, og hvis alt er som du forventer, klikker du på "*Neste*".

![GREEN-DESKTOP](assets/fr/25.webp)

Dobbeltsjekk at adressen, beløpet og kostnadene er korrekte, og klikk deretter på "*Bekreft transaksjon*".

![GREEN-DESKTOP](assets/fr/26.webp)

Kontroller at alle transaksjonsparametrene er korrekte på skjermen til maskinvarelommeboken, og signer deretter transaksjonen ved hjelp av den.

![GREEN-DESKTOP](assets/fr/27.webp)

Når transaksjonen er signert fra maskinvarelommeboken, sender Green den automatisk til Bitcoin-nettverket. Transaksjonen vises deretter på dashbordet i Bitcoin-lommeboken din, i påvente av bekreftelse.

![GREEN-DESKTOP](assets/fr/28.webp)

Nå vet du hvordan du enkelt konfigurerer Blockstream Green for å administrere Bitcoin-lommeboken din på en maskinvarelommebok.

Hvis du fant denne opplæringen nyttig, ville jeg være takknemlig hvis du legger igjen en grønn tommel nedenfor. Del gjerne denne artikkelen på dine sosiale nettverk. Tusen takk skal du ha!

Jeg anbefaler også at du sjekker ut denne andre omfattende veiledningen om Blockstream Green-mobilappen for å sette opp en hot wallet:

https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143