---
name: Bitcoin Core (Linux)
description: Kjør din egen node med Bitcoin core på Linux
---

![cover](assets/cover.webp)


## Kjører din egen node med Bitcoin core


Introduksjon til Bitcoin og nodekonseptet, supplert med en omfattende installasjonsveiledning for Linux.


Et av de mest spennende aspektene ved Bitcoin er muligheten til å kjøre programmet selv, og dermed delta på detaljnivå i nettverket og verifiseringen av den offentlige transaksjonen Ledger.


Bitcoin har vært et åpen kildekode-prosjekt som har vært fritt tilgjengelig og offentlig distribuert siden 2009. Nesten 17 år etter oppstarten er Bitcoin nå et robust og ustoppelig digitalt monetært nettverk som drar nytte av en kraftig organisk nettverkseffekt. Satoshi Nakamoto fortjener vår takknemlighet for sin innsats og visjon. Forresten, vi er vertskap for Bitcoin whitepaper her på Agora 256 (merk: også på universitetet).


### Bli din egen bank


Å drive sin egen node har blitt essensielt for tilhengere av Bitcoin-etoset. Uten å spørre noen om lov er det mulig å laste ned Blockchain fra begynnelsen av og dermed verifisere alle transaksjoner fra A til Å i henhold til Bitcoin-protokollen.


Programmet inkluderer også sin egen Wallet. Dermed har vi kontroll over transaksjonene vi sender til resten av nettverket, uten noe mellomledd eller tredjepart. Du er din egen bank.


Resten av denne artikkelen er derfor en veiledning i hvordan du installerer Bitcoin core - den mest brukte Bitcoin-programvareversjonen - spesielt på Debian-kompatible Linux-distribusjoner som Ubuntu og Pop!OS. Følg denne veiledningen for å ta et skritt nærmere din individuelle suverenitet.


## Bitcoin core Installasjonsveiledning for Debian/Ubuntu


**Forutsetninger**


- Minimum 6 GB datalagring (pruned-node) - 1 TB datalagring (Full node)
- Forvent at *Initial Block Download* (IBD) vil ta minst 24 timer. Denne operasjonen er obligatorisk selv for en pruned-node.
- Tillat ca. 600 GB båndbredde for IBD, selv for en pruned-node.


**Merk: 💡** følgende kommandoer er forhåndsdefinert for Bitcoin core versjon 24.1.


### Nedlasting og verifisering av filer



