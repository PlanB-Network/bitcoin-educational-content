---
name: RGB Lightning Node
description: Hvordan starter jeg en RGB-kompatibel Lightning-node med RLN?
---
![cover](assets/cover.webp)

I denne trinnvise opplæringen lærer du hvordan du setter opp en Lightning RGB-node i et Regtest-miljø. Vi ser hvordan du oppretter RGB-tokens og sirkulerer dem i kanaler.

## RLN-prosjektet

Bitfinex' RGB-team har jobbet siden 2022 for å berike RGB-økosystemet ved å utvikle en komplett teknologistack. I stedet for å sikte mot et enkelt kommersielt produkt, er innsatsen fokusert på å gjøre programvarebrikker med åpen kildekode tilgjengelig, bidra til RGB-protokollspesifikasjoner og lage implementeringsreferanser.

Blant Bitfinex' bemerkelsesverdige bidrag til RGB-økosystemet er [the *RGBlib* library] (https://github.com/RGB-Tools/rgb-lib), skrevet i Rust og tilgjengelig via bindinger i Kotlin og Python, som i stor grad forenkler utviklingen av RGB-applikasjoner ved å innkapsle komplekse validerings- og engasjementsmekanismer.

Bitfinex-teamet har også designet en RGB-mobil lommebok, kalt "[*Iris Wallet*] (https://iriswallet.com/)", tilgjengelig på Android. Denne lommeboken integrerer bruken av en RGB-proxyserver for å enkelt administrere datautveksling utenfor kjeden (*sendinger*) for *Validering på klientsiden* på RGB.

Bitfinex har også utviklet `rgb-lightning-node` (RLN) -prosjektet. Dette er en Rust-daemon basert på en gaffel av `rust-lightning` (LDK), modifisert for å ta hensyn til eksistensen av RGB-aktiva i en kanal. Når en kanal åpnes, kan tilstedeværelsen av RGB-tokens spesifiseres, og hver gang kanaltilstanden oppdateres, opprettes en tilstandsovergang som gjenspeiler fordelingen av tokens i Lightning-utgangene. Dette muliggjør :


- Åpne Lightning-kanaler i USDT, for eksempel;
- Rute disse tokens gjennom nettverket, forutsatt at rutingsstiene har tilstrekkelig likviditet;
- Utnytt Lightnings straffe- og tidslås-logikk uten endringer: RGB-overgangen forankres ganske enkelt i en ekstra utgang fra forpliktelsestransaksjonen.

RLN-koden er fortsatt på alfa-stadiet: Vi anbefaler at du bare bruker den i **regtest** eller på **testnet**.

## Påminnelse om RGB-protokoll

RGB er en protokoll som kjører på toppen av Bitcoin og emulerer smartkontraktsfunksjonalitet og forvaltning av digitale aktiva, uten å overbelaste blokkjeden som den er basert på. I motsetning til konvensjonelle smartkontrakter i kjeden (som for eksempel på Ethereum), baserer RGB seg på et "*Validering på klientsiden*"-system: mesteparten av data og statushistorikk utveksles og lagres utelukkende av de involverte deltakerne, mens Bitcoin-blokkjeden bare er vert for små kryptografiske forpliktelser (via mekanismer som *Tapret* eller *Opret*). I RGB-protokollen fungerer Bitcoin-blokkjeden derfor bare som en tidsstemplingsserver og et system for beskyttelse mot dobbeltbruk.

En RGB-kontrakt er strukturert som en evolusjonær tilstandsmaskin. Den starter med en Genesis som definerer den opprinnelige tilstanden (som for eksempel beskriver tilbudet, tickeren eller andre metadata) i henhold til et strengt typet og kompilert Schema. Deretter brukes State Transitions og, om nødvendig, State Extensions for å endre eller utvide denne tilstanden. Hver operasjon, enten det gjelder overføring av fungible aktiva (RGB20) eller opprettelse av unike aktiva (RGB21), involverer *Single-use Seals*. Disse kobler Bitcoin UTXOer til stater utenfor kjeden og forhindrer dobbeltbruk, samtidig som de sikrer konfidensialitet og skalerbarhet.

Hvis du vil lære mer om hvordan RGB-protokollen fungerer, anbefaler jeg at du tar dette omfattende opplæringskurset:

https://planb.network/courses/csv402
## RGB-kompatibel Lightning node-installasjon

For å kompilere og installere `rgb-lightning-node`-binærfilen, starter vi med å klone repositoryet og dets undermoduler, og deretter kjører vi :

```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```

![RLN](assets/fr/01.webp)


- Alternativet `--recurse-submodules` kloner også de nødvendige underenhetene (inkludert den modifiserte versjonen av `rust-lightning`);
- Alternativet `--shallow-submodules` begrenser dybden på klonen for å gjøre nedlastingen raskere, samtidig som det gir tilgang til viktige commits.

Kjør følgende kommando fra prosjektroten for å kompilere og installere den binære :

```bash
cargo install --locked --debug --path .
```

