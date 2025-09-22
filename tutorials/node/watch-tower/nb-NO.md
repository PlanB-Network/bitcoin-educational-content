---
name: Lightning Watchtower
description: Forstå og bruke en Watchtower på Lightning-noden din
---
![cover](assets/cover.webp)



## Hvordan fungerer Vakttårn?



_Watchtowers_ er en viktig del av Lightning Network-økosystemet og gir et ekstra beskyttelsesnivå for brukernes Lightning-kanaler. Hovedoppgaven deres er å overvåke kanalstatusen og gripe inn hvis den ene siden av kanalen forsøker å svindle den andre.



Hvordan kan en Watchtower avgjøre om en kanal har blitt kompromittert? Den mottar fra kunden (en av partene i kanalen) den informasjonen som er nødvendig for å identifisere og håndtere et eventuelt brudd. Denne informasjonen inkluderer detaljer om den siste transaksjonen, kanalens nåværende status og Elements som kreves for å opprette straffetransaksjoner. Før disse dataene overføres til Watchtower, kan kunden kryptere dem for å bevare konfidensialiteten. Så selv om Watchtower mottar dataene, vil de ikke kunne dekryptere dem før det faktisk har skjedd et brudd. Denne krypteringsmekanismen beskytter kundens personvern og hindrer Watchtower i å få uautorisert tilgang til sensitiv informasjon.



I denne veiledningen skal vi se på tre måter å bruke en **Watchtower** på:




- først den klassiske råmetoden via LND,
- så en annen tilnærming med Eye of Satoshi,
- og til slutt, den forenklede konfigurasjonen av en Watchtower på Lightning-noden din hos Umbrel.



## 1 - Konfigurering av en Watchtower eller en klient via LND



