---
name: Satochip
description: Sette opp og bruke et Satochip-smartkort
---
![cover](assets/cover.webp)

En maskinvarelommebok er en elektronisk enhet som er dedikert til å administrere og sikre de private nøklene til en Bitcoin-lommebok. I motsetning til programvarelommebøker (eller hot wallets) som er installert på generelle maskiner som ofte er koblet til Internett, gjør maskinvarelommebøker det mulig å isolere de private nøklene fysisk, noe som reduserer risikoen for hacking og tyveri.

Hovedmålet med en maskinvarelommebok er å minimere enhetens funksjonalitet for å redusere angrepsflaten. En mindre angrepsflate betyr også færre potensielle angrepsvektorer, dvs. færre svakheter i systemet som angripere kan utnytte for å få tilgang til bitcoins.

Det anbefales å bruke en maskinvarelommebok for å sikre bitcoinsene dine, spesielt hvis du har betydelige beløp, enten i absolutt verdi eller som en andel av de totale eiendelene dine.

Maskinvare-lommebøker brukes i kombinasjon med programvare for lommebokadministrasjon på en datamaskin eller smarttelefon. Programvaren administrerer opprettelsen av transaksjoner, men den kryptografiske signaturen som er nødvendig for å validere transaksjonene, utføres utelukkende i maskinvarelommeboken. Dette betyr at de private nøklene aldri blir eksponert for et potensielt sårbart miljø.

Maskinvare-lommebøker tilbyr dobbel beskyttelse for brukeren: På den ene siden sikrer de bitcoinsene dine mot eksterne angrep ved å holde de private nøklene offline, og på den andre siden tilbyr de generelt bedre fysisk motstand mot forsøk på å trekke ut nøklene. Og det er nettopp ut fra disse to sikkerhetskriteriene at man kan bedømme og rangere de forskjellige modellene som er tilgjengelige på markedet.

I denne veiledningen foreslår jeg å oppdage en av disse løsningene: Satochip.

## Introduksjon til Satochip

Satochip er en maskinvarelommebok i form av et kort med en *EAL6+*-sertifisert chip, som er en meget høy sikkerhetsstandard (*NXP JCOP*). Den produseres av et belgisk selskap.

![SATOCHIP](assets/notext/01.webp)

Dette smartkortet selges for €25, noe som er svært rimelig sammenlignet med andre hardware-lommebøker på markedet. Brikken er et sikkert element som sikrer svært god motstand mot fysiske angrep. Dessuten er koden åpen kildekode (*AGPLv3*).

På grunn av formatet tilbyr Satochip imidlertid ikke like mange alternativer som annen maskinvare. Det er åpenbart ikke noe batteri, ikke noe kamera eller en micro SD-kortleser, siden det er et kort. Den største ulempen er etter min mening mangelen på en skjerm på maskinvarelommeboken, noe som gjør den mer sårbar for visse typer fjernangrep. Dette tvinger brukeren til å signere blindt og stole på det de ser på dataskjermen.

Til tross for sine begrensninger er Satochip fortsatt interessant på grunn av den reduserte prisen. Denne lommeboken kan spesielt brukes til å forbedre sikkerheten til en forbrukslommebok i tillegg til en sparelommebok beskyttet av en maskinvarelommebok utstyrt med en skjerm. Den er også en god løsning for de som har små mengder bitcoins og ikke ønsker å investere hundre euro i en mer sofistikert enhet. Dessuten kan bruk av Satochips i multisig-konfigurasjoner, eller potensielt i lommeboksystemer med tidslås i fremtiden, gi interessante fordeler.

Satochip-selskapet tilbyr også to andre produkter. Det er Satodime, som er et bærerkort designet for å lagre bitcoins offline, men tillater ikke transaksjoner. Det er en slags papirlommebok som er mye sikrere, som for eksempel kan brukes til å gi en gave. Til slutt er det Seedkeeper, som er en mnemonisk fraseadministrator. Den kan brukes til å lagre frøene våre på en sikker måte uten at de noteres direkte på et stykke papir.

## Hvordan kjøpe en Satochip?

