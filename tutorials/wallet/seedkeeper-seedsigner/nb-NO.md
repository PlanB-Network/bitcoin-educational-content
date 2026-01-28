---
name: Seedkeeper x SeedSigner
description: Hvordan bruker jeg Seedkeeper med min SeedSigner?
---

![cover](assets/cover.webp)



*Takk til [Satochip](https://satochip.io/) for at du har gått med på å gjenbruke [videoene deres](https://www.youtube.com/@satochip/videos) i denne veiledningen. Takk også til [Crypto Guide](https://www.youtube.com/@CryptoGuide/) for fork av SeedSigner-fastvaren, noe som muliggjør støtte for smartkort



---

SeedSigner er en wallet-maskinvare som du setter sammen selv fra standard maskinvare, vanligvis rundt en Raspberry Pi Zero. Denne wallet kalles "*stateless*": i motsetning til de fleste andre modeller på markedet (Coldcard, Trezor, Ledger, etc.), lagrer den ingen data i permanent minne, og opererer kun live fra RAM. Som et resultat blir porteføljens seed aldri lagret på SeedSigner. Hver gang du starter på nytt, må du fylle den ut for å gjøre det mulig for enheten å signere transaksjonene dine. Den vanligste metoden er å lagre seed som en QR-kode, som du deretter skanner hver gang du bruker den (*SeedQR*).



Denne tilnærmingen innebærer imidlertid en betydelig risiko: seed må være tilgjengelig i klartekst slik at den kan skannes. I tilfelle tyveri eller innbrudd kan en angriper enkelt få tak i den og stjele bitcoinsene dine.



For å overkomme denne svakheten kan SeedSigner kombineres med [**Seedkeeper**](https://satochip.io/product/seedkeeper/), et smartkort utviklet av Satochip. Dette gjør det mulig å lagre mnemoniske fraser (eller andre hemmeligheter) i en secure element som er beskyttet av en PIN-kode. Seedkeeper-appleten er åpen kildekode, og secure element har EAL6+-sertifisering. Sammen med SeedSigner tilbyr den en svært interessant sikkerhetsfunksjon: Nøklene dine administreres helt offline, du signerer transaksjonene dine på en klarert skjerm, og seed er fysisk beskyttet i et smartkort som er motstandsdyktig mot fysiske angrep.



Alt du trenger for å fullføre installasjonen, er følgende elementer:




- Det vanlige utstyret som trengs for en klassisk SeedSigner: en Raspberry Pi Zero, en Waveshare 1,3" skjerm, et kompatibelt kamera og et microSD-kort (du finner mer informasjon i SeedSigner-opplæringen nedenfor);
- SeedSigner-utvidelsessettet, som er tilgjengelig [i den offisielle Satochip-butikken](https://satochip.io/product/seedsigner-extension-kit/), lar deg lese og skrive til smartkortet direkte fra SeedSigner. Et annet alternativ er å bruke en ekstern smartkortleser, som kan kobles til en Micro-USB-port på Raspberry Pi med en kabel. Jeg har imidlertid ikke testet denne løsningen selv;
- En Seedkeeper, eller alternativt et tomt smartkort som du kan installere Seedkeeper-appleten på (utvidelsessettet som selges av Satochip, inneholder allerede et tomt smartkort).



![Image](assets/fr/01.webp)



Denne veiledningen dekker to scenarier:




- Hvis du allerede har en Bitcoin-portefølje som administreres via SeedSigner, er det bare å installere den nye fastvaren. Du kan deretter fortsette å bruke din eksisterende wallet, men denne gangen med Seedkeeper for ekstra sikkerhet.
- Hvis du ennå ikke har en Bitcoin wallet tilknyttet din SeedSigner, må du følge trinn **5** og **6** i veiledningen som er nevnt nedenfor. Disse avsnittene forklarer hvordan du lager en mnemonisk frase med SeedSigner, lagrer den via en *SeedQR*, og deretter kobler denne wallet til Sparrow Wallet for å administrere den. Jeg vil ikke gå inn på disse prosedyrene her, og **Jeg antar at du allerede har en fungerende Bitcoin wallet, konfigurert med Sparrow og din SeedSigner**.



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 1. Installer fastvare



For å bruke din SeedSigner med en Seedkeeper, må du installere en alternativ fastvare, forskjellig fra den originale SeedSigner, for å støtte smartkortlesing. For dette [anbefaler jeg å bruke fork fra "*3rdIteration*"](https://github.com/3rdIteration/seedsigner). Last ned [den nyeste versjonen av bildet](https://github.com/3rdIteration/seedsigner/releases) (`.zip`) som tilsvarer Raspberry Pi-modellen du bruker.



![Image](assets/fr/02.webp)



Hvis du ikke allerede har det, laster du ned programvaren [Balena Etcher](https://etcher.balena.io/), og gjør deretter følgende:




- Sett microSD-kortet inn i datamaskinen;
- Start Etcher ;
- Velg `.zip`-filen du nettopp har lastet ned;
- Velg microSD-kortet som mål;
- Klikk på `Flash!`.



![Image](assets/fr/03.webp)



Vent til prosessen er fullført: microSD-kortet er nå klart til bruk. Du kan nå gå videre til å montere enheten.



For mer informasjon om installasjon av fastvare og verifisering av programvare (et trinn jeg anbefaler på det sterkeste at du tar), se følgende veiledning:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Montering av smartkortleseren



![video](https://youtu.be/jqE8HDMCImA)



Begynn med å installere kameraet på Raspberry Pi Zero ved å sette det forsiktig inn i kamerapinnen og låse det med den svarte tappen. Plasser deretter Pi på bunnen av kabinettet, og sørg for at portene er på linje med de tilsvarende åpningene.



![Image](assets/fr/04.webp)



Deretter kobler du smartkortleseren til Raspberry Pi Zeros GPIO-pinner.



![Image](assets/fr/05.webp)



Skyv plastdekselet over smartkortleseren til det er riktig plassert.



![Image](assets/fr/06.webp)



Legg deretter skjermen til GPIO-pinnene i utvidelsen.



![Image](assets/fr/07.webp)



Til slutt setter du microSD-kortet som inneholder fastvaren, inn i sideporten på Raspberry Pi Zero.



![Image](assets/fr/08.webp)



Du kan nå koble til SeedSigner enten via Raspberry Pi Zeros Micro-USB-port eller via USB-C-porten på utvidelsen. Begge alternativene fungerer. Vent noen sekunder på oppstart, så bør du se velkomstskjermen vises.



![Image](assets/fr/09.webp)



For mer informasjon om det første oppsettet av SeedSigner, anbefaler jeg følgende veiledning:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Flash et smartkort med Seedkeeper-appleten (valgfritt)



![video](https://youtu.be/NF4HemyEcOY)



Hvis du allerede eier en Seedkeeper, kan du hoppe over dette trinnet og gå rett til trinn 4. I denne delen skal vi se på hvordan du installerer Seedkeeper-appleten på et tomt smartkort (DIY-metode).



For å komme i gang åpner du menyen `Verktøy > Smartkortverktøy` på SeedSigner.



![Image](assets/fr/10.webp)



Velg deretter `DIY Tools > Install Applet`.



![Image](assets/fr/11.webp)



Sett smartkortet ditt inn i SeedSigner-leseren med brikken vendt ned, og velg deretter SeedKeeper-appleten.



![Image](assets/fr/12.webp)



Vær tålmodig under installasjonen: prosessen kan ta flere titalls sekunder.



![Image](assets/fr/13.webp)



Når appleten er installert, kan du gå videre til trinn 4.



![Image](assets/fr/14.webp)



## 4. Lagre en eksisterende SeedQR på Seedkeeper



![video](https://youtu.be/X-vmFHU9Ec8)



Nå som Seedkeeperen din er i drift, kan du lagre Bitcoin wallet mnemonic på smartkortet. For å begynne, slå på SeedSigner som vanlig, og skann deretter wallets *SeedQR* for å laste den inn i enheten. Når seed er importert, velger du bare `Done`.



![Image](assets/fr/15.webp)



Når seed er lastet inn, åpner du menyen `Backup Seed`.



![Image](assets/fr/16.webp)



Sett deretter Seedkeeperen inn i SeedSigner-stasjonen, og velg alternativet `Til SeedKeeper`.



![Image](assets/fr/17.webp)



SeedSigner vil deretter be deg om å taste inn en PIN-kode for din Seedkeeper. Siden dette er et tomt kort, er det ikke definert noen kode ennå. Skriv inn en hvilken som helst kode for å hoppe over dette trinnet, og valider deretter.



![Image](assets/fr/18.webp)



SeedSigner oppdager at Seedkeeper ennå ikke er initialisert (dvs. at det ikke er angitt noe passord). Klikk på `Jeg forstår` for å fortsette.



![Image](assets/fr/19.webp)



Nå velger du Seedkeeperens nye PIN-kode, mellom 4 og 16 tegn. For ekstra sikkerhet bør du velge en lang, tilfeldig kode: Det er den eneste barrieren som beskytter fysisk tilgang til minnefrasen din.



Husk å lagre PIN-koden så snart den er opprettet, enten i en pålitelig passordbehandler eller på et separat fysisk medium, avhengig av hvilken strategi du har valgt. I sistnevnte tilfelle må du sørge for å aldri oppbevare mediet som inneholder PIN-koden på samme sted som Seedkeeper, ellers vil beskyttelsen bli ineffektiv. Det er viktig å ha en sikkerhetskopi: **Uten denne PIN-koden vil du ikke kunne få tilgang til seed, og bitcoinsene dine vil gå tapt**.



![Image](assets/fr/20.webp)



Du kan deretter definere en "etikett" som er knyttet til den mnemoniske frasen. Denne etiketten er nyttig hvis du lagrer flere hemmeligheter på Seedkeeper, slik at du enkelt kan identifisere dem.



![Image](assets/fr/21.webp)



Den mnemotekniske frasen er nå lagret på smartkortet.



![Image](assets/fr/22.webp)



Når det gjelder sikkerhetsstrategi, er det flere mulige tilnærminger, avhengig av dine behov og graden av risikoeksponering. Personlig anbefaler jeg at du beholder minst to kopier av seed:




- Dette er en nyhet for smartkort, som du kan ha lett tilgjengelig i hverdagen, for eksempel for å verifisere adresser eller signere transaksjoner. Denne metoden er praktisk (som vi skal se i del 5) og forblir sikker takket være beskyttelsen som PIN-koden gir, slik at du kan ha den tilgjengelig uten større risiko;
- En andre kopi av den ukrypterte mnemotekniske frasen din, som fungerer som den ultimate sikkerhetskopien av porteføljen din, og som kun skal brukes i tilfelle tap eller tyveri av Seedkeeper. Ettersom denne versjonen er ukryptert, må den oppbevares på et separat, sikrere sted for å forhindre samtidig kompromittering av de to sikkerhetskopiene.



Avhengig av beskyttelsesstrategi og risikoprofil kan du også duplisere seed på flere forskjellige Seedkeepers, eller opprette flere fysiske kopier av mnemoteknikken. Hvis du vil lære mer om disse fremgangsmåtene, kan du ta en titt på følgende veiledning:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 5. Laster inn en seed fra Seedkeeper



![video](https://youtu.be/ms0Iq_IyaoE)



Du kan nå bruke din Seedkeeper til å laste inn din mnemoniske frase i SeedSigner ved oppstart, og dermed signere dine Bitcoin-transaksjoner. For å begynne, slå på SeedSigner ved å koble den til, og åpne deretter menyen `Seeds`.



![Image](assets/fr/23.webp)



Velg deretter alternativet `Fra SeedKeeper`.



![Image](assets/fr/24.webp)



Sett Seedkeeperen inn i smartkortleseren, og tast deretter inn PIN-koden for å låse den opp. Bekreft inntastingen ved å trykke på bekreftelsesknappen nederst til høyre, `KEY3`.



![Image](assets/fr/25.webp)



Seedkeeper kan inneholde flere hemmeligheter, så SeedSigner ber deg om å velge den du vil laste inn. Etiketten som vises, tilsvarer navnet du definerte i trinn 4. Hvis du, som i mitt tilfelle, bare har registrert én seed, vil bare ett alternativ være tilgjengelig.



![Image](assets/fr/26.webp)



Din seed er nå lastet inn. Kontroller at dette er riktig wallet ved å sammenligne fingeravtrykket som vises på skjermen, med det som er angitt i innstillingene for Sparrow Wallet. Dette fingeravtrykket ble også oppgitt da wallet først ble opprettet.



Hvis du bruker en passphrase, kan du bruke den på dette stadiet (se del 6 av denne veiledningen). Ellers klikker du bare på "Ferdig".



![Image](assets/fr/27.webp)



Deretter kan du bruke wallet som vanlig: sjekke leveringsadressene dine og signere transaksjoner, akkurat som med en klassisk SeedSigner. For å finne ut mer om hvordan du bruker den, se den dedikerte veiledningen :



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 6. Bruke Seedkeeper med en passphrase BIP39



Bruker du en passphrase for å beskytte Bitcoin-porteføljen din? Du kan også registrere den i Seedkeeper, sammen med din seed. Denne løsningen gjør at du raskt kan laste inn wallet på SeedSigner, uten å måtte taste inn passphrase manuelt på det lille tastaturet hver gang du bruker den.



Jeg synes denne metoden er spesielt interessant, siden den lar deg dra nytte av sikkerhetsfordelene ved passphrase, samtidig som du eliminerer begrensningene som er forbundet med den daglige bruken av den. Her er et eksempel på en konfigurasjon jeg vil anbefale:




- Oppbevar seed og passphrase i en Seedkeeper, beskyttet med en sterk PIN-kode (dette er viktig). Denne sikkerhetskopien gjør det enkelt for deg å bruke wallet på daglig basis. Hvis du ønsker det, kan du duplisere denne informasjonen på en annen Seedkeeper;
- Ta også vare på en tydelig kopi av huskereglene og passphrase, på papir eller metall. Dette er din siste utvei hvis du mister Seedkeeper eller PIN-koden. Sørg for å oppbevare disse kopiene på separate steder, slik at de ikke kan kompromitteres samtidig.



I denne konfigurasjonen vil ikke noen kunne stjele noe som helst uten å kjenne til passphrase (forutsatt, selvfølgelig, at den er sterk nok til å motstå et brute-force-angrep). Omvendt, hvis noen oppdager passphrase i klartekst, vil den forbli ubrukelig uten den tilsvarende mnemoniske frasen.



Til slutt, hvis noen klarer å få fysisk tilgang til Seedkeeperen din som inneholder seed og passphrase, vil de ikke kunne hente ut noe som helst uten å kjenne PIN-koden. I motsetning til passphrase kan denne koden ikke brytes, ettersom smartkortet automatisk låser seg selv etter fem ugyldige forsøk.



Sikkerheten til denne konfigurasjonen er derfor basert på to viktige punkter:




- En **passphrase strong**: den må være lang, tilfeldig og inneholde et bredt utvalg av tegn. Kompleksiteten er ikke noe problem for deg, siden du bare trenger å skrive det inn én gang på tastaturet under initialiseringen; etterpå vil det bli overført av Seedkeeper ;
- En **sterk PIN-kode** for Seedkeeper: også den er tilfeldig og består av 16 tegn.



For å sette opp dette oppsettet, begynner du med å laste passphrase inn i SeedSigner på vanlig måte. Du kan følge prosedyren som er beskrevet i denne veiledningen:



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Når porteføljen din med passphrase er korrekt lastet inn i SeedSigner, åpner du menyen `Seeds` og velger fotavtrykket som tilsvarer denne porteføljen. Merk at dette fotavtrykket er forskjellig fra porteføljen uten passphrase.



![Image](assets/fr/28.webp)



Klikk deretter på `Backup Seed`, sett Seedkeeperen inn i stasjonen, og velg `To SeedKeeper`.



![Image](assets/fr/29.webp)



Skriv inn PIN-koden din for å låse opp Seedkeeper, og tildel deretter en etikett til denne hemmeligheten. Du kan la fingeravtrykket være etiketten for å opprettholde en form for plausibel benektelse, eller du kan for eksempel eksplisitt oppgi `Passfrase Wallet`.



![Image](assets/fr/30.webp)



Din passphrase-portefølje er nå registrert på Seedkeeper.



![Image](assets/fr/31.webp)



Neste gang du starter opp, setter du bare Seedkeeperen inn i stasjonen og navigerer til `Seeds > From SeedKeeper`.



![Image](assets/fr/32.webp)



Tast inn PIN-koden for å låse opp smartkortet, og velg deretter den wallet som tilsvarer din passphrase.



![Image](assets/fr/33.webp)



Kontroller passphrase og wallet-avtrykket, og bekreft deretter.



![Image](assets/fr/34.webp)



Du kan nå få tilgang til porteføljen din med passphrase og signere transaksjonene dine på samme måte som du normalt ville gjort med en SeedSigner.



## 7. Ytterligere alternativer



I menyen `Verktøy > Smartkortverktøy` finner du flere alternativer for å administrere Seedkeeper:





- I menyen "Fellesverktøy" kan du :
 - Kontroller kortets autentisitet;
 - Endre PIN-kode ;
 - Endre etikettene som er knyttet til hemmelighetene dine ;
 - Deaktiver NFC-funksjonen (anbefales hvis du kun bruker chipleser) ;
 - Utfør en tilbakestilling til fabrikkinnstillingene.





- I menyen `SeedKeeper-funksjoner` kan du :
 - Se listen over registrerte hemmeligheter ;
 - Lagre en ny hemmelighet ;
 - Slett en eksisterende hemmelighet ;
 - Lagre eller last inn deskriptorene dine (nyttig funksjon for multi-sig-porteføljer).





- I menyen `DIY Tools` kan du :
 - Kompilere Seedkeeper-appleten ;
 - Installer appleten på et tomt kort ;
 - Slett en Seedkeeper-applet for å tilbakestille den og gjøre den tom igjen.



Nå vet du hvordan du kan bruke Seedkeeper til å sikkerhetskopiere porteføljen din på en sikker måte i kombinasjon med SeedSigner.



Hvis dette oppsettet har overbevist deg, ikke nøl med å støtte prosjektene som gjør det mulig:




- Ved å kjøpe utstyret ditt direkte [på Satochips nettsted](https://satochip.io/shop/);
- Ved å gi [en donasjon til SeedSigner-prosjektet](https://seedsigner.com/donate/);
- Ved å abonnere på [Crypto Guides YouTube-kanal](https://www.youtube.com/@CryptoGuide/), som drives av personen som vedlikeholder GitHub-depotet som er vert for den modifiserte fastvaren.