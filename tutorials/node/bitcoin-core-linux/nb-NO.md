---
name: Bitcoin Core Node (linux)
description: Kjør din egen node med Bitcoin Core
---

![cover](assets/cover.webp)

# Kjør din egen node med Bitcoin Core

Introduksjon til Bitcoin og konseptet med en node, supplert med en omfattende installasjonsguide på Linux.

En av de mest spennende forslagene med Bitcoin er muligheten til å kjøre programmet selv, og dermed delta på et detaljnivå i nettverket og verifiseringen av den offentlige transaksjonsloggen.

Bitcoin, et åpen kildekode-prosjekt, har vært offentlig distribuert og tilgjengelig gratis siden 2009. Nesten 15 år etter sin begynnelse, er Bitcoin nå et robust og ustoppelig digitalt pengeoverføringsnettverk, som nyter godt av en kraftig organisk nettverkseffekt. For deres innsats og visjon, fortjener Satoshi Nakamoto vår takknemlighet. For øvrig, vi er vert for Bitcoin-hvitboken her på Agora 256 (merk: også på universitetet).

## Bli din egen bank

Å kjøre din egen node har blitt essensielt for tilhengere av Bitcoin-aksiomet. Uten å spørre noen om tillatelse, er det mulig å laste ned blokkjeden fra begynnelsen og dermed verifisere alle transaksjoner fra A til Å i henhold til Bitcoin-protokollen.

Programmet inkluderer også sin egen lommebok. Dermed har vi kontroll over transaksjonene vi sender til resten av nettverket, uten noen mellommann eller tredjepart. Du er din egen bank.

Resten av denne artikkelen er derfor en guide til å installere Bitcoin Core — den mest brukte Bitcoin-programvareversjonen — spesifikt på Debian-kompatible Linux-distribusjoner som Ubuntu og Pop!_OS. Følg denne guiden for å ta et skritt nærmere din individuelle suverenitet.

## Bitcoin Core Installasjonsguide for Debian/Ubuntu

> Forutsetninger
>
> - Minimum 6GB med datalagring (beskåret node) — 1TB med datalagring (full node)
> - Beregn minst 24 timer for gjennomføringen av den første blokknedlastingen (IBD). Denne operasjonen er obligatorisk selv for en beskåret node.
> - Beregn ~600GB med båndbredde for IBD, selv for en beskåret node.

> 💡 Følgende kommandoer er forhåndsdefinert for Bitcoin Core versjon 24.1.

## Nedlasting og Verifisering av Filer