Satochip er tilgjengelig for salg [på den offisielle nettsiden](https://satochip.io/product/satochip/). Hvis du vil kjøpe den i en fysisk butikk, kan du også finne [listen over sertifiserte forhandlere](https://satochip.io/resellers/) på Satochips nettsted.

Satochip tilbyr to muligheter for å samhandle med programvaren for lommebokadministrasjon: gjennom NFC-kommunikasjon eller via en smartkortleser. For NFC-alternativet må du sørge for at maskinen din er kompatibel med denne teknologien, eller anskaffe en ekstern NFC-leser. Satochip opererer på standardfrekvensen 13,56 MHz. Ellers kan du også kjøpe en smartkortleser. Du finner en slik på Satochips nettsted eller andre steder.

![SATOCHIP](assets/notext/02.webp)

## Hvordan setter jeg opp en Satochip med Sparrow?

Når du har mottatt Satochip, er det første trinnet å undersøke emballasjen for å forsikre deg om at den ikke har blitt åpnet. Satochip-emballasjen skal inneholde et forseglingsklistremerke. Hvis dette klistremerket mangler eller er skadet, kan det tyde på at smartkortet har blitt kompromittert og kanskje ikke er ekte.

![SATOCHIP](assets/notext/03.webp)

Du finner Satochip inni.

![SATOCHIP](assets/notext/04.webp)

For å administrere lommeboken foreslår jeg i denne veiledningen at du bruker Sparrow. Hvis du ennå ikke har programvaren, [besøk den offisielle nettsiden for å laste den ned] (https://sparrowwallet.com/download/). Du kan også sjekke ut vår veiledning om Sparrow Wallet (kommer snart).

![SATOCHIP](assets/notext/05.webp)

Sett Satochip-en inn i smartkortleseren eller plasser den på NFC-leseren, og koble leseren til datamaskinen der Sparrow er åpen.

![SATOCHIP](assets/notext/06.webp)

Åpne Sparrow Wallet og sørg for at du er riktig koblet til en Bitcoin-node. Dette gjør du ved å sjekke krysset nederst til høyre: det skal være gult hvis du er koblet til en offentlig node, grønt for en tilkobling til Bitcoin Core, eller blått for Electrum.

![SATOCHIP](assets/notext/07.webp)

I Sparrow Wallet klikker du på fanen "*File*".

![SATOCHIP](assets/notext/08.webp)

Deretter på menyen "*Ny lommebok*".

![SATOCHIP](assets/notext/09.webp)

Velg et navn på lommeboken din, og klikk deretter på "*Create Wallet*".

![SATOCHIP](assets/notext/10.webp)

Klikk på knappen "*Connected Hardware Wallet*".

![SATOCHIP](assets/notext/11.webp)

Klikk på knappen "*Scan...*".

![SATOCHIP](assets/notext/12.webp)

Satochip-en din skal vises. Klikk på "*Importer nøkkellager*".

![SATOCHIP](assets/notext/13.webp)

Deretter må du sette opp en PIN-kode for å låse opp Satochip. Velg et sterkt passord på mellom 4 og 16 tegn. Ta en sikkerhetskopi av dette passordet.

Vær oppmerksom på at dette passordet ikke er en passordfrase. Det betyr at selv uten dette passordet vil den mnemoniske frasen din gjøre det mulig for deg å importere lommeboken din til programvaren på nytt om nødvendig. Passordet brukes kun for å sikre tilgangen til selve Satochip. Det tilsvarer PIN-koden som finnes på andre maskinvarelommebøker.

Når passordet er skrevet inn, klikker du igjen på knappen "*Importer nøkkellager*".

![SATOCHIP](assets/notext/14.webp)

Skriv inn passordet på nytt, og klikk deretter på knappen "*Initialize*".

![SATOCHIP](assets/notext/15.webp)

Deretter kommer du til vinduet for å generere minnefrasen din. Klikk på knappen "*Generere ny*".

![SATOCHIP](assets/notext/16.webp)

Lag en eller flere fysiske kopier av gjenopprettingsfrasen din ved å skrive den ned på et papir- eller metallmedium. Vær oppmerksom på at denne frasen gir full tilgang til bitcoinsene dine uten noen ekstra beskyttelse. Hvis noen skulle oppdage den, kan de derfor umiddelbart stjele bitcoinsene dine, selv uten tilgang til Satochip-en din eller PIN-koden. Det er derfor viktig å sikre disse sikkerhetskopiene. Denne setningen lar deg dessuten få tilgang til bitcoinsene dine igjen i tilfelle tap, skade på Satochip, eller hvis du glemmer PIN-koden din.

![SATOCHIP](assets/notext/17.webp)

Bitcoin-lommeboken din har blitt opprettet.

![SATOCHIP](assets/notext/18.webp)

Klikk på knappen "*Importer nøkkellager*" igjen.

![SATOCHIP](assets/notext/19.webp)

Lommeboken din er nå opprettet. De private nøklene dine er nå lagret på smartkortet til Satochip-enheten din. Klikk på "*Apply*"-knappen for å fortsette.

![SATOCHIP](assets/notext/20.webp)

Det anbefales å sette opp et ekstra passord for å sikre den offentlige informasjonen som administreres av Sparrow Wallet, i tillegg til PIN-koden til din Satochip. Dette passordet vil sikre tilgangen til Sparrow Wallet, noe som bidrar til å beskytte dine offentlige nøkler, adresser og transaksjonshistorikk mot uautorisert tilgang.

![SATOCHIP](assets/notext/21.webp)

Skriv inn passordet ditt i de to feltene, og klikk deretter på knappen "*Set Password*".

![SATOCHIP](assets/notext/22.webp)

Og det var det, Satochip er nå konfigurert på Sparrow Wallet.

![SATOCHIP](assets/notext/23.webp)

Nå som lommeboken din er opprettet, kan du koble fra Satochip. Oppbevar den på et trygt sted!

## Hvordan motta bitcoins med Satochip?

Når du er i lommeboken, klikker du på fanen "*Mottak*".

![SATOCHIP](assets/notext/24.webp)

Sparrow Wallet genererer en adresse for lommeboken din. For andre maskinvarelommebøker anbefales det vanligvis å klikke på "*Display Address*" for å verifisere adressen direkte på enhetens skjerm. Dessverre er ikke dette alternativet tilgjengelig med Satochip, men sørg for å bruke det for andre lommebøker.

![SATOCHIP](assets/notext/25.webp)

Du kan legge til en "*Label*" for å beskrive kilden til bitcoinsene som skal sikres med denne adressen. Dette er en god praksis som hjelper deg med å administrere UTXO-ene dine bedre.

![SATOCHIP](assets/notext/26.webp)

Hvis du vil ha mer informasjon om merking, anbefaler jeg også at du tar en titt på denne andre veiledningen:

https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52
Du kan deretter bruke denne adressen til å motta bitcoins.

![SATOCHIP](assets/notext/27.webp)

## Hvordan sende Bitcoins med Satochip?

Nå som du har mottatt dine første sats i din sikre lommebok med Satochip, kan du også bruke dem! Koble Satochip til datamaskinen, start Sparrow Wallet, og gå deretter til "*Send*"-fanen for å opprette en ny transaksjon.

![SATOCHIP](assets/notext/28.webp)

Hvis du vil utføre myntkontroll, det vil si spesifikt velge hvilke UTXO-er som skal brukes i transaksjonen, går du til fanen "*UTXO-er*". Velg UTXO-ene du ønsker å bruke, og klikk deretter på "*Send Selected*". Du blir omdirigert til samme skjermbilde som i "*Send*"-fanen, men med UTXO-ene du allerede har valgt for transaksjonen.

![SATOCHIP](assets/notext/29.webp)

Skriv inn destinasjonsadressen. Du kan også legge inn flere adresser ved å klikke på knappen "*+ Legg til*".

![SATOCHIP](assets/notext/30.webp)

Noter en "*Label*" for å huske formålet med denne utgiften.

![SATOCHIP](assets/notext/31.webp)

Velg beløpet som skal sendes til denne adressen.

![SATOCHIP](assets/notext/32.webp)

Juster gebyrsatsen for transaksjonen din i henhold til gjeldende marked.

![SATOCHIP](assets/notext/33.webp)

Kontroller at alle parameterne for transaksjonen er korrekte, og klikk deretter på "*Opprett transaksjon*".

![SATOCHIP](assets/notext/34.webp)

Hvis du er fornøyd med alt, klikker du på "*Finalize Transaction for Signing*".

![SATOCHIP](assets/notext/35.webp)

Klikk på "*Signer*".

![SATOCHIP](assets/notext/36.webp)

Klikk på "*Sign*" igjen ved siden av Satochip-en din.

![SATOCHIP](assets/notext/37.webp)

Skriv inn PIN-koden til Satochip, og klikk deretter på "*Signer*" igjen for å signere transaksjonen.

![SATOCHIP](assets/notext/38.webp)

Transaksjonen din er nå signert. Klikk på "*Broadcast Transaction*" for å kringkaste den til Bitcoin-nettverket.

![SATOCHIP](assets/notext/39.webp)

Du finner den under fanen "*Transaksjoner*" i Sparrow Wallet.

![SATOCHIP](assets/notext/40.webp)

Gratulerer, du har nå fått kunnskap om hvordan du bruker Satochip! Hvis du synes denne veiledningen var nyttig, vil jeg sette pris på en tommel opp nedenfor. Del gjerne denne artikkelen på dine sosiale nettverk. Tusen takk skal du ha!