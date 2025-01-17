---
name: Tapsigner
description: Sette opp og bruke en Tapsigner med Nunchuk
---
![cover](assets/cover.webp)

En maskinvarelommebok er en elektronisk enhet som er dedikert til å administrere og sikre Bitcoin-lommebokens private nøkler. I motsetning til programvarelommebøker (eller hot wallets) som er installert på generelle maskiner som ofte er koblet til Internett, gjør maskinvarelommebøker det mulig å isolere de private nøklene fysisk, noe som reduserer risikoen for hacking og tyveri.

Hovedmålet med en maskinvarelommebok er å minimere enhetens funksjonalitet for å redusere angrepsflaten. En mindre angrepsflate betyr også færre potensielle angrepsvektorer, dvs. færre svake punkter i systemet som angripere kan utnytte for å få tilgang til bitcoins.

Det anbefales å bruke en maskinvarelommebok for å sikre bitcoinsene dine, spesielt hvis du har betydelige beløp, enten i absolutt verdi eller som en andel av de totale eiendelene dine.

Maskinvare-lommebøker brukes i kombinasjon med en programvare for lommebokadministrasjon på en datamaskin eller smarttelefon. Programvaren administrerer opprettelsen av transaksjoner, men den kryptografiske signaturen som er nødvendig for å validere transaksjonene, utføres utelukkende i maskinvarelommeboken. Dette betyr at de private nøklene aldri blir eksponert for et potensielt sårbart miljø.

Maskinvare-lommebøker tilbyr dobbel beskyttelse for brukeren: På den ene siden sikrer de bitcoinsene dine mot eksterne angrep ved å holde de private nøklene offline, og på den andre siden tilbyr de generelt bedre fysisk motstand mot forsøk på å trekke ut nøklene. Og det er nettopp ut fra disse to sikkerhetskriteriene at man kan bedømme og rangere de forskjellige modellene som er tilgjengelige på markedet.

I denne veiledningen foreslår jeg å oppdage en av disse løsningene: Tapsigner fra Coinkite.

## Introduksjon til Tapsigner

Tapsigner er en maskinvarelommebok designet i form av et NFC-kort av selskapet Coinkite, som også er kjent for å produsere Coldcards.

![TAPSIGNER NUNCHUK](assets/notext/01.webp)

Tapsigner gjør det mulig å lagre et par bestående av en privat hovednøkkel og en kjedekode i samsvar med BIP32, slik at man får et tre av kryptografiske nøkler. Disse nøklene kan brukes til å signere transaksjoner ved å plassere Tapsigner mot en telefon eller en NFC-kortleser.

Dette NFC-kortet selges for $ 19.99, noe som er veldig rimelig sammenlignet med andre maskinvarelommebøker som er tilgjengelige på markedet. På grunn av formatet tilbyr Tapsigner imidlertid ikke så mange alternativer som andre enheter. Det er åpenbart ikke noe batteri, ikke noe kamera eller en micro SD-kortleser, da det er et kort. Etter min mening er den største ulempen mangelen på en skjerm på maskinvarelommeboken, noe som gjør den mer sårbar for visse typer fjernangrep. Dette tvinger brukeren til å signere blindt og stole på det de ser på dataskjermen.

Til tross for sine begrensninger kan Tapsigner være interessant på grunn av sin reduserte pris. Denne lommeboken kan spesielt brukes til å forbedre sikkerheten til en forbrukslommebok i tillegg til en sparelommebok beskyttet av en maskinvarelommebok utstyrt med en skjerm. Det representerer også en god løsning for de som har små mengder bitcoins og ikke ønsker å investere hundre euro i en mer sofistikert enhet. Dessuten kan bruken av Tapsigner i multisig-konfigurasjoner, eller potensielt i lommeboksystemer med tidslås i fremtiden, gi interessante fordeler.

## Hvordan kjøpe en Tapsigner?