1. Last ned bitcoin-24.1-x86_64-linux-gnu.tar.gz, samt SHA256SUMS og SHA256SUMS.asc filene. (https://bitcoincore.org/bin/bitcoin-core-24.1/bitcoin-24.1-x86_64-linux-gnu.tar.gz)

2. Åpne en terminal i mappen der de nedlastede filene befinner seg. F.eks., cd ~/Downloads/.
3. Verifiser at sjekksummen av versjonsfilen er oppført i sjekksumfilen ved å bruke kommandoen sha256sum --ignore-missing --check SHA256SUMS.
4. Utdata fra denne kommandoen skal inkludere navnet på den nedlastede versjonsfilen etterfulgt av "OK". Eksempel: bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK.

5. Installer git ved å bruke kommandoen sudo install git. Deretter, klone repositoriet som inneholder PGP-nøklene til Bitcoin Core-signerere ved å bruke kommandoen git clone https://github.com/bitcoin-core/guix.sigs.
6. Importer PGP-nøklene til alle signererne ved å bruke kommandoen gpg --import guix.sigs/builder-keys/\*
7. Verifiser at sjekksumfilen er signert med PGP-nøklene til signererne ved å bruke kommandoen gpg --verify SHA256SUMS.asc.
Hver signatur vil returnere en linje som starter med: gpg: Good signature og en annen linje som slutter med Primary key fingerprint: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320 (eksempel på Pieter Wuille sin PGP-nøkkelfingeravtrykk).
> 💡 Det er ikke nødvendig at alle signeringsnøkler returnerer et "OK". Faktisk kan det være nok med bare én. Det er opp til brukeren å bestemme sin egen valideringsterskel for PGP-verifisering.
>
> Du kan ignorere meldingene WARNING: This key is not certified with a trusted signature!

> Det er ingen indikasjon på at signaturen tilhører eieren.

## Installasjon av Bitcoin Core grafisk grensesnitt

1. I terminalen, fortsatt i mappen der Bitcoin Core-versjonsfilen ligger, bruk kommandoen tar xzf bitcoin-24.1-x86_64-linux-gnu.tar.gz for å pakke ut filene som er inneholdt i arkivet.

2. Installer de tidligere utpakkede filene ved å bruke kommandoen sudo install -m 0755 -o root -g root -t /usr/local/bin bitcoin-24.1/bin//\*

3. Installer nødvendige avhengigheter ved å bruke kommandoen sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev

4. Start bitcoin-qt (Bitcoin Core grafisk grensesnitt) ved å bruke kommandoen bitcoin-qt.

5. For å velge en beskåret node, sjekk Limit blockchain storage og konfigurer datagrensen som skal lagres:

![welcome](assets/1.webp)

## Konklusjon av Del 1: Installasjonsguide

Når Bitcoin Core er installert, anbefales det å holde det kjørende så mye som mulig for å bidra til Bitcoin-nettverket ved å verifisere transaksjoner og overføre nye blokker til andre noder.

Men, å kjøre og synkronisere noden din intermittently, selv bare for å validere mottatte og sendte transaksjoner, forblir en god praksis.

![Creation wallet](assets/2.webp)

# Konfigurering av Tor for en Bitcoin Core Node

> 💡 Denne guiden er designet for Bitcoin Core 24.0.1 på Ubuntu/Debian-kompatible Linux-distribusjoner.

## Installasjon og konfigurering av Tor for Bitcoin Core

Først må vi installere Tor-tjenesten (The Onion Router), et nettverk brukt for anonym kommunikasjon, som vil tillate oss å anonymisere våre interaksjoner med Bitcoin-nettverket. For en introduksjon til verktøy for beskyttelse av online personvern, inkludert Tor, se vår artikkel om dette emnet.

For å installere Tor, åpne en terminal og skriv inn sudo apt -y install tor. Når installasjonen er fullført, vil tjenesten normalt bli automatisk lansert i bakgrunnen. Sjekk at den kjører korrekt med kommandoen sudo systemctl status tor. Svaret bør vise Active: active (exited). Trykk Ctrl+C for å avslutte denne funksjonen.

> Uansett kan du bruke følgende kommandoer i terminalen for å starte, stoppe, eller restarte Tor:

```
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```

Deretter, la oss starte Bitcoin Core grafisk grensesnitt med kommandoen bitcoin-qt. Deretter, aktiver programmets automatiserte funksjon for å rute våre tilkoblinger gjennom en Tor-proxy: Settings > Network, og derfra kan vi sjekke Connect through SOCKS5 proxy (default proxy) samt Use a separate SOCKS5 proxy to reach peers via Tor onion services.

![option](assets/3.webp)

Bitcoin Core oppdager automatisk om Tor er installert og vil, hvis så, som standard opprette utgående tilkoblinger til andre noder som også bruker Tor, i tillegg til tilkoblinger til noder som bruker IPv4/IPv6-nettverk (clearnet).
💡 For å endre visningsspråket til fransk, gå til fanen Visning i Innstillinger.
## Avansert Tor-konfigurasjon (valgfritt)

Det er mulig å konfigurere Bitcoin Core til kun å bruke Tor-nettverket for å koble til jevnaldrende, og dermed optimalisere vår anonymitet gjennom vår node. Siden det ikke finnes innebygd funksjonalitet for dette i det grafiske grensesnittet, må vi manuelt opprette en konfigurasjonsfil. Gå til Innstillinger, deretter Alternativer.

![alternativ 2](assets/4.webp)

Her, klikk på Åpne konfigurasjonsfil. Når du er i bitcoin.conf-tekstfilen, legg ganske enkelt til en linje onlynet=onion og lagre filen. Du må starte Bitcoin Core på nytt for at denne kommandoen skal tre i kraft.
Vi vil deretter konfigurere Tor-tjenesten slik at Bitcoin Core kan motta innkommende tilkoblinger via en proxy, noe som lar andre noder i nettverket bruke vår node til å laste ned blockchain-data uten å kompromittere sikkerheten til vår maskin.

I terminalen, skriv inn sudo nano /etc/tor/torrc for å få tilgang til Tor-tjenestens konfigurasjonsfil. I denne filen, se etter linjen #ControlPort 9051 og fjern # for å aktivere den. Legg nå til to nye linjer i filen: HiddenServiceDir /var/lib/tor/bitcoin-service/ og HiddenServicePort 8333 127.0.0.1:8334. For å forlate filen mens du lagrer den, trykk Ctrl+X > Y > Enter. Tilbake i terminalen, start Tor på nytt ved å skrive inn kommandoen sudo systemctl restart tor.

Med denne konfigurasjonen vil Bitcoin Core kunne etablere innkommende og utgående tilkoblinger med andre noder i nettverket kun gjennom Tor-nettverket (Onion). For å bekrefte dette, klikk på fanen Vindu, deretter Jevnaldrende.

![Noder Vindu](assets/5.webp)

## Tilleggsressurser

Til slutt, ved å bruke kun Tor-nettverket (onlynet=onion) kan du bli sårbar for et Sybil-angrep. Derfor anbefaler noen å opprettholde en multi-nettverkskonfigurasjon for å redusere denne typen risiko. Videre vil alle IPv4/IPv6-tilkoblinger bli rutet gjennom Tor-proxyen når den er konfigurert, som tidligere indikert.

Alternativt, for å forbli utelukkende på Tor-nettverket og redusere risikoen for et Sybil-angrep, kan du legge til adressen til en annen pålitelig node i din bitcoin.conf-fil ved å legge til linjen addnode=trusted_address.onion. Du kan legge til denne linjen flere ganger hvis du ønsker å koble til flere pålitelige noder.

For å se loggene fra din Bitcoin-node spesifikt relatert til dens interaksjon med Tor, legg til debug=tor i din bitcoin.conf-fil. Du vil nå ha relevant Tor-informasjon i din feilsøkingslogg, som du kan se i Informasjonsvinduet med Debug File-knappen. Det er også mulig å se disse loggene direkte i terminalen med kommandoen bitcoind -debug=tor.

> 💡 Noen interessante lenker:
>
> - Wiki-side som forklarer Tor og dets forhold til Bitcoin
> - Bitcoin Core konfigurasjonsfilgenerator av Jameson Lopp
> - Tor-konfigurasjonsguide av Jon Atack

Som alltid, hvis du har noen spørsmål, føl deg fri til å dele dem med Agora256-fellesskapet. Vi lærer sammen for å være bedre i morgen enn vi er i dag!