*Denne veiledningen er hentet fra [den offisielle LND-dokumentasjonen] (https://github.com/lightningnetwork/LND/blob/master/docs/Watchtower.md). Noen endringer kan ha blitt gjort i forhold til den opprinnelige versjonen



Siden v0.7.0 har `LND` støttet kjøring av en privat altruistisk Watchtower som et fullt integrert delsystem i `LND`. Vakttårnene gir en ekstra forsvarslinje mot ondsinnede eller utilsiktede innbruddsscenarioer når kundenoden er frakoblet eller ikke er i stand til å svare på tidspunktet for innbruddet, noe som gir en økt grad av sikkerhet for kanalmidler.



I motsetning til et _belønningsvakttårn_, som krever en andel av kanalens midler som takk for tjenesten, returnerer et _altruistisk vakttårn_ alle offerets midler (minus On-Chain-avgifter) uten å kreve provisjon. Belønningsvakttårn vil bli aktivert i en senere versjon; de er fortsatt i test- og forbedringsfasen.



I tillegg kan `LND` nå konfigureres til å fungere som en _vakttårnklient_, som lagrer krypterte utbedringstransaksjoner (såkalte "rettferdighetstransaksjoner") fra andre altruistiske vakttårn. Watchtower lagrer krypterte blobber av fast størrelse og kan bare dekryptere og publisere rettferdighetstransaksjonen etter at den krenkende parten har kringkastet en tilbakekalt Commitment-tilstand. Kommunikasjonen mellom kunde og Watchtower krypteres og autentiseres ved hjelp av kortvarige nøkkelpar, noe som begrenser Watchtowers mulighet til å spore kundene sine via langsiktig legitimasjon.



Merk at vi har valgt å implementere et begrenset sett med funksjoner som allerede gir betydelig sikkerhet for `LND`-brukere i denne utgivelsen. Mange andre Watchtower-relaterte funksjoner er enten nær ferdigstillelse eller langt fremskredne; vi vil fortsette å levere dem etter hvert som vi tester dem, og så snart de anses som trygge.



merk: Foreløpig lagrer vakttårnene bare `to_local` og `to_remote`-utdataene fra tilbakekalte forpliktelser. Lagring av HTLC-utdata vil bli tatt i bruk i en fremtidig versjon, ettersom protokollen kan utvides til å inkludere ytterligere signaturdata i krypterte blobs



### Konfigurere en Watchtower



For å sette opp en Watchtower må kommandolinjebrukere kompilere den valgfrie underserveren `watchtowerrpc`, som gjør det mulig å samhandle med Watchtower via gRPC eller `lncli`. Publiserte binære filer inkluderer underserveren `watchtowerrpc` som standard.



Minimumskonfigurasjonen for å aktivere Watchtower er `Watchtower.active=1`.



Du kan hente informasjon om Watchtower-konfigurasjonen med `lncli tower info` :



```shell
$  lncli tower info
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"listeners": [
"[::]:9911"
],
"uris": [
],
}
```



Hele settet med Watchtower-konfigurasjonsalternativer er tilgjengelig via `LND -h` :



```shell
$  lnd -h
...
watchtower:
--watchtower.active                                     If the watchtower should be active or not
--watchtower.towerdir=                                  Directory of the watchtower.db (default: $HOME/.lnd/data/watchtower)
--watchtower.listen=                                    Add interfaces/ports to listen for peer connections
--watchtower.externalip=                                Add interfaces/ports where the watchtower can accept peer connections
--watchtower.readtimeout=                               Duration the watchtower server will wait for messages to be received before hanging up on client connections
--watchtower.writetimeout=                              Duration the watchtower server will wait for messages to be written before hanging up on client connections
...
```



#### Grensesnitt for lytting



Som standard lytter Watchtower på `:9911`, som tilsvarer port `9911` på alle tilgjengelige grensesnitt. Brukere kan definere sine egne lyttegrensesnitt via alternativet `--Watchtower.listen=`. Du kan sjekke konfigurasjonen din i `"listeners"-feltet i `lncli tower info`. Hvis du har problemer med å koble deg til Watchtower, må du kontrollere at `<port>` er åpen, eller at proxyen er riktig konfigurert til en aktiv Interface.



#### Eksterne IP-adresser



Brukere kan også spesifisere Watchtowers eksterne IP Address(er) med `Watchtower.externalip=`, som eksponerer Watchtowers fulle URI (pubkey@host:port) via RPC eller `lncli tower info` :



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911"
]
```



Watchtower URI-er kan kommuniseres til kunder for tilkobling og bruk med følgende kommando:



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Hvis Watchtower-kunder trenger ekstern tilgang, må du sørge for å :




- Åpne port 9911 (eller en port som er definert via `Watchtower.listen`).
- Bruk en proxy til å omdirigere trafikk fra en åpen port til Watchtowers lyttende Address.



#### Tor skjulte tjenester



Vakttårn støtter skjulte Tor-tjenester og kan automatisk generate en ved oppstart med følgende alternativer:



```shell
$  lnd --tor.active --tor.v3 --watchtower.active
```



Address vises deretter i feltet `"uris"` under en `lncli tower info`-spørring:



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@bn2kxggzjysvsd5o3uqe4h7655u7v2ydhxzy7ea2fx26duaixlwuguad.onion:9911"
]
```



merk: Den offentlige nøkkelen til Watchtower er forskjellig fra den offentlige nøkkelen til `LND`-noden. Inntil videre fungerer den som en "Soft-hviteliste", ettersom kundene må kjenne til Watchtowers offentlige nøkkel for å bruke den som en sikkerhetskopi, i påvente av mer avanserte mekanismer for hvitelisting. Vi anbefaler at du IKKE avslører denne offentlige nøkkelen åpent, med mindre du er forberedt på å eksponere din Watchtower for hele Internett



#### Watchtower databasekatalog



Watchtower-databasen kan flyttes ved hjelp av alternativet `Watchtower.towerdir=`. Merk at suffikset `/Bitcoin/Mainnet/Watchtower.db` vil bli lagt til den valgte stien for å isolere databasene etter streng. Hvis du setter `Watchtower.towerdir=/path/to/towerdir`, vil du dermed få en database på `/path/to/towerdir/Bitcoin/Mainnet/Watchtower.db`.



Under Linux ligger for eksempel Watchtowers standarddatabase på :


`/home/$USER/.LND/data/Watchtower/Bitcoin/Mainnet/Watchtower.db`



### Konfigurere en Watchtower-klient



For å konfigurere en Watchtower-klient trenger du to elementer:





- Aktiver Watchtower-klienten med alternativet `--wtclient.active`.



```shell
$  lnd --wtclient.active
```





- URI-en til en aktiv Watchtower.



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Du kan konfigurere flere vakttårn på denne måten.



#### Gebyrsatser for juridiske transaksjoner



Brukere kan eventuelt angi gebyrsatsen for rettferdige transaksjoner via alternativet `wtclient.sweep-fee-rate`, som aksepterer verdier i sat/byte. Standardverdien er 10 sat/byte, men det er mulig å sikte mot høyere satser for å oppnå høyere prioritet under belastningstopper. Endring av `sweep-fee-rate` gjelder for alle nye oppdateringer etter omstart av daemon.



#### Tilsyn



Med kommandoen `lncli wtclient` kan brukere nå samhandle direkte med Watchtower-klienten for å innhente eller endre informasjon om alle registrerte vakttårn.



Med `lncli wtclient tower` kan du for eksempel finne ut hvor mange økter som for øyeblikket forhandles med Watchtower som er lagt til ovenfor, og finne ut om den brukes til sikkerhetskopiering, takket være feltet `active_session_candidate`.



```shell
$  lncli wtclient tower 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": []
}
```



Hvis du vil ha informasjon om Watchtower-økter, bruker du alternativet `--include_sessions`.



```shell
$  lncli wtclient tower --include_sessions 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": [
{
"num_backups": 0,
"num_pending_backups": 0,
"max_backups": 1024,
"sweep_sat_per_vbyte": 10
}
]
}
```



Alle konfigurasjonsalternativer for Watchtower-klienten er tilgjengelige via `lncli wtclient -h` :



```shell
$  lncli wtclient -h
NAME:
lncli wtclient - Interact with the watchtower client.