![RLN](assets/fr/02.webp)


- `--locked` sikrer at versjonen av avhengighetene respekteres;
- `--debug` er ikke obligatorisk, men kan hjelpe deg med å fokusere (du kan bruke `--release` hvis du foretrekker det);
- `--path .` forteller `cargo install` å installere fra den aktuelle katalogen.

På slutten av denne kommandoen vil en kjørbar `rgb-lightning-node` være tilgjengelig i din `$CARGO_HOME/bin/`. Sørg for at denne stien ligger i `$PATH`, slik at du kan starte kommandoen fra en hvilken som helst katalog.

## Forutsetninger

For å fungere trenger `rgb-lightning-node` daemon tilstedeværelse og konfigurasjon av :


- En `bitcoind`**-node

Hver RLN-instans må kommunisere med `bitcoind` for å kringkaste og overvåke sine transaksjoner i kjeden. Autentisering (innlogging/passord) og URL (host/port) må oppgis til daemon.


- En indekseringsenhet** (Electrum eller Esplora)

Dæmonen må kunne liste opp og utforske transaksjoner i kjeden, spesielt for å finne UTXO-en som en eiendel er forankret på. Du må spesifisere URL-adressen til Electrum-serveren eller Esplora.


- En RGB**-proxy

Proxy-serveren er en komponent (valgfri, men anbefales på det sterkeste) som forenkler utvekslingen av RGB *konsigneringer* mellom Lightning-peers. Også her må en URL-adresse angis.

ID-er og URL-er legges inn når demonen *låses opp* via API-et.

## Regtest-lansering

For enkel bruk finnes det et `regtest.sh`-skript som automatisk starter et sett med tjenester via Docker: `bitcoind`, `electrs` (indekser), `rgb-proxy-server`.

![RLN](assets/fr/03.webp)

Dette gjør at du kan starte et lokalt, isolert og forhåndskonfigurert miljø. Den oppretter og ødelegger containere og datakataloger ved hver omstart. Vi begynner med å starte :

```bash
./regtest.sh start
```

Dette skriptet vil :


- Opprett en `docker/`-katalog for å lagre ;
- Kjør `bitcoind` i regtest, samt indekseren `electrs` og `rgb-proxy-serveren` ;
- Vent til alt er klart til bruk.

![RLN](assets/fr/04.webp)

Nå skal vi starte flere RLN-noder. I separate skall kjører du for eksempel (for å starte 3 RLN-noder) :

```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```

![RLN](assets/fr/05.webp)


- Parameteren `--network regtest` indikerer bruk av regtest-konfigurasjonen;
- `--daemon-listening-port` angir hvilken REST-port Lightning-noden skal lytte etter API-anrop på (JSON);
- `--ldk-peer-listening-port` angir hvilken Lightning p2p-port det skal lyttes på;
- `dataldk0/`, `dataldk1/` er stiene til lagringskatalogene (hver node lagrer informasjonen sin separat).

Takket være API-et kan du nå utføre kommandoer på RLN-nodene dine fra nettleseren din. Spesielt er det her du kan *låse opp* daemoner. Bare åpne en nettleser på samme datamaskin som nodene dine, og skriv inn URL-adressen :

```url
https://rgb-tools.github.io/rgb-lightning-node/
```

For at en node skal kunne åpne en kanal, må den først ha bitcoins på en adresse som er generert med følgende kommando (for node nr. 1, for eksempel):

```bash
curl -X POST http://localhost:3001/address
```

Svaret vil gi deg en adresse.

![RLN](assets/fr/06.webp)

På `bitcoind` Regtest skal vi utvinne noen bitcoins. Kjør :

```bash
./regtest.sh mine 101
```

![RLN](assets/fr/07.webp)

Send pengene til nodeadressen som er generert ovenfor:

```bash
./regtest.sh sendtoaddress <address> <amount>
```

![RLN](assets/fr/08.webp)

Deretter utvinner du en blokk for å bekrefte transaksjonen:

```bash
./regtest.sh mine 1
```

![RLN](assets/fr/09.webp)

## Testnet-lansering (uten Docker)

Hvis du vil teste et mer realistisk scenario, kan du starte RLN-noder på Testnet i stedet for i Regtest, som peker mot offentlige tjenester eller tjenester du kontrollerer:

```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```

Hvis ingen konfigurasjon blir funnet, vil daemon som standard prøve å bruke :


- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-rpc`

Med innlogging :


- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `passord`

Du kan også tilpasse disse elementene via API-et `init`/`unlock`.

## Utstedelse av en RGB-token

For å utstede et token begynner vi med å lage "fargeleggbare" UTXO-er:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```

![RLN](assets/fr/10.webp)

Du kan selvfølgelig tilpasse bestillingen. For å bekrefte transaksjonen, utvinner vi en :

```bash
./regtest.sh mine 1
```