- [Last ned] (https://bitcoincore.org/en/download/) `Bitcoin-24.1-x86_64-linux-gnu.tar.gz`, samt filene `SHA256SUMS` og `SHA256SUMS.asc` (du må selvsagt laste ned den nyeste versjonen av programvaren).



- Åpne en terminal i katalogen der de nedlastede filene befinner seg. Eksempel: `cd ~/Downloads/`.



- Kontroller at kontrollsummen for versjonsfilen er oppført i kontrollsumfilen ved hjelp av kommandoen `sha256sum --ignore-missing --check SHA256SUMS`.



- Utdataene fra denne kommandoen bør inneholde navnet på den nedlastede versjonen etterfulgt av `OK`. Example: `Bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK`.



- Installer git ved hjelp av kommandoen `sudo apt install git`. Deretter kloner du depotet som inneholder PGP-nøklene til Bitcoin core-signererne ved hjelp av kommandoen `git clone https://github.com/Bitcoin-core/guix.sigs`.



- Importer PGP-nøklene til alle underskrivere ved hjelp av kommandoen `gpg --import guix.sigs/builder-keys/*`



- Kontroller at sjekksumfilen er signert med PGP-nøklene til underskriverne ved hjelp av kommandoen `gpg --verify SHA256SUMS.asc`.



Hver gyldig signatur vil vise en linje som begynner med : `gpg: God signatur` og en annen linje som slutter med: `Primært nøkkelfingeravtrykk: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320` (eksempel på Pieter Wuille's PGP-nøkkelfingeravtrykk).


**Det er ikke nødvendig at alle signeringsnøkler returnerer et "OK". Faktisk kan bare én være nødvendig. Det er opp til brukeren å bestemme sin egen valideringsterskel for PGP-verifisering.


Du kan ignorere advarslene:



- "Denne nøkkelen er ikke sertifisert med en klarert signatur!



- "Det er ingen indikasjon på at signaturen tilhører eieren


### Installasjon av Bitcoin core grafisk Interface



- I terminalen, fortsatt i katalogen der Bitcoin core-versjonsfilen ligger, bruker du kommandoen `tar xzf Bitcoin-24.1-x86_64-linux-gnu.tar.gz` for å pakke ut filene i arkivet.



- Installer de tidligere utpakkede filene ved hjelp av kommandoen `sudo install -m 0755 -o root -g root -t /usr/local/bin Bitcoin-24.1/bin/*`



- Installer de nødvendige avhengighetene ved hjelp av kommandoen `sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev`



- Start _bitcoin-qt_ (Bitcoin core grafisk Interface) ved hjelp av kommandoen `Bitcoin-qt`.



- Hvis du vil velge en pruned-node, merker du av for _Limit Blockchain storage_ og konfigurerer datagrensen som skal lagres:


![welcome](assets/fr/02.webp)


### Konklusjon av del 1: Installasjonsveiledning


Når Bitcoin core er installert, anbefales det å holde den i gang så mye som mulig for å bidra til Bitcoin-nettverket ved å verifisere transaksjoner og sende nye blokker til andre peers.


Det er imidlertid lurt å kjøre og synkronisere noden med jevne mellomrom, selv om det bare er for å validere mottatte og sendte transaksjoner.


![Creation wallet](assets/fr/03.webp)


## Konfigurere Tor for en Bitcoin core-node


**Denne veiledningen er utviklet for Bitcoin core 24.0.1 på Ubuntu/Debian-kompatible Linux-distribusjoner.


### Installere og konfigurere Tor for Bitcoin core


Først må vi installere Tor-tjenesten (The Onion Router), et nettverk som brukes til anonym kommunikasjon, slik at vi kan anonymisere interaksjonene våre med Bitcoin-nettverket. For en introduksjon til verktøy for personvern på nettet, inkludert Tor, kan du lese artikkelen vår om dette emnet.


For å installere Tor åpner du en terminal og skriver inn `sudo apt -y install tor`. Når installasjonen er fullført, vil tjenesten normalt starte automatisk i bakgrunnen. Sjekk at den kjører som den skal med kommandoen `sudo systemctl status tor`. Svaret bør vise `Active: active (exited)`. Trykk `Ctrl+C` for å avslutte denne funksjonen.


**Du kan uansett bruke følgende kommandoer i terminalen for å starte, stoppe eller starte Tor på nytt:


```shell
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```


La oss deretter starte Bitcoin core grafisk Interface med kommandoen `Bitcoin-qt`. Aktiver deretter programvarens automatiske funksjon for å rute forbindelsene våre gjennom en Tor-proxy: _Innstillinger > Nettverk_, og derfra merker du av for _Connect through SOCKS5 proxy (default proxy)_ samt _Use a separate SOCKS5 proxy to reach peers via Tor onion services_.


![option](assets/fr/04.webp)


Bitcoin core oppdager automatisk om Tor er installert, og vil i så fall som standard opprette utgående forbindelser til andre noder som også bruker Tor, i tillegg til forbindelser til noder som bruker IPv4/IPv6-nettverk (clearnet).


**Merknad💡:** For å endre skjermspråket til fransk, går du til fanen Skjerm i Innstillinger.


### Avansert Tor-konfigurasjon (valgfritt)


Det er mulig å konfigurere Bitcoin core slik at den kun bruker Tor-nettverket til å koble seg til motparter, og dermed optimalisere anonymiteten gjennom noden vår. Siden det ikke finnes noen innebygd funksjonalitet for dette i den grafiske Interface, må vi opprette en konfigurasjonsfil manuelt. Gå til Innstillinger og deretter Alternativer.


![option 2](assets/fr/05.webp)


Her klikker du på _Åpne konfigurasjonsfil_. Når du er i tekstfilen `Bitcoin.conf`, legger du bare til en linje `onlynet=onion` og lagrer filen. Du må starte Bitcoin core på nytt for at denne kommandoen skal tre i kraft.


Deretter konfigurerer vi Tor-tjenesten slik at Bitcoin core kan motta innkommende tilkoblinger via en proxy, slik at andre noder i nettverket kan bruke noden vår til å laste ned Blockchain-data uten at det går på bekostning av sikkerheten til maskinen vår.


I terminalen skriver du inn `sudo nano /etc/tor/torrc` for å få tilgang til konfigurasjonsfilen for Tor-tjenesten. I denne filen, se etter linjen `#ControlPort 9051` og fjern `#` for å aktivere den. Legg nå til to nye linjer i filen:


```
HiddenServiceDir /var/lib/tor/bitcoin-service/
HiddenServicePort 8333 127.0.0.1:8334
```


For å avslutte filen mens du lagrer den, trykker du på `Ctrl+X > Y > Enter`. Tilbake i terminalen starter du Tor på nytt ved å skrive inn kommandoen `sudo systemctl restart tor`.


Med denne konfigurasjonen vil Bitcoin core kun kunne opprette innkommende og utgående forbindelser med andre noder i nettverket gjennom Tor-nettverket (Onion). For å bekrefte dette, klikk på fanen _Window_ og deretter på _Peers_.


![Nodes Window](assets/fr/06.webp)


### Ytterligere ressurser


Hvis du bare bruker Tor-nettverket (`onlynet=onion`), kan det gjøre deg sårbar for en Sybil Attack. Det er derfor noen anbefaler å opprettholde en konfigurasjon med flere nettverk for å redusere denne typen risiko. Videre vil alle IPv4/IPv6-tilkoblinger bli rutet gjennom Tor-proxyen når den er konfigurert, som tidligere angitt.


Alternativt, for å forbli utelukkende på Tor-nettverket og redusere risikoen for en Sybil Attack, kan du legge til Address for en annen klarert node i filen `Bitcoin.conf` ved å legge til linjen `addnode=trusted_address.onion`. Du kan legge til denne linjen flere ganger hvis du vil koble deg til flere klarerte noder.


Hvis du vil se loggene til Bitcoin-noden din spesifikt relatert til samspillet med Tor, legger du til `debug=tor` i filen `Bitcoin.conf`. Du vil nå ha relevant Tor-informasjon i feilsøkingsloggen, som du kan se i _Information_-vinduet med _Debug File_-knappen. Det er også mulig å vise disse loggene direkte i terminalen med kommandoen `bitcoind -debug=tor`.


**Tips: Her er noen interessante lenker:


- [Wiki-side som forklarer Tor og forholdet til Bitcoin] (https://en.Bitcoin.it/wiki/Tor)
- [Bitcoin core konfigurasjonsfilgenerator av Jameson Lopp](https://jlopp.github.io/Bitcoin-core-config-generator/)
- [Tor-konfigurasjonsveiledning av Jon Atack] (https://github.com/Bitcoin/Bitcoin/blob/master/doc/tor.md)


Hvis du har spørsmål, er du som alltid velkommen til å dele dem med Agora256-fellesskapet. Vi lærer sammen for å bli bedre i morgen enn vi er i dag!