USAGE:
lncli wtclient command [command options] [arguments...]

COMMANDS:
add     Register a watchtower to use for future sessions/backups.
remove  Remove a watchtower to prevent its use for future sessions/backups.
towers  Display information about all registered watchtowers.
tower   Display information about a specific registered watchtower.
stats   Display the session stats of the watchtower client.
policy  Display the active watchtower client policy configuration.

OPTIONS:
--help, -h  show help
```




## 2 - Installere din egen Eye of Satoshi



*Denne veiledningen er delvis hentet fra en artikkel på [Summer of Bitcoin Blog] (https://blog.summerofbitcoin.org/). Det er gjort endringer i den opprinnelige versjonen*



The Eye of Satoshi ([Rust-TEOS](https://github.com/talaia-labs/Rust-teos)) er en ikke-deponert Watchtower Lightning, i samsvar med [Bolt 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org). Det består av to hovedkomponenter:





- teos**: inkluderer en kommandolinje-Interface (CLI) og de viktigste serverfunksjonene i Watchtower. To binære filer - **teosd** og **teos-CLI** - blir produsert når denne _krisen_ kompileres.





- teos-common**: inkluderer delt funksjonalitet på server- og klientsiden (nyttig for å opprette en klient).



For å kjøre Watchtower på riktig måte må du kjøre **bitcoind** før du starter Watchtower med kommandoen **teosd**. Før du kjører disse to kommandoene, må du konfigurere filen **Bitcoin.conf**. Slik gjør du det:





- Installer Bitcoin core fra kildekode eller last den ned. Etter nedlasting plasserer du filen **Bitcoin.conf** i brukerkatalogen til Bitcoin core. Se denne lenken for mer informasjon om hvor filen skal plasseres, ettersom dette avhenger av operativsystemet som brukes.





- Når plasseringen er identifisert, legger du til følgende alternativer:



```shell
# RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