Vi kan nå opprette en RGB-ressurs. Kommandoen avhenger av hvilken type eiendel du ønsker å opprette og dens parametere. Her oppretter jeg et NIA-token (*Non Inflatable Asset*) ved navn "PBN" med en forsyning på 1000 enheter. Med `precision` kan du definere delbarheten til enhetene.

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "PBN",
"name": "Plan B Network",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```

![RLN](assets/fr/11.webp)

Svaret inneholder ID-en til den nyopprettede ressursen. Husk å notere denne identifikatoren. I mitt tilfelle er den :

```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```

![RLN](assets/fr/12.webp)

Deretter kan du overføre den videre i kjeden, eller allokere den i en Lightning-kanal. Det er akkurat det vi skal gjøre i neste avsnitt.

## Åpne en kanal og overføre en RGB-ressurs

Du må først koble noden din til en motpart i Lightning-nettverket ved hjelp av kommandoen `/connectpeer`. I mitt eksempel kontrollerer jeg begge nodene. Derfor henter jeg den offentlige nøkkelen til min andre Lightning-node med denne kommandoen:

```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```

Kommandoen returnerer den offentlige nøkkelen til min node nr. 2 :

```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```

![RLN](assets/fr/13.webp)

Deretter åpner vi kanalen ved å spesifisere den relevante ressursen (`PBN`). Med kommandoen `/openchannel` kan du definere størrelsen på kanalen i satoshis og velge om du vil inkludere RGB-aktivet. Det kommer an på hva du ønsker å lage, men i mitt tilfelle er kommandoen :

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```

Finn ut mer her:


- `peer_pubkey_and_opt_addr`: Identifikatoren til motparten vi ønsker å koble oss til (den offentlige nøkkelen vi fant tidligere);
- `kapasitet_sat`: Total kanalkapasitet i satoshis ;
- `push_msat`: Beløp i millisatoshis som overføres til motparten når kanalen åpnes (her overfører jeg 10 000 sats med en gang, slik at han kan foreta en RGB-overføring senere);
- `asset_amount`: Mengde RGB-ressurser som skal bindes til kanalen ;
- `asset_id` : Unik identifikator for RGB-aktiva som er involvert i kanalen;
- `offentlig`: Angir om kanalen skal gjøres offentlig for ruting i nettverket.

![RLN](assets/fr/14.webp)

For å bekrefte transaksjonen utvinnes 6 blokker:

```bash
./regtest.sh mine 6
```

![RLN](assets/fr/15.webp)

Lightning-kanalen er nå åpen og inneholder også 500 `PBN`-tokens på node nr. 1 sin side. Hvis node nr. 2 ønsker å motta `PBN`-tokens, må den generere en faktura. Slik gjør du det:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```

Med :


- `amt_msat`: Fakturabeløp i millisatoshis (minimum 3000 sats) ;
- `expiry_sec` : Fakturaens utløpstid i sekunder ;
- `asset_id` : Identifikator for RGB-eiendelen som er knyttet til fakturaen ;
- `aktivum_beløp`: Beløpet for RGB-eiendelen som skal overføres med denne fakturaen.

Som svar får du en RGB-faktura:

```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```

![RLN](assets/fr/16.webp)

Vi vil nå betale denne fakturaen fra den første noden, som har de nødvendige kontantene med `PBN`-tokenet:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```

![RLN](assets/fr/17.webp)

Betaling har blitt utført. Dette kan bekreftes ved å utføre kommandoen :

```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```

![RLN](assets/fr/18.webp)

Slik distribuerer du en Lightning-node som er modifisert for å transportere RGB-ressurser. Denne demonstrasjonen er basert på :


- Et regtest-miljø (via `./regtest.sh`) eller testnet ;
- En Lightning-node (`rgb-lightning-node`) basert på en `bitcoind`, en indekserer og en `rgb-proxy-server` ;
- En serie JSON REST API-er for åpning/lukking av kanaler, utstedelse av tokens, overføring av eiendeler via Lightning osv.

Takket være denne prosessen :


- Lightning Engagement-transaksjoner inkluderer en ekstra utgang (OP_RETURN eller Taproot) med forankring av en RGB-overgang;
- Overføringer gjøres på nøyaktig samme måte som tradisjonelle Lightning-betalinger, men med tillegg av et RGB-token;
- Flere RLN-noder kan kobles sammen for å dirigere og eksperimentere med betalinger på tvers av flere noder, forutsatt at det er tilstrekkelig likviditet i både bitcoins og aktivumet RGB på stien.

Hvis du fant denne opplæringen nyttig, ville jeg være veldig takknemlig hvis du setter en grønn tommel nedenfor. Del gjerne denne artikkelen på dine sosiale nettverk. Tusen takk skal du ha!

Jeg anbefaler også denne andre veiledningen, der jeg forklarer hvordan du bruker RGB CLI-verktøyet som er utviklet av LNP/BP-foreningen, til å opprette en RGB-kontrakt:

https://planb.network/tutorials/node/rgb/rgb-cli-1f8a28d4-fa99-4261-9d80-48275b496fd4