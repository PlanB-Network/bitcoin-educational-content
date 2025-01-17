---
term: TRANSAKSJONSSTANDARD

---
En Bitcoin-transaksjon som, i tillegg til å følge konsensusreglene, også faller innenfor standardiseringsreglene som er satt som standard på Bitcoin Core-noder. Disse standardiseringsreglene innføres individuelt av hver Bitcoin-node, i tillegg til konsensusreglene, for å definere strukturen til ubekreftede transaksjoner som den aksepterer i sin mempool og sender til sine likemenn.

Disse reglene konfigureres og utføres lokalt av hver enkelt node, og kan variere fra node til node. De gjelder utelukkende for ubekreftede transaksjoner. En node vil derfor bare godta en transaksjon som den anser som ikke-standard, hvis den allerede er inkludert i en gyldig blokk.

Det bemerkes at de fleste noder forlater standardkonfigurasjonene som er etablert i Bitcoin Core, og dermed skaper en ensartethet av standardiseringsregler i hele nettverket. En transaksjon som ikke respekterer disse standardiseringsreglene, selv om den er i samsvar med konsensusreglene, vil ha vanskeligheter med å forplante seg gjennom nettverket. Den kan likevel bli inkludert i en gyldig blokk hvis den når frem til en miner. I praksis blir disse transaksjonene, som er kvalifisert som ikke-standardiserte, ofte overført direkte til en utvinner via eksterne midler til Bitcoin peer-to-peer-nettverket. Dette er ofte den eneste måten å bekrefte en slik transaksjon på. For eksempel er en transaksjon som ikke tildeler noen avgifter både gyldig i henhold til konsensusreglene og ikke-standard, fordi standardpolicyen til Bitcoin Core for parameteren `minRelayTxFee` er `0,00001` (i BTC/kB).