# chaîne
regtest=1
```





- server**: for RPC-forespørsler





- rpcuser** og **rpcpassword**: autentiserer RPC-klienter overfor serveren





- regtest**: ikke påkrevd, men nyttig hvis du planlegger utvikling.



Verdiene for **rpcuser** og **rpcpassword** velger du selv. De må skrives uten anførselstegn. For eksempel



```shell
rpcuser=aniketh
rpcpassword=strongpassword
```



Hvis du nå kjører **bitcoind**, skal noden starte.





- For Watchtower-delen må du først installere **teos** fra kildekode. Følg instruksjonene som er gitt i denne lenken.





- Når du har installert **teos** på systemet ditt og kjørt testene, kan du gå videre til det siste trinnet: å sette opp **teos.toml**-filen i teos-brukerkatalogen. Filen skal plasseres i en mappe med navnet **.teos** (legg merke til prikken) under hjemmekatalogen din. For eksempel **/home//.teos** under Linux. Når du har funnet plasseringen, oppretter du en **teos.toml**-fil og angir disse alternativene i tråd med endringene som ble gjort på **bitcoind** :



```shell
# bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>
```



Merk at her må brukernavn og passord skrives **innenfor anførselstegn**. Ved å bruke det forrige eksempelet :



```shell
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"
```



Når dette er gjort, bør du være klar til å starte Watchtower. Siden vi kjører på **regtest**, er det sannsynlig at ingen blokker ble utvunnet på vårt Bitcoin-testnettverk da Watchtower først ble koblet til (hvis de ble det, er det noe galt). Watchtower bygger en intern cache av de siste 100 blokkene i **bitcoind**; så ved første oppstart kan du få følgende feil:



```shell
ERROR [teosd] Not enough blocks to start the tower (required: 100). Mine at least 100 more
```



Siden vi bruker **regtest**, kan vi Miner-blokker ved å utstede en RPC-kommando, uten å måtte vente på medianforsinkelsen på 10 minutter som man ser i andre nettverk (for eksempel Mainnet eller Testnet). Se **bitcoin-cli**-hjelpen for mer informasjon om hvordan du Miner-blokkerer.



![Image](assets/fr/01.webp)



Det var alt: Du har kjørt Watchtower. Gratulerer med det. 🎉




## 3 - Konfigurere en Watchtower på Umbrel



På Umbrel er det svært enkelt å koble til en Watchtower for å beskytte Lightning-noden din, ettersom alt gjøres via den grafiske Interface. Etter at du har koblet deg til noden din, åpner du programmet "**Lightning Node**".



![Image](assets/fr/02.webp)



Klikk på de tre små prikkene øverst til høyre på Interface, og velg deretter "**Avanserte innstillinger**".



![Image](assets/fr/03.webp)



I menyen "**Watchtower**" er to alternativer tilgjengelige:





- Watchtower-tjeneste**: Med dette alternativet kan du drive en Watchtower, dvs. en tjeneste som overvåker kanalene til andre noder for å oppdage eventuelle svindelforsøk. I tilfelle brudd publiserer din Watchtower en transaksjon på Blockchain, slik at brukerne kan få tilbake de låste midlene sine. Når den er aktivert, vises URI-en til din Watchtower og kan kommuniseres til andre noder, slik at de kan legge den til i Watchtower-klienten sin;





- Watchtower Client**: Med dette alternativet kan du koble deg til eksterne vakttårn for å beskytte dine egne kanaler. Når den er aktivert, kan du legge til Watchtower-tjenester som noden din sender nødvendig informasjon om kanalene sine til. Disse vakttårnene vil deretter overvåke statusen deres og gripe inn i tilfelle forsøk på svindel.



Det viktigste for deg er selvfølgelig å aktivere *Watchtower Client* for å beskytte noden din, men jeg anbefaler også at du aktiverer *Watchtower Service* for å bidra til sikkerheten til andre brukere.



![Image](assets/fr/04.webp)



Klikk deretter på Green-knappen "**Lagre og start noden på nytt**". LND vil starte på nytt.



I den samme menyen finner du også URI-en til Watchtower-tjenesten din, hvis du har aktivert den. Du kan også legge til URI-en til en ekstern Watchtower for å beskytte kanalene dine. Klikk på "**ADD**" for å bekrefte.



![Image](assets/fr/05.webp)



Det finnes flere Watchtowers tilgjengelig på nettet. For eksempel tilbyr [LN+ og Voltage en altruistisk Watchtower] (https://lightningnetwork.plus/Watchtower) som du kan koble deg til:



```
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



![Image](assets/fr/06.webp)



Et annet alternativ er å Exchange din Watchtower URI med andre bitcoinere, slik at alle beskytter hverandres node.



Jeg anbefaler også at du setter opp flere vakttårn for å redusere risikoen i tilfelle ett av dem skulle bli utilgjengelig.



Til slutt kan du justere parameteren "**Watchtower Client Sweep Fee Rate**". Denne definerer den maksimale gebyrsatsen du er villig til å betale for at en Watchtower-sendingsstraffetransaksjon skal inkluderes i en blokk. Sørg for at du angir en tilstrekkelig høy verdi, tilpasset beløpene som er låst i kanalene dine.