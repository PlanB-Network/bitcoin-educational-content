---
name: Nerdminer
description: Start å utvinne bitcoin med en sjanse for å vinne nær 0
---

![cover](assets/cover.webp)

> Sette opp din NerdMiner_v2

I denne veiledningen vil vi lede deg gjennom de nødvendige stegene for å sette opp en NerdMiner_v2, som er en maskinvareenhet (en ESP-32 S3) dedikert til bitcoin-utvinning.
Selvfølgelig kan ikke databehandlingskraften til en slik enhet konkurrere med ASIC-ene til amatør- eller profesjonelle utvinnere. Likevel er NerdMiner et perfekt pedagogisk verktøy for å gjøre bitcoin-utvinning håndgripelig. Og hvem vet, med (mye) flaks, kan du finne en blokk og belønningen som følger med den. For de nysgjerrige, vil vi se i [Estimering av sannsynligheten for å vinne](#estimation-de-la-probabilite-de-gain) seksjonen. Når det gjelder strømforbruk, bruker en NerdMiner 0.5W; til sammenligning forbruker en LED-lampe i gjennomsnitt 20 ganger mer.

Før vi går gjennom de forskjellige stegene, la oss liste opp det nødvendige utstyret for å lage det:

- en [Lilygo T-display S3](https://lilygo.cc/products/t-display-s3)
- en [USB-C strømforsyning](https://amzn.eu/d/gIOot90)
- et 3D-deksel: hvis du har en 3D-printer, kan du laste ned [3D-filen](https://www.printables.com/model/501547-nerdminer-v2-click-case-w-buttons) ellers kan du kjøpe en på [Silexperience online butikk](https://silexperience.company.site/NerdMiner_V2-p544379757).
- en PC med Chrome-nettleser installert
- en internettforbindelse
- en bitcoin-adresse

Du kan også kjøpe et forhåndsmontert NerdMiner-kit fra flere forhandlere som:

- [DécouvreBitcoin](https://shop.decouvrebitcoin.com/products/nerd-miner?_pos=1&_psq=nerd&_ss=e&_v=1.0)
- [BitMaker](https://bitronics.store/shop/)

Først vil vi se hvordan du flasher programvaren på ESP-32 S3, og deretter vil vi se hvordan du omstarter den for å endre wifi-nettverket. Disse stegene er for Windows-brukere, hvis du bruker et Linux OS, vennligst utfør [forberedende steg](#etapes-preliminaires-pour-utilisateurs-linux) for å tillate gjenkjenning av ESP-32 S3 av systemet ditt.

# Installasjon av NerdMiner_v2-programvare

Installasjonen av programvaren er sterkt forenklet takket være bruken av webflasher.

## Steg 1: Forberedelse av webflasher

Først må du gå til [online NM2 flasher](https://bitmaker-hub.github.io/diyflasher/).

Velg deretter firmwaren som tilsvarer din ESP-32. De fleste ganger er det den som er standard: T-Display S3. Klikk deretter på "Flash".

> ⚠️ Det er viktig at du bruker Chrome-nettleseren - da den tillater, som standard, bruk av flash og tilgang til USB-portene dine.

![](assets/webflasher.webp)

## Steg 2: Koble til ESP-32

Når webflasher er lansert, vil et pop-up vindu åpne som viser de forskjellige USB-portene som er gjenkjent av nettleseren.
Du kan deretter koble til din ESP-32, og en ny port vil bli vist (i dette tilfellet er det ttyACM0-porten). Du må deretter velge den og klikke på "koble til".
![](assets/flasher-port-serial.webp)

Programvaren vil da bli lastet ned til din ESP32 på noen få sekunder.

![](assets/NM2-sucessfully-installed.webp)

## Steg 3: NerdMiner-konfigurasjon

Konfigurasjonen av din NerdMiner vil bli gjort via en smarttelefon eller en datamaskin.
Aktiver WiFi og koble til det lokale NerdMinerAP-nettverket. Hvis du bruker en smarttelefon, vil konfigurasjonsportalen åpne seg automatisk. Ellers, skriv inn adressen 192.168.4.1 i en nettleser.
Deretter velger du "Konfigurer WiFi".

Du kan nå konfigurere din NerdMiner.
Først, start med å koble til ditt WiFi-nettverk ved å velge nettverksnavnet ditt og skrive inn det tilhørende passordet.

Deretter kan du velge miningpoolen du ønsker å delta i. Det er vanlig i bitcoin mining-industrien å samle databehandlingskraft for å øke sjansene for å finne en blokk i bytte mot å dele belønningen proporsjonalt med den tilbudte hashraten.
For NerdMiners, kan du velge å koble til en av disse poolene:

| Pool URL          | Port  | URL                        | Status                                   |
| ----------------- | ----- | -------------------------- | ---------------------------------------- |
| public-pool.io    | 21496 | https://web.public-pool.io | Standard Solo og åpen kildekode miningpool |
| pool.nerdminer.io | 3333  | https://nerdminer.io       | Vedlikeholdt av CHMEX                    |
| pool.vkbit.com    | 3333  | https://vkbit.com/         | Vedlikeholdt av djerfy                   |

Når du har valgt din pool, må du skrive inn din bitcoin-adresse for å motta belønningen i tilfelle (unntaksvis) en blokk blir funnet.

Velg også din tidssone slik at NerdMiner kan vise tiden korrekt.
Du kan nå klikke på "lagre".

![](assets/wifi-configuration.webp)

Gratulerer, du er nå en del av Bitcoin mining-nettverket!

## NerdMiner-drift

NerdMinerv2-programvaren har 3 forskjellige skjermer, som du kan få tilgang til ved å klikke på den øverste knappen på høyre side av skjermen din:

- Hovedskjermen gir tilgang til statistikken for din NerdMiner.
- Den andre skjermen gir tilgang til tiden, din hashrate, prisen på bitcoin, og blokkhøyden.
- Den tredje skjermen gir tilgang til statistikk om det globale bitcoin mining-nettverket.
  ![](assets/NM2-screens.webp)

Hvis du ønsker å starte din NerdMiner på nytt, for eksempel for å endre WiFi-nettverket, må du trykke på den øverste knappen i 5 sekunder.

Å trykke på den nederste knappen én gang vil slå av din NerdMiner. Å klikke to ganger vil rotere skjermorienteringen.

### Forberedende steg for Linux-brukere

Her er stegene for at Chrome skal oppdage din serielle port på Linux.

1. Identifiser den tilknyttede porten:

- Koble din ESP-32 til datamaskinen din.
- Åpne en terminal.
- Skriv inn følgende kommando for å liste alle porter:
  - `dmesg | grep tty`
  - eller `ls /dev/tty*`
- For å være sikker på porten, kan du fortsette med eliminering ved å gjenta kommandoen uten at ESP-32 er tilkoblet.

2. Endre tillatelsen for den tilknyttede porten:
- Som standard kan tilgang til serieporter kreve rotrettigheter, så vi vil gjøre dem tilgjengelige ved å legge brukeren din til `dialout`-gruppen. - `sudo usermod -a -G dialout DITT_BRUKERNAVN`, erstatt `DITT_BRUKERNAVN` med ditt brukernavn.
  - logg deretter ut og inn igjen som denne brukeren, eller start systemet på nytt for å sikre at gruppeendringene trer i kraft.

Nå som din ESP-32 er gjenkjent av systemet ditt, kan du gå tilbake til [første steg](#etape-1-preparation-du-webflasher) for programvareinstallasjon.

## Konklusjon

Og der har du det! Din NerdMiner_v2 er nå konfigurert og klar til bruk.

Lykke til med mining og måtte lykken være på din side!

### Estimere sannsynligheten for å vinne

La oss ha det litt gøy med å estimere sannsynligheten for å vinne en blokkbelønning. Denne estimasjonen vil være grov og søker bare å få en størrelsesorden på sannsynligheten.
Bassenget som en NerdMiner kan koble til er kun "solo mining pool", noe som betyr at bassenget ikke mutualiserer hashraten til alle tilkoblede gruvearbeidere, men simpelthen fungerer som en koordinator.
La oss nå anta at vår NerdMiner har en hashrate på omtrent 45kH/s.

Med tanke på at den totale hashraten er omtrent 450 EH/s (eller 4.5 x 10^20 hasher per sekund), kan vi vurdere at sannsynligheten for å finne neste blokk er 1 i 100 millioner milliarder, noe som er veldig veldig veldig usannsynlig å skje. Så i tillegg til å være et pedagogisk verktøy og et objekt av nysgjerrighet, kan en NerdMiner tjene som et lodd i bitcoin-mining til en marginal elektrisk kostnad på 0,5 W--selv om vi nettopp har sett at sannsynligheten for å vinne er latterlig lav. Men hvorfor ikke utfordre lykken?

### Tilleggsinformasjon

Her er noen lenker hvis du vil lese mer om emnet:

- [NerdMiner_v2 prosjektside](http://github.com/BitMaker-hub/NerdMiner_v2)
- [Komplett dokumentasjon av NerdMiners](https://docs.bitwater.ch/nerd-miner-v2/)