Tapsigner er tilgjengelig for kjøp [på Coinkites offisielle nettsted](https://store.coinkite.com/store/category/tapsigner). Hvis du vil kjøpe den i en fysisk butikk, kan du også finne [listen over sertifiserte forhandlere](https://coinkite.com/resellers) på nettstedet.

Du trenger også en telefon som er kompatibel med NFC-kommunikasjon, eller en USB-enhet som kan lese NFC-kort på standardfrekvensen 13,56 MHz.

## Hvordan initialiserer jeg en Tapsigner med Nunchuk?

Når du har mottatt Tapsigner, er det første trinnet å undersøke emballasjen for å forsikre deg om at den ikke har blitt åpnet. Hvis pakken er skadet, kan det tyde på at kortet har blitt kompromittert og kanskje ikke er autentisk. CoinKite leverer din Tapsigner med et etui som blokkerer radiobølger. Forsikre deg om at det er til stede i pakken.

![TAPSIGNER NUNCHUK](assets/notext/02.webp)

For å administrere lommeboken bruker vi mobilappen **Nunchuk Wallet**. Sørg for at smarttelefonen din er NFC-kompatibel, og last deretter ned Nunchuk fra [Google Play Store] (https://play.google.com/store/apps/details?id=io.nunchuk.android), [App Store] (https://apps.apple.com/us/app/nunchuk-bitcoin-wallet/id1563190073) eller direkte via [`.apk`-filen] (https://github.com/nunchuk-io/nunchuk-android/releases).

![TAPSIGNER NUNCHUK](assets/notext/03.webp)

Hvis du bruker Nunchuk for første gang, vil appen be deg om å opprette en konto. I denne veiledningen er det ikke nødvendig å opprette en konto. Velg "*Fortsett som gjest*" for å fortsette uten konto.

![TAPSIGNER NUNCHUK](assets/notext/04.webp)

Klikk deretter på "*Uassistert lommebok*".

![TAPSIGNER NUNCHUK](assets/notext/05.webp)

Deretter klikker du på knappen "*Jeg utforsker på egen hånd*".

![TAPSIGNER NUNCHUK](assets/notext/06.webp)

Når du er i Nunchuk, klikker du på "*+*"-knappen ved siden av "*Keys*"-fanen.

![TAPSIGNER NUNCHUK](assets/notext/07.webp)

Velg "*Legg til NFC-nøkkel*".

![TAPSIGNER NUNCHUK](assets/notext/08.webp)

Klikk deretter på "*Add TAPSIGNER*".

![TAPSIGNER NUNCHUK](assets/notext/09.webp)

Klikk på "*Continue*", og plasser deretter Tapsigner NFC-kortet mot smarttelefonen.

![TAPSIGNER NUNCHUK](assets/notext/10.webp)

Hvis Tapsigner er ny, vil Nunchuk tilby deg å initialisere den. Klikk på "*Yes*".

![TAPSIGNER NUNCHUK](assets/notext/11.webp)

Du må nå velge hvordan du genererer hovedkjedekoden.

Tapsigner bruker BIP32-standarden. Dette betyr at utledningen av de kryptografiske nøklene som sikrer bitcoinsene dine, ikke er avhengig av en mnemonisk frase som BIP39-lommebøker, men direkte av den private hovednøkkelen og hovedkjedekoden. Disse to elementene sendes gjennom HMAC-funksjonen for å utlede resten av lommeboken din på en deterministisk og hierarkisk måte.

Den private hovednøkkelen genereres direkte av TRNG (*True Random Number Generator*) som er integrert i Tapsigner. Masterkjedekoden må derimot oppgis utenfra. På dette trinnet har du valget mellom å la Nunchuk generere den automatisk ved å klikke på "*Automatisk*", eller å generere den selv ved å velge "*Avansert*" og skrive den inn i det angitte feltet.

![TAPSIGNER NUNCHUK](assets/notext/12.webp)

Deretter må du velge en PIN-kode. I området "*Start PIN*" skriver du inn PIN-koden som står på baksiden av Tapsigner.

![TAPSIGNER NUNCHUK](assets/notext/13.webp)

Velg en PIN-kode for å sikre fysisk tilgang til Tapsigner. Denne PIN-koden spiller ingen rolle i prosessen med å gjenopprette lommeboken. Dens eneste funksjon er å låse opp Tapsigner for å signere transaksjoner. Sørg for å lagre denne PIN-koden for å unngå å glemme den. Klikk på "*Fortsett*" for å fortsette.

![TAPSIGNER NUNCHUK](assets/notext/14.webp)

Plasser Tapsigner-kortet på baksiden av telefonen for å initialisere den.

![TAPSIGNER NUNCHUK](assets/notext/15.webp)

Nunchuk genererer deretter gjenopprettingsfilen for lommeboken din, slik at du kan få tilgang til bitcoinsene dine igjen hvis du mister NFC-kortet ditt. Denne filen er kryptert med sikkerhetskopieringskoden som er skrevet på baksiden av Tapsigner. For å få tilbake bitcoinsene dine trenger du absolutt denne filen samt koden for å dekryptere den. Det er derfor viktig å ta en papirkopi av denne koden, for hvis du mister NFC-kortet ditt, vil tilgangen til denne koden også gå tapt, siden den foreløpig bare er skrevet på kortet. Sørg også for å ta flere sikkerhetskopier av den krypterte gjenopprettingsfilen.

![TAPSIGNER NUNCHUK](assets/notext/16.webp)

Velg et navn til lommeboken din.

![TAPSIGNER NUNCHUK](assets/notext/17.webp)

Grunnlaget for lommeboken din er nå satt opp. Du kan når som helst klikke på knappen "*Kjør helsesjekk*" for å bekrefte ektheten til din Tapsigner.

![TAPSIGNER NUNCHUK](assets/notext/18.webp)

Tast inn PIN-koden din.

![TAPSIGNER NUNCHUK](assets/notext/19.webp)

Plasser deretter kortet på baksiden av telefonen.

![TAPSIGNER NUNCHUK](assets/notext/20.webp)

## Hvordan oppretter jeg en lommebok på en Tapsigner?

Tilbake på Nunchuk-hjemmesiden kan du se at Tapsigner er registrert blant de tilgjengelige signeringsenhetene.

![TAPSIGNER NUNCHUK](assets/notext/21.webp)

Du må nå generere nøklene til Bitcoin-lommeboken din. Dette gjør du ved å klikke på "*+*"-knappen til høyre for "*Wallets*"-fanen.

![TAPSIGNER NUNCHUK](assets/notext/22.webp)

Klikk på "*Opprett ny lommebok*".

![TAPSIGNER NUNCHUK](assets/notext/23.webp)

Velg deretter alternativet "*Opprett en ny lommebok ved hjelp av eksisterende nøkler*".

![TAPSIGNER NUNCHUK](assets/notext/24.webp)

Velg et navn på lommeboken din, og klikk deretter på "*Fortsett*".

![TAPSIGNER NUNCHUK](assets/notext/25.webp)

Velg Tapsigner som signeringsenhet for dette nye settet med nøkler, og klikk deretter på "*Fortsett*".

![TAPSIGNER NUNCHUK](assets/notext/26.webp)

Hvis alt er tilfredsstillende, bekrefter du opprettelsen.

![TAPSIGNER NUNCHUK](assets/notext/27.webp)

Deretter kan du lagre konfigurasjonsfilen til lommeboken din. Denne filen inneholder utelukkende dine offentlige nøkler, noe som betyr at selv om noen får tilgang til den, kan de ikke stjele bitcoinsene dine. De kan imidlertid følge med på alle transaksjonene dine. Derfor utgjør denne filen kun en risiko for personvernet ditt. I noen tilfeller kan den være avgjørende for å gjenopprette lommeboken din.

![TAPSIGNER NUNCHUK](assets/notext/28.webp)

Og der har du det, lommeboken din er opprettet!

![TAPSIGNER NUNCHUK](assets/notext/29.webp)

Når du ikke bruker Tapsigner, må du huske å oppbevare den i etuiet fra Coinkite, som blokkerer radiobølger for å beskytte mot uautoriserte avlesninger.

## Hvordan motta bitcoins på Tapsigner?

For å motta bitcoins klikker du på lommeboken din.

![TAPSIGNER NUNCHUK](assets/notext/30.webp)

Bruk deretter den genererte adressen til å motta bitcoins. Hvis du tidligere har mottatt bitcoins på denne lommeboken, må du klikke på "*Receive*"-knappen for å generere en ny tom mottakeradresse.

![TAPSIGNER NUNCHUK](assets/notext/31.webp)

Når avsenderens transaksjon er sendt, vil du se den i lommeboken din.

![TAPSIGNER NUNCHUK](assets/notext/32.webp)

Klikk på "*Vis mynter*".

![TAPSIGNER NUNCHUK](assets/notext/33.webp)

Velg din nye UTXO.

![TAPSIGNER NUNCHUK](assets/notext/34.webp)

Klikk på "*+*" ved siden av "*Tags*" for å legge til en etikett på UTXO-en din. Dette er en god praksis, ettersom det hjelper deg med å huske hvor myntene dine kommer fra og optimaliserer personvernet ditt for fremtidig bruk.

![TAPSIGNER NUNCHUK](assets/notext/35.webp)

Velg en eksisterende tagg eller opprett en ny, og klikk deretter på "*Lagre*". Du har også mulighet til å opprette "*samlinger*" for å organisere myntene dine på en mer strukturert måte.

![TAPSIGNER NUNCHUK](assets/notext/36.webp)

## Hvordan sende bitcoins med Tapsigner?

Nå som du har bitcoins i lommeboken din, kan du også sende dem. For å gjøre dette klikker du på lommeboken du ønsker.

![TAPSIGNER NUNCHUK](assets/notext/37.webp)

Klikk på "*Send*"-knappen.

![TAPSIGNER NUNCHUK](assets/notext/38.webp)

Velg beløpet du vil sende, og klikk deretter på "*Fortsett*".

![TAPSIGNER NUNCHUK](assets/notext/39.webp)

Legg til en "*note*" i den fremtidige transaksjonen for å huske formålet med den.

![TAPSIGNER NUNCHUK](assets/notext/40.webp)

Deretter skriver du inn mottakerens adresse manuelt i det angitte feltet.

![TAPSIGNER NUNCHUK](assets/notext/41.webp)

Du kan også skanne en QR-kodekodet adresse ved å klikke på ikonet øverst til høyre på skjermen.

![TAPSIGNER NUNCHUK](assets/notext/42.webp)

Klikk på knappen "*Opprett transaksjon*".

![TAPSIGNER NUNCHUK](assets/notext/43.webp)

Bekreft detaljene i transaksjonen, og klikk deretter på "*Signer*"-knappen ved siden av Tapsigner.

![TAPSIGNER NUNCHUK](assets/notext/44.webp)

Tast inn PIN-koden din for å låse den opp.

![TAPSIGNER NUNCHUK](assets/notext/45.webp)

Plasser deretter Tapsigner på baksiden av smarttelefonen.

![TAPSIGNER NUNCHUK](assets/notext/46.webp)

Transaksjonen din er nå signert. Sjekk en siste gang at alt er riktig, og klikk deretter på "*Broadcast Transaction*" for å kringkaste den på Bitcoin-nettverket.

![TAPSIGNER NUNCHUK](assets/notext/47.webp)

Transaksjonen din venter nå på bekreftelse.

![TAPSIGNER NUNCHUK](assets/notext/48.webp)

## Hvordan gjenopprette lommeboken i tilfelle tap av Tapsigner?

Hvis du har mistet Tapsigneren din, kan du få tilbake lommeboken din ved hjelp av koden som står på baksiden av kortet. Det er derfor viktig å lagre denne koden separat fra Tapsigner, for hvis kortet går tapt, vil også tilgangen til denne koden gå tapt. Du trenger også den krypterte sikkerhetskopien av lommeboken.

For gjenoppretting vil vi bruke Nunchuk-appen, men husk at dette betyr at du midlertidig må sikre pengene dine i en varm lommebok. Hvis Tapsigneren din sikret betydelige beløp, bør du vurdere å følge den samme gjenopprettingsprosessen med et nytt Coldcard i stedet.

Åpne Nunchuk-appen, og klikk på "*+*"-knappen ved siden av "*Keys*"-fanen.

![TAPSIGNER NUNCHUK](assets/notext/49.webp)

Velg "*Legg til NFC-nøkkel*".

![TAPSIGNER NUNCHUK](assets/notext/50.webp)

Velg alternativet "*Gjenopprett TAPSIGNER-nøkkel fra sikkerhetskopi*".

![TAPSIGNER NUNCHUK](assets/notext/51.webp)

Du blir deretter omdirigert til enhetens filutforsker. Finn og velg den krypterte sikkerhetskopifilen til lommeboken din. Navnet på denne filen starter vanligvis med `backup...`.

![TAPSIGNER NUNCHUK](assets/notext/52.webp)

Skriv inn passordet som dekrypterer sikkerhetskopifilen. Dette passordet tilsvarer det som opprinnelig er angitt på baksiden av Tapsigner.

![TAPSIGNER NUNCHUK](assets/notext/53.webp)

Velg deretter et navn for gjenopprettingslommeboken.

![TAPSIGNER NUNCHUK](assets/notext/54.webp)

Du har nå fått tilbake tilgangen til bitcoinsene dine. Lommeboken din administreres nå som en hot wallet som er synlig i "*Keys*"-fanen i Nunchuk-appen. Deretter må du opprette et nytt sett med kryptografiske nøkler i "*Wallets*"-delen ved å knytte denne nøkkelen til den. For å gjøre dette kan du følge trinnene igjen i delen "*Hvordan opprette en lommebok på en Tapsigner*" i denne veiledningen.

![TAPSIGNER NUNCHUK](assets/notext/55.webp)

Hvis du har mistet din Tapsigner, anbefaler jeg deg på det sterkeste å umiddelbart overføre bitcoinsene dine til en annen lommebok du eier, ideelt sett beskyttet av en maskinvarelommebok. Tapsigneren du har mistet kan potensielt være i gale hender. Det er derfor viktig å tømme lommeboken du nettopp har fått tilbake, og slutte å bruke den.

Gratulerer, du er nå i gang med å bruke Tapsigner! Hvis du fant denne opplæringen nyttig, vil jeg sette pris på det hvis du kan legge igjen en tommel opp nedenfor. Del gjerne denne artikkelen på dine sosiale nettverk. Tusen takk skal du ha!