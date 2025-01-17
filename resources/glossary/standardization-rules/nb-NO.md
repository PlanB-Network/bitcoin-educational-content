---
term: STANDARDISERINGSREGLER

---
Standardiseringsregler vedtas individuelt av hver Bitcoin-node, i tillegg til konsensusreglene, for å definere strukturen til ubekreftede transaksjoner som den aksepterer i sin mempool og sender til sine likemenn. Disse reglene konfigureres og utføres lokalt av hver enkelt node, og kan variere fra node til node. De gjelder utelukkende for ubekreftede transaksjoner. En node vil derfor bare godta en transaksjon som den anser som ikke-standard, hvis den allerede er inkludert i en gyldig blokk.

Det bemerkes at de fleste noder forlater standardkonfigurasjonene som er etablert i Bitcoin Core, og dermed skaper en ensartethet av standardiseringsregler i hele nettverket. En transaksjon som ikke følger disse standardiseringsreglene, selv om den er i samsvar med konsensusreglene, vil ha vanskeligheter med å bli kringkastet over nettverket. Den kan likevel bli inkludert i en gyldig blokk hvis den når frem til en utvinner. I praksis blir disse transaksjonene, som kalles "ikke-standard", ofte sendt direkte til en utvinner på eksterne måter utenfor Bitcoins peer-to-peer-nettverk. Dette er ofte den eneste måten å bekrefte denne typen transaksjoner på.

For eksempel er en transaksjon som ikke tildeler noen gebyrer, både gyldig i henhold til konsensusreglene og ikke-standard fordi standardpolicyen til Bitcoin Core for parameteren `minRelayTxFee` er `0,00001` (i BTC/kB).

> begrepet "mempool-regler" brukes også noen ganger om standardiseringsreglene