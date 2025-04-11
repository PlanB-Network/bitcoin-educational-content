---
name: Watch Tower
description: Forståelse og bruk av et vakttårn
---

## Hvordan fungerer vakttårn?

En essensiell del av Lightning Network-økosystemet, vakttårn gir en ekstra grad av beskyttelse til brukernes lynkanaler. Hovedansvaret er å holde et øye med kanalenes helse og gripe inn hvis en av partene i kanalen prøver å svindle den andre.

Så hvordan kan et vakttårn avgjøre om en kanal har blitt kompromittert? Vakttårnet mottar informasjonen det trenger fra klienten, en av partene i kanalen, for å kunne identifisere og reagere på eventuelle brudd korrekt. Informasjonen inkluderer ofte de mest nylige transaksjonsdetaljene, den nåværende tilstanden til kanalen, og informasjonen som kreves for å opprette straffetransaksjoner. Før klienten sender dataene til vakttårnet, kan den kryptere dem for å beskytte personvern og hemmelighold. Dette forhindrer vakttårnet i å dekryptere de krypterte dataene med mindre et brudd faktisk har funnet sted, selv om det mottar dataene. Dette krypteringssystemet beskytter klientens personvern og stopper vakttårnet fra å få tilgang til private data uten tillatelse.

## Hvordan sette opp ditt eget Eye of Satoshi og begynne å bidra

Eye of Satoshi ([RUST-TEOS](https://github.com/talaia-labs/rust-teos?ref=blog.summerofbitcoin.org)) er et ikke-forvaringsbasert Lightning vakttårn i samsvar med [BOLT 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org). Det har to hovedkomponenter:

1. teos: inkluderer et CLI og server-siden kjernefunksjonaliteten til tårnet. To binærfiler—teosd og teos-cli—vil bli produsert når denne pakken bygges.

2. teos-common: Inkluderer delt server-side og klient-side funksjonalitet (nyttig for å opprette en klient).

For å kjøre tårnet vellykket, vil du trenge bitcoind kjørende før du kjører tårnet med teosd-kommandoen. Før du kjører begge disse kommandoene, må du sette opp din bitcoin.conf-fil. Her er stegene for hvordan du gjør dette:-

1. Installer bitcoin core fra kilden eller last den ned. Etter nedlasting, plasser bitcoin.conf-filen i Bitcoin core brukerkatalogen. Sjekk denne lenken for mer informasjon angående hvor du skal plassere filen ettersom det avhenger av operativsystemet du bruker.

2. Etter å ha identifisert hvor filen trenger å bli opprettet, legg til disse alternativene:-

'''
#RPC
server=1
rpcuser=<ditt-brukernavn>
rpcpassword=<ditt-passord>

#chain
regtest=1
'''

- server: For RPC-forespørsler
- rpcuser og rpcpassword: RPC-klienter kan autentisere med serveren
- regtest: Ikke nødvendig, men nyttig hvis du planlegger for utvikling.

rpcuser og rpcpassword må velges av deg. De må skrives uten anførselstegn. F.eks:-

'''
rpcuser=aniketh
rpcpassword=sterktpassord
'''

Nå, hvis du kjører bitcoind, bør det starte å kjøre noden.

1. For tårndelen, først må du installere teos fra kilden. Følg instruksjonene gitt i denne lenken.

2. Etter å ha installert teos på systemet ditt og kjørt testene, kan du fortsette med det siste steget som er å sette opp teos.toml-filen i teos brukerkatalogen. Filen må plasseres i en mappe kalt .teos (husk punktumet) under hjemmemappen din. Det vil si, for eksempel, /home/<ditt-brukernavn>/.teos for Linux. Når du har funnet stedet, opprett en teos.toml-fil og sett disse alternativene tilsvarende til tingene vi har endret på bitcoind.
#bitcoindbtc_network = "regtest"
btc_rpc_bruker = <din-bruker>
btc_rpc_passord = <ditt-passord>
'''

Merk at her må brukernavnet og passordet skrives i anførselstegn, det vil si, for samme eksempel som før:

'''
btc_rpc_bruker = "aniketh"
btc_rpc_passord = "sterktpassord"
'''

Når du har gjort det, bør du være klar til å kjøre tårnet. Siden vi kjører på regtest, er det sjanser for at det ikke vil være noen blokker utvunnet i vårt bitcoin testnettverk første gang tårnet kobler seg til det (hvis det er, er noe definitivt galt). Tårnet bygger en intern cache av de siste 100 blokkene fra bitcoind, så ved første kjøring kan vi få følgende feilmelding:

> ERROR [teosd] Ikke nok blokker for å starte tårnet (kreves: 100). Utvinn minst 100 flere

Siden vi kjører på regtest, kan vi utvinne blokker ved å gi en RPC-kommando, uten behov for å vente på den 10-minutters median tiden som vi vanligvis ser i andre nettverk (som mainnet eller testnet). Sjekk bitcoin-cli hjelp og se etter hvordan du kan utvinne blokker. Hvis du trenger litt hjelp, kan du gå gjennom denne artikkelen.

![bilde](assets/2.webp)

Det var det, du har vellykket kjørt tårnet. Gratulerer. 🎉