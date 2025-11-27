---
name: BIP-39 Passordfrase SeedSigner
description: Hvordan legger jeg til en passphrase i SeedSigner-porteføljen min?
---

![cover](assets/cover.webp)



En passphrase BIP39 er et valgfritt passord som, kombinert med den mnemoniske frasen, gir et ekstra sikkerhetslag for deterministiske og hierarkiske Bitcoin-lommebøker. I denne veiledningen vil vi sammen finne ut hvordan du setter opp en passphrase på din Bitcoin wallet som brukes med en SeedSigner.



![Image](assets/fr/01.webp)



## Forutsetninger før du legger til en passordfrase



Hvis du ikke er kjent med passphrase-konseptet, hvordan det fungerer og hvilke konsekvenser det har for din Bitcoin wallet, anbefaler jeg på det sterkeste at du leser denne andre teoretiske artikkelen der jeg forklarer alt (dette er veldig viktig, ettersom bruk av en passphrase uten å forstå hvordan den fungerer kan sette bitcoinsene dine i fare) :



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Før du starter denne veiledningen, må du også forsikre deg om at du allerede har initialisert din SeedSigner og generert din mnemoniske frase. Hvis du ikke har gjort det, og din SeedSigner er helt ny, kan du følge veiledningen på Plan ₿ Academy. Når du har fullført dette trinnet, kan du gå tilbake til denne veiledningen:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## Hvordan legger jeg til en passphrase i SeedSigner?



Når du legger til en passphrase i porteføljen din som administreres via SeedSigner, opprettes det en helt ny portefølje som genererer et helt separat sett med nøkler. Hvis du allerede har en portefølje som inneholder satss, vil du derfor ikke lenger kunne få tilgang til den med passphrase, siden den genererer en helt annen portefølje.



For å bruke en passphrase på din SeedSigner, slår du på enheten og skanner din SeedQR som vanlig. SeedSigner vil da vise fingeravtrykket til din nåværende wallet, som tilsvarer den **uten passphrase**. wallet med passphrase vil ha et annet fingeravtrykk.



Klikk på knappen `BIP-39 Passphrase`.



![Image](assets/fr/02.webp)



Skriv deretter inn den passphrase du ønsker i det angitte feltet ved hjelp av tastaturet på skjermen. Sørg for å ta en eller flere fysiske sikkerhetskopier (papir eller metall): tap av denne passphrase vil føre til permanent tap av tilgang til bitcoinsene dine. **For å gjenopprette en wallet er både huskeregelen og passphrase avgjørende ** Hvis en av dem går tapt, vil bitcoinsene dine bli ugjenkallelig blokkert.



Når du har fullført oppføringen, validerer du ved å trykke på `KEY3`-knappen nederst til høyre på SeedSigner.



![Image](assets/fr/03.webp)



*I dette eksempelet brukte jeg passphrase `pba`. I ditt tilfelle må du imidlertid sørge for at du velger en robust passphrase. For å finne ut hvordan du definerer en optimal passphrase, kan du lese denne andre artikkelen:*



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

SeedSigner viser deretter det nye fingeravtrykket til din passphrase wallet. Lag flere kopier av dette fingeravtrykket: Det er viktig når du bruker en wallet med passphrase, ettersom det gjør at du hver gang du skriver inn passphrase, kan kontrollere at du ikke har gjort noen skrivefeil og at du får tilgang til riktig wallet.



Hvis jeg for eksempel ved en feiltakelse skriver ned passphrase `Pba` når jeg starter SeedSigner i stedet for `pba`, vil denne enkle endringen fra små til store bokstaver føre til at det opprettes en helt annen portefølje enn den jeg ønsker tilgang til.



Dette fingeravtrykket utgjør ingen risiko for sikkerheten eller konfidensialiteten til wallet. Det avslører ingen informasjon, offentlig eller privat, om nøklene dine. I motsetning til mnemonikken og passphrase kan du lagre fingeravtrykket på et digitalt medium. Jeg anbefaler at du oppbevarer en kopi flere steder: på et stykke papir, i en passordbehandler osv.



Når du har lagret fingeravtrykket ditt, klikker du på "Ferdig".



![Image](assets/fr/04.webp)



Du har da tilgang til alle porteføljens funksjoner, akkurat som på en klassisk SeedSigner.



![Image](assets/fr/05.webp)



Du kan nå importere keystore til Sparrow Wallet og bruke din wallet som normalt. Hver gang du starter på nytt, må du både skanne SeedQR og skrive inn passphrase på nytt ved hjelp av tastaturet, slik vi gjorde her.



Før du faktisk bruker wallet med passphrase, anbefaler jeg på det sterkeste at du utfører en fullstendig tom gjenopprettingstest. På denne måten kan du bekrefte at sikkerhetskopiene av den mnemoniske frasen og passphrase er gyldige. Hvis du vil lære hvordan du utfører denne kontrollen, kan du se følgende veiledning:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895